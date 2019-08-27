---
title: Module compute
---

<div class="section" id="compute">
<h1>compute<a class="headerlink" href="#compute" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-azure/issues">pulumi/pulumi-azure repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/issues">terraform-providers/terraform-provider-azurerm repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_azure.compute"></span><dl class="class">
<dt id="pulumi_azure.compute.AvailabilitySet">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.compute.</code><code class="sig-name descname">AvailabilitySet</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">managed=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">platform_fault_domain_count=None</em>, <em class="sig-param">platform_update_domain_count=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.compute.AvailabilitySet" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an availability set for virtual machines.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>managed</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specifies whether the availability set is managed or not. Possible values are <code class="docutils literal notranslate"><span class="pre">true</span></code> (to specify aligned) or <code class="docutils literal notranslate"><span class="pre">false</span></code> (to specify classic). Default is <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the availability set. Changing this forces a new resource to be created.</p></li>
<li><p><strong>platform_fault_domain_count</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Specifies the number of fault domains that are used. Defaults to 3.</p></li>
<li><p><strong>platform_update_domain_count</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Specifies the number of update domains that are used. Defaults to 5.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the availability set. Changing this forces a new resource to be created.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/availability_set.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/availability_set.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_azure.compute.AvailabilitySet.location">
<code class="sig-name descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.AvailabilitySet.location" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.AvailabilitySet.managed">
<code class="sig-name descname">managed</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.AvailabilitySet.managed" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies whether the availability set is managed or not. Possible values are <code class="docutils literal notranslate"><span class="pre">true</span></code> (to specify aligned) or <code class="docutils literal notranslate"><span class="pre">false</span></code> (to specify classic). Default is <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.AvailabilitySet.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.AvailabilitySet.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the availability set. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.AvailabilitySet.platform_fault_domain_count">
<code class="sig-name descname">platform_fault_domain_count</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.AvailabilitySet.platform_fault_domain_count" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the number of fault domains that are used. Defaults to 3.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.AvailabilitySet.platform_update_domain_count">
<code class="sig-name descname">platform_update_domain_count</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.AvailabilitySet.platform_update_domain_count" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the number of update domains that are used. Defaults to 5.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.AvailabilitySet.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.AvailabilitySet.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to create the availability set. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.AvailabilitySet.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.AvailabilitySet.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.compute.AvailabilitySet.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">managed=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">platform_fault_domain_count=None</em>, <em class="sig-param">platform_update_domain_count=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.compute.AvailabilitySet.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing AvailabilitySet resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>managed</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specifies whether the availability set is managed or not. Possible values are <code class="docutils literal notranslate"><span class="pre">true</span></code> (to specify aligned) or <code class="docutils literal notranslate"><span class="pre">false</span></code> (to specify classic). Default is <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the availability set. Changing this forces a new resource to be created.</p></li>
<li><p><strong>platform_fault_domain_count</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Specifies the number of fault domains that are used. Defaults to 3.</p></li>
<li><p><strong>platform_update_domain_count</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Specifies the number of update domains that are used. Defaults to 5.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the availability set. Changing this forces a new resource to be created.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/availability_set.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/availability_set.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.compute.AvailabilitySet.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.compute.AvailabilitySet.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.compute.AvailabilitySet.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.compute.AvailabilitySet.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.compute.AwaitableGetAvailabilitySetResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.compute.</code><code class="sig-name descname">AwaitableGetAvailabilitySetResult</code><span class="sig-paren">(</span><em class="sig-param">location=None</em>, <em class="sig-param">managed=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">platform_fault_domain_count=None</em>, <em class="sig-param">platform_update_domain_count=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.compute.AwaitableGetAvailabilitySetResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_azure.compute.AwaitableGetImageResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.compute.</code><code class="sig-name descname">AwaitableGetImageResult</code><span class="sig-paren">(</span><em class="sig-param">data_disks=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">name_regex=None</em>, <em class="sig-param">os_disks=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">sort_descending=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">zone_resilient=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.compute.AwaitableGetImageResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_azure.compute.AwaitableGetManagedDiskResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.compute.</code><code class="sig-name descname">AwaitableGetManagedDiskResult</code><span class="sig-paren">(</span><em class="sig-param">create_option=None</em>, <em class="sig-param">disk_size_gb=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">os_type=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">source_resource_id=None</em>, <em class="sig-param">source_uri=None</em>, <em class="sig-param">storage_account_type=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">zones=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.compute.AwaitableGetManagedDiskResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_azure.compute.AwaitableGetPlatformImageResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.compute.</code><code class="sig-name descname">AwaitableGetPlatformImageResult</code><span class="sig-paren">(</span><em class="sig-param">location=None</em>, <em class="sig-param">offer=None</em>, <em class="sig-param">publisher=None</em>, <em class="sig-param">sku=None</em>, <em class="sig-param">version=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.compute.AwaitableGetPlatformImageResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_azure.compute.AwaitableGetSharedImageGalleryResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.compute.</code><code class="sig-name descname">AwaitableGetSharedImageGalleryResult</code><span class="sig-paren">(</span><em class="sig-param">description=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">unique_name=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.compute.AwaitableGetSharedImageGalleryResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_azure.compute.AwaitableGetSharedImageResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.compute.</code><code class="sig-name descname">AwaitableGetSharedImageResult</code><span class="sig-paren">(</span><em class="sig-param">description=None</em>, <em class="sig-param">eula=None</em>, <em class="sig-param">gallery_name=None</em>, <em class="sig-param">identifiers=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">os_type=None</em>, <em class="sig-param">privacy_statement_uri=None</em>, <em class="sig-param">release_note_uri=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.compute.AwaitableGetSharedImageResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_azure.compute.AwaitableGetSharedImageVersionResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.compute.</code><code class="sig-name descname">AwaitableGetSharedImageVersionResult</code><span class="sig-paren">(</span><em class="sig-param">exclude_from_latest=None</em>, <em class="sig-param">gallery_name=None</em>, <em class="sig-param">image_name=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">managed_image_id=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">target_regions=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.compute.AwaitableGetSharedImageVersionResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_azure.compute.AwaitableGetSnapshotResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.compute.</code><code class="sig-name descname">AwaitableGetSnapshotResult</code><span class="sig-paren">(</span><em class="sig-param">creation_option=None</em>, <em class="sig-param">disk_size_gb=None</em>, <em class="sig-param">encryption_settings=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">os_type=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">source_resource_id=None</em>, <em class="sig-param">source_uri=None</em>, <em class="sig-param">storage_account_id=None</em>, <em class="sig-param">time_created=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.compute.AwaitableGetSnapshotResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_azure.compute.AwaitableGetVirtualMachineResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.compute.</code><code class="sig-name descname">AwaitableGetVirtualMachineResult</code><span class="sig-paren">(</span><em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.compute.AwaitableGetVirtualMachineResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_azure.compute.DataDiskAttachment">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.compute.</code><code class="sig-name descname">DataDiskAttachment</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">caching=None</em>, <em class="sig-param">create_option=None</em>, <em class="sig-param">lun=None</em>, <em class="sig-param">managed_disk_id=None</em>, <em class="sig-param">virtual_machine_id=None</em>, <em class="sig-param">write_accelerator_enabled=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.compute.DataDiskAttachment" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages attaching a Disk to a Virtual Machine.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Data Disks can be attached either directly on the <code class="docutils literal notranslate"><span class="pre">compute.VirtualMachine</span></code> resource, or using the <code class="docutils literal notranslate"><span class="pre">compute.DataDiskAttachment</span></code> resource - but the two cannot be used together. If both are used against the same Virtual Machine, spurious changes will occur.</p>
<p><strong>Please Note:</strong> only Managed Disks are supported via this separate resource, Unmanaged Disks can be attached using the <code class="docutils literal notranslate"><span class="pre">storage_data_disk</span></code> block in the <code class="docutils literal notranslate"><span class="pre">compute.VirtualMachine</span></code> resource.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>caching</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the caching requirements for this Data Disk. Possible values include <code class="docutils literal notranslate"><span class="pre">None</span></code>, <code class="docutils literal notranslate"><span class="pre">ReadOnly</span></code> and <code class="docutils literal notranslate"><span class="pre">ReadWrite</span></code>.</p></li>
<li><p><strong>create_option</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Create Option of the Data Disk, such as <code class="docutils literal notranslate"><span class="pre">Empty</span></code> or <code class="docutils literal notranslate"><span class="pre">Attach</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">Attach</span></code>. Changing this forces a new resource to be created.</p></li>
<li><p><strong>lun</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The Logical Unit Number of the Data Disk, which needs to be unique within the Virtual Machine. Changing this forces a new resource to be created.</p></li>
<li><p><strong>managed_disk_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of an existing Managed Disk which should be attached. Changing this forces a new resource to be created.</p></li>
<li><p><strong>virtual_machine_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Virtual Machine to which the Data Disk should be attached. Changing this forces a new resource to be created.</p></li>
<li><p><strong>write_accelerator_enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specifies if Write Accelerator is enabled on the disk. This can only be enabled on <code class="docutils literal notranslate"><span class="pre">Premium_LRS</span></code> managed disks with no caching and <a class="reference external" href="https://docs.microsoft.com/en-us/azure/virtual-machines/workloads/sap/how-to-enable-write-accelerator">M-Series VMs</a>. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/virtual_machine_data_disk_attachment.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/virtual_machine_data_disk_attachment.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_azure.compute.DataDiskAttachment.caching">
<code class="sig-name descname">caching</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.DataDiskAttachment.caching" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the caching requirements for this Data Disk. Possible values include <code class="docutils literal notranslate"><span class="pre">None</span></code>, <code class="docutils literal notranslate"><span class="pre">ReadOnly</span></code> and <code class="docutils literal notranslate"><span class="pre">ReadWrite</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.DataDiskAttachment.create_option">
<code class="sig-name descname">create_option</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.DataDiskAttachment.create_option" title="Permalink to this definition">¶</a></dt>
<dd><p>The Create Option of the Data Disk, such as <code class="docutils literal notranslate"><span class="pre">Empty</span></code> or <code class="docutils literal notranslate"><span class="pre">Attach</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">Attach</span></code>. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.DataDiskAttachment.lun">
<code class="sig-name descname">lun</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.DataDiskAttachment.lun" title="Permalink to this definition">¶</a></dt>
<dd><p>The Logical Unit Number of the Data Disk, which needs to be unique within the Virtual Machine. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.DataDiskAttachment.managed_disk_id">
<code class="sig-name descname">managed_disk_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.DataDiskAttachment.managed_disk_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of an existing Managed Disk which should be attached. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.DataDiskAttachment.virtual_machine_id">
<code class="sig-name descname">virtual_machine_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.DataDiskAttachment.virtual_machine_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Virtual Machine to which the Data Disk should be attached. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.DataDiskAttachment.write_accelerator_enabled">
<code class="sig-name descname">write_accelerator_enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.DataDiskAttachment.write_accelerator_enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies if Write Accelerator is enabled on the disk. This can only be enabled on <code class="docutils literal notranslate"><span class="pre">Premium_LRS</span></code> managed disks with no caching and <a class="reference external" href="https://docs.microsoft.com/en-us/azure/virtual-machines/workloads/sap/how-to-enable-write-accelerator">M-Series VMs</a>. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.compute.DataDiskAttachment.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">caching=None</em>, <em class="sig-param">create_option=None</em>, <em class="sig-param">lun=None</em>, <em class="sig-param">managed_disk_id=None</em>, <em class="sig-param">virtual_machine_id=None</em>, <em class="sig-param">write_accelerator_enabled=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.compute.DataDiskAttachment.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing DataDiskAttachment resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>caching</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the caching requirements for this Data Disk. Possible values include <code class="docutils literal notranslate"><span class="pre">None</span></code>, <code class="docutils literal notranslate"><span class="pre">ReadOnly</span></code> and <code class="docutils literal notranslate"><span class="pre">ReadWrite</span></code>.</p></li>
<li><p><strong>create_option</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Create Option of the Data Disk, such as <code class="docutils literal notranslate"><span class="pre">Empty</span></code> or <code class="docutils literal notranslate"><span class="pre">Attach</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">Attach</span></code>. Changing this forces a new resource to be created.</p></li>
<li><p><strong>lun</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The Logical Unit Number of the Data Disk, which needs to be unique within the Virtual Machine. Changing this forces a new resource to be created.</p></li>
<li><p><strong>managed_disk_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of an existing Managed Disk which should be attached. Changing this forces a new resource to be created.</p></li>
<li><p><strong>virtual_machine_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Virtual Machine to which the Data Disk should be attached. Changing this forces a new resource to be created.</p></li>
<li><p><strong>write_accelerator_enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – <p>Specifies if Write Accelerator is enabled on the disk. This can only be enabled on <code class="docutils literal notranslate"><span class="pre">Premium_LRS</span></code> managed disks with no caching and <a class="reference external" href="https://docs.microsoft.com/en-us/azure/virtual-machines/workloads/sap/how-to-enable-write-accelerator">M-Series VMs</a>. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/virtual_machine_data_disk_attachment.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/virtual_machine_data_disk_attachment.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.compute.DataDiskAttachment.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.compute.DataDiskAttachment.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.compute.DataDiskAttachment.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.compute.DataDiskAttachment.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.compute.Extension">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.compute.</code><code class="sig-name descname">Extension</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">auto_upgrade_minor_version=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">protected_settings=None</em>, <em class="sig-param">publisher=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">settings=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">type=None</em>, <em class="sig-param">type_handler_version=None</em>, <em class="sig-param">virtual_machine_name=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.compute.Extension" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Virtual Machine Extension to provide post deployment configuration
and run automated tasks.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Custom Script Extensions for Linux &amp; Windows require that the <code class="docutils literal notranslate"><span class="pre">commandToExecute</span></code> returns a <code class="docutils literal notranslate"><span class="pre">0</span></code> exit code to be classified as successfully deployed. You can achieve this by appending <code class="docutils literal notranslate"><span class="pre">exit</span> <span class="pre">0</span></code> to the end of your <code class="docutils literal notranslate"><span class="pre">commandToExecute</span></code>.</p>
<p><strong>NOTE:</strong> Custom Script Extensions require that the Azure Virtual Machine Guest Agent is running on the Virtual Machine.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>auto_upgrade_minor_version</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specifies if the platform deploys
the latest minor version update to the <code class="docutils literal notranslate"><span class="pre">type_handler_version</span></code> specified.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The location where the extension is created. Changing
this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the virtual machine extension peering. Changing
this forces a new resource to be created.</p></li>
<li><p><strong>protected_settings</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The protected_settings passed to the
extension, like settings, these are specified as a JSON object in a string.</p></li>
<li><p><strong>publisher</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The publisher of the extension, available publishers
can be found by using the Azure CLI.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to
create the virtual network. Changing this forces a new resource to be
created.</p></li>
<li><p><strong>settings</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The settings passed to the extension, these are
specified as a JSON object in a string.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of extension, available types for a publisher can
be found using the Azure CLI.</p></li>
<li><p><strong>type_handler_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the version of the extension to
use, available versions can be found using the Azure CLI.</p></li>
<li><p><strong>virtual_machine_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the virtual machine. Changing
this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/virtual_machine_extension.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/virtual_machine_extension.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_azure.compute.Extension.auto_upgrade_minor_version">
<code class="sig-name descname">auto_upgrade_minor_version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.Extension.auto_upgrade_minor_version" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies if the platform deploys
the latest minor version update to the <code class="docutils literal notranslate"><span class="pre">type_handler_version</span></code> specified.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.Extension.location">
<code class="sig-name descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.Extension.location" title="Permalink to this definition">¶</a></dt>
<dd><p>The location where the extension is created. Changing
this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.Extension.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.Extension.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the virtual machine extension peering. Changing
this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.Extension.protected_settings">
<code class="sig-name descname">protected_settings</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.Extension.protected_settings" title="Permalink to this definition">¶</a></dt>
<dd><p>The protected_settings passed to the
extension, like settings, these are specified as a JSON object in a string.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.Extension.publisher">
<code class="sig-name descname">publisher</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.Extension.publisher" title="Permalink to this definition">¶</a></dt>
<dd><p>The publisher of the extension, available publishers
can be found by using the Azure CLI.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.Extension.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.Extension.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to
create the virtual network. Changing this forces a new resource to be
created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.Extension.settings">
<code class="sig-name descname">settings</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.Extension.settings" title="Permalink to this definition">¶</a></dt>
<dd><p>The settings passed to the extension, these are
specified as a JSON object in a string.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.Extension.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.Extension.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.Extension.type">
<code class="sig-name descname">type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.Extension.type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of extension, available types for a publisher can
be found using the Azure CLI.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.Extension.type_handler_version">
<code class="sig-name descname">type_handler_version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.Extension.type_handler_version" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the version of the extension to
use, available versions can be found using the Azure CLI.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.Extension.virtual_machine_name">
<code class="sig-name descname">virtual_machine_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.Extension.virtual_machine_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the virtual machine. Changing
this forces a new resource to be created.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.compute.Extension.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">auto_upgrade_minor_version=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">protected_settings=None</em>, <em class="sig-param">publisher=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">settings=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">type=None</em>, <em class="sig-param">type_handler_version=None</em>, <em class="sig-param">virtual_machine_name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.compute.Extension.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Extension resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>auto_upgrade_minor_version</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specifies if the platform deploys
the latest minor version update to the <code class="docutils literal notranslate"><span class="pre">type_handler_version</span></code> specified.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The location where the extension is created. Changing
this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the virtual machine extension peering. Changing
this forces a new resource to be created.</p></li>
<li><p><strong>protected_settings</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The protected_settings passed to the
extension, like settings, these are specified as a JSON object in a string.</p></li>
<li><p><strong>publisher</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The publisher of the extension, available publishers
can be found by using the Azure CLI.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to
create the virtual network. Changing this forces a new resource to be
created.</p></li>
<li><p><strong>settings</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The settings passed to the extension, these are
specified as a JSON object in a string.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of extension, available types for a publisher can
be found using the Azure CLI.</p></li>
<li><p><strong>type_handler_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the version of the extension to
use, available versions can be found using the Azure CLI.</p></li>
<li><p><strong>virtual_machine_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the virtual machine. Changing
this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/virtual_machine_extension.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/virtual_machine_extension.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.compute.Extension.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.compute.Extension.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.compute.Extension.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.compute.Extension.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.compute.GetAvailabilitySetResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.compute.</code><code class="sig-name descname">GetAvailabilitySetResult</code><span class="sig-paren">(</span><em class="sig-param">location=None</em>, <em class="sig-param">managed=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">platform_fault_domain_count=None</em>, <em class="sig-param">platform_update_domain_count=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.compute.GetAvailabilitySetResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getAvailabilitySet.</p>
<dl class="attribute">
<dt id="pulumi_azure.compute.GetAvailabilitySetResult.location">
<code class="sig-name descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.GetAvailabilitySetResult.location" title="Permalink to this definition">¶</a></dt>
<dd><p>The supported Azure location where the Availability Set exists.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.GetAvailabilitySetResult.managed">
<code class="sig-name descname">managed</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.GetAvailabilitySetResult.managed" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the availability set is managed or not.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.GetAvailabilitySetResult.platform_fault_domain_count">
<code class="sig-name descname">platform_fault_domain_count</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.GetAvailabilitySetResult.platform_fault_domain_count" title="Permalink to this definition">¶</a></dt>
<dd><p>The number of fault domains that are used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.GetAvailabilitySetResult.platform_update_domain_count">
<code class="sig-name descname">platform_update_domain_count</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.GetAvailabilitySetResult.platform_update_domain_count" title="Permalink to this definition">¶</a></dt>
<dd><p>The number of update domains that are used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.GetAvailabilitySetResult.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.GetAvailabilitySetResult.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags assigned to the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.GetAvailabilitySetResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.GetAvailabilitySetResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azure.compute.GetImageResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.compute.</code><code class="sig-name descname">GetImageResult</code><span class="sig-paren">(</span><em class="sig-param">data_disks=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">name_regex=None</em>, <em class="sig-param">os_disks=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">sort_descending=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">zone_resilient=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.compute.GetImageResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getImage.</p>
<dl class="attribute">
<dt id="pulumi_azure.compute.GetImageResult.data_disks">
<code class="sig-name descname">data_disks</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.GetImageResult.data_disks" title="Permalink to this definition">¶</a></dt>
<dd><p>a collection of <code class="docutils literal notranslate"><span class="pre">data_disk</span></code> blocks as defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.GetImageResult.location">
<code class="sig-name descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.GetImageResult.location" title="Permalink to this definition">¶</a></dt>
<dd><p>the Azure Location where this Image exists.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.GetImageResult.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.GetImageResult.name" title="Permalink to this definition">¶</a></dt>
<dd><p>the name of the Image.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.GetImageResult.os_disks">
<code class="sig-name descname">os_disks</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.GetImageResult.os_disks" title="Permalink to this definition">¶</a></dt>
<dd><p>a <code class="docutils literal notranslate"><span class="pre">os_disk</span></code> block as defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.GetImageResult.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.GetImageResult.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>a mapping of tags to assigned to the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.GetImageResult.zone_resilient">
<code class="sig-name descname">zone_resilient</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.GetImageResult.zone_resilient" title="Permalink to this definition">¶</a></dt>
<dd><p>is zone resiliency enabled?</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.GetImageResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.GetImageResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azure.compute.GetManagedDiskResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.compute.</code><code class="sig-name descname">GetManagedDiskResult</code><span class="sig-paren">(</span><em class="sig-param">create_option=None</em>, <em class="sig-param">disk_size_gb=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">os_type=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">source_resource_id=None</em>, <em class="sig-param">source_uri=None</em>, <em class="sig-param">storage_account_type=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">zones=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.compute.GetManagedDiskResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getManagedDisk.</p>
<dl class="attribute">
<dt id="pulumi_azure.compute.GetManagedDiskResult.disk_size_gb">
<code class="sig-name descname">disk_size_gb</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.GetManagedDiskResult.disk_size_gb" title="Permalink to this definition">¶</a></dt>
<dd><p>The size of the managed disk in gigabytes.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.GetManagedDiskResult.os_type">
<code class="sig-name descname">os_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.GetManagedDiskResult.os_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The operating system for managed disk. Valid values are <code class="docutils literal notranslate"><span class="pre">Linux</span></code> or <code class="docutils literal notranslate"><span class="pre">Windows</span></code></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.GetManagedDiskResult.source_resource_id">
<code class="sig-name descname">source_resource_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.GetManagedDiskResult.source_resource_id" title="Permalink to this definition">¶</a></dt>
<dd><p>ID of an existing managed disk that the current resource was created from.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.GetManagedDiskResult.source_uri">
<code class="sig-name descname">source_uri</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.GetManagedDiskResult.source_uri" title="Permalink to this definition">¶</a></dt>
<dd><p>The source URI for the managed disk</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.GetManagedDiskResult.storage_account_type">
<code class="sig-name descname">storage_account_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.GetManagedDiskResult.storage_account_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The storage account type for the managed disk.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.GetManagedDiskResult.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.GetManagedDiskResult.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags assigned to the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.GetManagedDiskResult.zones">
<code class="sig-name descname">zones</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.GetManagedDiskResult.zones" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection containing the availability zone the managed disk is allocated in.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.GetManagedDiskResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.GetManagedDiskResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azure.compute.GetPlatformImageResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.compute.</code><code class="sig-name descname">GetPlatformImageResult</code><span class="sig-paren">(</span><em class="sig-param">location=None</em>, <em class="sig-param">offer=None</em>, <em class="sig-param">publisher=None</em>, <em class="sig-param">sku=None</em>, <em class="sig-param">version=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.compute.GetPlatformImageResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getPlatformImage.</p>
<dl class="attribute">
<dt id="pulumi_azure.compute.GetPlatformImageResult.version">
<code class="sig-name descname">version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.GetPlatformImageResult.version" title="Permalink to this definition">¶</a></dt>
<dd><p>The latest version of the Platform Image.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.GetPlatformImageResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.GetPlatformImageResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azure.compute.GetSharedImageGalleryResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.compute.</code><code class="sig-name descname">GetSharedImageGalleryResult</code><span class="sig-paren">(</span><em class="sig-param">description=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">unique_name=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.compute.GetSharedImageGalleryResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getSharedImageGallery.</p>
<dl class="attribute">
<dt id="pulumi_azure.compute.GetSharedImageGalleryResult.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.GetSharedImageGalleryResult.description" title="Permalink to this definition">¶</a></dt>
<dd><p>A description for the Shared Image Gallery.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.GetSharedImageGalleryResult.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.GetSharedImageGalleryResult.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags which are assigned to the Shared Image Gallery.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.GetSharedImageGalleryResult.unique_name">
<code class="sig-name descname">unique_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.GetSharedImageGalleryResult.unique_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The unique name assigned to the Shared Image Gallery.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.GetSharedImageGalleryResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.GetSharedImageGalleryResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azure.compute.GetSharedImageResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.compute.</code><code class="sig-name descname">GetSharedImageResult</code><span class="sig-paren">(</span><em class="sig-param">description=None</em>, <em class="sig-param">eula=None</em>, <em class="sig-param">gallery_name=None</em>, <em class="sig-param">identifiers=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">os_type=None</em>, <em class="sig-param">privacy_statement_uri=None</em>, <em class="sig-param">release_note_uri=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.compute.GetSharedImageResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getSharedImage.</p>
<dl class="attribute">
<dt id="pulumi_azure.compute.GetSharedImageResult.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.GetSharedImageResult.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description of this Shared Image.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.GetSharedImageResult.eula">
<code class="sig-name descname">eula</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.GetSharedImageResult.eula" title="Permalink to this definition">¶</a></dt>
<dd><p>The End User Licence Agreement for the Shared Image.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.GetSharedImageResult.identifiers">
<code class="sig-name descname">identifiers</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.GetSharedImageResult.identifiers" title="Permalink to this definition">¶</a></dt>
<dd><p>An <code class="docutils literal notranslate"><span class="pre">identifier</span></code> block as defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.GetSharedImageResult.location">
<code class="sig-name descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.GetSharedImageResult.location" title="Permalink to this definition">¶</a></dt>
<dd><p>The supported Azure location where the Shared Image Gallery exists.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.GetSharedImageResult.os_type">
<code class="sig-name descname">os_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.GetSharedImageResult.os_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of Operating System present in this Shared Image.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.GetSharedImageResult.privacy_statement_uri">
<code class="sig-name descname">privacy_statement_uri</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.GetSharedImageResult.privacy_statement_uri" title="Permalink to this definition">¶</a></dt>
<dd><p>The URI containing the Privacy Statement for this Shared Image.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.GetSharedImageResult.release_note_uri">
<code class="sig-name descname">release_note_uri</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.GetSharedImageResult.release_note_uri" title="Permalink to this definition">¶</a></dt>
<dd><p>The URI containing the Release Notes for this Shared Image.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.GetSharedImageResult.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.GetSharedImageResult.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags assigned to the Shared Image.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.GetSharedImageResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.GetSharedImageResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azure.compute.GetSharedImageVersionResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.compute.</code><code class="sig-name descname">GetSharedImageVersionResult</code><span class="sig-paren">(</span><em class="sig-param">exclude_from_latest=None</em>, <em class="sig-param">gallery_name=None</em>, <em class="sig-param">image_name=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">managed_image_id=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">target_regions=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.compute.GetSharedImageVersionResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getSharedImageVersion.</p>
<dl class="attribute">
<dt id="pulumi_azure.compute.GetSharedImageVersionResult.exclude_from_latest">
<code class="sig-name descname">exclude_from_latest</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.GetSharedImageVersionResult.exclude_from_latest" title="Permalink to this definition">¶</a></dt>
<dd><p>Is this Image Version excluded from the <code class="docutils literal notranslate"><span class="pre">latest</span></code> filter?</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.GetSharedImageVersionResult.location">
<code class="sig-name descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.GetSharedImageVersionResult.location" title="Permalink to this definition">¶</a></dt>
<dd><p>The supported Azure location where the Shared Image Gallery exists.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.GetSharedImageVersionResult.managed_image_id">
<code class="sig-name descname">managed_image_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.GetSharedImageVersionResult.managed_image_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Managed Image which was the source of this Shared Image Version.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.GetSharedImageVersionResult.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.GetSharedImageVersionResult.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The Azure Region in which this Image Version exists.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.GetSharedImageVersionResult.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.GetSharedImageVersionResult.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags assigned to the Shared Image.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.GetSharedImageVersionResult.target_regions">
<code class="sig-name descname">target_regions</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.GetSharedImageVersionResult.target_regions" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more <code class="docutils literal notranslate"><span class="pre">target_region</span></code> blocks as documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.GetSharedImageVersionResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.GetSharedImageVersionResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azure.compute.GetSnapshotResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.compute.</code><code class="sig-name descname">GetSnapshotResult</code><span class="sig-paren">(</span><em class="sig-param">creation_option=None</em>, <em class="sig-param">disk_size_gb=None</em>, <em class="sig-param">encryption_settings=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">os_type=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">source_resource_id=None</em>, <em class="sig-param">source_uri=None</em>, <em class="sig-param">storage_account_id=None</em>, <em class="sig-param">time_created=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.compute.GetSnapshotResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getSnapshot.</p>
<dl class="attribute">
<dt id="pulumi_azure.compute.GetSnapshotResult.disk_size_gb">
<code class="sig-name descname">disk_size_gb</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.GetSnapshotResult.disk_size_gb" title="Permalink to this definition">¶</a></dt>
<dd><p>The size of the Snapshotted Disk in GB.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.GetSnapshotResult.source_resource_id">
<code class="sig-name descname">source_resource_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.GetSnapshotResult.source_resource_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The reference to an existing snapshot.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.GetSnapshotResult.source_uri">
<code class="sig-name descname">source_uri</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.GetSnapshotResult.source_uri" title="Permalink to this definition">¶</a></dt>
<dd><p>The URI to a Managed or Unmanaged Disk.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.GetSnapshotResult.storage_account_id">
<code class="sig-name descname">storage_account_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.GetSnapshotResult.storage_account_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of an storage account.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.GetSnapshotResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.GetSnapshotResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azure.compute.GetVirtualMachineResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.compute.</code><code class="sig-name descname">GetVirtualMachineResult</code><span class="sig-paren">(</span><em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.compute.GetVirtualMachineResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getVirtualMachine.</p>
<dl class="attribute">
<dt id="pulumi_azure.compute.GetVirtualMachineResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.GetVirtualMachineResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azure.compute.Image">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.compute.</code><code class="sig-name descname">Image</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">data_disks=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">os_disk=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">source_virtual_machine_id=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">zone_resilient=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.compute.Image" title="Permalink to this definition">¶</a></dt>
<dd><p>Manage a custom virtual machine image that can be used to create virtual machines.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>data_disks</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">data_disk</span></code> elements as defined below.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specified the supported Azure location where the resource exists.
Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the image. Changing this forces a
new resource to be created.</p></li>
<li><p><strong>os_disk</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">os_disk</span></code> elements as defined below.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create
the image. Changing this forces a new resource to be created.</p></li>
<li><p><strong>source_virtual_machine_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Virtual Machine ID from which to create the image.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
<li><p><strong>zone_resilient</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Is zone resiliency enabled?  Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.  Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/image.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/image.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_azure.compute.Image.data_disks">
<code class="sig-name descname">data_disks</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.Image.data_disks" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more <code class="docutils literal notranslate"><span class="pre">data_disk</span></code> elements as defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.Image.location">
<code class="sig-name descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.Image.location" title="Permalink to this definition">¶</a></dt>
<dd><p>Specified the supported Azure location where the resource exists.
Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.Image.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.Image.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the image. Changing this forces a
new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.Image.os_disk">
<code class="sig-name descname">os_disk</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.Image.os_disk" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more <code class="docutils literal notranslate"><span class="pre">os_disk</span></code> elements as defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.Image.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.Image.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to create
the image. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.Image.source_virtual_machine_id">
<code class="sig-name descname">source_virtual_machine_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.Image.source_virtual_machine_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The Virtual Machine ID from which to create the image.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.Image.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.Image.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.Image.zone_resilient">
<code class="sig-name descname">zone_resilient</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.Image.zone_resilient" title="Permalink to this definition">¶</a></dt>
<dd><p>Is zone resiliency enabled?  Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.  Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.compute.Image.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">data_disks=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">os_disk=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">source_virtual_machine_id=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">zone_resilient=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.compute.Image.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Image resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>data_disks</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">data_disk</span></code> elements as defined below.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specified the supported Azure location where the resource exists.
Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the image. Changing this forces a
new resource to be created.</p></li>
<li><p><strong>os_disk</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">os_disk</span></code> elements as defined below.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create
the image. Changing this forces a new resource to be created.</p></li>
<li><p><strong>source_virtual_machine_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Virtual Machine ID from which to create the image.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
<li><p><strong>zone_resilient</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Is zone resiliency enabled?  Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.  Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/image.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/image.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.compute.Image.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.compute.Image.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.compute.Image.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.compute.Image.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.compute.ManagedDisk">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.compute.</code><code class="sig-name descname">ManagedDisk</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">create_option=None</em>, <em class="sig-param">disk_size_gb=None</em>, <em class="sig-param">encryption_settings=None</em>, <em class="sig-param">image_reference_id=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">os_type=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">source_resource_id=None</em>, <em class="sig-param">source_uri=None</em>, <em class="sig-param">storage_account_type=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">zones=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.compute.ManagedDisk" title="Permalink to this definition">¶</a></dt>
<dd><p>Manage a managed disk.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>create_option</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The method to use when creating the managed disk. Possible values include:</p></li>
<li><p><strong>disk_size_gb</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Specifies the size of the managed disk to create in gigabytes.
If <code class="docutils literal notranslate"><span class="pre">create_option</span></code> is <code class="docutils literal notranslate"><span class="pre">Copy</span></code> or <code class="docutils literal notranslate"><span class="pre">FromImage</span></code>, then the value must be equal to or greater than the source’s size.</p></li>
<li><p><strong>encryption_settings</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – an <code class="docutils literal notranslate"><span class="pre">encryption_settings</span></code> block as defined below.</p></li>
<li><p><strong>image_reference_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – ID of an existing platform/marketplace disk image to copy when <code class="docutils literal notranslate"><span class="pre">create_option</span></code> is <code class="docutils literal notranslate"><span class="pre">FromImage</span></code>.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specified the supported Azure location where the resource exists.
Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the managed disk. Changing this forces a
new resource to be created.</p></li>
<li><p><strong>os_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specify a value when the source of an <code class="docutils literal notranslate"><span class="pre">Import</span></code> or <code class="docutils literal notranslate"><span class="pre">Copy</span></code>
operation targets a source that contains an operating system. Valid values are <code class="docutils literal notranslate"><span class="pre">Linux</span></code> or <code class="docutils literal notranslate"><span class="pre">Windows</span></code></p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create
the managed disk.</p></li>
<li><p><strong>source_resource_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – ID of an existing managed disk to copy <code class="docutils literal notranslate"><span class="pre">create_option</span></code> is <code class="docutils literal notranslate"><span class="pre">Copy</span></code>
or the recovery point to restore when <code class="docutils literal notranslate"><span class="pre">create_option</span></code> is <code class="docutils literal notranslate"><span class="pre">Restore</span></code></p></li>
<li><p><strong>source_uri</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – URI to a valid VHD file to be used when <code class="docutils literal notranslate"><span class="pre">create_option</span></code> is <code class="docutils literal notranslate"><span class="pre">Import</span></code>.</p></li>
<li><p><strong>storage_account_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of storage to use for the managed disk.
Allowable values are <code class="docutils literal notranslate"><span class="pre">Standard_LRS</span></code>, <code class="docutils literal notranslate"><span class="pre">Premium_LRS</span></code>, <code class="docutils literal notranslate"><span class="pre">StandardSSD_LRS</span></code> or <code class="docutils literal notranslate"><span class="pre">UltraSSD_LRS</span></code>.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
<li><p><strong>zones</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A collection containing the availability zone to allocate the Managed Disk in.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/managed_disk.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/managed_disk.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_azure.compute.ManagedDisk.create_option">
<code class="sig-name descname">create_option</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.ManagedDisk.create_option" title="Permalink to this definition">¶</a></dt>
<dd><p>The method to use when creating the managed disk. Possible values include:</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.ManagedDisk.disk_size_gb">
<code class="sig-name descname">disk_size_gb</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.ManagedDisk.disk_size_gb" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the size of the managed disk to create in gigabytes.
If <code class="docutils literal notranslate"><span class="pre">create_option</span></code> is <code class="docutils literal notranslate"><span class="pre">Copy</span></code> or <code class="docutils literal notranslate"><span class="pre">FromImage</span></code>, then the value must be equal to or greater than the source’s size.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.ManagedDisk.encryption_settings">
<code class="sig-name descname">encryption_settings</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.ManagedDisk.encryption_settings" title="Permalink to this definition">¶</a></dt>
<dd><p>an <code class="docutils literal notranslate"><span class="pre">encryption_settings</span></code> block as defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.ManagedDisk.image_reference_id">
<code class="sig-name descname">image_reference_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.ManagedDisk.image_reference_id" title="Permalink to this definition">¶</a></dt>
<dd><p>ID of an existing platform/marketplace disk image to copy when <code class="docutils literal notranslate"><span class="pre">create_option</span></code> is <code class="docutils literal notranslate"><span class="pre">FromImage</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.ManagedDisk.location">
<code class="sig-name descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.ManagedDisk.location" title="Permalink to this definition">¶</a></dt>
<dd><p>Specified the supported Azure location where the resource exists.
Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.ManagedDisk.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.ManagedDisk.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the managed disk. Changing this forces a
new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.ManagedDisk.os_type">
<code class="sig-name descname">os_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.ManagedDisk.os_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Specify a value when the source of an <code class="docutils literal notranslate"><span class="pre">Import</span></code> or <code class="docutils literal notranslate"><span class="pre">Copy</span></code>
operation targets a source that contains an operating system. Valid values are <code class="docutils literal notranslate"><span class="pre">Linux</span></code> or <code class="docutils literal notranslate"><span class="pre">Windows</span></code></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.ManagedDisk.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.ManagedDisk.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to create
the managed disk.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.ManagedDisk.source_resource_id">
<code class="sig-name descname">source_resource_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.ManagedDisk.source_resource_id" title="Permalink to this definition">¶</a></dt>
<dd><p>ID of an existing managed disk to copy <code class="docutils literal notranslate"><span class="pre">create_option</span></code> is <code class="docutils literal notranslate"><span class="pre">Copy</span></code>
or the recovery point to restore when <code class="docutils literal notranslate"><span class="pre">create_option</span></code> is <code class="docutils literal notranslate"><span class="pre">Restore</span></code></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.ManagedDisk.source_uri">
<code class="sig-name descname">source_uri</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.ManagedDisk.source_uri" title="Permalink to this definition">¶</a></dt>
<dd><p>URI to a valid VHD file to be used when <code class="docutils literal notranslate"><span class="pre">create_option</span></code> is <code class="docutils literal notranslate"><span class="pre">Import</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.ManagedDisk.storage_account_type">
<code class="sig-name descname">storage_account_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.ManagedDisk.storage_account_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of storage to use for the managed disk.
Allowable values are <code class="docutils literal notranslate"><span class="pre">Standard_LRS</span></code>, <code class="docutils literal notranslate"><span class="pre">Premium_LRS</span></code>, <code class="docutils literal notranslate"><span class="pre">StandardSSD_LRS</span></code> or <code class="docutils literal notranslate"><span class="pre">UltraSSD_LRS</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.ManagedDisk.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.ManagedDisk.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.ManagedDisk.zones">
<code class="sig-name descname">zones</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.ManagedDisk.zones" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection containing the availability zone to allocate the Managed Disk in.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.compute.ManagedDisk.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">create_option=None</em>, <em class="sig-param">disk_size_gb=None</em>, <em class="sig-param">encryption_settings=None</em>, <em class="sig-param">image_reference_id=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">os_type=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">source_resource_id=None</em>, <em class="sig-param">source_uri=None</em>, <em class="sig-param">storage_account_type=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">zones=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.compute.ManagedDisk.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ManagedDisk resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>create_option</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The method to use when creating the managed disk. Possible values include:</p></li>
<li><p><strong>disk_size_gb</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Specifies the size of the managed disk to create in gigabytes.
If <code class="docutils literal notranslate"><span class="pre">create_option</span></code> is <code class="docutils literal notranslate"><span class="pre">Copy</span></code> or <code class="docutils literal notranslate"><span class="pre">FromImage</span></code>, then the value must be equal to or greater than the source’s size.</p></li>
<li><p><strong>encryption_settings</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – an <code class="docutils literal notranslate"><span class="pre">encryption_settings</span></code> block as defined below.</p></li>
<li><p><strong>image_reference_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – ID of an existing platform/marketplace disk image to copy when <code class="docutils literal notranslate"><span class="pre">create_option</span></code> is <code class="docutils literal notranslate"><span class="pre">FromImage</span></code>.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specified the supported Azure location where the resource exists.
Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the managed disk. Changing this forces a
new resource to be created.</p></li>
<li><p><strong>os_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specify a value when the source of an <code class="docutils literal notranslate"><span class="pre">Import</span></code> or <code class="docutils literal notranslate"><span class="pre">Copy</span></code>
operation targets a source that contains an operating system. Valid values are <code class="docutils literal notranslate"><span class="pre">Linux</span></code> or <code class="docutils literal notranslate"><span class="pre">Windows</span></code></p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create
the managed disk.</p></li>
<li><p><strong>source_resource_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – ID of an existing managed disk to copy <code class="docutils literal notranslate"><span class="pre">create_option</span></code> is <code class="docutils literal notranslate"><span class="pre">Copy</span></code>
or the recovery point to restore when <code class="docutils literal notranslate"><span class="pre">create_option</span></code> is <code class="docutils literal notranslate"><span class="pre">Restore</span></code></p></li>
<li><p><strong>source_uri</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – URI to a valid VHD file to be used when <code class="docutils literal notranslate"><span class="pre">create_option</span></code> is <code class="docutils literal notranslate"><span class="pre">Import</span></code>.</p></li>
<li><p><strong>storage_account_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of storage to use for the managed disk.
Allowable values are <code class="docutils literal notranslate"><span class="pre">Standard_LRS</span></code>, <code class="docutils literal notranslate"><span class="pre">Premium_LRS</span></code>, <code class="docutils literal notranslate"><span class="pre">StandardSSD_LRS</span></code> or <code class="docutils literal notranslate"><span class="pre">UltraSSD_LRS</span></code>.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
<li><p><strong>zones</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A collection containing the availability zone to allocate the Managed Disk in.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/managed_disk.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/managed_disk.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.compute.ManagedDisk.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.compute.ManagedDisk.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.compute.ManagedDisk.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.compute.ManagedDisk.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.compute.ScaleSet">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.compute.</code><code class="sig-name descname">ScaleSet</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">automatic_os_upgrade=None</em>, <em class="sig-param">boot_diagnostics=None</em>, <em class="sig-param">eviction_policy=None</em>, <em class="sig-param">extensions=None</em>, <em class="sig-param">health_probe_id=None</em>, <em class="sig-param">identity=None</em>, <em class="sig-param">license_type=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">network_profiles=None</em>, <em class="sig-param">os_profile=None</em>, <em class="sig-param">os_profile_linux_config=None</em>, <em class="sig-param">os_profile_secrets=None</em>, <em class="sig-param">os_profile_windows_config=None</em>, <em class="sig-param">overprovision=None</em>, <em class="sig-param">plan=None</em>, <em class="sig-param">priority=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">rolling_upgrade_policy=None</em>, <em class="sig-param">single_placement_group=None</em>, <em class="sig-param">sku=None</em>, <em class="sig-param">storage_profile_data_disks=None</em>, <em class="sig-param">storage_profile_image_reference=None</em>, <em class="sig-param">storage_profile_os_disk=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">upgrade_policy_mode=None</em>, <em class="sig-param">zones=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.compute.ScaleSet" title="Permalink to this definition">¶</a></dt>
<dd><p>Manage a virtual machine scale set.</p>
<blockquote>
<div><p><strong>Note:</strong> All arguments including the administrator login and password will be stored in the raw state as plain-text.
<a class="reference external" href="https://www.terraform.io/docs/state/sensitive-data.html">Read more about sensitive data in state</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>automatic_os_upgrade</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Automatic OS patches can be applied by Azure to your scaleset. This is particularly useful when <code class="docutils literal notranslate"><span class="pre">upgrade_policy_mode</span></code> is set to <code class="docutils literal notranslate"><span class="pre">Rolling</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>boot_diagnostics</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A boot diagnostics profile block as referenced below.</p></li>
<li><p><strong>eviction_policy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the eviction policy for Virtual Machines in this Scale Set. Possible values are <code class="docutils literal notranslate"><span class="pre">Deallocate</span></code> and <code class="docutils literal notranslate"><span class="pre">Delete</span></code>.</p></li>
<li><p><strong>extensions</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Can be specified multiple times to add extension profiles to the scale set. Each <code class="docutils literal notranslate"><span class="pre">extension</span></code> block supports the fields documented below.</p></li>
<li><p><strong>health_probe_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the identifier for the load balancer health probe. Required when using <code class="docutils literal notranslate"><span class="pre">Rolling</span></code> as your <code class="docutils literal notranslate"><span class="pre">upgrade_policy_mode</span></code>.</p></li>
<li><p><strong>license_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the Windows OS license type. If supplied, the only allowed values are <code class="docutils literal notranslate"><span class="pre">Windows_Client</span></code> and <code class="docutils literal notranslate"><span class="pre">Windows_Server</span></code>.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the image from the marketplace.</p></li>
<li><p><strong>network_profiles</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A collection of network profile block as documented below.</p></li>
<li><p><strong>os_profile</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A Virtual Machine OS Profile block as documented below.</p></li>
<li><p><strong>os_profile_linux_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A Linux config block as documented below.</p></li>
<li><p><strong>os_profile_secrets</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A collection of Secret blocks as documented below.</p></li>
<li><p><strong>os_profile_windows_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A Windows config block as documented below.</p></li>
<li><p><strong>overprovision</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specifies whether the virtual machine scale set should be overprovisioned.</p></li>
<li><p><strong>plan</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A plan block as documented below.</p></li>
<li><p><strong>priority</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the priority for the Virtual Machines in the Scale Set. Defaults to <code class="docutils literal notranslate"><span class="pre">Regular</span></code>. Possible values are <code class="docutils literal notranslate"><span class="pre">Low</span></code> and <code class="docutils literal notranslate"><span class="pre">Regular</span></code>.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the virtual machine scale set. Changing this forces a new resource to be created.</p></li>
<li><p><strong>rolling_upgrade_policy</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">rolling_upgrade_policy</span></code> block as defined below. This is only applicable when the <code class="docutils literal notranslate"><span class="pre">upgrade_policy_mode</span></code> is <code class="docutils literal notranslate"><span class="pre">Rolling</span></code>.</p></li>
<li><p><strong>single_placement_group</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specifies whether the scale set is limited to a single placement group with a maximum size of 100 virtual machines. If set to false, managed disks must be used. Default is true. Changing this forces a new resource to be created. See <a class="reference external" href="http://docs.microsoft.com/en-us/azure/virtual-machine-scale-sets/virtual-machine-scale-sets-placement-groups">documentation</a> for more information.</p></li>
<li><p><strong>sku</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Specifies the SKU of the image used to create the virtual machines.</p></li>
<li><p><strong>storage_profile_data_disks</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A storage profile data disk block as documented below</p></li>
<li><p><strong>storage_profile_image_reference</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A storage profile image reference block as documented below.</p></li>
<li><p><strong>storage_profile_os_disk</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A storage profile os disk block as documented below</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
<li><p><strong>upgrade_policy_mode</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the mode of an upgrade to virtual machines in the scale set. Possible values, <code class="docutils literal notranslate"><span class="pre">Rolling</span></code>, <code class="docutils literal notranslate"><span class="pre">Manual</span></code>, or <code class="docutils literal notranslate"><span class="pre">Automatic</span></code>. When choosing <code class="docutils literal notranslate"><span class="pre">Rolling</span></code>, you will need to set a health probe.</p></li>
<li><p><strong>zones</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A collection of availability zones to spread the Virtual Machines over.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/virtual_machine_scale_set.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/virtual_machine_scale_set.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_azure.compute.ScaleSet.automatic_os_upgrade">
<code class="sig-name descname">automatic_os_upgrade</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.ScaleSet.automatic_os_upgrade" title="Permalink to this definition">¶</a></dt>
<dd><p>Automatic OS patches can be applied by Azure to your scaleset. This is particularly useful when <code class="docutils literal notranslate"><span class="pre">upgrade_policy_mode</span></code> is set to <code class="docutils literal notranslate"><span class="pre">Rolling</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.ScaleSet.boot_diagnostics">
<code class="sig-name descname">boot_diagnostics</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.ScaleSet.boot_diagnostics" title="Permalink to this definition">¶</a></dt>
<dd><p>A boot diagnostics profile block as referenced below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.ScaleSet.eviction_policy">
<code class="sig-name descname">eviction_policy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.ScaleSet.eviction_policy" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the eviction policy for Virtual Machines in this Scale Set. Possible values are <code class="docutils literal notranslate"><span class="pre">Deallocate</span></code> and <code class="docutils literal notranslate"><span class="pre">Delete</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.ScaleSet.extensions">
<code class="sig-name descname">extensions</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.ScaleSet.extensions" title="Permalink to this definition">¶</a></dt>
<dd><p>Can be specified multiple times to add extension profiles to the scale set. Each <code class="docutils literal notranslate"><span class="pre">extension</span></code> block supports the fields documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.ScaleSet.health_probe_id">
<code class="sig-name descname">health_probe_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.ScaleSet.health_probe_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the identifier for the load balancer health probe. Required when using <code class="docutils literal notranslate"><span class="pre">Rolling</span></code> as your <code class="docutils literal notranslate"><span class="pre">upgrade_policy_mode</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.ScaleSet.license_type">
<code class="sig-name descname">license_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.ScaleSet.license_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the Windows OS license type. If supplied, the only allowed values are <code class="docutils literal notranslate"><span class="pre">Windows_Client</span></code> and <code class="docutils literal notranslate"><span class="pre">Windows_Server</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.ScaleSet.location">
<code class="sig-name descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.ScaleSet.location" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.ScaleSet.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.ScaleSet.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the image from the marketplace.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.ScaleSet.network_profiles">
<code class="sig-name descname">network_profiles</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.ScaleSet.network_profiles" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of network profile block as documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.ScaleSet.os_profile">
<code class="sig-name descname">os_profile</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.ScaleSet.os_profile" title="Permalink to this definition">¶</a></dt>
<dd><p>A Virtual Machine OS Profile block as documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.ScaleSet.os_profile_linux_config">
<code class="sig-name descname">os_profile_linux_config</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.ScaleSet.os_profile_linux_config" title="Permalink to this definition">¶</a></dt>
<dd><p>A Linux config block as documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.ScaleSet.os_profile_secrets">
<code class="sig-name descname">os_profile_secrets</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.ScaleSet.os_profile_secrets" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of Secret blocks as documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.ScaleSet.os_profile_windows_config">
<code class="sig-name descname">os_profile_windows_config</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.ScaleSet.os_profile_windows_config" title="Permalink to this definition">¶</a></dt>
<dd><p>A Windows config block as documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.ScaleSet.overprovision">
<code class="sig-name descname">overprovision</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.ScaleSet.overprovision" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies whether the virtual machine scale set should be overprovisioned.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.ScaleSet.plan">
<code class="sig-name descname">plan</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.ScaleSet.plan" title="Permalink to this definition">¶</a></dt>
<dd><p>A plan block as documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.ScaleSet.priority">
<code class="sig-name descname">priority</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.ScaleSet.priority" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the priority for the Virtual Machines in the Scale Set. Defaults to <code class="docutils literal notranslate"><span class="pre">Regular</span></code>. Possible values are <code class="docutils literal notranslate"><span class="pre">Low</span></code> and <code class="docutils literal notranslate"><span class="pre">Regular</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.ScaleSet.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.ScaleSet.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to create the virtual machine scale set. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.ScaleSet.rolling_upgrade_policy">
<code class="sig-name descname">rolling_upgrade_policy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.ScaleSet.rolling_upgrade_policy" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">rolling_upgrade_policy</span></code> block as defined below. This is only applicable when the <code class="docutils literal notranslate"><span class="pre">upgrade_policy_mode</span></code> is <code class="docutils literal notranslate"><span class="pre">Rolling</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.ScaleSet.single_placement_group">
<code class="sig-name descname">single_placement_group</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.ScaleSet.single_placement_group" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies whether the scale set is limited to a single placement group with a maximum size of 100 virtual machines. If set to false, managed disks must be used. Default is true. Changing this forces a new resource to be created. See <a class="reference external" href="http://docs.microsoft.com/en-us/azure/virtual-machine-scale-sets/virtual-machine-scale-sets-placement-groups">documentation</a> for more information.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.ScaleSet.sku">
<code class="sig-name descname">sku</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.ScaleSet.sku" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the SKU of the image used to create the virtual machines.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.ScaleSet.storage_profile_data_disks">
<code class="sig-name descname">storage_profile_data_disks</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.ScaleSet.storage_profile_data_disks" title="Permalink to this definition">¶</a></dt>
<dd><p>A storage profile data disk block as documented below</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.ScaleSet.storage_profile_image_reference">
<code class="sig-name descname">storage_profile_image_reference</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.ScaleSet.storage_profile_image_reference" title="Permalink to this definition">¶</a></dt>
<dd><p>A storage profile image reference block as documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.ScaleSet.storage_profile_os_disk">
<code class="sig-name descname">storage_profile_os_disk</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.ScaleSet.storage_profile_os_disk" title="Permalink to this definition">¶</a></dt>
<dd><p>A storage profile os disk block as documented below</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.ScaleSet.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.ScaleSet.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.ScaleSet.upgrade_policy_mode">
<code class="sig-name descname">upgrade_policy_mode</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.ScaleSet.upgrade_policy_mode" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the mode of an upgrade to virtual machines in the scale set. Possible values, <code class="docutils literal notranslate"><span class="pre">Rolling</span></code>, <code class="docutils literal notranslate"><span class="pre">Manual</span></code>, or <code class="docutils literal notranslate"><span class="pre">Automatic</span></code>. When choosing <code class="docutils literal notranslate"><span class="pre">Rolling</span></code>, you will need to set a health probe.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.ScaleSet.zones">
<code class="sig-name descname">zones</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.ScaleSet.zones" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of availability zones to spread the Virtual Machines over.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.compute.ScaleSet.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">automatic_os_upgrade=None</em>, <em class="sig-param">boot_diagnostics=None</em>, <em class="sig-param">eviction_policy=None</em>, <em class="sig-param">extensions=None</em>, <em class="sig-param">health_probe_id=None</em>, <em class="sig-param">identity=None</em>, <em class="sig-param">license_type=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">network_profiles=None</em>, <em class="sig-param">os_profile=None</em>, <em class="sig-param">os_profile_linux_config=None</em>, <em class="sig-param">os_profile_secrets=None</em>, <em class="sig-param">os_profile_windows_config=None</em>, <em class="sig-param">overprovision=None</em>, <em class="sig-param">plan=None</em>, <em class="sig-param">priority=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">rolling_upgrade_policy=None</em>, <em class="sig-param">single_placement_group=None</em>, <em class="sig-param">sku=None</em>, <em class="sig-param">storage_profile_data_disks=None</em>, <em class="sig-param">storage_profile_image_reference=None</em>, <em class="sig-param">storage_profile_os_disk=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">upgrade_policy_mode=None</em>, <em class="sig-param">zones=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.compute.ScaleSet.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ScaleSet resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>automatic_os_upgrade</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Automatic OS patches can be applied by Azure to your scaleset. This is particularly useful when <code class="docutils literal notranslate"><span class="pre">upgrade_policy_mode</span></code> is set to <code class="docutils literal notranslate"><span class="pre">Rolling</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>boot_diagnostics</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A boot diagnostics profile block as referenced below.</p></li>
<li><p><strong>eviction_policy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the eviction policy for Virtual Machines in this Scale Set. Possible values are <code class="docutils literal notranslate"><span class="pre">Deallocate</span></code> and <code class="docutils literal notranslate"><span class="pre">Delete</span></code>.</p></li>
<li><p><strong>extensions</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Can be specified multiple times to add extension profiles to the scale set. Each <code class="docutils literal notranslate"><span class="pre">extension</span></code> block supports the fields documented below.</p></li>
<li><p><strong>health_probe_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the identifier for the load balancer health probe. Required when using <code class="docutils literal notranslate"><span class="pre">Rolling</span></code> as your <code class="docutils literal notranslate"><span class="pre">upgrade_policy_mode</span></code>.</p></li>
<li><p><strong>license_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the Windows OS license type. If supplied, the only allowed values are <code class="docutils literal notranslate"><span class="pre">Windows_Client</span></code> and <code class="docutils literal notranslate"><span class="pre">Windows_Server</span></code>.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the image from the marketplace.</p></li>
<li><p><strong>network_profiles</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A collection of network profile block as documented below.</p></li>
<li><p><strong>os_profile</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A Virtual Machine OS Profile block as documented below.</p></li>
<li><p><strong>os_profile_linux_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A Linux config block as documented below.</p></li>
<li><p><strong>os_profile_secrets</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A collection of Secret blocks as documented below.</p></li>
<li><p><strong>os_profile_windows_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A Windows config block as documented below.</p></li>
<li><p><strong>overprovision</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specifies whether the virtual machine scale set should be overprovisioned.</p></li>
<li><p><strong>plan</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A plan block as documented below.</p></li>
<li><p><strong>priority</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the priority for the Virtual Machines in the Scale Set. Defaults to <code class="docutils literal notranslate"><span class="pre">Regular</span></code>. Possible values are <code class="docutils literal notranslate"><span class="pre">Low</span></code> and <code class="docutils literal notranslate"><span class="pre">Regular</span></code>.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the virtual machine scale set. Changing this forces a new resource to be created.</p></li>
<li><p><strong>rolling_upgrade_policy</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">rolling_upgrade_policy</span></code> block as defined below. This is only applicable when the <code class="docutils literal notranslate"><span class="pre">upgrade_policy_mode</span></code> is <code class="docutils literal notranslate"><span class="pre">Rolling</span></code>.</p></li>
<li><p><strong>single_placement_group</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – <p>Specifies whether the scale set is limited to a single placement group with a maximum size of 100 virtual machines. If set to false, managed disks must be used. Default is true. Changing this forces a new resource to be created. See <a class="reference external" href="http://docs.microsoft.com/en-us/azure/virtual-machine-scale-sets/virtual-machine-scale-sets-placement-groups">documentation</a> for more information.</p>
</p></li>
<li><p><strong>sku</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Specifies the SKU of the image used to create the virtual machines.</p></li>
<li><p><strong>storage_profile_data_disks</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A storage profile data disk block as documented below</p></li>
<li><p><strong>storage_profile_image_reference</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A storage profile image reference block as documented below.</p></li>
<li><p><strong>storage_profile_os_disk</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A storage profile os disk block as documented below</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
<li><p><strong>upgrade_policy_mode</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the mode of an upgrade to virtual machines in the scale set. Possible values, <code class="docutils literal notranslate"><span class="pre">Rolling</span></code>, <code class="docutils literal notranslate"><span class="pre">Manual</span></code>, or <code class="docutils literal notranslate"><span class="pre">Automatic</span></code>. When choosing <code class="docutils literal notranslate"><span class="pre">Rolling</span></code>, you will need to set a health probe.</p></li>
<li><p><strong>zones</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A collection of availability zones to spread the Virtual Machines over.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/virtual_machine_scale_set.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/virtual_machine_scale_set.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.compute.ScaleSet.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.compute.ScaleSet.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.compute.ScaleSet.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.compute.ScaleSet.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.compute.SharedImage">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.compute.</code><code class="sig-name descname">SharedImage</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">eula=None</em>, <em class="sig-param">gallery_name=None</em>, <em class="sig-param">identifier=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">os_type=None</em>, <em class="sig-param">privacy_statement_uri=None</em>, <em class="sig-param">release_note_uri=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.compute.SharedImage" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Shared Image within a Shared Image Gallery.</p>
<blockquote>
<div><p><strong>NOTE</strong> Shared Image Galleries are currently in Public Preview. You can find more information, including <a class="reference external" href="https://azure.microsoft.com/en-gb/blog/announcing-the-public-preview-of-shared-image-gallery/">how to register for the Public Preview here</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A description of this Shared Image.</p></li>
<li><p><strong>eula</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The End User Licence Agreement for the Shared Image.</p></li>
<li><p><strong>gallery_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Shared Image Gallery in which this Shared Image should exist. Changing this forces a new resource to be created.</p></li>
<li><p><strong>identifier</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – An <code class="docutils literal notranslate"><span class="pre">identifier</span></code> block as defined below.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the Shared Image Gallery exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Shared Image. Changing this forces a new resource to be created.</p></li>
<li><p><strong>os_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of Operating System present in this Shared Image. Possible values are <code class="docutils literal notranslate"><span class="pre">Linux</span></code> and <code class="docutils literal notranslate"><span class="pre">Windows</span></code>.</p></li>
<li><p><strong>privacy_statement_uri</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The URI containing the Privacy Statement associated with this Shared Image.</p></li>
<li><p><strong>release_note_uri</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The URI containing the Release Notes associated with this Shared Image.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which the Shared Image Gallery exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the Shared Image.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/shared_image.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/shared_image.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_azure.compute.SharedImage.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.SharedImage.description" title="Permalink to this definition">¶</a></dt>
<dd><p>A description of this Shared Image.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.SharedImage.eula">
<code class="sig-name descname">eula</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.SharedImage.eula" title="Permalink to this definition">¶</a></dt>
<dd><p>The End User Licence Agreement for the Shared Image.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.SharedImage.gallery_name">
<code class="sig-name descname">gallery_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.SharedImage.gallery_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Shared Image Gallery in which this Shared Image should exist. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.SharedImage.identifier">
<code class="sig-name descname">identifier</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.SharedImage.identifier" title="Permalink to this definition">¶</a></dt>
<dd><p>An <code class="docutils literal notranslate"><span class="pre">identifier</span></code> block as defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.SharedImage.location">
<code class="sig-name descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.SharedImage.location" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the supported Azure location where the Shared Image Gallery exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.SharedImage.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.SharedImage.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Shared Image. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.SharedImage.os_type">
<code class="sig-name descname">os_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.SharedImage.os_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of Operating System present in this Shared Image. Possible values are <code class="docutils literal notranslate"><span class="pre">Linux</span></code> and <code class="docutils literal notranslate"><span class="pre">Windows</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.SharedImage.privacy_statement_uri">
<code class="sig-name descname">privacy_statement_uri</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.SharedImage.privacy_statement_uri" title="Permalink to this definition">¶</a></dt>
<dd><p>The URI containing the Privacy Statement associated with this Shared Image.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.SharedImage.release_note_uri">
<code class="sig-name descname">release_note_uri</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.SharedImage.release_note_uri" title="Permalink to this definition">¶</a></dt>
<dd><p>The URI containing the Release Notes associated with this Shared Image.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.SharedImage.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.SharedImage.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which the Shared Image Gallery exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.SharedImage.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.SharedImage.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the Shared Image.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.compute.SharedImage.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">eula=None</em>, <em class="sig-param">gallery_name=None</em>, <em class="sig-param">identifier=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">os_type=None</em>, <em class="sig-param">privacy_statement_uri=None</em>, <em class="sig-param">release_note_uri=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.compute.SharedImage.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing SharedImage resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A description of this Shared Image.</p></li>
<li><p><strong>eula</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The End User Licence Agreement for the Shared Image.</p></li>
<li><p><strong>gallery_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Shared Image Gallery in which this Shared Image should exist. Changing this forces a new resource to be created.</p></li>
<li><p><strong>identifier</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – An <code class="docutils literal notranslate"><span class="pre">identifier</span></code> block as defined below.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the Shared Image Gallery exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Shared Image. Changing this forces a new resource to be created.</p></li>
<li><p><strong>os_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of Operating System present in this Shared Image. Possible values are <code class="docutils literal notranslate"><span class="pre">Linux</span></code> and <code class="docutils literal notranslate"><span class="pre">Windows</span></code>.</p></li>
<li><p><strong>privacy_statement_uri</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The URI containing the Privacy Statement associated with this Shared Image.</p></li>
<li><p><strong>release_note_uri</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The URI containing the Release Notes associated with this Shared Image.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which the Shared Image Gallery exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the Shared Image.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/shared_image.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/shared_image.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.compute.SharedImage.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.compute.SharedImage.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.compute.SharedImage.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.compute.SharedImage.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.compute.SharedImageGallery">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.compute.</code><code class="sig-name descname">SharedImageGallery</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.compute.SharedImageGallery" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Shared Image Gallery.</p>
<blockquote>
<div><p><strong>NOTE</strong> Shared Image Galleries are currently in Public Preview. You can find more information, including <a class="reference external" href="https://azure.microsoft.com/en-gb/blog/announcing-the-public-preview-of-shared-image-gallery/">how to register for the Public Preview here</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A description for this Shared Image Gallery.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Shared Image Gallery. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the Shared Image Gallery. Changing this forces a new resource to be created.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the Shared Image Gallery.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/shared_image_gallery.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/shared_image_gallery.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_azure.compute.SharedImageGallery.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.SharedImageGallery.description" title="Permalink to this definition">¶</a></dt>
<dd><p>A description for this Shared Image Gallery.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.SharedImageGallery.location">
<code class="sig-name descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.SharedImageGallery.location" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.SharedImageGallery.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.SharedImageGallery.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Shared Image Gallery. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.SharedImageGallery.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.SharedImageGallery.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to create the Shared Image Gallery. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.SharedImageGallery.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.SharedImageGallery.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the Shared Image Gallery.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.SharedImageGallery.unique_name">
<code class="sig-name descname">unique_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.SharedImageGallery.unique_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The Unique Name for this Shared Image Gallery.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.compute.SharedImageGallery.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">unique_name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.compute.SharedImageGallery.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing SharedImageGallery resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A description for this Shared Image Gallery.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Shared Image Gallery. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the Shared Image Gallery. Changing this forces a new resource to be created.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the Shared Image Gallery.</p></li>
<li><p><strong>unique_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Unique Name for this Shared Image Gallery.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/shared_image_gallery.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/shared_image_gallery.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.compute.SharedImageGallery.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.compute.SharedImageGallery.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.compute.SharedImageGallery.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.compute.SharedImageGallery.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.compute.SharedImageVersion">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.compute.</code><code class="sig-name descname">SharedImageVersion</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">exclude_from_latest=None</em>, <em class="sig-param">gallery_name=None</em>, <em class="sig-param">image_name=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">managed_image_id=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">target_regions=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.compute.SharedImageVersion" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Version of a Shared Image within a Shared Image Gallery.</p>
<blockquote>
<div><p><strong>NOTE</strong> Shared Image Galleries are currently in Public Preview. You can find more information, including <a class="reference external" href="https://azure.microsoft.com/en-gb/blog/announcing-the-public-preview-of-shared-image-gallery/">how to register for the Public Preview here</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>exclude_from_latest</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Should this Image Version be excluded from the <code class="docutils literal notranslate"><span class="pre">latest</span></code> filter? If set to <code class="docutils literal notranslate"><span class="pre">true</span></code> this Image Version won’t be returned for the <code class="docutils literal notranslate"><span class="pre">latest</span></code> version. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>gallery_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Shared Image Gallery in which the Shared Image exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>image_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Shared Image within the Shared Image Gallery in which this Version should be created. Changing this forces a new resource to be created.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Azure Region in which the Shared Image Gallery exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>managed_image_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Managed Image which should be used for this Shared Image Version. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The version number for this Image Version, such as <code class="docutils literal notranslate"><span class="pre">1.0.0</span></code>. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Resource Group in which the Shared Image Gallery exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A collection of tags which should be applied to this resource.</p></li>
<li><p><strong>target_regions</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">target_region</span></code> blocks as documented below.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/shared_image_version.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/shared_image_version.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_azure.compute.SharedImageVersion.exclude_from_latest">
<code class="sig-name descname">exclude_from_latest</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.SharedImageVersion.exclude_from_latest" title="Permalink to this definition">¶</a></dt>
<dd><p>Should this Image Version be excluded from the <code class="docutils literal notranslate"><span class="pre">latest</span></code> filter? If set to <code class="docutils literal notranslate"><span class="pre">true</span></code> this Image Version won’t be returned for the <code class="docutils literal notranslate"><span class="pre">latest</span></code> version. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.SharedImageVersion.gallery_name">
<code class="sig-name descname">gallery_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.SharedImageVersion.gallery_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Shared Image Gallery in which the Shared Image exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.SharedImageVersion.image_name">
<code class="sig-name descname">image_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.SharedImageVersion.image_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Shared Image within the Shared Image Gallery in which this Version should be created. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.SharedImageVersion.location">
<code class="sig-name descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.SharedImageVersion.location" title="Permalink to this definition">¶</a></dt>
<dd><p>The Azure Region in which the Shared Image Gallery exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.SharedImageVersion.managed_image_id">
<code class="sig-name descname">managed_image_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.SharedImageVersion.managed_image_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Managed Image which should be used for this Shared Image Version. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.SharedImageVersion.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.SharedImageVersion.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The version number for this Image Version, such as <code class="docutils literal notranslate"><span class="pre">1.0.0</span></code>. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.SharedImageVersion.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.SharedImageVersion.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Resource Group in which the Shared Image Gallery exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.SharedImageVersion.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.SharedImageVersion.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of tags which should be applied to this resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.SharedImageVersion.target_regions">
<code class="sig-name descname">target_regions</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.SharedImageVersion.target_regions" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more <code class="docutils literal notranslate"><span class="pre">target_region</span></code> blocks as documented below.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.compute.SharedImageVersion.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">exclude_from_latest=None</em>, <em class="sig-param">gallery_name=None</em>, <em class="sig-param">image_name=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">managed_image_id=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">target_regions=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.compute.SharedImageVersion.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing SharedImageVersion resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>exclude_from_latest</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Should this Image Version be excluded from the <code class="docutils literal notranslate"><span class="pre">latest</span></code> filter? If set to <code class="docutils literal notranslate"><span class="pre">true</span></code> this Image Version won’t be returned for the <code class="docutils literal notranslate"><span class="pre">latest</span></code> version. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>gallery_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Shared Image Gallery in which the Shared Image exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>image_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Shared Image within the Shared Image Gallery in which this Version should be created. Changing this forces a new resource to be created.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Azure Region in which the Shared Image Gallery exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>managed_image_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Managed Image which should be used for this Shared Image Version. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The version number for this Image Version, such as <code class="docutils literal notranslate"><span class="pre">1.0.0</span></code>. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Resource Group in which the Shared Image Gallery exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A collection of tags which should be applied to this resource.</p></li>
<li><p><strong>target_regions</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">target_region</span></code> blocks as documented below.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/shared_image_version.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/shared_image_version.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.compute.SharedImageVersion.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.compute.SharedImageVersion.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.compute.SharedImageVersion.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.compute.SharedImageVersion.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.compute.Snapshot">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.compute.</code><code class="sig-name descname">Snapshot</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">create_option=None</em>, <em class="sig-param">disk_size_gb=None</em>, <em class="sig-param">encryption_settings=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">source_resource_id=None</em>, <em class="sig-param">source_uri=None</em>, <em class="sig-param">storage_account_id=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.compute.Snapshot" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Disk Snapshot.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>create_option</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Indicates how the snapshot is to be created. Possible values are <code class="docutils literal notranslate"><span class="pre">Copy</span></code> or <code class="docutils literal notranslate"><span class="pre">Import</span></code>. Changing this forces a new resource to be created.</p></li>
<li><p><strong>disk_size_gb</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The size of the Snapshotted Disk in GB.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Snapshot resource. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the Snapshot. Changing this forces a new resource to be created.</p></li>
<li><p><strong>source_resource_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies a reference to an existing snapshot, when <code class="docutils literal notranslate"><span class="pre">create_option</span></code> is <code class="docutils literal notranslate"><span class="pre">Copy</span></code>. Changing this forces a new resource to be created.</p></li>
<li><p><strong>source_uri</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the URI to a Managed or Unmanaged Disk. Changing this forces a new resource to be created.</p></li>
<li><p><strong>storage_account_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the ID of an storage account. Used with <code class="docutils literal notranslate"><span class="pre">source_uri</span></code> to allow authorization during import of unmanaged blobs from a different subscription. Changing this forces a new resource to be created.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/snapshot.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/snapshot.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_azure.compute.Snapshot.create_option">
<code class="sig-name descname">create_option</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.Snapshot.create_option" title="Permalink to this definition">¶</a></dt>
<dd><p>Indicates how the snapshot is to be created. Possible values are <code class="docutils literal notranslate"><span class="pre">Copy</span></code> or <code class="docutils literal notranslate"><span class="pre">Import</span></code>. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.Snapshot.disk_size_gb">
<code class="sig-name descname">disk_size_gb</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.Snapshot.disk_size_gb" title="Permalink to this definition">¶</a></dt>
<dd><p>The size of the Snapshotted Disk in GB.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.Snapshot.location">
<code class="sig-name descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.Snapshot.location" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.Snapshot.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.Snapshot.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Snapshot resource. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.Snapshot.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.Snapshot.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to create the Snapshot. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.Snapshot.source_resource_id">
<code class="sig-name descname">source_resource_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.Snapshot.source_resource_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies a reference to an existing snapshot, when <code class="docutils literal notranslate"><span class="pre">create_option</span></code> is <code class="docutils literal notranslate"><span class="pre">Copy</span></code>. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.Snapshot.source_uri">
<code class="sig-name descname">source_uri</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.Snapshot.source_uri" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the URI to a Managed or Unmanaged Disk. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.Snapshot.storage_account_id">
<code class="sig-name descname">storage_account_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.Snapshot.storage_account_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the ID of an storage account. Used with <code class="docutils literal notranslate"><span class="pre">source_uri</span></code> to allow authorization during import of unmanaged blobs from a different subscription. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.Snapshot.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.Snapshot.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.compute.Snapshot.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">create_option=None</em>, <em class="sig-param">disk_size_gb=None</em>, <em class="sig-param">encryption_settings=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">source_resource_id=None</em>, <em class="sig-param">source_uri=None</em>, <em class="sig-param">storage_account_id=None</em>, <em class="sig-param">tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.compute.Snapshot.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Snapshot resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>create_option</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Indicates how the snapshot is to be created. Possible values are <code class="docutils literal notranslate"><span class="pre">Copy</span></code> or <code class="docutils literal notranslate"><span class="pre">Import</span></code>. Changing this forces a new resource to be created.</p></li>
<li><p><strong>disk_size_gb</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The size of the Snapshotted Disk in GB.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Snapshot resource. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the Snapshot. Changing this forces a new resource to be created.</p></li>
<li><p><strong>source_resource_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies a reference to an existing snapshot, when <code class="docutils literal notranslate"><span class="pre">create_option</span></code> is <code class="docutils literal notranslate"><span class="pre">Copy</span></code>. Changing this forces a new resource to be created.</p></li>
<li><p><strong>source_uri</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the URI to a Managed or Unmanaged Disk. Changing this forces a new resource to be created.</p></li>
<li><p><strong>storage_account_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the ID of an storage account. Used with <code class="docutils literal notranslate"><span class="pre">source_uri</span></code> to allow authorization during import of unmanaged blobs from a different subscription. Changing this forces a new resource to be created.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/snapshot.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/snapshot.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.compute.Snapshot.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.compute.Snapshot.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.compute.Snapshot.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.compute.Snapshot.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.compute.VirtualMachine">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.compute.</code><code class="sig-name descname">VirtualMachine</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">availability_set_id=None</em>, <em class="sig-param">boot_diagnostics=None</em>, <em class="sig-param">delete_data_disks_on_termination=None</em>, <em class="sig-param">delete_os_disk_on_termination=None</em>, <em class="sig-param">identity=None</em>, <em class="sig-param">license_type=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">network_interface_ids=None</em>, <em class="sig-param">os_profile=None</em>, <em class="sig-param">os_profile_linux_config=None</em>, <em class="sig-param">os_profile_secrets=None</em>, <em class="sig-param">os_profile_windows_config=None</em>, <em class="sig-param">plan=None</em>, <em class="sig-param">primary_network_interface_id=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">storage_data_disks=None</em>, <em class="sig-param">storage_image_reference=None</em>, <em class="sig-param">storage_os_disk=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">vm_size=None</em>, <em class="sig-param">zones=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.compute.VirtualMachine" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Virtual Machine.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Data Disks can be attached either directly on the <code class="docutils literal notranslate"><span class="pre">compute.VirtualMachine</span></code> resource, or using the <code class="docutils literal notranslate"><span class="pre">compute.DataDiskAttachment</span></code> resource - but the two cannot be used together. If both are used against the same Virtual Machine, spurious changes will occur.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>availability_set_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Availability Set in which the Virtual Machine should exist. Changing this forces a new resource to be created.</p></li>
<li><p><strong>boot_diagnostics</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">boot_diagnostics</span></code> block.</p></li>
<li><p><strong>delete_data_disks_on_termination</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Should the Data Disks (either the Managed Disks / VHD Blobs) be deleted when the Virtual Machine is destroyed? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>delete_os_disk_on_termination</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Should the OS Disk (either the Managed Disk / VHD Blob) be deleted when the Virtual Machine is destroyed? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>identity</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">identity</span></code> block.</p></li>
<li><p><strong>license_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the BYOL Type for this Virtual Machine. This is only applicable to Windows Virtual Machines. Possible values are <code class="docutils literal notranslate"><span class="pre">Windows_Client</span></code> and <code class="docutils literal notranslate"><span class="pre">Windows_Server</span></code>.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the Azure Region where the Virtual Machine exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Virtual Machine. Changing this forces a new resource to be created.</p></li>
<li><p><strong>network_interface_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of Network Interface ID’s which should be associated with the Virtual Machine.</p></li>
<li><p><strong>os_profile</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – An <code class="docutils literal notranslate"><span class="pre">os_profile</span></code> block. Required when <code class="docutils literal notranslate"><span class="pre">create_option</span></code> in the <code class="docutils literal notranslate"><span class="pre">storage_os_disk</span></code> block is set to <code class="docutils literal notranslate"><span class="pre">FromImage</span></code>.</p></li>
<li><p><strong>os_profile_linux_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">os_profile_linux_config</span></code> block.</p></li>
<li><p><strong>os_profile_secrets</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">os_profile_secrets</span></code> blocks.</p></li>
<li><p><strong>os_profile_windows_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">os_profile_windows_config</span></code> block.</p></li>
<li><p><strong>plan</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">plan</span></code> block.</p></li>
<li><p><strong>primary_network_interface_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Network Interface (which must be attached to the Virtual Machine) which should be the Primary Network Interface for this Virtual Machine.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Resource Group in which the Virtual Machine should exist. Changing this forces a new resource to be created.</p></li>
<li><p><strong>storage_data_disks</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">storage_data_disk</span></code> blocks.</p></li>
<li><p><strong>storage_image_reference</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">storage_image_reference</span></code> block.</p></li>
<li><p><strong>storage_os_disk</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">storage_os_disk</span></code> block.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the Virtual Machine.</p></li>
<li><p><strong>vm_size</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the <a class="reference external" href="https://azure.microsoft.com/en-us/documentation/articles/virtual-machines-size-specs/">size of the Virtual Machine</a>.</p></li>
<li><p><strong>zones</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A list of a single item of the Availability Zone which the Virtual Machine should be allocated in.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/virtual_machine.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/virtual_machine.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_azure.compute.VirtualMachine.availability_set_id">
<code class="sig-name descname">availability_set_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.VirtualMachine.availability_set_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Availability Set in which the Virtual Machine should exist. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.VirtualMachine.boot_diagnostics">
<code class="sig-name descname">boot_diagnostics</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.VirtualMachine.boot_diagnostics" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">boot_diagnostics</span></code> block.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.VirtualMachine.delete_data_disks_on_termination">
<code class="sig-name descname">delete_data_disks_on_termination</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.VirtualMachine.delete_data_disks_on_termination" title="Permalink to this definition">¶</a></dt>
<dd><p>Should the Data Disks (either the Managed Disks / VHD Blobs) be deleted when the Virtual Machine is destroyed? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.VirtualMachine.delete_os_disk_on_termination">
<code class="sig-name descname">delete_os_disk_on_termination</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.VirtualMachine.delete_os_disk_on_termination" title="Permalink to this definition">¶</a></dt>
<dd><p>Should the OS Disk (either the Managed Disk / VHD Blob) be deleted when the Virtual Machine is destroyed? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.VirtualMachine.identity">
<code class="sig-name descname">identity</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.VirtualMachine.identity" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">identity</span></code> block.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.VirtualMachine.license_type">
<code class="sig-name descname">license_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.VirtualMachine.license_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the BYOL Type for this Virtual Machine. This is only applicable to Windows Virtual Machines. Possible values are <code class="docutils literal notranslate"><span class="pre">Windows_Client</span></code> and <code class="docutils literal notranslate"><span class="pre">Windows_Server</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.VirtualMachine.location">
<code class="sig-name descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.VirtualMachine.location" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the Azure Region where the Virtual Machine exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.VirtualMachine.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.VirtualMachine.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Virtual Machine. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.VirtualMachine.network_interface_ids">
<code class="sig-name descname">network_interface_ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.VirtualMachine.network_interface_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of Network Interface ID’s which should be associated with the Virtual Machine.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.VirtualMachine.os_profile">
<code class="sig-name descname">os_profile</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.VirtualMachine.os_profile" title="Permalink to this definition">¶</a></dt>
<dd><p>An <code class="docutils literal notranslate"><span class="pre">os_profile</span></code> block. Required when <code class="docutils literal notranslate"><span class="pre">create_option</span></code> in the <code class="docutils literal notranslate"><span class="pre">storage_os_disk</span></code> block is set to <code class="docutils literal notranslate"><span class="pre">FromImage</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.VirtualMachine.os_profile_linux_config">
<code class="sig-name descname">os_profile_linux_config</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.VirtualMachine.os_profile_linux_config" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">os_profile_linux_config</span></code> block.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.VirtualMachine.os_profile_secrets">
<code class="sig-name descname">os_profile_secrets</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.VirtualMachine.os_profile_secrets" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more <code class="docutils literal notranslate"><span class="pre">os_profile_secrets</span></code> blocks.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.VirtualMachine.os_profile_windows_config">
<code class="sig-name descname">os_profile_windows_config</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.VirtualMachine.os_profile_windows_config" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">os_profile_windows_config</span></code> block.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.VirtualMachine.plan">
<code class="sig-name descname">plan</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.VirtualMachine.plan" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">plan</span></code> block.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.VirtualMachine.primary_network_interface_id">
<code class="sig-name descname">primary_network_interface_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.VirtualMachine.primary_network_interface_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Network Interface (which must be attached to the Virtual Machine) which should be the Primary Network Interface for this Virtual Machine.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.VirtualMachine.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.VirtualMachine.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Resource Group in which the Virtual Machine should exist. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.VirtualMachine.storage_data_disks">
<code class="sig-name descname">storage_data_disks</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.VirtualMachine.storage_data_disks" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more <code class="docutils literal notranslate"><span class="pre">storage_data_disk</span></code> blocks.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.VirtualMachine.storage_image_reference">
<code class="sig-name descname">storage_image_reference</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.VirtualMachine.storage_image_reference" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">storage_image_reference</span></code> block.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.VirtualMachine.storage_os_disk">
<code class="sig-name descname">storage_os_disk</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.VirtualMachine.storage_os_disk" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">storage_os_disk</span></code> block.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.VirtualMachine.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.VirtualMachine.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the Virtual Machine.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.VirtualMachine.vm_size">
<code class="sig-name descname">vm_size</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.VirtualMachine.vm_size" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the <a class="reference external" href="https://azure.microsoft.com/en-us/documentation/articles/virtual-machines-size-specs/">size of the Virtual Machine</a>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.VirtualMachine.zones">
<code class="sig-name descname">zones</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.VirtualMachine.zones" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of a single item of the Availability Zone which the Virtual Machine should be allocated in.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.compute.VirtualMachine.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">availability_set_id=None</em>, <em class="sig-param">boot_diagnostics=None</em>, <em class="sig-param">delete_data_disks_on_termination=None</em>, <em class="sig-param">delete_os_disk_on_termination=None</em>, <em class="sig-param">identity=None</em>, <em class="sig-param">license_type=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">network_interface_ids=None</em>, <em class="sig-param">os_profile=None</em>, <em class="sig-param">os_profile_linux_config=None</em>, <em class="sig-param">os_profile_secrets=None</em>, <em class="sig-param">os_profile_windows_config=None</em>, <em class="sig-param">plan=None</em>, <em class="sig-param">primary_network_interface_id=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">storage_data_disks=None</em>, <em class="sig-param">storage_image_reference=None</em>, <em class="sig-param">storage_os_disk=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">vm_size=None</em>, <em class="sig-param">zones=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.compute.VirtualMachine.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing VirtualMachine resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>availability_set_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Availability Set in which the Virtual Machine should exist. Changing this forces a new resource to be created.</p></li>
<li><p><strong>boot_diagnostics</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">boot_diagnostics</span></code> block.</p></li>
<li><p><strong>delete_data_disks_on_termination</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Should the Data Disks (either the Managed Disks / VHD Blobs) be deleted when the Virtual Machine is destroyed? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>delete_os_disk_on_termination</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Should the OS Disk (either the Managed Disk / VHD Blob) be deleted when the Virtual Machine is destroyed? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>identity</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">identity</span></code> block.</p></li>
<li><p><strong>license_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the BYOL Type for this Virtual Machine. This is only applicable to Windows Virtual Machines. Possible values are <code class="docutils literal notranslate"><span class="pre">Windows_Client</span></code> and <code class="docutils literal notranslate"><span class="pre">Windows_Server</span></code>.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the Azure Region where the Virtual Machine exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Virtual Machine. Changing this forces a new resource to be created.</p></li>
<li><p><strong>network_interface_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of Network Interface ID’s which should be associated with the Virtual Machine.</p></li>
<li><p><strong>os_profile</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – An <code class="docutils literal notranslate"><span class="pre">os_profile</span></code> block. Required when <code class="docutils literal notranslate"><span class="pre">create_option</span></code> in the <code class="docutils literal notranslate"><span class="pre">storage_os_disk</span></code> block is set to <code class="docutils literal notranslate"><span class="pre">FromImage</span></code>.</p></li>
<li><p><strong>os_profile_linux_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">os_profile_linux_config</span></code> block.</p></li>
<li><p><strong>os_profile_secrets</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">os_profile_secrets</span></code> blocks.</p></li>
<li><p><strong>os_profile_windows_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">os_profile_windows_config</span></code> block.</p></li>
<li><p><strong>plan</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">plan</span></code> block.</p></li>
<li><p><strong>primary_network_interface_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Network Interface (which must be attached to the Virtual Machine) which should be the Primary Network Interface for this Virtual Machine.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Resource Group in which the Virtual Machine should exist. Changing this forces a new resource to be created.</p></li>
<li><p><strong>storage_data_disks</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">storage_data_disk</span></code> blocks.</p></li>
<li><p><strong>storage_image_reference</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">storage_image_reference</span></code> block.</p></li>
<li><p><strong>storage_os_disk</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">storage_os_disk</span></code> block.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the Virtual Machine.</p></li>
<li><p><strong>vm_size</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>Specifies the <a class="reference external" href="https://azure.microsoft.com/en-us/documentation/articles/virtual-machines-size-specs/">size of the Virtual Machine</a>.</p>
</p></li>
<li><p><strong>zones</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A list of a single item of the Availability Zone which the Virtual Machine should be allocated in.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/virtual_machine.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/virtual_machine.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.compute.VirtualMachine.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.compute.VirtualMachine.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.compute.VirtualMachine.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.compute.VirtualMachine.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.compute.get_availability_set">
<code class="sig-prename descclassname">pulumi_azure.compute.</code><code class="sig-name descname">get_availability_set</code><span class="sig-paren">(</span><em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.compute.get_availability_set" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing Availability Set.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/availability_set.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/availability_set.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="function">
<dt id="pulumi_azure.compute.get_image">
<code class="sig-prename descclassname">pulumi_azure.compute.</code><code class="sig-name descname">get_image</code><span class="sig-paren">(</span><em class="sig-param">name=None</em>, <em class="sig-param">name_regex=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">sort_descending=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.compute.get_image" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing Image.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/image.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/image.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="function">
<dt id="pulumi_azure.compute.get_managed_disk">
<code class="sig-prename descclassname">pulumi_azure.compute.</code><code class="sig-name descname">get_managed_disk</code><span class="sig-paren">(</span><em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">zones=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.compute.get_managed_disk" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing Managed Disk.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/managed_disk.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/managed_disk.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="function">
<dt id="pulumi_azure.compute.get_platform_image">
<code class="sig-prename descclassname">pulumi_azure.compute.</code><code class="sig-name descname">get_platform_image</code><span class="sig-paren">(</span><em class="sig-param">location=None</em>, <em class="sig-param">offer=None</em>, <em class="sig-param">publisher=None</em>, <em class="sig-param">sku=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.compute.get_platform_image" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about a Platform Image.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/platform_image.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/platform_image.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="function">
<dt id="pulumi_azure.compute.get_shared_image">
<code class="sig-prename descclassname">pulumi_azure.compute.</code><code class="sig-name descname">get_shared_image</code><span class="sig-paren">(</span><em class="sig-param">gallery_name=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.compute.get_shared_image" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing Shared Image within a Shared Image Gallery.</p>
<blockquote>
<div><p><strong>NOTE</strong> Shared Image Galleries are currently in Public Preview. You can find more information, including <a class="reference external" href="https://azure.microsoft.com/en-gb/blog/announcing-the-public-preview-of-shared-image-gallery/">how to register for the Public Preview here</a>.</p>
<p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/shared_image.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/shared_image.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="function">
<dt id="pulumi_azure.compute.get_shared_image_gallery">
<code class="sig-prename descclassname">pulumi_azure.compute.</code><code class="sig-name descname">get_shared_image_gallery</code><span class="sig-paren">(</span><em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.compute.get_shared_image_gallery" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing Shared Image Gallery.</p>
<blockquote>
<div><p><strong>NOTE</strong> Shared Image Galleries are currently in Public Preview. You can find more information, including <a class="reference external" href="https://azure.microsoft.com/en-gb/blog/announcing-the-public-preview-of-shared-image-gallery/">how to register for the Public Preview here</a>.</p>
<p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/shared_image_gallery.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/shared_image_gallery.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="function">
<dt id="pulumi_azure.compute.get_shared_image_version">
<code class="sig-prename descclassname">pulumi_azure.compute.</code><code class="sig-name descname">get_shared_image_version</code><span class="sig-paren">(</span><em class="sig-param">gallery_name=None</em>, <em class="sig-param">image_name=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.compute.get_shared_image_version" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing Version of a Shared Image within a Shared Image Gallery.</p>
<blockquote>
<div><p><strong>NOTE</strong> Shared Image Galleries are currently in Public Preview. You can find more information, including <a class="reference external" href="https://azure.microsoft.com/en-gb/blog/announcing-the-public-preview-of-shared-image-gallery/">how to register for the Public Preview here</a>.</p>
<p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/shared_image_version.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/shared_image_version.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="function">
<dt id="pulumi_azure.compute.get_snapshot">
<code class="sig-prename descclassname">pulumi_azure.compute.</code><code class="sig-name descname">get_snapshot</code><span class="sig-paren">(</span><em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.compute.get_snapshot" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing Snapshot.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/snapshot.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/snapshot.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="function">
<dt id="pulumi_azure.compute.get_virtual_machine">
<code class="sig-prename descclassname">pulumi_azure.compute.</code><code class="sig-name descname">get_virtual_machine</code><span class="sig-paren">(</span><em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.compute.get_virtual_machine" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing Virtual Machine.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/virtual_machine.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/virtual_machine.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

</div>
