---
---

<div class="section" id="devtest">
<h1>devtest<a class="headerlink" href="#devtest" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azure">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-azure/issues">pulumi/pulumi-azure repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azure/issues">terraform-providers/terraform-provider-azure repo</a>.</div></blockquote>
<span class="target" id="module-pulumi_azure.devtest"></span><dl class="class">
<dt id="pulumi_azure.devtest.GetLabResult">
<em class="property">class </em><code class="descclassname">pulumi_azure.devtest.</code><code class="descname">GetLabResult</code><span class="sig-paren">(</span><em>artifacts_storage_account_id=None</em>, <em>default_premium_storage_account_id=None</em>, <em>default_storage_account_id=None</em>, <em>key_vault_id=None</em>, <em>location=None</em>, <em>name=None</em>, <em>premium_data_disk_storage_account_id=None</em>, <em>resource_group_name=None</em>, <em>storage_type=None</em>, <em>tags=None</em>, <em>unique_identifier=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.devtest.GetLabResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getLab.</p>
<dl class="attribute">
<dt id="pulumi_azure.devtest.GetLabResult.artifacts_storage_account_id">
<code class="descname">artifacts_storage_account_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.devtest.GetLabResult.artifacts_storage_account_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Storage Account used for Artifact Storage.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.devtest.GetLabResult.default_premium_storage_account_id">
<code class="descname">default_premium_storage_account_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.devtest.GetLabResult.default_premium_storage_account_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Default Premium Storage Account for this Dev Test Lab.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.devtest.GetLabResult.default_storage_account_id">
<code class="descname">default_storage_account_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.devtest.GetLabResult.default_storage_account_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Default Storage Account for this Dev Test Lab.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.devtest.GetLabResult.key_vault_id">
<code class="descname">key_vault_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.devtest.GetLabResult.key_vault_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Key used for this Dev Test Lab.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.devtest.GetLabResult.location">
<code class="descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.devtest.GetLabResult.location" title="Permalink to this definition">¶</a></dt>
<dd><p>The Azure location where the Dev Test Lab exists.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.devtest.GetLabResult.premium_data_disk_storage_account_id">
<code class="descname">premium_data_disk_storage_account_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.devtest.GetLabResult.premium_data_disk_storage_account_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Storage Account used for Storage of Premium Data Disk.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.devtest.GetLabResult.storage_type">
<code class="descname">storage_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.devtest.GetLabResult.storage_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of storage used by the Dev Test Lab.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.devtest.GetLabResult.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.devtest.GetLabResult.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.devtest.GetLabResult.unique_identifier">
<code class="descname">unique_identifier</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.devtest.GetLabResult.unique_identifier" title="Permalink to this definition">¶</a></dt>
<dd><p>The unique immutable identifier of the Dev Test Lab.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.devtest.GetLabResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.devtest.GetLabResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azure.devtest.Lab">
<em class="property">class </em><code class="descclassname">pulumi_azure.devtest.</code><code class="descname">Lab</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>location=None</em>, <em>name=None</em>, <em>resource_group_name=None</em>, <em>storage_type=None</em>, <em>tags=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.devtest.Lab" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Dev Test Lab.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the Dev Test Lab should exist. Changing this forces a new resource to be created.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Dev Test Lab. Changing this forces a new resource to be created.</li>
<li><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group under which the Dev Test Lab resource has to be created. Changing this forces a new resource to be created.</li>
<li><strong>storage_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of storage used by the Dev Test Lab. Possible values are <code class="docutils literal notranslate"><span class="pre">Standard</span></code> and <code class="docutils literal notranslate"><span class="pre">Premium</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">Premium</span></code>. Changing this forces a new resource to be created.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/dev_test_lab.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/dev_test_lab.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_azure.devtest.Lab.artifacts_storage_account_id">
<code class="descname">artifacts_storage_account_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.devtest.Lab.artifacts_storage_account_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Storage Account used for Artifact Storage.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.devtest.Lab.default_premium_storage_account_id">
<code class="descname">default_premium_storage_account_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.devtest.Lab.default_premium_storage_account_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Default Premium Storage Account for this Dev Test Lab.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.devtest.Lab.default_storage_account_id">
<code class="descname">default_storage_account_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.devtest.Lab.default_storage_account_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Default Storage Account for this Dev Test Lab.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.devtest.Lab.key_vault_id">
<code class="descname">key_vault_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.devtest.Lab.key_vault_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Key used for this Dev Test Lab.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.devtest.Lab.location">
<code class="descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.devtest.Lab.location" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the supported Azure location where the Dev Test Lab should exist. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.devtest.Lab.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.devtest.Lab.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Dev Test Lab. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.devtest.Lab.premium_data_disk_storage_account_id">
<code class="descname">premium_data_disk_storage_account_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.devtest.Lab.premium_data_disk_storage_account_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Storage Account used for Storage of Premium Data Disk.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.devtest.Lab.resource_group_name">
<code class="descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.devtest.Lab.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group under which the Dev Test Lab resource has to be created. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.devtest.Lab.storage_type">
<code class="descname">storage_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.devtest.Lab.storage_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of storage used by the Dev Test Lab. Possible values are <code class="docutils literal notranslate"><span class="pre">Standard</span></code> and <code class="docutils literal notranslate"><span class="pre">Premium</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">Premium</span></code>. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.devtest.Lab.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.devtest.Lab.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.devtest.Lab.unique_identifier">
<code class="descname">unique_identifier</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.devtest.Lab.unique_identifier" title="Permalink to this definition">¶</a></dt>
<dd><p>The unique immutable identifier of the Dev Test Lab.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.devtest.Lab.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.devtest.Lab.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.devtest.Lab.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.devtest.Lab.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.devtest.LinuxVirtualMachine">
<em class="property">class </em><code class="descclassname">pulumi_azure.devtest.</code><code class="descname">LinuxVirtualMachine</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>allow_claim=None</em>, <em>disallow_public_ip_address=None</em>, <em>gallery_image_reference=None</em>, <em>inbound_nat_rules=None</em>, <em>lab_name=None</em>, <em>lab_subnet_name=None</em>, <em>lab_virtual_network_id=None</em>, <em>location=None</em>, <em>name=None</em>, <em>notes=None</em>, <em>password=None</em>, <em>resource_group_name=None</em>, <em>size=None</em>, <em>ssh_key=None</em>, <em>storage_type=None</em>, <em>tags=None</em>, <em>username=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.devtest.LinuxVirtualMachine" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Linux Virtual Machine within a Dev Test Lab.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>allow_claim</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Can this Virtual Machine be claimed by users? Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</li>
<li><strong>disallow_public_ip_address</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Should the Virtual Machine be created without a Public IP Address? Changing this forces a new resource to be created.</li>
<li><strong>gallery_image_reference</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">gallery_image_reference</span></code> block as defined below.</li>
<li><strong>inbound_nat_rules</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">inbound_nat_rule</span></code> blocks as defined below. Changing this forces a new resource to be created.</li>
<li><strong>lab_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Dev Test Lab in which the Virtual Machine should be created. Changing this forces a new resource to be created.</li>
<li><strong>lab_subnet_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of a Subnet within the Dev Test Virtual Network where this machine should exist. Changing this forces a new resource to be created.</li>
<li><strong>lab_virtual_network_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Dev Test Virtual Network where this Virtual Machine should be created. Changing this forces a new resource to be created.</li>
<li><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the Dev Test Lab exists. Changing this forces a new resource to be created.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Dev Test Machine. Changing this forces a new resource to be created.</li>
<li><strong>notes</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Any notes about the Virtual Machine.</li>
<li><strong>password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Password associated with the <code class="docutils literal notranslate"><span class="pre">username</span></code> used to login to this Virtual Machine. Changing this forces a new resource to be created.</li>
<li><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which the Dev Test Lab resource exists. Changing this forces a new resource to be created.</li>
<li><strong>size</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Machine Size to use for this Virtual Machine, such as <code class="docutils literal notranslate"><span class="pre">Standard_F2</span></code>. Changing this forces a new resource to be created.</li>
<li><strong>ssh_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The SSH Key associated with the <code class="docutils literal notranslate"><span class="pre">username</span></code> used to login to this Virtual Machine. Changing this forces a new resource to be created.</li>
<li><strong>storage_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of Storage to use on this Virtual Machine. Possible values are <code class="docutils literal notranslate"><span class="pre">Standard</span></code> and <code class="docutils literal notranslate"><span class="pre">Premium</span></code>.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</li>
<li><strong>username</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Username associated with the local administrator on this Virtual Machine. Changing this forces a new resource to be created.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/dev_test_linux_virtual_machine.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/dev_test_linux_virtual_machine.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_azure.devtest.LinuxVirtualMachine.allow_claim">
<code class="descname">allow_claim</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.devtest.LinuxVirtualMachine.allow_claim" title="Permalink to this definition">¶</a></dt>
<dd><p>Can this Virtual Machine be claimed by users? Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.devtest.LinuxVirtualMachine.disallow_public_ip_address">
<code class="descname">disallow_public_ip_address</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.devtest.LinuxVirtualMachine.disallow_public_ip_address" title="Permalink to this definition">¶</a></dt>
<dd><p>Should the Virtual Machine be created without a Public IP Address? Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.devtest.LinuxVirtualMachine.fqdn">
<code class="descname">fqdn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.devtest.LinuxVirtualMachine.fqdn" title="Permalink to this definition">¶</a></dt>
<dd><p>The FQDN of the Virtual Machine.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.devtest.LinuxVirtualMachine.gallery_image_reference">
<code class="descname">gallery_image_reference</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.devtest.LinuxVirtualMachine.gallery_image_reference" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">gallery_image_reference</span></code> block as defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.devtest.LinuxVirtualMachine.inbound_nat_rules">
<code class="descname">inbound_nat_rules</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.devtest.LinuxVirtualMachine.inbound_nat_rules" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more <code class="docutils literal notranslate"><span class="pre">inbound_nat_rule</span></code> blocks as defined below. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.devtest.LinuxVirtualMachine.lab_name">
<code class="descname">lab_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.devtest.LinuxVirtualMachine.lab_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Dev Test Lab in which the Virtual Machine should be created. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.devtest.LinuxVirtualMachine.lab_subnet_name">
<code class="descname">lab_subnet_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.devtest.LinuxVirtualMachine.lab_subnet_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of a Subnet within the Dev Test Virtual Network where this machine should exist. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.devtest.LinuxVirtualMachine.lab_virtual_network_id">
<code class="descname">lab_virtual_network_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.devtest.LinuxVirtualMachine.lab_virtual_network_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Dev Test Virtual Network where this Virtual Machine should be created. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.devtest.LinuxVirtualMachine.location">
<code class="descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.devtest.LinuxVirtualMachine.location" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the supported Azure location where the Dev Test Lab exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.devtest.LinuxVirtualMachine.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.devtest.LinuxVirtualMachine.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Dev Test Machine. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.devtest.LinuxVirtualMachine.notes">
<code class="descname">notes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.devtest.LinuxVirtualMachine.notes" title="Permalink to this definition">¶</a></dt>
<dd><p>Any notes about the Virtual Machine.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.devtest.LinuxVirtualMachine.password">
<code class="descname">password</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.devtest.LinuxVirtualMachine.password" title="Permalink to this definition">¶</a></dt>
<dd><p>The Password associated with the <code class="docutils literal notranslate"><span class="pre">username</span></code> used to login to this Virtual Machine. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.devtest.LinuxVirtualMachine.resource_group_name">
<code class="descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.devtest.LinuxVirtualMachine.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which the Dev Test Lab resource exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.devtest.LinuxVirtualMachine.size">
<code class="descname">size</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.devtest.LinuxVirtualMachine.size" title="Permalink to this definition">¶</a></dt>
<dd><p>The Machine Size to use for this Virtual Machine, such as <code class="docutils literal notranslate"><span class="pre">Standard_F2</span></code>. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.devtest.LinuxVirtualMachine.ssh_key">
<code class="descname">ssh_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.devtest.LinuxVirtualMachine.ssh_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The SSH Key associated with the <code class="docutils literal notranslate"><span class="pre">username</span></code> used to login to this Virtual Machine. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.devtest.LinuxVirtualMachine.storage_type">
<code class="descname">storage_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.devtest.LinuxVirtualMachine.storage_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of Storage to use on this Virtual Machine. Possible values are <code class="docutils literal notranslate"><span class="pre">Standard</span></code> and <code class="docutils literal notranslate"><span class="pre">Premium</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.devtest.LinuxVirtualMachine.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.devtest.LinuxVirtualMachine.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.devtest.LinuxVirtualMachine.unique_identifier">
<code class="descname">unique_identifier</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.devtest.LinuxVirtualMachine.unique_identifier" title="Permalink to this definition">¶</a></dt>
<dd><p>The unique immutable identifier of the Virtual Machine.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.devtest.LinuxVirtualMachine.username">
<code class="descname">username</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.devtest.LinuxVirtualMachine.username" title="Permalink to this definition">¶</a></dt>
<dd><p>The Username associated with the local administrator on this Virtual Machine. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.devtest.LinuxVirtualMachine.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.devtest.LinuxVirtualMachine.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.devtest.LinuxVirtualMachine.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.devtest.LinuxVirtualMachine.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.devtest.Policy">
<em class="property">class </em><code class="descclassname">pulumi_azure.devtest.</code><code class="descname">Policy</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>description=None</em>, <em>evaluator_type=None</em>, <em>fact_data=None</em>, <em>lab_name=None</em>, <em>name=None</em>, <em>policy_set_name=None</em>, <em>resource_group_name=None</em>, <em>tags=None</em>, <em>threshold=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.devtest.Policy" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Policy within a Dev Test Policy Set.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A description for the Policy.</li>
<li><strong>evaluator_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Evaluation Type used for this Policy. Possible values include: ‘AllowedValuesPolicy’, ‘MaxValuePolicy’. Changing this forces a new resource to be created.</li>
<li><strong>fact_data</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Fact Data for this Policy.</li>
<li><strong>lab_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Dev Test Lab in which the Policy should be created. Changing this forces a new resource to be created.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Dev Test Policy. Possible values are <code class="docutils literal notranslate"><span class="pre">GalleryImage</span></code>, <code class="docutils literal notranslate"><span class="pre">LabPremiumVmCount</span></code>, <code class="docutils literal notranslate"><span class="pre">LabTargetCost</span></code>, <code class="docutils literal notranslate"><span class="pre">LabVmCount</span></code>, <code class="docutils literal notranslate"><span class="pre">LabVmSize</span></code>, <code class="docutils literal notranslate"><span class="pre">UserOwnedLabPremiumVmCount</span></code>, <code class="docutils literal notranslate"><span class="pre">UserOwnedLabVmCount</span></code> and <code class="docutils literal notranslate"><span class="pre">UserOwnedLabVmCountInSubnet</span></code>. Changing this forces a new resource to be created.</li>
<li><strong>policy_set_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Policy Set within the Dev Test Lab where this policy should be created. Changing this forces a new resource to be created.</li>
<li><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which the Dev Test Lab resource exists. Changing this forces a new resource to be created.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</li>
<li><strong>threshold</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Threshold for this Policy.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/dev_test_policy.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/dev_test_policy.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_azure.devtest.Policy.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.devtest.Policy.description" title="Permalink to this definition">¶</a></dt>
<dd><p>A description for the Policy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.devtest.Policy.evaluator_type">
<code class="descname">evaluator_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.devtest.Policy.evaluator_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The Evaluation Type used for this Policy. Possible values include: ‘AllowedValuesPolicy’, ‘MaxValuePolicy’. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.devtest.Policy.fact_data">
<code class="descname">fact_data</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.devtest.Policy.fact_data" title="Permalink to this definition">¶</a></dt>
<dd><p>The Fact Data for this Policy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.devtest.Policy.lab_name">
<code class="descname">lab_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.devtest.Policy.lab_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Dev Test Lab in which the Policy should be created. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.devtest.Policy.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.devtest.Policy.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Dev Test Policy. Possible values are <code class="docutils literal notranslate"><span class="pre">GalleryImage</span></code>, <code class="docutils literal notranslate"><span class="pre">LabPremiumVmCount</span></code>, <code class="docutils literal notranslate"><span class="pre">LabTargetCost</span></code>, <code class="docutils literal notranslate"><span class="pre">LabVmCount</span></code>, <code class="docutils literal notranslate"><span class="pre">LabVmSize</span></code>, <code class="docutils literal notranslate"><span class="pre">UserOwnedLabPremiumVmCount</span></code>, <code class="docutils literal notranslate"><span class="pre">UserOwnedLabVmCount</span></code> and <code class="docutils literal notranslate"><span class="pre">UserOwnedLabVmCountInSubnet</span></code>. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.devtest.Policy.policy_set_name">
<code class="descname">policy_set_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.devtest.Policy.policy_set_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Policy Set within the Dev Test Lab where this policy should be created. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.devtest.Policy.resource_group_name">
<code class="descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.devtest.Policy.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which the Dev Test Lab resource exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.devtest.Policy.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.devtest.Policy.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.devtest.Policy.threshold">
<code class="descname">threshold</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.devtest.Policy.threshold" title="Permalink to this definition">¶</a></dt>
<dd><p>The Threshold for this Policy.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.devtest.Policy.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.devtest.Policy.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.devtest.Policy.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.devtest.Policy.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.devtest.VirtualNetwork">
<em class="property">class </em><code class="descclassname">pulumi_azure.devtest.</code><code class="descname">VirtualNetwork</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>description=None</em>, <em>lab_name=None</em>, <em>name=None</em>, <em>resource_group_name=None</em>, <em>subnet=None</em>, <em>tags=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.devtest.VirtualNetwork" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Virtual Network within a Dev Test Lab.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A description for the Virtual Network.</li>
<li><strong>lab_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Dev Test Lab in which the Virtual Network should be created. Changing this forces a new resource to be created.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Dev Test Virtual Network. Changing this forces a new resource to be created.</li>
<li><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which the Dev Test Lab resource exists. Changing this forces a new resource to be created.</li>
<li><strong>subnet</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">subnet</span></code> block as defined below.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/dev_test_virtual_network.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/dev_test_virtual_network.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_azure.devtest.VirtualNetwork.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.devtest.VirtualNetwork.description" title="Permalink to this definition">¶</a></dt>
<dd><p>A description for the Virtual Network.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.devtest.VirtualNetwork.lab_name">
<code class="descname">lab_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.devtest.VirtualNetwork.lab_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Dev Test Lab in which the Virtual Network should be created. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.devtest.VirtualNetwork.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.devtest.VirtualNetwork.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Dev Test Virtual Network. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.devtest.VirtualNetwork.resource_group_name">
<code class="descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.devtest.VirtualNetwork.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which the Dev Test Lab resource exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.devtest.VirtualNetwork.subnet">
<code class="descname">subnet</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.devtest.VirtualNetwork.subnet" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">subnet</span></code> block as defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.devtest.VirtualNetwork.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.devtest.VirtualNetwork.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.devtest.VirtualNetwork.unique_identifier">
<code class="descname">unique_identifier</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.devtest.VirtualNetwork.unique_identifier" title="Permalink to this definition">¶</a></dt>
<dd><p>The unique immutable identifier of the Dev Test Virtual Network.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.devtest.VirtualNetwork.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.devtest.VirtualNetwork.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.devtest.VirtualNetwork.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.devtest.VirtualNetwork.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.devtest.WindowsVirtualMachine">
<em class="property">class </em><code class="descclassname">pulumi_azure.devtest.</code><code class="descname">WindowsVirtualMachine</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>allow_claim=None</em>, <em>disallow_public_ip_address=None</em>, <em>gallery_image_reference=None</em>, <em>inbound_nat_rules=None</em>, <em>lab_name=None</em>, <em>lab_subnet_name=None</em>, <em>lab_virtual_network_id=None</em>, <em>location=None</em>, <em>name=None</em>, <em>notes=None</em>, <em>password=None</em>, <em>resource_group_name=None</em>, <em>size=None</em>, <em>storage_type=None</em>, <em>tags=None</em>, <em>username=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.devtest.WindowsVirtualMachine" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Windows Virtual Machine within a Dev Test Lab.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>allow_claim</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Can this Virtual Machine be claimed by users? Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</li>
<li><strong>disallow_public_ip_address</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Should the Virtual Machine be created without a Public IP Address? Changing this forces a new resource to be created.</li>
<li><strong>gallery_image_reference</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">gallery_image_reference</span></code> block as defined below.</li>
<li><strong>inbound_nat_rules</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">inbound_nat_rule</span></code> blocks as defined below. Changing this forces a new resource to be created.</li>
<li><strong>lab_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Dev Test Lab in which the Virtual Machine should be created. Changing this forces a new resource to be created.</li>
<li><strong>lab_subnet_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of a Subnet within the Dev Test Virtual Network where this machine should exist. Changing this forces a new resource to be created.</li>
<li><strong>lab_virtual_network_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Dev Test Virtual Network where this Virtual Machine should be created. Changing this forces a new resource to be created.</li>
<li><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the Dev Test Lab exists. Changing this forces a new resource to be created.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Dev Test Machine. Changing this forces a new resource to be created.</li>
<li><strong>notes</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Any notes about the Virtual Machine.</li>
<li><strong>password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Password associated with the <code class="docutils literal notranslate"><span class="pre">username</span></code> used to login to this Virtual Machine. Changing this forces a new resource to be created.</li>
<li><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which the Dev Test Lab resource exists. Changing this forces a new resource to be created.</li>
<li><strong>size</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Machine Size to use for this Virtual Machine, such as <code class="docutils literal notranslate"><span class="pre">Standard_F2</span></code>. Changing this forces a new resource to be created.</li>
<li><strong>storage_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of Storage to use on this Virtual Machine. Possible values are <code class="docutils literal notranslate"><span class="pre">Standard</span></code> and <code class="docutils literal notranslate"><span class="pre">Premium</span></code>.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</li>
<li><strong>username</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Username associated with the local administrator on this Virtual Machine. Changing this forces a new resource to be created.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/dev_test_windows_virtual_machine.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/dev_test_windows_virtual_machine.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_azure.devtest.WindowsVirtualMachine.allow_claim">
<code class="descname">allow_claim</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.devtest.WindowsVirtualMachine.allow_claim" title="Permalink to this definition">¶</a></dt>
<dd><p>Can this Virtual Machine be claimed by users? Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.devtest.WindowsVirtualMachine.disallow_public_ip_address">
<code class="descname">disallow_public_ip_address</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.devtest.WindowsVirtualMachine.disallow_public_ip_address" title="Permalink to this definition">¶</a></dt>
<dd><p>Should the Virtual Machine be created without a Public IP Address? Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.devtest.WindowsVirtualMachine.fqdn">
<code class="descname">fqdn</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.devtest.WindowsVirtualMachine.fqdn" title="Permalink to this definition">¶</a></dt>
<dd><p>The FQDN of the Virtual Machine.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.devtest.WindowsVirtualMachine.gallery_image_reference">
<code class="descname">gallery_image_reference</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.devtest.WindowsVirtualMachine.gallery_image_reference" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">gallery_image_reference</span></code> block as defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.devtest.WindowsVirtualMachine.inbound_nat_rules">
<code class="descname">inbound_nat_rules</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.devtest.WindowsVirtualMachine.inbound_nat_rules" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more <code class="docutils literal notranslate"><span class="pre">inbound_nat_rule</span></code> blocks as defined below. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.devtest.WindowsVirtualMachine.lab_name">
<code class="descname">lab_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.devtest.WindowsVirtualMachine.lab_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Dev Test Lab in which the Virtual Machine should be created. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.devtest.WindowsVirtualMachine.lab_subnet_name">
<code class="descname">lab_subnet_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.devtest.WindowsVirtualMachine.lab_subnet_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of a Subnet within the Dev Test Virtual Network where this machine should exist. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.devtest.WindowsVirtualMachine.lab_virtual_network_id">
<code class="descname">lab_virtual_network_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.devtest.WindowsVirtualMachine.lab_virtual_network_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Dev Test Virtual Network where this Virtual Machine should be created. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.devtest.WindowsVirtualMachine.location">
<code class="descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.devtest.WindowsVirtualMachine.location" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the supported Azure location where the Dev Test Lab exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.devtest.WindowsVirtualMachine.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.devtest.WindowsVirtualMachine.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Dev Test Machine. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.devtest.WindowsVirtualMachine.notes">
<code class="descname">notes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.devtest.WindowsVirtualMachine.notes" title="Permalink to this definition">¶</a></dt>
<dd><p>Any notes about the Virtual Machine.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.devtest.WindowsVirtualMachine.password">
<code class="descname">password</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.devtest.WindowsVirtualMachine.password" title="Permalink to this definition">¶</a></dt>
<dd><p>The Password associated with the <code class="docutils literal notranslate"><span class="pre">username</span></code> used to login to this Virtual Machine. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.devtest.WindowsVirtualMachine.resource_group_name">
<code class="descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.devtest.WindowsVirtualMachine.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which the Dev Test Lab resource exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.devtest.WindowsVirtualMachine.size">
<code class="descname">size</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.devtest.WindowsVirtualMachine.size" title="Permalink to this definition">¶</a></dt>
<dd><p>The Machine Size to use for this Virtual Machine, such as <code class="docutils literal notranslate"><span class="pre">Standard_F2</span></code>. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.devtest.WindowsVirtualMachine.storage_type">
<code class="descname">storage_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.devtest.WindowsVirtualMachine.storage_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of Storage to use on this Virtual Machine. Possible values are <code class="docutils literal notranslate"><span class="pre">Standard</span></code> and <code class="docutils literal notranslate"><span class="pre">Premium</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.devtest.WindowsVirtualMachine.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.devtest.WindowsVirtualMachine.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.devtest.WindowsVirtualMachine.unique_identifier">
<code class="descname">unique_identifier</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.devtest.WindowsVirtualMachine.unique_identifier" title="Permalink to this definition">¶</a></dt>
<dd><p>The unique immutable identifier of the Virtual Machine.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.devtest.WindowsVirtualMachine.username">
<code class="descname">username</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.devtest.WindowsVirtualMachine.username" title="Permalink to this definition">¶</a></dt>
<dd><p>The Username associated with the local administrator on this Virtual Machine. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.devtest.WindowsVirtualMachine.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.devtest.WindowsVirtualMachine.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.devtest.WindowsVirtualMachine.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.devtest.WindowsVirtualMachine.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.devtest.get_lab">
<code class="descclassname">pulumi_azure.devtest.</code><code class="descname">get_lab</code><span class="sig-paren">(</span><em>name=None</em>, <em>resource_group_name=None</em>, <em>opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.devtest.get_lab" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing Dev Test Lab.</p>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/dev_test_lab.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/dev_test_lab.html.markdown</a>.</div></blockquote>
</dd></dl>

</div>
