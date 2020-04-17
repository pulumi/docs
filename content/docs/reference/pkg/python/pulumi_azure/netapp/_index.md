---
title: Module netapp
title_tag: Module netapp | Package pulumi_azure | Python SDK
linktitle: netapp
notitle: true
---

<div class="section" id="netapp">
<h1>netapp<a class="headerlink" href="#netapp" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-azure/issues">pulumi/pulumi-azure repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/issues">terraform-providers/terraform-provider-azurerm repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_azure.netapp"></span><dl class="class">
<dt id="pulumi_azure.netapp.Account">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.netapp.</code><code class="sig-name descname">Account</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">active_directory=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.netapp.Account" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a NetApp Account.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Azure allows only one active directory can be joined to a single subscription at a time for NetApp Account.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>active_directory</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">active_directory</span></code> block as defined below.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the NetApp Account. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group where the NetApp Account should be created. Changing this forces a new resource to be created.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>active_directory</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">dns_servers</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of DNS server IP addresses for the Active Directory domain. Only allows <code class="docutils literal notranslate"><span class="pre">IPv4</span></code> address.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">domain</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the Active Directory domain.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">organizationalUnit</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Organizational Unit (OU) within the Active Directory Domain.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The password associated with the <code class="docutils literal notranslate"><span class="pre">username</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">smbServerName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The NetBIOS name which should be used for the NetApp SMB Server, which will be registered as a computer account in the AD and used to mount volumes.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Username of Active Directory Domain Administrator.</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_azure.netapp.Account.active_directory">
<code class="sig-name descname">active_directory</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.netapp.Account.active_directory" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">active_directory</span></code> block as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">dns_servers</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - A list of DNS server IP addresses for the Active Directory domain. Only allows <code class="docutils literal notranslate"><span class="pre">IPv4</span></code> address.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">domain</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the Active Directory domain.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">organizationalUnit</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Organizational Unit (OU) within the Active Directory Domain.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The password associated with the <code class="docutils literal notranslate"><span class="pre">username</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">smbServerName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The NetBIOS name which should be used for the NetApp SMB Server, which will be registered as a computer account in the AD and used to mount volumes.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Username of Active Directory Domain Administrator.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.netapp.Account.location">
<code class="sig-name descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.netapp.Account.location" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.netapp.Account.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.netapp.Account.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the NetApp Account. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.netapp.Account.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.netapp.Account.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group where the NetApp Account should be created. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.netapp.Account.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.netapp.Account.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.netapp.Account.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">active_directory=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.netapp.Account.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Account resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>active_directory</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">active_directory</span></code> block as defined below.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the NetApp Account. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group where the NetApp Account should be created. Changing this forces a new resource to be created.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>active_directory</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">dns_servers</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of DNS server IP addresses for the Active Directory domain. Only allows <code class="docutils literal notranslate"><span class="pre">IPv4</span></code> address.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">domain</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the Active Directory domain.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">organizationalUnit</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Organizational Unit (OU) within the Active Directory Domain.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">password</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The password associated with the <code class="docutils literal notranslate"><span class="pre">username</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">smbServerName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The NetBIOS name which should be used for the NetApp SMB Server, which will be registered as a computer account in the AD and used to mount volumes.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Username of Active Directory Domain Administrator.</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.netapp.Account.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.netapp.Account.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.netapp.Account.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.netapp.Account.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.netapp.AwaitableGetAccountResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.netapp.</code><code class="sig-name descname">AwaitableGetAccountResult</code><span class="sig-paren">(</span><em class="sig-param">id=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.netapp.AwaitableGetAccountResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_azure.netapp.AwaitableGetPoolResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.netapp.</code><code class="sig-name descname">AwaitableGetPoolResult</code><span class="sig-paren">(</span><em class="sig-param">account_name=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">service_level=None</em>, <em class="sig-param">size_in_tb=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.netapp.AwaitableGetPoolResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_azure.netapp.AwaitableGetSnapshotResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.netapp.</code><code class="sig-name descname">AwaitableGetSnapshotResult</code><span class="sig-paren">(</span><em class="sig-param">account_name=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">pool_name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">volume_name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.netapp.AwaitableGetSnapshotResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_azure.netapp.AwaitableGetVolumeResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.netapp.</code><code class="sig-name descname">AwaitableGetVolumeResult</code><span class="sig-paren">(</span><em class="sig-param">account_name=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">pool_name=None</em>, <em class="sig-param">protocols=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">service_level=None</em>, <em class="sig-param">storage_quota_in_gb=None</em>, <em class="sig-param">subnet_id=None</em>, <em class="sig-param">volume_path=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.netapp.AwaitableGetVolumeResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_azure.netapp.GetAccountResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.netapp.</code><code class="sig-name descname">GetAccountResult</code><span class="sig-paren">(</span><em class="sig-param">id=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.netapp.GetAccountResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getAccount.</p>
<dl class="attribute">
<dt id="pulumi_azure.netapp.GetAccountResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.netapp.GetAccountResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.netapp.GetAccountResult.location">
<code class="sig-name descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.netapp.GetAccountResult.location" title="Permalink to this definition">¶</a></dt>
<dd><p>The Azure Region where the NetApp Account exists.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azure.netapp.GetPoolResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.netapp.</code><code class="sig-name descname">GetPoolResult</code><span class="sig-paren">(</span><em class="sig-param">account_name=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">service_level=None</em>, <em class="sig-param">size_in_tb=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.netapp.GetPoolResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getPool.</p>
<dl class="attribute">
<dt id="pulumi_azure.netapp.GetPoolResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.netapp.GetPoolResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.netapp.GetPoolResult.location">
<code class="sig-name descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.netapp.GetPoolResult.location" title="Permalink to this definition">¶</a></dt>
<dd><p>The Azure Region where the NetApp Pool exists.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.netapp.GetPoolResult.service_level">
<code class="sig-name descname">service_level</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.netapp.GetPoolResult.service_level" title="Permalink to this definition">¶</a></dt>
<dd><p>The service level of the file system.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.netapp.GetPoolResult.size_in_tb">
<code class="sig-name descname">size_in_tb</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.netapp.GetPoolResult.size_in_tb" title="Permalink to this definition">¶</a></dt>
<dd><p>Provisioned size of the pool in TB.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azure.netapp.GetSnapshotResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.netapp.</code><code class="sig-name descname">GetSnapshotResult</code><span class="sig-paren">(</span><em class="sig-param">account_name=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">pool_name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">volume_name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.netapp.GetSnapshotResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getSnapshot.</p>
<dl class="attribute">
<dt id="pulumi_azure.netapp.GetSnapshotResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.netapp.GetSnapshotResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.netapp.GetSnapshotResult.location">
<code class="sig-name descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.netapp.GetSnapshotResult.location" title="Permalink to this definition">¶</a></dt>
<dd><p>The Azure Region where the NetApp Snapshot exists.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azure.netapp.GetVolumeResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.netapp.</code><code class="sig-name descname">GetVolumeResult</code><span class="sig-paren">(</span><em class="sig-param">account_name=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">pool_name=None</em>, <em class="sig-param">protocols=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">service_level=None</em>, <em class="sig-param">storage_quota_in_gb=None</em>, <em class="sig-param">subnet_id=None</em>, <em class="sig-param">volume_path=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.netapp.GetVolumeResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getVolume.</p>
<dl class="attribute">
<dt id="pulumi_azure.netapp.GetVolumeResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.netapp.GetVolumeResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.netapp.GetVolumeResult.location">
<code class="sig-name descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.netapp.GetVolumeResult.location" title="Permalink to this definition">¶</a></dt>
<dd><p>The Azure Region where the NetApp Volume exists.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.netapp.GetVolumeResult.service_level">
<code class="sig-name descname">service_level</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.netapp.GetVolumeResult.service_level" title="Permalink to this definition">¶</a></dt>
<dd><p>The service level of the file system.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.netapp.GetVolumeResult.storage_quota_in_gb">
<code class="sig-name descname">storage_quota_in_gb</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.netapp.GetVolumeResult.storage_quota_in_gb" title="Permalink to this definition">¶</a></dt>
<dd><p>The maximum Storage Quota in Gigabytes allowed for a file system.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.netapp.GetVolumeResult.subnet_id">
<code class="sig-name descname">subnet_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.netapp.GetVolumeResult.subnet_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of a Subnet in which the NetApp Volume resides.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.netapp.GetVolumeResult.volume_path">
<code class="sig-name descname">volume_path</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.netapp.GetVolumeResult.volume_path" title="Permalink to this definition">¶</a></dt>
<dd><p>The unique file path of the volume.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azure.netapp.Pool">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.netapp.</code><code class="sig-name descname">Pool</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">account_name=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">service_level=None</em>, <em class="sig-param">size_in_tb=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.netapp.Pool" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Pool within a NetApp Account.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>account_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the NetApp account in which the NetApp Pool should be created. Changing this forces a new resource to be created.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the NetApp Pool. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group where the NetApp Pool should be created. Changing this forces a new resource to be created.</p></li>
<li><p><strong>service_level</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The service level of the file system. Valid values include <code class="docutils literal notranslate"><span class="pre">Premium</span></code>, <code class="docutils literal notranslate"><span class="pre">Standard</span></code>, or <code class="docutils literal notranslate"><span class="pre">Ultra</span></code>.</p></li>
<li><p><strong>size_in_tb</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Provisioned size of the pool in TB. Value must be between <code class="docutils literal notranslate"><span class="pre">4</span></code> and <code class="docutils literal notranslate"><span class="pre">500</span></code>.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_azure.netapp.Pool.account_name">
<code class="sig-name descname">account_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.netapp.Pool.account_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the NetApp account in which the NetApp Pool should be created. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.netapp.Pool.location">
<code class="sig-name descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.netapp.Pool.location" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.netapp.Pool.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.netapp.Pool.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the NetApp Pool. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.netapp.Pool.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.netapp.Pool.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group where the NetApp Pool should be created. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.netapp.Pool.service_level">
<code class="sig-name descname">service_level</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.netapp.Pool.service_level" title="Permalink to this definition">¶</a></dt>
<dd><p>The service level of the file system. Valid values include <code class="docutils literal notranslate"><span class="pre">Premium</span></code>, <code class="docutils literal notranslate"><span class="pre">Standard</span></code>, or <code class="docutils literal notranslate"><span class="pre">Ultra</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.netapp.Pool.size_in_tb">
<code class="sig-name descname">size_in_tb</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.netapp.Pool.size_in_tb" title="Permalink to this definition">¶</a></dt>
<dd><p>Provisioned size of the pool in TB. Value must be between <code class="docutils literal notranslate"><span class="pre">4</span></code> and <code class="docutils literal notranslate"><span class="pre">500</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.netapp.Pool.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.netapp.Pool.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.netapp.Pool.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">account_name=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">service_level=None</em>, <em class="sig-param">size_in_tb=None</em>, <em class="sig-param">tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.netapp.Pool.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Pool resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>account_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the NetApp account in which the NetApp Pool should be created. Changing this forces a new resource to be created.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the NetApp Pool. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group where the NetApp Pool should be created. Changing this forces a new resource to be created.</p></li>
<li><p><strong>service_level</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The service level of the file system. Valid values include <code class="docutils literal notranslate"><span class="pre">Premium</span></code>, <code class="docutils literal notranslate"><span class="pre">Standard</span></code>, or <code class="docutils literal notranslate"><span class="pre">Ultra</span></code>.</p></li>
<li><p><strong>size_in_tb</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Provisioned size of the pool in TB. Value must be between <code class="docutils literal notranslate"><span class="pre">4</span></code> and <code class="docutils literal notranslate"><span class="pre">500</span></code>.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.netapp.Pool.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.netapp.Pool.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.netapp.Pool.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.netapp.Pool.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.netapp.Snapshot">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.netapp.</code><code class="sig-name descname">Snapshot</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">account_name=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">pool_name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">volume_name=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.netapp.Snapshot" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a NetApp Snapshot.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>account_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the NetApp account in which the NetApp Pool should be created. Changing this forces a new resource to be created.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the NetApp Snapshot. Changing this forces a new resource to be created.</p></li>
<li><p><strong>pool_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the NetApp pool in which the NetApp Volume should be created. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group where the NetApp Snapshot should be created. Changing this forces a new resource to be created.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
<li><p><strong>volume_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the NetApp volume in which the NetApp Snapshot should be created. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_azure.netapp.Snapshot.account_name">
<code class="sig-name descname">account_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.netapp.Snapshot.account_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the NetApp account in which the NetApp Pool should be created. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.netapp.Snapshot.location">
<code class="sig-name descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.netapp.Snapshot.location" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.netapp.Snapshot.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.netapp.Snapshot.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the NetApp Snapshot. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.netapp.Snapshot.pool_name">
<code class="sig-name descname">pool_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.netapp.Snapshot.pool_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the NetApp pool in which the NetApp Volume should be created. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.netapp.Snapshot.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.netapp.Snapshot.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group where the NetApp Snapshot should be created. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.netapp.Snapshot.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.netapp.Snapshot.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.netapp.Snapshot.volume_name">
<code class="sig-name descname">volume_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.netapp.Snapshot.volume_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the NetApp volume in which the NetApp Snapshot should be created. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.netapp.Snapshot.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">account_name=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">pool_name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">volume_name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.netapp.Snapshot.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Snapshot resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>account_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the NetApp account in which the NetApp Pool should be created. Changing this forces a new resource to be created.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the NetApp Snapshot. Changing this forces a new resource to be created.</p></li>
<li><p><strong>pool_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the NetApp pool in which the NetApp Volume should be created. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group where the NetApp Snapshot should be created. Changing this forces a new resource to be created.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
<li><p><strong>volume_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the NetApp volume in which the NetApp Snapshot should be created. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.netapp.Snapshot.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.netapp.Snapshot.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.netapp.Snapshot.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.netapp.Snapshot.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.netapp.Volume">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.netapp.</code><code class="sig-name descname">Volume</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">account_name=None</em>, <em class="sig-param">export_policy_rules=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">pool_name=None</em>, <em class="sig-param">protocols=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">service_level=None</em>, <em class="sig-param">storage_quota_in_gb=None</em>, <em class="sig-param">subnet_id=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">volume_path=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.netapp.Volume" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a NetApp Volume.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>account_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the NetApp account in which the NetApp Pool should be created. Changing this forces a new resource to be created.</p></li>
<li><p><strong>export_policy_rules</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">export_policy_rule</span></code> block defined below.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the NetApp Volume. Changing this forces a new resource to be created.</p></li>
<li><p><strong>pool_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the NetApp pool in which the NetApp Volume should be created. Changing this forces a new resource to be created.</p></li>
<li><p><strong>protocols</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The target volume protocol expressed as a list. Supported single value include <code class="docutils literal notranslate"><span class="pre">CIFS</span></code>, <code class="docutils literal notranslate"><span class="pre">NFSv3</span></code>, or <code class="docutils literal notranslate"><span class="pre">NFSv4.1</span></code>. If argument is not defined it will default to <code class="docutils literal notranslate"><span class="pre">NFSv3</span></code>. Changing this forces a new resource to be created and data will be lost.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group where the NetApp Volume should be created. Changing this forces a new resource to be created.</p></li>
<li><p><strong>service_level</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The target performance of the file system. Valid values include <code class="docutils literal notranslate"><span class="pre">Premium</span></code>, <code class="docutils literal notranslate"><span class="pre">Standard</span></code>, or <code class="docutils literal notranslate"><span class="pre">Ultra</span></code>.</p></li>
<li><p><strong>storage_quota_in_gb</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The maximum Storage Quota allowed for a file system in Gigabytes.</p></li>
<li><p><strong>subnet_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Subnet the NetApp Volume resides in, which must have the <code class="docutils literal notranslate"><span class="pre">Microsoft.NetApp/volumes</span></code> delegation. Changing this forces a new resource to be created.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
<li><p><strong>volume_path</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A unique file path for the volume. Used when creating mount targets. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>export_policy_rules</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">allowedClients</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of allowed clients IPv4 addresses.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cifsEnabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Is the CIFS protocol allowed?</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">nfsv3Enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Is the NFSv3 protocol allowed?</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">nfsv4Enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Is the NFSv4 protocol allowed?</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">protocolsEnabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A list of allowed protocols. Valid values include <code class="docutils literal notranslate"><span class="pre">CIFS</span></code>, <code class="docutils literal notranslate"><span class="pre">NFSv3</span></code>, or <code class="docutils literal notranslate"><span class="pre">NFSv4.1</span></code>. Only one value is supported at this time. This replaces the previous arguments: <code class="docutils literal notranslate"><span class="pre">cifs_enabled</span></code>, <code class="docutils literal notranslate"><span class="pre">nfsv3_enabled</span></code> and <code class="docutils literal notranslate"><span class="pre">nfsv4_enabled</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ruleIndex</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The index number of the rule.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">unixReadOnly</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Is the file system on unix read only?</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">unixReadWrite</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Is the file system on unix read and write?</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_azure.netapp.Volume.account_name">
<code class="sig-name descname">account_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.netapp.Volume.account_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the NetApp account in which the NetApp Pool should be created. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.netapp.Volume.export_policy_rules">
<code class="sig-name descname">export_policy_rules</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.netapp.Volume.export_policy_rules" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more <code class="docutils literal notranslate"><span class="pre">export_policy_rule</span></code> block defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">allowedClients</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - A list of allowed clients IPv4 addresses.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cifsEnabled</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Is the CIFS protocol allowed?</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">nfsv3Enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Is the NFSv3 protocol allowed?</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">nfsv4Enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Is the NFSv4 protocol allowed?</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">protocolsEnabled</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - A list of allowed protocols. Valid values include <code class="docutils literal notranslate"><span class="pre">CIFS</span></code>, <code class="docutils literal notranslate"><span class="pre">NFSv3</span></code>, or <code class="docutils literal notranslate"><span class="pre">NFSv4.1</span></code>. Only one value is supported at this time. This replaces the previous arguments: <code class="docutils literal notranslate"><span class="pre">cifs_enabled</span></code>, <code class="docutils literal notranslate"><span class="pre">nfsv3_enabled</span></code> and <code class="docutils literal notranslate"><span class="pre">nfsv4_enabled</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ruleIndex</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The index number of the rule.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">unixReadOnly</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Is the file system on unix read only?</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">unixReadWrite</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Is the file system on unix read and write?</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.netapp.Volume.location">
<code class="sig-name descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.netapp.Volume.location" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.netapp.Volume.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.netapp.Volume.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the NetApp Volume. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.netapp.Volume.pool_name">
<code class="sig-name descname">pool_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.netapp.Volume.pool_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the NetApp pool in which the NetApp Volume should be created. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.netapp.Volume.protocols">
<code class="sig-name descname">protocols</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.netapp.Volume.protocols" title="Permalink to this definition">¶</a></dt>
<dd><p>The target volume protocol expressed as a list. Supported single value include <code class="docutils literal notranslate"><span class="pre">CIFS</span></code>, <code class="docutils literal notranslate"><span class="pre">NFSv3</span></code>, or <code class="docutils literal notranslate"><span class="pre">NFSv4.1</span></code>. If argument is not defined it will default to <code class="docutils literal notranslate"><span class="pre">NFSv3</span></code>. Changing this forces a new resource to be created and data will be lost.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.netapp.Volume.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.netapp.Volume.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group where the NetApp Volume should be created. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.netapp.Volume.service_level">
<code class="sig-name descname">service_level</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.netapp.Volume.service_level" title="Permalink to this definition">¶</a></dt>
<dd><p>The target performance of the file system. Valid values include <code class="docutils literal notranslate"><span class="pre">Premium</span></code>, <code class="docutils literal notranslate"><span class="pre">Standard</span></code>, or <code class="docutils literal notranslate"><span class="pre">Ultra</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.netapp.Volume.storage_quota_in_gb">
<code class="sig-name descname">storage_quota_in_gb</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.netapp.Volume.storage_quota_in_gb" title="Permalink to this definition">¶</a></dt>
<dd><p>The maximum Storage Quota allowed for a file system in Gigabytes.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.netapp.Volume.subnet_id">
<code class="sig-name descname">subnet_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.netapp.Volume.subnet_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Subnet the NetApp Volume resides in, which must have the <code class="docutils literal notranslate"><span class="pre">Microsoft.NetApp/volumes</span></code> delegation. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.netapp.Volume.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.netapp.Volume.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.netapp.Volume.volume_path">
<code class="sig-name descname">volume_path</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.netapp.Volume.volume_path" title="Permalink to this definition">¶</a></dt>
<dd><p>A unique file path for the volume. Used when creating mount targets. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.netapp.Volume.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">account_name=None</em>, <em class="sig-param">export_policy_rules=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">pool_name=None</em>, <em class="sig-param">protocols=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">service_level=None</em>, <em class="sig-param">storage_quota_in_gb=None</em>, <em class="sig-param">subnet_id=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">volume_path=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.netapp.Volume.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Volume resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>account_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the NetApp account in which the NetApp Pool should be created. Changing this forces a new resource to be created.</p></li>
<li><p><strong>export_policy_rules</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">export_policy_rule</span></code> block defined below.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the NetApp Volume. Changing this forces a new resource to be created.</p></li>
<li><p><strong>pool_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the NetApp pool in which the NetApp Volume should be created. Changing this forces a new resource to be created.</p></li>
<li><p><strong>protocols</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The target volume protocol expressed as a list. Supported single value include <code class="docutils literal notranslate"><span class="pre">CIFS</span></code>, <code class="docutils literal notranslate"><span class="pre">NFSv3</span></code>, or <code class="docutils literal notranslate"><span class="pre">NFSv4.1</span></code>. If argument is not defined it will default to <code class="docutils literal notranslate"><span class="pre">NFSv3</span></code>. Changing this forces a new resource to be created and data will be lost.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group where the NetApp Volume should be created. Changing this forces a new resource to be created.</p></li>
<li><p><strong>service_level</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The target performance of the file system. Valid values include <code class="docutils literal notranslate"><span class="pre">Premium</span></code>, <code class="docutils literal notranslate"><span class="pre">Standard</span></code>, or <code class="docutils literal notranslate"><span class="pre">Ultra</span></code>.</p></li>
<li><p><strong>storage_quota_in_gb</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The maximum Storage Quota allowed for a file system in Gigabytes.</p></li>
<li><p><strong>subnet_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Subnet the NetApp Volume resides in, which must have the <code class="docutils literal notranslate"><span class="pre">Microsoft.NetApp/volumes</span></code> delegation. Changing this forces a new resource to be created.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
<li><p><strong>volume_path</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A unique file path for the volume. Used when creating mount targets. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>export_policy_rules</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">allowedClients</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of allowed clients IPv4 addresses.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cifsEnabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Is the CIFS protocol allowed?</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">nfsv3Enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Is the NFSv3 protocol allowed?</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">nfsv4Enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Is the NFSv4 protocol allowed?</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">protocolsEnabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A list of allowed protocols. Valid values include <code class="docutils literal notranslate"><span class="pre">CIFS</span></code>, <code class="docutils literal notranslate"><span class="pre">NFSv3</span></code>, or <code class="docutils literal notranslate"><span class="pre">NFSv4.1</span></code>. Only one value is supported at this time. This replaces the previous arguments: <code class="docutils literal notranslate"><span class="pre">cifs_enabled</span></code>, <code class="docutils literal notranslate"><span class="pre">nfsv3_enabled</span></code> and <code class="docutils literal notranslate"><span class="pre">nfsv4_enabled</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ruleIndex</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The index number of the rule.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">unixReadOnly</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Is the file system on unix read only?</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">unixReadWrite</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Is the file system on unix read and write?</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.netapp.Volume.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.netapp.Volume.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.netapp.Volume.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.netapp.Volume.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.netapp.get_account">
<code class="sig-prename descclassname">pulumi_azure.netapp.</code><code class="sig-name descname">get_account</code><span class="sig-paren">(</span><em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.netapp.get_account" title="Permalink to this definition">¶</a></dt>
<dd><p>Uses this data source to access information about an existing NetApp Account.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>name</strong> (<em>str</em>) – The name of the NetApp Account.</p></li>
<li><p><strong>resource_group_name</strong> (<em>str</em>) – The Name of the Resource Group where the NetApp Account exists.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="function">
<dt id="pulumi_azure.netapp.get_pool">
<code class="sig-prename descclassname">pulumi_azure.netapp.</code><code class="sig-name descname">get_pool</code><span class="sig-paren">(</span><em class="sig-param">account_name=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.netapp.get_pool" title="Permalink to this definition">¶</a></dt>
<dd><p>Uses this data source to access information about an existing NetApp Pool.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>account_name</strong> (<em>str</em>) – The name of the NetApp account where the NetApp pool exists.</p></li>
<li><p><strong>name</strong> (<em>str</em>) – The name of the NetApp Pool.</p></li>
<li><p><strong>resource_group_name</strong> (<em>str</em>) – The Name of the Resource Group where the NetApp Pool exists.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="function">
<dt id="pulumi_azure.netapp.get_snapshot">
<code class="sig-prename descclassname">pulumi_azure.netapp.</code><code class="sig-name descname">get_snapshot</code><span class="sig-paren">(</span><em class="sig-param">account_name=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">pool_name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">volume_name=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.netapp.get_snapshot" title="Permalink to this definition">¶</a></dt>
<dd><p>Uses this data source to access information about an existing NetApp Snapshot.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>account_name</strong> (<em>str</em>) – The name of the NetApp Account where the NetApp Pool exists.</p></li>
<li><p><strong>name</strong> (<em>str</em>) – The name of the NetApp Snapshot.</p></li>
<li><p><strong>pool_name</strong> (<em>str</em>) – The name of the NetApp Pool where the NetApp Volume exists.</p></li>
<li><p><strong>resource_group_name</strong> (<em>str</em>) – The Name of the Resource Group where the NetApp Snapshot exists.</p></li>
<li><p><strong>volume_name</strong> (<em>str</em>) – The name of the NetApp Volume where the NetApp Snapshot exists.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="function">
<dt id="pulumi_azure.netapp.get_volume">
<code class="sig-prename descclassname">pulumi_azure.netapp.</code><code class="sig-name descname">get_volume</code><span class="sig-paren">(</span><em class="sig-param">account_name=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">pool_name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.netapp.get_volume" title="Permalink to this definition">¶</a></dt>
<dd><p>Uses this data source to access information about an existing NetApp Volume.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>account_name</strong> (<em>str</em>) – The name of the NetApp account where the NetApp pool exists.</p></li>
<li><p><strong>name</strong> (<em>str</em>) – The name of the NetApp Volume.</p></li>
<li><p><strong>pool_name</strong> (<em>str</em>) – The name of the NetApp pool where the NetApp volume exists.</p></li>
<li><p><strong>resource_group_name</strong> (<em>str</em>) – The Name of the Resource Group where the NetApp Volume exists.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

</div>
