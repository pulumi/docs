<div class="section" id="module-pulumi_azure.compute">
<span id="compute"></span><h1>compute<a class="headerlink" href="#module-pulumi_azure.compute" title="Permalink to this headline">¶</a></h1>
<dl class="class">
<dt id="pulumi_azure.compute.AvailabilitySet">
<em class="property">class </em><code class="descclassname">pulumi_azure.compute.</code><code class="descname">AvailabilitySet</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>location=None</em>, <em>managed=None</em>, <em>name=None</em>, <em>platform_fault_domain_count=None</em>, <em>platform_update_domain_count=None</em>, <em>resource_group_name=None</em>, <em>tags=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.compute.AvailabilitySet" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an availability set for virtual machines.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</li>
<li><strong>managed</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specifies whether the availability set is managed or not. Possible values are <code class="docutils literal notranslate"><span class="pre">true</span></code> (to specify aligned) or <code class="docutils literal notranslate"><span class="pre">false</span></code> (to specify classic). Default is <code class="docutils literal notranslate"><span class="pre">false</span></code>.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the availability set. Changing this forces a new resource to be created.</li>
<li><strong>platform_fault_domain_count</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Specifies the number of fault domains that are used. Defaults to 3.</li>
<li><strong>platform_update_domain_count</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Specifies the number of update domains that are used. Defaults to 5.</li>
<li><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the availability set. Changing this forces a new resource to be created.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_azure.compute.AvailabilitySet.location">
<code class="descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.AvailabilitySet.location" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.AvailabilitySet.managed">
<code class="descname">managed</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.AvailabilitySet.managed" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies whether the availability set is managed or not. Possible values are <code class="docutils literal notranslate"><span class="pre">true</span></code> (to specify aligned) or <code class="docutils literal notranslate"><span class="pre">false</span></code> (to specify classic). Default is <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.AvailabilitySet.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.AvailabilitySet.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the availability set. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.AvailabilitySet.platform_fault_domain_count">
<code class="descname">platform_fault_domain_count</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.AvailabilitySet.platform_fault_domain_count" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the number of fault domains that are used. Defaults to 3.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.AvailabilitySet.platform_update_domain_count">
<code class="descname">platform_update_domain_count</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.AvailabilitySet.platform_update_domain_count" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the number of update domains that are used. Defaults to 5.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.AvailabilitySet.resource_group_name">
<code class="descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.AvailabilitySet.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to create the availability set. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.AvailabilitySet.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.AvailabilitySet.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.compute.AvailabilitySet.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.compute.AvailabilitySet.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.compute.AvailabilitySet.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.compute.AvailabilitySet.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.compute.DataDiskAttachment">
<em class="property">class </em><code class="descclassname">pulumi_azure.compute.</code><code class="descname">DataDiskAttachment</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>caching=None</em>, <em>create_option=None</em>, <em>lun=None</em>, <em>managed_disk_id=None</em>, <em>virtual_machine_id=None</em>, <em>write_accelerator_enabled=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.compute.DataDiskAttachment" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages attaching a Disk to a Virtual Machine.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Data Disks can be attached either directly on the <code class="docutils literal notranslate"><span class="pre">azurerm_virtual_machine</span></code> resource, or using the <code class="docutils literal notranslate"><span class="pre">azurerm_virtual_machine_data_disk_attachment</span></code> resource - but the two cannot be used together. If both are used against the same Virtual Machine, spurious changes will occur.</p>
<p><strong>Please Note:</strong> only Managed Disks are supported via this separate resource, Unmanaged Disks can be attached using the <code class="docutils literal notranslate"><span class="pre">storage_data_disk</span></code> block in the <code class="docutils literal notranslate"><span class="pre">azurerm_virtual_machine</span></code> resource.</p>
</div></blockquote>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>caching</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the caching requirements for this Data Disk. Possible values include <code class="docutils literal notranslate"><span class="pre">None</span></code>, <code class="docutils literal notranslate"><span class="pre">ReadOnly</span></code> and <code class="docutils literal notranslate"><span class="pre">ReadWrite</span></code>.</li>
<li><strong>create_option</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Create Option of the Data Disk, such as <code class="docutils literal notranslate"><span class="pre">Empty</span></code> or <code class="docutils literal notranslate"><span class="pre">Attach</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">Attach</span></code>. Changing this forces a new resource to be created.</li>
<li><strong>lun</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The Logical Unit Number of the Data Disk, which needs to be unique within the Virtual Machine. Changing this forces a new resource to be created.</li>
<li><strong>managed_disk_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of an existing Managed Disk which should be attached. Changing this forces a new resource to be created.</li>
<li><strong>virtual_machine_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Virtual Machine to which the Data Disk should be attached. Changing this forces a new resource to be created.</li>
<li><strong>write_accelerator_enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specifies if Write Accelerator is enabled on the disk. This can only be enabled on <code class="docutils literal notranslate"><span class="pre">Premium_LRS</span></code> managed disks with no caching and <a class="reference external" href="https://docs.microsoft.com/en-us/azure/virtual-machines/workloads/sap/how-to-enable-write-accelerator">M-Series VMs</a>. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_azure.compute.DataDiskAttachment.caching">
<code class="descname">caching</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.DataDiskAttachment.caching" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the caching requirements for this Data Disk. Possible values include <code class="docutils literal notranslate"><span class="pre">None</span></code>, <code class="docutils literal notranslate"><span class="pre">ReadOnly</span></code> and <code class="docutils literal notranslate"><span class="pre">ReadWrite</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.DataDiskAttachment.create_option">
<code class="descname">create_option</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.DataDiskAttachment.create_option" title="Permalink to this definition">¶</a></dt>
<dd><p>The Create Option of the Data Disk, such as <code class="docutils literal notranslate"><span class="pre">Empty</span></code> or <code class="docutils literal notranslate"><span class="pre">Attach</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">Attach</span></code>. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.DataDiskAttachment.lun">
<code class="descname">lun</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.DataDiskAttachment.lun" title="Permalink to this definition">¶</a></dt>
<dd><p>The Logical Unit Number of the Data Disk, which needs to be unique within the Virtual Machine. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.DataDiskAttachment.managed_disk_id">
<code class="descname">managed_disk_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.DataDiskAttachment.managed_disk_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of an existing Managed Disk which should be attached. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.DataDiskAttachment.virtual_machine_id">
<code class="descname">virtual_machine_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.DataDiskAttachment.virtual_machine_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Virtual Machine to which the Data Disk should be attached. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.DataDiskAttachment.write_accelerator_enabled">
<code class="descname">write_accelerator_enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.DataDiskAttachment.write_accelerator_enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies if Write Accelerator is enabled on the disk. This can only be enabled on <code class="docutils literal notranslate"><span class="pre">Premium_LRS</span></code> managed disks with no caching and <a class="reference external" href="https://docs.microsoft.com/en-us/azure/virtual-machines/workloads/sap/how-to-enable-write-accelerator">M-Series VMs</a>. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.compute.DataDiskAttachment.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.compute.DataDiskAttachment.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.compute.DataDiskAttachment.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.compute.DataDiskAttachment.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.compute.Extension">
<em class="property">class </em><code class="descclassname">pulumi_azure.compute.</code><code class="descname">Extension</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>auto_upgrade_minor_version=None</em>, <em>location=None</em>, <em>name=None</em>, <em>protected_settings=None</em>, <em>publisher=None</em>, <em>resource_group_name=None</em>, <em>settings=None</em>, <em>tags=None</em>, <em>type=None</em>, <em>type_handler_version=None</em>, <em>virtual_machine_name=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.compute.Extension" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Virtual Machine Extension to provide post deployment configuration
and run automated tasks.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Custom Script Extensions for Linux &amp; Windows require that the <code class="docutils literal notranslate"><span class="pre">commandToExecute</span></code> returns a <code class="docutils literal notranslate"><span class="pre">0</span></code> exit code to be classified as successfully deployed. You can achieve this by appending <code class="docutils literal notranslate"><span class="pre">exit</span> <span class="pre">0</span></code> to the end of your <code class="docutils literal notranslate"><span class="pre">commandToExecute</span></code>.</p>
<p><strong>NOTE:</strong> Custom Script Extensions require that the Azure Virtual Machine Guest Agent is running on the Virtual Machine.</p>
</div></blockquote>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>auto_upgrade_minor_version</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specifies if the platform deploys
the latest minor version update to the <code class="docutils literal notranslate"><span class="pre">type_handler_version</span></code> specified.</li>
<li><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The location where the extension is created. Changing
this forces a new resource to be created.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the virtual machine extension peering. Changing
this forces a new resource to be created.</li>
<li><strong>protected_settings</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The protected_settings passed to the
extension, like settings, these are specified as a JSON object in a string.</li>
<li><strong>publisher</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The publisher of the extension, available publishers
can be found by using the Azure CLI.</li>
<li><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to
create the virtual network. Changing this forces a new resource to be
created.</li>
<li><strong>settings</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The settings passed to the extension, these are
specified as a JSON object in a string.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</li>
<li><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of extension, available types for a publisher can
be found using the Azure CLI.</li>
<li><strong>type_handler_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the version of the extension to
use, available versions can be found using the Azure CLI.</li>
<li><strong>virtual_machine_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the virtual machine. Changing
this forces a new resource to be created.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_azure.compute.Extension.auto_upgrade_minor_version">
<code class="descname">auto_upgrade_minor_version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.Extension.auto_upgrade_minor_version" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies if the platform deploys
the latest minor version update to the <code class="docutils literal notranslate"><span class="pre">type_handler_version</span></code> specified.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.Extension.location">
<code class="descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.Extension.location" title="Permalink to this definition">¶</a></dt>
<dd><p>The location where the extension is created. Changing
this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.Extension.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.Extension.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the virtual machine extension peering. Changing
this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.Extension.protected_settings">
<code class="descname">protected_settings</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.Extension.protected_settings" title="Permalink to this definition">¶</a></dt>
<dd><p>The protected_settings passed to the
extension, like settings, these are specified as a JSON object in a string.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.Extension.publisher">
<code class="descname">publisher</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.Extension.publisher" title="Permalink to this definition">¶</a></dt>
<dd><p>The publisher of the extension, available publishers
can be found by using the Azure CLI.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.Extension.resource_group_name">
<code class="descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.Extension.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to
create the virtual network. Changing this forces a new resource to be
created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.Extension.settings">
<code class="descname">settings</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.Extension.settings" title="Permalink to this definition">¶</a></dt>
<dd><p>The settings passed to the extension, these are
specified as a JSON object in a string.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.Extension.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.Extension.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.Extension.type">
<code class="descname">type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.Extension.type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of extension, available types for a publisher can
be found using the Azure CLI.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.Extension.type_handler_version">
<code class="descname">type_handler_version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.Extension.type_handler_version" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the version of the extension to
use, available versions can be found using the Azure CLI.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.Extension.virtual_machine_name">
<code class="descname">virtual_machine_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.Extension.virtual_machine_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the virtual machine. Changing
this forces a new resource to be created.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.compute.Extension.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.compute.Extension.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.compute.Extension.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.compute.Extension.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.compute.GetImageResult">
<em class="property">class </em><code class="descclassname">pulumi_azure.compute.</code><code class="descname">GetImageResult</code><span class="sig-paren">(</span><em>data_disks=None</em>, <em>location=None</em>, <em>os_disks=None</em>, <em>tags=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.compute.GetImageResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getImage.</p>
<dl class="attribute">
<dt id="pulumi_azure.compute.GetImageResult.data_disks">
<code class="descname">data_disks</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.GetImageResult.data_disks" title="Permalink to this definition">¶</a></dt>
<dd><p>a collection of <code class="docutils literal notranslate"><span class="pre">data_disk</span></code> blocks as defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.GetImageResult.location">
<code class="descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.GetImageResult.location" title="Permalink to this definition">¶</a></dt>
<dd><p>the Azure Location where this Image exists.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.GetImageResult.os_disks">
<code class="descname">os_disks</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.GetImageResult.os_disks" title="Permalink to this definition">¶</a></dt>
<dd><p>a <code class="docutils literal notranslate"><span class="pre">os_disk</span></code> block as defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.GetImageResult.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.GetImageResult.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>a mapping of tags to assigned to the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.GetImageResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.GetImageResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azure.compute.GetManagedDiskResult">
<em class="property">class </em><code class="descclassname">pulumi_azure.compute.</code><code class="descname">GetManagedDiskResult</code><span class="sig-paren">(</span><em>create_option=None</em>, <em>disk_size_gb=None</em>, <em>os_type=None</em>, <em>source_resource_id=None</em>, <em>source_uri=None</em>, <em>storage_account_type=None</em>, <em>tags=None</em>, <em>zones=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.compute.GetManagedDiskResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getManagedDisk.</p>
<dl class="attribute">
<dt id="pulumi_azure.compute.GetManagedDiskResult.disk_size_gb">
<code class="descname">disk_size_gb</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.GetManagedDiskResult.disk_size_gb" title="Permalink to this definition">¶</a></dt>
<dd><p>The size of the managed disk in gigabytes.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.GetManagedDiskResult.os_type">
<code class="descname">os_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.GetManagedDiskResult.os_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The operating system for managed disk. Valid values are <code class="docutils literal notranslate"><span class="pre">Linux</span></code> or <code class="docutils literal notranslate"><span class="pre">Windows</span></code></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.GetManagedDiskResult.source_resource_id">
<code class="descname">source_resource_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.GetManagedDiskResult.source_resource_id" title="Permalink to this definition">¶</a></dt>
<dd><p>ID of an existing managed disk that the current resource was created from.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.GetManagedDiskResult.source_uri">
<code class="descname">source_uri</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.GetManagedDiskResult.source_uri" title="Permalink to this definition">¶</a></dt>
<dd><p>The source URI for the managed disk</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.GetManagedDiskResult.storage_account_type">
<code class="descname">storage_account_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.GetManagedDiskResult.storage_account_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The storage account type for the managed disk.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.GetManagedDiskResult.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.GetManagedDiskResult.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags assigned to the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.GetManagedDiskResult.zones">
<code class="descname">zones</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.GetManagedDiskResult.zones" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection containing the availability zone the managed disk is allocated in.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.GetManagedDiskResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.GetManagedDiskResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azure.compute.GetPlatformImageResult">
<em class="property">class </em><code class="descclassname">pulumi_azure.compute.</code><code class="descname">GetPlatformImageResult</code><span class="sig-paren">(</span><em>version=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.compute.GetPlatformImageResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getPlatformImage.</p>
<dl class="attribute">
<dt id="pulumi_azure.compute.GetPlatformImageResult.version">
<code class="descname">version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.GetPlatformImageResult.version" title="Permalink to this definition">¶</a></dt>
<dd><p>The latest version of the Platform Image.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.GetPlatformImageResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.GetPlatformImageResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azure.compute.GetSharedImageGalleryResult">
<em class="property">class </em><code class="descclassname">pulumi_azure.compute.</code><code class="descname">GetSharedImageGalleryResult</code><span class="sig-paren">(</span><em>description=None</em>, <em>location=None</em>, <em>tags=None</em>, <em>unique_name=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.compute.GetSharedImageGalleryResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getSharedImageGallery.</p>
<dl class="attribute">
<dt id="pulumi_azure.compute.GetSharedImageGalleryResult.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.GetSharedImageGalleryResult.description" title="Permalink to this definition">¶</a></dt>
<dd><p>A description for the Shared Image Gallery.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.GetSharedImageGalleryResult.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.GetSharedImageGalleryResult.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags which are assigned to the Shared Image Gallery.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.GetSharedImageGalleryResult.unique_name">
<code class="descname">unique_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.GetSharedImageGalleryResult.unique_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The unique name assigned to the Shared Image Gallery.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.GetSharedImageGalleryResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.GetSharedImageGalleryResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azure.compute.GetSharedImageResult">
<em class="property">class </em><code class="descclassname">pulumi_azure.compute.</code><code class="descname">GetSharedImageResult</code><span class="sig-paren">(</span><em>description=None</em>, <em>eula=None</em>, <em>identifiers=None</em>, <em>location=None</em>, <em>os_type=None</em>, <em>privacy_statement_uri=None</em>, <em>release_note_uri=None</em>, <em>tags=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.compute.GetSharedImageResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getSharedImage.</p>
<dl class="attribute">
<dt id="pulumi_azure.compute.GetSharedImageResult.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.GetSharedImageResult.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description of this Shared Image.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.GetSharedImageResult.eula">
<code class="descname">eula</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.GetSharedImageResult.eula" title="Permalink to this definition">¶</a></dt>
<dd><p>The End User Licence Agreement for the Shared Image.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.GetSharedImageResult.location">
<code class="descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.GetSharedImageResult.location" title="Permalink to this definition">¶</a></dt>
<dd><p>The supported Azure location where the Shared Image Gallery exists.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.GetSharedImageResult.os_type">
<code class="descname">os_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.GetSharedImageResult.os_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of Operating System present in this Shared Image.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.GetSharedImageResult.privacy_statement_uri">
<code class="descname">privacy_statement_uri</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.GetSharedImageResult.privacy_statement_uri" title="Permalink to this definition">¶</a></dt>
<dd><p>The URI containing the Privacy Statement for this Shared Image.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.GetSharedImageResult.release_note_uri">
<code class="descname">release_note_uri</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.GetSharedImageResult.release_note_uri" title="Permalink to this definition">¶</a></dt>
<dd><p>The URI containing the Release Notes for this Shared Image.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.GetSharedImageResult.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.GetSharedImageResult.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags assigned to the Shared Image.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.GetSharedImageResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.GetSharedImageResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azure.compute.GetSharedImageVersionResult">
<em class="property">class </em><code class="descclassname">pulumi_azure.compute.</code><code class="descname">GetSharedImageVersionResult</code><span class="sig-paren">(</span><em>exclude_from_latest=None</em>, <em>location=None</em>, <em>managed_image_id=None</em>, <em>tags=None</em>, <em>target_regions=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.compute.GetSharedImageVersionResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getSharedImageVersion.</p>
<dl class="attribute">
<dt id="pulumi_azure.compute.GetSharedImageVersionResult.exclude_from_latest">
<code class="descname">exclude_from_latest</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.GetSharedImageVersionResult.exclude_from_latest" title="Permalink to this definition">¶</a></dt>
<dd><p>Is this Image Version excluded from the <code class="docutils literal notranslate"><span class="pre">latest</span></code> filter?</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.GetSharedImageVersionResult.location">
<code class="descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.GetSharedImageVersionResult.location" title="Permalink to this definition">¶</a></dt>
<dd><p>The supported Azure location where the Shared Image Gallery exists.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.GetSharedImageVersionResult.managed_image_id">
<code class="descname">managed_image_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.GetSharedImageVersionResult.managed_image_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Managed Image which was the source of this Shared Image Version.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.GetSharedImageVersionResult.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.GetSharedImageVersionResult.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags assigned to the Shared Image.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.GetSharedImageVersionResult.target_regions">
<code class="descname">target_regions</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.GetSharedImageVersionResult.target_regions" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more <code class="docutils literal notranslate"><span class="pre">target_region</span></code> blocks as documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.GetSharedImageVersionResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.GetSharedImageVersionResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azure.compute.GetSnapshotResult">
<em class="property">class </em><code class="descclassname">pulumi_azure.compute.</code><code class="descname">GetSnapshotResult</code><span class="sig-paren">(</span><em>creation_option=None</em>, <em>disk_size_gb=None</em>, <em>encryption_settings=None</em>, <em>os_type=None</em>, <em>source_resource_id=None</em>, <em>source_uri=None</em>, <em>storage_account_id=None</em>, <em>time_created=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.compute.GetSnapshotResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getSnapshot.</p>
<dl class="attribute">
<dt id="pulumi_azure.compute.GetSnapshotResult.disk_size_gb">
<code class="descname">disk_size_gb</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.GetSnapshotResult.disk_size_gb" title="Permalink to this definition">¶</a></dt>
<dd><p>The size of the Snapshotted Disk in GB.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.GetSnapshotResult.source_resource_id">
<code class="descname">source_resource_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.GetSnapshotResult.source_resource_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The reference to an existing snapshot.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.GetSnapshotResult.source_uri">
<code class="descname">source_uri</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.GetSnapshotResult.source_uri" title="Permalink to this definition">¶</a></dt>
<dd><p>The URI to a Managed or Unmanaged Disk.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.GetSnapshotResult.storage_account_id">
<code class="descname">storage_account_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.GetSnapshotResult.storage_account_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of an storage account.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.GetSnapshotResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.GetSnapshotResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azure.compute.GetVirtualMachineResult">
<em class="property">class </em><code class="descclassname">pulumi_azure.compute.</code><code class="descname">GetVirtualMachineResult</code><span class="sig-paren">(</span><em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.compute.GetVirtualMachineResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getVirtualMachine.</p>
<dl class="attribute">
<dt id="pulumi_azure.compute.GetVirtualMachineResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.GetVirtualMachineResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azure.compute.Image">
<em class="property">class </em><code class="descclassname">pulumi_azure.compute.</code><code class="descname">Image</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>data_disks=None</em>, <em>location=None</em>, <em>name=None</em>, <em>os_disk=None</em>, <em>resource_group_name=None</em>, <em>source_virtual_machine_id=None</em>, <em>tags=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.compute.Image" title="Permalink to this definition">¶</a></dt>
<dd><p>Manage a custom virtual machine image that can be used to create virtual machines.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>data_disks</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">data_disk</span></code> elements as defined below.</li>
<li><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specified the supported Azure location where the resource exists.
Changing this forces a new resource to be created.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the image. Changing this forces a
new resource to be created.</li>
<li><strong>os_disk</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">os_disk</span></code> elements as defined below.</li>
<li><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create
the image. Changing this forces a new resource to be created.</li>
<li><strong>source_virtual_machine_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Virtual Machine ID from which to create the image.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_azure.compute.Image.data_disks">
<code class="descname">data_disks</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.Image.data_disks" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more <code class="docutils literal notranslate"><span class="pre">data_disk</span></code> elements as defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.Image.location">
<code class="descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.Image.location" title="Permalink to this definition">¶</a></dt>
<dd><p>Specified the supported Azure location where the resource exists.
Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.Image.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.Image.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the image. Changing this forces a
new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.Image.os_disk">
<code class="descname">os_disk</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.Image.os_disk" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more <code class="docutils literal notranslate"><span class="pre">os_disk</span></code> elements as defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.Image.resource_group_name">
<code class="descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.Image.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to create
the image. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.Image.source_virtual_machine_id">
<code class="descname">source_virtual_machine_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.Image.source_virtual_machine_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The Virtual Machine ID from which to create the image.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.Image.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.Image.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.compute.Image.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.compute.Image.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.compute.Image.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.compute.Image.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.compute.ManagedDisk">
<em class="property">class </em><code class="descclassname">pulumi_azure.compute.</code><code class="descname">ManagedDisk</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>create_option=None</em>, <em>disk_size_gb=None</em>, <em>encryption_settings=None</em>, <em>image_reference_id=None</em>, <em>location=None</em>, <em>name=None</em>, <em>os_type=None</em>, <em>resource_group_name=None</em>, <em>source_resource_id=None</em>, <em>source_uri=None</em>, <em>storage_account_type=None</em>, <em>tags=None</em>, <em>zones=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.compute.ManagedDisk" title="Permalink to this definition">¶</a></dt>
<dd><p>Manage a managed disk.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>create_option</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The method to use when creating the managed disk. Possible values include:</li>
<li><strong>disk_size_gb</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Specifies the size of the managed disk to create in gigabytes.
If <code class="docutils literal notranslate"><span class="pre">create_option</span></code> is <code class="docutils literal notranslate"><span class="pre">Copy</span></code> or <code class="docutils literal notranslate"><span class="pre">FromImage</span></code>, then the value must be equal to or greater than the source’s size.</li>
<li><strong>encryption_settings</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – an <code class="docutils literal notranslate"><span class="pre">encryption_settings</span></code> block as defined below.</li>
<li><strong>image_reference_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – ID of an existing platform/marketplace disk image to copy when <code class="docutils literal notranslate"><span class="pre">create_option</span></code> is <code class="docutils literal notranslate"><span class="pre">FromImage</span></code>.</li>
<li><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specified the supported Azure location where the resource exists.
Changing this forces a new resource to be created.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the managed disk. Changing this forces a
new resource to be created.</li>
<li><strong>os_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specify a value when the source of an <code class="docutils literal notranslate"><span class="pre">Import</span></code> or <code class="docutils literal notranslate"><span class="pre">Copy</span></code>
operation targets a source that contains an operating system. Valid values are <code class="docutils literal notranslate"><span class="pre">Linux</span></code> or <code class="docutils literal notranslate"><span class="pre">Windows</span></code></li>
<li><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create
the managed disk.</li>
<li><strong>source_resource_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – ID of an existing managed disk to copy when <code class="docutils literal notranslate"><span class="pre">create_option</span></code> is <code class="docutils literal notranslate"><span class="pre">Copy</span></code>.</li>
<li><strong>source_uri</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – URI to a valid VHD file to be used when <code class="docutils literal notranslate"><span class="pre">create_option</span></code> is <code class="docutils literal notranslate"><span class="pre">Import</span></code>.</li>
<li><strong>storage_account_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of storage to use for the managed disk.
Allowable values are <code class="docutils literal notranslate"><span class="pre">Standard_LRS</span></code>, <code class="docutils literal notranslate"><span class="pre">Premium_LRS</span></code>, <code class="docutils literal notranslate"><span class="pre">StandardSSD_LRS</span></code> or <code class="docutils literal notranslate"><span class="pre">UltraSSD_LRS</span></code>.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</li>
<li><strong>zones</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A collection containing the availability zone to allocate the Managed Disk in.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_azure.compute.ManagedDisk.create_option">
<code class="descname">create_option</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.ManagedDisk.create_option" title="Permalink to this definition">¶</a></dt>
<dd><p>The method to use when creating the managed disk. Possible values include:</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.ManagedDisk.disk_size_gb">
<code class="descname">disk_size_gb</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.ManagedDisk.disk_size_gb" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the size of the managed disk to create in gigabytes.
If <code class="docutils literal notranslate"><span class="pre">create_option</span></code> is <code class="docutils literal notranslate"><span class="pre">Copy</span></code> or <code class="docutils literal notranslate"><span class="pre">FromImage</span></code>, then the value must be equal to or greater than the source’s size.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.ManagedDisk.encryption_settings">
<code class="descname">encryption_settings</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.ManagedDisk.encryption_settings" title="Permalink to this definition">¶</a></dt>
<dd><p>an <code class="docutils literal notranslate"><span class="pre">encryption_settings</span></code> block as defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.ManagedDisk.image_reference_id">
<code class="descname">image_reference_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.ManagedDisk.image_reference_id" title="Permalink to this definition">¶</a></dt>
<dd><p>ID of an existing platform/marketplace disk image to copy when <code class="docutils literal notranslate"><span class="pre">create_option</span></code> is <code class="docutils literal notranslate"><span class="pre">FromImage</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.ManagedDisk.location">
<code class="descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.ManagedDisk.location" title="Permalink to this definition">¶</a></dt>
<dd><p>Specified the supported Azure location where the resource exists.
Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.ManagedDisk.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.ManagedDisk.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the managed disk. Changing this forces a
new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.ManagedDisk.os_type">
<code class="descname">os_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.ManagedDisk.os_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Specify a value when the source of an <code class="docutils literal notranslate"><span class="pre">Import</span></code> or <code class="docutils literal notranslate"><span class="pre">Copy</span></code>
operation targets a source that contains an operating system. Valid values are <code class="docutils literal notranslate"><span class="pre">Linux</span></code> or <code class="docutils literal notranslate"><span class="pre">Windows</span></code></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.ManagedDisk.resource_group_name">
<code class="descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.ManagedDisk.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to create
the managed disk.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.ManagedDisk.source_resource_id">
<code class="descname">source_resource_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.ManagedDisk.source_resource_id" title="Permalink to this definition">¶</a></dt>
<dd><p>ID of an existing managed disk to copy when <code class="docutils literal notranslate"><span class="pre">create_option</span></code> is <code class="docutils literal notranslate"><span class="pre">Copy</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.ManagedDisk.source_uri">
<code class="descname">source_uri</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.ManagedDisk.source_uri" title="Permalink to this definition">¶</a></dt>
<dd><p>URI to a valid VHD file to be used when <code class="docutils literal notranslate"><span class="pre">create_option</span></code> is <code class="docutils literal notranslate"><span class="pre">Import</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.ManagedDisk.storage_account_type">
<code class="descname">storage_account_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.ManagedDisk.storage_account_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of storage to use for the managed disk.
Allowable values are <code class="docutils literal notranslate"><span class="pre">Standard_LRS</span></code>, <code class="docutils literal notranslate"><span class="pre">Premium_LRS</span></code>, <code class="docutils literal notranslate"><span class="pre">StandardSSD_LRS</span></code> or <code class="docutils literal notranslate"><span class="pre">UltraSSD_LRS</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.ManagedDisk.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.ManagedDisk.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.ManagedDisk.zones">
<code class="descname">zones</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.ManagedDisk.zones" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection containing the availability zone to allocate the Managed Disk in.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.compute.ManagedDisk.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.compute.ManagedDisk.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.compute.ManagedDisk.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.compute.ManagedDisk.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.compute.ScaleSet">
<em class="property">class </em><code class="descclassname">pulumi_azure.compute.</code><code class="descname">ScaleSet</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>automatic_os_upgrade=None</em>, <em>boot_diagnostics=None</em>, <em>eviction_policy=None</em>, <em>extensions=None</em>, <em>health_probe_id=None</em>, <em>identity=None</em>, <em>license_type=None</em>, <em>location=None</em>, <em>name=None</em>, <em>network_profiles=None</em>, <em>os_profile=None</em>, <em>os_profile_linux_config=None</em>, <em>os_profile_secrets=None</em>, <em>os_profile_windows_config=None</em>, <em>overprovision=None</em>, <em>plan=None</em>, <em>priority=None</em>, <em>resource_group_name=None</em>, <em>rolling_upgrade_policy=None</em>, <em>single_placement_group=None</em>, <em>sku=None</em>, <em>storage_profile_data_disks=None</em>, <em>storage_profile_image_reference=None</em>, <em>storage_profile_os_disk=None</em>, <em>tags=None</em>, <em>upgrade_policy_mode=None</em>, <em>zones=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.compute.ScaleSet" title="Permalink to this definition">¶</a></dt>
<dd><p>Manage a virtual machine scale set.</p>
<blockquote>
<div><strong>Note:</strong> All arguments including the administrator login and password will be stored in the raw state as plain-text.
<a class="reference external" href="https://www.terraform.io/docs/state/sensitive-data.html">Read more about sensitive data in state</a>.</div></blockquote>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>automatic_os_upgrade</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Automatic OS patches can be applied by Azure to your scaleset. This is particularly useful when <code class="docutils literal notranslate"><span class="pre">upgrade_policy_mode</span></code> is set to <code class="docutils literal notranslate"><span class="pre">Rolling</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</li>
<li><strong>boot_diagnostics</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A boot diagnostics profile block as referenced below.</li>
<li><strong>eviction_policy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the eviction policy for Virtual Machines in this Scale Set. Possible values are <code class="docutils literal notranslate"><span class="pre">Deallocate</span></code> and <code class="docutils literal notranslate"><span class="pre">Delete</span></code>.</li>
<li><strong>extensions</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Can be specified multiple times to add extension profiles to the scale set. Each <code class="docutils literal notranslate"><span class="pre">extension</span></code> block supports the fields documented below.</li>
<li><strong>health_probe_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the identifier for the load balancer health probe. Required when using <code class="docutils literal notranslate"><span class="pre">Rolling</span></code> as your <code class="docutils literal notranslate"><span class="pre">upgrade_policy_mode</span></code>.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<p>:param pulumi.Input[dict] identity
:param pulumi.Input[str] license_type: Specifies the Windows OS license type. If supplied, the only allowed values are <code class="docutils literal notranslate"><span class="pre">Windows_Client</span></code> and <code class="docutils literal notranslate"><span class="pre">Windows_Server</span></code>.
:param pulumi.Input[str] location: Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.
:param pulumi.Input[str] name: Specifies the name of the image from the marketplace.
:param pulumi.Input[list] network_profiles: A collection of network profile block as documented below.
:param pulumi.Input[dict] os_profile: A Virtual Machine OS Profile block as documented below.
:param pulumi.Input[dict] os_profile_linux_config: A Linux config block as documented below.
:param pulumi.Input[list] os_profile_secrets: A collection of Secret blocks as documented below.
:param pulumi.Input[dict] os_profile_windows_config: A Windows config block as documented below.
:param pulumi.Input[bool] overprovision: Specifies whether the virtual machine scale set should be overprovisioned.
:param pulumi.Input[dict] plan: A plan block as documented below.
:param pulumi.Input[str] priority: Specifies the priority for the Virtual Machines in the Scale Set. Defaults to <code class="docutils literal notranslate"><span class="pre">Regular</span></code>. Possible values are <code class="docutils literal notranslate"><span class="pre">Low</span></code> and <code class="docutils literal notranslate"><span class="pre">Regular</span></code>.
:param pulumi.Input[str] resource_group_name: The name of the resource group in which to create the virtual machine scale set. Changing this forces a new resource to be created.
:param pulumi.Input[dict] rolling_upgrade_policy: A <code class="docutils literal notranslate"><span class="pre">rolling_upgrade_policy</span></code> block as defined below. This is only applicable when the <code class="docutils literal notranslate"><span class="pre">upgrade_policy_mode</span></code> is <code class="docutils literal notranslate"><span class="pre">Rolling</span></code>.
:param pulumi.Input[bool] single_placement_group: Specifies whether the scale set is limited to a single placement group with a maximum size of 100 virtual machines. If set to false, managed disks must be used. Default is true. Changing this forces a new resource to be created. See <a class="reference external" href="http://docs.microsoft.com/en-us/azure/virtual-machine-scale-sets/virtual-machine-scale-sets-placement-groups">documentation</a> for more information.
:param pulumi.Input[dict] sku: Specifies the SKU of the image used to create the virtual machines.
:param pulumi.Input[list] storage_profile_data_disks: A storage profile data disk block as documented below
:param pulumi.Input[dict] storage_profile_image_reference: A storage profile image reference block as documented below.
:param pulumi.Input[dict] storage_profile_os_disk: A storage profile os disk block as documented below
:param pulumi.Input[dict] tags: A mapping of tags to assign to the resource.
:param pulumi.Input[str] upgrade_policy_mode: Specifies the mode of an upgrade to virtual machines in the scale set. Possible values, <code class="docutils literal notranslate"><span class="pre">Rolling</span></code>, <code class="docutils literal notranslate"><span class="pre">Manual</span></code>, or <code class="docutils literal notranslate"><span class="pre">Automatic</span></code>. When choosing <code class="docutils literal notranslate"><span class="pre">Rolling</span></code>, you will need to set a health probe.
:param pulumi.Input[list] zones: A collection of availability zones to spread the Virtual Machines over.</p>
<dl class="attribute">
<dt id="pulumi_azure.compute.ScaleSet.automatic_os_upgrade">
<code class="descname">automatic_os_upgrade</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.ScaleSet.automatic_os_upgrade" title="Permalink to this definition">¶</a></dt>
<dd><p>Automatic OS patches can be applied by Azure to your scaleset. This is particularly useful when <code class="docutils literal notranslate"><span class="pre">upgrade_policy_mode</span></code> is set to <code class="docutils literal notranslate"><span class="pre">Rolling</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.ScaleSet.boot_diagnostics">
<code class="descname">boot_diagnostics</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.ScaleSet.boot_diagnostics" title="Permalink to this definition">¶</a></dt>
<dd><p>A boot diagnostics profile block as referenced below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.ScaleSet.eviction_policy">
<code class="descname">eviction_policy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.ScaleSet.eviction_policy" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the eviction policy for Virtual Machines in this Scale Set. Possible values are <code class="docutils literal notranslate"><span class="pre">Deallocate</span></code> and <code class="docutils literal notranslate"><span class="pre">Delete</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.ScaleSet.extensions">
<code class="descname">extensions</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.ScaleSet.extensions" title="Permalink to this definition">¶</a></dt>
<dd><p>Can be specified multiple times to add extension profiles to the scale set. Each <code class="docutils literal notranslate"><span class="pre">extension</span></code> block supports the fields documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.ScaleSet.health_probe_id">
<code class="descname">health_probe_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.ScaleSet.health_probe_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the identifier for the load balancer health probe. Required when using <code class="docutils literal notranslate"><span class="pre">Rolling</span></code> as your <code class="docutils literal notranslate"><span class="pre">upgrade_policy_mode</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.ScaleSet.license_type">
<code class="descname">license_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.ScaleSet.license_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the Windows OS license type. If supplied, the only allowed values are <code class="docutils literal notranslate"><span class="pre">Windows_Client</span></code> and <code class="docutils literal notranslate"><span class="pre">Windows_Server</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.ScaleSet.location">
<code class="descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.ScaleSet.location" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.ScaleSet.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.ScaleSet.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the image from the marketplace.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.ScaleSet.network_profiles">
<code class="descname">network_profiles</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.ScaleSet.network_profiles" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of network profile block as documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.ScaleSet.os_profile">
<code class="descname">os_profile</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.ScaleSet.os_profile" title="Permalink to this definition">¶</a></dt>
<dd><p>A Virtual Machine OS Profile block as documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.ScaleSet.os_profile_linux_config">
<code class="descname">os_profile_linux_config</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.ScaleSet.os_profile_linux_config" title="Permalink to this definition">¶</a></dt>
<dd><p>A Linux config block as documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.ScaleSet.os_profile_secrets">
<code class="descname">os_profile_secrets</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.ScaleSet.os_profile_secrets" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of Secret blocks as documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.ScaleSet.os_profile_windows_config">
<code class="descname">os_profile_windows_config</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.ScaleSet.os_profile_windows_config" title="Permalink to this definition">¶</a></dt>
<dd><p>A Windows config block as documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.ScaleSet.overprovision">
<code class="descname">overprovision</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.ScaleSet.overprovision" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies whether the virtual machine scale set should be overprovisioned.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.ScaleSet.plan">
<code class="descname">plan</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.ScaleSet.plan" title="Permalink to this definition">¶</a></dt>
<dd><p>A plan block as documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.ScaleSet.priority">
<code class="descname">priority</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.ScaleSet.priority" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the priority for the Virtual Machines in the Scale Set. Defaults to <code class="docutils literal notranslate"><span class="pre">Regular</span></code>. Possible values are <code class="docutils literal notranslate"><span class="pre">Low</span></code> and <code class="docutils literal notranslate"><span class="pre">Regular</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.ScaleSet.resource_group_name">
<code class="descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.ScaleSet.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to create the virtual machine scale set. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.ScaleSet.rolling_upgrade_policy">
<code class="descname">rolling_upgrade_policy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.ScaleSet.rolling_upgrade_policy" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">rolling_upgrade_policy</span></code> block as defined below. This is only applicable when the <code class="docutils literal notranslate"><span class="pre">upgrade_policy_mode</span></code> is <code class="docutils literal notranslate"><span class="pre">Rolling</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.ScaleSet.single_placement_group">
<code class="descname">single_placement_group</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.ScaleSet.single_placement_group" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies whether the scale set is limited to a single placement group with a maximum size of 100 virtual machines. If set to false, managed disks must be used. Default is true. Changing this forces a new resource to be created. See <a class="reference external" href="http://docs.microsoft.com/en-us/azure/virtual-machine-scale-sets/virtual-machine-scale-sets-placement-groups">documentation</a> for more information.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.ScaleSet.sku">
<code class="descname">sku</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.ScaleSet.sku" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the SKU of the image used to create the virtual machines.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.ScaleSet.storage_profile_data_disks">
<code class="descname">storage_profile_data_disks</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.ScaleSet.storage_profile_data_disks" title="Permalink to this definition">¶</a></dt>
<dd><p>A storage profile data disk block as documented below</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.ScaleSet.storage_profile_image_reference">
<code class="descname">storage_profile_image_reference</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.ScaleSet.storage_profile_image_reference" title="Permalink to this definition">¶</a></dt>
<dd><p>A storage profile image reference block as documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.ScaleSet.storage_profile_os_disk">
<code class="descname">storage_profile_os_disk</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.ScaleSet.storage_profile_os_disk" title="Permalink to this definition">¶</a></dt>
<dd><p>A storage profile os disk block as documented below</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.ScaleSet.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.ScaleSet.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.ScaleSet.upgrade_policy_mode">
<code class="descname">upgrade_policy_mode</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.ScaleSet.upgrade_policy_mode" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the mode of an upgrade to virtual machines in the scale set. Possible values, <code class="docutils literal notranslate"><span class="pre">Rolling</span></code>, <code class="docutils literal notranslate"><span class="pre">Manual</span></code>, or <code class="docutils literal notranslate"><span class="pre">Automatic</span></code>. When choosing <code class="docutils literal notranslate"><span class="pre">Rolling</span></code>, you will need to set a health probe.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.ScaleSet.zones">
<code class="descname">zones</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.ScaleSet.zones" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of availability zones to spread the Virtual Machines over.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.compute.ScaleSet.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.compute.ScaleSet.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.compute.ScaleSet.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.compute.ScaleSet.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.compute.SharedImage">
<em class="property">class </em><code class="descclassname">pulumi_azure.compute.</code><code class="descname">SharedImage</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>description=None</em>, <em>eula=None</em>, <em>gallery_name=None</em>, <em>identifier=None</em>, <em>location=None</em>, <em>name=None</em>, <em>os_type=None</em>, <em>privacy_statement_uri=None</em>, <em>release_note_uri=None</em>, <em>resource_group_name=None</em>, <em>tags=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.compute.SharedImage" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Shared Image within a Shared Image Gallery.</p>
<blockquote>
<div><strong>NOTE</strong> Shared Image Galleries are currently in Public Preview. You can find more information, including <a class="reference external" href="https://azure.microsoft.com/en-gb/blog/announcing-the-public-preview-of-shared-image-gallery/">how to register for the Public Preview here</a>.</div></blockquote>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A description of this Shared Image.</li>
<li><strong>eula</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The End User Licence Agreement for the Shared Image.</li>
<li><strong>gallery_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Shared Image Gallery in which this Shared Image should exist. Changing this forces a new resource to be created.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<p>:param pulumi.Input[dict] identifier
:param pulumi.Input[str] location: Specifies the supported Azure location where the Shared Image Gallery exists. Changing this forces a new resource to be created.
:param pulumi.Input[str] name: Specifies the name of the Shared Image. Changing this forces a new resource to be created.
:param pulumi.Input[str] os_type: The type of Operating System present in this Shared Image. Possible values are <code class="docutils literal notranslate"><span class="pre">Linux</span></code> and <code class="docutils literal notranslate"><span class="pre">Windows</span></code>.
:param pulumi.Input[str] privacy_statement_uri: The URI containing the Privacy Statement associated with this Shared Image.
:param pulumi.Input[str] release_note_uri: The URI containing the Release Notes associated with this Shared Image.
:param pulumi.Input[str] resource_group_name: The name of the resource group in which the Shared Image Gallery exists. Changing this forces a new resource to be created.
:param pulumi.Input[dict] tags: A mapping of tags to assign to the Shared Image.</p>
<dl class="attribute">
<dt id="pulumi_azure.compute.SharedImage.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.SharedImage.description" title="Permalink to this definition">¶</a></dt>
<dd><p>A description of this Shared Image.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.SharedImage.eula">
<code class="descname">eula</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.SharedImage.eula" title="Permalink to this definition">¶</a></dt>
<dd><p>The End User Licence Agreement for the Shared Image.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.SharedImage.gallery_name">
<code class="descname">gallery_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.SharedImage.gallery_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Shared Image Gallery in which this Shared Image should exist. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.SharedImage.location">
<code class="descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.SharedImage.location" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the supported Azure location where the Shared Image Gallery exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.SharedImage.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.SharedImage.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Shared Image. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.SharedImage.os_type">
<code class="descname">os_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.SharedImage.os_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of Operating System present in this Shared Image. Possible values are <code class="docutils literal notranslate"><span class="pre">Linux</span></code> and <code class="docutils literal notranslate"><span class="pre">Windows</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.SharedImage.privacy_statement_uri">
<code class="descname">privacy_statement_uri</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.SharedImage.privacy_statement_uri" title="Permalink to this definition">¶</a></dt>
<dd><p>The URI containing the Privacy Statement associated with this Shared Image.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.SharedImage.release_note_uri">
<code class="descname">release_note_uri</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.SharedImage.release_note_uri" title="Permalink to this definition">¶</a></dt>
<dd><p>The URI containing the Release Notes associated with this Shared Image.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.SharedImage.resource_group_name">
<code class="descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.SharedImage.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which the Shared Image Gallery exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.SharedImage.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.SharedImage.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the Shared Image.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.compute.SharedImage.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.compute.SharedImage.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.compute.SharedImage.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.compute.SharedImage.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.compute.SharedImageGallery">
<em class="property">class </em><code class="descclassname">pulumi_azure.compute.</code><code class="descname">SharedImageGallery</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>description=None</em>, <em>location=None</em>, <em>name=None</em>, <em>resource_group_name=None</em>, <em>tags=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.compute.SharedImageGallery" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Shared Image Gallery.</p>
<blockquote>
<div><strong>NOTE</strong> Shared Image Galleries are currently in Public Preview. You can find more information, including <a class="reference external" href="https://azure.microsoft.com/en-gb/blog/announcing-the-public-preview-of-shared-image-gallery/">how to register for the Public Preview here</a>.</div></blockquote>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A description for this Shared Image Gallery.</li>
<li><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Shared Image Gallery. Changing this forces a new resource to be created.</li>
<li><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the Shared Image Gallery. Changing this forces a new resource to be created.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the Shared Image Gallery.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_azure.compute.SharedImageGallery.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.SharedImageGallery.description" title="Permalink to this definition">¶</a></dt>
<dd><p>A description for this Shared Image Gallery.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.SharedImageGallery.location">
<code class="descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.SharedImageGallery.location" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.SharedImageGallery.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.SharedImageGallery.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Shared Image Gallery. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.SharedImageGallery.resource_group_name">
<code class="descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.SharedImageGallery.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to create the Shared Image Gallery. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.SharedImageGallery.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.SharedImageGallery.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the Shared Image Gallery.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.compute.SharedImageGallery.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.compute.SharedImageGallery.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.compute.SharedImageGallery.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.compute.SharedImageGallery.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.compute.SharedImageVersion">
<em class="property">class </em><code class="descclassname">pulumi_azure.compute.</code><code class="descname">SharedImageVersion</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>exclude_from_latest=None</em>, <em>gallery_name=None</em>, <em>image_name=None</em>, <em>location=None</em>, <em>managed_image_id=None</em>, <em>name=None</em>, <em>resource_group_name=None</em>, <em>tags=None</em>, <em>target_regions=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.compute.SharedImageVersion" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Version of a Shared Image within a Shared Image Gallery.</p>
<blockquote>
<div><strong>NOTE</strong> Shared Image Galleries are currently in Public Preview. You can find more information, including <a class="reference external" href="https://azure.microsoft.com/en-gb/blog/announcing-the-public-preview-of-shared-image-gallery/">how to register for the Public Preview here</a>.</div></blockquote>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>exclude_from_latest</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Should this Image Version be excluded from the <code class="docutils literal notranslate"><span class="pre">latest</span></code> filter? If set to <code class="docutils literal notranslate"><span class="pre">true</span></code> this Image Version won’t be returned for the <code class="docutils literal notranslate"><span class="pre">latest</span></code> version. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</li>
<li><strong>gallery_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Shared Image Gallery in which the Shared Image exists. Changing this forces a new resource to be created.</li>
<li><strong>image_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Shared Image within the Shared Image Gallery in which this Version should be created. Changing this forces a new resource to be created.</li>
<li><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Azure Region in which the Shared Image Gallery exists. Changing this forces a new resource to be created.</li>
<li><strong>managed_image_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Managed Image which should be used for this Shared Image Version. Changing this forces a new resource to be created.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The version number for this Image Version, such as <code class="docutils literal notranslate"><span class="pre">1.0.0</span></code>. Changing this forces a new resource to be created.</li>
<li><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Resource Group in which the Shared Image Gallery exists. Changing this forces a new resource to be created.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A collection of tags which should be applied to this resource.</li>
<li><strong>target_regions</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">target_region</span></code> blocks as documented below.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_azure.compute.SharedImageVersion.exclude_from_latest">
<code class="descname">exclude_from_latest</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.SharedImageVersion.exclude_from_latest" title="Permalink to this definition">¶</a></dt>
<dd><p>Should this Image Version be excluded from the <code class="docutils literal notranslate"><span class="pre">latest</span></code> filter? If set to <code class="docutils literal notranslate"><span class="pre">true</span></code> this Image Version won’t be returned for the <code class="docutils literal notranslate"><span class="pre">latest</span></code> version. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.SharedImageVersion.gallery_name">
<code class="descname">gallery_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.SharedImageVersion.gallery_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Shared Image Gallery in which the Shared Image exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.SharedImageVersion.image_name">
<code class="descname">image_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.SharedImageVersion.image_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Shared Image within the Shared Image Gallery in which this Version should be created. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.SharedImageVersion.location">
<code class="descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.SharedImageVersion.location" title="Permalink to this definition">¶</a></dt>
<dd><p>The Azure Region in which the Shared Image Gallery exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.SharedImageVersion.managed_image_id">
<code class="descname">managed_image_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.SharedImageVersion.managed_image_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Managed Image which should be used for this Shared Image Version. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.SharedImageVersion.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.SharedImageVersion.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The version number for this Image Version, such as <code class="docutils literal notranslate"><span class="pre">1.0.0</span></code>. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.SharedImageVersion.resource_group_name">
<code class="descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.SharedImageVersion.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Resource Group in which the Shared Image Gallery exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.SharedImageVersion.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.SharedImageVersion.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of tags which should be applied to this resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.SharedImageVersion.target_regions">
<code class="descname">target_regions</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.SharedImageVersion.target_regions" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more <code class="docutils literal notranslate"><span class="pre">target_region</span></code> blocks as documented below.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.compute.SharedImageVersion.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.compute.SharedImageVersion.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.compute.SharedImageVersion.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.compute.SharedImageVersion.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.compute.Snapshot">
<em class="property">class </em><code class="descclassname">pulumi_azure.compute.</code><code class="descname">Snapshot</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>create_option=None</em>, <em>disk_size_gb=None</em>, <em>encryption_settings=None</em>, <em>location=None</em>, <em>name=None</em>, <em>resource_group_name=None</em>, <em>source_resource_id=None</em>, <em>source_uri=None</em>, <em>storage_account_id=None</em>, <em>tags=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.compute.Snapshot" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Disk Snapshot.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>create_option</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Indicates how the snapshot is to be created. Possible values are <code class="docutils literal notranslate"><span class="pre">Copy</span></code> or <code class="docutils literal notranslate"><span class="pre">Import</span></code>. Changing this forces a new resource to be created.</li>
<li><strong>disk_size_gb</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The size of the Snapshotted Disk in GB.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<p>:param pulumi.Input[dict] encryption_settings
:param pulumi.Input[str] location: Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.
:param pulumi.Input[str] name: Specifies the name of the Snapshot resource. Changing this forces a new resource to be created.
:param pulumi.Input[str] resource_group_name: The name of the resource group in which to create the Snapshot. Changing this forces a new resource to be created.
:param pulumi.Input[str] source_resource_id: Specifies a reference to an existing snapshot, when <code class="docutils literal notranslate"><span class="pre">create_option</span></code> is <code class="docutils literal notranslate"><span class="pre">Copy</span></code>. Changing this forces a new resource to be created.
:param pulumi.Input[str] source_uri: Specifies the URI to a Managed or Unmanaged Disk. Changing this forces a new resource to be created.
:param pulumi.Input[str] storage_account_id: Specifies the ID of an storage account. Used with <code class="docutils literal notranslate"><span class="pre">source_uri</span></code> to allow authorization during import of unmanaged blobs from a different subscription. Changing this forces a new resource to be created.
:param pulumi.Input[dict] tags: A mapping of tags to assign to the resource.</p>
<dl class="attribute">
<dt id="pulumi_azure.compute.Snapshot.create_option">
<code class="descname">create_option</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.Snapshot.create_option" title="Permalink to this definition">¶</a></dt>
<dd><p>Indicates how the snapshot is to be created. Possible values are <code class="docutils literal notranslate"><span class="pre">Copy</span></code> or <code class="docutils literal notranslate"><span class="pre">Import</span></code>. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.Snapshot.disk_size_gb">
<code class="descname">disk_size_gb</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.Snapshot.disk_size_gb" title="Permalink to this definition">¶</a></dt>
<dd><p>The size of the Snapshotted Disk in GB.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.Snapshot.location">
<code class="descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.Snapshot.location" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.Snapshot.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.Snapshot.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Snapshot resource. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.Snapshot.resource_group_name">
<code class="descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.Snapshot.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to create the Snapshot. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.Snapshot.source_resource_id">
<code class="descname">source_resource_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.Snapshot.source_resource_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies a reference to an existing snapshot, when <code class="docutils literal notranslate"><span class="pre">create_option</span></code> is <code class="docutils literal notranslate"><span class="pre">Copy</span></code>. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.Snapshot.source_uri">
<code class="descname">source_uri</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.Snapshot.source_uri" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the URI to a Managed or Unmanaged Disk. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.Snapshot.storage_account_id">
<code class="descname">storage_account_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.Snapshot.storage_account_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the ID of an storage account. Used with <code class="docutils literal notranslate"><span class="pre">source_uri</span></code> to allow authorization during import of unmanaged blobs from a different subscription. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.Snapshot.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.Snapshot.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.compute.Snapshot.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.compute.Snapshot.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.compute.Snapshot.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.compute.Snapshot.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.compute.VirtualMachine">
<em class="property">class </em><code class="descclassname">pulumi_azure.compute.</code><code class="descname">VirtualMachine</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>availability_set_id=None</em>, <em>boot_diagnostics=None</em>, <em>delete_data_disks_on_termination=None</em>, <em>delete_os_disk_on_termination=None</em>, <em>identity=None</em>, <em>license_type=None</em>, <em>location=None</em>, <em>name=None</em>, <em>network_interface_ids=None</em>, <em>os_profile=None</em>, <em>os_profile_linux_config=None</em>, <em>os_profile_secrets=None</em>, <em>os_profile_windows_config=None</em>, <em>plan=None</em>, <em>primary_network_interface_id=None</em>, <em>resource_group_name=None</em>, <em>storage_data_disks=None</em>, <em>storage_image_reference=None</em>, <em>storage_os_disk=None</em>, <em>tags=None</em>, <em>vm_size=None</em>, <em>zones=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.compute.VirtualMachine" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Virtual Machine.</p>
<blockquote>
<div><strong>NOTE:</strong> Data Disks can be attached either directly on the <code class="docutils literal notranslate"><span class="pre">azurerm_virtual_machine</span></code> resource, or using the <code class="docutils literal notranslate"><span class="pre">azurerm_virtual_machine_data_disk_attachment</span></code> resource - but the two cannot be used together. If both are used against the same Virtual Machine, spurious changes will occur.</div></blockquote>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>availability_set_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Availability Set in which the Virtual Machine should exist. Changing this forces a new resource to be created.</li>
<li><strong>boot_diagnostics</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">boot_diagnostics</span></code> block.</li>
<li><strong>delete_data_disks_on_termination</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Should the Data Disks (either the Managed Disks / VHD Blobs) be deleted when the Virtual Machine is destroyed? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</li>
<li><strong>delete_os_disk_on_termination</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Should the OS Disk (either the Managed Disk / VHD Blob) be deleted when the Virtual Machine is destroyed? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</li>
<li><strong>identity</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">identity</span></code> block.</li>
<li><strong>license_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the BYOL Type for this Virtual Machine. This is only applicable to Windows Virtual Machines. Possible values are <code class="docutils literal notranslate"><span class="pre">Windows_Client</span></code> and <code class="docutils literal notranslate"><span class="pre">Windows_Server</span></code>.</li>
<li><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the Azure Region where the Virtual Machine exists. Changing this forces a new resource to be created.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Virtual Machine. Changing this forces a new resource to be created.</li>
<li><strong>network_interface_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of Network Interface ID’s which should be associated with the Virtual Machine.</li>
<li><strong>os_profile</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – An <code class="docutils literal notranslate"><span class="pre">os_profile</span></code> block. Required when <code class="docutils literal notranslate"><span class="pre">create_option</span></code> in the <code class="docutils literal notranslate"><span class="pre">storage_os_disk</span></code> block is set to <code class="docutils literal notranslate"><span class="pre">FromImage</span></code>.</li>
<li><strong>os_profile_linux_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">os_profile_linux_config</span></code> block.</li>
<li><strong>os_profile_secrets</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">os_profile_secrets</span></code> blocks.</li>
<li><strong>os_profile_windows_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">os_profile_windows_config</span></code> block.</li>
<li><strong>plan</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">plan</span></code> block.</li>
<li><strong>primary_network_interface_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Network Interface (which must be attached to the Virtual Machine) which should be the Primary Network Interface for this Virtual Machine.</li>
<li><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Resource Group in which the Virtual Machine should exist. Changing this forces a new resource to be created.</li>
<li><strong>storage_data_disks</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">storage_data_disk</span></code> blocks.</li>
<li><strong>storage_image_reference</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">storage_image_reference</span></code> block.</li>
<li><strong>storage_os_disk</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">storage_os_disk</span></code> block.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the Virtual Machine.</li>
<li><strong>vm_size</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the <a class="reference external" href="https://azure.microsoft.com/en-us/documentation/articles/virtual-machines-size-specs/">size of the Virtual Machine</a>.</li>
<li><strong>zones</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A list of a single item of the Availability Zone which the Virtual Machine should be allocated in.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_azure.compute.VirtualMachine.availability_set_id">
<code class="descname">availability_set_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.VirtualMachine.availability_set_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Availability Set in which the Virtual Machine should exist. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.VirtualMachine.boot_diagnostics">
<code class="descname">boot_diagnostics</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.VirtualMachine.boot_diagnostics" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">boot_diagnostics</span></code> block.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.VirtualMachine.delete_data_disks_on_termination">
<code class="descname">delete_data_disks_on_termination</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.VirtualMachine.delete_data_disks_on_termination" title="Permalink to this definition">¶</a></dt>
<dd><p>Should the Data Disks (either the Managed Disks / VHD Blobs) be deleted when the Virtual Machine is destroyed? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.VirtualMachine.delete_os_disk_on_termination">
<code class="descname">delete_os_disk_on_termination</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.VirtualMachine.delete_os_disk_on_termination" title="Permalink to this definition">¶</a></dt>
<dd><p>Should the OS Disk (either the Managed Disk / VHD Blob) be deleted when the Virtual Machine is destroyed? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.VirtualMachine.identity">
<code class="descname">identity</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.VirtualMachine.identity" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">identity</span></code> block.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.VirtualMachine.license_type">
<code class="descname">license_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.VirtualMachine.license_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the BYOL Type for this Virtual Machine. This is only applicable to Windows Virtual Machines. Possible values are <code class="docutils literal notranslate"><span class="pre">Windows_Client</span></code> and <code class="docutils literal notranslate"><span class="pre">Windows_Server</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.VirtualMachine.location">
<code class="descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.VirtualMachine.location" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the Azure Region where the Virtual Machine exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.VirtualMachine.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.VirtualMachine.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Virtual Machine. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.VirtualMachine.network_interface_ids">
<code class="descname">network_interface_ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.VirtualMachine.network_interface_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of Network Interface ID’s which should be associated with the Virtual Machine.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.VirtualMachine.os_profile">
<code class="descname">os_profile</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.VirtualMachine.os_profile" title="Permalink to this definition">¶</a></dt>
<dd><p>An <code class="docutils literal notranslate"><span class="pre">os_profile</span></code> block. Required when <code class="docutils literal notranslate"><span class="pre">create_option</span></code> in the <code class="docutils literal notranslate"><span class="pre">storage_os_disk</span></code> block is set to <code class="docutils literal notranslate"><span class="pre">FromImage</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.VirtualMachine.os_profile_linux_config">
<code class="descname">os_profile_linux_config</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.VirtualMachine.os_profile_linux_config" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">os_profile_linux_config</span></code> block.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.VirtualMachine.os_profile_secrets">
<code class="descname">os_profile_secrets</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.VirtualMachine.os_profile_secrets" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more <code class="docutils literal notranslate"><span class="pre">os_profile_secrets</span></code> blocks.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.VirtualMachine.os_profile_windows_config">
<code class="descname">os_profile_windows_config</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.VirtualMachine.os_profile_windows_config" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">os_profile_windows_config</span></code> block.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.VirtualMachine.plan">
<code class="descname">plan</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.VirtualMachine.plan" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">plan</span></code> block.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.VirtualMachine.primary_network_interface_id">
<code class="descname">primary_network_interface_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.VirtualMachine.primary_network_interface_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Network Interface (which must be attached to the Virtual Machine) which should be the Primary Network Interface for this Virtual Machine.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.VirtualMachine.resource_group_name">
<code class="descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.VirtualMachine.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Resource Group in which the Virtual Machine should exist. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.VirtualMachine.storage_data_disks">
<code class="descname">storage_data_disks</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.VirtualMachine.storage_data_disks" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more <code class="docutils literal notranslate"><span class="pre">storage_data_disk</span></code> blocks.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.VirtualMachine.storage_image_reference">
<code class="descname">storage_image_reference</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.VirtualMachine.storage_image_reference" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">storage_image_reference</span></code> block.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.VirtualMachine.storage_os_disk">
<code class="descname">storage_os_disk</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.VirtualMachine.storage_os_disk" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">storage_os_disk</span></code> block.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.VirtualMachine.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.VirtualMachine.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the Virtual Machine.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.VirtualMachine.vm_size">
<code class="descname">vm_size</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.VirtualMachine.vm_size" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the <a class="reference external" href="https://azure.microsoft.com/en-us/documentation/articles/virtual-machines-size-specs/">size of the Virtual Machine</a>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.VirtualMachine.zones">
<code class="descname">zones</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.VirtualMachine.zones" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of a single item of the Availability Zone which the Virtual Machine should be allocated in.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.compute.VirtualMachine.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.compute.VirtualMachine.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.compute.VirtualMachine.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.compute.VirtualMachine.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.compute.get_image">
<code class="descclassname">pulumi_azure.compute.</code><code class="descname">get_image</code><span class="sig-paren">(</span><em>name=None</em>, <em>name_regex=None</em>, <em>resource_group_name=None</em>, <em>sort_descending=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.compute.get_image" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing Image.</p>
</dd></dl>

<dl class="function">
<dt id="pulumi_azure.compute.get_managed_disk">
<code class="descclassname">pulumi_azure.compute.</code><code class="descname">get_managed_disk</code><span class="sig-paren">(</span><em>name=None</em>, <em>resource_group_name=None</em>, <em>tags=None</em>, <em>zones=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.compute.get_managed_disk" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing Managed Disk.</p>
</dd></dl>

<dl class="function">
<dt id="pulumi_azure.compute.get_platform_image">
<code class="descclassname">pulumi_azure.compute.</code><code class="descname">get_platform_image</code><span class="sig-paren">(</span><em>location=None</em>, <em>offer=None</em>, <em>publisher=None</em>, <em>sku=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.compute.get_platform_image" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about a Platform Image.</p>
</dd></dl>

<dl class="function">
<dt id="pulumi_azure.compute.get_shared_image">
<code class="descclassname">pulumi_azure.compute.</code><code class="descname">get_shared_image</code><span class="sig-paren">(</span><em>gallery_name=None</em>, <em>name=None</em>, <em>resource_group_name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.compute.get_shared_image" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing Shared Image within a Shared Image Gallery.</p>
<blockquote>
<div><strong>NOTE</strong> Shared Image Galleries are currently in Public Preview. You can find more information, including <a class="reference external" href="https://azure.microsoft.com/en-gb/blog/announcing-the-public-preview-of-shared-image-gallery/">how to register for the Public Preview here</a>.</div></blockquote>
</dd></dl>

<dl class="function">
<dt id="pulumi_azure.compute.get_shared_image_gallery">
<code class="descclassname">pulumi_azure.compute.</code><code class="descname">get_shared_image_gallery</code><span class="sig-paren">(</span><em>name=None</em>, <em>resource_group_name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.compute.get_shared_image_gallery" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing Shared Image Gallery.</p>
<blockquote>
<div><strong>NOTE</strong> Shared Image Galleries are currently in Public Preview. You can find more information, including <a class="reference external" href="https://azure.microsoft.com/en-gb/blog/announcing-the-public-preview-of-shared-image-gallery/">how to register for the Public Preview here</a>.</div></blockquote>
</dd></dl>

<dl class="function">
<dt id="pulumi_azure.compute.get_shared_image_version">
<code class="descclassname">pulumi_azure.compute.</code><code class="descname">get_shared_image_version</code><span class="sig-paren">(</span><em>gallery_name=None</em>, <em>image_name=None</em>, <em>name=None</em>, <em>resource_group_name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.compute.get_shared_image_version" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing Version of a Shared Image within a Shared Image Gallery.</p>
<blockquote>
<div><strong>NOTE</strong> Shared Image Galleries are currently in Public Preview. You can find more information, including <a class="reference external" href="https://azure.microsoft.com/en-gb/blog/announcing-the-public-preview-of-shared-image-gallery/">how to register for the Public Preview here</a>.</div></blockquote>
</dd></dl>

<dl class="function">
<dt id="pulumi_azure.compute.get_snapshot">
<code class="descclassname">pulumi_azure.compute.</code><code class="descname">get_snapshot</code><span class="sig-paren">(</span><em>name=None</em>, <em>resource_group_name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.compute.get_snapshot" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing Snapshot.</p>
</dd></dl>

<dl class="function">
<dt id="pulumi_azure.compute.get_virtual_machine">
<code class="descclassname">pulumi_azure.compute.</code><code class="descname">get_virtual_machine</code><span class="sig-paren">(</span><em>name=None</em>, <em>resource_group_name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.compute.get_virtual_machine" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing Virtual Machine.</p>
</dd></dl>

</div>
