---
title: Module batch
---

<div class="section" id="batch">
<h1>batch<a class="headerlink" href="#batch" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-azure/issues">pulumi/pulumi-azure repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/issues">terraform-providers/terraform-provider-azurerm repo</a>.</div></blockquote>
<span class="target" id="module-pulumi_azure.batch"></span><dl class="class">
<dt id="pulumi_azure.batch.Account">
<em class="property">class </em><code class="descclassname">pulumi_azure.batch.</code><code class="descname">Account</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>location=None</em>, <em>name=None</em>, <em>pool_allocation_mode=None</em>, <em>resource_group_name=None</em>, <em>storage_account_id=None</em>, <em>tags=None</em>, <em>__props__=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.batch.Account" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an Azure Batch account.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Batch account. Changing this forces a new resource to be created.</li>
<li><strong>pool_allocation_mode</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the mode to use for pool allocation. Possible values are <code class="docutils literal notranslate"><span class="pre">BatchService</span></code> or <code class="docutils literal notranslate"><span class="pre">UserSubscription</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">BatchService</span></code>.</li>
<li><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the Batch account. Changing this forces a new resource to be created.</li>
<li><strong>storage_account_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the storage account to use for the Batch account. If not specified, Azure Batch will manage the storage.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/batch_account.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/batch_account.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_azure.batch.Account.account_endpoint">
<code class="descname">account_endpoint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.batch.Account.account_endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>The account endpoint used to interact with the Batch service.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.batch.Account.location">
<code class="descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.batch.Account.location" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.batch.Account.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.batch.Account.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Batch account. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.batch.Account.pool_allocation_mode">
<code class="descname">pool_allocation_mode</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.batch.Account.pool_allocation_mode" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the mode to use for pool allocation. Possible values are <code class="docutils literal notranslate"><span class="pre">BatchService</span></code> or <code class="docutils literal notranslate"><span class="pre">UserSubscription</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">BatchService</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.batch.Account.primary_access_key">
<code class="descname">primary_access_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.batch.Account.primary_access_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The Batch account primary access key.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.batch.Account.resource_group_name">
<code class="descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.batch.Account.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to create the Batch account. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.batch.Account.secondary_access_key">
<code class="descname">secondary_access_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.batch.Account.secondary_access_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The Batch account secondary access key.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.batch.Account.storage_account_id">
<code class="descname">storage_account_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.batch.Account.storage_account_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the storage account to use for the Batch account. If not specified, Azure Batch will manage the storage.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.batch.Account.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.batch.Account.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="staticmethod">
<dt id="pulumi_azure.batch.Account.get">
<em class="property">static </em><code class="descname">get</code><span class="sig-paren">(</span><em>resource_name</em>, <em>id</em>, <em>opts=None</em>, <em>account_endpoint=None</em>, <em>location=None</em>, <em>name=None</em>, <em>pool_allocation_mode=None</em>, <em>primary_access_key=None</em>, <em>resource_group_name=None</em>, <em>secondary_access_key=None</em>, <em>storage_account_id=None</em>, <em>tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.batch.Account.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Account resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.
:param str resource_name: The unique name of the resulting resource.
:param str id: The unique provider ID of the resource to lookup.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] account_endpoint: The account endpoint used to interact with the Batch service.
:param pulumi.Input[str] location: Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.
:param pulumi.Input[str] name: Specifies the name of the Batch account. Changing this forces a new resource to be created.
:param pulumi.Input[str] pool_allocation_mode: Specifies the mode to use for pool allocation. Possible values are <code class="docutils literal notranslate"><span class="pre">BatchService</span></code> or <code class="docutils literal notranslate"><span class="pre">UserSubscription</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">BatchService</span></code>.
:param pulumi.Input[str] primary_access_key: The Batch account primary access key.
:param pulumi.Input[str] resource_group_name: The name of the resource group in which to create the Batch account. Changing this forces a new resource to be created.
:param pulumi.Input[str] secondary_access_key: The Batch account secondary access key.
:param pulumi.Input[str] storage_account_id: Specifies the storage account to use for the Batch account. If not specified, Azure Batch will manage the storage.
:param pulumi.Input[dict] tags: A mapping of tags to assign to the resource.</p>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/batch_account.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/batch_account.html.markdown</a>.</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.batch.Account.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.batch.Account.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.batch.Account.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.batch.Account.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.batch.AwaitableGetAccountResult">
<em class="property">class </em><code class="descclassname">pulumi_azure.batch.</code><code class="descname">AwaitableGetAccountResult</code><span class="sig-paren">(</span><em>account_endpoint=None</em>, <em>location=None</em>, <em>name=None</em>, <em>pool_allocation_mode=None</em>, <em>primary_access_key=None</em>, <em>resource_group_name=None</em>, <em>secondary_access_key=None</em>, <em>storage_account_id=None</em>, <em>tags=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.batch.AwaitableGetAccountResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_azure.batch.AwaitableGetCertificateResult">
<em class="property">class </em><code class="descclassname">pulumi_azure.batch.</code><code class="descname">AwaitableGetCertificateResult</code><span class="sig-paren">(</span><em>account_name=None</em>, <em>format=None</em>, <em>name=None</em>, <em>public_data=None</em>, <em>resource_group_name=None</em>, <em>thumbprint=None</em>, <em>thumbprint_algorithm=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.batch.AwaitableGetCertificateResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_azure.batch.AwaitableGetPoolResult">
<em class="property">class </em><code class="descclassname">pulumi_azure.batch.</code><code class="descname">AwaitableGetPoolResult</code><span class="sig-paren">(</span><em>account_name=None</em>, <em>auto_scales=None</em>, <em>certificates=None</em>, <em>container_configurations=None</em>, <em>display_name=None</em>, <em>fixed_scales=None</em>, <em>max_tasks_per_node=None</em>, <em>name=None</em>, <em>node_agent_sku_id=None</em>, <em>resource_group_name=None</em>, <em>start_task=None</em>, <em>storage_image_references=None</em>, <em>vm_size=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.batch.AwaitableGetPoolResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_azure.batch.Certificate">
<em class="property">class </em><code class="descclassname">pulumi_azure.batch.</code><code class="descname">Certificate</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>account_name=None</em>, <em>certificate=None</em>, <em>format=None</em>, <em>password=None</em>, <em>resource_group_name=None</em>, <em>thumbprint=None</em>, <em>thumbprint_algorithm=None</em>, <em>__props__=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.batch.Certificate" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a certificate in an Azure Batch account.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>account_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Batch account. Changing this forces a new resource to be created.</li>
<li><strong>certificate</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The base64-encoded contents of the certificate.</li>
<li><strong>format</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The format of the certificate. Possible values are <code class="docutils literal notranslate"><span class="pre">Cer</span></code> or <code class="docutils literal notranslate"><span class="pre">Pfx</span></code>.</li>
<li><strong>password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The password to access the certificate’s private key. This must and can only be specified when <code class="docutils literal notranslate"><span class="pre">format</span></code> is <code class="docutils literal notranslate"><span class="pre">Pfx</span></code>.</li>
<li><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the Batch account. Changing this forces a new resource to be created.</li>
<li><strong>thumbprint</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The thumbprint of the certificate. At this time the only supported value is ‘SHA1’.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/batch_certificate.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/batch_certificate.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_azure.batch.Certificate.account_name">
<code class="descname">account_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.batch.Certificate.account_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Batch account. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.batch.Certificate.certificate">
<code class="descname">certificate</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.batch.Certificate.certificate" title="Permalink to this definition">¶</a></dt>
<dd><p>The base64-encoded contents of the certificate.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.batch.Certificate.format">
<code class="descname">format</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.batch.Certificate.format" title="Permalink to this definition">¶</a></dt>
<dd><p>The format of the certificate. Possible values are <code class="docutils literal notranslate"><span class="pre">Cer</span></code> or <code class="docutils literal notranslate"><span class="pre">Pfx</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.batch.Certificate.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.batch.Certificate.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The generated name of the certificate.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.batch.Certificate.password">
<code class="descname">password</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.batch.Certificate.password" title="Permalink to this definition">¶</a></dt>
<dd><p>The password to access the certificate’s private key. This must and can only be specified when <code class="docutils literal notranslate"><span class="pre">format</span></code> is <code class="docutils literal notranslate"><span class="pre">Pfx</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.batch.Certificate.public_data">
<code class="descname">public_data</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.batch.Certificate.public_data" title="Permalink to this definition">¶</a></dt>
<dd><p>The public key of the certificate.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.batch.Certificate.resource_group_name">
<code class="descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.batch.Certificate.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to create the Batch account. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.batch.Certificate.thumbprint">
<code class="descname">thumbprint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.batch.Certificate.thumbprint" title="Permalink to this definition">¶</a></dt>
<dd><p>The thumbprint of the certificate. At this time the only supported value is ‘SHA1’.</p>
</dd></dl>

<dl class="staticmethod">
<dt id="pulumi_azure.batch.Certificate.get">
<em class="property">static </em><code class="descname">get</code><span class="sig-paren">(</span><em>resource_name</em>, <em>id</em>, <em>opts=None</em>, <em>account_name=None</em>, <em>certificate=None</em>, <em>format=None</em>, <em>name=None</em>, <em>password=None</em>, <em>public_data=None</em>, <em>resource_group_name=None</em>, <em>thumbprint=None</em>, <em>thumbprint_algorithm=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.batch.Certificate.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Certificate resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.
:param str resource_name: The unique name of the resulting resource.
:param str id: The unique provider ID of the resource to lookup.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] account_name: Specifies the name of the Batch account. Changing this forces a new resource to be created.
:param pulumi.Input[str] certificate: The base64-encoded contents of the certificate.
:param pulumi.Input[str] format: The format of the certificate. Possible values are <code class="docutils literal notranslate"><span class="pre">Cer</span></code> or <code class="docutils literal notranslate"><span class="pre">Pfx</span></code>.
:param pulumi.Input[str] name: The generated name of the certificate.
:param pulumi.Input[str] password: The password to access the certificate’s private key. This must and can only be specified when <code class="docutils literal notranslate"><span class="pre">format</span></code> is <code class="docutils literal notranslate"><span class="pre">Pfx</span></code>.
:param pulumi.Input[str] public_data: The public key of the certificate.
:param pulumi.Input[str] resource_group_name: The name of the resource group in which to create the Batch account. Changing this forces a new resource to be created.
:param pulumi.Input[str] thumbprint: The thumbprint of the certificate. At this time the only supported value is ‘SHA1’.</p>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/batch_certificate.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/batch_certificate.html.markdown</a>.</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.batch.Certificate.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.batch.Certificate.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.batch.Certificate.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.batch.Certificate.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.batch.GetAccountResult">
<em class="property">class </em><code class="descclassname">pulumi_azure.batch.</code><code class="descname">GetAccountResult</code><span class="sig-paren">(</span><em>account_endpoint=None</em>, <em>location=None</em>, <em>name=None</em>, <em>pool_allocation_mode=None</em>, <em>primary_access_key=None</em>, <em>resource_group_name=None</em>, <em>secondary_access_key=None</em>, <em>storage_account_id=None</em>, <em>tags=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.batch.GetAccountResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getAccount.</p>
<dl class="attribute">
<dt id="pulumi_azure.batch.GetAccountResult.account_endpoint">
<code class="descname">account_endpoint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.batch.GetAccountResult.account_endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>The account endpoint used to interact with the Batch service.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.batch.GetAccountResult.location">
<code class="descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.batch.GetAccountResult.location" title="Permalink to this definition">¶</a></dt>
<dd><p>The Azure Region in which this Batch account exists.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.batch.GetAccountResult.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.batch.GetAccountResult.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The Batch account name.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.batch.GetAccountResult.pool_allocation_mode">
<code class="descname">pool_allocation_mode</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.batch.GetAccountResult.pool_allocation_mode" title="Permalink to this definition">¶</a></dt>
<dd><p>The pool allocation mode configured for this Batch account.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.batch.GetAccountResult.primary_access_key">
<code class="descname">primary_access_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.batch.GetAccountResult.primary_access_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The Batch account primary access key.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.batch.GetAccountResult.secondary_access_key">
<code class="descname">secondary_access_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.batch.GetAccountResult.secondary_access_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The Batch account secondary access key.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.batch.GetAccountResult.storage_account_id">
<code class="descname">storage_account_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.batch.GetAccountResult.storage_account_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Storage Account used for this Batch account.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.batch.GetAccountResult.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.batch.GetAccountResult.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A map of tags assigned to the Batch account.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.batch.GetAccountResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.batch.GetAccountResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azure.batch.GetCertificateResult">
<em class="property">class </em><code class="descclassname">pulumi_azure.batch.</code><code class="descname">GetCertificateResult</code><span class="sig-paren">(</span><em>account_name=None</em>, <em>format=None</em>, <em>name=None</em>, <em>public_data=None</em>, <em>resource_group_name=None</em>, <em>thumbprint=None</em>, <em>thumbprint_algorithm=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.batch.GetCertificateResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getCertificate.</p>
<dl class="attribute">
<dt id="pulumi_azure.batch.GetCertificateResult.format">
<code class="descname">format</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.batch.GetCertificateResult.format" title="Permalink to this definition">¶</a></dt>
<dd><p>The format of the certificate, such as <code class="docutils literal notranslate"><span class="pre">Cer</span></code> or <code class="docutils literal notranslate"><span class="pre">Pfx</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.batch.GetCertificateResult.public_data">
<code class="descname">public_data</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.batch.GetCertificateResult.public_data" title="Permalink to this definition">¶</a></dt>
<dd><p>The public key of the certificate.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.batch.GetCertificateResult.thumbprint">
<code class="descname">thumbprint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.batch.GetCertificateResult.thumbprint" title="Permalink to this definition">¶</a></dt>
<dd><p>The thumbprint of the certificate.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.batch.GetCertificateResult.thumbprint_algorithm">
<code class="descname">thumbprint_algorithm</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.batch.GetCertificateResult.thumbprint_algorithm" title="Permalink to this definition">¶</a></dt>
<dd><p>The algorithm of the certificate thumbprint.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.batch.GetCertificateResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.batch.GetCertificateResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azure.batch.GetPoolResult">
<em class="property">class </em><code class="descclassname">pulumi_azure.batch.</code><code class="descname">GetPoolResult</code><span class="sig-paren">(</span><em>account_name=None</em>, <em>auto_scales=None</em>, <em>certificates=None</em>, <em>container_configurations=None</em>, <em>display_name=None</em>, <em>fixed_scales=None</em>, <em>max_tasks_per_node=None</em>, <em>name=None</em>, <em>node_agent_sku_id=None</em>, <em>resource_group_name=None</em>, <em>start_task=None</em>, <em>storage_image_references=None</em>, <em>vm_size=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.batch.GetPoolResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getPool.</p>
<dl class="attribute">
<dt id="pulumi_azure.batch.GetPoolResult.account_name">
<code class="descname">account_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.batch.GetPoolResult.account_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Batch account.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.batch.GetPoolResult.auto_scales">
<code class="descname">auto_scales</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.batch.GetPoolResult.auto_scales" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">auto_scale</span></code> block that describes the scale settings when using auto scale.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.batch.GetPoolResult.certificates">
<code class="descname">certificates</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.batch.GetPoolResult.certificates" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more <code class="docutils literal notranslate"><span class="pre">certificate</span></code> blocks that describe the certificates installed on each compute node in the pool.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.batch.GetPoolResult.container_configurations">
<code class="descname">container_configurations</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.batch.GetPoolResult.container_configurations" title="Permalink to this definition">¶</a></dt>
<dd><p>The container configuration used in the pool’s VMs.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.batch.GetPoolResult.fixed_scales">
<code class="descname">fixed_scales</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.batch.GetPoolResult.fixed_scales" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">fixed_scale</span></code> block that describes the scale settings when using fixed scale.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.batch.GetPoolResult.max_tasks_per_node">
<code class="descname">max_tasks_per_node</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.batch.GetPoolResult.max_tasks_per_node" title="Permalink to this definition">¶</a></dt>
<dd><p>The maximum number of tasks that can run concurrently on a single compute node in the pool.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.batch.GetPoolResult.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.batch.GetPoolResult.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Batch pool.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.batch.GetPoolResult.node_agent_sku_id">
<code class="descname">node_agent_sku_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.batch.GetPoolResult.node_agent_sku_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The Sku of the node agents in the Batch pool.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.batch.GetPoolResult.start_task">
<code class="descname">start_task</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.batch.GetPoolResult.start_task" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">start_task</span></code> block that describes the start task settings for the Batch pool.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.batch.GetPoolResult.storage_image_references">
<code class="descname">storage_image_references</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.batch.GetPoolResult.storage_image_references" title="Permalink to this definition">¶</a></dt>
<dd><p>The reference of the storage image used by the nodes in the Batch pool.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.batch.GetPoolResult.vm_size">
<code class="descname">vm_size</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.batch.GetPoolResult.vm_size" title="Permalink to this definition">¶</a></dt>
<dd><p>The size of the VM created in the Batch pool.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.batch.GetPoolResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.batch.GetPoolResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azure.batch.Pool">
<em class="property">class </em><code class="descclassname">pulumi_azure.batch.</code><code class="descname">Pool</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>account_name=None</em>, <em>auto_scale=None</em>, <em>certificates=None</em>, <em>container_configuration=None</em>, <em>display_name=None</em>, <em>fixed_scale=None</em>, <em>max_tasks_per_node=None</em>, <em>name=None</em>, <em>node_agent_sku_id=None</em>, <em>resource_group_name=None</em>, <em>start_task=None</em>, <em>stop_pending_resize_operation=None</em>, <em>storage_image_reference=None</em>, <em>vm_size=None</em>, <em>__props__=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.batch.Pool" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an Azure Batch pool.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>account_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Batch account in which the pool will be created. Changing this forces a new resource to be created.</li>
<li><strong>auto_scale</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">auto_scale</span></code> block that describes the scale settings when using auto scale.</li>
<li><strong>certificates</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">certificate</span></code> blocks that describe the certificates to be installed on each compute node in the pool.</li>
<li><strong>container_configuration</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The container configuration used in the pool’s VMs.</li>
<li><strong>display_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the display name of the Batch pool.</li>
<li><strong>fixed_scale</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">fixed_scale</span></code> block that describes the scale settings when using fixed scale.</li>
<li><strong>max_tasks_per_node</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Specifies the maximum number of tasks that can run concurrently on a single compute node in the pool. Defaults to <code class="docutils literal notranslate"><span class="pre">1</span></code>. Changing this forces a new resource to be created.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Batch pool. Changing this forces a new resource to be created.</li>
<li><strong>node_agent_sku_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the Sku of the node agents that will be created in the Batch pool.</li>
<li><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the Batch pool. Changing this forces a new resource to be created.</li>
<li><strong>start_task</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">start_task</span></code> block that describes the start task settings for the Batch pool.</li>
<li><strong>storage_image_reference</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">storage_image_reference</span></code> for the virtual machines that will compose the Batch pool.</li>
<li><strong>vm_size</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the size of the VM created in the Batch pool.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/batch_pool.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/batch_pool.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_azure.batch.Pool.account_name">
<code class="descname">account_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.batch.Pool.account_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Batch account in which the pool will be created. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.batch.Pool.auto_scale">
<code class="descname">auto_scale</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.batch.Pool.auto_scale" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">auto_scale</span></code> block that describes the scale settings when using auto scale.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.batch.Pool.certificates">
<code class="descname">certificates</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.batch.Pool.certificates" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more <code class="docutils literal notranslate"><span class="pre">certificate</span></code> blocks that describe the certificates to be installed on each compute node in the pool.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.batch.Pool.container_configuration">
<code class="descname">container_configuration</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.batch.Pool.container_configuration" title="Permalink to this definition">¶</a></dt>
<dd><p>The container configuration used in the pool’s VMs.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.batch.Pool.display_name">
<code class="descname">display_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.batch.Pool.display_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the display name of the Batch pool.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.batch.Pool.fixed_scale">
<code class="descname">fixed_scale</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.batch.Pool.fixed_scale" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">fixed_scale</span></code> block that describes the scale settings when using fixed scale.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.batch.Pool.max_tasks_per_node">
<code class="descname">max_tasks_per_node</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.batch.Pool.max_tasks_per_node" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the maximum number of tasks that can run concurrently on a single compute node in the pool. Defaults to <code class="docutils literal notranslate"><span class="pre">1</span></code>. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.batch.Pool.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.batch.Pool.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Batch pool. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.batch.Pool.node_agent_sku_id">
<code class="descname">node_agent_sku_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.batch.Pool.node_agent_sku_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the Sku of the node agents that will be created in the Batch pool.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.batch.Pool.resource_group_name">
<code class="descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.batch.Pool.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to create the Batch pool. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.batch.Pool.start_task">
<code class="descname">start_task</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.batch.Pool.start_task" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">start_task</span></code> block that describes the start task settings for the Batch pool.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.batch.Pool.storage_image_reference">
<code class="descname">storage_image_reference</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.batch.Pool.storage_image_reference" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">storage_image_reference</span></code> for the virtual machines that will compose the Batch pool.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.batch.Pool.vm_size">
<code class="descname">vm_size</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.batch.Pool.vm_size" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the size of the VM created in the Batch pool.</p>
</dd></dl>

<dl class="staticmethod">
<dt id="pulumi_azure.batch.Pool.get">
<em class="property">static </em><code class="descname">get</code><span class="sig-paren">(</span><em>resource_name</em>, <em>id</em>, <em>opts=None</em>, <em>account_name=None</em>, <em>auto_scale=None</em>, <em>certificates=None</em>, <em>container_configuration=None</em>, <em>display_name=None</em>, <em>fixed_scale=None</em>, <em>max_tasks_per_node=None</em>, <em>name=None</em>, <em>node_agent_sku_id=None</em>, <em>resource_group_name=None</em>, <em>start_task=None</em>, <em>stop_pending_resize_operation=None</em>, <em>storage_image_reference=None</em>, <em>vm_size=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.batch.Pool.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Pool resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.
:param str resource_name: The unique name of the resulting resource.
:param str id: The unique provider ID of the resource to lookup.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] account_name: Specifies the name of the Batch account in which the pool will be created. Changing this forces a new resource to be created.
:param pulumi.Input[dict] auto_scale: A <code class="docutils literal notranslate"><span class="pre">auto_scale</span></code> block that describes the scale settings when using auto scale.
:param pulumi.Input[list] certificates: One or more <code class="docutils literal notranslate"><span class="pre">certificate</span></code> blocks that describe the certificates to be installed on each compute node in the pool.
:param pulumi.Input[dict] container_configuration: The container configuration used in the pool’s VMs.
:param pulumi.Input[str] display_name: Specifies the display name of the Batch pool.
:param pulumi.Input[dict] fixed_scale: A <code class="docutils literal notranslate"><span class="pre">fixed_scale</span></code> block that describes the scale settings when using fixed scale.
:param pulumi.Input[float] max_tasks_per_node: Specifies the maximum number of tasks that can run concurrently on a single compute node in the pool. Defaults to <code class="docutils literal notranslate"><span class="pre">1</span></code>. Changing this forces a new resource to be created.
:param pulumi.Input[str] name: Specifies the name of the Batch pool. Changing this forces a new resource to be created.
:param pulumi.Input[str] node_agent_sku_id: Specifies the Sku of the node agents that will be created in the Batch pool.
:param pulumi.Input[str] resource_group_name: The name of the resource group in which to create the Batch pool. Changing this forces a new resource to be created.
:param pulumi.Input[dict] start_task: A <code class="docutils literal notranslate"><span class="pre">start_task</span></code> block that describes the start task settings for the Batch pool.
:param pulumi.Input[dict] storage_image_reference: A <code class="docutils literal notranslate"><span class="pre">storage_image_reference</span></code> for the virtual machines that will compose the Batch pool.
:param pulumi.Input[str] vm_size: Specifies the size of the VM created in the Batch pool.</p>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/batch_pool.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/batch_pool.html.markdown</a>.</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.batch.Pool.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.batch.Pool.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.batch.Pool.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.batch.Pool.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.batch.get_account">
<code class="descclassname">pulumi_azure.batch.</code><code class="descname">get_account</code><span class="sig-paren">(</span><em>name=None</em>, <em>resource_group_name=None</em>, <em>opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.batch.get_account" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing Batch Account.</p>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/batch_account.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/batch_account.html.markdown</a>.</div></blockquote>
</dd></dl>

<dl class="function">
<dt id="pulumi_azure.batch.get_certificate">
<code class="descclassname">pulumi_azure.batch.</code><code class="descname">get_certificate</code><span class="sig-paren">(</span><em>account_name=None</em>, <em>name=None</em>, <em>resource_group_name=None</em>, <em>opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.batch.get_certificate" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing certificate in a Batch Account.</p>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/batch_certificate.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/batch_certificate.html.markdown</a>.</div></blockquote>
</dd></dl>

<dl class="function">
<dt id="pulumi_azure.batch.get_pool">
<code class="descclassname">pulumi_azure.batch.</code><code class="descname">get_pool</code><span class="sig-paren">(</span><em>account_name=None</em>, <em>certificates=None</em>, <em>name=None</em>, <em>resource_group_name=None</em>, <em>start_task=None</em>, <em>opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.batch.get_pool" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing Batch pool</p>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/batch_pool.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/batch_pool.html.markdown</a>.</div></blockquote>
</dd></dl>

</div>
