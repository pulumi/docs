---
title: Module compute
title_tag: Module compute | Package pulumi_azure | Python SDK
linktitle: compute
notitle: true
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
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.compute.</code><code class="sig-name descname">AvailabilitySet</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">managed=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">platform_fault_domain_count=None</em>, <em class="sig-param">platform_update_domain_count=None</em>, <em class="sig-param">proximity_placement_group_id=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.compute.AvailabilitySet" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an Availability Set for Virtual Machines.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>managed</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specifies whether the availability set is managed or not. Possible values are <code class="docutils literal notranslate"><span class="pre">true</span></code> (to specify aligned) or <code class="docutils literal notranslate"><span class="pre">false</span></code> (to specify classic). Default is <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the availability set. Changing this forces a new resource to be created.</p></li>
<li><p><strong>platform_fault_domain_count</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Specifies the number of fault domains that are used. Defaults to <code class="docutils literal notranslate"><span class="pre">3</span></code>.</p></li>
<li><p><strong>platform_update_domain_count</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Specifies the number of update domains that are used. Defaults to <code class="docutils literal notranslate"><span class="pre">5</span></code>.</p></li>
<li><p><strong>proximity_placement_group_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Proximity Placement Group to which this Virtual Machine should be assigned. Changing this forces a new resource to be created</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the availability set. Changing this forces a new resource to be created.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_azure.compute.AvailabilitySet.location">
<code class="sig-name descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.AvailabilitySet.location" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.AvailabilitySet.managed">
<code class="sig-name descname">managed</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.AvailabilitySet.managed" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies whether the availability set is managed or not. Possible values are <code class="docutils literal notranslate"><span class="pre">true</span></code> (to specify aligned) or <code class="docutils literal notranslate"><span class="pre">false</span></code> (to specify classic). Default is <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.AvailabilitySet.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.AvailabilitySet.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the availability set. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.AvailabilitySet.platform_fault_domain_count">
<code class="sig-name descname">platform_fault_domain_count</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.AvailabilitySet.platform_fault_domain_count" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the number of fault domains that are used. Defaults to <code class="docutils literal notranslate"><span class="pre">3</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.AvailabilitySet.platform_update_domain_count">
<code class="sig-name descname">platform_update_domain_count</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.AvailabilitySet.platform_update_domain_count" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the number of update domains that are used. Defaults to <code class="docutils literal notranslate"><span class="pre">5</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.AvailabilitySet.proximity_placement_group_id">
<code class="sig-name descname">proximity_placement_group_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.AvailabilitySet.proximity_placement_group_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Proximity Placement Group to which this Virtual Machine should be assigned. Changing this forces a new resource to be created</p>
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
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">managed=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">platform_fault_domain_count=None</em>, <em class="sig-param">platform_update_domain_count=None</em>, <em class="sig-param">proximity_placement_group_id=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.compute.AvailabilitySet.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing AvailabilitySet resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>managed</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specifies whether the availability set is managed or not. Possible values are <code class="docutils literal notranslate"><span class="pre">true</span></code> (to specify aligned) or <code class="docutils literal notranslate"><span class="pre">false</span></code> (to specify classic). Default is <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the availability set. Changing this forces a new resource to be created.</p></li>
<li><p><strong>platform_fault_domain_count</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Specifies the number of fault domains that are used. Defaults to <code class="docutils literal notranslate"><span class="pre">3</span></code>.</p></li>
<li><p><strong>platform_update_domain_count</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Specifies the number of update domains that are used. Defaults to <code class="docutils literal notranslate"><span class="pre">5</span></code>.</p></li>
<li><p><strong>proximity_placement_group_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Proximity Placement Group to which this Virtual Machine should be assigned. Changing this forces a new resource to be created</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the availability set. Changing this forces a new resource to be created.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
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
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.compute.</code><code class="sig-name descname">AwaitableGetAvailabilitySetResult</code><span class="sig-paren">(</span><em class="sig-param">id=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">managed=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">platform_fault_domain_count=None</em>, <em class="sig-param">platform_update_domain_count=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.compute.AwaitableGetAvailabilitySetResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_azure.compute.AwaitableGetDedicatedHostGroupResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.compute.</code><code class="sig-name descname">AwaitableGetDedicatedHostGroupResult</code><span class="sig-paren">(</span><em class="sig-param">id=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">platform_fault_domain_count=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">zones=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.compute.AwaitableGetDedicatedHostGroupResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_azure.compute.AwaitableGetDedicatedHostResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.compute.</code><code class="sig-name descname">AwaitableGetDedicatedHostResult</code><span class="sig-paren">(</span><em class="sig-param">dedicated_host_group_name=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.compute.AwaitableGetDedicatedHostResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_azure.compute.AwaitableGetDiskEncryptionSetResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.compute.</code><code class="sig-name descname">AwaitableGetDiskEncryptionSetResult</code><span class="sig-paren">(</span><em class="sig-param">id=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.compute.AwaitableGetDiskEncryptionSetResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_azure.compute.AwaitableGetImageResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.compute.</code><code class="sig-name descname">AwaitableGetImageResult</code><span class="sig-paren">(</span><em class="sig-param">data_disks=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">name_regex=None</em>, <em class="sig-param">os_disks=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">sort_descending=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">zone_resilient=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.compute.AwaitableGetImageResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_azure.compute.AwaitableGetManagedDiskResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.compute.</code><code class="sig-name descname">AwaitableGetManagedDiskResult</code><span class="sig-paren">(</span><em class="sig-param">create_option=None</em>, <em class="sig-param">disk_encryption_set_id=None</em>, <em class="sig-param">disk_iops_read_write=None</em>, <em class="sig-param">disk_mbps_read_write=None</em>, <em class="sig-param">disk_size_gb=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">os_type=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">source_resource_id=None</em>, <em class="sig-param">source_uri=None</em>, <em class="sig-param">storage_account_id=None</em>, <em class="sig-param">storage_account_type=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">zones=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.compute.AwaitableGetManagedDiskResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_azure.compute.AwaitableGetPlatformImageResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.compute.</code><code class="sig-name descname">AwaitableGetPlatformImageResult</code><span class="sig-paren">(</span><em class="sig-param">id=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">offer=None</em>, <em class="sig-param">publisher=None</em>, <em class="sig-param">sku=None</em>, <em class="sig-param">version=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.compute.AwaitableGetPlatformImageResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_azure.compute.AwaitableGetSharedImageGalleryResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.compute.</code><code class="sig-name descname">AwaitableGetSharedImageGalleryResult</code><span class="sig-paren">(</span><em class="sig-param">description=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">unique_name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.compute.AwaitableGetSharedImageGalleryResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_azure.compute.AwaitableGetSharedImageResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.compute.</code><code class="sig-name descname">AwaitableGetSharedImageResult</code><span class="sig-paren">(</span><em class="sig-param">description=None</em>, <em class="sig-param">eula=None</em>, <em class="sig-param">gallery_name=None</em>, <em class="sig-param">hyper_v_generation=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">identifiers=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">os_type=None</em>, <em class="sig-param">privacy_statement_uri=None</em>, <em class="sig-param">release_note_uri=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.compute.AwaitableGetSharedImageResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_azure.compute.AwaitableGetSharedImageVersionResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.compute.</code><code class="sig-name descname">AwaitableGetSharedImageVersionResult</code><span class="sig-paren">(</span><em class="sig-param">exclude_from_latest=None</em>, <em class="sig-param">gallery_name=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">image_name=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">managed_image_id=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">target_regions=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.compute.AwaitableGetSharedImageVersionResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_azure.compute.AwaitableGetSnapshotResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.compute.</code><code class="sig-name descname">AwaitableGetSnapshotResult</code><span class="sig-paren">(</span><em class="sig-param">creation_option=None</em>, <em class="sig-param">disk_size_gb=None</em>, <em class="sig-param">encryption_settings=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">os_type=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">source_resource_id=None</em>, <em class="sig-param">source_uri=None</em>, <em class="sig-param">storage_account_id=None</em>, <em class="sig-param">time_created=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.compute.AwaitableGetSnapshotResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_azure.compute.AwaitableGetVirtualMachineResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.compute.</code><code class="sig-name descname">AwaitableGetVirtualMachineResult</code><span class="sig-paren">(</span><em class="sig-param">id=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.compute.AwaitableGetVirtualMachineResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_azure.compute.BastionHost">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.compute.</code><code class="sig-name descname">BastionHost</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">ip_configuration=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.compute.BastionHost" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Bastion Host.</p>
<blockquote>
<div><p><strong>Note:</strong> Bastion Hosts are a preview feature in Azure, and therefore are only supported in a select number of regions. <a class="reference external" href="https://docs.microsoft.com/en-us/azure/bastion/bastion-faq">Read more</a>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>ip_configuration</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">ip_configuration</span></code> block as defined below.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Bastion Host. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the Bastion Host.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>ip_configuration</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the IP configuration.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">publicIpAddressId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Reference to a Public IP Address to associate with this Bastion Host.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnet_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Reference to a subnet in which this Bastion Host has been created.</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_azure.compute.BastionHost.dns_name">
<code class="sig-name descname">dns_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.BastionHost.dns_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The FQDN for the Bastion Host.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.BastionHost.ip_configuration">
<code class="sig-name descname">ip_configuration</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.BastionHost.ip_configuration" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">ip_configuration</span></code> block as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the IP configuration.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">publicIpAddressId</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Reference to a Public IP Address to associate with this Bastion Host.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnet_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Reference to a subnet in which this Bastion Host has been created.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.BastionHost.location">
<code class="sig-name descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.BastionHost.location" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.BastionHost.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.BastionHost.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Bastion Host. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.BastionHost.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.BastionHost.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to create the Bastion Host.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.BastionHost.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.BastionHost.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.compute.BastionHost.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">dns_name=None</em>, <em class="sig-param">ip_configuration=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.compute.BastionHost.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing BastionHost resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>dns_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The FQDN for the Bastion Host.</p></li>
<li><p><strong>ip_configuration</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">ip_configuration</span></code> block as defined below.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Bastion Host. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the Bastion Host.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>ip_configuration</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the IP configuration.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">publicIpAddressId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Reference to a Public IP Address to associate with this Bastion Host.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnet_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Reference to a subnet in which this Bastion Host has been created.</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.compute.BastionHost.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.compute.BastionHost.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.compute.BastionHost.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.compute.BastionHost.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.compute.DedicatedHost">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.compute.</code><code class="sig-name descname">DedicatedHost</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">auto_replace_on_failure=None</em>, <em class="sig-param">dedicated_host_group_id=None</em>, <em class="sig-param">license_type=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">platform_fault_domain=None</em>, <em class="sig-param">sku_name=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.compute.DedicatedHost" title="Permalink to this definition">¶</a></dt>
<dd><p>Manage a Dedicated Host within a Dedicated Host Group.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>auto_replace_on_failure</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Should the Dedicated Host automatically be replaced in case of a Hardware Failure? Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>dedicated_host_group_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the ID of the Dedicated Host Group where the Dedicated Host should exist. Changing this forces a new resource to be created.</p></li>
<li><p><strong>license_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the software license type that will be applied to the VMs deployed on the Dedicated Host. Possible values are <code class="docutils literal notranslate"><span class="pre">None</span></code>, <code class="docutils literal notranslate"><span class="pre">Windows_Server_Hybrid</span></code> and <code class="docutils literal notranslate"><span class="pre">Windows_Server_Perpetual</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">None</span></code>.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specify the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of this Dedicated Host. Changing this forces a new resource to be created.</p></li>
<li><p><strong>platform_fault_domain</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Specify the fault domain of the Dedicated Host Group in which to create the Dedicated Host. Changing this forces a new resource to be created.</p></li>
<li><p><strong>sku_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specify the sku name of the Dedicated Host. Possible values are <code class="docutils literal notranslate"><span class="pre">DSv3-Type1</span></code>, <code class="docutils literal notranslate"><span class="pre">DSv3-Type2</span></code>, <code class="docutils literal notranslate"><span class="pre">ESv3-Type1</span></code>, <code class="docutils literal notranslate"><span class="pre">ESv3-Type2</span></code>,<code class="docutils literal notranslate"><span class="pre">FSv2-Type2</span></code>. Changing this forces a new resource to be created.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_azure.compute.DedicatedHost.auto_replace_on_failure">
<code class="sig-name descname">auto_replace_on_failure</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.DedicatedHost.auto_replace_on_failure" title="Permalink to this definition">¶</a></dt>
<dd><p>Should the Dedicated Host automatically be replaced in case of a Hardware Failure? Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.DedicatedHost.dedicated_host_group_id">
<code class="sig-name descname">dedicated_host_group_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.DedicatedHost.dedicated_host_group_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the ID of the Dedicated Host Group where the Dedicated Host should exist. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.DedicatedHost.license_type">
<code class="sig-name descname">license_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.DedicatedHost.license_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the software license type that will be applied to the VMs deployed on the Dedicated Host. Possible values are <code class="docutils literal notranslate"><span class="pre">None</span></code>, <code class="docutils literal notranslate"><span class="pre">Windows_Server_Hybrid</span></code> and <code class="docutils literal notranslate"><span class="pre">Windows_Server_Perpetual</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">None</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.DedicatedHost.location">
<code class="sig-name descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.DedicatedHost.location" title="Permalink to this definition">¶</a></dt>
<dd><p>Specify the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.DedicatedHost.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.DedicatedHost.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of this Dedicated Host. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.DedicatedHost.platform_fault_domain">
<code class="sig-name descname">platform_fault_domain</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.DedicatedHost.platform_fault_domain" title="Permalink to this definition">¶</a></dt>
<dd><p>Specify the fault domain of the Dedicated Host Group in which to create the Dedicated Host. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.DedicatedHost.sku_name">
<code class="sig-name descname">sku_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.DedicatedHost.sku_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specify the sku name of the Dedicated Host. Possible values are <code class="docutils literal notranslate"><span class="pre">DSv3-Type1</span></code>, <code class="docutils literal notranslate"><span class="pre">DSv3-Type2</span></code>, <code class="docutils literal notranslate"><span class="pre">ESv3-Type1</span></code>, <code class="docutils literal notranslate"><span class="pre">ESv3-Type2</span></code>,<code class="docutils literal notranslate"><span class="pre">FSv2-Type2</span></code>. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.DedicatedHost.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.DedicatedHost.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.compute.DedicatedHost.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">auto_replace_on_failure=None</em>, <em class="sig-param">dedicated_host_group_id=None</em>, <em class="sig-param">license_type=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">platform_fault_domain=None</em>, <em class="sig-param">sku_name=None</em>, <em class="sig-param">tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.compute.DedicatedHost.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing DedicatedHost resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>auto_replace_on_failure</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Should the Dedicated Host automatically be replaced in case of a Hardware Failure? Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>dedicated_host_group_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the ID of the Dedicated Host Group where the Dedicated Host should exist. Changing this forces a new resource to be created.</p></li>
<li><p><strong>license_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the software license type that will be applied to the VMs deployed on the Dedicated Host. Possible values are <code class="docutils literal notranslate"><span class="pre">None</span></code>, <code class="docutils literal notranslate"><span class="pre">Windows_Server_Hybrid</span></code> and <code class="docutils literal notranslate"><span class="pre">Windows_Server_Perpetual</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">None</span></code>.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specify the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of this Dedicated Host. Changing this forces a new resource to be created.</p></li>
<li><p><strong>platform_fault_domain</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Specify the fault domain of the Dedicated Host Group in which to create the Dedicated Host. Changing this forces a new resource to be created.</p></li>
<li><p><strong>sku_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specify the sku name of the Dedicated Host. Possible values are <code class="docutils literal notranslate"><span class="pre">DSv3-Type1</span></code>, <code class="docutils literal notranslate"><span class="pre">DSv3-Type2</span></code>, <code class="docutils literal notranslate"><span class="pre">ESv3-Type1</span></code>, <code class="docutils literal notranslate"><span class="pre">ESv3-Type2</span></code>,<code class="docutils literal notranslate"><span class="pre">FSv2-Type2</span></code>. Changing this forces a new resource to be created.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.compute.DedicatedHost.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.compute.DedicatedHost.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.compute.DedicatedHost.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.compute.DedicatedHost.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.compute.DedicatedHostGroup">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.compute.</code><code class="sig-name descname">DedicatedHostGroup</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">platform_fault_domain_count=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">zones=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.compute.DedicatedHostGroup" title="Permalink to this definition">¶</a></dt>
<dd><p>Manage a Dedicated Host Group.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Azure location where the Dedicated Host Group exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Dedicated Host Group. Changing this forces a new resource to be created.</p></li>
<li><p><strong>platform_fault_domain_count</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The number of fault domains that the Dedicated Host Group spans. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the resource group the Dedicated Host Group is located in. Changing this forces a new resource to be created.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
<li><p><strong>zones</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A list of Availability Zones in which the Dedicated Host Group should be located. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_azure.compute.DedicatedHostGroup.location">
<code class="sig-name descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.DedicatedHostGroup.location" title="Permalink to this definition">¶</a></dt>
<dd><p>The Azure location where the Dedicated Host Group exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.DedicatedHostGroup.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.DedicatedHostGroup.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Dedicated Host Group. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.DedicatedHostGroup.platform_fault_domain_count">
<code class="sig-name descname">platform_fault_domain_count</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.DedicatedHostGroup.platform_fault_domain_count" title="Permalink to this definition">¶</a></dt>
<dd><p>The number of fault domains that the Dedicated Host Group spans. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.DedicatedHostGroup.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.DedicatedHostGroup.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the resource group the Dedicated Host Group is located in. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.DedicatedHostGroup.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.DedicatedHostGroup.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.DedicatedHostGroup.zones">
<code class="sig-name descname">zones</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.DedicatedHostGroup.zones" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of Availability Zones in which the Dedicated Host Group should be located. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.compute.DedicatedHostGroup.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">platform_fault_domain_count=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">zones=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.compute.DedicatedHostGroup.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing DedicatedHostGroup resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Azure location where the Dedicated Host Group exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Dedicated Host Group. Changing this forces a new resource to be created.</p></li>
<li><p><strong>platform_fault_domain_count</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The number of fault domains that the Dedicated Host Group spans. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the resource group the Dedicated Host Group is located in. Changing this forces a new resource to be created.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
<li><p><strong>zones</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A list of Availability Zones in which the Dedicated Host Group should be located. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.compute.DedicatedHostGroup.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.compute.DedicatedHostGroup.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.compute.DedicatedHostGroup.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.compute.DedicatedHostGroup.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.compute.DiskEncryptionSet">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.compute.</code><code class="sig-name descname">DiskEncryptionSet</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">identity=None</em>, <em class="sig-param">key_vault_key_id=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.compute.DiskEncryptionSet" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Disk Encryption Set.</p>
<blockquote>
<div><p><strong>NOTE</strong>: Disk Encryption Sets are in Public Preview and at this time is only available in <code class="docutils literal notranslate"><span class="pre">Canada</span> <span class="pre">Central</span></code>, <code class="docutils literal notranslate"><span class="pre">North</span> <span class="pre">Europe</span></code> and <code class="docutils literal notranslate"><span class="pre">West</span> <span class="pre">Central</span> <span class="pre">US</span></code> regions - <a class="reference external" href="https://docs.microsoft.com/en-us/azure/virtual-machines/linux/disk-encryption">more information can be found in the preview documentation</a>.</p>
<p><strong>NOTE:</strong> At this time the Key Vault used to store the Active Key for this Disk Encryption Set must have both Soft Delete &amp; Purge Protection enabled - which are not yet supported by this provider.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>identity</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">identity</span></code> block defined below.</p></li>
<li><p><strong>key_vault_key_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the URL to a Key Vault Key (either from a Key Vault Key, or the Key URL for the Key Vault Secret).</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the Azure Region where the Disk Encryption Set exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Disk Encryption Set. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Resource Group where the Disk Encryption Set should exist. Changing this forces a new resource to be created.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the Disk Encryption Set.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>identity</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">principal_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The (Client) ID of the Service Principal.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tenant_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Tenant the Service Principal is assigned in.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Type of Identity which should be used for this Disk Encryption Set. At this time the only possible value is <code class="docutils literal notranslate"><span class="pre">SystemAssigned</span></code>.</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_azure.compute.DiskEncryptionSet.identity">
<code class="sig-name descname">identity</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.DiskEncryptionSet.identity" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">identity</span></code> block defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">principal_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The (Client) ID of the Service Principal.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tenant_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the Tenant the Service Principal is assigned in.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Type of Identity which should be used for this Disk Encryption Set. At this time the only possible value is <code class="docutils literal notranslate"><span class="pre">SystemAssigned</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.DiskEncryptionSet.key_vault_key_id">
<code class="sig-name descname">key_vault_key_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.DiskEncryptionSet.key_vault_key_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the URL to a Key Vault Key (either from a Key Vault Key, or the Key URL for the Key Vault Secret).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.DiskEncryptionSet.location">
<code class="sig-name descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.DiskEncryptionSet.location" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the Azure Region where the Disk Encryption Set exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.DiskEncryptionSet.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.DiskEncryptionSet.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Disk Encryption Set. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.DiskEncryptionSet.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.DiskEncryptionSet.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Resource Group where the Disk Encryption Set should exist. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.DiskEncryptionSet.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.DiskEncryptionSet.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the Disk Encryption Set.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.compute.DiskEncryptionSet.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">identity=None</em>, <em class="sig-param">key_vault_key_id=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.compute.DiskEncryptionSet.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing DiskEncryptionSet resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>identity</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">identity</span></code> block defined below.</p></li>
<li><p><strong>key_vault_key_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the URL to a Key Vault Key (either from a Key Vault Key, or the Key URL for the Key Vault Secret).</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the Azure Region where the Disk Encryption Set exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Disk Encryption Set. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Resource Group where the Disk Encryption Set should exist. Changing this forces a new resource to be created.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the Disk Encryption Set.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>identity</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">principal_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The (Client) ID of the Service Principal.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tenant_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Tenant the Service Principal is assigned in.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Type of Identity which should be used for this Disk Encryption Set. At this time the only possible value is <code class="docutils literal notranslate"><span class="pre">SystemAssigned</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.compute.DiskEncryptionSet.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.compute.DiskEncryptionSet.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.compute.DiskEncryptionSet.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.compute.DiskEncryptionSet.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.compute.</code><code class="sig-name descname">Extension</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">auto_upgrade_minor_version=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">protected_settings=None</em>, <em class="sig-param">publisher=None</em>, <em class="sig-param">settings=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">type=None</em>, <em class="sig-param">type_handler_version=None</em>, <em class="sig-param">virtual_machine_id=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.compute.Extension" title="Permalink to this definition">¶</a></dt>
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
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the virtual machine extension peering. Changing
this forces a new resource to be created.</p></li>
<li><p><strong>protected_settings</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The protected_settings passed to the
extension, like settings, these are specified as a JSON object in a string.</p></li>
<li><p><strong>publisher</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The publisher of the extension, available publishers
can be found by using the Azure CLI.</p></li>
<li><p><strong>settings</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The settings passed to the extension, these are
specified as a JSON object in a string.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of extension, available types for a publisher can
be found using the Azure CLI.</p></li>
<li><p><strong>type_handler_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the version of the extension to
use, available versions can be found using the Azure CLI.</p></li>
<li><p><strong>virtual_machine_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Virtual Machine. Changing this forces a new resource to be created</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_azure.compute.Extension.auto_upgrade_minor_version">
<code class="sig-name descname">auto_upgrade_minor_version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.Extension.auto_upgrade_minor_version" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies if the platform deploys
the latest minor version update to the <code class="docutils literal notranslate"><span class="pre">type_handler_version</span></code> specified.</p>
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
<dt id="pulumi_azure.compute.Extension.virtual_machine_id">
<code class="sig-name descname">virtual_machine_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.Extension.virtual_machine_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Virtual Machine. Changing this forces a new resource to be created</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.compute.Extension.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">auto_upgrade_minor_version=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">protected_settings=None</em>, <em class="sig-param">publisher=None</em>, <em class="sig-param">settings=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">type=None</em>, <em class="sig-param">type_handler_version=None</em>, <em class="sig-param">virtual_machine_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.compute.Extension.get" title="Permalink to this definition">¶</a></dt>
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
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the virtual machine extension peering. Changing
this forces a new resource to be created.</p></li>
<li><p><strong>protected_settings</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The protected_settings passed to the
extension, like settings, these are specified as a JSON object in a string.</p></li>
<li><p><strong>publisher</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The publisher of the extension, available publishers
can be found by using the Azure CLI.</p></li>
<li><p><strong>settings</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The settings passed to the extension, these are
specified as a JSON object in a string.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of extension, available types for a publisher can
be found using the Azure CLI.</p></li>
<li><p><strong>type_handler_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the version of the extension to
use, available versions can be found using the Azure CLI.</p></li>
<li><p><strong>virtual_machine_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Virtual Machine. Changing this forces a new resource to be created</p></li>
</ul>
</dd>
</dl>
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
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.compute.</code><code class="sig-name descname">GetAvailabilitySetResult</code><span class="sig-paren">(</span><em class="sig-param">id=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">managed=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">platform_fault_domain_count=None</em>, <em class="sig-param">platform_update_domain_count=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.compute.GetAvailabilitySetResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getAvailabilitySet.</p>
<dl class="attribute">
<dt id="pulumi_azure.compute.GetAvailabilitySetResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.GetAvailabilitySetResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

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

</dd></dl>

<dl class="class">
<dt id="pulumi_azure.compute.GetDedicatedHostGroupResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.compute.</code><code class="sig-name descname">GetDedicatedHostGroupResult</code><span class="sig-paren">(</span><em class="sig-param">id=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">platform_fault_domain_count=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">zones=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.compute.GetDedicatedHostGroupResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getDedicatedHostGroup.</p>
<dl class="attribute">
<dt id="pulumi_azure.compute.GetDedicatedHostGroupResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.GetDedicatedHostGroupResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.GetDedicatedHostGroupResult.location">
<code class="sig-name descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.GetDedicatedHostGroupResult.location" title="Permalink to this definition">¶</a></dt>
<dd><p>The Azure location where the Dedicated Host Group exists.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.GetDedicatedHostGroupResult.platform_fault_domain_count">
<code class="sig-name descname">platform_fault_domain_count</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.GetDedicatedHostGroupResult.platform_fault_domain_count" title="Permalink to this definition">¶</a></dt>
<dd><p>The number of fault domains that the Dedicated Host Group spans.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.GetDedicatedHostGroupResult.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.GetDedicatedHostGroupResult.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags assigned to the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.GetDedicatedHostGroupResult.zones">
<code class="sig-name descname">zones</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.GetDedicatedHostGroupResult.zones" title="Permalink to this definition">¶</a></dt>
<dd><p>The Availability Zones in which this Dedicated Host Group is located.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azure.compute.GetDedicatedHostResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.compute.</code><code class="sig-name descname">GetDedicatedHostResult</code><span class="sig-paren">(</span><em class="sig-param">dedicated_host_group_name=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.compute.GetDedicatedHostResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getDedicatedHost.</p>
<dl class="attribute">
<dt id="pulumi_azure.compute.GetDedicatedHostResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.GetDedicatedHostResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.GetDedicatedHostResult.location">
<code class="sig-name descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.GetDedicatedHostResult.location" title="Permalink to this definition">¶</a></dt>
<dd><p>The location where the Dedicated Host exists.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.GetDedicatedHostResult.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.GetDedicatedHostResult.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags assigned to the Dedicated Host.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azure.compute.GetDiskEncryptionSetResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.compute.</code><code class="sig-name descname">GetDiskEncryptionSetResult</code><span class="sig-paren">(</span><em class="sig-param">id=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.compute.GetDiskEncryptionSetResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getDiskEncryptionSet.</p>
<dl class="attribute">
<dt id="pulumi_azure.compute.GetDiskEncryptionSetResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.GetDiskEncryptionSetResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.GetDiskEncryptionSetResult.location">
<code class="sig-name descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.GetDiskEncryptionSetResult.location" title="Permalink to this definition">¶</a></dt>
<dd><p>The location where the Disk Encryption Set exists.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.GetDiskEncryptionSetResult.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.GetDiskEncryptionSetResult.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags assigned to the Disk Encryption Set.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azure.compute.GetImageResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.compute.</code><code class="sig-name descname">GetImageResult</code><span class="sig-paren">(</span><em class="sig-param">data_disks=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">name_regex=None</em>, <em class="sig-param">os_disks=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">sort_descending=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">zone_resilient=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.compute.GetImageResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getImage.</p>
<dl class="attribute">
<dt id="pulumi_azure.compute.GetImageResult.data_disks">
<code class="sig-name descname">data_disks</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.GetImageResult.data_disks" title="Permalink to this definition">¶</a></dt>
<dd><p>a collection of <code class="docutils literal notranslate"><span class="pre">data_disk</span></code> blocks as defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.GetImageResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.GetImageResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
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

</dd></dl>

<dl class="class">
<dt id="pulumi_azure.compute.GetManagedDiskResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.compute.</code><code class="sig-name descname">GetManagedDiskResult</code><span class="sig-paren">(</span><em class="sig-param">create_option=None</em>, <em class="sig-param">disk_encryption_set_id=None</em>, <em class="sig-param">disk_iops_read_write=None</em>, <em class="sig-param">disk_mbps_read_write=None</em>, <em class="sig-param">disk_size_gb=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">os_type=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">source_resource_id=None</em>, <em class="sig-param">source_uri=None</em>, <em class="sig-param">storage_account_id=None</em>, <em class="sig-param">storage_account_type=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">zones=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.compute.GetManagedDiskResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getManagedDisk.</p>
<dl class="attribute">
<dt id="pulumi_azure.compute.GetManagedDiskResult.disk_encryption_set_id">
<code class="sig-name descname">disk_encryption_set_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.GetManagedDiskResult.disk_encryption_set_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Disk Encryption Set used to encrypt this Managed Disk.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.GetManagedDiskResult.disk_iops_read_write">
<code class="sig-name descname">disk_iops_read_write</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.GetManagedDiskResult.disk_iops_read_write" title="Permalink to this definition">¶</a></dt>
<dd><p>The number of IOPS allowed for this disk, where one operation can transfer between 4k and 256k bytes.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.GetManagedDiskResult.disk_mbps_read_write">
<code class="sig-name descname">disk_mbps_read_write</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.GetManagedDiskResult.disk_mbps_read_write" title="Permalink to this definition">¶</a></dt>
<dd><p>The bandwidth allowed for this disk.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.GetManagedDiskResult.disk_size_gb">
<code class="sig-name descname">disk_size_gb</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.GetManagedDiskResult.disk_size_gb" title="Permalink to this definition">¶</a></dt>
<dd><p>The size of the Managed Disk in gigabytes.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.GetManagedDiskResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.GetManagedDiskResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.GetManagedDiskResult.os_type">
<code class="sig-name descname">os_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.GetManagedDiskResult.os_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The operating system used for this Managed Disk.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.GetManagedDiskResult.source_resource_id">
<code class="sig-name descname">source_resource_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.GetManagedDiskResult.source_resource_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of an existing Managed Disk which this Disk was created from.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.GetManagedDiskResult.source_uri">
<code class="sig-name descname">source_uri</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.GetManagedDiskResult.source_uri" title="Permalink to this definition">¶</a></dt>
<dd><p>The Source URI for this Managed Disk.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.GetManagedDiskResult.storage_account_id">
<code class="sig-name descname">storage_account_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.GetManagedDiskResult.storage_account_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Storage Account where the <code class="docutils literal notranslate"><span class="pre">source_uri</span></code> is located.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.GetManagedDiskResult.storage_account_type">
<code class="sig-name descname">storage_account_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.GetManagedDiskResult.storage_account_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The storage account type for the Managed Disk.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.GetManagedDiskResult.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.GetManagedDiskResult.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags assigned to the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.GetManagedDiskResult.zones">
<code class="sig-name descname">zones</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.GetManagedDiskResult.zones" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of Availability Zones where the Managed Disk exists.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azure.compute.GetPlatformImageResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.compute.</code><code class="sig-name descname">GetPlatformImageResult</code><span class="sig-paren">(</span><em class="sig-param">id=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">offer=None</em>, <em class="sig-param">publisher=None</em>, <em class="sig-param">sku=None</em>, <em class="sig-param">version=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.compute.GetPlatformImageResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getPlatformImage.</p>
<dl class="attribute">
<dt id="pulumi_azure.compute.GetPlatformImageResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.GetPlatformImageResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.GetPlatformImageResult.version">
<code class="sig-name descname">version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.GetPlatformImageResult.version" title="Permalink to this definition">¶</a></dt>
<dd><p>The latest version of the Platform Image.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azure.compute.GetSharedImageGalleryResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.compute.</code><code class="sig-name descname">GetSharedImageGalleryResult</code><span class="sig-paren">(</span><em class="sig-param">description=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">unique_name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.compute.GetSharedImageGalleryResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getSharedImageGallery.</p>
<dl class="attribute">
<dt id="pulumi_azure.compute.GetSharedImageGalleryResult.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.GetSharedImageGalleryResult.description" title="Permalink to this definition">¶</a></dt>
<dd><p>A description for the Shared Image Gallery.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.GetSharedImageGalleryResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.GetSharedImageGalleryResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
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

</dd></dl>

<dl class="class">
<dt id="pulumi_azure.compute.GetSharedImageResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.compute.</code><code class="sig-name descname">GetSharedImageResult</code><span class="sig-paren">(</span><em class="sig-param">description=None</em>, <em class="sig-param">eula=None</em>, <em class="sig-param">gallery_name=None</em>, <em class="sig-param">hyper_v_generation=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">identifiers=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">os_type=None</em>, <em class="sig-param">privacy_statement_uri=None</em>, <em class="sig-param">release_note_uri=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.compute.GetSharedImageResult" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.compute.GetSharedImageResult.hyper_v_generation">
<code class="sig-name descname">hyper_v_generation</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.GetSharedImageResult.hyper_v_generation" title="Permalink to this definition">¶</a></dt>
<dd><p>The generation of HyperV that the Virtual Machine used to create the Shared Image is based on.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.GetSharedImageResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.GetSharedImageResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
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

</dd></dl>

<dl class="class">
<dt id="pulumi_azure.compute.GetSharedImageVersionResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.compute.</code><code class="sig-name descname">GetSharedImageVersionResult</code><span class="sig-paren">(</span><em class="sig-param">exclude_from_latest=None</em>, <em class="sig-param">gallery_name=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">image_name=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">managed_image_id=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">target_regions=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.compute.GetSharedImageVersionResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getSharedImageVersion.</p>
<dl class="attribute">
<dt id="pulumi_azure.compute.GetSharedImageVersionResult.exclude_from_latest">
<code class="sig-name descname">exclude_from_latest</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.GetSharedImageVersionResult.exclude_from_latest" title="Permalink to this definition">¶</a></dt>
<dd><p>Is this Image Version excluded from the <code class="docutils literal notranslate"><span class="pre">latest</span></code> filter?</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.GetSharedImageVersionResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.GetSharedImageVersionResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
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

</dd></dl>

<dl class="class">
<dt id="pulumi_azure.compute.GetSnapshotResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.compute.</code><code class="sig-name descname">GetSnapshotResult</code><span class="sig-paren">(</span><em class="sig-param">creation_option=None</em>, <em class="sig-param">disk_size_gb=None</em>, <em class="sig-param">encryption_settings=None</em>, <em class="sig-param">id=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">os_type=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">source_resource_id=None</em>, <em class="sig-param">source_uri=None</em>, <em class="sig-param">storage_account_id=None</em>, <em class="sig-param">time_created=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.compute.GetSnapshotResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getSnapshot.</p>
<dl class="attribute">
<dt id="pulumi_azure.compute.GetSnapshotResult.disk_size_gb">
<code class="sig-name descname">disk_size_gb</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.GetSnapshotResult.disk_size_gb" title="Permalink to this definition">¶</a></dt>
<dd><p>The size of the Snapshotted Disk in GB.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.GetSnapshotResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.GetSnapshotResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
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

</dd></dl>

<dl class="class">
<dt id="pulumi_azure.compute.GetVirtualMachineResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.compute.</code><code class="sig-name descname">GetVirtualMachineResult</code><span class="sig-paren">(</span><em class="sig-param">id=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.compute.GetVirtualMachineResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getVirtualMachine.</p>
<dl class="attribute">
<dt id="pulumi_azure.compute.GetVirtualMachineResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.GetVirtualMachineResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azure.compute.Image">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.compute.</code><code class="sig-name descname">Image</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">data_disks=None</em>, <em class="sig-param">hyper_v_generation=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">os_disk=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">source_virtual_machine_id=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">zone_resilient=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.compute.Image" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a custom virtual machine image that can be used to create virtual machines.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>data_disks</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">data_disk</span></code> elements as defined below.</p></li>
<li><p><strong>hyper_v_generation</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The HyperVGenerationType of the VirtualMachine created from the image as <code class="docutils literal notranslate"><span class="pre">V1</span></code>, <code class="docutils literal notranslate"><span class="pre">V2</span></code>. The default is <code class="docutils literal notranslate"><span class="pre">V1</span></code>.</p></li>
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
<p>The <strong>data_disks</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">blobUri</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the URI in Azure storage of the blob that you want to use to create the image.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">caching</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the caching mode as <code class="docutils literal notranslate"><span class="pre">ReadWrite</span></code>, <code class="docutils literal notranslate"><span class="pre">ReadOnly</span></code>, or <code class="docutils literal notranslate"><span class="pre">None</span></code>. The default is <code class="docutils literal notranslate"><span class="pre">None</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">lun</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Specifies the logical unit number of the data disk.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">managed_disk_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the ID of the managed disk resource that you want to use to create the image.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sizeGb</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Specifies the size of the image to be created. The target size can’t be smaller than the source size.</p></li>
</ul>
<p>The <strong>os_disk</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">blobUri</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the URI in Azure storage of the blob that you want to use to create the image.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">caching</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the caching mode as <code class="docutils literal notranslate"><span class="pre">ReadWrite</span></code>, <code class="docutils literal notranslate"><span class="pre">ReadOnly</span></code>, or <code class="docutils literal notranslate"><span class="pre">None</span></code>. The default is <code class="docutils literal notranslate"><span class="pre">None</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">managed_disk_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the ID of the managed disk resource that you want to use to create the image.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">osState</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the state of the operating system contained in the blob. Currently, the only value is Generalized.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">os_type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the type of operating system contained in the virtual machine image. Possible values are: Windows or Linux.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sizeGb</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Specifies the size of the image to be created. The target size can’t be smaller than the source size.</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_azure.compute.Image.data_disks">
<code class="sig-name descname">data_disks</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.Image.data_disks" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more <code class="docutils literal notranslate"><span class="pre">data_disk</span></code> elements as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">blobUri</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the URI in Azure storage of the blob that you want to use to create the image.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">caching</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the caching mode as <code class="docutils literal notranslate"><span class="pre">ReadWrite</span></code>, <code class="docutils literal notranslate"><span class="pre">ReadOnly</span></code>, or <code class="docutils literal notranslate"><span class="pre">None</span></code>. The default is <code class="docutils literal notranslate"><span class="pre">None</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">lun</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Specifies the logical unit number of the data disk.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">managed_disk_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the ID of the managed disk resource that you want to use to create the image.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sizeGb</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Specifies the size of the image to be created. The target size can’t be smaller than the source size.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.Image.hyper_v_generation">
<code class="sig-name descname">hyper_v_generation</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.Image.hyper_v_generation" title="Permalink to this definition">¶</a></dt>
<dd><p>The HyperVGenerationType of the VirtualMachine created from the image as <code class="docutils literal notranslate"><span class="pre">V1</span></code>, <code class="docutils literal notranslate"><span class="pre">V2</span></code>. The default is <code class="docutils literal notranslate"><span class="pre">V1</span></code>.</p>
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
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">blobUri</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the URI in Azure storage of the blob that you want to use to create the image.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">caching</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the caching mode as <code class="docutils literal notranslate"><span class="pre">ReadWrite</span></code>, <code class="docutils literal notranslate"><span class="pre">ReadOnly</span></code>, or <code class="docutils literal notranslate"><span class="pre">None</span></code>. The default is <code class="docutils literal notranslate"><span class="pre">None</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">managed_disk_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the ID of the managed disk resource that you want to use to create the image.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">osState</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the state of the operating system contained in the blob. Currently, the only value is Generalized.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">os_type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the type of operating system contained in the virtual machine image. Possible values are: Windows or Linux.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sizeGb</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Specifies the size of the image to be created. The target size can’t be smaller than the source size.</p></li>
</ul>
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
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">data_disks=None</em>, <em class="sig-param">hyper_v_generation=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">os_disk=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">source_virtual_machine_id=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">zone_resilient=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.compute.Image.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Image resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>data_disks</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">data_disk</span></code> elements as defined below.</p></li>
<li><p><strong>hyper_v_generation</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The HyperVGenerationType of the VirtualMachine created from the image as <code class="docutils literal notranslate"><span class="pre">V1</span></code>, <code class="docutils literal notranslate"><span class="pre">V2</span></code>. The default is <code class="docutils literal notranslate"><span class="pre">V1</span></code>.</p></li>
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
<p>The <strong>data_disks</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">blobUri</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the URI in Azure storage of the blob that you want to use to create the image.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">caching</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the caching mode as <code class="docutils literal notranslate"><span class="pre">ReadWrite</span></code>, <code class="docutils literal notranslate"><span class="pre">ReadOnly</span></code>, or <code class="docutils literal notranslate"><span class="pre">None</span></code>. The default is <code class="docutils literal notranslate"><span class="pre">None</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">lun</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Specifies the logical unit number of the data disk.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">managed_disk_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the ID of the managed disk resource that you want to use to create the image.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sizeGb</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Specifies the size of the image to be created. The target size can’t be smaller than the source size.</p></li>
</ul>
<p>The <strong>os_disk</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">blobUri</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the URI in Azure storage of the blob that you want to use to create the image.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">caching</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the caching mode as <code class="docutils literal notranslate"><span class="pre">ReadWrite</span></code>, <code class="docutils literal notranslate"><span class="pre">ReadOnly</span></code>, or <code class="docutils literal notranslate"><span class="pre">None</span></code>. The default is <code class="docutils literal notranslate"><span class="pre">None</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">managed_disk_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the ID of the managed disk resource that you want to use to create the image.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">osState</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the state of the operating system contained in the blob. Currently, the only value is Generalized.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">os_type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the type of operating system contained in the virtual machine image. Possible values are: Windows or Linux.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sizeGb</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Specifies the size of the image to be created. The target size can’t be smaller than the source size.</p></li>
</ul>
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
<dt id="pulumi_azure.compute.LinuxVirtualMachine">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.compute.</code><code class="sig-name descname">LinuxVirtualMachine</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">additional_capabilities=None</em>, <em class="sig-param">admin_password=None</em>, <em class="sig-param">admin_ssh_keys=None</em>, <em class="sig-param">admin_username=None</em>, <em class="sig-param">allow_extension_operations=None</em>, <em class="sig-param">availability_set_id=None</em>, <em class="sig-param">boot_diagnostics=None</em>, <em class="sig-param">computer_name=None</em>, <em class="sig-param">custom_data=None</em>, <em class="sig-param">dedicated_host_id=None</em>, <em class="sig-param">disable_password_authentication=None</em>, <em class="sig-param">eviction_policy=None</em>, <em class="sig-param">identity=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">max_bid_price=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">network_interface_ids=None</em>, <em class="sig-param">os_disk=None</em>, <em class="sig-param">plan=None</em>, <em class="sig-param">priority=None</em>, <em class="sig-param">provision_vm_agent=None</em>, <em class="sig-param">proximity_placement_group_id=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">secrets=None</em>, <em class="sig-param">size=None</em>, <em class="sig-param">source_image_id=None</em>, <em class="sig-param">source_image_reference=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">zone=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.compute.LinuxVirtualMachine" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Linux Virtual Machine.</p>
<blockquote>
<div><p><strong>Note</strong> This provider will automatically remove the OS Disk by default - this behaviour can be configured using the <code class="docutils literal notranslate"><span class="pre">features</span></code> configuration within the Provider configuration block.</p>
<p><strong>Note</strong> This resource does not support Unmanaged Disks. If you need to use Unmanaged Disks you can continue to use the <code class="docutils literal notranslate"><span class="pre">compute.VirtualMachine</span></code> resource instead.</p>
<p><strong>Note</strong> This resource does not support attaching existing OS Disks. You can instead capture an image of the OS Disk or continue to use the <code class="docutils literal notranslate"><span class="pre">compute.VirtualMachine</span></code> resource instead.</p>
<p>In this release there’s a known issue where the <code class="docutils literal notranslate"><span class="pre">public_ip_address</span></code> and <code class="docutils literal notranslate"><span class="pre">public_ip_addresses</span></code> fields may not be fully populated for Dynamic Public IP’s.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>additional_capabilities</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">additional_capabilities</span></code> block as defined below.</p></li>
<li><p><strong>admin_password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Password which should be used for the local-administrator on this Virtual Machine. Changing this forces a new resource to be created.</p></li>
<li><p><strong>admin_ssh_keys</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">admin_ssh_key</span></code> blocks as defined below.</p></li>
<li><p><strong>admin_username</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The username of the local administrator used for the Virtual Machine. Changing this forces a new resource to be created.</p></li>
<li><p><strong>allow_extension_operations</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Should Extension Operations be allowed on this Virtual Machine? Changing this forces a new resource to be created.</p></li>
<li><p><strong>availability_set_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the ID of the Availability Set in which the Virtual Machine should exist. Changing this forces a new resource to be created.</p></li>
<li><p><strong>boot_diagnostics</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">boot_diagnostics</span></code> block as defined below.</p></li>
<li><p><strong>computer_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the Hostname which should be used for this Virtual Machine. If unspecified this defaults to the value for the <code class="docutils literal notranslate"><span class="pre">name</span></code> field. Changing this forces a new resource to be created.</p></li>
<li><p><strong>custom_data</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Base64-Encoded Custom Data which should be used for this Virtual Machine. Changing this forces a new resource to be created.</p></li>
<li><p><strong>dedicated_host_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of a Dedicated Host where this machine should be run on. Changing this forces a new resource to be created.</p></li>
<li><p><strong>disable_password_authentication</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Should Password Authentication be disabled on this Virtual Machine? Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>. Changing this forces a new resource to be created.</p></li>
<li><p><strong>eviction_policy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies what should happen when the Virtual Machine is evicted for price reasons when using a Spot instance. At this time the only supported value is <code class="docutils literal notranslate"><span class="pre">Deallocate</span></code>. Changing this forces a new resource to be created.</p></li>
<li><p><strong>identity</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – An <code class="docutils literal notranslate"><span class="pre">identity</span></code> block as defined below.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Azure location where the Linux Virtual Machine should exist. Changing this forces a new resource to be created.</p></li>
<li><p><strong>max_bid_price</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The maximum price you’re willing to pay for this Virtual Machine, in US Dollars; which must be greater than the current spot price. If this bid price falls below the current spot price the Virtual Machine will be evicted using the <code class="docutils literal notranslate"><span class="pre">eviction_policy</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">-1</span></code>, which means that the Virtual Machine should not be evicted for price reasons.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Linux Virtual Machine. Changing this forces a new resource to be created.</p></li>
<li><p><strong>network_interface_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – . A list of Network Interface ID’s which should be attached to this Virtual Machine. The first Network Interface ID in this list will be the Primary Network Interface on the Virtual Machine.</p></li>
<li><p><strong>os_disk</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">os_disk</span></code> block as defined below.</p></li>
<li><p><strong>plan</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">plan</span></code> block as defined below. Changing this forces a new resource to be created.</p></li>
<li><p><strong>priority</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the priority of this Virtual Machine. Possible values are <code class="docutils literal notranslate"><span class="pre">Regular</span></code> and <code class="docutils literal notranslate"><span class="pre">Spot</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">Regular</span></code>. Changing this forces a new resource to be created.</p></li>
<li><p><strong>provision_vm_agent</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Should the Azure VM Agent be provisioned on this Virtual Machine? Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>. Changing this forces a new resource to be created.</p></li>
<li><p><strong>proximity_placement_group_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Proximity Placement Group which the Virtual Machine should be assigned to. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Resource Group in which the Linux Virtual Machine should be exist. Changing this forces a new resource to be created.</p></li>
<li><p><strong>secrets</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">secret</span></code> blocks as defined below.</p></li>
<li><p><strong>size</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The SKU which should be used for this Virtual Machine, such as <code class="docutils literal notranslate"><span class="pre">Standard_F2</span></code>.</p></li>
<li><p><strong>source_image_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Image which this Virtual Machine should be created from. Changing this forces a new resource to be created.</p></li>
<li><p><strong>source_image_reference</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">source_image_reference</span></code> block as defined below. Changing this forces a new resource to be created.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags which should be assigned to this Virtual Machine.</p></li>
<li><p><strong>zone</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Zone in which this Virtual Machine should be created. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>additional_capabilities</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">ultraSsdEnabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Should the capacity to enable Data Disks of the <code class="docutils literal notranslate"><span class="pre">UltraSSD_LRS</span></code> storage account type be supported on this Virtual Machine? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>. Changing this forces a new resource to be created.</p></li>
</ul>
<p>The <strong>admin_ssh_keys</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">publicKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Public Key which should be used for authentication, which needs to be at least 2048-bit and in <code class="docutils literal notranslate"><span class="pre">ssh-rsa</span></code> format. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Username for which this Public SSH Key should be configured. Changing this forces a new resource to be created.</p></li>
</ul>
<p>The <strong>boot_diagnostics</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">storageAccountUri</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Primary/Secondary Endpoint for the Azure Storage Account which should be used to store Boot Diagnostics, including Console Output and Screenshots from the Hypervisor.</p></li>
</ul>
<p>The <strong>identity</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">identityIds</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of User Managed Identity ID’s which should be assigned to the Linux Virtual Machine.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">principal_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the System Managed Service Principal.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The type of Managed Identity which should be assigned to the Linux Virtual Machine. Possible values are <code class="docutils literal notranslate"><span class="pre">SystemAssigned</span></code>, <code class="docutils literal notranslate"><span class="pre">UserAssigned</span></code> and <code class="docutils literal notranslate"><span class="pre">SystemAssigned,</span> <span class="pre">UserAssigned</span></code>.</p></li>
</ul>
<p>The <strong>os_disk</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">caching</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Type of Caching which should be used for the Internal OS Disk. Possible values are <code class="docutils literal notranslate"><span class="pre">None</span></code>, <code class="docutils literal notranslate"><span class="pre">ReadOnly</span></code> and <code class="docutils literal notranslate"><span class="pre">ReadWrite</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">diffDiskSettings</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">diff_disk_settings</span></code> block as defined above.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">option</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the Ephemeral Disk Settings for the OS Disk. At this time the only possible value is <code class="docutils literal notranslate"><span class="pre">Local</span></code>. Changing this forces a new resource to be created.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">disk_encryption_set_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Disk Encryption Set which should be used to Encrypt this OS Disk.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">disk_size_gb</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The Size of the Internal OS Disk in GB, if you wish to vary from the size used in the image this Virtual Machine is sourced from.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name which should be used for the Internal OS Disk. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">storage_account_type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Type of Storage Account which should back this the Internal OS Disk. Possible values are <code class="docutils literal notranslate"><span class="pre">Standard_LRS</span></code>, <code class="docutils literal notranslate"><span class="pre">StandardSSD_LRS</span></code> and <code class="docutils literal notranslate"><span class="pre">Premium_LRS</span></code>. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">write_accelerator_enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Should Write Accelerator be Enabled for this OS Disk? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
</ul>
<p>The <strong>plan</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the Name of the Marketplace Image this Virtual Machine should be created from. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">product</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the Product of the Marketplace Image this Virtual Machine should be created from. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">publisher</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the Publisher of the Marketplace Image this Virtual Machine should be created from. Changing this forces a new resource to be created.</p></li>
</ul>
<p>The <strong>secrets</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">certificates</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - One or more <code class="docutils literal notranslate"><span class="pre">certificate</span></code> blocks as defined above.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">url</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Secret URL of a Key Vault Certificate.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">key_vault_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Key Vault from which all Secrets should be sourced.</p></li>
</ul>
<p>The <strong>source_image_reference</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">offer</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">publisher</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the Publisher of the Marketplace Image this Virtual Machine should be created from. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sku</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">version</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_azure.compute.LinuxVirtualMachine.additional_capabilities">
<code class="sig-name descname">additional_capabilities</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.LinuxVirtualMachine.additional_capabilities" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">additional_capabilities</span></code> block as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">ultraSsdEnabled</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Should the capacity to enable Data Disks of the <code class="docutils literal notranslate"><span class="pre">UltraSSD_LRS</span></code> storage account type be supported on this Virtual Machine? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>. Changing this forces a new resource to be created.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.LinuxVirtualMachine.admin_password">
<code class="sig-name descname">admin_password</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.LinuxVirtualMachine.admin_password" title="Permalink to this definition">¶</a></dt>
<dd><p>The Password which should be used for the local-administrator on this Virtual Machine. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.LinuxVirtualMachine.admin_ssh_keys">
<code class="sig-name descname">admin_ssh_keys</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.LinuxVirtualMachine.admin_ssh_keys" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more <code class="docutils literal notranslate"><span class="pre">admin_ssh_key</span></code> blocks as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">publicKey</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Public Key which should be used for authentication, which needs to be at least 2048-bit and in <code class="docutils literal notranslate"><span class="pre">ssh-rsa</span></code> format. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Username for which this Public SSH Key should be configured. Changing this forces a new resource to be created.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.LinuxVirtualMachine.admin_username">
<code class="sig-name descname">admin_username</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.LinuxVirtualMachine.admin_username" title="Permalink to this definition">¶</a></dt>
<dd><p>The username of the local administrator used for the Virtual Machine. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.LinuxVirtualMachine.allow_extension_operations">
<code class="sig-name descname">allow_extension_operations</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.LinuxVirtualMachine.allow_extension_operations" title="Permalink to this definition">¶</a></dt>
<dd><p>Should Extension Operations be allowed on this Virtual Machine? Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.LinuxVirtualMachine.availability_set_id">
<code class="sig-name descname">availability_set_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.LinuxVirtualMachine.availability_set_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the ID of the Availability Set in which the Virtual Machine should exist. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.LinuxVirtualMachine.boot_diagnostics">
<code class="sig-name descname">boot_diagnostics</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.LinuxVirtualMachine.boot_diagnostics" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">boot_diagnostics</span></code> block as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">storageAccountUri</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Primary/Secondary Endpoint for the Azure Storage Account which should be used to store Boot Diagnostics, including Console Output and Screenshots from the Hypervisor.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.LinuxVirtualMachine.computer_name">
<code class="sig-name descname">computer_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.LinuxVirtualMachine.computer_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the Hostname which should be used for this Virtual Machine. If unspecified this defaults to the value for the <code class="docutils literal notranslate"><span class="pre">name</span></code> field. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.LinuxVirtualMachine.custom_data">
<code class="sig-name descname">custom_data</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.LinuxVirtualMachine.custom_data" title="Permalink to this definition">¶</a></dt>
<dd><p>The Base64-Encoded Custom Data which should be used for this Virtual Machine. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.LinuxVirtualMachine.dedicated_host_id">
<code class="sig-name descname">dedicated_host_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.LinuxVirtualMachine.dedicated_host_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of a Dedicated Host where this machine should be run on. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.LinuxVirtualMachine.disable_password_authentication">
<code class="sig-name descname">disable_password_authentication</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.LinuxVirtualMachine.disable_password_authentication" title="Permalink to this definition">¶</a></dt>
<dd><p>Should Password Authentication be disabled on this Virtual Machine? Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.LinuxVirtualMachine.eviction_policy">
<code class="sig-name descname">eviction_policy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.LinuxVirtualMachine.eviction_policy" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies what should happen when the Virtual Machine is evicted for price reasons when using a Spot instance. At this time the only supported value is <code class="docutils literal notranslate"><span class="pre">Deallocate</span></code>. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.LinuxVirtualMachine.identity">
<code class="sig-name descname">identity</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.LinuxVirtualMachine.identity" title="Permalink to this definition">¶</a></dt>
<dd><p>An <code class="docutils literal notranslate"><span class="pre">identity</span></code> block as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">identityIds</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - A list of User Managed Identity ID’s which should be assigned to the Linux Virtual Machine.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">principal_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the System Managed Service Principal.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The type of Managed Identity which should be assigned to the Linux Virtual Machine. Possible values are <code class="docutils literal notranslate"><span class="pre">SystemAssigned</span></code>, <code class="docutils literal notranslate"><span class="pre">UserAssigned</span></code> and <code class="docutils literal notranslate"><span class="pre">SystemAssigned,</span> <span class="pre">UserAssigned</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.LinuxVirtualMachine.location">
<code class="sig-name descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.LinuxVirtualMachine.location" title="Permalink to this definition">¶</a></dt>
<dd><p>The Azure location where the Linux Virtual Machine should exist. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.LinuxVirtualMachine.max_bid_price">
<code class="sig-name descname">max_bid_price</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.LinuxVirtualMachine.max_bid_price" title="Permalink to this definition">¶</a></dt>
<dd><p>The maximum price you’re willing to pay for this Virtual Machine, in US Dollars; which must be greater than the current spot price. If this bid price falls below the current spot price the Virtual Machine will be evicted using the <code class="docutils literal notranslate"><span class="pre">eviction_policy</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">-1</span></code>, which means that the Virtual Machine should not be evicted for price reasons.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.LinuxVirtualMachine.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.LinuxVirtualMachine.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Linux Virtual Machine. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.LinuxVirtualMachine.network_interface_ids">
<code class="sig-name descname">network_interface_ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.LinuxVirtualMachine.network_interface_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>. A list of Network Interface ID’s which should be attached to this Virtual Machine. The first Network Interface ID in this list will be the Primary Network Interface on the Virtual Machine.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.LinuxVirtualMachine.os_disk">
<code class="sig-name descname">os_disk</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.LinuxVirtualMachine.os_disk" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">os_disk</span></code> block as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">caching</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Type of Caching which should be used for the Internal OS Disk. Possible values are <code class="docutils literal notranslate"><span class="pre">None</span></code>, <code class="docutils literal notranslate"><span class="pre">ReadOnly</span></code> and <code class="docutils literal notranslate"><span class="pre">ReadWrite</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">diffDiskSettings</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - A <code class="docutils literal notranslate"><span class="pre">diff_disk_settings</span></code> block as defined above.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">option</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the Ephemeral Disk Settings for the OS Disk. At this time the only possible value is <code class="docutils literal notranslate"><span class="pre">Local</span></code>. Changing this forces a new resource to be created.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">disk_encryption_set_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the Disk Encryption Set which should be used to Encrypt this OS Disk.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">disk_size_gb</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The Size of the Internal OS Disk in GB, if you wish to vary from the size used in the image this Virtual Machine is sourced from.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name which should be used for the Internal OS Disk. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">storage_account_type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Type of Storage Account which should back this the Internal OS Disk. Possible values are <code class="docutils literal notranslate"><span class="pre">Standard_LRS</span></code>, <code class="docutils literal notranslate"><span class="pre">StandardSSD_LRS</span></code> and <code class="docutils literal notranslate"><span class="pre">Premium_LRS</span></code>. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">write_accelerator_enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Should Write Accelerator be Enabled for this OS Disk? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.LinuxVirtualMachine.plan">
<code class="sig-name descname">plan</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.LinuxVirtualMachine.plan" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">plan</span></code> block as defined below. Changing this forces a new resource to be created.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the Name of the Marketplace Image this Virtual Machine should be created from. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">product</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the Product of the Marketplace Image this Virtual Machine should be created from. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">publisher</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the Publisher of the Marketplace Image this Virtual Machine should be created from. Changing this forces a new resource to be created.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.LinuxVirtualMachine.priority">
<code class="sig-name descname">priority</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.LinuxVirtualMachine.priority" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the priority of this Virtual Machine. Possible values are <code class="docutils literal notranslate"><span class="pre">Regular</span></code> and <code class="docutils literal notranslate"><span class="pre">Spot</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">Regular</span></code>. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.LinuxVirtualMachine.private_ip_address">
<code class="sig-name descname">private_ip_address</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.LinuxVirtualMachine.private_ip_address" title="Permalink to this definition">¶</a></dt>
<dd><p>The Primary Private IP Address assigned to this Virtual Machine.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.LinuxVirtualMachine.private_ip_addresses">
<code class="sig-name descname">private_ip_addresses</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.LinuxVirtualMachine.private_ip_addresses" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of Private IP Addresses assigned to this Virtual Machine.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.LinuxVirtualMachine.provision_vm_agent">
<code class="sig-name descname">provision_vm_agent</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.LinuxVirtualMachine.provision_vm_agent" title="Permalink to this definition">¶</a></dt>
<dd><p>Should the Azure VM Agent be provisioned on this Virtual Machine? Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.LinuxVirtualMachine.proximity_placement_group_id">
<code class="sig-name descname">proximity_placement_group_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.LinuxVirtualMachine.proximity_placement_group_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Proximity Placement Group which the Virtual Machine should be assigned to. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.LinuxVirtualMachine.public_ip_address">
<code class="sig-name descname">public_ip_address</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.LinuxVirtualMachine.public_ip_address" title="Permalink to this definition">¶</a></dt>
<dd><p>The Primary Public IP Address assigned to this Virtual Machine.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.LinuxVirtualMachine.public_ip_addresses">
<code class="sig-name descname">public_ip_addresses</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.LinuxVirtualMachine.public_ip_addresses" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of the Public IP Addresses assigned to this Virtual Machine.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.LinuxVirtualMachine.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.LinuxVirtualMachine.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Resource Group in which the Linux Virtual Machine should be exist. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.LinuxVirtualMachine.secrets">
<code class="sig-name descname">secrets</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.LinuxVirtualMachine.secrets" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more <code class="docutils literal notranslate"><span class="pre">secret</span></code> blocks as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">certificates</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - One or more <code class="docutils literal notranslate"><span class="pre">certificate</span></code> blocks as defined above.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">url</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Secret URL of a Key Vault Certificate.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">key_vault_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the Key Vault from which all Secrets should be sourced.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.LinuxVirtualMachine.size">
<code class="sig-name descname">size</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.LinuxVirtualMachine.size" title="Permalink to this definition">¶</a></dt>
<dd><p>The SKU which should be used for this Virtual Machine, such as <code class="docutils literal notranslate"><span class="pre">Standard_F2</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.LinuxVirtualMachine.source_image_id">
<code class="sig-name descname">source_image_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.LinuxVirtualMachine.source_image_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Image which this Virtual Machine should be created from. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.LinuxVirtualMachine.source_image_reference">
<code class="sig-name descname">source_image_reference</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.LinuxVirtualMachine.source_image_reference" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">source_image_reference</span></code> block as defined below. Changing this forces a new resource to be created.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">offer</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">publisher</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the Publisher of the Marketplace Image this Virtual Machine should be created from. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sku</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">version</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.LinuxVirtualMachine.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.LinuxVirtualMachine.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags which should be assigned to this Virtual Machine.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.LinuxVirtualMachine.virtual_machine_id">
<code class="sig-name descname">virtual_machine_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.LinuxVirtualMachine.virtual_machine_id" title="Permalink to this definition">¶</a></dt>
<dd><p>A 128-bit identifier which uniquely identifies this Virtual Machine.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.LinuxVirtualMachine.zone">
<code class="sig-name descname">zone</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.LinuxVirtualMachine.zone" title="Permalink to this definition">¶</a></dt>
<dd><p>The Zone in which this Virtual Machine should be created. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.compute.LinuxVirtualMachine.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">additional_capabilities=None</em>, <em class="sig-param">admin_password=None</em>, <em class="sig-param">admin_ssh_keys=None</em>, <em class="sig-param">admin_username=None</em>, <em class="sig-param">allow_extension_operations=None</em>, <em class="sig-param">availability_set_id=None</em>, <em class="sig-param">boot_diagnostics=None</em>, <em class="sig-param">computer_name=None</em>, <em class="sig-param">custom_data=None</em>, <em class="sig-param">dedicated_host_id=None</em>, <em class="sig-param">disable_password_authentication=None</em>, <em class="sig-param">eviction_policy=None</em>, <em class="sig-param">identity=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">max_bid_price=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">network_interface_ids=None</em>, <em class="sig-param">os_disk=None</em>, <em class="sig-param">plan=None</em>, <em class="sig-param">priority=None</em>, <em class="sig-param">private_ip_address=None</em>, <em class="sig-param">private_ip_addresses=None</em>, <em class="sig-param">provision_vm_agent=None</em>, <em class="sig-param">proximity_placement_group_id=None</em>, <em class="sig-param">public_ip_address=None</em>, <em class="sig-param">public_ip_addresses=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">secrets=None</em>, <em class="sig-param">size=None</em>, <em class="sig-param">source_image_id=None</em>, <em class="sig-param">source_image_reference=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">virtual_machine_id=None</em>, <em class="sig-param">zone=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.compute.LinuxVirtualMachine.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing LinuxVirtualMachine resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>additional_capabilities</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">additional_capabilities</span></code> block as defined below.</p></li>
<li><p><strong>admin_password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Password which should be used for the local-administrator on this Virtual Machine. Changing this forces a new resource to be created.</p></li>
<li><p><strong>admin_ssh_keys</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">admin_ssh_key</span></code> blocks as defined below.</p></li>
<li><p><strong>admin_username</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The username of the local administrator used for the Virtual Machine. Changing this forces a new resource to be created.</p></li>
<li><p><strong>allow_extension_operations</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Should Extension Operations be allowed on this Virtual Machine? Changing this forces a new resource to be created.</p></li>
<li><p><strong>availability_set_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the ID of the Availability Set in which the Virtual Machine should exist. Changing this forces a new resource to be created.</p></li>
<li><p><strong>boot_diagnostics</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">boot_diagnostics</span></code> block as defined below.</p></li>
<li><p><strong>computer_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the Hostname which should be used for this Virtual Machine. If unspecified this defaults to the value for the <code class="docutils literal notranslate"><span class="pre">name</span></code> field. Changing this forces a new resource to be created.</p></li>
<li><p><strong>custom_data</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Base64-Encoded Custom Data which should be used for this Virtual Machine. Changing this forces a new resource to be created.</p></li>
<li><p><strong>dedicated_host_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of a Dedicated Host where this machine should be run on. Changing this forces a new resource to be created.</p></li>
<li><p><strong>disable_password_authentication</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Should Password Authentication be disabled on this Virtual Machine? Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>. Changing this forces a new resource to be created.</p></li>
<li><p><strong>eviction_policy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies what should happen when the Virtual Machine is evicted for price reasons when using a Spot instance. At this time the only supported value is <code class="docutils literal notranslate"><span class="pre">Deallocate</span></code>. Changing this forces a new resource to be created.</p></li>
<li><p><strong>identity</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – An <code class="docutils literal notranslate"><span class="pre">identity</span></code> block as defined below.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Azure location where the Linux Virtual Machine should exist. Changing this forces a new resource to be created.</p></li>
<li><p><strong>max_bid_price</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The maximum price you’re willing to pay for this Virtual Machine, in US Dollars; which must be greater than the current spot price. If this bid price falls below the current spot price the Virtual Machine will be evicted using the <code class="docutils literal notranslate"><span class="pre">eviction_policy</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">-1</span></code>, which means that the Virtual Machine should not be evicted for price reasons.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Linux Virtual Machine. Changing this forces a new resource to be created.</p></li>
<li><p><strong>network_interface_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – . A list of Network Interface ID’s which should be attached to this Virtual Machine. The first Network Interface ID in this list will be the Primary Network Interface on the Virtual Machine.</p></li>
<li><p><strong>os_disk</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">os_disk</span></code> block as defined below.</p></li>
<li><p><strong>plan</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">plan</span></code> block as defined below. Changing this forces a new resource to be created.</p></li>
<li><p><strong>priority</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the priority of this Virtual Machine. Possible values are <code class="docutils literal notranslate"><span class="pre">Regular</span></code> and <code class="docutils literal notranslate"><span class="pre">Spot</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">Regular</span></code>. Changing this forces a new resource to be created.</p></li>
<li><p><strong>private_ip_address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Primary Private IP Address assigned to this Virtual Machine.</p></li>
<li><p><strong>private_ip_addresses</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of Private IP Addresses assigned to this Virtual Machine.</p></li>
<li><p><strong>provision_vm_agent</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Should the Azure VM Agent be provisioned on this Virtual Machine? Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>. Changing this forces a new resource to be created.</p></li>
<li><p><strong>proximity_placement_group_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Proximity Placement Group which the Virtual Machine should be assigned to. Changing this forces a new resource to be created.</p></li>
<li><p><strong>public_ip_address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Primary Public IP Address assigned to this Virtual Machine.</p></li>
<li><p><strong>public_ip_addresses</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of the Public IP Addresses assigned to this Virtual Machine.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Resource Group in which the Linux Virtual Machine should be exist. Changing this forces a new resource to be created.</p></li>
<li><p><strong>secrets</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">secret</span></code> blocks as defined below.</p></li>
<li><p><strong>size</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The SKU which should be used for this Virtual Machine, such as <code class="docutils literal notranslate"><span class="pre">Standard_F2</span></code>.</p></li>
<li><p><strong>source_image_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Image which this Virtual Machine should be created from. Changing this forces a new resource to be created.</p></li>
<li><p><strong>source_image_reference</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">source_image_reference</span></code> block as defined below. Changing this forces a new resource to be created.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags which should be assigned to this Virtual Machine.</p></li>
<li><p><strong>virtual_machine_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A 128-bit identifier which uniquely identifies this Virtual Machine.</p></li>
<li><p><strong>zone</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Zone in which this Virtual Machine should be created. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>additional_capabilities</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">ultraSsdEnabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Should the capacity to enable Data Disks of the <code class="docutils literal notranslate"><span class="pre">UltraSSD_LRS</span></code> storage account type be supported on this Virtual Machine? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>. Changing this forces a new resource to be created.</p></li>
</ul>
<p>The <strong>admin_ssh_keys</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">publicKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Public Key which should be used for authentication, which needs to be at least 2048-bit and in <code class="docutils literal notranslate"><span class="pre">ssh-rsa</span></code> format. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Username for which this Public SSH Key should be configured. Changing this forces a new resource to be created.</p></li>
</ul>
<p>The <strong>boot_diagnostics</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">storageAccountUri</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Primary/Secondary Endpoint for the Azure Storage Account which should be used to store Boot Diagnostics, including Console Output and Screenshots from the Hypervisor.</p></li>
</ul>
<p>The <strong>identity</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">identityIds</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of User Managed Identity ID’s which should be assigned to the Linux Virtual Machine.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">principal_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the System Managed Service Principal.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The type of Managed Identity which should be assigned to the Linux Virtual Machine. Possible values are <code class="docutils literal notranslate"><span class="pre">SystemAssigned</span></code>, <code class="docutils literal notranslate"><span class="pre">UserAssigned</span></code> and <code class="docutils literal notranslate"><span class="pre">SystemAssigned,</span> <span class="pre">UserAssigned</span></code>.</p></li>
</ul>
<p>The <strong>os_disk</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">caching</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Type of Caching which should be used for the Internal OS Disk. Possible values are <code class="docutils literal notranslate"><span class="pre">None</span></code>, <code class="docutils literal notranslate"><span class="pre">ReadOnly</span></code> and <code class="docutils literal notranslate"><span class="pre">ReadWrite</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">diffDiskSettings</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">diff_disk_settings</span></code> block as defined above.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">option</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the Ephemeral Disk Settings for the OS Disk. At this time the only possible value is <code class="docutils literal notranslate"><span class="pre">Local</span></code>. Changing this forces a new resource to be created.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">disk_encryption_set_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Disk Encryption Set which should be used to Encrypt this OS Disk.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">disk_size_gb</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The Size of the Internal OS Disk in GB, if you wish to vary from the size used in the image this Virtual Machine is sourced from.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name which should be used for the Internal OS Disk. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">storage_account_type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Type of Storage Account which should back this the Internal OS Disk. Possible values are <code class="docutils literal notranslate"><span class="pre">Standard_LRS</span></code>, <code class="docutils literal notranslate"><span class="pre">StandardSSD_LRS</span></code> and <code class="docutils literal notranslate"><span class="pre">Premium_LRS</span></code>. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">write_accelerator_enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Should Write Accelerator be Enabled for this OS Disk? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
</ul>
<p>The <strong>plan</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the Name of the Marketplace Image this Virtual Machine should be created from. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">product</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the Product of the Marketplace Image this Virtual Machine should be created from. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">publisher</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the Publisher of the Marketplace Image this Virtual Machine should be created from. Changing this forces a new resource to be created.</p></li>
</ul>
<p>The <strong>secrets</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">certificates</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - One or more <code class="docutils literal notranslate"><span class="pre">certificate</span></code> blocks as defined above.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">url</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Secret URL of a Key Vault Certificate.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">key_vault_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Key Vault from which all Secrets should be sourced.</p></li>
</ul>
<p>The <strong>source_image_reference</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">offer</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">publisher</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the Publisher of the Marketplace Image this Virtual Machine should be created from. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sku</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">version</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.compute.LinuxVirtualMachine.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.compute.LinuxVirtualMachine.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.compute.LinuxVirtualMachine.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.compute.LinuxVirtualMachine.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.compute.LinuxVirtualMachineScaleSet">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.compute.</code><code class="sig-name descname">LinuxVirtualMachineScaleSet</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">additional_capabilities=None</em>, <em class="sig-param">admin_password=None</em>, <em class="sig-param">admin_ssh_keys=None</em>, <em class="sig-param">admin_username=None</em>, <em class="sig-param">automatic_instance_repair=None</em>, <em class="sig-param">automatic_os_upgrade_policy=None</em>, <em class="sig-param">boot_diagnostics=None</em>, <em class="sig-param">computer_name_prefix=None</em>, <em class="sig-param">custom_data=None</em>, <em class="sig-param">data_disks=None</em>, <em class="sig-param">disable_password_authentication=None</em>, <em class="sig-param">do_not_run_extensions_on_overprovisioned_machines=None</em>, <em class="sig-param">eviction_policy=None</em>, <em class="sig-param">health_probe_id=None</em>, <em class="sig-param">identity=None</em>, <em class="sig-param">instances=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">max_bid_price=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">network_interfaces=None</em>, <em class="sig-param">os_disk=None</em>, <em class="sig-param">overprovision=None</em>, <em class="sig-param">plan=None</em>, <em class="sig-param">priority=None</em>, <em class="sig-param">provision_vm_agent=None</em>, <em class="sig-param">proximity_placement_group_id=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">rolling_upgrade_policy=None</em>, <em class="sig-param">scale_in_policy=None</em>, <em class="sig-param">secrets=None</em>, <em class="sig-param">single_placement_group=None</em>, <em class="sig-param">sku=None</em>, <em class="sig-param">source_image_id=None</em>, <em class="sig-param">source_image_reference=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">terminate_notification=None</em>, <em class="sig-param">upgrade_mode=None</em>, <em class="sig-param">zone_balance=None</em>, <em class="sig-param">zones=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.compute.LinuxVirtualMachineScaleSet" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Linux Virtual Machine Scale Set.</p>
<blockquote>
<div><p><strong>Note</strong> This provider will automatically update &amp; reimage the nodes in the Scale Set (if Required) during an Update - this behaviour can be configured using the <code class="docutils literal notranslate"><span class="pre">features</span></code> configuration within the Provider configuration block.</p>
<p><strong>Note:</strong> This resource does not support Unmanaged Disks. If you need to use Unmanaged Disks you can continue to use the <code class="docutils literal notranslate"><span class="pre">compute.ScaleSet</span></code> resource instead</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>additional_capabilities</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">additional_capabilities</span></code> block as defined below.</p></li>
<li><p><strong>admin_password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Password which should be used for the local-administrator on this Virtual Machine. Changing this forces a new resource to be created.</p></li>
<li><p><strong>admin_ssh_keys</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">admin_ssh_key</span></code> blocks as defined below.</p></li>
<li><p><strong>admin_username</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The username of the local administrator on each Virtual Machine Scale Set instance. Changing this forces a new resource to be created.</p></li>
<li><p><strong>automatic_instance_repair</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">automatic_instance_repair</span></code> block as defined below. To enable the automatic instance repair, this Virtual Machine Scale Set must have a valid <code class="docutils literal notranslate"><span class="pre">health_probe_id</span></code> or an <a class="reference external" href="https://docs.microsoft.com/en-us/azure/virtual-machine-scale-sets/virtual-machine-scale-sets-health-extension">Application Health Extension</a>.</p></li>
<li><p><strong>automatic_os_upgrade_policy</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">automatic_os_upgrade_policy</span></code> block as defined below. This is Required and can only be specified when <code class="docutils literal notranslate"><span class="pre">upgrade_mode</span></code> is set to <code class="docutils literal notranslate"><span class="pre">Automatic</span></code>.</p></li>
<li><p><strong>boot_diagnostics</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">boot_diagnostics</span></code> block as defined below.</p></li>
<li><p><strong>computer_name_prefix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The prefix which should be used for the name of the Virtual Machines in this Scale Set. If unspecified this defaults to the value for the <code class="docutils literal notranslate"><span class="pre">name</span></code> field.</p></li>
<li><p><strong>custom_data</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Base64-Encoded Custom Data which should be used for this Virtual Machine Scale Set.</p></li>
<li><p><strong>data_disks</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">data_disk</span></code> blocks as defined below.</p></li>
<li><p><strong>disable_password_authentication</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Should Password Authentication be disabled on this Virtual Machine Scale Set? Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>do_not_run_extensions_on_overprovisioned_machines</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Should Virtual Machine Extensions be run on Overprovisioned Virtual Machines in the Scale Set? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>eviction_policy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Policy which should be used Virtual Machines are Evicted from the Scale Set. Changing this forces a new resource to be created.</p></li>
<li><p><strong>health_probe_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of a Load Balancer Probe which should be used to determine the health of an instance. Changing this forces a new resource to be created. This is Required and can only be specified when <code class="docutils literal notranslate"><span class="pre">upgrade_mode</span></code> is set to <code class="docutils literal notranslate"><span class="pre">Automatic</span></code> or <code class="docutils literal notranslate"><span class="pre">Rolling</span></code>.</p></li>
<li><p><strong>identity</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">identity</span></code> block as defined below.</p></li>
<li><p><strong>instances</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The number of Virtual Machines in the Scale Set.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Azure location where the Linux Virtual Machine Scale Set should exist. Changing this forces a new resource to be created.</p></li>
<li><p><strong>max_bid_price</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The maximum price you’re willing to pay for each Virtual Machine in this Scale Set, in US Dollars; which must be greater than the current spot price. If this bid price falls below the current spot price the Virtual Machines in the Scale Set will be evicted using the <code class="docutils literal notranslate"><span class="pre">eviction_policy</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">-1</span></code>, which means that each Virtual Machine in this Scale Set should not be evicted for price reasons.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Linux Virtual Machine Scale Set. Changing this forces a new resource to be created.</p></li>
<li><p><strong>network_interfaces</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">network_interface</span></code> blocks as defined below.</p></li>
<li><p><strong>os_disk</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – An <code class="docutils literal notranslate"><span class="pre">os_disk</span></code> block as defined below.</p></li>
<li><p><strong>overprovision</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Should Azure over-provision Virtual Machines in this Scale Set? This means that multiple Virtual Machines will be provisioned and Azure will keep the instances which become available first - which improves provisioning success rates and improves deployment time. You’re not billed for these over-provisioned VM’s and they don’t count towards the Subscription Quota. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>priority</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Priority of this Virtual Machine Scale Set. Possible values are <code class="docutils literal notranslate"><span class="pre">Regular</span></code> and <code class="docutils literal notranslate"><span class="pre">Spot</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">Regular</span></code>. Changing this value forces a new resource.</p></li>
<li><p><strong>provision_vm_agent</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Should the Azure VM Agent be provisioned on each Virtual Machine in the Scale Set? Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>. Changing this value forces a new resource to be created.</p></li>
<li><p><strong>proximity_placement_group_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Proximity Placement Group in which the Virtual Machine Scale Set should be assigned to. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Resource Group in which the Linux Virtual Machine Scale Set should be exist. Changing this forces a new resource to be created.</p></li>
<li><p><strong>rolling_upgrade_policy</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">rolling_upgrade_policy</span></code> block as defined below. This is Required and can only be specified when <code class="docutils literal notranslate"><span class="pre">upgrade_mode</span></code> is set to <code class="docutils literal notranslate"><span class="pre">Automatic</span></code> or <code class="docutils literal notranslate"><span class="pre">Rolling</span></code>.</p></li>
<li><p><strong>scale_in_policy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The scale-in policy rule that decides which virtual machines are chosen for removal when a Virtual Machine Scale Set is scaled in. Possible values for the scale-in policy rules are <code class="docutils literal notranslate"><span class="pre">Default</span></code>, <code class="docutils literal notranslate"><span class="pre">NewestVM</span></code> and <code class="docutils literal notranslate"><span class="pre">OldestVM</span></code>, defaults to <code class="docutils literal notranslate"><span class="pre">Default</span></code>. For more information about scale in policy, please <a class="reference external" href="https://docs.microsoft.com/en-us/azure/virtual-machine-scale-sets/virtual-machine-scale-sets-scale-in-policy">refer to this doc</a>.</p></li>
<li><p><strong>secrets</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">secret</span></code> blocks as defined below.</p></li>
<li><p><strong>single_placement_group</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Should this Virtual Machine Scale Set be limited to a Single Placement Group, which means the number of instances will be capped at 100 Virtual Machines. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>sku</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Virtual Machine SKU for the Scale Set, such as <code class="docutils literal notranslate"><span class="pre">Standard_F2</span></code>.</p></li>
<li><p><strong>source_image_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of an Image which each Virtual Machine in this Scale Set should be based on.</p></li>
<li><p><strong>source_image_reference</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">source_image_reference</span></code> block as defined below.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags which should be assigned to this Virtual Machine Scale Set.</p></li>
<li><p><strong>terminate_notification</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">terminate_notification</span></code> block as defined below.</p></li>
<li><p><strong>upgrade_mode</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies how Upgrades (e.g. changing the Image/SKU) should be performed to Virtual Machine Instances. Possible values are <code class="docutils literal notranslate"><span class="pre">Automatic</span></code>, <code class="docutils literal notranslate"><span class="pre">Manual</span></code> and <code class="docutils literal notranslate"><span class="pre">Rolling</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">Manual</span></code>.</p></li>
<li><p><strong>zone_balance</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Should the Virtual Machines in this Scale Set be strictly evenly distributed across Availability Zones? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>. Changing this forces a new resource to be created.</p></li>
<li><p><strong>zones</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of Availability Zones in which the Virtual Machines in this Scale Set should be created in. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>additional_capabilities</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">ultraSsdEnabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Should the capacity to enable Data Disks of the <code class="docutils literal notranslate"><span class="pre">UltraSSD_LRS</span></code> storage account type be supported on this Virtual Machine Scale Set? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>. Changing this forces a new resource to be created.</p></li>
</ul>
<p>The <strong>admin_ssh_keys</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">publicKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Public Key which should be used for authentication, which needs to be at least 2048-bit and in <code class="docutils literal notranslate"><span class="pre">ssh-rsa</span></code> format.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Username for which this Public SSH Key should be configured.</p></li>
</ul>
<p>The <strong>automatic_instance_repair</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Should the automatic instance repair be enabled on this Virtual Machine Scale Set?</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">gracePeriod</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Amount of time (in minutes, between 30 and 90, defaults to 30 minutes) for which automatic repairs will be delayed. The grace period starts right after the VM is found unhealthy. The time duration should be specified in ISO 8601 format.</p></li>
</ul>
<p>The <strong>automatic_os_upgrade_policy</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">disableAutomaticRollback</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Should automatic rollbacks be disabled? Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enableAutomaticOsUpgrade</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Should OS Upgrades automatically be applied to Scale Set instances in a rolling fashion when a newer version of the OS Image becomes available? Changing this forces a new resource to be created.</p></li>
</ul>
<p>The <strong>boot_diagnostics</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">storageAccountUri</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Primary/Secondary Endpoint for the Azure Storage Account which should be used to store Boot Diagnostics, including Console Output and Screenshots from the Hypervisor.</p></li>
</ul>
<p>The <strong>data_disks</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">caching</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The type of Caching which should be used for this Data Disk. Possible values are <code class="docutils literal notranslate"><span class="pre">None</span></code>, <code class="docutils literal notranslate"><span class="pre">ReadOnly</span></code> and <code class="docutils literal notranslate"><span class="pre">ReadWrite</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">disk_encryption_set_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Disk Encryption Set which should be used to encrypt this Data Disk.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">disk_size_gb</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The size of the Data Disk which should be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">lun</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The Logical Unit Number of the Data Disk, which must be unique within the Virtual Machine.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">storage_account_type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Type of Storage Account which should back this Data Disk. Possible values include <code class="docutils literal notranslate"><span class="pre">Standard_LRS</span></code>, <code class="docutils literal notranslate"><span class="pre">StandardSSD_LRS</span></code>, <code class="docutils literal notranslate"><span class="pre">Premium_LRS</span></code> and <code class="docutils literal notranslate"><span class="pre">UltraSSD_LRS</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">write_accelerator_enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Should Write Accelerator be enabled for this Data Disk? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
</ul>
<p>The <strong>identity</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">identityIds</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of User Managed Identity ID’s which should be assigned to the Linux Virtual Machine Scale Set.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">principal_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the System Managed Service Principal.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The type of Managed Identity which should be assigned to the Linux Virtual Machine Scale Set. Possible values are <code class="docutils literal notranslate"><span class="pre">SystemAssigned</span></code>, <code class="docutils literal notranslate"><span class="pre">UserAssigned</span></code> and <code class="docutils literal notranslate"><span class="pre">SystemAssigned,</span> <span class="pre">UserAssigned</span></code>.</p></li>
</ul>
<p>The <strong>network_interfaces</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">dns_servers</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of IP Addresses of DNS Servers which should be assigned to the Network Interface.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enable_accelerated_networking</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Does this Network Interface support Accelerated Networking? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enable_ip_forwarding</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Does this Network Interface support IP Forwarding? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ip_configurations</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - One or more <code class="docutils literal notranslate"><span class="pre">ip_configuration</span></code> blocks as defined above.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">applicationGatewayBackendAddressPoolIds</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of Backend Address Pools ID’s from a Application Gateway which this Virtual Machine Scale Set should be connected to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">applicationSecurityGroupIds</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of Application Security Group ID’s which this Virtual Machine Scale Set should be connected to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">loadBalancerBackendAddressPoolIds</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of Backend Address Pools ID’s from a Load Balancer which this Virtual Machine Scale Set should be connected to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">loadBalancerInboundNatRulesIds</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of NAT Rule ID’s from a Load Balancer which this Virtual Machine Scale Set should be connected to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Name which should be used for this IP Configuration.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">primary</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Is this the Primary IP Configuration for this Network Interface? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">public_ip_addresses</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">public_ip_address</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">domain_name_label</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Prefix which should be used for the Domain Name Label for each Virtual Machine Instance. Azure concatenates the Domain Name Label and Virtual Machine Index to create a unique Domain Name Label for each Virtual Machine.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">idle_timeout_in_minutes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The Idle Timeout in Minutes for the Public IP Address. Possible values are in the range <code class="docutils literal notranslate"><span class="pre">4</span></code> to <code class="docutils literal notranslate"><span class="pre">32</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ipTags</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - One or more <code class="docutils literal notranslate"><span class="pre">ip_tag</span></code> blocks as defined above.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">tag</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The IP Tag associated with the Public IP, such as <code class="docutils literal notranslate"><span class="pre">SQL</span></code> or <code class="docutils literal notranslate"><span class="pre">Storage</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Type of IP Tag, such as <code class="docutils literal notranslate"><span class="pre">FirstPartyUsage</span></code>.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Name of the Public IP Address Configuration.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">public_ip_prefix_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Public IP Address Prefix from where Public IP Addresses should be allocated. Changing this forces a new resource to be created.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnet_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Subnet which this IP Configuration should be connected to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">version</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Internet Protocol Version which should be used for this IP Configuration. Possible values are <code class="docutils literal notranslate"><span class="pre">IPv4</span></code> and <code class="docutils literal notranslate"><span class="pre">IPv6</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">IPv4</span></code>.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Name which should be used for this Network Interface. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">network_security_group_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of a Network Security Group which should be assigned to this Network Interface.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">primary</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Is this the Primary IP Configuration?</p></li>
</ul>
<p>The <strong>os_disk</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">caching</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Type of Caching which should be used for the Internal OS Disk. Possible values are <code class="docutils literal notranslate"><span class="pre">None</span></code>, <code class="docutils literal notranslate"><span class="pre">ReadOnly</span></code> and <code class="docutils literal notranslate"><span class="pre">ReadWrite</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">diffDiskSettings</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">diff_disk_settings</span></code> block as defined above. Changing this forces a new resource to be created.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">option</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">disk_encryption_set_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Disk Encryption Set which should be used to encrypt this OS Disk.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">disk_size_gb</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The Size of the Internal OS Disk in GB, if you wish to vary from the size used in the image this Virtual Machine Scale Set is sourced from.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">storage_account_type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Type of Storage Account which should back this the Internal OS Disk. Possible values include <code class="docutils literal notranslate"><span class="pre">Standard_LRS</span></code>, <code class="docutils literal notranslate"><span class="pre">StandardSSD_LRS</span></code> and <code class="docutils literal notranslate"><span class="pre">Premium_LRS</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">write_accelerator_enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Should Write Accelerator be Enabled for this OS Disk? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
</ul>
<p>The <strong>plan</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the Linux Virtual Machine Scale Set. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">product</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">publisher</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>rolling_upgrade_policy</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">maxBatchInstancePercent</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The maximum percent of total virtual machine instances that will be upgraded simultaneously by the rolling upgrade in one batch. As this is a maximum, unhealthy instances in previous or future batches can cause the percentage of instances in a batch to decrease to ensure higher reliability. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxUnhealthyInstancePercent</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The maximum percentage of the total virtual machine instances in the scale set that can be simultaneously unhealthy, either as a result of being upgraded, or by being found in an unhealthy state by the virtual machine health checks before the rolling upgrade aborts. This constraint will be checked prior to starting any batch. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxUnhealthyUpgradedInstancePercent</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The maximum percentage of upgraded virtual machine instances that can be found to be in an unhealthy state. This check will happen after each batch is upgraded. If this percentage is ever exceeded, the rolling update aborts. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">pauseTimeBetweenBatches</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The wait time between completing the update for all virtual machines in one batch and starting the next batch. The time duration should be specified in ISO 8601 format. Changing this forces a new resource to be created.</p></li>
</ul>
<p>The <strong>secrets</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">certificates</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - One or more <code class="docutils literal notranslate"><span class="pre">certificate</span></code> blocks as defined above.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">url</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Secret URL of a Key Vault Certificate.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">key_vault_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Key Vault from which all Secrets should be sourced.</p></li>
</ul>
<p>The <strong>source_image_reference</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">offer</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">publisher</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sku</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Virtual Machine SKU for the Scale Set, such as <code class="docutils literal notranslate"><span class="pre">Standard_F2</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">version</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Internet Protocol Version which should be used for this IP Configuration. Possible values are <code class="docutils literal notranslate"><span class="pre">IPv4</span></code> and <code class="docutils literal notranslate"><span class="pre">IPv6</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">IPv4</span></code>.</p></li>
</ul>
<p>The <strong>terminate_notification</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Should the terminate notification be enabled on this Virtual Machine Scale Set? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timeout</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Length of time (in minutes, between 5 and 15) a notification to be sent to the VM on the instance metadata server till the VM gets deleted. The time duration should be specified in ISO 8601 format.</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_azure.compute.LinuxVirtualMachineScaleSet.additional_capabilities">
<code class="sig-name descname">additional_capabilities</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.LinuxVirtualMachineScaleSet.additional_capabilities" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">additional_capabilities</span></code> block as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">ultraSsdEnabled</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Should the capacity to enable Data Disks of the <code class="docutils literal notranslate"><span class="pre">UltraSSD_LRS</span></code> storage account type be supported on this Virtual Machine Scale Set? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>. Changing this forces a new resource to be created.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.LinuxVirtualMachineScaleSet.admin_password">
<code class="sig-name descname">admin_password</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.LinuxVirtualMachineScaleSet.admin_password" title="Permalink to this definition">¶</a></dt>
<dd><p>The Password which should be used for the local-administrator on this Virtual Machine. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.LinuxVirtualMachineScaleSet.admin_ssh_keys">
<code class="sig-name descname">admin_ssh_keys</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.LinuxVirtualMachineScaleSet.admin_ssh_keys" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more <code class="docutils literal notranslate"><span class="pre">admin_ssh_key</span></code> blocks as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">publicKey</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Public Key which should be used for authentication, which needs to be at least 2048-bit and in <code class="docutils literal notranslate"><span class="pre">ssh-rsa</span></code> format.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Username for which this Public SSH Key should be configured.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.LinuxVirtualMachineScaleSet.admin_username">
<code class="sig-name descname">admin_username</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.LinuxVirtualMachineScaleSet.admin_username" title="Permalink to this definition">¶</a></dt>
<dd><p>The username of the local administrator on each Virtual Machine Scale Set instance. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.LinuxVirtualMachineScaleSet.automatic_instance_repair">
<code class="sig-name descname">automatic_instance_repair</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.LinuxVirtualMachineScaleSet.automatic_instance_repair" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">automatic_instance_repair</span></code> block as defined below. To enable the automatic instance repair, this Virtual Machine Scale Set must have a valid <code class="docutils literal notranslate"><span class="pre">health_probe_id</span></code> or an <a class="reference external" href="https://docs.microsoft.com/en-us/azure/virtual-machine-scale-sets/virtual-machine-scale-sets-health-extension">Application Health Extension</a>.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Should the automatic instance repair be enabled on this Virtual Machine Scale Set?</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">gracePeriod</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Amount of time (in minutes, between 30 and 90, defaults to 30 minutes) for which automatic repairs will be delayed. The grace period starts right after the VM is found unhealthy. The time duration should be specified in ISO 8601 format.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.LinuxVirtualMachineScaleSet.automatic_os_upgrade_policy">
<code class="sig-name descname">automatic_os_upgrade_policy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.LinuxVirtualMachineScaleSet.automatic_os_upgrade_policy" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">automatic_os_upgrade_policy</span></code> block as defined below. This is Required and can only be specified when <code class="docutils literal notranslate"><span class="pre">upgrade_mode</span></code> is set to <code class="docutils literal notranslate"><span class="pre">Automatic</span></code>.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">disableAutomaticRollback</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Should automatic rollbacks be disabled? Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enableAutomaticOsUpgrade</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Should OS Upgrades automatically be applied to Scale Set instances in a rolling fashion when a newer version of the OS Image becomes available? Changing this forces a new resource to be created.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.LinuxVirtualMachineScaleSet.boot_diagnostics">
<code class="sig-name descname">boot_diagnostics</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.LinuxVirtualMachineScaleSet.boot_diagnostics" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">boot_diagnostics</span></code> block as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">storageAccountUri</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Primary/Secondary Endpoint for the Azure Storage Account which should be used to store Boot Diagnostics, including Console Output and Screenshots from the Hypervisor.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.LinuxVirtualMachineScaleSet.computer_name_prefix">
<code class="sig-name descname">computer_name_prefix</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.LinuxVirtualMachineScaleSet.computer_name_prefix" title="Permalink to this definition">¶</a></dt>
<dd><p>The prefix which should be used for the name of the Virtual Machines in this Scale Set. If unspecified this defaults to the value for the <code class="docutils literal notranslate"><span class="pre">name</span></code> field.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.LinuxVirtualMachineScaleSet.custom_data">
<code class="sig-name descname">custom_data</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.LinuxVirtualMachineScaleSet.custom_data" title="Permalink to this definition">¶</a></dt>
<dd><p>The Base64-Encoded Custom Data which should be used for this Virtual Machine Scale Set.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.LinuxVirtualMachineScaleSet.data_disks">
<code class="sig-name descname">data_disks</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.LinuxVirtualMachineScaleSet.data_disks" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more <code class="docutils literal notranslate"><span class="pre">data_disk</span></code> blocks as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">caching</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The type of Caching which should be used for this Data Disk. Possible values are <code class="docutils literal notranslate"><span class="pre">None</span></code>, <code class="docutils literal notranslate"><span class="pre">ReadOnly</span></code> and <code class="docutils literal notranslate"><span class="pre">ReadWrite</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">disk_encryption_set_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the Disk Encryption Set which should be used to encrypt this Data Disk.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">disk_size_gb</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The size of the Data Disk which should be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">lun</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The Logical Unit Number of the Data Disk, which must be unique within the Virtual Machine.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">storage_account_type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Type of Storage Account which should back this Data Disk. Possible values include <code class="docutils literal notranslate"><span class="pre">Standard_LRS</span></code>, <code class="docutils literal notranslate"><span class="pre">StandardSSD_LRS</span></code>, <code class="docutils literal notranslate"><span class="pre">Premium_LRS</span></code> and <code class="docutils literal notranslate"><span class="pre">UltraSSD_LRS</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">write_accelerator_enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Should Write Accelerator be enabled for this Data Disk? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.LinuxVirtualMachineScaleSet.disable_password_authentication">
<code class="sig-name descname">disable_password_authentication</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.LinuxVirtualMachineScaleSet.disable_password_authentication" title="Permalink to this definition">¶</a></dt>
<dd><p>Should Password Authentication be disabled on this Virtual Machine Scale Set? Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.LinuxVirtualMachineScaleSet.do_not_run_extensions_on_overprovisioned_machines">
<code class="sig-name descname">do_not_run_extensions_on_overprovisioned_machines</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.LinuxVirtualMachineScaleSet.do_not_run_extensions_on_overprovisioned_machines" title="Permalink to this definition">¶</a></dt>
<dd><p>Should Virtual Machine Extensions be run on Overprovisioned Virtual Machines in the Scale Set? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.LinuxVirtualMachineScaleSet.eviction_policy">
<code class="sig-name descname">eviction_policy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.LinuxVirtualMachineScaleSet.eviction_policy" title="Permalink to this definition">¶</a></dt>
<dd><p>The Policy which should be used Virtual Machines are Evicted from the Scale Set. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.LinuxVirtualMachineScaleSet.health_probe_id">
<code class="sig-name descname">health_probe_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.LinuxVirtualMachineScaleSet.health_probe_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of a Load Balancer Probe which should be used to determine the health of an instance. Changing this forces a new resource to be created. This is Required and can only be specified when <code class="docutils literal notranslate"><span class="pre">upgrade_mode</span></code> is set to <code class="docutils literal notranslate"><span class="pre">Automatic</span></code> or <code class="docutils literal notranslate"><span class="pre">Rolling</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.LinuxVirtualMachineScaleSet.identity">
<code class="sig-name descname">identity</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.LinuxVirtualMachineScaleSet.identity" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">identity</span></code> block as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">identityIds</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - A list of User Managed Identity ID’s which should be assigned to the Linux Virtual Machine Scale Set.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">principal_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the System Managed Service Principal.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The type of Managed Identity which should be assigned to the Linux Virtual Machine Scale Set. Possible values are <code class="docutils literal notranslate"><span class="pre">SystemAssigned</span></code>, <code class="docutils literal notranslate"><span class="pre">UserAssigned</span></code> and <code class="docutils literal notranslate"><span class="pre">SystemAssigned,</span> <span class="pre">UserAssigned</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.LinuxVirtualMachineScaleSet.instances">
<code class="sig-name descname">instances</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.LinuxVirtualMachineScaleSet.instances" title="Permalink to this definition">¶</a></dt>
<dd><p>The number of Virtual Machines in the Scale Set.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.LinuxVirtualMachineScaleSet.location">
<code class="sig-name descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.LinuxVirtualMachineScaleSet.location" title="Permalink to this definition">¶</a></dt>
<dd><p>The Azure location where the Linux Virtual Machine Scale Set should exist. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.LinuxVirtualMachineScaleSet.max_bid_price">
<code class="sig-name descname">max_bid_price</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.LinuxVirtualMachineScaleSet.max_bid_price" title="Permalink to this definition">¶</a></dt>
<dd><p>The maximum price you’re willing to pay for each Virtual Machine in this Scale Set, in US Dollars; which must be greater than the current spot price. If this bid price falls below the current spot price the Virtual Machines in the Scale Set will be evicted using the <code class="docutils literal notranslate"><span class="pre">eviction_policy</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">-1</span></code>, which means that each Virtual Machine in this Scale Set should not be evicted for price reasons.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.LinuxVirtualMachineScaleSet.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.LinuxVirtualMachineScaleSet.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Linux Virtual Machine Scale Set. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.LinuxVirtualMachineScaleSet.network_interfaces">
<code class="sig-name descname">network_interfaces</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.LinuxVirtualMachineScaleSet.network_interfaces" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more <code class="docutils literal notranslate"><span class="pre">network_interface</span></code> blocks as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">dns_servers</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - A list of IP Addresses of DNS Servers which should be assigned to the Network Interface.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enable_accelerated_networking</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Does this Network Interface support Accelerated Networking? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enable_ip_forwarding</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Does this Network Interface support IP Forwarding? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ip_configurations</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - One or more <code class="docutils literal notranslate"><span class="pre">ip_configuration</span></code> blocks as defined above.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">applicationGatewayBackendAddressPoolIds</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - A list of Backend Address Pools ID’s from a Application Gateway which this Virtual Machine Scale Set should be connected to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">applicationSecurityGroupIds</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - A list of Application Security Group ID’s which this Virtual Machine Scale Set should be connected to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">loadBalancerBackendAddressPoolIds</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - A list of Backend Address Pools ID’s from a Load Balancer which this Virtual Machine Scale Set should be connected to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">loadBalancerInboundNatRulesIds</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - A list of NAT Rule ID’s from a Load Balancer which this Virtual Machine Scale Set should be connected to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Name which should be used for this IP Configuration.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">primary</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Is this the Primary IP Configuration for this Network Interface? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">public_ip_addresses</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - A <code class="docutils literal notranslate"><span class="pre">public_ip_address</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">domain_name_label</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Prefix which should be used for the Domain Name Label for each Virtual Machine Instance. Azure concatenates the Domain Name Label and Virtual Machine Index to create a unique Domain Name Label for each Virtual Machine.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">idle_timeout_in_minutes</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The Idle Timeout in Minutes for the Public IP Address. Possible values are in the range <code class="docutils literal notranslate"><span class="pre">4</span></code> to <code class="docutils literal notranslate"><span class="pre">32</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ipTags</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - One or more <code class="docutils literal notranslate"><span class="pre">ip_tag</span></code> blocks as defined above.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">tag</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The IP Tag associated with the Public IP, such as <code class="docutils literal notranslate"><span class="pre">SQL</span></code> or <code class="docutils literal notranslate"><span class="pre">Storage</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Type of IP Tag, such as <code class="docutils literal notranslate"><span class="pre">FirstPartyUsage</span></code>.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Name of the Public IP Address Configuration.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">public_ip_prefix_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the Public IP Address Prefix from where Public IP Addresses should be allocated. Changing this forces a new resource to be created.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnet_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the Subnet which this IP Configuration should be connected to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">version</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Internet Protocol Version which should be used for this IP Configuration. Possible values are <code class="docutils literal notranslate"><span class="pre">IPv4</span></code> and <code class="docutils literal notranslate"><span class="pre">IPv6</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">IPv4</span></code>.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Name which should be used for this Network Interface. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">network_security_group_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of a Network Security Group which should be assigned to this Network Interface.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">primary</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Is this the Primary IP Configuration?</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.LinuxVirtualMachineScaleSet.os_disk">
<code class="sig-name descname">os_disk</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.LinuxVirtualMachineScaleSet.os_disk" title="Permalink to this definition">¶</a></dt>
<dd><p>An <code class="docutils literal notranslate"><span class="pre">os_disk</span></code> block as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">caching</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Type of Caching which should be used for the Internal OS Disk. Possible values are <code class="docutils literal notranslate"><span class="pre">None</span></code>, <code class="docutils literal notranslate"><span class="pre">ReadOnly</span></code> and <code class="docutils literal notranslate"><span class="pre">ReadWrite</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">diffDiskSettings</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - A <code class="docutils literal notranslate"><span class="pre">diff_disk_settings</span></code> block as defined above. Changing this forces a new resource to be created.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">option</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">disk_encryption_set_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the Disk Encryption Set which should be used to encrypt this OS Disk.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">disk_size_gb</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The Size of the Internal OS Disk in GB, if you wish to vary from the size used in the image this Virtual Machine Scale Set is sourced from.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">storage_account_type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Type of Storage Account which should back this the Internal OS Disk. Possible values include <code class="docutils literal notranslate"><span class="pre">Standard_LRS</span></code>, <code class="docutils literal notranslate"><span class="pre">StandardSSD_LRS</span></code> and <code class="docutils literal notranslate"><span class="pre">Premium_LRS</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">write_accelerator_enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Should Write Accelerator be Enabled for this OS Disk? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.LinuxVirtualMachineScaleSet.overprovision">
<code class="sig-name descname">overprovision</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.LinuxVirtualMachineScaleSet.overprovision" title="Permalink to this definition">¶</a></dt>
<dd><p>Should Azure over-provision Virtual Machines in this Scale Set? This means that multiple Virtual Machines will be provisioned and Azure will keep the instances which become available first - which improves provisioning success rates and improves deployment time. You’re not billed for these over-provisioned VM’s and they don’t count towards the Subscription Quota. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.LinuxVirtualMachineScaleSet.priority">
<code class="sig-name descname">priority</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.LinuxVirtualMachineScaleSet.priority" title="Permalink to this definition">¶</a></dt>
<dd><p>The Priority of this Virtual Machine Scale Set. Possible values are <code class="docutils literal notranslate"><span class="pre">Regular</span></code> and <code class="docutils literal notranslate"><span class="pre">Spot</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">Regular</span></code>. Changing this value forces a new resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.LinuxVirtualMachineScaleSet.provision_vm_agent">
<code class="sig-name descname">provision_vm_agent</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.LinuxVirtualMachineScaleSet.provision_vm_agent" title="Permalink to this definition">¶</a></dt>
<dd><p>Should the Azure VM Agent be provisioned on each Virtual Machine in the Scale Set? Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>. Changing this value forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.LinuxVirtualMachineScaleSet.proximity_placement_group_id">
<code class="sig-name descname">proximity_placement_group_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.LinuxVirtualMachineScaleSet.proximity_placement_group_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Proximity Placement Group in which the Virtual Machine Scale Set should be assigned to. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.LinuxVirtualMachineScaleSet.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.LinuxVirtualMachineScaleSet.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Resource Group in which the Linux Virtual Machine Scale Set should be exist. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.LinuxVirtualMachineScaleSet.rolling_upgrade_policy">
<code class="sig-name descname">rolling_upgrade_policy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.LinuxVirtualMachineScaleSet.rolling_upgrade_policy" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">rolling_upgrade_policy</span></code> block as defined below. This is Required and can only be specified when <code class="docutils literal notranslate"><span class="pre">upgrade_mode</span></code> is set to <code class="docutils literal notranslate"><span class="pre">Automatic</span></code> or <code class="docutils literal notranslate"><span class="pre">Rolling</span></code>.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">maxBatchInstancePercent</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The maximum percent of total virtual machine instances that will be upgraded simultaneously by the rolling upgrade in one batch. As this is a maximum, unhealthy instances in previous or future batches can cause the percentage of instances in a batch to decrease to ensure higher reliability. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxUnhealthyInstancePercent</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The maximum percentage of the total virtual machine instances in the scale set that can be simultaneously unhealthy, either as a result of being upgraded, or by being found in an unhealthy state by the virtual machine health checks before the rolling upgrade aborts. This constraint will be checked prior to starting any batch. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxUnhealthyUpgradedInstancePercent</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The maximum percentage of upgraded virtual machine instances that can be found to be in an unhealthy state. This check will happen after each batch is upgraded. If this percentage is ever exceeded, the rolling update aborts. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">pauseTimeBetweenBatches</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The wait time between completing the update for all virtual machines in one batch and starting the next batch. The time duration should be specified in ISO 8601 format. Changing this forces a new resource to be created.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.LinuxVirtualMachineScaleSet.scale_in_policy">
<code class="sig-name descname">scale_in_policy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.LinuxVirtualMachineScaleSet.scale_in_policy" title="Permalink to this definition">¶</a></dt>
<dd><p>The scale-in policy rule that decides which virtual machines are chosen for removal when a Virtual Machine Scale Set is scaled in. Possible values for the scale-in policy rules are <code class="docutils literal notranslate"><span class="pre">Default</span></code>, <code class="docutils literal notranslate"><span class="pre">NewestVM</span></code> and <code class="docutils literal notranslate"><span class="pre">OldestVM</span></code>, defaults to <code class="docutils literal notranslate"><span class="pre">Default</span></code>. For more information about scale in policy, please <a class="reference external" href="https://docs.microsoft.com/en-us/azure/virtual-machine-scale-sets/virtual-machine-scale-sets-scale-in-policy">refer to this doc</a>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.LinuxVirtualMachineScaleSet.secrets">
<code class="sig-name descname">secrets</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.LinuxVirtualMachineScaleSet.secrets" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more <code class="docutils literal notranslate"><span class="pre">secret</span></code> blocks as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">certificates</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - One or more <code class="docutils literal notranslate"><span class="pre">certificate</span></code> blocks as defined above.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">url</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Secret URL of a Key Vault Certificate.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">key_vault_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the Key Vault from which all Secrets should be sourced.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.LinuxVirtualMachineScaleSet.single_placement_group">
<code class="sig-name descname">single_placement_group</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.LinuxVirtualMachineScaleSet.single_placement_group" title="Permalink to this definition">¶</a></dt>
<dd><p>Should this Virtual Machine Scale Set be limited to a Single Placement Group, which means the number of instances will be capped at 100 Virtual Machines. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.LinuxVirtualMachineScaleSet.sku">
<code class="sig-name descname">sku</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.LinuxVirtualMachineScaleSet.sku" title="Permalink to this definition">¶</a></dt>
<dd><p>The Virtual Machine SKU for the Scale Set, such as <code class="docutils literal notranslate"><span class="pre">Standard_F2</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.LinuxVirtualMachineScaleSet.source_image_id">
<code class="sig-name descname">source_image_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.LinuxVirtualMachineScaleSet.source_image_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of an Image which each Virtual Machine in this Scale Set should be based on.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.LinuxVirtualMachineScaleSet.source_image_reference">
<code class="sig-name descname">source_image_reference</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.LinuxVirtualMachineScaleSet.source_image_reference" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">source_image_reference</span></code> block as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">offer</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">publisher</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sku</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Virtual Machine SKU for the Scale Set, such as <code class="docutils literal notranslate"><span class="pre">Standard_F2</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">version</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Internet Protocol Version which should be used for this IP Configuration. Possible values are <code class="docutils literal notranslate"><span class="pre">IPv4</span></code> and <code class="docutils literal notranslate"><span class="pre">IPv6</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">IPv4</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.LinuxVirtualMachineScaleSet.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.LinuxVirtualMachineScaleSet.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags which should be assigned to this Virtual Machine Scale Set.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.LinuxVirtualMachineScaleSet.terminate_notification">
<code class="sig-name descname">terminate_notification</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.LinuxVirtualMachineScaleSet.terminate_notification" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">terminate_notification</span></code> block as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Should the terminate notification be enabled on this Virtual Machine Scale Set? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timeout</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Length of time (in minutes, between 5 and 15) a notification to be sent to the VM on the instance metadata server till the VM gets deleted. The time duration should be specified in ISO 8601 format.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.LinuxVirtualMachineScaleSet.unique_id">
<code class="sig-name descname">unique_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.LinuxVirtualMachineScaleSet.unique_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The Unique ID for this Linux Virtual Machine Scale Set.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.LinuxVirtualMachineScaleSet.upgrade_mode">
<code class="sig-name descname">upgrade_mode</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.LinuxVirtualMachineScaleSet.upgrade_mode" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies how Upgrades (e.g. changing the Image/SKU) should be performed to Virtual Machine Instances. Possible values are <code class="docutils literal notranslate"><span class="pre">Automatic</span></code>, <code class="docutils literal notranslate"><span class="pre">Manual</span></code> and <code class="docutils literal notranslate"><span class="pre">Rolling</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">Manual</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.LinuxVirtualMachineScaleSet.zone_balance">
<code class="sig-name descname">zone_balance</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.LinuxVirtualMachineScaleSet.zone_balance" title="Permalink to this definition">¶</a></dt>
<dd><p>Should the Virtual Machines in this Scale Set be strictly evenly distributed across Availability Zones? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.LinuxVirtualMachineScaleSet.zones">
<code class="sig-name descname">zones</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.LinuxVirtualMachineScaleSet.zones" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of Availability Zones in which the Virtual Machines in this Scale Set should be created in. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.compute.LinuxVirtualMachineScaleSet.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">additional_capabilities=None</em>, <em class="sig-param">admin_password=None</em>, <em class="sig-param">admin_ssh_keys=None</em>, <em class="sig-param">admin_username=None</em>, <em class="sig-param">automatic_instance_repair=None</em>, <em class="sig-param">automatic_os_upgrade_policy=None</em>, <em class="sig-param">boot_diagnostics=None</em>, <em class="sig-param">computer_name_prefix=None</em>, <em class="sig-param">custom_data=None</em>, <em class="sig-param">data_disks=None</em>, <em class="sig-param">disable_password_authentication=None</em>, <em class="sig-param">do_not_run_extensions_on_overprovisioned_machines=None</em>, <em class="sig-param">eviction_policy=None</em>, <em class="sig-param">health_probe_id=None</em>, <em class="sig-param">identity=None</em>, <em class="sig-param">instances=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">max_bid_price=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">network_interfaces=None</em>, <em class="sig-param">os_disk=None</em>, <em class="sig-param">overprovision=None</em>, <em class="sig-param">plan=None</em>, <em class="sig-param">priority=None</em>, <em class="sig-param">provision_vm_agent=None</em>, <em class="sig-param">proximity_placement_group_id=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">rolling_upgrade_policy=None</em>, <em class="sig-param">scale_in_policy=None</em>, <em class="sig-param">secrets=None</em>, <em class="sig-param">single_placement_group=None</em>, <em class="sig-param">sku=None</em>, <em class="sig-param">source_image_id=None</em>, <em class="sig-param">source_image_reference=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">terminate_notification=None</em>, <em class="sig-param">unique_id=None</em>, <em class="sig-param">upgrade_mode=None</em>, <em class="sig-param">zone_balance=None</em>, <em class="sig-param">zones=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.compute.LinuxVirtualMachineScaleSet.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing LinuxVirtualMachineScaleSet resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>additional_capabilities</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">additional_capabilities</span></code> block as defined below.</p></li>
<li><p><strong>admin_password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Password which should be used for the local-administrator on this Virtual Machine. Changing this forces a new resource to be created.</p></li>
<li><p><strong>admin_ssh_keys</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">admin_ssh_key</span></code> blocks as defined below.</p></li>
<li><p><strong>admin_username</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The username of the local administrator on each Virtual Machine Scale Set instance. Changing this forces a new resource to be created.</p></li>
<li><p><strong>automatic_instance_repair</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – <p>A <code class="docutils literal notranslate"><span class="pre">automatic_instance_repair</span></code> block as defined below. To enable the automatic instance repair, this Virtual Machine Scale Set must have a valid <code class="docutils literal notranslate"><span class="pre">health_probe_id</span></code> or an <a class="reference external" href="https://docs.microsoft.com/en-us/azure/virtual-machine-scale-sets/virtual-machine-scale-sets-health-extension">Application Health Extension</a>.</p>
</p></li>
<li><p><strong>automatic_os_upgrade_policy</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">automatic_os_upgrade_policy</span></code> block as defined below. This is Required and can only be specified when <code class="docutils literal notranslate"><span class="pre">upgrade_mode</span></code> is set to <code class="docutils literal notranslate"><span class="pre">Automatic</span></code>.</p></li>
<li><p><strong>boot_diagnostics</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">boot_diagnostics</span></code> block as defined below.</p></li>
<li><p><strong>computer_name_prefix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The prefix which should be used for the name of the Virtual Machines in this Scale Set. If unspecified this defaults to the value for the <code class="docutils literal notranslate"><span class="pre">name</span></code> field.</p></li>
<li><p><strong>custom_data</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Base64-Encoded Custom Data which should be used for this Virtual Machine Scale Set.</p></li>
<li><p><strong>data_disks</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">data_disk</span></code> blocks as defined below.</p></li>
<li><p><strong>disable_password_authentication</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Should Password Authentication be disabled on this Virtual Machine Scale Set? Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>do_not_run_extensions_on_overprovisioned_machines</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Should Virtual Machine Extensions be run on Overprovisioned Virtual Machines in the Scale Set? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>eviction_policy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Policy which should be used Virtual Machines are Evicted from the Scale Set. Changing this forces a new resource to be created.</p></li>
<li><p><strong>health_probe_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of a Load Balancer Probe which should be used to determine the health of an instance. Changing this forces a new resource to be created. This is Required and can only be specified when <code class="docutils literal notranslate"><span class="pre">upgrade_mode</span></code> is set to <code class="docutils literal notranslate"><span class="pre">Automatic</span></code> or <code class="docutils literal notranslate"><span class="pre">Rolling</span></code>.</p></li>
<li><p><strong>identity</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">identity</span></code> block as defined below.</p></li>
<li><p><strong>instances</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The number of Virtual Machines in the Scale Set.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Azure location where the Linux Virtual Machine Scale Set should exist. Changing this forces a new resource to be created.</p></li>
<li><p><strong>max_bid_price</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The maximum price you’re willing to pay for each Virtual Machine in this Scale Set, in US Dollars; which must be greater than the current spot price. If this bid price falls below the current spot price the Virtual Machines in the Scale Set will be evicted using the <code class="docutils literal notranslate"><span class="pre">eviction_policy</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">-1</span></code>, which means that each Virtual Machine in this Scale Set should not be evicted for price reasons.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Linux Virtual Machine Scale Set. Changing this forces a new resource to be created.</p></li>
<li><p><strong>network_interfaces</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">network_interface</span></code> blocks as defined below.</p></li>
<li><p><strong>os_disk</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – An <code class="docutils literal notranslate"><span class="pre">os_disk</span></code> block as defined below.</p></li>
<li><p><strong>overprovision</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Should Azure over-provision Virtual Machines in this Scale Set? This means that multiple Virtual Machines will be provisioned and Azure will keep the instances which become available first - which improves provisioning success rates and improves deployment time. You’re not billed for these over-provisioned VM’s and they don’t count towards the Subscription Quota. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>priority</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Priority of this Virtual Machine Scale Set. Possible values are <code class="docutils literal notranslate"><span class="pre">Regular</span></code> and <code class="docutils literal notranslate"><span class="pre">Spot</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">Regular</span></code>. Changing this value forces a new resource.</p></li>
<li><p><strong>provision_vm_agent</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Should the Azure VM Agent be provisioned on each Virtual Machine in the Scale Set? Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>. Changing this value forces a new resource to be created.</p></li>
<li><p><strong>proximity_placement_group_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Proximity Placement Group in which the Virtual Machine Scale Set should be assigned to. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Resource Group in which the Linux Virtual Machine Scale Set should be exist. Changing this forces a new resource to be created.</p></li>
<li><p><strong>rolling_upgrade_policy</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">rolling_upgrade_policy</span></code> block as defined below. This is Required and can only be specified when <code class="docutils literal notranslate"><span class="pre">upgrade_mode</span></code> is set to <code class="docutils literal notranslate"><span class="pre">Automatic</span></code> or <code class="docutils literal notranslate"><span class="pre">Rolling</span></code>.</p></li>
<li><p><strong>scale_in_policy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The scale-in policy rule that decides which virtual machines are chosen for removal when a Virtual Machine Scale Set is scaled in. Possible values for the scale-in policy rules are <code class="docutils literal notranslate"><span class="pre">Default</span></code>, <code class="docutils literal notranslate"><span class="pre">NewestVM</span></code> and <code class="docutils literal notranslate"><span class="pre">OldestVM</span></code>, defaults to <code class="docutils literal notranslate"><span class="pre">Default</span></code>. For more information about scale in policy, please <a class="reference external" href="https://docs.microsoft.com/en-us/azure/virtual-machine-scale-sets/virtual-machine-scale-sets-scale-in-policy">refer to this doc</a>.</p>
</p></li>
<li><p><strong>secrets</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">secret</span></code> blocks as defined below.</p></li>
<li><p><strong>single_placement_group</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Should this Virtual Machine Scale Set be limited to a Single Placement Group, which means the number of instances will be capped at 100 Virtual Machines. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>sku</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Virtual Machine SKU for the Scale Set, such as <code class="docutils literal notranslate"><span class="pre">Standard_F2</span></code>.</p></li>
<li><p><strong>source_image_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of an Image which each Virtual Machine in this Scale Set should be based on.</p></li>
<li><p><strong>source_image_reference</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">source_image_reference</span></code> block as defined below.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags which should be assigned to this Virtual Machine Scale Set.</p></li>
<li><p><strong>terminate_notification</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">terminate_notification</span></code> block as defined below.</p></li>
<li><p><strong>unique_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Unique ID for this Linux Virtual Machine Scale Set.</p></li>
<li><p><strong>upgrade_mode</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies how Upgrades (e.g. changing the Image/SKU) should be performed to Virtual Machine Instances. Possible values are <code class="docutils literal notranslate"><span class="pre">Automatic</span></code>, <code class="docutils literal notranslate"><span class="pre">Manual</span></code> and <code class="docutils literal notranslate"><span class="pre">Rolling</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">Manual</span></code>.</p></li>
<li><p><strong>zone_balance</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Should the Virtual Machines in this Scale Set be strictly evenly distributed across Availability Zones? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>. Changing this forces a new resource to be created.</p></li>
<li><p><strong>zones</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of Availability Zones in which the Virtual Machines in this Scale Set should be created in. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>additional_capabilities</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">ultraSsdEnabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Should the capacity to enable Data Disks of the <code class="docutils literal notranslate"><span class="pre">UltraSSD_LRS</span></code> storage account type be supported on this Virtual Machine Scale Set? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>. Changing this forces a new resource to be created.</p></li>
</ul>
<p>The <strong>admin_ssh_keys</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">publicKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Public Key which should be used for authentication, which needs to be at least 2048-bit and in <code class="docutils literal notranslate"><span class="pre">ssh-rsa</span></code> format.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">username</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Username for which this Public SSH Key should be configured.</p></li>
</ul>
<p>The <strong>automatic_instance_repair</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Should the automatic instance repair be enabled on this Virtual Machine Scale Set?</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">gracePeriod</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Amount of time (in minutes, between 30 and 90, defaults to 30 minutes) for which automatic repairs will be delayed. The grace period starts right after the VM is found unhealthy. The time duration should be specified in ISO 8601 format.</p></li>
</ul>
<p>The <strong>automatic_os_upgrade_policy</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">disableAutomaticRollback</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Should automatic rollbacks be disabled? Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enableAutomaticOsUpgrade</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Should OS Upgrades automatically be applied to Scale Set instances in a rolling fashion when a newer version of the OS Image becomes available? Changing this forces a new resource to be created.</p></li>
</ul>
<p>The <strong>boot_diagnostics</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">storageAccountUri</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Primary/Secondary Endpoint for the Azure Storage Account which should be used to store Boot Diagnostics, including Console Output and Screenshots from the Hypervisor.</p></li>
</ul>
<p>The <strong>data_disks</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">caching</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The type of Caching which should be used for this Data Disk. Possible values are <code class="docutils literal notranslate"><span class="pre">None</span></code>, <code class="docutils literal notranslate"><span class="pre">ReadOnly</span></code> and <code class="docutils literal notranslate"><span class="pre">ReadWrite</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">disk_encryption_set_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Disk Encryption Set which should be used to encrypt this Data Disk.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">disk_size_gb</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The size of the Data Disk which should be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">lun</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The Logical Unit Number of the Data Disk, which must be unique within the Virtual Machine.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">storage_account_type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Type of Storage Account which should back this Data Disk. Possible values include <code class="docutils literal notranslate"><span class="pre">Standard_LRS</span></code>, <code class="docutils literal notranslate"><span class="pre">StandardSSD_LRS</span></code>, <code class="docutils literal notranslate"><span class="pre">Premium_LRS</span></code> and <code class="docutils literal notranslate"><span class="pre">UltraSSD_LRS</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">write_accelerator_enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Should Write Accelerator be enabled for this Data Disk? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
</ul>
<p>The <strong>identity</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">identityIds</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of User Managed Identity ID’s which should be assigned to the Linux Virtual Machine Scale Set.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">principal_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the System Managed Service Principal.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The type of Managed Identity which should be assigned to the Linux Virtual Machine Scale Set. Possible values are <code class="docutils literal notranslate"><span class="pre">SystemAssigned</span></code>, <code class="docutils literal notranslate"><span class="pre">UserAssigned</span></code> and <code class="docutils literal notranslate"><span class="pre">SystemAssigned,</span> <span class="pre">UserAssigned</span></code>.</p></li>
</ul>
<p>The <strong>network_interfaces</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">dns_servers</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of IP Addresses of DNS Servers which should be assigned to the Network Interface.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enable_accelerated_networking</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Does this Network Interface support Accelerated Networking? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enable_ip_forwarding</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Does this Network Interface support IP Forwarding? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ip_configurations</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - One or more <code class="docutils literal notranslate"><span class="pre">ip_configuration</span></code> blocks as defined above.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">applicationGatewayBackendAddressPoolIds</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of Backend Address Pools ID’s from a Application Gateway which this Virtual Machine Scale Set should be connected to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">applicationSecurityGroupIds</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of Application Security Group ID’s which this Virtual Machine Scale Set should be connected to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">loadBalancerBackendAddressPoolIds</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of Backend Address Pools ID’s from a Load Balancer which this Virtual Machine Scale Set should be connected to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">loadBalancerInboundNatRulesIds</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of NAT Rule ID’s from a Load Balancer which this Virtual Machine Scale Set should be connected to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Name which should be used for this IP Configuration.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">primary</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Is this the Primary IP Configuration for this Network Interface? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">public_ip_addresses</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">public_ip_address</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">domain_name_label</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Prefix which should be used for the Domain Name Label for each Virtual Machine Instance. Azure concatenates the Domain Name Label and Virtual Machine Index to create a unique Domain Name Label for each Virtual Machine.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">idle_timeout_in_minutes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The Idle Timeout in Minutes for the Public IP Address. Possible values are in the range <code class="docutils literal notranslate"><span class="pre">4</span></code> to <code class="docutils literal notranslate"><span class="pre">32</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ipTags</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - One or more <code class="docutils literal notranslate"><span class="pre">ip_tag</span></code> blocks as defined above.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">tag</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The IP Tag associated with the Public IP, such as <code class="docutils literal notranslate"><span class="pre">SQL</span></code> or <code class="docutils literal notranslate"><span class="pre">Storage</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Type of IP Tag, such as <code class="docutils literal notranslate"><span class="pre">FirstPartyUsage</span></code>.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Name of the Public IP Address Configuration.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">public_ip_prefix_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Public IP Address Prefix from where Public IP Addresses should be allocated. Changing this forces a new resource to be created.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnet_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Subnet which this IP Configuration should be connected to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">version</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Internet Protocol Version which should be used for this IP Configuration. Possible values are <code class="docutils literal notranslate"><span class="pre">IPv4</span></code> and <code class="docutils literal notranslate"><span class="pre">IPv6</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">IPv4</span></code>.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Name which should be used for this Network Interface. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">network_security_group_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of a Network Security Group which should be assigned to this Network Interface.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">primary</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Is this the Primary IP Configuration?</p></li>
</ul>
<p>The <strong>os_disk</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">caching</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Type of Caching which should be used for the Internal OS Disk. Possible values are <code class="docutils literal notranslate"><span class="pre">None</span></code>, <code class="docutils literal notranslate"><span class="pre">ReadOnly</span></code> and <code class="docutils literal notranslate"><span class="pre">ReadWrite</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">diffDiskSettings</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">diff_disk_settings</span></code> block as defined above. Changing this forces a new resource to be created.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">option</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">disk_encryption_set_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Disk Encryption Set which should be used to encrypt this OS Disk.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">disk_size_gb</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The Size of the Internal OS Disk in GB, if you wish to vary from the size used in the image this Virtual Machine Scale Set is sourced from.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">storage_account_type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Type of Storage Account which should back this the Internal OS Disk. Possible values include <code class="docutils literal notranslate"><span class="pre">Standard_LRS</span></code>, <code class="docutils literal notranslate"><span class="pre">StandardSSD_LRS</span></code> and <code class="docutils literal notranslate"><span class="pre">Premium_LRS</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">write_accelerator_enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Should Write Accelerator be Enabled for this OS Disk? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
</ul>
<p>The <strong>plan</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the Linux Virtual Machine Scale Set. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">product</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">publisher</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>rolling_upgrade_policy</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">maxBatchInstancePercent</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The maximum percent of total virtual machine instances that will be upgraded simultaneously by the rolling upgrade in one batch. As this is a maximum, unhealthy instances in previous or future batches can cause the percentage of instances in a batch to decrease to ensure higher reliability. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxUnhealthyInstancePercent</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The maximum percentage of the total virtual machine instances in the scale set that can be simultaneously unhealthy, either as a result of being upgraded, or by being found in an unhealthy state by the virtual machine health checks before the rolling upgrade aborts. This constraint will be checked prior to starting any batch. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxUnhealthyUpgradedInstancePercent</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The maximum percentage of upgraded virtual machine instances that can be found to be in an unhealthy state. This check will happen after each batch is upgraded. If this percentage is ever exceeded, the rolling update aborts. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">pauseTimeBetweenBatches</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The wait time between completing the update for all virtual machines in one batch and starting the next batch. The time duration should be specified in ISO 8601 format. Changing this forces a new resource to be created.</p></li>
</ul>
<p>The <strong>secrets</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">certificates</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - One or more <code class="docutils literal notranslate"><span class="pre">certificate</span></code> blocks as defined above.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">url</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Secret URL of a Key Vault Certificate.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">key_vault_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Key Vault from which all Secrets should be sourced.</p></li>
</ul>
<p>The <strong>source_image_reference</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">offer</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">publisher</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sku</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Virtual Machine SKU for the Scale Set, such as <code class="docutils literal notranslate"><span class="pre">Standard_F2</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">version</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Internet Protocol Version which should be used for this IP Configuration. Possible values are <code class="docutils literal notranslate"><span class="pre">IPv4</span></code> and <code class="docutils literal notranslate"><span class="pre">IPv6</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">IPv4</span></code>.</p></li>
</ul>
<p>The <strong>terminate_notification</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Should the terminate notification be enabled on this Virtual Machine Scale Set? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timeout</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Length of time (in minutes, between 5 and 15) a notification to be sent to the VM on the instance metadata server till the VM gets deleted. The time duration should be specified in ISO 8601 format.</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.compute.LinuxVirtualMachineScaleSet.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.compute.LinuxVirtualMachineScaleSet.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.compute.LinuxVirtualMachineScaleSet.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.compute.LinuxVirtualMachineScaleSet.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.compute.</code><code class="sig-name descname">ManagedDisk</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">create_option=None</em>, <em class="sig-param">disk_encryption_set_id=None</em>, <em class="sig-param">disk_iops_read_write=None</em>, <em class="sig-param">disk_mbps_read_write=None</em>, <em class="sig-param">disk_size_gb=None</em>, <em class="sig-param">encryption_settings=None</em>, <em class="sig-param">image_reference_id=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">os_type=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">source_resource_id=None</em>, <em class="sig-param">source_uri=None</em>, <em class="sig-param">storage_account_id=None</em>, <em class="sig-param">storage_account_type=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">zones=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.compute.ManagedDisk" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a managed disk.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>create_option</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The method to use when creating the managed disk. Changing this forces a new resource to be created. Possible values include:</p></li>
<li><p><strong>disk_encryption_set_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of a Disk Encryption Set which should be used to encrypt this Managed Disk.</p></li>
<li><p><strong>disk_iops_read_write</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The number of IOPS allowed for this disk; only settable for UltraSSD disks. One operation can transfer between 4k and 256k bytes.</p></li>
<li><p><strong>disk_mbps_read_write</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The bandwidth allowed for this disk; only settable for UltraSSD disks. MBps means millions of bytes per second.</p></li>
<li><p><strong>disk_size_gb</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Specifies the size of the managed disk to create in gigabytes. If <code class="docutils literal notranslate"><span class="pre">create_option</span></code> is <code class="docutils literal notranslate"><span class="pre">Copy</span></code> or <code class="docutils literal notranslate"><span class="pre">FromImage</span></code>, then the value must be equal to or greater than the source’s size. The size can only be increased.</p></li>
<li><p><strong>encryption_settings</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">encryption_settings</span></code> block as defined below.</p></li>
<li><p><strong>image_reference_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – ID of an existing platform/marketplace disk image to copy when <code class="docutils literal notranslate"><span class="pre">create_option</span></code> is <code class="docutils literal notranslate"><span class="pre">FromImage</span></code>.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specified the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Managed Disk. Changing this forces a new resource to be created.</p></li>
<li><p><strong>os_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specify a value when the source of an <code class="docutils literal notranslate"><span class="pre">Import</span></code> or <code class="docutils literal notranslate"><span class="pre">Copy</span></code> operation targets a source that contains an operating system. Valid values are <code class="docutils literal notranslate"><span class="pre">Linux</span></code> or <code class="docutils literal notranslate"><span class="pre">Windows</span></code>.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Resource Group where the Managed Disk should exist.</p></li>
<li><p><strong>source_resource_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of an existing Managed Disk to copy <code class="docutils literal notranslate"><span class="pre">create_option</span></code> is <code class="docutils literal notranslate"><span class="pre">Copy</span></code> or the recovery point to restore when <code class="docutils literal notranslate"><span class="pre">create_option</span></code> is <code class="docutils literal notranslate"><span class="pre">Restore</span></code></p></li>
<li><p><strong>source_uri</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – URI to a valid VHD file to be used when <code class="docutils literal notranslate"><span class="pre">create_option</span></code> is <code class="docutils literal notranslate"><span class="pre">Import</span></code>.</p></li>
<li><p><strong>storage_account_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Storage Account where the <code class="docutils literal notranslate"><span class="pre">source_uri</span></code> is located. Required when <code class="docutils literal notranslate"><span class="pre">create_option</span></code> is set to <code class="docutils literal notranslate"><span class="pre">Import</span></code>.  Changing this forces a new resource to be created.</p></li>
<li><p><strong>storage_account_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of storage to use for the managed disk. Possible values are <code class="docutils literal notranslate"><span class="pre">Standard_LRS</span></code>, <code class="docutils literal notranslate"><span class="pre">Premium_LRS</span></code>, <code class="docutils literal notranslate"><span class="pre">StandardSSD_LRS</span></code> or <code class="docutils literal notranslate"><span class="pre">UltraSSD_LRS</span></code>.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
<li><p><strong>zones</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A collection containing the availability zone to allocate the Managed Disk in.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>encryption_settings</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">diskEncryptionKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">disk_encryption_key</span></code> block as defined above.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">secretUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The URL to the Key Vault Secret used as the Disk Encryption Key. This can be found as <code class="docutils literal notranslate"><span class="pre">id</span></code> on the <code class="docutils literal notranslate"><span class="pre">keyvault.Secret</span></code> resource.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sourceVaultId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the source Key Vault.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Is Encryption enabled on this Managed Disk? Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">keyEncryptionKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">key_encryption_key</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">keyUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The URL to the Key Vault Key used as the Key Encryption Key. This can be found as <code class="docutils literal notranslate"><span class="pre">id</span></code> on the <code class="docutils literal notranslate"><span class="pre">keyvault.Key</span></code> resource.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sourceVaultId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the source Key Vault.</p></li>
</ul>
</li>
</ul>
<dl class="attribute">
<dt id="pulumi_azure.compute.ManagedDisk.create_option">
<code class="sig-name descname">create_option</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.ManagedDisk.create_option" title="Permalink to this definition">¶</a></dt>
<dd><p>The method to use when creating the managed disk. Changing this forces a new resource to be created. Possible values include:</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.ManagedDisk.disk_encryption_set_id">
<code class="sig-name descname">disk_encryption_set_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.ManagedDisk.disk_encryption_set_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of a Disk Encryption Set which should be used to encrypt this Managed Disk.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.ManagedDisk.disk_iops_read_write">
<code class="sig-name descname">disk_iops_read_write</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.ManagedDisk.disk_iops_read_write" title="Permalink to this definition">¶</a></dt>
<dd><p>The number of IOPS allowed for this disk; only settable for UltraSSD disks. One operation can transfer between 4k and 256k bytes.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.ManagedDisk.disk_mbps_read_write">
<code class="sig-name descname">disk_mbps_read_write</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.ManagedDisk.disk_mbps_read_write" title="Permalink to this definition">¶</a></dt>
<dd><p>The bandwidth allowed for this disk; only settable for UltraSSD disks. MBps means millions of bytes per second.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.ManagedDisk.disk_size_gb">
<code class="sig-name descname">disk_size_gb</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.ManagedDisk.disk_size_gb" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the size of the managed disk to create in gigabytes. If <code class="docutils literal notranslate"><span class="pre">create_option</span></code> is <code class="docutils literal notranslate"><span class="pre">Copy</span></code> or <code class="docutils literal notranslate"><span class="pre">FromImage</span></code>, then the value must be equal to or greater than the source’s size. The size can only be increased.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.ManagedDisk.encryption_settings">
<code class="sig-name descname">encryption_settings</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.ManagedDisk.encryption_settings" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">encryption_settings</span></code> block as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">diskEncryptionKey</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - A <code class="docutils literal notranslate"><span class="pre">disk_encryption_key</span></code> block as defined above.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">secretUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The URL to the Key Vault Secret used as the Disk Encryption Key. This can be found as <code class="docutils literal notranslate"><span class="pre">id</span></code> on the <code class="docutils literal notranslate"><span class="pre">keyvault.Secret</span></code> resource.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sourceVaultId</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the source Key Vault.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Is Encryption enabled on this Managed Disk? Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">keyEncryptionKey</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - A <code class="docutils literal notranslate"><span class="pre">key_encryption_key</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">keyUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The URL to the Key Vault Key used as the Key Encryption Key. This can be found as <code class="docutils literal notranslate"><span class="pre">id</span></code> on the <code class="docutils literal notranslate"><span class="pre">keyvault.Key</span></code> resource.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sourceVaultId</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the source Key Vault.</p></li>
</ul>
</li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.ManagedDisk.image_reference_id">
<code class="sig-name descname">image_reference_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.ManagedDisk.image_reference_id" title="Permalink to this definition">¶</a></dt>
<dd><p>ID of an existing platform/marketplace disk image to copy when <code class="docutils literal notranslate"><span class="pre">create_option</span></code> is <code class="docutils literal notranslate"><span class="pre">FromImage</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.ManagedDisk.location">
<code class="sig-name descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.ManagedDisk.location" title="Permalink to this definition">¶</a></dt>
<dd><p>Specified the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.ManagedDisk.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.ManagedDisk.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Managed Disk. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.ManagedDisk.os_type">
<code class="sig-name descname">os_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.ManagedDisk.os_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Specify a value when the source of an <code class="docutils literal notranslate"><span class="pre">Import</span></code> or <code class="docutils literal notranslate"><span class="pre">Copy</span></code> operation targets a source that contains an operating system. Valid values are <code class="docutils literal notranslate"><span class="pre">Linux</span></code> or <code class="docutils literal notranslate"><span class="pre">Windows</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.ManagedDisk.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.ManagedDisk.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Resource Group where the Managed Disk should exist.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.ManagedDisk.source_resource_id">
<code class="sig-name descname">source_resource_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.ManagedDisk.source_resource_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of an existing Managed Disk to copy <code class="docutils literal notranslate"><span class="pre">create_option</span></code> is <code class="docutils literal notranslate"><span class="pre">Copy</span></code> or the recovery point to restore when <code class="docutils literal notranslate"><span class="pre">create_option</span></code> is <code class="docutils literal notranslate"><span class="pre">Restore</span></code></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.ManagedDisk.source_uri">
<code class="sig-name descname">source_uri</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.ManagedDisk.source_uri" title="Permalink to this definition">¶</a></dt>
<dd><p>URI to a valid VHD file to be used when <code class="docutils literal notranslate"><span class="pre">create_option</span></code> is <code class="docutils literal notranslate"><span class="pre">Import</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.ManagedDisk.storage_account_id">
<code class="sig-name descname">storage_account_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.ManagedDisk.storage_account_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Storage Account where the <code class="docutils literal notranslate"><span class="pre">source_uri</span></code> is located. Required when <code class="docutils literal notranslate"><span class="pre">create_option</span></code> is set to <code class="docutils literal notranslate"><span class="pre">Import</span></code>.  Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.ManagedDisk.storage_account_type">
<code class="sig-name descname">storage_account_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.ManagedDisk.storage_account_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of storage to use for the managed disk. Possible values are <code class="docutils literal notranslate"><span class="pre">Standard_LRS</span></code>, <code class="docutils literal notranslate"><span class="pre">Premium_LRS</span></code>, <code class="docutils literal notranslate"><span class="pre">StandardSSD_LRS</span></code> or <code class="docutils literal notranslate"><span class="pre">UltraSSD_LRS</span></code>.</p>
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
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">create_option=None</em>, <em class="sig-param">disk_encryption_set_id=None</em>, <em class="sig-param">disk_iops_read_write=None</em>, <em class="sig-param">disk_mbps_read_write=None</em>, <em class="sig-param">disk_size_gb=None</em>, <em class="sig-param">encryption_settings=None</em>, <em class="sig-param">image_reference_id=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">os_type=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">source_resource_id=None</em>, <em class="sig-param">source_uri=None</em>, <em class="sig-param">storage_account_id=None</em>, <em class="sig-param">storage_account_type=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">zones=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.compute.ManagedDisk.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ManagedDisk resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>create_option</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The method to use when creating the managed disk. Changing this forces a new resource to be created. Possible values include:</p></li>
<li><p><strong>disk_encryption_set_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of a Disk Encryption Set which should be used to encrypt this Managed Disk.</p></li>
<li><p><strong>disk_iops_read_write</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The number of IOPS allowed for this disk; only settable for UltraSSD disks. One operation can transfer between 4k and 256k bytes.</p></li>
<li><p><strong>disk_mbps_read_write</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The bandwidth allowed for this disk; only settable for UltraSSD disks. MBps means millions of bytes per second.</p></li>
<li><p><strong>disk_size_gb</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Specifies the size of the managed disk to create in gigabytes. If <code class="docutils literal notranslate"><span class="pre">create_option</span></code> is <code class="docutils literal notranslate"><span class="pre">Copy</span></code> or <code class="docutils literal notranslate"><span class="pre">FromImage</span></code>, then the value must be equal to or greater than the source’s size. The size can only be increased.</p></li>
<li><p><strong>encryption_settings</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">encryption_settings</span></code> block as defined below.</p></li>
<li><p><strong>image_reference_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – ID of an existing platform/marketplace disk image to copy when <code class="docutils literal notranslate"><span class="pre">create_option</span></code> is <code class="docutils literal notranslate"><span class="pre">FromImage</span></code>.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specified the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Managed Disk. Changing this forces a new resource to be created.</p></li>
<li><p><strong>os_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specify a value when the source of an <code class="docutils literal notranslate"><span class="pre">Import</span></code> or <code class="docutils literal notranslate"><span class="pre">Copy</span></code> operation targets a source that contains an operating system. Valid values are <code class="docutils literal notranslate"><span class="pre">Linux</span></code> or <code class="docutils literal notranslate"><span class="pre">Windows</span></code>.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Resource Group where the Managed Disk should exist.</p></li>
<li><p><strong>source_resource_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of an existing Managed Disk to copy <code class="docutils literal notranslate"><span class="pre">create_option</span></code> is <code class="docutils literal notranslate"><span class="pre">Copy</span></code> or the recovery point to restore when <code class="docutils literal notranslate"><span class="pre">create_option</span></code> is <code class="docutils literal notranslate"><span class="pre">Restore</span></code></p></li>
<li><p><strong>source_uri</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – URI to a valid VHD file to be used when <code class="docutils literal notranslate"><span class="pre">create_option</span></code> is <code class="docutils literal notranslate"><span class="pre">Import</span></code>.</p></li>
<li><p><strong>storage_account_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Storage Account where the <code class="docutils literal notranslate"><span class="pre">source_uri</span></code> is located. Required when <code class="docutils literal notranslate"><span class="pre">create_option</span></code> is set to <code class="docutils literal notranslate"><span class="pre">Import</span></code>.  Changing this forces a new resource to be created.</p></li>
<li><p><strong>storage_account_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of storage to use for the managed disk. Possible values are <code class="docutils literal notranslate"><span class="pre">Standard_LRS</span></code>, <code class="docutils literal notranslate"><span class="pre">Premium_LRS</span></code>, <code class="docutils literal notranslate"><span class="pre">StandardSSD_LRS</span></code> or <code class="docutils literal notranslate"><span class="pre">UltraSSD_LRS</span></code>.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
<li><p><strong>zones</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A collection containing the availability zone to allocate the Managed Disk in.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>encryption_settings</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">diskEncryptionKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">disk_encryption_key</span></code> block as defined above.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">secretUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The URL to the Key Vault Secret used as the Disk Encryption Key. This can be found as <code class="docutils literal notranslate"><span class="pre">id</span></code> on the <code class="docutils literal notranslate"><span class="pre">keyvault.Secret</span></code> resource.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sourceVaultId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the source Key Vault.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Is Encryption enabled on this Managed Disk? Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">keyEncryptionKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">key_encryption_key</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">keyUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The URL to the Key Vault Key used as the Key Encryption Key. This can be found as <code class="docutils literal notranslate"><span class="pre">id</span></code> on the <code class="docutils literal notranslate"><span class="pre">keyvault.Key</span></code> resource.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sourceVaultId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the source Key Vault.</p></li>
</ul>
</li>
</ul>
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
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.compute.</code><code class="sig-name descname">ScaleSet</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">automatic_os_upgrade=None</em>, <em class="sig-param">boot_diagnostics=None</em>, <em class="sig-param">eviction_policy=None</em>, <em class="sig-param">extensions=None</em>, <em class="sig-param">health_probe_id=None</em>, <em class="sig-param">identity=None</em>, <em class="sig-param">license_type=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">network_profiles=None</em>, <em class="sig-param">os_profile=None</em>, <em class="sig-param">os_profile_linux_config=None</em>, <em class="sig-param">os_profile_secrets=None</em>, <em class="sig-param">os_profile_windows_config=None</em>, <em class="sig-param">overprovision=None</em>, <em class="sig-param">plan=None</em>, <em class="sig-param">priority=None</em>, <em class="sig-param">proximity_placement_group_id=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">rolling_upgrade_policy=None</em>, <em class="sig-param">single_placement_group=None</em>, <em class="sig-param">sku=None</em>, <em class="sig-param">storage_profile_data_disks=None</em>, <em class="sig-param">storage_profile_image_reference=None</em>, <em class="sig-param">storage_profile_os_disk=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">upgrade_policy_mode=None</em>, <em class="sig-param">zones=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.compute.ScaleSet" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a virtual machine scale set.</p>
<blockquote>
<div><p><strong>Note:</strong> The <code class="docutils literal notranslate"><span class="pre">compute.ScaleSet</span></code> resource has been superseded by the <code class="docutils literal notranslate"><span class="pre">compute.LinuxVirtualMachineScaleSet</span></code> and <code class="docutils literal notranslate"><span class="pre">compute.WindowsVirtualMachineScaleSet</span></code> resources. The existing <code class="docutils literal notranslate"><span class="pre">compute.ScaleSet</span></code> resource will continue to be available throughout the 2.x releases however is in a feature-frozen state to maintain compatibility - new functionality will instead be added to the <code class="docutils literal notranslate"><span class="pre">compute.LinuxVirtualMachineScaleSet</span></code> and <code class="docutils literal notranslate"><span class="pre">compute.WindowsVirtualMachineScaleSet</span></code> resources.</p>
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
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the virtual machine scale set resource. Changing this forces a new resource to be created.</p></li>
<li><p><strong>network_profiles</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A collection of network profile block as documented below.</p></li>
<li><p><strong>os_profile</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A Virtual Machine OS Profile block as documented below.</p></li>
<li><p><strong>os_profile_linux_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A Linux config block as documented below.</p></li>
<li><p><strong>os_profile_secrets</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A collection of Secret blocks as documented below.</p></li>
<li><p><strong>os_profile_windows_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A Windows config block as documented below.</p></li>
<li><p><strong>overprovision</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specifies whether the virtual machine scale set should be overprovisioned.</p></li>
<li><p><strong>plan</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A plan block as documented below.</p></li>
<li><p><strong>priority</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the priority for the Virtual Machines in the Scale Set. Defaults to <code class="docutils literal notranslate"><span class="pre">Regular</span></code>. Possible values are <code class="docutils literal notranslate"><span class="pre">Low</span></code> and <code class="docutils literal notranslate"><span class="pre">Regular</span></code>.</p></li>
<li><p><strong>proximity_placement_group_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Proximity Placement Group to which this Virtual Machine should be assigned. Changing this forces a new resource to be created</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the virtual machine scale set. Changing this forces a new resource to be created.</p></li>
<li><p><strong>rolling_upgrade_policy</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">rolling_upgrade_policy</span></code> block as defined below. This is only applicable when the <code class="docutils literal notranslate"><span class="pre">upgrade_policy_mode</span></code> is <code class="docutils literal notranslate"><span class="pre">Rolling</span></code>.</p></li>
<li><p><strong>single_placement_group</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specifies whether the scale set is limited to a single placement group with a maximum size of 100 virtual machines. If set to false, managed disks must be used. Default is true. Changing this forces a new resource to be created. See <a class="reference external" href="http://docs.microsoft.com/en-us/azure/virtual-machine-scale-sets/virtual-machine-scale-sets-placement-groups">documentation</a> for more information.</p></li>
<li><p><strong>sku</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A sku block as documented below.</p></li>
<li><p><strong>storage_profile_data_disks</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A storage profile data disk block as documented below</p></li>
<li><p><strong>storage_profile_image_reference</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A storage profile image reference block as documented below.</p></li>
<li><p><strong>storage_profile_os_disk</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A storage profile os disk block as documented below</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
<li><p><strong>upgrade_policy_mode</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the mode of an upgrade to virtual machines in the scale set. Possible values, <code class="docutils literal notranslate"><span class="pre">Rolling</span></code>, <code class="docutils literal notranslate"><span class="pre">Manual</span></code>, or <code class="docutils literal notranslate"><span class="pre">Automatic</span></code>. When choosing <code class="docutils literal notranslate"><span class="pre">Rolling</span></code>, you will need to set a health probe.</p></li>
<li><p><strong>zones</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A collection of availability zones to spread the Virtual Machines over.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>boot_diagnostics</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">storageUri</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>extensions</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">auto_upgrade_minor_version</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Specifies whether or not to use the latest minor version available.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the name of the extension.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">protected_settings</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The protected_settings passed to the extension, like settings, these are specified as a JSON object in a string.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">provision_after_extensions</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Specifies a dependency array of extensions required to be executed before, the array stores the name of each extension.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">publisher</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The publisher of the extension, available publishers can be found by using the Azure CLI.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">settings</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The settings passed to the extension, these are specified as a JSON object in a string.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The type of extension, available types for a publisher can be found using the Azure CLI.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type_handler_version</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the version of the extension to use, available versions can be found using the Azure CLI.</p></li>
</ul>
<p>The <strong>identity</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">identityIds</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Specifies a list of user managed identity ids to be assigned to the VMSS. Required if <code class="docutils literal notranslate"><span class="pre">type</span></code> is <code class="docutils literal notranslate"><span class="pre">UserAssigned</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">principal_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the identity type to be assigned to the scale set. Allowable values are <code class="docutils literal notranslate"><span class="pre">SystemAssigned</span></code> and <code class="docutils literal notranslate"><span class="pre">UserAssigned</span></code>. For the <code class="docutils literal notranslate"><span class="pre">SystemAssigned</span></code> identity the scale set’s Service Principal ID (SPN) can be retrieved after the scale set has been created. See <a class="reference external" href="https://docs.microsoft.com/en-us/azure/active-directory/managed-service-identity/overview">documentation</a> for more information.</p></li>
</ul>
<p>The <strong>network_profiles</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">acceleratedNetworking</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Specifies whether to enable accelerated networking or not. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">dnsSettings</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A dns_settings block as documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">dns_servers</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Specifies an array of dns servers.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">ip_configurations</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - An ip_configuration block as documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">applicationGatewayBackendAddressPoolIds</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Specifies an array of references to backend address pools of application gateways. A scale set can reference backend address pools of multiple application gateways. Multiple scale sets can use the same application gateway.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">applicationSecurityGroupIds</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Specifies up to <code class="docutils literal notranslate"><span class="pre">20</span></code> application security group IDs.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">loadBalancerBackendAddressPoolIds</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Specifies an array of references to backend address pools of load balancers. A scale set can reference backend address pools of one public and one internal load balancer. Multiple scale sets cannot use the same load balancer.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">loadBalancerInboundNatRulesIds</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Specifies an array of references to inbound NAT pools for load balancers. A scale set can reference inbound nat pools of one public and one internal load balancer. Multiple scale sets cannot use the same load balancer.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies name of the IP configuration.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">primary</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Specifies if this ip_configuration is the primary one.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">publicIpAddressConfiguration</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Describes a virtual machines scale set IP Configuration’s PublicIPAddress configuration. The public_ip_address_configuration is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">domain_name_label</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The domain name label for the dns settings.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">idleTimeout</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The idle timeout in minutes. This value must be between 4 and 30.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the public ip address configuration</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnet_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the identifier of the subnet.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">ipForwarding</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Whether IP forwarding is enabled on this NIC. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the name of the network interface configuration.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">network_security_group_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the identifier for the network security group.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">primary</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Indicates whether network interfaces created from the network interface configuration will be the primary NIC of the VM.</p></li>
</ul>
<p>The <strong>os_profile</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">admin_password</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the administrator password to use for all the instances of virtual machines in a scale set.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">admin_username</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the administrator account name to use for all the instances of virtual machines in the scale set.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">computer_name_prefix</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the computer name prefix for all of the virtual machines in the scale set. Computer name prefixes must be 1 to 9 characters long for windows images and 1 - 58 for linux. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">custom_data</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies custom data to supply to the machine. On linux-based systems, this can be used as a cloud-init script. On other systems, this will be copied as a file on disk. Internally, this provider will base64 encode this value before sending it to the API. The maximum length of the binary array is 65535 bytes.</p></li>
</ul>
<p>The <strong>os_profile_linux_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">disable_password_authentication</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Specifies whether password authentication should be disabled. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sshKeys</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Specifies a collection of <code class="docutils literal notranslate"><span class="pre">path</span></code> and <code class="docutils literal notranslate"><span class="pre">key_data</span></code> to be placed on the virtual machine.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">keyData</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">path</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
</ul>
<p>The <strong>os_profile_secrets</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">sourceVaultId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the key vault to use.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">vaultCertificates</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A collection of Vault Certificates as documented below</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">certificateStore</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the certificate store on the Virtual Machine where the certificate should be added to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">certificateUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - It is the Base64 encoding of a JSON Object that which is encoded in UTF-8 of which the contents need to be <code class="docutils literal notranslate"><span class="pre">data</span></code>, <code class="docutils literal notranslate"><span class="pre">dataType</span></code> and <code class="docutils literal notranslate"><span class="pre">password</span></code>.</p></li>
</ul>
</li>
</ul>
<p>The <strong>os_profile_windows_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">additionalUnattendConfigs</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - An Additional Unattended Config block as documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">component</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the name of the component to configure with the added content. The only allowable value is <code class="docutils literal notranslate"><span class="pre">Microsoft-Windows-Shell-Setup</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">content</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the base-64 encoded XML formatted content that is added to the unattend.xml file for the specified path and component.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">pass</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the name of the pass that the content applies to. The only allowable value is <code class="docutils literal notranslate"><span class="pre">oobeSystem</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">settingName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the name of the setting to which the content applies. Possible values are: <code class="docutils literal notranslate"><span class="pre">FirstLogonCommands</span></code> and <code class="docutils literal notranslate"><span class="pre">AutoLogon</span></code>.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">enableAutomaticUpgrades</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Indicates whether virtual machines in the scale set are enabled for automatic updates.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">provision_vm_agent</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Indicates whether virtual machine agent should be provisioned on the virtual machines in the scale set.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">winrms</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A collection of WinRM configuration blocks as documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">certificateUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies URL of the certificate with which new Virtual Machines is provisioned.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">protocol</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the protocol of listener</p></li>
</ul>
</li>
</ul>
<p>The <strong>plan</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the name of the image from the marketplace.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">product</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the product of the image from the marketplace.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">publisher</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the publisher of the image.</p></li>
</ul>
<p>The <strong>rolling_upgrade_policy</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">maxBatchInstancePercent</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The maximum percent of total virtual machine instances that will be upgraded simultaneously by the rolling upgrade in one batch. As this is a maximum, unhealthy instances in previous or future batches can cause the percentage of instances in a batch to decrease to ensure higher reliability. Defaults to <code class="docutils literal notranslate"><span class="pre">20</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxUnhealthyInstancePercent</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The maximum percentage of the total virtual machine instances in the scale set that can be simultaneously unhealthy, either as a result of being upgraded, or by being found in an unhealthy state by the virtual machine health checks before the rolling upgrade aborts. This constraint will be checked prior to starting any batch. Defaults to <code class="docutils literal notranslate"><span class="pre">20</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxUnhealthyUpgradedInstancePercent</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The maximum percentage of upgraded virtual machine instances that can be found to be in an unhealthy state. This check will happen after each batch is upgraded. If this percentage is ever exceeded, the rolling update aborts. Defaults to <code class="docutils literal notranslate"><span class="pre">20</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">pauseTimeBetweenBatches</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The wait time between completing the update for all virtual machines in one batch and starting the next batch. The time duration should be specified in ISO 8601 format for duration (<a class="reference external" href="https://en.wikipedia.org/wiki/ISO_8601#Durations">https://en.wikipedia.org/wiki/ISO_8601#Durations</a>). Defaults to <code class="docutils literal notranslate"><span class="pre">0</span></code> seconds represented as <code class="docutils literal notranslate"><span class="pre">PT0S</span></code>.</p></li>
</ul>
<p>The <strong>sku</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">capacity</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Specifies the number of virtual machines in the scale set.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the size of virtual machines in a scale set.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tier</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the tier of virtual machines in a scale set. Possible values, <code class="docutils literal notranslate"><span class="pre">standard</span></code> or <code class="docutils literal notranslate"><span class="pre">basic</span></code>.</p></li>
</ul>
<p>The <strong>storage_profile_data_disks</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">caching</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the caching requirements. Possible values include: <code class="docutils literal notranslate"><span class="pre">None</span></code> (default), <code class="docutils literal notranslate"><span class="pre">ReadOnly</span></code>, <code class="docutils literal notranslate"><span class="pre">ReadWrite</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">create_option</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies how the data disk should be created. The only possible options are <code class="docutils literal notranslate"><span class="pre">FromImage</span></code> and <code class="docutils literal notranslate"><span class="pre">Empty</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">disk_size_gb</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Specifies the size of the disk in GB. This element is required when creating an empty disk.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">lun</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Specifies the Logical Unit Number of the disk in each virtual machine in the scale set.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">managedDiskType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the type of managed disk to create. Value must be either <code class="docutils literal notranslate"><span class="pre">Standard_LRS</span></code>, <code class="docutils literal notranslate"><span class="pre">StandardSSD_LRS</span></code> or <code class="docutils literal notranslate"><span class="pre">Premium_LRS</span></code>.</p></li>
</ul>
<p>The <strong>storage_profile_image_reference</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the ID of the (custom) image to use to create the virtual
machine scale set, as in the example below.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">offer</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the offer of the image used to create the virtual machines.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">publisher</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the publisher of the image used to create the virtual machines.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sku</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the SKU of the image used to create the virtual machines.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">version</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the version of the image used to create the virtual machines.</p></li>
</ul>
<p>The <strong>storage_profile_os_disk</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">caching</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the caching requirements. Possible values include: <code class="docutils literal notranslate"><span class="pre">None</span></code> (default), <code class="docutils literal notranslate"><span class="pre">ReadOnly</span></code>, <code class="docutils literal notranslate"><span class="pre">ReadWrite</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">create_option</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies how the virtual machine should be created. The only possible option is <code class="docutils literal notranslate"><span class="pre">FromImage</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">image</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the blob uri for user image. A virtual machine scale set creates an os disk in the same container as the user image.
Updating the osDisk image causes the existing disk to be deleted and a new one created with the new image. If the VM scale set is in Manual upgrade mode then the virtual machines are not updated until they have manualUpgrade applied to them.
When setting this field <code class="docutils literal notranslate"><span class="pre">os_type</span></code> needs to be specified. Cannot be used when <code class="docutils literal notranslate"><span class="pre">vhd_containers</span></code>, <code class="docutils literal notranslate"><span class="pre">managed_disk_type</span></code> or <code class="docutils literal notranslate"><span class="pre">storage_profile_image_reference</span></code> are specified.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">managedDiskType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the type of managed disk to create. Value you must be either <code class="docutils literal notranslate"><span class="pre">Standard_LRS</span></code>, <code class="docutils literal notranslate"><span class="pre">StandardSSD_LRS</span></code> or <code class="docutils literal notranslate"><span class="pre">Premium_LRS</span></code>. Cannot be used when <code class="docutils literal notranslate"><span class="pre">vhd_containers</span></code> or <code class="docutils literal notranslate"><span class="pre">image</span></code> is specified.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the disk name. Must be specified when using unmanaged disk (‘managed_disk_type’ property not set).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">os_type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the operating system Type, valid values are windows, linux.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">vhdContainers</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Specifies the vhd uri. Cannot be used when <code class="docutils literal notranslate"><span class="pre">image</span></code> or <code class="docutils literal notranslate"><span class="pre">managed_disk_type</span></code> is specified.</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_azure.compute.ScaleSet.automatic_os_upgrade">
<code class="sig-name descname">automatic_os_upgrade</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.ScaleSet.automatic_os_upgrade" title="Permalink to this definition">¶</a></dt>
<dd><p>Automatic OS patches can be applied by Azure to your scaleset. This is particularly useful when <code class="docutils literal notranslate"><span class="pre">upgrade_policy_mode</span></code> is set to <code class="docutils literal notranslate"><span class="pre">Rolling</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.ScaleSet.boot_diagnostics">
<code class="sig-name descname">boot_diagnostics</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.ScaleSet.boot_diagnostics" title="Permalink to this definition">¶</a></dt>
<dd><p>A boot diagnostics profile block as referenced below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">storageUri</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
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
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">auto_upgrade_minor_version</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Specifies whether or not to use the latest minor version available.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the name of the extension.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">protected_settings</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The protected_settings passed to the extension, like settings, these are specified as a JSON object in a string.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">provision_after_extensions</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - Specifies a dependency array of extensions required to be executed before, the array stores the name of each extension.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">publisher</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The publisher of the extension, available publishers can be found by using the Azure CLI.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">settings</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The settings passed to the extension, these are specified as a JSON object in a string.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The type of extension, available types for a publisher can be found using the Azure CLI.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type_handler_version</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the version of the extension to use, available versions can be found using the Azure CLI.</p></li>
</ul>
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
<dd><p>Specifies the name of the virtual machine scale set resource. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.ScaleSet.network_profiles">
<code class="sig-name descname">network_profiles</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.ScaleSet.network_profiles" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of network profile block as documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">acceleratedNetworking</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Specifies whether to enable accelerated networking or not. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">dnsSettings</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - A dns_settings block as documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">dns_servers</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - Specifies an array of dns servers.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">ip_configurations</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - An ip_configuration block as documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">applicationGatewayBackendAddressPoolIds</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - Specifies an array of references to backend address pools of application gateways. A scale set can reference backend address pools of multiple application gateways. Multiple scale sets can use the same application gateway.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">applicationSecurityGroupIds</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - Specifies up to <code class="docutils literal notranslate"><span class="pre">20</span></code> application security group IDs.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">loadBalancerBackendAddressPoolIds</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - Specifies an array of references to backend address pools of load balancers. A scale set can reference backend address pools of one public and one internal load balancer. Multiple scale sets cannot use the same load balancer.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">loadBalancerInboundNatRulesIds</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - Specifies an array of references to inbound NAT pools for load balancers. A scale set can reference inbound nat pools of one public and one internal load balancer. Multiple scale sets cannot use the same load balancer.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies name of the IP configuration.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">primary</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Specifies if this ip_configuration is the primary one.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">publicIpAddressConfiguration</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - Describes a virtual machines scale set IP Configuration’s PublicIPAddress configuration. The public_ip_address_configuration is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">domain_name_label</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The domain name label for the dns settings.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">idleTimeout</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The idle timeout in minutes. This value must be between 4 and 30.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the public ip address configuration</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnet_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the identifier of the subnet.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">ipForwarding</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Whether IP forwarding is enabled on this NIC. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the name of the network interface configuration.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">network_security_group_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the identifier for the network security group.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">primary</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Indicates whether network interfaces created from the network interface configuration will be the primary NIC of the VM.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.ScaleSet.os_profile">
<code class="sig-name descname">os_profile</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.ScaleSet.os_profile" title="Permalink to this definition">¶</a></dt>
<dd><p>A Virtual Machine OS Profile block as documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">admin_password</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the administrator password to use for all the instances of virtual machines in a scale set.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">admin_username</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the administrator account name to use for all the instances of virtual machines in the scale set.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">computer_name_prefix</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the computer name prefix for all of the virtual machines in the scale set. Computer name prefixes must be 1 to 9 characters long for windows images and 1 - 58 for linux. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">custom_data</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies custom data to supply to the machine. On linux-based systems, this can be used as a cloud-init script. On other systems, this will be copied as a file on disk. Internally, this provider will base64 encode this value before sending it to the API. The maximum length of the binary array is 65535 bytes.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.ScaleSet.os_profile_linux_config">
<code class="sig-name descname">os_profile_linux_config</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.ScaleSet.os_profile_linux_config" title="Permalink to this definition">¶</a></dt>
<dd><p>A Linux config block as documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">disable_password_authentication</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Specifies whether password authentication should be disabled. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sshKeys</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - Specifies a collection of <code class="docutils literal notranslate"><span class="pre">path</span></code> and <code class="docutils literal notranslate"><span class="pre">key_data</span></code> to be placed on the virtual machine.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">keyData</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">path</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.ScaleSet.os_profile_secrets">
<code class="sig-name descname">os_profile_secrets</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.ScaleSet.os_profile_secrets" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of Secret blocks as documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">sourceVaultId</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the key vault to use.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">vaultCertificates</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - A collection of Vault Certificates as documented below</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">certificateStore</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the certificate store on the Virtual Machine where the certificate should be added to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">certificateUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - It is the Base64 encoding of a JSON Object that which is encoded in UTF-8 of which the contents need to be <code class="docutils literal notranslate"><span class="pre">data</span></code>, <code class="docutils literal notranslate"><span class="pre">dataType</span></code> and <code class="docutils literal notranslate"><span class="pre">password</span></code>.</p></li>
</ul>
</li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.ScaleSet.os_profile_windows_config">
<code class="sig-name descname">os_profile_windows_config</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.ScaleSet.os_profile_windows_config" title="Permalink to this definition">¶</a></dt>
<dd><p>A Windows config block as documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">additionalUnattendConfigs</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - An Additional Unattended Config block as documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">component</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the name of the component to configure with the added content. The only allowable value is <code class="docutils literal notranslate"><span class="pre">Microsoft-Windows-Shell-Setup</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">content</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the base-64 encoded XML formatted content that is added to the unattend.xml file for the specified path and component.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">pass</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the name of the pass that the content applies to. The only allowable value is <code class="docutils literal notranslate"><span class="pre">oobeSystem</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">settingName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the name of the setting to which the content applies. Possible values are: <code class="docutils literal notranslate"><span class="pre">FirstLogonCommands</span></code> and <code class="docutils literal notranslate"><span class="pre">AutoLogon</span></code>.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">enableAutomaticUpgrades</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Indicates whether virtual machines in the scale set are enabled for automatic updates.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">provision_vm_agent</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Indicates whether virtual machine agent should be provisioned on the virtual machines in the scale set.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">winrms</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - A collection of WinRM configuration blocks as documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">certificateUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies URL of the certificate with which new Virtual Machines is provisioned.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">protocol</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the protocol of listener</p></li>
</ul>
</li>
</ul>
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
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the name of the image from the marketplace.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">product</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the product of the image from the marketplace.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">publisher</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the publisher of the image.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.ScaleSet.priority">
<code class="sig-name descname">priority</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.ScaleSet.priority" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the priority for the Virtual Machines in the Scale Set. Defaults to <code class="docutils literal notranslate"><span class="pre">Regular</span></code>. Possible values are <code class="docutils literal notranslate"><span class="pre">Low</span></code> and <code class="docutils literal notranslate"><span class="pre">Regular</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.ScaleSet.proximity_placement_group_id">
<code class="sig-name descname">proximity_placement_group_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.ScaleSet.proximity_placement_group_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Proximity Placement Group to which this Virtual Machine should be assigned. Changing this forces a new resource to be created</p>
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
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">maxBatchInstancePercent</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The maximum percent of total virtual machine instances that will be upgraded simultaneously by the rolling upgrade in one batch. As this is a maximum, unhealthy instances in previous or future batches can cause the percentage of instances in a batch to decrease to ensure higher reliability. Defaults to <code class="docutils literal notranslate"><span class="pre">20</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxUnhealthyInstancePercent</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The maximum percentage of the total virtual machine instances in the scale set that can be simultaneously unhealthy, either as a result of being upgraded, or by being found in an unhealthy state by the virtual machine health checks before the rolling upgrade aborts. This constraint will be checked prior to starting any batch. Defaults to <code class="docutils literal notranslate"><span class="pre">20</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxUnhealthyUpgradedInstancePercent</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The maximum percentage of upgraded virtual machine instances that can be found to be in an unhealthy state. This check will happen after each batch is upgraded. If this percentage is ever exceeded, the rolling update aborts. Defaults to <code class="docutils literal notranslate"><span class="pre">20</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">pauseTimeBetweenBatches</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The wait time between completing the update for all virtual machines in one batch and starting the next batch. The time duration should be specified in ISO 8601 format for duration (<a class="reference external" href="https://en.wikipedia.org/wiki/ISO_8601#Durations">https://en.wikipedia.org/wiki/ISO_8601#Durations</a>). Defaults to <code class="docutils literal notranslate"><span class="pre">0</span></code> seconds represented as <code class="docutils literal notranslate"><span class="pre">PT0S</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.ScaleSet.single_placement_group">
<code class="sig-name descname">single_placement_group</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.ScaleSet.single_placement_group" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies whether the scale set is limited to a single placement group with a maximum size of 100 virtual machines. If set to false, managed disks must be used. Default is true. Changing this forces a new resource to be created. See <a class="reference external" href="http://docs.microsoft.com/en-us/azure/virtual-machine-scale-sets/virtual-machine-scale-sets-placement-groups">documentation</a> for more information.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.ScaleSet.sku">
<code class="sig-name descname">sku</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.ScaleSet.sku" title="Permalink to this definition">¶</a></dt>
<dd><p>A sku block as documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">capacity</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Specifies the number of virtual machines in the scale set.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the size of virtual machines in a scale set.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tier</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the tier of virtual machines in a scale set. Possible values, <code class="docutils literal notranslate"><span class="pre">standard</span></code> or <code class="docutils literal notranslate"><span class="pre">basic</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.ScaleSet.storage_profile_data_disks">
<code class="sig-name descname">storage_profile_data_disks</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.ScaleSet.storage_profile_data_disks" title="Permalink to this definition">¶</a></dt>
<dd><p>A storage profile data disk block as documented below</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">caching</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the caching requirements. Possible values include: <code class="docutils literal notranslate"><span class="pre">None</span></code> (default), <code class="docutils literal notranslate"><span class="pre">ReadOnly</span></code>, <code class="docutils literal notranslate"><span class="pre">ReadWrite</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">create_option</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies how the data disk should be created. The only possible options are <code class="docutils literal notranslate"><span class="pre">FromImage</span></code> and <code class="docutils literal notranslate"><span class="pre">Empty</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">disk_size_gb</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Specifies the size of the disk in GB. This element is required when creating an empty disk.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">lun</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Specifies the Logical Unit Number of the disk in each virtual machine in the scale set.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">managedDiskType</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the type of managed disk to create. Value must be either <code class="docutils literal notranslate"><span class="pre">Standard_LRS</span></code>, <code class="docutils literal notranslate"><span class="pre">StandardSSD_LRS</span></code> or <code class="docutils literal notranslate"><span class="pre">Premium_LRS</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.ScaleSet.storage_profile_image_reference">
<code class="sig-name descname">storage_profile_image_reference</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.ScaleSet.storage_profile_image_reference" title="Permalink to this definition">¶</a></dt>
<dd><p>A storage profile image reference block as documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the ID of the (custom) image to use to create the virtual
machine scale set, as in the example below.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">offer</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the offer of the image used to create the virtual machines.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">publisher</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the publisher of the image used to create the virtual machines.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sku</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the SKU of the image used to create the virtual machines.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">version</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the version of the image used to create the virtual machines.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.ScaleSet.storage_profile_os_disk">
<code class="sig-name descname">storage_profile_os_disk</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.ScaleSet.storage_profile_os_disk" title="Permalink to this definition">¶</a></dt>
<dd><p>A storage profile os disk block as documented below</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">caching</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the caching requirements. Possible values include: <code class="docutils literal notranslate"><span class="pre">None</span></code> (default), <code class="docutils literal notranslate"><span class="pre">ReadOnly</span></code>, <code class="docutils literal notranslate"><span class="pre">ReadWrite</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">create_option</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies how the virtual machine should be created. The only possible option is <code class="docutils literal notranslate"><span class="pre">FromImage</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">image</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the blob uri for user image. A virtual machine scale set creates an os disk in the same container as the user image.
Updating the osDisk image causes the existing disk to be deleted and a new one created with the new image. If the VM scale set is in Manual upgrade mode then the virtual machines are not updated until they have manualUpgrade applied to them.
When setting this field <code class="docutils literal notranslate"><span class="pre">os_type</span></code> needs to be specified. Cannot be used when <code class="docutils literal notranslate"><span class="pre">vhd_containers</span></code>, <code class="docutils literal notranslate"><span class="pre">managed_disk_type</span></code> or <code class="docutils literal notranslate"><span class="pre">storage_profile_image_reference</span></code> are specified.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">managedDiskType</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the type of managed disk to create. Value you must be either <code class="docutils literal notranslate"><span class="pre">Standard_LRS</span></code>, <code class="docutils literal notranslate"><span class="pre">StandardSSD_LRS</span></code> or <code class="docutils literal notranslate"><span class="pre">Premium_LRS</span></code>. Cannot be used when <code class="docutils literal notranslate"><span class="pre">vhd_containers</span></code> or <code class="docutils literal notranslate"><span class="pre">image</span></code> is specified.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the disk name. Must be specified when using unmanaged disk (‘managed_disk_type’ property not set).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">os_type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the operating system Type, valid values are windows, linux.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">vhdContainers</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - Specifies the vhd uri. Cannot be used when <code class="docutils literal notranslate"><span class="pre">image</span></code> or <code class="docutils literal notranslate"><span class="pre">managed_disk_type</span></code> is specified.</p></li>
</ul>
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
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">automatic_os_upgrade=None</em>, <em class="sig-param">boot_diagnostics=None</em>, <em class="sig-param">eviction_policy=None</em>, <em class="sig-param">extensions=None</em>, <em class="sig-param">health_probe_id=None</em>, <em class="sig-param">identity=None</em>, <em class="sig-param">license_type=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">network_profiles=None</em>, <em class="sig-param">os_profile=None</em>, <em class="sig-param">os_profile_linux_config=None</em>, <em class="sig-param">os_profile_secrets=None</em>, <em class="sig-param">os_profile_windows_config=None</em>, <em class="sig-param">overprovision=None</em>, <em class="sig-param">plan=None</em>, <em class="sig-param">priority=None</em>, <em class="sig-param">proximity_placement_group_id=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">rolling_upgrade_policy=None</em>, <em class="sig-param">single_placement_group=None</em>, <em class="sig-param">sku=None</em>, <em class="sig-param">storage_profile_data_disks=None</em>, <em class="sig-param">storage_profile_image_reference=None</em>, <em class="sig-param">storage_profile_os_disk=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">upgrade_policy_mode=None</em>, <em class="sig-param">zones=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.compute.ScaleSet.get" title="Permalink to this definition">¶</a></dt>
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
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the virtual machine scale set resource. Changing this forces a new resource to be created.</p></li>
<li><p><strong>network_profiles</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A collection of network profile block as documented below.</p></li>
<li><p><strong>os_profile</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A Virtual Machine OS Profile block as documented below.</p></li>
<li><p><strong>os_profile_linux_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A Linux config block as documented below.</p></li>
<li><p><strong>os_profile_secrets</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A collection of Secret blocks as documented below.</p></li>
<li><p><strong>os_profile_windows_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A Windows config block as documented below.</p></li>
<li><p><strong>overprovision</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specifies whether the virtual machine scale set should be overprovisioned.</p></li>
<li><p><strong>plan</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A plan block as documented below.</p></li>
<li><p><strong>priority</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the priority for the Virtual Machines in the Scale Set. Defaults to <code class="docutils literal notranslate"><span class="pre">Regular</span></code>. Possible values are <code class="docutils literal notranslate"><span class="pre">Low</span></code> and <code class="docutils literal notranslate"><span class="pre">Regular</span></code>.</p></li>
<li><p><strong>proximity_placement_group_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Proximity Placement Group to which this Virtual Machine should be assigned. Changing this forces a new resource to be created</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the virtual machine scale set. Changing this forces a new resource to be created.</p></li>
<li><p><strong>rolling_upgrade_policy</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">rolling_upgrade_policy</span></code> block as defined below. This is only applicable when the <code class="docutils literal notranslate"><span class="pre">upgrade_policy_mode</span></code> is <code class="docutils literal notranslate"><span class="pre">Rolling</span></code>.</p></li>
<li><p><strong>single_placement_group</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – <p>Specifies whether the scale set is limited to a single placement group with a maximum size of 100 virtual machines. If set to false, managed disks must be used. Default is true. Changing this forces a new resource to be created. See <a class="reference external" href="http://docs.microsoft.com/en-us/azure/virtual-machine-scale-sets/virtual-machine-scale-sets-placement-groups">documentation</a> for more information.</p>
</p></li>
<li><p><strong>sku</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A sku block as documented below.</p></li>
<li><p><strong>storage_profile_data_disks</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A storage profile data disk block as documented below</p></li>
<li><p><strong>storage_profile_image_reference</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A storage profile image reference block as documented below.</p></li>
<li><p><strong>storage_profile_os_disk</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A storage profile os disk block as documented below</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
<li><p><strong>upgrade_policy_mode</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the mode of an upgrade to virtual machines in the scale set. Possible values, <code class="docutils literal notranslate"><span class="pre">Rolling</span></code>, <code class="docutils literal notranslate"><span class="pre">Manual</span></code>, or <code class="docutils literal notranslate"><span class="pre">Automatic</span></code>. When choosing <code class="docutils literal notranslate"><span class="pre">Rolling</span></code>, you will need to set a health probe.</p></li>
<li><p><strong>zones</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A collection of availability zones to spread the Virtual Machines over.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>boot_diagnostics</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">storageUri</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>extensions</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">auto_upgrade_minor_version</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Specifies whether or not to use the latest minor version available.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the name of the extension.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">protected_settings</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The protected_settings passed to the extension, like settings, these are specified as a JSON object in a string.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">provision_after_extensions</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Specifies a dependency array of extensions required to be executed before, the array stores the name of each extension.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">publisher</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The publisher of the extension, available publishers can be found by using the Azure CLI.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">settings</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The settings passed to the extension, these are specified as a JSON object in a string.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The type of extension, available types for a publisher can be found using the Azure CLI.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type_handler_version</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the version of the extension to use, available versions can be found using the Azure CLI.</p></li>
</ul>
<p>The <strong>identity</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">identityIds</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Specifies a list of user managed identity ids to be assigned to the VMSS. Required if <code class="docutils literal notranslate"><span class="pre">type</span></code> is <code class="docutils literal notranslate"><span class="pre">UserAssigned</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">principal_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the identity type to be assigned to the scale set. Allowable values are <code class="docutils literal notranslate"><span class="pre">SystemAssigned</span></code> and <code class="docutils literal notranslate"><span class="pre">UserAssigned</span></code>. For the <code class="docutils literal notranslate"><span class="pre">SystemAssigned</span></code> identity the scale set’s Service Principal ID (SPN) can be retrieved after the scale set has been created. See <a class="reference external" href="https://docs.microsoft.com/en-us/azure/active-directory/managed-service-identity/overview">documentation</a> for more information.</p></li>
</ul>
<p>The <strong>network_profiles</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">acceleratedNetworking</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Specifies whether to enable accelerated networking or not. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">dnsSettings</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A dns_settings block as documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">dns_servers</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Specifies an array of dns servers.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">ip_configurations</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - An ip_configuration block as documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">applicationGatewayBackendAddressPoolIds</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Specifies an array of references to backend address pools of application gateways. A scale set can reference backend address pools of multiple application gateways. Multiple scale sets can use the same application gateway.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">applicationSecurityGroupIds</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Specifies up to <code class="docutils literal notranslate"><span class="pre">20</span></code> application security group IDs.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">loadBalancerBackendAddressPoolIds</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Specifies an array of references to backend address pools of load balancers. A scale set can reference backend address pools of one public and one internal load balancer. Multiple scale sets cannot use the same load balancer.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">loadBalancerInboundNatRulesIds</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Specifies an array of references to inbound NAT pools for load balancers. A scale set can reference inbound nat pools of one public and one internal load balancer. Multiple scale sets cannot use the same load balancer.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies name of the IP configuration.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">primary</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Specifies if this ip_configuration is the primary one.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">publicIpAddressConfiguration</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Describes a virtual machines scale set IP Configuration’s PublicIPAddress configuration. The public_ip_address_configuration is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">domain_name_label</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The domain name label for the dns settings.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">idleTimeout</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The idle timeout in minutes. This value must be between 4 and 30.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the public ip address configuration</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnet_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the identifier of the subnet.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">ipForwarding</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Whether IP forwarding is enabled on this NIC. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the name of the network interface configuration.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">network_security_group_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the identifier for the network security group.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">primary</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Indicates whether network interfaces created from the network interface configuration will be the primary NIC of the VM.</p></li>
</ul>
<p>The <strong>os_profile</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">admin_password</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the administrator password to use for all the instances of virtual machines in a scale set.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">admin_username</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the administrator account name to use for all the instances of virtual machines in the scale set.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">computer_name_prefix</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the computer name prefix for all of the virtual machines in the scale set. Computer name prefixes must be 1 to 9 characters long for windows images and 1 - 58 for linux. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">custom_data</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies custom data to supply to the machine. On linux-based systems, this can be used as a cloud-init script. On other systems, this will be copied as a file on disk. Internally, this provider will base64 encode this value before sending it to the API. The maximum length of the binary array is 65535 bytes.</p></li>
</ul>
<p>The <strong>os_profile_linux_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">disable_password_authentication</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Specifies whether password authentication should be disabled. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sshKeys</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Specifies a collection of <code class="docutils literal notranslate"><span class="pre">path</span></code> and <code class="docutils literal notranslate"><span class="pre">key_data</span></code> to be placed on the virtual machine.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">keyData</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">path</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
</ul>
<p>The <strong>os_profile_secrets</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">sourceVaultId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the key vault to use.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">vaultCertificates</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A collection of Vault Certificates as documented below</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">certificateStore</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the certificate store on the Virtual Machine where the certificate should be added to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">certificateUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - It is the Base64 encoding of a JSON Object that which is encoded in UTF-8 of which the contents need to be <code class="docutils literal notranslate"><span class="pre">data</span></code>, <code class="docutils literal notranslate"><span class="pre">dataType</span></code> and <code class="docutils literal notranslate"><span class="pre">password</span></code>.</p></li>
</ul>
</li>
</ul>
<p>The <strong>os_profile_windows_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">additionalUnattendConfigs</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - An Additional Unattended Config block as documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">component</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the name of the component to configure with the added content. The only allowable value is <code class="docutils literal notranslate"><span class="pre">Microsoft-Windows-Shell-Setup</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">content</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the base-64 encoded XML formatted content that is added to the unattend.xml file for the specified path and component.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">pass</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the name of the pass that the content applies to. The only allowable value is <code class="docutils literal notranslate"><span class="pre">oobeSystem</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">settingName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the name of the setting to which the content applies. Possible values are: <code class="docutils literal notranslate"><span class="pre">FirstLogonCommands</span></code> and <code class="docutils literal notranslate"><span class="pre">AutoLogon</span></code>.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">enableAutomaticUpgrades</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Indicates whether virtual machines in the scale set are enabled for automatic updates.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">provision_vm_agent</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Indicates whether virtual machine agent should be provisioned on the virtual machines in the scale set.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">winrms</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A collection of WinRM configuration blocks as documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">certificateUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies URL of the certificate with which new Virtual Machines is provisioned.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">protocol</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the protocol of listener</p></li>
</ul>
</li>
</ul>
<p>The <strong>plan</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the name of the image from the marketplace.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">product</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the product of the image from the marketplace.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">publisher</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the publisher of the image.</p></li>
</ul>
<p>The <strong>rolling_upgrade_policy</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">maxBatchInstancePercent</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The maximum percent of total virtual machine instances that will be upgraded simultaneously by the rolling upgrade in one batch. As this is a maximum, unhealthy instances in previous or future batches can cause the percentage of instances in a batch to decrease to ensure higher reliability. Defaults to <code class="docutils literal notranslate"><span class="pre">20</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxUnhealthyInstancePercent</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The maximum percentage of the total virtual machine instances in the scale set that can be simultaneously unhealthy, either as a result of being upgraded, or by being found in an unhealthy state by the virtual machine health checks before the rolling upgrade aborts. This constraint will be checked prior to starting any batch. Defaults to <code class="docutils literal notranslate"><span class="pre">20</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxUnhealthyUpgradedInstancePercent</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The maximum percentage of upgraded virtual machine instances that can be found to be in an unhealthy state. This check will happen after each batch is upgraded. If this percentage is ever exceeded, the rolling update aborts. Defaults to <code class="docutils literal notranslate"><span class="pre">20</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">pauseTimeBetweenBatches</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The wait time between completing the update for all virtual machines in one batch and starting the next batch. The time duration should be specified in ISO 8601 format for duration (<a class="reference external" href="https://en.wikipedia.org/wiki/ISO_8601#Durations">https://en.wikipedia.org/wiki/ISO_8601#Durations</a>). Defaults to <code class="docutils literal notranslate"><span class="pre">0</span></code> seconds represented as <code class="docutils literal notranslate"><span class="pre">PT0S</span></code>.</p></li>
</ul>
<p>The <strong>sku</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">capacity</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Specifies the number of virtual machines in the scale set.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the size of virtual machines in a scale set.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tier</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the tier of virtual machines in a scale set. Possible values, <code class="docutils literal notranslate"><span class="pre">standard</span></code> or <code class="docutils literal notranslate"><span class="pre">basic</span></code>.</p></li>
</ul>
<p>The <strong>storage_profile_data_disks</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">caching</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the caching requirements. Possible values include: <code class="docutils literal notranslate"><span class="pre">None</span></code> (default), <code class="docutils literal notranslate"><span class="pre">ReadOnly</span></code>, <code class="docutils literal notranslate"><span class="pre">ReadWrite</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">create_option</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies how the data disk should be created. The only possible options are <code class="docutils literal notranslate"><span class="pre">FromImage</span></code> and <code class="docutils literal notranslate"><span class="pre">Empty</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">disk_size_gb</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Specifies the size of the disk in GB. This element is required when creating an empty disk.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">lun</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Specifies the Logical Unit Number of the disk in each virtual machine in the scale set.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">managedDiskType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the type of managed disk to create. Value must be either <code class="docutils literal notranslate"><span class="pre">Standard_LRS</span></code>, <code class="docutils literal notranslate"><span class="pre">StandardSSD_LRS</span></code> or <code class="docutils literal notranslate"><span class="pre">Premium_LRS</span></code>.</p></li>
</ul>
<p>The <strong>storage_profile_image_reference</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the ID of the (custom) image to use to create the virtual
machine scale set, as in the example below.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">offer</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the offer of the image used to create the virtual machines.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">publisher</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the publisher of the image used to create the virtual machines.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sku</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the SKU of the image used to create the virtual machines.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">version</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the version of the image used to create the virtual machines.</p></li>
</ul>
<p>The <strong>storage_profile_os_disk</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">caching</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the caching requirements. Possible values include: <code class="docutils literal notranslate"><span class="pre">None</span></code> (default), <code class="docutils literal notranslate"><span class="pre">ReadOnly</span></code>, <code class="docutils literal notranslate"><span class="pre">ReadWrite</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">create_option</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies how the virtual machine should be created. The only possible option is <code class="docutils literal notranslate"><span class="pre">FromImage</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">image</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the blob uri for user image. A virtual machine scale set creates an os disk in the same container as the user image.
Updating the osDisk image causes the existing disk to be deleted and a new one created with the new image. If the VM scale set is in Manual upgrade mode then the virtual machines are not updated until they have manualUpgrade applied to them.
When setting this field <code class="docutils literal notranslate"><span class="pre">os_type</span></code> needs to be specified. Cannot be used when <code class="docutils literal notranslate"><span class="pre">vhd_containers</span></code>, <code class="docutils literal notranslate"><span class="pre">managed_disk_type</span></code> or <code class="docutils literal notranslate"><span class="pre">storage_profile_image_reference</span></code> are specified.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">managedDiskType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the type of managed disk to create. Value you must be either <code class="docutils literal notranslate"><span class="pre">Standard_LRS</span></code>, <code class="docutils literal notranslate"><span class="pre">StandardSSD_LRS</span></code> or <code class="docutils literal notranslate"><span class="pre">Premium_LRS</span></code>. Cannot be used when <code class="docutils literal notranslate"><span class="pre">vhd_containers</span></code> or <code class="docutils literal notranslate"><span class="pre">image</span></code> is specified.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the disk name. Must be specified when using unmanaged disk (‘managed_disk_type’ property not set).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">os_type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the operating system Type, valid values are windows, linux.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">vhdContainers</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Specifies the vhd uri. Cannot be used when <code class="docutils literal notranslate"><span class="pre">image</span></code> or <code class="docutils literal notranslate"><span class="pre">managed_disk_type</span></code> is specified.</p></li>
</ul>
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
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.compute.</code><code class="sig-name descname">SharedImage</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">eula=None</em>, <em class="sig-param">gallery_name=None</em>, <em class="sig-param">hyper_v_generation=None</em>, <em class="sig-param">identifier=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">os_type=None</em>, <em class="sig-param">privacy_statement_uri=None</em>, <em class="sig-param">release_note_uri=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.compute.SharedImage" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Shared Image within a Shared Image Gallery.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A description of this Shared Image.</p></li>
<li><p><strong>eula</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The End User Licence Agreement for the Shared Image.</p></li>
<li><p><strong>gallery_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Shared Image Gallery in which this Shared Image should exist. Changing this forces a new resource to be created.</p></li>
<li><p><strong>hyper_v_generation</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The generation of HyperV that the Virtual Machine used to create the Shared Image is based on. Possible values are <code class="docutils literal notranslate"><span class="pre">V1</span></code> and <code class="docutils literal notranslate"><span class="pre">V2</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">V1</span></code>. Changing this forces a new resource to be created.</p></li>
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
<p>The <strong>identifier</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">offer</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Offer Name for this Shared Image.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">publisher</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Publisher Name for this Gallery Image.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sku</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Name of the SKU for this Gallery Image.</p></li>
</ul>
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
<dt id="pulumi_azure.compute.SharedImage.hyper_v_generation">
<code class="sig-name descname">hyper_v_generation</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.SharedImage.hyper_v_generation" title="Permalink to this definition">¶</a></dt>
<dd><p>The generation of HyperV that the Virtual Machine used to create the Shared Image is based on. Possible values are <code class="docutils literal notranslate"><span class="pre">V1</span></code> and <code class="docutils literal notranslate"><span class="pre">V2</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">V1</span></code>. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.SharedImage.identifier">
<code class="sig-name descname">identifier</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.SharedImage.identifier" title="Permalink to this definition">¶</a></dt>
<dd><p>An <code class="docutils literal notranslate"><span class="pre">identifier</span></code> block as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">offer</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Offer Name for this Shared Image.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">publisher</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Publisher Name for this Gallery Image.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sku</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Name of the SKU for this Gallery Image.</p></li>
</ul>
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
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">eula=None</em>, <em class="sig-param">gallery_name=None</em>, <em class="sig-param">hyper_v_generation=None</em>, <em class="sig-param">identifier=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">os_type=None</em>, <em class="sig-param">privacy_statement_uri=None</em>, <em class="sig-param">release_note_uri=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">tags=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.compute.SharedImage.get" title="Permalink to this definition">¶</a></dt>
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
<li><p><strong>hyper_v_generation</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The generation of HyperV that the Virtual Machine used to create the Shared Image is based on. Possible values are <code class="docutils literal notranslate"><span class="pre">V1</span></code> and <code class="docutils literal notranslate"><span class="pre">V2</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">V1</span></code>. Changing this forces a new resource to be created.</p></li>
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
<p>The <strong>identifier</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">offer</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Offer Name for this Shared Image.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">publisher</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Publisher Name for this Gallery Image.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sku</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Name of the SKU for this Gallery Image.</p></li>
</ul>
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
<p>The <strong>target_regions</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Azure Region in which this Image Version should exist.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">regionalReplicaCount</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of replicas of the Image Version to be created per region.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">storage_account_type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The storage account type for the image version, which defaults to <code class="docutils literal notranslate"><span class="pre">Standard_LRS</span></code>. You can store all of your image version replicas in Zone Redundant Storage by specifying <code class="docutils literal notranslate"><span class="pre">Standard_ZRS</span></code>.</p></li>
</ul>
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
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Azure Region in which this Image Version should exist.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">regionalReplicaCount</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The number of replicas of the Image Version to be created per region.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">storage_account_type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The storage account type for the image version, which defaults to <code class="docutils literal notranslate"><span class="pre">Standard_LRS</span></code>. You can store all of your image version replicas in Zone Redundant Storage by specifying <code class="docutils literal notranslate"><span class="pre">Standard_ZRS</span></code>.</p></li>
</ul>
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
<p>The <strong>target_regions</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Azure Region in which this Image Version should exist.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">regionalReplicaCount</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of replicas of the Image Version to be created per region.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">storage_account_type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The storage account type for the image version, which defaults to <code class="docutils literal notranslate"><span class="pre">Standard_LRS</span></code>. You can store all of your image version replicas in Zone Redundant Storage by specifying <code class="docutils literal notranslate"><span class="pre">Standard_ZRS</span></code>.</p></li>
</ul>
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
<p>The <strong>encryption_settings</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">diskEncryptionKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">secretUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sourceVaultId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">keyEncryptionKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">keyUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sourceVaultId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
</ul>
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
<p>The <strong>encryption_settings</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">diskEncryptionKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">secretUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sourceVaultId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">keyEncryptionKey</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">keyUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sourceVaultId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
</ul>
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
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.compute.</code><code class="sig-name descname">VirtualMachine</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">additional_capabilities=None</em>, <em class="sig-param">availability_set_id=None</em>, <em class="sig-param">boot_diagnostics=None</em>, <em class="sig-param">delete_data_disks_on_termination=None</em>, <em class="sig-param">delete_os_disk_on_termination=None</em>, <em class="sig-param">identity=None</em>, <em class="sig-param">license_type=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">network_interface_ids=None</em>, <em class="sig-param">os_profile=None</em>, <em class="sig-param">os_profile_linux_config=None</em>, <em class="sig-param">os_profile_secrets=None</em>, <em class="sig-param">os_profile_windows_config=None</em>, <em class="sig-param">plan=None</em>, <em class="sig-param">primary_network_interface_id=None</em>, <em class="sig-param">proximity_placement_group_id=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">storage_data_disks=None</em>, <em class="sig-param">storage_image_reference=None</em>, <em class="sig-param">storage_os_disk=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">vm_size=None</em>, <em class="sig-param">zones=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.compute.VirtualMachine" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Virtual Machine.</p>
<blockquote>
<div><p><strong>Note:</strong> The <code class="docutils literal notranslate"><span class="pre">compute.VirtualMachine</span></code> resource has been superseded by the <code class="docutils literal notranslate"><span class="pre">compute.LinuxVirtualMachine</span></code> and <code class="docutils literal notranslate"><span class="pre">compute.WindowsVirtualMachine</span></code> resources. The existing <code class="docutils literal notranslate"><span class="pre">compute.VirtualMachine</span></code> resource will continue to be available throughout the 2.x releases however is in a feature-frozen state to maintain compatibility - new functionality will instead be added to the <code class="docutils literal notranslate"><span class="pre">compute.LinuxVirtualMachine</span></code> and <code class="docutils literal notranslate"><span class="pre">compute.WindowsVirtualMachine</span></code> resources.</p>
<p><strong>Note:</strong> Data Disks can be attached either directly on the <code class="docutils literal notranslate"><span class="pre">compute.VirtualMachine</span></code> resource, or using the <code class="docutils literal notranslate"><span class="pre">compute.DataDiskAttachment</span></code> resource - but the two cannot be used together. If both are used against the same Virtual Machine, spurious changes will occur.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>additional_capabilities</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">additional_capabilities</span></code> block.</p></li>
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
<li><p><strong>proximity_placement_group_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Proximity Placement Group to which this Virtual Machine should be assigned. Changing this forces a new resource to be created</p></li>
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
<p>The <strong>additional_capabilities</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">ultraSsdEnabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Should Ultra SSD disk be enabled for this Virtual Machine?</p></li>
</ul>
<p>The <strong>boot_diagnostics</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Should Boot Diagnostics be enabled for this Virtual Machine?</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">storageUri</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Storage Account’s Blob Endpoint which should hold the virtual machine’s diagnostic files.</p></li>
</ul>
<p>The <strong>identity</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">identityIds</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Specifies a list of user managed identity ids to be assigned to the VM. Required if <code class="docutils literal notranslate"><span class="pre">type</span></code> is <code class="docutils literal notranslate"><span class="pre">UserAssigned</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">principal_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Principal ID for the Service Principal associated with the Managed Service Identity of this Virtual Machine.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Managed Service Identity Type of this Virtual Machine. Possible values are <code class="docutils literal notranslate"><span class="pre">SystemAssigned</span></code> (where Azure will generate a Service Principal for you), <code class="docutils literal notranslate"><span class="pre">UserAssigned</span></code> (where you can specify the Service Principal ID’s) to be used by this Virtual Machine using the <code class="docutils literal notranslate"><span class="pre">identity_ids</span></code> field, and <code class="docutils literal notranslate"><span class="pre">SystemAssigned,</span> <span class="pre">UserAssigned</span></code> which assigns both a system managed identity as well as the specified user assigned identities.</p></li>
</ul>
<p>The <strong>os_profile</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">admin_password</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The password associated with the local administrator account.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">admin_username</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the name of the local administrator account.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">computer_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the name of the Virtual Machine.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">custom_data</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies custom data to supply to the machine. On Linux-based systems, this can be used as a cloud-init script. On other systems, this will be copied as a file on disk. Internally, this provider will base64 encode this value before sending it to the API. The maximum length of the binary array is 65535 bytes.</p></li>
</ul>
<p>The <strong>os_profile_linux_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">disable_password_authentication</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Specifies whether password authentication should be disabled. If set to <code class="docutils literal notranslate"><span class="pre">false</span></code>, an <code class="docutils literal notranslate"><span class="pre">admin_password</span></code> must be specified.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sshKeys</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - One or more <code class="docutils literal notranslate"><span class="pre">ssh_keys</span></code> blocks. This field is required if <code class="docutils literal notranslate"><span class="pre">disable_password_authentication</span></code> is set to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">keyData</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Public SSH Key which should be written to the <code class="docutils literal notranslate"><span class="pre">path</span></code> defined above.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">path</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The path of the destination file on the virtual machine</p></li>
</ul>
</li>
</ul>
<p>The <strong>os_profile_secrets</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">sourceVaultId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the ID of the Key Vault to use.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">vaultCertificates</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - One or more <code class="docutils literal notranslate"><span class="pre">vault_certificates</span></code> blocks.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">certificateStore</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the certificate store on the Virtual Machine where the certificate should be added to, such as <code class="docutils literal notranslate"><span class="pre">My</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">certificateUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Key Vault Secret. Stored secret is the Base64 encoding of a JSON Object that which is encoded in UTF-8 of which the contents need to be:</p></li>
</ul>
</li>
</ul>
<p>The <strong>os_profile_windows_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">additionalUnattendConfigs</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">additional_unattend_config</span></code> block.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">component</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the name of the component to configure with the added content. The only allowable value is <code class="docutils literal notranslate"><span class="pre">Microsoft-Windows-Shell-Setup</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">content</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the base-64 encoded XML formatted content that is added to the unattend.xml file for the specified path and component.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">pass</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the name of the pass that the content applies to. The only allowable value is <code class="docutils literal notranslate"><span class="pre">oobeSystem</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">settingName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the name of the setting to which the content applies. Possible values are: <code class="docutils literal notranslate"><span class="pre">FirstLogonCommands</span></code> and <code class="docutils literal notranslate"><span class="pre">AutoLogon</span></code>.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">enableAutomaticUpgrades</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Are automatic updates enabled on this Virtual Machine? Defaults to <code class="docutils literal notranslate"><span class="pre">false.</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">provision_vm_agent</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Should the Azure Virtual Machine Guest Agent be installed on this Virtual Machine? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timezone</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the time zone of the virtual machine, <a class="reference external" href="http://jackstromberg.com/2017/01/list-of-time-zones-consumed-by-azure/">the possible values are defined here</a>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">winrms</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - One or more <code class="docutils literal notranslate"><span class="pre">winrm</span></code> block.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">certificateUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Key Vault Secret which contains the encrypted Certificate which should be installed on the Virtual Machine. This certificate must also be specified in the <code class="docutils literal notranslate"><span class="pre">vault_certificates</span></code> block within the <code class="docutils literal notranslate"><span class="pre">os_profile_secrets</span></code> block.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">protocol</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the protocol of listener. Possible values are <code class="docutils literal notranslate"><span class="pre">HTTP</span></code> or <code class="docutils literal notranslate"><span class="pre">HTTPS</span></code>.</p></li>
</ul>
</li>
</ul>
<p>The <strong>plan</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the name of the image from the marketplace.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">product</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the product of the image from the marketplace.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">publisher</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the publisher of the image.</p></li>
</ul>
<p>The <strong>storage_data_disks</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">caching</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the caching requirements for the Data Disk. Possible values include <code class="docutils literal notranslate"><span class="pre">None</span></code>, <code class="docutils literal notranslate"><span class="pre">ReadOnly</span></code> and <code class="docutils literal notranslate"><span class="pre">ReadWrite</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">create_option</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies how the data disk should be created. Possible values are <code class="docutils literal notranslate"><span class="pre">Attach</span></code>, <code class="docutils literal notranslate"><span class="pre">FromImage</span></code> and <code class="docutils literal notranslate"><span class="pre">Empty</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">disk_size_gb</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Specifies the size of the data disk in gigabytes.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">lun</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Specifies the logical unit number of the data disk. This needs to be unique within all the Data Disks on the Virtual Machine.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">managed_disk_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the ID of an Existing Managed Disk which should be attached to this Virtual Machine. When this field is set <code class="docutils literal notranslate"><span class="pre">create_option</span></code> must be set to <code class="docutils literal notranslate"><span class="pre">Attach</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">managedDiskType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the type of managed disk to create. Possible values are either <code class="docutils literal notranslate"><span class="pre">Standard_LRS</span></code>, <code class="docutils literal notranslate"><span class="pre">StandardSSD_LRS</span></code>, <code class="docutils literal notranslate"><span class="pre">Premium_LRS</span></code> or <code class="docutils literal notranslate"><span class="pre">UltraSSD_LRS</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the Data Disk.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">vhdUri</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the URI of the VHD file backing this Unmanaged Data Disk. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">write_accelerator_enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Specifies if Write Accelerator is enabled on the disk. This can only be enabled on <code class="docutils literal notranslate"><span class="pre">Premium_LRS</span></code> managed disks with no caching and <a class="reference external" href="https://docs.microsoft.com/en-us/azure/virtual-machines/workloads/sap/how-to-enable-write-accelerator">M-Series VMs</a>. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
</ul>
<p>The <strong>storage_image_reference</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the ID of the Custom Image which the Virtual Machine should be created from. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">offer</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the offer of the image used to create the virtual machine. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">publisher</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the publisher of the image used to create the virtual machine. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sku</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the SKU of the image used to create the virtual machine. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">version</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the version of the image used to create the virtual machine. Changing this forces a new resource to be created.</p></li>
</ul>
<p>The <strong>storage_os_disk</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">caching</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the caching requirements for the OS Disk. Possible values include <code class="docutils literal notranslate"><span class="pre">None</span></code>, <code class="docutils literal notranslate"><span class="pre">ReadOnly</span></code> and <code class="docutils literal notranslate"><span class="pre">ReadWrite</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">create_option</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies how the OS Disk should be created. Possible values are <code class="docutils literal notranslate"><span class="pre">Attach</span></code> (managed disks only) and <code class="docutils literal notranslate"><span class="pre">FromImage</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">disk_size_gb</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Specifies the size of the OS Disk in gigabytes.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">imageUri</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the Image URI in the format <code class="docutils literal notranslate"><span class="pre">publisherName:offer:skus:version</span></code>. This field can also specify the <a class="reference external" href="https://azure.microsoft.com/en-us/documentation/articles/virtual-machines-linux-cli-deploy-templates/#create-a-custom-vm-image">VHD uri</a> of a custom VM image to clone. When cloning a Custom (Unmanaged) Disk Image the <code class="docutils literal notranslate"><span class="pre">os_type</span></code> field must be set.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">managed_disk_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the ID of an existing Managed Disk which should be attached as the OS Disk of this Virtual Machine. If this is set then the <code class="docutils literal notranslate"><span class="pre">create_option</span></code> must be set to <code class="docutils literal notranslate"><span class="pre">Attach</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">managedDiskType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the type of Managed Disk which should be created. Possible values are <code class="docutils literal notranslate"><span class="pre">Standard_LRS</span></code>, <code class="docutils literal notranslate"><span class="pre">StandardSSD_LRS</span></code> or <code class="docutils literal notranslate"><span class="pre">Premium_LRS</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the name of the OS Disk.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">os_type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the Operating System on the OS Disk. Possible values are <code class="docutils literal notranslate"><span class="pre">Linux</span></code> and <code class="docutils literal notranslate"><span class="pre">Windows</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">vhdUri</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the URI of the VHD file backing this Unmanaged OS Disk. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">write_accelerator_enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Specifies if Write Accelerator is enabled on the disk. This can only be enabled on <code class="docutils literal notranslate"><span class="pre">Premium_LRS</span></code> managed disks with no caching and <a class="reference external" href="https://docs.microsoft.com/en-us/azure/virtual-machines/workloads/sap/how-to-enable-write-accelerator">M-Series VMs</a>. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_azure.compute.VirtualMachine.additional_capabilities">
<code class="sig-name descname">additional_capabilities</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.VirtualMachine.additional_capabilities" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">additional_capabilities</span></code> block.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">ultraSsdEnabled</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Should Ultra SSD disk be enabled for this Virtual Machine?</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.VirtualMachine.availability_set_id">
<code class="sig-name descname">availability_set_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.VirtualMachine.availability_set_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Availability Set in which the Virtual Machine should exist. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.VirtualMachine.boot_diagnostics">
<code class="sig-name descname">boot_diagnostics</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.VirtualMachine.boot_diagnostics" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">boot_diagnostics</span></code> block.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Should Boot Diagnostics be enabled for this Virtual Machine?</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">storageUri</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Storage Account’s Blob Endpoint which should hold the virtual machine’s diagnostic files.</p></li>
</ul>
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
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">identityIds</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - Specifies a list of user managed identity ids to be assigned to the VM. Required if <code class="docutils literal notranslate"><span class="pre">type</span></code> is <code class="docutils literal notranslate"><span class="pre">UserAssigned</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">principal_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Principal ID for the Service Principal associated with the Managed Service Identity of this Virtual Machine.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Managed Service Identity Type of this Virtual Machine. Possible values are <code class="docutils literal notranslate"><span class="pre">SystemAssigned</span></code> (where Azure will generate a Service Principal for you), <code class="docutils literal notranslate"><span class="pre">UserAssigned</span></code> (where you can specify the Service Principal ID’s) to be used by this Virtual Machine using the <code class="docutils literal notranslate"><span class="pre">identity_ids</span></code> field, and <code class="docutils literal notranslate"><span class="pre">SystemAssigned,</span> <span class="pre">UserAssigned</span></code> which assigns both a system managed identity as well as the specified user assigned identities.</p></li>
</ul>
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
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">admin_password</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The password associated with the local administrator account.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">admin_username</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the name of the local administrator account.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">computer_name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the name of the Virtual Machine.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">custom_data</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies custom data to supply to the machine. On Linux-based systems, this can be used as a cloud-init script. On other systems, this will be copied as a file on disk. Internally, this provider will base64 encode this value before sending it to the API. The maximum length of the binary array is 65535 bytes.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.VirtualMachine.os_profile_linux_config">
<code class="sig-name descname">os_profile_linux_config</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.VirtualMachine.os_profile_linux_config" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">os_profile_linux_config</span></code> block.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">disable_password_authentication</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Specifies whether password authentication should be disabled. If set to <code class="docutils literal notranslate"><span class="pre">false</span></code>, an <code class="docutils literal notranslate"><span class="pre">admin_password</span></code> must be specified.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sshKeys</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - One or more <code class="docutils literal notranslate"><span class="pre">ssh_keys</span></code> blocks. This field is required if <code class="docutils literal notranslate"><span class="pre">disable_password_authentication</span></code> is set to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">keyData</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Public SSH Key which should be written to the <code class="docutils literal notranslate"><span class="pre">path</span></code> defined above.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">path</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The path of the destination file on the virtual machine</p></li>
</ul>
</li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.VirtualMachine.os_profile_secrets">
<code class="sig-name descname">os_profile_secrets</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.VirtualMachine.os_profile_secrets" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more <code class="docutils literal notranslate"><span class="pre">os_profile_secrets</span></code> blocks.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">sourceVaultId</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the ID of the Key Vault to use.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">vaultCertificates</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - One or more <code class="docutils literal notranslate"><span class="pre">vault_certificates</span></code> blocks.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">certificateStore</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the certificate store on the Virtual Machine where the certificate should be added to, such as <code class="docutils literal notranslate"><span class="pre">My</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">certificateUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the Key Vault Secret. Stored secret is the Base64 encoding of a JSON Object that which is encoded in UTF-8 of which the contents need to be:</p></li>
</ul>
</li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.VirtualMachine.os_profile_windows_config">
<code class="sig-name descname">os_profile_windows_config</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.VirtualMachine.os_profile_windows_config" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">os_profile_windows_config</span></code> block.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">additionalUnattendConfigs</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - A <code class="docutils literal notranslate"><span class="pre">additional_unattend_config</span></code> block.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">component</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the name of the component to configure with the added content. The only allowable value is <code class="docutils literal notranslate"><span class="pre">Microsoft-Windows-Shell-Setup</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">content</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the base-64 encoded XML formatted content that is added to the unattend.xml file for the specified path and component.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">pass</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the name of the pass that the content applies to. The only allowable value is <code class="docutils literal notranslate"><span class="pre">oobeSystem</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">settingName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the name of the setting to which the content applies. Possible values are: <code class="docutils literal notranslate"><span class="pre">FirstLogonCommands</span></code> and <code class="docutils literal notranslate"><span class="pre">AutoLogon</span></code>.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">enableAutomaticUpgrades</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Are automatic updates enabled on this Virtual Machine? Defaults to <code class="docutils literal notranslate"><span class="pre">false.</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">provision_vm_agent</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Should the Azure Virtual Machine Guest Agent be installed on this Virtual Machine? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timezone</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the time zone of the virtual machine, <a class="reference external" href="http://jackstromberg.com/2017/01/list-of-time-zones-consumed-by-azure/">the possible values are defined here</a>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">winrms</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - One or more <code class="docutils literal notranslate"><span class="pre">winrm</span></code> block.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">certificateUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the Key Vault Secret which contains the encrypted Certificate which should be installed on the Virtual Machine. This certificate must also be specified in the <code class="docutils literal notranslate"><span class="pre">vault_certificates</span></code> block within the <code class="docutils literal notranslate"><span class="pre">os_profile_secrets</span></code> block.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">protocol</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the protocol of listener. Possible values are <code class="docutils literal notranslate"><span class="pre">HTTP</span></code> or <code class="docutils literal notranslate"><span class="pre">HTTPS</span></code>.</p></li>
</ul>
</li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.VirtualMachine.plan">
<code class="sig-name descname">plan</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.VirtualMachine.plan" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">plan</span></code> block.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the name of the image from the marketplace.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">product</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the product of the image from the marketplace.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">publisher</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the publisher of the image.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.VirtualMachine.primary_network_interface_id">
<code class="sig-name descname">primary_network_interface_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.VirtualMachine.primary_network_interface_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Network Interface (which must be attached to the Virtual Machine) which should be the Primary Network Interface for this Virtual Machine.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.VirtualMachine.proximity_placement_group_id">
<code class="sig-name descname">proximity_placement_group_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.VirtualMachine.proximity_placement_group_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Proximity Placement Group to which this Virtual Machine should be assigned. Changing this forces a new resource to be created</p>
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
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">caching</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the caching requirements for the Data Disk. Possible values include <code class="docutils literal notranslate"><span class="pre">None</span></code>, <code class="docutils literal notranslate"><span class="pre">ReadOnly</span></code> and <code class="docutils literal notranslate"><span class="pre">ReadWrite</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">create_option</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies how the data disk should be created. Possible values are <code class="docutils literal notranslate"><span class="pre">Attach</span></code>, <code class="docutils literal notranslate"><span class="pre">FromImage</span></code> and <code class="docutils literal notranslate"><span class="pre">Empty</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">disk_size_gb</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Specifies the size of the data disk in gigabytes.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">lun</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Specifies the logical unit number of the data disk. This needs to be unique within all the Data Disks on the Virtual Machine.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">managed_disk_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the ID of an Existing Managed Disk which should be attached to this Virtual Machine. When this field is set <code class="docutils literal notranslate"><span class="pre">create_option</span></code> must be set to <code class="docutils literal notranslate"><span class="pre">Attach</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">managedDiskType</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the type of managed disk to create. Possible values are either <code class="docutils literal notranslate"><span class="pre">Standard_LRS</span></code>, <code class="docutils literal notranslate"><span class="pre">StandardSSD_LRS</span></code>, <code class="docutils literal notranslate"><span class="pre">Premium_LRS</span></code> or <code class="docutils literal notranslate"><span class="pre">UltraSSD_LRS</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the Data Disk.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">vhdUri</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the URI of the VHD file backing this Unmanaged Data Disk. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">write_accelerator_enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Specifies if Write Accelerator is enabled on the disk. This can only be enabled on <code class="docutils literal notranslate"><span class="pre">Premium_LRS</span></code> managed disks with no caching and <a class="reference external" href="https://docs.microsoft.com/en-us/azure/virtual-machines/workloads/sap/how-to-enable-write-accelerator">M-Series VMs</a>. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.VirtualMachine.storage_image_reference">
<code class="sig-name descname">storage_image_reference</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.VirtualMachine.storage_image_reference" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">storage_image_reference</span></code> block.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the ID of the Custom Image which the Virtual Machine should be created from. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">offer</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the offer of the image used to create the virtual machine. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">publisher</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the publisher of the image used to create the virtual machine. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sku</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the SKU of the image used to create the virtual machine. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">version</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the version of the image used to create the virtual machine. Changing this forces a new resource to be created.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.VirtualMachine.storage_os_disk">
<code class="sig-name descname">storage_os_disk</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.VirtualMachine.storage_os_disk" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">storage_os_disk</span></code> block.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">caching</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the caching requirements for the OS Disk. Possible values include <code class="docutils literal notranslate"><span class="pre">None</span></code>, <code class="docutils literal notranslate"><span class="pre">ReadOnly</span></code> and <code class="docutils literal notranslate"><span class="pre">ReadWrite</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">create_option</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies how the OS Disk should be created. Possible values are <code class="docutils literal notranslate"><span class="pre">Attach</span></code> (managed disks only) and <code class="docutils literal notranslate"><span class="pre">FromImage</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">disk_size_gb</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Specifies the size of the OS Disk in gigabytes.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">imageUri</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the Image URI in the format <code class="docutils literal notranslate"><span class="pre">publisherName:offer:skus:version</span></code>. This field can also specify the <a class="reference external" href="https://azure.microsoft.com/en-us/documentation/articles/virtual-machines-linux-cli-deploy-templates/#create-a-custom-vm-image">VHD uri</a> of a custom VM image to clone. When cloning a Custom (Unmanaged) Disk Image the <code class="docutils literal notranslate"><span class="pre">os_type</span></code> field must be set.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">managed_disk_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the ID of an existing Managed Disk which should be attached as the OS Disk of this Virtual Machine. If this is set then the <code class="docutils literal notranslate"><span class="pre">create_option</span></code> must be set to <code class="docutils literal notranslate"><span class="pre">Attach</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">managedDiskType</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the type of Managed Disk which should be created. Possible values are <code class="docutils literal notranslate"><span class="pre">Standard_LRS</span></code>, <code class="docutils literal notranslate"><span class="pre">StandardSSD_LRS</span></code> or <code class="docutils literal notranslate"><span class="pre">Premium_LRS</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the name of the OS Disk.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">os_type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the Operating System on the OS Disk. Possible values are <code class="docutils literal notranslate"><span class="pre">Linux</span></code> and <code class="docutils literal notranslate"><span class="pre">Windows</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">vhdUri</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the URI of the VHD file backing this Unmanaged OS Disk. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">write_accelerator_enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Specifies if Write Accelerator is enabled on the disk. This can only be enabled on <code class="docutils literal notranslate"><span class="pre">Premium_LRS</span></code> managed disks with no caching and <a class="reference external" href="https://docs.microsoft.com/en-us/azure/virtual-machines/workloads/sap/how-to-enable-write-accelerator">M-Series VMs</a>. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
</ul>
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
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">additional_capabilities=None</em>, <em class="sig-param">availability_set_id=None</em>, <em class="sig-param">boot_diagnostics=None</em>, <em class="sig-param">delete_data_disks_on_termination=None</em>, <em class="sig-param">delete_os_disk_on_termination=None</em>, <em class="sig-param">identity=None</em>, <em class="sig-param">license_type=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">network_interface_ids=None</em>, <em class="sig-param">os_profile=None</em>, <em class="sig-param">os_profile_linux_config=None</em>, <em class="sig-param">os_profile_secrets=None</em>, <em class="sig-param">os_profile_windows_config=None</em>, <em class="sig-param">plan=None</em>, <em class="sig-param">primary_network_interface_id=None</em>, <em class="sig-param">proximity_placement_group_id=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">storage_data_disks=None</em>, <em class="sig-param">storage_image_reference=None</em>, <em class="sig-param">storage_os_disk=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">vm_size=None</em>, <em class="sig-param">zones=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.compute.VirtualMachine.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing VirtualMachine resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>additional_capabilities</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">additional_capabilities</span></code> block.</p></li>
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
<li><p><strong>proximity_placement_group_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Proximity Placement Group to which this Virtual Machine should be assigned. Changing this forces a new resource to be created</p></li>
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
<p>The <strong>additional_capabilities</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">ultraSsdEnabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Should Ultra SSD disk be enabled for this Virtual Machine?</p></li>
</ul>
<p>The <strong>boot_diagnostics</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Should Boot Diagnostics be enabled for this Virtual Machine?</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">storageUri</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Storage Account’s Blob Endpoint which should hold the virtual machine’s diagnostic files.</p></li>
</ul>
<p>The <strong>identity</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">identityIds</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Specifies a list of user managed identity ids to be assigned to the VM. Required if <code class="docutils literal notranslate"><span class="pre">type</span></code> is <code class="docutils literal notranslate"><span class="pre">UserAssigned</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">principal_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Principal ID for the Service Principal associated with the Managed Service Identity of this Virtual Machine.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Managed Service Identity Type of this Virtual Machine. Possible values are <code class="docutils literal notranslate"><span class="pre">SystemAssigned</span></code> (where Azure will generate a Service Principal for you), <code class="docutils literal notranslate"><span class="pre">UserAssigned</span></code> (where you can specify the Service Principal ID’s) to be used by this Virtual Machine using the <code class="docutils literal notranslate"><span class="pre">identity_ids</span></code> field, and <code class="docutils literal notranslate"><span class="pre">SystemAssigned,</span> <span class="pre">UserAssigned</span></code> which assigns both a system managed identity as well as the specified user assigned identities.</p></li>
</ul>
<p>The <strong>os_profile</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">admin_password</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The password associated with the local administrator account.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">admin_username</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the name of the local administrator account.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">computer_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the name of the Virtual Machine.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">custom_data</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies custom data to supply to the machine. On Linux-based systems, this can be used as a cloud-init script. On other systems, this will be copied as a file on disk. Internally, this provider will base64 encode this value before sending it to the API. The maximum length of the binary array is 65535 bytes.</p></li>
</ul>
<p>The <strong>os_profile_linux_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">disable_password_authentication</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Specifies whether password authentication should be disabled. If set to <code class="docutils literal notranslate"><span class="pre">false</span></code>, an <code class="docutils literal notranslate"><span class="pre">admin_password</span></code> must be specified.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sshKeys</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - One or more <code class="docutils literal notranslate"><span class="pre">ssh_keys</span></code> blocks. This field is required if <code class="docutils literal notranslate"><span class="pre">disable_password_authentication</span></code> is set to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">keyData</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Public SSH Key which should be written to the <code class="docutils literal notranslate"><span class="pre">path</span></code> defined above.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">path</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The path of the destination file on the virtual machine</p></li>
</ul>
</li>
</ul>
<p>The <strong>os_profile_secrets</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">sourceVaultId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the ID of the Key Vault to use.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">vaultCertificates</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - One or more <code class="docutils literal notranslate"><span class="pre">vault_certificates</span></code> blocks.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">certificateStore</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the certificate store on the Virtual Machine where the certificate should be added to, such as <code class="docutils literal notranslate"><span class="pre">My</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">certificateUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Key Vault Secret. Stored secret is the Base64 encoding of a JSON Object that which is encoded in UTF-8 of which the contents need to be:</p></li>
</ul>
</li>
</ul>
<p>The <strong>os_profile_windows_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">additionalUnattendConfigs</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">additional_unattend_config</span></code> block.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">component</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the name of the component to configure with the added content. The only allowable value is <code class="docutils literal notranslate"><span class="pre">Microsoft-Windows-Shell-Setup</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">content</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the base-64 encoded XML formatted content that is added to the unattend.xml file for the specified path and component.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">pass</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the name of the pass that the content applies to. The only allowable value is <code class="docutils literal notranslate"><span class="pre">oobeSystem</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">settingName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the name of the setting to which the content applies. Possible values are: <code class="docutils literal notranslate"><span class="pre">FirstLogonCommands</span></code> and <code class="docutils literal notranslate"><span class="pre">AutoLogon</span></code>.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">enableAutomaticUpgrades</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Are automatic updates enabled on this Virtual Machine? Defaults to <code class="docutils literal notranslate"><span class="pre">false.</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">provision_vm_agent</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Should the Azure Virtual Machine Guest Agent be installed on this Virtual Machine? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timezone</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the time zone of the virtual machine, <a class="reference external" href="http://jackstromberg.com/2017/01/list-of-time-zones-consumed-by-azure/">the possible values are defined here</a>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">winrms</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - One or more <code class="docutils literal notranslate"><span class="pre">winrm</span></code> block.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">certificateUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Key Vault Secret which contains the encrypted Certificate which should be installed on the Virtual Machine. This certificate must also be specified in the <code class="docutils literal notranslate"><span class="pre">vault_certificates</span></code> block within the <code class="docutils literal notranslate"><span class="pre">os_profile_secrets</span></code> block.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">protocol</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the protocol of listener. Possible values are <code class="docutils literal notranslate"><span class="pre">HTTP</span></code> or <code class="docutils literal notranslate"><span class="pre">HTTPS</span></code>.</p></li>
</ul>
</li>
</ul>
<p>The <strong>plan</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the name of the image from the marketplace.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">product</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the product of the image from the marketplace.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">publisher</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the publisher of the image.</p></li>
</ul>
<p>The <strong>storage_data_disks</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">caching</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the caching requirements for the Data Disk. Possible values include <code class="docutils literal notranslate"><span class="pre">None</span></code>, <code class="docutils literal notranslate"><span class="pre">ReadOnly</span></code> and <code class="docutils literal notranslate"><span class="pre">ReadWrite</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">create_option</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies how the data disk should be created. Possible values are <code class="docutils literal notranslate"><span class="pre">Attach</span></code>, <code class="docutils literal notranslate"><span class="pre">FromImage</span></code> and <code class="docutils literal notranslate"><span class="pre">Empty</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">disk_size_gb</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Specifies the size of the data disk in gigabytes.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">lun</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Specifies the logical unit number of the data disk. This needs to be unique within all the Data Disks on the Virtual Machine.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">managed_disk_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the ID of an Existing Managed Disk which should be attached to this Virtual Machine. When this field is set <code class="docutils literal notranslate"><span class="pre">create_option</span></code> must be set to <code class="docutils literal notranslate"><span class="pre">Attach</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">managedDiskType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the type of managed disk to create. Possible values are either <code class="docutils literal notranslate"><span class="pre">Standard_LRS</span></code>, <code class="docutils literal notranslate"><span class="pre">StandardSSD_LRS</span></code>, <code class="docutils literal notranslate"><span class="pre">Premium_LRS</span></code> or <code class="docutils literal notranslate"><span class="pre">UltraSSD_LRS</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the Data Disk.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">vhdUri</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the URI of the VHD file backing this Unmanaged Data Disk. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">write_accelerator_enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Specifies if Write Accelerator is enabled on the disk. This can only be enabled on <code class="docutils literal notranslate"><span class="pre">Premium_LRS</span></code> managed disks with no caching and <a class="reference external" href="https://docs.microsoft.com/en-us/azure/virtual-machines/workloads/sap/how-to-enable-write-accelerator">M-Series VMs</a>. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
</ul>
<p>The <strong>storage_image_reference</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the ID of the Custom Image which the Virtual Machine should be created from. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">offer</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the offer of the image used to create the virtual machine. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">publisher</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the publisher of the image used to create the virtual machine. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sku</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the SKU of the image used to create the virtual machine. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">version</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the version of the image used to create the virtual machine. Changing this forces a new resource to be created.</p></li>
</ul>
<p>The <strong>storage_os_disk</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">caching</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the caching requirements for the OS Disk. Possible values include <code class="docutils literal notranslate"><span class="pre">None</span></code>, <code class="docutils literal notranslate"><span class="pre">ReadOnly</span></code> and <code class="docutils literal notranslate"><span class="pre">ReadWrite</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">create_option</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies how the OS Disk should be created. Possible values are <code class="docutils literal notranslate"><span class="pre">Attach</span></code> (managed disks only) and <code class="docutils literal notranslate"><span class="pre">FromImage</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">disk_size_gb</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Specifies the size of the OS Disk in gigabytes.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">imageUri</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the Image URI in the format <code class="docutils literal notranslate"><span class="pre">publisherName:offer:skus:version</span></code>. This field can also specify the <a class="reference external" href="https://azure.microsoft.com/en-us/documentation/articles/virtual-machines-linux-cli-deploy-templates/#create-a-custom-vm-image">VHD uri</a> of a custom VM image to clone. When cloning a Custom (Unmanaged) Disk Image the <code class="docutils literal notranslate"><span class="pre">os_type</span></code> field must be set.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">managed_disk_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the ID of an existing Managed Disk which should be attached as the OS Disk of this Virtual Machine. If this is set then the <code class="docutils literal notranslate"><span class="pre">create_option</span></code> must be set to <code class="docutils literal notranslate"><span class="pre">Attach</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">managedDiskType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the type of Managed Disk which should be created. Possible values are <code class="docutils literal notranslate"><span class="pre">Standard_LRS</span></code>, <code class="docutils literal notranslate"><span class="pre">StandardSSD_LRS</span></code> or <code class="docutils literal notranslate"><span class="pre">Premium_LRS</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the name of the OS Disk.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">os_type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the Operating System on the OS Disk. Possible values are <code class="docutils literal notranslate"><span class="pre">Linux</span></code> and <code class="docutils literal notranslate"><span class="pre">Windows</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">vhdUri</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the URI of the VHD file backing this Unmanaged OS Disk. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">write_accelerator_enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Specifies if Write Accelerator is enabled on the disk. This can only be enabled on <code class="docutils literal notranslate"><span class="pre">Premium_LRS</span></code> managed disks with no caching and <a class="reference external" href="https://docs.microsoft.com/en-us/azure/virtual-machines/workloads/sap/how-to-enable-write-accelerator">M-Series VMs</a>. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
</ul>
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

<dl class="class">
<dt id="pulumi_azure.compute.VirtualMachineScaleSetExtension">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.compute.</code><code class="sig-name descname">VirtualMachineScaleSetExtension</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">auto_upgrade_minor_version=None</em>, <em class="sig-param">force_update_tag=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">protected_settings=None</em>, <em class="sig-param">provision_after_extensions=None</em>, <em class="sig-param">publisher=None</em>, <em class="sig-param">settings=None</em>, <em class="sig-param">type=None</em>, <em class="sig-param">type_handler_version=None</em>, <em class="sig-param">virtual_machine_scale_set_id=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.compute.VirtualMachineScaleSetExtension" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an Extension for a Virtual Machine Scale Set.</p>
<blockquote>
<div><p><strong>NOTE:</strong> This resource is not intended to be used with the <code class="docutils literal notranslate"><span class="pre">compute.ScaleSet</span></code> resource - instead it’s intended for this to be used with the <code class="docutils literal notranslate"><span class="pre">compute.LinuxVirtualMachineScaleSet</span></code> and <code class="docutils literal notranslate"><span class="pre">compute.WindowsVirtualMachineScaleSet</span></code> resources.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>auto_upgrade_minor_version</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Should the latest version of the Extension be used at Deployment Time, if one is available? This won’t auto-update the extension on existing installation. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>force_update_tag</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A value which, when different to the previous value can be used to force-run the Extension even if the Extension Configuration hasn’t changed.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name for the Virtual Machine Scale Set Extension. Changing this forces a new resource to be created.</p></li>
<li><p><strong>protected_settings</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A JSON String which specifies Sensitive Settings (such as Passwords) for the Extension.</p></li>
<li><p><strong>provision_after_extensions</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – An ordered list of Extension names which this should be provisioned after.</p></li>
<li><p><strong>publisher</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the Publisher of the Extension. Changing this forces a new resource to be created.</p></li>
<li><p><strong>settings</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A JSON String which specifies Settings for the Extension.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the Type of the Extension. Changing this forces a new resource to be created.</p></li>
<li><p><strong>type_handler_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the version of the extension to use, available versions can be found using the Azure CLI.</p></li>
<li><p><strong>virtual_machine_scale_set_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Virtual Machine Scale Set. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
<dl class="attribute">
<dt id="pulumi_azure.compute.VirtualMachineScaleSetExtension.auto_upgrade_minor_version">
<code class="sig-name descname">auto_upgrade_minor_version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.VirtualMachineScaleSetExtension.auto_upgrade_minor_version" title="Permalink to this definition">¶</a></dt>
<dd><p>Should the latest version of the Extension be used at Deployment Time, if one is available? This won’t auto-update the extension on existing installation. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.VirtualMachineScaleSetExtension.force_update_tag">
<code class="sig-name descname">force_update_tag</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.VirtualMachineScaleSetExtension.force_update_tag" title="Permalink to this definition">¶</a></dt>
<dd><p>A value which, when different to the previous value can be used to force-run the Extension even if the Extension Configuration hasn’t changed.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.VirtualMachineScaleSetExtension.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.VirtualMachineScaleSetExtension.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name for the Virtual Machine Scale Set Extension. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.VirtualMachineScaleSetExtension.protected_settings">
<code class="sig-name descname">protected_settings</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.VirtualMachineScaleSetExtension.protected_settings" title="Permalink to this definition">¶</a></dt>
<dd><p>A JSON String which specifies Sensitive Settings (such as Passwords) for the Extension.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.VirtualMachineScaleSetExtension.provision_after_extensions">
<code class="sig-name descname">provision_after_extensions</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.VirtualMachineScaleSetExtension.provision_after_extensions" title="Permalink to this definition">¶</a></dt>
<dd><p>An ordered list of Extension names which this should be provisioned after.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.VirtualMachineScaleSetExtension.publisher">
<code class="sig-name descname">publisher</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.VirtualMachineScaleSetExtension.publisher" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the Publisher of the Extension. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.VirtualMachineScaleSetExtension.settings">
<code class="sig-name descname">settings</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.VirtualMachineScaleSetExtension.settings" title="Permalink to this definition">¶</a></dt>
<dd><p>A JSON String which specifies Settings for the Extension.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.VirtualMachineScaleSetExtension.type">
<code class="sig-name descname">type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.VirtualMachineScaleSetExtension.type" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the Type of the Extension. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.VirtualMachineScaleSetExtension.type_handler_version">
<code class="sig-name descname">type_handler_version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.VirtualMachineScaleSetExtension.type_handler_version" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the version of the extension to use, available versions can be found using the Azure CLI.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.VirtualMachineScaleSetExtension.virtual_machine_scale_set_id">
<code class="sig-name descname">virtual_machine_scale_set_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.VirtualMachineScaleSetExtension.virtual_machine_scale_set_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Virtual Machine Scale Set. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.compute.VirtualMachineScaleSetExtension.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">auto_upgrade_minor_version=None</em>, <em class="sig-param">force_update_tag=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">protected_settings=None</em>, <em class="sig-param">provision_after_extensions=None</em>, <em class="sig-param">publisher=None</em>, <em class="sig-param">settings=None</em>, <em class="sig-param">type=None</em>, <em class="sig-param">type_handler_version=None</em>, <em class="sig-param">virtual_machine_scale_set_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.compute.VirtualMachineScaleSetExtension.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing VirtualMachineScaleSetExtension resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>auto_upgrade_minor_version</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Should the latest version of the Extension be used at Deployment Time, if one is available? This won’t auto-update the extension on existing installation. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>force_update_tag</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A value which, when different to the previous value can be used to force-run the Extension even if the Extension Configuration hasn’t changed.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name for the Virtual Machine Scale Set Extension. Changing this forces a new resource to be created.</p></li>
<li><p><strong>protected_settings</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A JSON String which specifies Sensitive Settings (such as Passwords) for the Extension.</p></li>
<li><p><strong>provision_after_extensions</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – An ordered list of Extension names which this should be provisioned after.</p></li>
<li><p><strong>publisher</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the Publisher of the Extension. Changing this forces a new resource to be created.</p></li>
<li><p><strong>settings</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A JSON String which specifies Settings for the Extension.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the Type of the Extension. Changing this forces a new resource to be created.</p></li>
<li><p><strong>type_handler_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the version of the extension to use, available versions can be found using the Azure CLI.</p></li>
<li><p><strong>virtual_machine_scale_set_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Virtual Machine Scale Set. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.compute.VirtualMachineScaleSetExtension.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.compute.VirtualMachineScaleSetExtension.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.compute.VirtualMachineScaleSetExtension.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.compute.VirtualMachineScaleSetExtension.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.compute.WindowsVirtualMachine">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.compute.</code><code class="sig-name descname">WindowsVirtualMachine</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">additional_capabilities=None</em>, <em class="sig-param">additional_unattend_contents=None</em>, <em class="sig-param">admin_password=None</em>, <em class="sig-param">admin_username=None</em>, <em class="sig-param">allow_extension_operations=None</em>, <em class="sig-param">availability_set_id=None</em>, <em class="sig-param">boot_diagnostics=None</em>, <em class="sig-param">computer_name=None</em>, <em class="sig-param">custom_data=None</em>, <em class="sig-param">dedicated_host_id=None</em>, <em class="sig-param">enable_automatic_updates=None</em>, <em class="sig-param">eviction_policy=None</em>, <em class="sig-param">identity=None</em>, <em class="sig-param">license_type=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">max_bid_price=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">network_interface_ids=None</em>, <em class="sig-param">os_disk=None</em>, <em class="sig-param">plan=None</em>, <em class="sig-param">priority=None</em>, <em class="sig-param">provision_vm_agent=None</em>, <em class="sig-param">proximity_placement_group_id=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">secrets=None</em>, <em class="sig-param">size=None</em>, <em class="sig-param">source_image_id=None</em>, <em class="sig-param">source_image_reference=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">timezone=None</em>, <em class="sig-param">winrm_listeners=None</em>, <em class="sig-param">zone=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.compute.WindowsVirtualMachine" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Windows Virtual Machine.</p>
<blockquote>
<div><p><strong>Note</strong> This provider will automatically remove the OS Disk by default - this behaviour can be configured using the <code class="docutils literal notranslate"><span class="pre">features</span></code> configuration within the Provider configuration block.</p>
<p><strong>Note</strong> This resource does not support Unmanaged Disks. If you need to use Unmanaged Disks you can continue to use the <code class="docutils literal notranslate"><span class="pre">compute.VirtualMachine</span></code> resource instead.</p>
<p><strong>Note</strong> This resource does not support attaching existing OS Disks. You can instead capture an image of the OS Disk or continue to use the <code class="docutils literal notranslate"><span class="pre">compute.VirtualMachine</span></code> resource instead.</p>
<p>In this release there’s a known issue where the <code class="docutils literal notranslate"><span class="pre">public_ip_address</span></code> and <code class="docutils literal notranslate"><span class="pre">public_ip_addresses</span></code> fields may not be fully populated for Dynamic Public IP’s.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>additional_capabilities</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">additional_capabilities</span></code> block as defined below.</p></li>
<li><p><strong>additional_unattend_contents</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">additional_unattend_content</span></code> blocks as defined below. Changing this forces a new resource to be created.</p></li>
<li><p><strong>admin_password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Password which should be used for the local-administrator on this Virtual Machine. Changing this forces a new resource to be created.</p></li>
<li><p><strong>admin_username</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The username of the local administrator used for the Virtual Machine. Changing this forces a new resource to be created.</p></li>
<li><p><strong>allow_extension_operations</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Should Extension Operations be allowed on this Virtual Machine? Changing this forces a new resource to be created.</p></li>
<li><p><strong>availability_set_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the ID of the Availability Set in which the Virtual Machine should exist. Changing this forces a new resource to be created.</p></li>
<li><p><strong>boot_diagnostics</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">boot_diagnostics</span></code> block as defined below.</p></li>
<li><p><strong>computer_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the Hostname which should be used for this Virtual Machine. If unspecified this defaults to the value for the <code class="docutils literal notranslate"><span class="pre">name</span></code> field. Changing this forces a new resource to be created.</p></li>
<li><p><strong>custom_data</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Base64-Encoded Custom Data which should be used for this Virtual Machine. Changing this forces a new resource to be created.</p></li>
<li><p><strong>dedicated_host_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of a Dedicated Host where this machine should be run on. Changing this forces a new resource to be created.</p></li>
<li><p><strong>enable_automatic_updates</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specifies if Automatic Updates are Enabled for the Windows Virtual Machine. Changing this forces a new resource to be created.</p></li>
<li><p><strong>eviction_policy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies what should happen when the Virtual Machine is evicted for price reasons when using a Spot instance. At this time the only supported value is <code class="docutils literal notranslate"><span class="pre">Deallocate</span></code>. Changing this forces a new resource to be created.</p></li>
<li><p><strong>identity</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – An <code class="docutils literal notranslate"><span class="pre">identity</span></code> block as defined below.</p></li>
<li><p><strong>license_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the type of on-premise license (also known as <a class="reference external" href="https://docs.microsoft.com/azure/virtual-machines/virtual-machines-windows-hybrid-use-benefit-licensing">Azure Hybrid Use Benefit</a>) which should be used for this Virtual Machine. Possible values are <code class="docutils literal notranslate"><span class="pre">None</span></code>, <code class="docutils literal notranslate"><span class="pre">Windows_Client</span></code> and <code class="docutils literal notranslate"><span class="pre">Windows_Server</span></code>. Changing this forces a new resource to be created.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Azure location where the Windows Virtual Machine should exist. Changing this forces a new resource to be created.</p></li>
<li><p><strong>max_bid_price</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The maximum price you’re willing to pay for this Virtual Machine, in US Dollars; which must be greater than the current spot price. If this bid price falls below the current spot price the Virtual Machine will be evicted using the <code class="docutils literal notranslate"><span class="pre">eviction_policy</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">-1</span></code>, which means that the Virtual Machine should not be evicted for price reasons.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Windows Virtual Machine. Changing this forces a new resource to be created.</p></li>
<li><p><strong>network_interface_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – . A list of Network Interface ID’s which should be attached to this Virtual Machine. The first Network Interface ID in this list will be the Primary Network Interface on the Virtual Machine.</p></li>
<li><p><strong>os_disk</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">os_disk</span></code> block as defined below.</p></li>
<li><p><strong>plan</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">plan</span></code> block as defined below. Changing this forces a new resource to be created.</p></li>
<li><p><strong>priority</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the priority of this Virtual Machine. Possible values are <code class="docutils literal notranslate"><span class="pre">Regular</span></code> and <code class="docutils literal notranslate"><span class="pre">Spot</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">Regular</span></code>. Changing this forces a new resource to be created.</p></li>
<li><p><strong>provision_vm_agent</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Should the Azure VM Agent be provisioned on this Virtual Machine? Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>. Changing this forces a new resource to be created.</p></li>
<li><p><strong>proximity_placement_group_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Proximity Placement Group which the Virtual Machine should be assigned to. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Resource Group in which the Windows Virtual Machine should be exist. Changing this forces a new resource to be created.</p></li>
<li><p><strong>secrets</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">secret</span></code> blocks as defined below.</p></li>
<li><p><strong>size</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The SKU which should be used for this Virtual Machine, such as <code class="docutils literal notranslate"><span class="pre">Standard_F2</span></code>.</p></li>
<li><p><strong>source_image_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Image which this Virtual Machine should be created from. Changing this forces a new resource to be created.</p></li>
<li><p><strong>source_image_reference</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">source_image_reference</span></code> block as defined below. Changing this forces a new resource to be created.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags which should be assigned to this Virtual Machine.</p></li>
<li><p><strong>timezone</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>Specifies the Time Zone which should be used by the Virtual Machine, <a class="reference external" href="https://jackstromberg.com/2017/01/list-of-time-zones-consumed-by-azure/">the possible values are defined here</a>.</p>
</p></li>
<li><p><strong>winrm_listeners</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">winrm_listener</span></code> blocks as defined below.</p></li>
<li><p><strong>zone</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Zone in which this Virtual Machine should be created. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>additional_capabilities</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">ultraSsdEnabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Should the capacity to enable Data Disks of the <code class="docutils literal notranslate"><span class="pre">UltraSSD_LRS</span></code> storage account type be supported on this Virtual Machine? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>. Changing this forces a new resource to be created.</p></li>
</ul>
<p>The <strong>additional_unattend_contents</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">content</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The XML formatted content that is added to the unattend.xml file for the specified path and component. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">setting</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the setting to which the content applies. Possible values are <code class="docutils literal notranslate"><span class="pre">AutoLogon</span></code> and <code class="docutils literal notranslate"><span class="pre">FirstLogonCommands</span></code>. Changing this forces a new resource to be created.</p></li>
</ul>
<p>The <strong>boot_diagnostics</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">storageAccountUri</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Primary/Secondary Endpoint for the Azure Storage Account which should be used to store Boot Diagnostics, including Console Output and Screenshots from the Hypervisor.</p></li>
</ul>
<p>The <strong>identity</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">identityIds</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of User Managed Identity ID’s which should be assigned to the Windows Virtual Machine.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">principal_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the System Managed Service Principal.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The type of Managed Identity which should be assigned to the Windows Virtual Machine. Possible values are <code class="docutils literal notranslate"><span class="pre">SystemAssigned</span></code>, <code class="docutils literal notranslate"><span class="pre">UserAssigned</span></code> and <code class="docutils literal notranslate"><span class="pre">SystemAssigned,</span> <span class="pre">UserAssigned</span></code>.</p></li>
</ul>
<p>The <strong>os_disk</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">caching</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Type of Caching which should be used for the Internal OS Disk. Possible values are <code class="docutils literal notranslate"><span class="pre">None</span></code>, <code class="docutils literal notranslate"><span class="pre">ReadOnly</span></code> and <code class="docutils literal notranslate"><span class="pre">ReadWrite</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">diffDiskSettings</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">diff_disk_settings</span></code> block as defined above.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">option</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the Ephemeral Disk Settings for the OS Disk. At this time the only possible value is <code class="docutils literal notranslate"><span class="pre">Local</span></code>. Changing this forces a new resource to be created.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">disk_encryption_set_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Disk Encryption Set which should be used to Encrypt this OS Disk.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">disk_size_gb</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The Size of the Internal OS Disk in GB, if you wish to vary from the size used in the image this Virtual Machine is sourced from.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name which should be used for the Internal OS Disk. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">storage_account_type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Type of Storage Account which should back this the Internal OS Disk. Possible values are <code class="docutils literal notranslate"><span class="pre">Standard_LRS</span></code>, <code class="docutils literal notranslate"><span class="pre">StandardSSD_LRS</span></code> and <code class="docutils literal notranslate"><span class="pre">Premium_LRS</span></code>. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">write_accelerator_enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Should Write Accelerator be Enabled for this OS Disk? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
</ul>
<p>The <strong>plan</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the Name of the Marketplace Image this Virtual Machine should be created from. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">product</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the Product of the Marketplace Image this Virtual Machine should be created from. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">publisher</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the Publisher of the Marketplace Image this Virtual Machine should be created from. Changing this forces a new resource to be created.</p></li>
</ul>
<p>The <strong>secrets</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">certificates</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - One or more <code class="docutils literal notranslate"><span class="pre">certificate</span></code> blocks as defined above.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">store</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The certificate store on the Virtual Machine where the certificate should be added.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">url</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Secret URL of a Key Vault Certificate.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">key_vault_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Key Vault from which all Secrets should be sourced.</p></li>
</ul>
<p>The <strong>source_image_reference</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">offer</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">publisher</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the Publisher of the Marketplace Image this Virtual Machine should be created from. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sku</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">version</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>winrm_listeners</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">certificateUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Secret URL of a Key Vault Certificate, which must be specified when <code class="docutils literal notranslate"><span class="pre">protocol</span></code> is set to <code class="docutils literal notranslate"><span class="pre">Https</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">protocol</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_azure.compute.WindowsVirtualMachine.additional_capabilities">
<code class="sig-name descname">additional_capabilities</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.WindowsVirtualMachine.additional_capabilities" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">additional_capabilities</span></code> block as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">ultraSsdEnabled</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Should the capacity to enable Data Disks of the <code class="docutils literal notranslate"><span class="pre">UltraSSD_LRS</span></code> storage account type be supported on this Virtual Machine? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>. Changing this forces a new resource to be created.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.WindowsVirtualMachine.additional_unattend_contents">
<code class="sig-name descname">additional_unattend_contents</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.WindowsVirtualMachine.additional_unattend_contents" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more <code class="docutils literal notranslate"><span class="pre">additional_unattend_content</span></code> blocks as defined below. Changing this forces a new resource to be created.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">content</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The XML formatted content that is added to the unattend.xml file for the specified path and component. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">setting</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the setting to which the content applies. Possible values are <code class="docutils literal notranslate"><span class="pre">AutoLogon</span></code> and <code class="docutils literal notranslate"><span class="pre">FirstLogonCommands</span></code>. Changing this forces a new resource to be created.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.WindowsVirtualMachine.admin_password">
<code class="sig-name descname">admin_password</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.WindowsVirtualMachine.admin_password" title="Permalink to this definition">¶</a></dt>
<dd><p>The Password which should be used for the local-administrator on this Virtual Machine. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.WindowsVirtualMachine.admin_username">
<code class="sig-name descname">admin_username</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.WindowsVirtualMachine.admin_username" title="Permalink to this definition">¶</a></dt>
<dd><p>The username of the local administrator used for the Virtual Machine. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.WindowsVirtualMachine.allow_extension_operations">
<code class="sig-name descname">allow_extension_operations</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.WindowsVirtualMachine.allow_extension_operations" title="Permalink to this definition">¶</a></dt>
<dd><p>Should Extension Operations be allowed on this Virtual Machine? Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.WindowsVirtualMachine.availability_set_id">
<code class="sig-name descname">availability_set_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.WindowsVirtualMachine.availability_set_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the ID of the Availability Set in which the Virtual Machine should exist. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.WindowsVirtualMachine.boot_diagnostics">
<code class="sig-name descname">boot_diagnostics</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.WindowsVirtualMachine.boot_diagnostics" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">boot_diagnostics</span></code> block as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">storageAccountUri</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Primary/Secondary Endpoint for the Azure Storage Account which should be used to store Boot Diagnostics, including Console Output and Screenshots from the Hypervisor.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.WindowsVirtualMachine.computer_name">
<code class="sig-name descname">computer_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.WindowsVirtualMachine.computer_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the Hostname which should be used for this Virtual Machine. If unspecified this defaults to the value for the <code class="docutils literal notranslate"><span class="pre">name</span></code> field. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.WindowsVirtualMachine.custom_data">
<code class="sig-name descname">custom_data</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.WindowsVirtualMachine.custom_data" title="Permalink to this definition">¶</a></dt>
<dd><p>The Base64-Encoded Custom Data which should be used for this Virtual Machine. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.WindowsVirtualMachine.dedicated_host_id">
<code class="sig-name descname">dedicated_host_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.WindowsVirtualMachine.dedicated_host_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of a Dedicated Host where this machine should be run on. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.WindowsVirtualMachine.enable_automatic_updates">
<code class="sig-name descname">enable_automatic_updates</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.WindowsVirtualMachine.enable_automatic_updates" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies if Automatic Updates are Enabled for the Windows Virtual Machine. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.WindowsVirtualMachine.eviction_policy">
<code class="sig-name descname">eviction_policy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.WindowsVirtualMachine.eviction_policy" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies what should happen when the Virtual Machine is evicted for price reasons when using a Spot instance. At this time the only supported value is <code class="docutils literal notranslate"><span class="pre">Deallocate</span></code>. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.WindowsVirtualMachine.identity">
<code class="sig-name descname">identity</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.WindowsVirtualMachine.identity" title="Permalink to this definition">¶</a></dt>
<dd><p>An <code class="docutils literal notranslate"><span class="pre">identity</span></code> block as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">identityIds</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - A list of User Managed Identity ID’s which should be assigned to the Windows Virtual Machine.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">principal_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the System Managed Service Principal.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The type of Managed Identity which should be assigned to the Windows Virtual Machine. Possible values are <code class="docutils literal notranslate"><span class="pre">SystemAssigned</span></code>, <code class="docutils literal notranslate"><span class="pre">UserAssigned</span></code> and <code class="docutils literal notranslate"><span class="pre">SystemAssigned,</span> <span class="pre">UserAssigned</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.WindowsVirtualMachine.license_type">
<code class="sig-name descname">license_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.WindowsVirtualMachine.license_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the type of on-premise license (also known as <a class="reference external" href="https://docs.microsoft.com/azure/virtual-machines/virtual-machines-windows-hybrid-use-benefit-licensing">Azure Hybrid Use Benefit</a>) which should be used for this Virtual Machine. Possible values are <code class="docutils literal notranslate"><span class="pre">None</span></code>, <code class="docutils literal notranslate"><span class="pre">Windows_Client</span></code> and <code class="docutils literal notranslate"><span class="pre">Windows_Server</span></code>. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.WindowsVirtualMachine.location">
<code class="sig-name descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.WindowsVirtualMachine.location" title="Permalink to this definition">¶</a></dt>
<dd><p>The Azure location where the Windows Virtual Machine should exist. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.WindowsVirtualMachine.max_bid_price">
<code class="sig-name descname">max_bid_price</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.WindowsVirtualMachine.max_bid_price" title="Permalink to this definition">¶</a></dt>
<dd><p>The maximum price you’re willing to pay for this Virtual Machine, in US Dollars; which must be greater than the current spot price. If this bid price falls below the current spot price the Virtual Machine will be evicted using the <code class="docutils literal notranslate"><span class="pre">eviction_policy</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">-1</span></code>, which means that the Virtual Machine should not be evicted for price reasons.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.WindowsVirtualMachine.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.WindowsVirtualMachine.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Windows Virtual Machine. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.WindowsVirtualMachine.network_interface_ids">
<code class="sig-name descname">network_interface_ids</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.WindowsVirtualMachine.network_interface_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>. A list of Network Interface ID’s which should be attached to this Virtual Machine. The first Network Interface ID in this list will be the Primary Network Interface on the Virtual Machine.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.WindowsVirtualMachine.os_disk">
<code class="sig-name descname">os_disk</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.WindowsVirtualMachine.os_disk" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">os_disk</span></code> block as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">caching</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Type of Caching which should be used for the Internal OS Disk. Possible values are <code class="docutils literal notranslate"><span class="pre">None</span></code>, <code class="docutils literal notranslate"><span class="pre">ReadOnly</span></code> and <code class="docutils literal notranslate"><span class="pre">ReadWrite</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">diffDiskSettings</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - A <code class="docutils literal notranslate"><span class="pre">diff_disk_settings</span></code> block as defined above.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">option</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the Ephemeral Disk Settings for the OS Disk. At this time the only possible value is <code class="docutils literal notranslate"><span class="pre">Local</span></code>. Changing this forces a new resource to be created.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">disk_encryption_set_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the Disk Encryption Set which should be used to Encrypt this OS Disk.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">disk_size_gb</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The Size of the Internal OS Disk in GB, if you wish to vary from the size used in the image this Virtual Machine is sourced from.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name which should be used for the Internal OS Disk. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">storage_account_type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Type of Storage Account which should back this the Internal OS Disk. Possible values are <code class="docutils literal notranslate"><span class="pre">Standard_LRS</span></code>, <code class="docutils literal notranslate"><span class="pre">StandardSSD_LRS</span></code> and <code class="docutils literal notranslate"><span class="pre">Premium_LRS</span></code>. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">write_accelerator_enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Should Write Accelerator be Enabled for this OS Disk? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.WindowsVirtualMachine.plan">
<code class="sig-name descname">plan</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.WindowsVirtualMachine.plan" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">plan</span></code> block as defined below. Changing this forces a new resource to be created.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the Name of the Marketplace Image this Virtual Machine should be created from. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">product</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the Product of the Marketplace Image this Virtual Machine should be created from. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">publisher</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the Publisher of the Marketplace Image this Virtual Machine should be created from. Changing this forces a new resource to be created.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.WindowsVirtualMachine.priority">
<code class="sig-name descname">priority</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.WindowsVirtualMachine.priority" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the priority of this Virtual Machine. Possible values are <code class="docutils literal notranslate"><span class="pre">Regular</span></code> and <code class="docutils literal notranslate"><span class="pre">Spot</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">Regular</span></code>. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.WindowsVirtualMachine.private_ip_address">
<code class="sig-name descname">private_ip_address</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.WindowsVirtualMachine.private_ip_address" title="Permalink to this definition">¶</a></dt>
<dd><p>The Primary Private IP Address assigned to this Virtual Machine.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.WindowsVirtualMachine.private_ip_addresses">
<code class="sig-name descname">private_ip_addresses</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.WindowsVirtualMachine.private_ip_addresses" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of Private IP Addresses assigned to this Virtual Machine.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.WindowsVirtualMachine.provision_vm_agent">
<code class="sig-name descname">provision_vm_agent</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.WindowsVirtualMachine.provision_vm_agent" title="Permalink to this definition">¶</a></dt>
<dd><p>Should the Azure VM Agent be provisioned on this Virtual Machine? Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.WindowsVirtualMachine.proximity_placement_group_id">
<code class="sig-name descname">proximity_placement_group_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.WindowsVirtualMachine.proximity_placement_group_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Proximity Placement Group which the Virtual Machine should be assigned to. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.WindowsVirtualMachine.public_ip_address">
<code class="sig-name descname">public_ip_address</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.WindowsVirtualMachine.public_ip_address" title="Permalink to this definition">¶</a></dt>
<dd><p>The Primary Public IP Address assigned to this Virtual Machine.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.WindowsVirtualMachine.public_ip_addresses">
<code class="sig-name descname">public_ip_addresses</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.WindowsVirtualMachine.public_ip_addresses" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of the Public IP Addresses assigned to this Virtual Machine.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.WindowsVirtualMachine.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.WindowsVirtualMachine.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Resource Group in which the Windows Virtual Machine should be exist. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.WindowsVirtualMachine.secrets">
<code class="sig-name descname">secrets</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.WindowsVirtualMachine.secrets" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more <code class="docutils literal notranslate"><span class="pre">secret</span></code> blocks as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">certificates</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - One or more <code class="docutils literal notranslate"><span class="pre">certificate</span></code> blocks as defined above.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">store</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The certificate store on the Virtual Machine where the certificate should be added.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">url</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Secret URL of a Key Vault Certificate.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">key_vault_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the Key Vault from which all Secrets should be sourced.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.WindowsVirtualMachine.size">
<code class="sig-name descname">size</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.WindowsVirtualMachine.size" title="Permalink to this definition">¶</a></dt>
<dd><p>The SKU which should be used for this Virtual Machine, such as <code class="docutils literal notranslate"><span class="pre">Standard_F2</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.WindowsVirtualMachine.source_image_id">
<code class="sig-name descname">source_image_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.WindowsVirtualMachine.source_image_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Image which this Virtual Machine should be created from. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.WindowsVirtualMachine.source_image_reference">
<code class="sig-name descname">source_image_reference</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.WindowsVirtualMachine.source_image_reference" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">source_image_reference</span></code> block as defined below. Changing this forces a new resource to be created.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">offer</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">publisher</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the Publisher of the Marketplace Image this Virtual Machine should be created from. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sku</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">version</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.WindowsVirtualMachine.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.WindowsVirtualMachine.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags which should be assigned to this Virtual Machine.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.WindowsVirtualMachine.timezone">
<code class="sig-name descname">timezone</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.WindowsVirtualMachine.timezone" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the Time Zone which should be used by the Virtual Machine, <a class="reference external" href="https://jackstromberg.com/2017/01/list-of-time-zones-consumed-by-azure/">the possible values are defined here</a>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.WindowsVirtualMachine.virtual_machine_id">
<code class="sig-name descname">virtual_machine_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.WindowsVirtualMachine.virtual_machine_id" title="Permalink to this definition">¶</a></dt>
<dd><p>A 128-bit identifier which uniquely identifies this Virtual Machine.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.WindowsVirtualMachine.winrm_listeners">
<code class="sig-name descname">winrm_listeners</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.WindowsVirtualMachine.winrm_listeners" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more <code class="docutils literal notranslate"><span class="pre">winrm_listener</span></code> blocks as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">certificateUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Secret URL of a Key Vault Certificate, which must be specified when <code class="docutils literal notranslate"><span class="pre">protocol</span></code> is set to <code class="docutils literal notranslate"><span class="pre">Https</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">protocol</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.WindowsVirtualMachine.zone">
<code class="sig-name descname">zone</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.WindowsVirtualMachine.zone" title="Permalink to this definition">¶</a></dt>
<dd><p>The Zone in which this Virtual Machine should be created. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.compute.WindowsVirtualMachine.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">additional_capabilities=None</em>, <em class="sig-param">additional_unattend_contents=None</em>, <em class="sig-param">admin_password=None</em>, <em class="sig-param">admin_username=None</em>, <em class="sig-param">allow_extension_operations=None</em>, <em class="sig-param">availability_set_id=None</em>, <em class="sig-param">boot_diagnostics=None</em>, <em class="sig-param">computer_name=None</em>, <em class="sig-param">custom_data=None</em>, <em class="sig-param">dedicated_host_id=None</em>, <em class="sig-param">enable_automatic_updates=None</em>, <em class="sig-param">eviction_policy=None</em>, <em class="sig-param">identity=None</em>, <em class="sig-param">license_type=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">max_bid_price=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">network_interface_ids=None</em>, <em class="sig-param">os_disk=None</em>, <em class="sig-param">plan=None</em>, <em class="sig-param">priority=None</em>, <em class="sig-param">private_ip_address=None</em>, <em class="sig-param">private_ip_addresses=None</em>, <em class="sig-param">provision_vm_agent=None</em>, <em class="sig-param">proximity_placement_group_id=None</em>, <em class="sig-param">public_ip_address=None</em>, <em class="sig-param">public_ip_addresses=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">secrets=None</em>, <em class="sig-param">size=None</em>, <em class="sig-param">source_image_id=None</em>, <em class="sig-param">source_image_reference=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">timezone=None</em>, <em class="sig-param">virtual_machine_id=None</em>, <em class="sig-param">winrm_listeners=None</em>, <em class="sig-param">zone=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.compute.WindowsVirtualMachine.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing WindowsVirtualMachine resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>additional_capabilities</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">additional_capabilities</span></code> block as defined below.</p></li>
<li><p><strong>additional_unattend_contents</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">additional_unattend_content</span></code> blocks as defined below. Changing this forces a new resource to be created.</p></li>
<li><p><strong>admin_password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Password which should be used for the local-administrator on this Virtual Machine. Changing this forces a new resource to be created.</p></li>
<li><p><strong>admin_username</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The username of the local administrator used for the Virtual Machine. Changing this forces a new resource to be created.</p></li>
<li><p><strong>allow_extension_operations</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Should Extension Operations be allowed on this Virtual Machine? Changing this forces a new resource to be created.</p></li>
<li><p><strong>availability_set_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the ID of the Availability Set in which the Virtual Machine should exist. Changing this forces a new resource to be created.</p></li>
<li><p><strong>boot_diagnostics</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">boot_diagnostics</span></code> block as defined below.</p></li>
<li><p><strong>computer_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the Hostname which should be used for this Virtual Machine. If unspecified this defaults to the value for the <code class="docutils literal notranslate"><span class="pre">name</span></code> field. Changing this forces a new resource to be created.</p></li>
<li><p><strong>custom_data</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Base64-Encoded Custom Data which should be used for this Virtual Machine. Changing this forces a new resource to be created.</p></li>
<li><p><strong>dedicated_host_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of a Dedicated Host where this machine should be run on. Changing this forces a new resource to be created.</p></li>
<li><p><strong>enable_automatic_updates</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specifies if Automatic Updates are Enabled for the Windows Virtual Machine. Changing this forces a new resource to be created.</p></li>
<li><p><strong>eviction_policy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies what should happen when the Virtual Machine is evicted for price reasons when using a Spot instance. At this time the only supported value is <code class="docutils literal notranslate"><span class="pre">Deallocate</span></code>. Changing this forces a new resource to be created.</p></li>
<li><p><strong>identity</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – An <code class="docutils literal notranslate"><span class="pre">identity</span></code> block as defined below.</p></li>
<li><p><strong>license_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>Specifies the type of on-premise license (also known as <a class="reference external" href="https://docs.microsoft.com/azure/virtual-machines/virtual-machines-windows-hybrid-use-benefit-licensing">Azure Hybrid Use Benefit</a>) which should be used for this Virtual Machine. Possible values are <code class="docutils literal notranslate"><span class="pre">None</span></code>, <code class="docutils literal notranslate"><span class="pre">Windows_Client</span></code> and <code class="docutils literal notranslate"><span class="pre">Windows_Server</span></code>. Changing this forces a new resource to be created.</p>
</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Azure location where the Windows Virtual Machine should exist. Changing this forces a new resource to be created.</p></li>
<li><p><strong>max_bid_price</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The maximum price you’re willing to pay for this Virtual Machine, in US Dollars; which must be greater than the current spot price. If this bid price falls below the current spot price the Virtual Machine will be evicted using the <code class="docutils literal notranslate"><span class="pre">eviction_policy</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">-1</span></code>, which means that the Virtual Machine should not be evicted for price reasons.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Windows Virtual Machine. Changing this forces a new resource to be created.</p></li>
<li><p><strong>network_interface_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – . A list of Network Interface ID’s which should be attached to this Virtual Machine. The first Network Interface ID in this list will be the Primary Network Interface on the Virtual Machine.</p></li>
<li><p><strong>os_disk</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">os_disk</span></code> block as defined below.</p></li>
<li><p><strong>plan</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">plan</span></code> block as defined below. Changing this forces a new resource to be created.</p></li>
<li><p><strong>priority</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the priority of this Virtual Machine. Possible values are <code class="docutils literal notranslate"><span class="pre">Regular</span></code> and <code class="docutils literal notranslate"><span class="pre">Spot</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">Regular</span></code>. Changing this forces a new resource to be created.</p></li>
<li><p><strong>private_ip_address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Primary Private IP Address assigned to this Virtual Machine.</p></li>
<li><p><strong>private_ip_addresses</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of Private IP Addresses assigned to this Virtual Machine.</p></li>
<li><p><strong>provision_vm_agent</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Should the Azure VM Agent be provisioned on this Virtual Machine? Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>. Changing this forces a new resource to be created.</p></li>
<li><p><strong>proximity_placement_group_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Proximity Placement Group which the Virtual Machine should be assigned to. Changing this forces a new resource to be created.</p></li>
<li><p><strong>public_ip_address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Primary Public IP Address assigned to this Virtual Machine.</p></li>
<li><p><strong>public_ip_addresses</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of the Public IP Addresses assigned to this Virtual Machine.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Resource Group in which the Windows Virtual Machine should be exist. Changing this forces a new resource to be created.</p></li>
<li><p><strong>secrets</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">secret</span></code> blocks as defined below.</p></li>
<li><p><strong>size</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The SKU which should be used for this Virtual Machine, such as <code class="docutils literal notranslate"><span class="pre">Standard_F2</span></code>.</p></li>
<li><p><strong>source_image_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Image which this Virtual Machine should be created from. Changing this forces a new resource to be created.</p></li>
<li><p><strong>source_image_reference</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">source_image_reference</span></code> block as defined below. Changing this forces a new resource to be created.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags which should be assigned to this Virtual Machine.</p></li>
<li><p><strong>timezone</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>Specifies the Time Zone which should be used by the Virtual Machine, <a class="reference external" href="https://jackstromberg.com/2017/01/list-of-time-zones-consumed-by-azure/">the possible values are defined here</a>.</p>
</p></li>
<li><p><strong>virtual_machine_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A 128-bit identifier which uniquely identifies this Virtual Machine.</p></li>
<li><p><strong>winrm_listeners</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">winrm_listener</span></code> blocks as defined below.</p></li>
<li><p><strong>zone</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Zone in which this Virtual Machine should be created. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>additional_capabilities</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">ultraSsdEnabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Should the capacity to enable Data Disks of the <code class="docutils literal notranslate"><span class="pre">UltraSSD_LRS</span></code> storage account type be supported on this Virtual Machine? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>. Changing this forces a new resource to be created.</p></li>
</ul>
<p>The <strong>additional_unattend_contents</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">content</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The XML formatted content that is added to the unattend.xml file for the specified path and component. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">setting</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the setting to which the content applies. Possible values are <code class="docutils literal notranslate"><span class="pre">AutoLogon</span></code> and <code class="docutils literal notranslate"><span class="pre">FirstLogonCommands</span></code>. Changing this forces a new resource to be created.</p></li>
</ul>
<p>The <strong>boot_diagnostics</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">storageAccountUri</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Primary/Secondary Endpoint for the Azure Storage Account which should be used to store Boot Diagnostics, including Console Output and Screenshots from the Hypervisor.</p></li>
</ul>
<p>The <strong>identity</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">identityIds</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of User Managed Identity ID’s which should be assigned to the Windows Virtual Machine.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">principal_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the System Managed Service Principal.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The type of Managed Identity which should be assigned to the Windows Virtual Machine. Possible values are <code class="docutils literal notranslate"><span class="pre">SystemAssigned</span></code>, <code class="docutils literal notranslate"><span class="pre">UserAssigned</span></code> and <code class="docutils literal notranslate"><span class="pre">SystemAssigned,</span> <span class="pre">UserAssigned</span></code>.</p></li>
</ul>
<p>The <strong>os_disk</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">caching</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Type of Caching which should be used for the Internal OS Disk. Possible values are <code class="docutils literal notranslate"><span class="pre">None</span></code>, <code class="docutils literal notranslate"><span class="pre">ReadOnly</span></code> and <code class="docutils literal notranslate"><span class="pre">ReadWrite</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">diffDiskSettings</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">diff_disk_settings</span></code> block as defined above.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">option</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the Ephemeral Disk Settings for the OS Disk. At this time the only possible value is <code class="docutils literal notranslate"><span class="pre">Local</span></code>. Changing this forces a new resource to be created.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">disk_encryption_set_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Disk Encryption Set which should be used to Encrypt this OS Disk.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">disk_size_gb</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The Size of the Internal OS Disk in GB, if you wish to vary from the size used in the image this Virtual Machine is sourced from.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name which should be used for the Internal OS Disk. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">storage_account_type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Type of Storage Account which should back this the Internal OS Disk. Possible values are <code class="docutils literal notranslate"><span class="pre">Standard_LRS</span></code>, <code class="docutils literal notranslate"><span class="pre">StandardSSD_LRS</span></code> and <code class="docutils literal notranslate"><span class="pre">Premium_LRS</span></code>. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">write_accelerator_enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Should Write Accelerator be Enabled for this OS Disk? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
</ul>
<p>The <strong>plan</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the Name of the Marketplace Image this Virtual Machine should be created from. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">product</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the Product of the Marketplace Image this Virtual Machine should be created from. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">publisher</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the Publisher of the Marketplace Image this Virtual Machine should be created from. Changing this forces a new resource to be created.</p></li>
</ul>
<p>The <strong>secrets</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">certificates</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - One or more <code class="docutils literal notranslate"><span class="pre">certificate</span></code> blocks as defined above.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">store</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The certificate store on the Virtual Machine where the certificate should be added.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">url</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Secret URL of a Key Vault Certificate.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">key_vault_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Key Vault from which all Secrets should be sourced.</p></li>
</ul>
<p>The <strong>source_image_reference</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">offer</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">publisher</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the Publisher of the Marketplace Image this Virtual Machine should be created from. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sku</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">version</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>winrm_listeners</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">certificateUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Secret URL of a Key Vault Certificate, which must be specified when <code class="docutils literal notranslate"><span class="pre">protocol</span></code> is set to <code class="docutils literal notranslate"><span class="pre">Https</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">protocol</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.compute.WindowsVirtualMachine.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.compute.WindowsVirtualMachine.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.compute.WindowsVirtualMachine.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.compute.WindowsVirtualMachine.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.compute.WindowsVirtualMachineScaleSet">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.compute.</code><code class="sig-name descname">WindowsVirtualMachineScaleSet</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">additional_capabilities=None</em>, <em class="sig-param">additional_unattend_contents=None</em>, <em class="sig-param">admin_password=None</em>, <em class="sig-param">admin_username=None</em>, <em class="sig-param">automatic_instance_repair=None</em>, <em class="sig-param">automatic_os_upgrade_policy=None</em>, <em class="sig-param">boot_diagnostics=None</em>, <em class="sig-param">computer_name_prefix=None</em>, <em class="sig-param">custom_data=None</em>, <em class="sig-param">data_disks=None</em>, <em class="sig-param">do_not_run_extensions_on_overprovisioned_machines=None</em>, <em class="sig-param">enable_automatic_updates=None</em>, <em class="sig-param">eviction_policy=None</em>, <em class="sig-param">health_probe_id=None</em>, <em class="sig-param">identity=None</em>, <em class="sig-param">instances=None</em>, <em class="sig-param">license_type=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">max_bid_price=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">network_interfaces=None</em>, <em class="sig-param">os_disk=None</em>, <em class="sig-param">overprovision=None</em>, <em class="sig-param">plan=None</em>, <em class="sig-param">priority=None</em>, <em class="sig-param">provision_vm_agent=None</em>, <em class="sig-param">proximity_placement_group_id=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">rolling_upgrade_policy=None</em>, <em class="sig-param">scale_in_policy=None</em>, <em class="sig-param">secrets=None</em>, <em class="sig-param">single_placement_group=None</em>, <em class="sig-param">sku=None</em>, <em class="sig-param">source_image_id=None</em>, <em class="sig-param">source_image_reference=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">terminate_notification=None</em>, <em class="sig-param">timezone=None</em>, <em class="sig-param">upgrade_mode=None</em>, <em class="sig-param">winrm_listeners=None</em>, <em class="sig-param">zone_balance=None</em>, <em class="sig-param">zones=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.compute.WindowsVirtualMachineScaleSet" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Windows Virtual Machine Scale Set.</p>
<blockquote>
<div><p><strong>Note</strong> This provider will automatically update &amp; reimage the nodes in the Scale Set (if Required) during an Update - this behaviour can be configured using the <code class="docutils literal notranslate"><span class="pre">features</span></code> configuration within the Provider configuration block.</p>
<p><strong>Note:</strong> This resource does not support Unmanaged Disks. If you need to use Unmanaged Disks you can continue to use the <code class="docutils literal notranslate"><span class="pre">compute.ScaleSet</span></code> resource instead</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>additional_capabilities</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">additional_capabilities</span></code> block as defined below.</p></li>
<li><p><strong>additional_unattend_contents</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">additional_unattend_content</span></code> blocks as defined below.</p></li>
<li><p><strong>admin_password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Password which should be used for the local-administrator on this Virtual Machine. Changing this forces a new resource to be created.</p></li>
<li><p><strong>admin_username</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The username of the local administrator on each Virtual Machine Scale Set instance. Changing this forces a new resource to be created.</p></li>
<li><p><strong>automatic_instance_repair</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – <p>A <code class="docutils literal notranslate"><span class="pre">automatic_instance_repair</span></code> block as defined below. To enable the automatic instance repair, this Virtual Machine Scale Set must have a valid <code class="docutils literal notranslate"><span class="pre">health_probe_id</span></code> or an <a class="reference external" href="https://docs.microsoft.com/en-us/azure/virtual-machine-scale-sets/virtual-machine-scale-sets-health-extension">Application Health Extension</a>.</p>
</p></li>
<li><p><strong>automatic_os_upgrade_policy</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">automatic_os_upgrade_policy</span></code> block as defined below. This is Required and can only be specified when <code class="docutils literal notranslate"><span class="pre">upgrade_mode</span></code> is set to <code class="docutils literal notranslate"><span class="pre">Automatic</span></code>.</p></li>
<li><p><strong>boot_diagnostics</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">boot_diagnostics</span></code> block as defined below.</p></li>
<li><p><strong>computer_name_prefix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The prefix which should be used for the name of the Virtual Machines in this Scale Set. If unspecified this defaults to the value for the <code class="docutils literal notranslate"><span class="pre">name</span></code> field.</p></li>
<li><p><strong>custom_data</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Base64-Encoded Custom Data which should be used for this Virtual Machine Scale Set.</p></li>
<li><p><strong>data_disks</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">data_disk</span></code> blocks as defined below.</p></li>
<li><p><strong>do_not_run_extensions_on_overprovisioned_machines</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Should Virtual Machine Extensions be run on Overprovisioned Virtual Machines in the Scale Set? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>enable_automatic_updates</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Are automatic updates enabled for this Virtual Machine? Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>eviction_policy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Policy which should be used Virtual Machines are Evicted from the Scale Set. Changing this forces a new resource to be created.</p></li>
<li><p><strong>health_probe_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of a Load Balancer Probe which should be used to determine the health of an instance. Changing this forces a new resource to be created. This is Required and can only be specified when <code class="docutils literal notranslate"><span class="pre">upgrade_mode</span></code> is set to <code class="docutils literal notranslate"><span class="pre">Automatic</span></code> or <code class="docutils literal notranslate"><span class="pre">Rolling</span></code>.</p></li>
<li><p><strong>identity</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">identity</span></code> block as defined below.</p></li>
<li><p><strong>instances</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The number of Virtual Machines in the Scale Set.</p></li>
<li><p><strong>license_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>Specifies the type of on-premise license (also known as <a class="reference external" href="https://docs.microsoft.com/azure/virtual-machines/virtual-machines-windows-hybrid-use-benefit-licensing">Azure Hybrid Use Benefit</a>) which should be used for this Virtual Machine Scale Set. Possible values are <code class="docutils literal notranslate"><span class="pre">None</span></code>, <code class="docutils literal notranslate"><span class="pre">Windows_Client</span></code> and <code class="docutils literal notranslate"><span class="pre">Windows_Server</span></code>. Changing this forces a new resource to be created.</p>
</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Azure location where the Windows Virtual Machine Scale Set should exist. Changing this forces a new resource to be created.</p></li>
<li><p><strong>max_bid_price</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The maximum price you’re willing to pay for each Virtual Machine in this Scale Set, in US Dollars; which must be greater than the current spot price. If this bid price falls below the current spot price the Virtual Machines in the Scale Set will be evicted using the <code class="docutils literal notranslate"><span class="pre">eviction_policy</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">-1</span></code>, which means that each Virtual Machine in the Scale Set should not be evicted for price reasons.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Windows Virtual Machine Scale Set. Changing this forces a new resource to be created.</p></li>
<li><p><strong>network_interfaces</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">network_interface</span></code> blocks as defined below.</p></li>
<li><p><strong>os_disk</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – An <code class="docutils literal notranslate"><span class="pre">os_disk</span></code> block as defined below.</p></li>
<li><p><strong>overprovision</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Should Azure over-provision Virtual Machines in this Scale Set? This means that multiple Virtual Machines will be provisioned and Azure will keep the instances which become available first - which improves provisioning success rates and improves deployment time. You’re not billed for these over-provisioned VM’s and they don’t count towards the Subscription Quota. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>priority</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Priority of this Virtual Machine Scale Set. Possible values are <code class="docutils literal notranslate"><span class="pre">Regular</span></code> and <code class="docutils literal notranslate"><span class="pre">Spot</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">Regular</span></code>. Changing this value forces a new resource.</p></li>
<li><p><strong>provision_vm_agent</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Should the Azure VM Agent be provisioned on each Virtual Machine in the Scale Set? Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>. Changing this value forces a new resource to be created.</p></li>
<li><p><strong>proximity_placement_group_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Proximity Placement Group in which the Virtual Machine Scale Set should be assigned to. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Resource Group in which the Windows Virtual Machine Scale Set should be exist. Changing this forces a new resource to be created.</p></li>
<li><p><strong>rolling_upgrade_policy</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">rolling_upgrade_policy</span></code> block as defined below. This is Required and can only be specified when <code class="docutils literal notranslate"><span class="pre">upgrade_mode</span></code> is set to <code class="docutils literal notranslate"><span class="pre">Automatic</span></code> or <code class="docutils literal notranslate"><span class="pre">Rolling</span></code>.</p></li>
<li><p><strong>scale_in_policy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The scale-in policy rule that decides which virtual machines are chosen for removal when a Virtual Machine Scale Set is scaled in. Possible values for the scale-in policy rules are <code class="docutils literal notranslate"><span class="pre">Default</span></code>, <code class="docutils literal notranslate"><span class="pre">NewestVM</span></code> and <code class="docutils literal notranslate"><span class="pre">OldestVM</span></code>, defaults to <code class="docutils literal notranslate"><span class="pre">Default</span></code>. For more information about scale in policy, please <a class="reference external" href="https://docs.microsoft.com/en-us/azure/virtual-machine-scale-sets/virtual-machine-scale-sets-scale-in-policy">refer to this doc</a>.</p>
</p></li>
<li><p><strong>secrets</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">secret</span></code> blocks as defined below.</p></li>
<li><p><strong>single_placement_group</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Should this Virtual Machine Scale Set be limited to a Single Placement Group, which means the number of instances will be capped at 100 Virtual Machines. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>sku</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Virtual Machine SKU for the Scale Set, such as <code class="docutils literal notranslate"><span class="pre">Standard_F2</span></code>.</p></li>
<li><p><strong>source_image_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of an Image which each Virtual Machine in this Scale Set should be based on.</p></li>
<li><p><strong>source_image_reference</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">source_image_reference</span></code> block as defined below.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags which should be assigned to this Virtual Machine Scale Set.</p></li>
<li><p><strong>terminate_notification</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">terminate_notification</span></code> block as defined below.</p></li>
<li><p><strong>timezone</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>Specifies the time zone of the virtual machine, <a class="reference external" href="https://jackstromberg.com/2017/01/list-of-time-zones-consumed-by-azure/">the possible values are defined here</a>.</p>
</p></li>
<li><p><strong>upgrade_mode</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies how Upgrades (e.g. changing the Image/SKU) should be performed to Virtual Machine Instances. Possible values are <code class="docutils literal notranslate"><span class="pre">Automatic</span></code>, <code class="docutils literal notranslate"><span class="pre">Manual</span></code> and <code class="docutils literal notranslate"><span class="pre">Rolling</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">Manual</span></code>.</p></li>
<li><p><strong>winrm_listeners</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">winrm_listener</span></code> blocks as defined below.</p></li>
<li><p><strong>zone_balance</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Should the Virtual Machines in this Scale Set be strictly evenly distributed across Availability Zones? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>. Changing this forces a new resource to be created.</p></li>
<li><p><strong>zones</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of Availability Zones in which the Virtual Machines in this Scale Set should be created in. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>additional_capabilities</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">ultraSsdEnabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Should the capacity to enable Data Disks of the <code class="docutils literal notranslate"><span class="pre">UltraSSD_LRS</span></code> storage account type be supported on this Virtual Machine Scale Set? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>. Changing this forces a new resource to be created.</p></li>
</ul>
<p>The <strong>additional_unattend_contents</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">content</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The XML formatted content that is added to the unattend.xml file for the specified path and component. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">setting</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the setting to which the content applies. Possible values are <code class="docutils literal notranslate"><span class="pre">AutoLogon</span></code> and <code class="docutils literal notranslate"><span class="pre">FirstLogonCommands</span></code>. Changing this forces a new resource to be created.</p></li>
</ul>
<p>The <strong>automatic_instance_repair</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Should the automatic instance repair be enabled on this Virtual Machine Scale Set?</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">gracePeriod</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Amount of time (in minutes, between 30 and 90, defaults to 30 minutes) for which automatic repairs will be delayed. The grace period starts right after the VM is found unhealthy. The time duration should be specified in ISO 8601 format.</p></li>
</ul>
<p>The <strong>automatic_os_upgrade_policy</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">disableAutomaticRollback</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Should automatic rollbacks be disabled? Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enableAutomaticOsUpgrade</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Should OS Upgrades automatically be applied to Scale Set instances in a rolling fashion when a newer version of the OS Image becomes available? Changing this forces a new resource to be created.</p></li>
</ul>
<p>The <strong>boot_diagnostics</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">storageAccountUri</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Primary/Secondary Endpoint for the Azure Storage Account which should be used to store Boot Diagnostics, including Console Output and Screenshots from the Hypervisor.</p></li>
</ul>
<p>The <strong>data_disks</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">caching</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The type of Caching which should be used for this Data Disk. Possible values are <code class="docutils literal notranslate"><span class="pre">None</span></code>, <code class="docutils literal notranslate"><span class="pre">ReadOnly</span></code> and <code class="docutils literal notranslate"><span class="pre">ReadWrite</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">disk_encryption_set_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Disk Encryption Set which should be used to encrypt this Data Disk.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">disk_size_gb</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The size of the Data Disk which should be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">lun</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The Logical Unit Number of the Data Disk, which must be unique within the Virtual Machine.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">storage_account_type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Type of Storage Account which should back this Data Disk. Possible values include <code class="docutils literal notranslate"><span class="pre">Standard_LRS</span></code>, <code class="docutils literal notranslate"><span class="pre">StandardSSD_LRS</span></code>, <code class="docutils literal notranslate"><span class="pre">Premium_LRS</span></code> and <code class="docutils literal notranslate"><span class="pre">UltraSSD_LRS</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">write_accelerator_enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Should Write Accelerator be enabled for this Data Disk? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
</ul>
<p>The <strong>identity</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">identityIds</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of User Managed Identity ID’s which should be assigned to the Windows Virtual Machine Scale Set.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">principal_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the System Managed Service Principal.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The type of Managed Identity which should be assigned to the Windows Virtual Machine Scale Set. Possible values are <code class="docutils literal notranslate"><span class="pre">SystemAssigned</span></code>, <code class="docutils literal notranslate"><span class="pre">UserAssigned</span></code> and <code class="docutils literal notranslate"><span class="pre">SystemAssigned,</span> <span class="pre">UserAssigned</span></code>.</p></li>
</ul>
<p>The <strong>network_interfaces</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">dns_servers</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of IP Addresses of DNS Servers which should be assigned to the Network Interface.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enable_accelerated_networking</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Does this Network Interface support Accelerated Networking? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enable_ip_forwarding</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Does this Network Interface support IP Forwarding? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ip_configurations</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - One or more <code class="docutils literal notranslate"><span class="pre">ip_configuration</span></code> blocks as defined above.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">applicationGatewayBackendAddressPoolIds</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of Backend Address Pools ID’s from a Application Gateway which this Virtual Machine Scale Set should be connected to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">applicationSecurityGroupIds</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of Application Security Group ID’s which this Virtual Machine Scale Set should be connected to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">loadBalancerBackendAddressPoolIds</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of Backend Address Pools ID’s from a Load Balancer which this Virtual Machine Scale Set should be connected to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">loadBalancerInboundNatRulesIds</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of NAT Rule ID’s from a Load Balancer which this Virtual Machine Scale Set should be connected to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Name which should be used for this IP Configuration.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">primary</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Is this the Primary IP Configuration for this Network Interface? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">public_ip_addresses</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">public_ip_address</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">domain_name_label</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Prefix which should be used for the Domain Name Label for each Virtual Machine Instance. Azure concatenates the Domain Name Label and Virtual Machine Index to create a unique Domain Name Label for each Virtual Machine.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">idle_timeout_in_minutes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The Idle Timeout in Minutes for the Public IP Address. Possible values are in the range <code class="docutils literal notranslate"><span class="pre">4</span></code> to <code class="docutils literal notranslate"><span class="pre">32</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ipTags</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - One or more <code class="docutils literal notranslate"><span class="pre">ip_tag</span></code> blocks as defined above.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">tag</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The IP Tag associated with the Public IP, such as <code class="docutils literal notranslate"><span class="pre">SQL</span></code> or <code class="docutils literal notranslate"><span class="pre">Storage</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Type of IP Tag, such as <code class="docutils literal notranslate"><span class="pre">FirstPartyUsage</span></code>.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Name of the Public IP Address Configuration.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">public_ip_prefix_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Public IP Address Prefix from where Public IP Addresses should be allocated. Changing this forces a new resource to be created.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnet_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Subnet which this IP Configuration should be connected to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">version</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Internet Protocol Version which should be used for this IP Configuration. Possible values are <code class="docutils literal notranslate"><span class="pre">IPv4</span></code> and <code class="docutils literal notranslate"><span class="pre">IPv6</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">IPv4</span></code>.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Name which should be used for this Network Interface. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">network_security_group_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of a Network Security Group which should be assigned to this Network Interface.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">primary</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Is this the Primary IP Configuration?</p></li>
</ul>
<p>The <strong>os_disk</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">caching</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Type of Caching which should be used for the Internal OS Disk. Possible values are <code class="docutils literal notranslate"><span class="pre">None</span></code>, <code class="docutils literal notranslate"><span class="pre">ReadOnly</span></code> and <code class="docutils literal notranslate"><span class="pre">ReadWrite</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">diffDiskSettings</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">diff_disk_settings</span></code> block as defined above. Changing this forces a new resource to be created.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">option</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">disk_encryption_set_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Disk Encryption Set which should be used to encrypt this OS Disk.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">disk_size_gb</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The Size of the Internal OS Disk in GB, if you wish to vary from the size used in the image this Virtual Machine Scale Set is sourced from.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">storage_account_type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Type of Storage Account which should back this the Internal OS Disk. Possible values include <code class="docutils literal notranslate"><span class="pre">Standard_LRS</span></code>, <code class="docutils literal notranslate"><span class="pre">StandardSSD_LRS</span></code> and <code class="docutils literal notranslate"><span class="pre">Premium_LRS</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">write_accelerator_enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Should Write Accelerator be Enabled for this OS Disk? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
</ul>
<p>The <strong>plan</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the Windows Virtual Machine Scale Set. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">product</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">publisher</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>rolling_upgrade_policy</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">maxBatchInstancePercent</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The maximum percent of total virtual machine instances that will be upgraded simultaneously by the rolling upgrade in one batch. As this is a maximum, unhealthy instances in previous or future batches can cause the percentage of instances in a batch to decrease to ensure higher reliability. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxUnhealthyInstancePercent</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The maximum percentage of the total virtual machine instances in the scale set that can be simultaneously unhealthy, either as a result of being upgraded, or by being found in an unhealthy state by the virtual machine health checks before the rolling upgrade aborts. This constraint will be checked prior to starting any batch. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxUnhealthyUpgradedInstancePercent</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The maximum percentage of upgraded virtual machine instances that can be found to be in an unhealthy state. This check will happen after each batch is upgraded. If this percentage is ever exceeded, the rolling update aborts. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">pauseTimeBetweenBatches</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The wait time between completing the update for all virtual machines in one batch and starting the next batch. The time duration should be specified in ISO 8601 format. Changing this forces a new resource to be created.</p></li>
</ul>
<p>The <strong>secrets</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">certificates</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - One or more <code class="docutils literal notranslate"><span class="pre">certificate</span></code> blocks as defined above.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">store</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The certificate store on the Virtual Machine where the certificate should be added.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">url</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Secret URL of a Key Vault Certificate.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">key_vault_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Key Vault from which all Secrets should be sourced.</p></li>
</ul>
<p>The <strong>source_image_reference</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">offer</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">publisher</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sku</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Virtual Machine SKU for the Scale Set, such as <code class="docutils literal notranslate"><span class="pre">Standard_F2</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">version</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Internet Protocol Version which should be used for this IP Configuration. Possible values are <code class="docutils literal notranslate"><span class="pre">IPv4</span></code> and <code class="docutils literal notranslate"><span class="pre">IPv6</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">IPv4</span></code>.</p></li>
</ul>
<p>The <strong>terminate_notification</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Should the terminate notification be enabled on this Virtual Machine Scale Set? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timeout</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Length of time (in minutes, between 5 and 15) a notification to be sent to the VM on the instance metadata server till the VM gets deleted. The time duration should be specified in ISO 8601 format.</p></li>
</ul>
<p>The <strong>winrm_listeners</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">certificateUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Secret URL of a Key Vault Certificate, which must be specified when <code class="docutils literal notranslate"><span class="pre">protocol</span></code> is set to <code class="docutils literal notranslate"><span class="pre">Https</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">protocol</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Protocol of the WinRM Listener. Possible values are <code class="docutils literal notranslate"><span class="pre">Http</span></code> and <code class="docutils literal notranslate"><span class="pre">Https</span></code>.</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_azure.compute.WindowsVirtualMachineScaleSet.additional_capabilities">
<code class="sig-name descname">additional_capabilities</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.WindowsVirtualMachineScaleSet.additional_capabilities" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">additional_capabilities</span></code> block as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">ultraSsdEnabled</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Should the capacity to enable Data Disks of the <code class="docutils literal notranslate"><span class="pre">UltraSSD_LRS</span></code> storage account type be supported on this Virtual Machine Scale Set? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>. Changing this forces a new resource to be created.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.WindowsVirtualMachineScaleSet.additional_unattend_contents">
<code class="sig-name descname">additional_unattend_contents</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.WindowsVirtualMachineScaleSet.additional_unattend_contents" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more <code class="docutils literal notranslate"><span class="pre">additional_unattend_content</span></code> blocks as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">content</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The XML formatted content that is added to the unattend.xml file for the specified path and component. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">setting</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the setting to which the content applies. Possible values are <code class="docutils literal notranslate"><span class="pre">AutoLogon</span></code> and <code class="docutils literal notranslate"><span class="pre">FirstLogonCommands</span></code>. Changing this forces a new resource to be created.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.WindowsVirtualMachineScaleSet.admin_password">
<code class="sig-name descname">admin_password</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.WindowsVirtualMachineScaleSet.admin_password" title="Permalink to this definition">¶</a></dt>
<dd><p>The Password which should be used for the local-administrator on this Virtual Machine. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.WindowsVirtualMachineScaleSet.admin_username">
<code class="sig-name descname">admin_username</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.WindowsVirtualMachineScaleSet.admin_username" title="Permalink to this definition">¶</a></dt>
<dd><p>The username of the local administrator on each Virtual Machine Scale Set instance. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.WindowsVirtualMachineScaleSet.automatic_instance_repair">
<code class="sig-name descname">automatic_instance_repair</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.WindowsVirtualMachineScaleSet.automatic_instance_repair" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">automatic_instance_repair</span></code> block as defined below. To enable the automatic instance repair, this Virtual Machine Scale Set must have a valid <code class="docutils literal notranslate"><span class="pre">health_probe_id</span></code> or an <a class="reference external" href="https://docs.microsoft.com/en-us/azure/virtual-machine-scale-sets/virtual-machine-scale-sets-health-extension">Application Health Extension</a>.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Should the automatic instance repair be enabled on this Virtual Machine Scale Set?</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">gracePeriod</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Amount of time (in minutes, between 30 and 90, defaults to 30 minutes) for which automatic repairs will be delayed. The grace period starts right after the VM is found unhealthy. The time duration should be specified in ISO 8601 format.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.WindowsVirtualMachineScaleSet.automatic_os_upgrade_policy">
<code class="sig-name descname">automatic_os_upgrade_policy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.WindowsVirtualMachineScaleSet.automatic_os_upgrade_policy" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">automatic_os_upgrade_policy</span></code> block as defined below. This is Required and can only be specified when <code class="docutils literal notranslate"><span class="pre">upgrade_mode</span></code> is set to <code class="docutils literal notranslate"><span class="pre">Automatic</span></code>.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">disableAutomaticRollback</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Should automatic rollbacks be disabled? Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enableAutomaticOsUpgrade</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Should OS Upgrades automatically be applied to Scale Set instances in a rolling fashion when a newer version of the OS Image becomes available? Changing this forces a new resource to be created.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.WindowsVirtualMachineScaleSet.boot_diagnostics">
<code class="sig-name descname">boot_diagnostics</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.WindowsVirtualMachineScaleSet.boot_diagnostics" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">boot_diagnostics</span></code> block as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">storageAccountUri</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Primary/Secondary Endpoint for the Azure Storage Account which should be used to store Boot Diagnostics, including Console Output and Screenshots from the Hypervisor.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.WindowsVirtualMachineScaleSet.computer_name_prefix">
<code class="sig-name descname">computer_name_prefix</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.WindowsVirtualMachineScaleSet.computer_name_prefix" title="Permalink to this definition">¶</a></dt>
<dd><p>The prefix which should be used for the name of the Virtual Machines in this Scale Set. If unspecified this defaults to the value for the <code class="docutils literal notranslate"><span class="pre">name</span></code> field.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.WindowsVirtualMachineScaleSet.custom_data">
<code class="sig-name descname">custom_data</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.WindowsVirtualMachineScaleSet.custom_data" title="Permalink to this definition">¶</a></dt>
<dd><p>The Base64-Encoded Custom Data which should be used for this Virtual Machine Scale Set.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.WindowsVirtualMachineScaleSet.data_disks">
<code class="sig-name descname">data_disks</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.WindowsVirtualMachineScaleSet.data_disks" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more <code class="docutils literal notranslate"><span class="pre">data_disk</span></code> blocks as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">caching</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The type of Caching which should be used for this Data Disk. Possible values are <code class="docutils literal notranslate"><span class="pre">None</span></code>, <code class="docutils literal notranslate"><span class="pre">ReadOnly</span></code> and <code class="docutils literal notranslate"><span class="pre">ReadWrite</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">disk_encryption_set_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the Disk Encryption Set which should be used to encrypt this Data Disk.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">disk_size_gb</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The size of the Data Disk which should be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">lun</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The Logical Unit Number of the Data Disk, which must be unique within the Virtual Machine.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">storage_account_type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Type of Storage Account which should back this Data Disk. Possible values include <code class="docutils literal notranslate"><span class="pre">Standard_LRS</span></code>, <code class="docutils literal notranslate"><span class="pre">StandardSSD_LRS</span></code>, <code class="docutils literal notranslate"><span class="pre">Premium_LRS</span></code> and <code class="docutils literal notranslate"><span class="pre">UltraSSD_LRS</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">write_accelerator_enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Should Write Accelerator be enabled for this Data Disk? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.WindowsVirtualMachineScaleSet.do_not_run_extensions_on_overprovisioned_machines">
<code class="sig-name descname">do_not_run_extensions_on_overprovisioned_machines</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.WindowsVirtualMachineScaleSet.do_not_run_extensions_on_overprovisioned_machines" title="Permalink to this definition">¶</a></dt>
<dd><p>Should Virtual Machine Extensions be run on Overprovisioned Virtual Machines in the Scale Set? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.WindowsVirtualMachineScaleSet.enable_automatic_updates">
<code class="sig-name descname">enable_automatic_updates</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.WindowsVirtualMachineScaleSet.enable_automatic_updates" title="Permalink to this definition">¶</a></dt>
<dd><p>Are automatic updates enabled for this Virtual Machine? Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.WindowsVirtualMachineScaleSet.eviction_policy">
<code class="sig-name descname">eviction_policy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.WindowsVirtualMachineScaleSet.eviction_policy" title="Permalink to this definition">¶</a></dt>
<dd><p>The Policy which should be used Virtual Machines are Evicted from the Scale Set. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.WindowsVirtualMachineScaleSet.health_probe_id">
<code class="sig-name descname">health_probe_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.WindowsVirtualMachineScaleSet.health_probe_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of a Load Balancer Probe which should be used to determine the health of an instance. Changing this forces a new resource to be created. This is Required and can only be specified when <code class="docutils literal notranslate"><span class="pre">upgrade_mode</span></code> is set to <code class="docutils literal notranslate"><span class="pre">Automatic</span></code> or <code class="docutils literal notranslate"><span class="pre">Rolling</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.WindowsVirtualMachineScaleSet.identity">
<code class="sig-name descname">identity</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.WindowsVirtualMachineScaleSet.identity" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">identity</span></code> block as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">identityIds</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - A list of User Managed Identity ID’s which should be assigned to the Windows Virtual Machine Scale Set.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">principal_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the System Managed Service Principal.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The type of Managed Identity which should be assigned to the Windows Virtual Machine Scale Set. Possible values are <code class="docutils literal notranslate"><span class="pre">SystemAssigned</span></code>, <code class="docutils literal notranslate"><span class="pre">UserAssigned</span></code> and <code class="docutils literal notranslate"><span class="pre">SystemAssigned,</span> <span class="pre">UserAssigned</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.WindowsVirtualMachineScaleSet.instances">
<code class="sig-name descname">instances</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.WindowsVirtualMachineScaleSet.instances" title="Permalink to this definition">¶</a></dt>
<dd><p>The number of Virtual Machines in the Scale Set.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.WindowsVirtualMachineScaleSet.license_type">
<code class="sig-name descname">license_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.WindowsVirtualMachineScaleSet.license_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the type of on-premise license (also known as <a class="reference external" href="https://docs.microsoft.com/azure/virtual-machines/virtual-machines-windows-hybrid-use-benefit-licensing">Azure Hybrid Use Benefit</a>) which should be used for this Virtual Machine Scale Set. Possible values are <code class="docutils literal notranslate"><span class="pre">None</span></code>, <code class="docutils literal notranslate"><span class="pre">Windows_Client</span></code> and <code class="docutils literal notranslate"><span class="pre">Windows_Server</span></code>. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.WindowsVirtualMachineScaleSet.location">
<code class="sig-name descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.WindowsVirtualMachineScaleSet.location" title="Permalink to this definition">¶</a></dt>
<dd><p>The Azure location where the Windows Virtual Machine Scale Set should exist. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.WindowsVirtualMachineScaleSet.max_bid_price">
<code class="sig-name descname">max_bid_price</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.WindowsVirtualMachineScaleSet.max_bid_price" title="Permalink to this definition">¶</a></dt>
<dd><p>The maximum price you’re willing to pay for each Virtual Machine in this Scale Set, in US Dollars; which must be greater than the current spot price. If this bid price falls below the current spot price the Virtual Machines in the Scale Set will be evicted using the <code class="docutils literal notranslate"><span class="pre">eviction_policy</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">-1</span></code>, which means that each Virtual Machine in the Scale Set should not be evicted for price reasons.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.WindowsVirtualMachineScaleSet.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.WindowsVirtualMachineScaleSet.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Windows Virtual Machine Scale Set. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.WindowsVirtualMachineScaleSet.network_interfaces">
<code class="sig-name descname">network_interfaces</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.WindowsVirtualMachineScaleSet.network_interfaces" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more <code class="docutils literal notranslate"><span class="pre">network_interface</span></code> blocks as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">dns_servers</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - A list of IP Addresses of DNS Servers which should be assigned to the Network Interface.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enable_accelerated_networking</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Does this Network Interface support Accelerated Networking? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enable_ip_forwarding</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Does this Network Interface support IP Forwarding? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ip_configurations</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - One or more <code class="docutils literal notranslate"><span class="pre">ip_configuration</span></code> blocks as defined above.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">applicationGatewayBackendAddressPoolIds</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - A list of Backend Address Pools ID’s from a Application Gateway which this Virtual Machine Scale Set should be connected to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">applicationSecurityGroupIds</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - A list of Application Security Group ID’s which this Virtual Machine Scale Set should be connected to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">loadBalancerBackendAddressPoolIds</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - A list of Backend Address Pools ID’s from a Load Balancer which this Virtual Machine Scale Set should be connected to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">loadBalancerInboundNatRulesIds</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - A list of NAT Rule ID’s from a Load Balancer which this Virtual Machine Scale Set should be connected to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Name which should be used for this IP Configuration.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">primary</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Is this the Primary IP Configuration for this Network Interface? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">public_ip_addresses</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - A <code class="docutils literal notranslate"><span class="pre">public_ip_address</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">domain_name_label</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Prefix which should be used for the Domain Name Label for each Virtual Machine Instance. Azure concatenates the Domain Name Label and Virtual Machine Index to create a unique Domain Name Label for each Virtual Machine.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">idle_timeout_in_minutes</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The Idle Timeout in Minutes for the Public IP Address. Possible values are in the range <code class="docutils literal notranslate"><span class="pre">4</span></code> to <code class="docutils literal notranslate"><span class="pre">32</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ipTags</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - One or more <code class="docutils literal notranslate"><span class="pre">ip_tag</span></code> blocks as defined above.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">tag</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The IP Tag associated with the Public IP, such as <code class="docutils literal notranslate"><span class="pre">SQL</span></code> or <code class="docutils literal notranslate"><span class="pre">Storage</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Type of IP Tag, such as <code class="docutils literal notranslate"><span class="pre">FirstPartyUsage</span></code>.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Name of the Public IP Address Configuration.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">public_ip_prefix_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the Public IP Address Prefix from where Public IP Addresses should be allocated. Changing this forces a new resource to be created.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnet_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the Subnet which this IP Configuration should be connected to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">version</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Internet Protocol Version which should be used for this IP Configuration. Possible values are <code class="docutils literal notranslate"><span class="pre">IPv4</span></code> and <code class="docutils literal notranslate"><span class="pre">IPv6</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">IPv4</span></code>.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Name which should be used for this Network Interface. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">network_security_group_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of a Network Security Group which should be assigned to this Network Interface.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">primary</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Is this the Primary IP Configuration?</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.WindowsVirtualMachineScaleSet.os_disk">
<code class="sig-name descname">os_disk</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.WindowsVirtualMachineScaleSet.os_disk" title="Permalink to this definition">¶</a></dt>
<dd><p>An <code class="docutils literal notranslate"><span class="pre">os_disk</span></code> block as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">caching</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Type of Caching which should be used for the Internal OS Disk. Possible values are <code class="docutils literal notranslate"><span class="pre">None</span></code>, <code class="docutils literal notranslate"><span class="pre">ReadOnly</span></code> and <code class="docutils literal notranslate"><span class="pre">ReadWrite</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">diffDiskSettings</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - A <code class="docutils literal notranslate"><span class="pre">diff_disk_settings</span></code> block as defined above. Changing this forces a new resource to be created.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">option</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">disk_encryption_set_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the Disk Encryption Set which should be used to encrypt this OS Disk.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">disk_size_gb</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The Size of the Internal OS Disk in GB, if you wish to vary from the size used in the image this Virtual Machine Scale Set is sourced from.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">storage_account_type</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Type of Storage Account which should back this the Internal OS Disk. Possible values include <code class="docutils literal notranslate"><span class="pre">Standard_LRS</span></code>, <code class="docutils literal notranslate"><span class="pre">StandardSSD_LRS</span></code> and <code class="docutils literal notranslate"><span class="pre">Premium_LRS</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">write_accelerator_enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Should Write Accelerator be Enabled for this OS Disk? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.WindowsVirtualMachineScaleSet.overprovision">
<code class="sig-name descname">overprovision</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.WindowsVirtualMachineScaleSet.overprovision" title="Permalink to this definition">¶</a></dt>
<dd><p>Should Azure over-provision Virtual Machines in this Scale Set? This means that multiple Virtual Machines will be provisioned and Azure will keep the instances which become available first - which improves provisioning success rates and improves deployment time. You’re not billed for these over-provisioned VM’s and they don’t count towards the Subscription Quota. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.WindowsVirtualMachineScaleSet.priority">
<code class="sig-name descname">priority</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.WindowsVirtualMachineScaleSet.priority" title="Permalink to this definition">¶</a></dt>
<dd><p>The Priority of this Virtual Machine Scale Set. Possible values are <code class="docutils literal notranslate"><span class="pre">Regular</span></code> and <code class="docutils literal notranslate"><span class="pre">Spot</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">Regular</span></code>. Changing this value forces a new resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.WindowsVirtualMachineScaleSet.provision_vm_agent">
<code class="sig-name descname">provision_vm_agent</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.WindowsVirtualMachineScaleSet.provision_vm_agent" title="Permalink to this definition">¶</a></dt>
<dd><p>Should the Azure VM Agent be provisioned on each Virtual Machine in the Scale Set? Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>. Changing this value forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.WindowsVirtualMachineScaleSet.proximity_placement_group_id">
<code class="sig-name descname">proximity_placement_group_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.WindowsVirtualMachineScaleSet.proximity_placement_group_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Proximity Placement Group in which the Virtual Machine Scale Set should be assigned to. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.WindowsVirtualMachineScaleSet.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.WindowsVirtualMachineScaleSet.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Resource Group in which the Windows Virtual Machine Scale Set should be exist. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.WindowsVirtualMachineScaleSet.rolling_upgrade_policy">
<code class="sig-name descname">rolling_upgrade_policy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.WindowsVirtualMachineScaleSet.rolling_upgrade_policy" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">rolling_upgrade_policy</span></code> block as defined below. This is Required and can only be specified when <code class="docutils literal notranslate"><span class="pre">upgrade_mode</span></code> is set to <code class="docutils literal notranslate"><span class="pre">Automatic</span></code> or <code class="docutils literal notranslate"><span class="pre">Rolling</span></code>.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">maxBatchInstancePercent</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The maximum percent of total virtual machine instances that will be upgraded simultaneously by the rolling upgrade in one batch. As this is a maximum, unhealthy instances in previous or future batches can cause the percentage of instances in a batch to decrease to ensure higher reliability. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxUnhealthyInstancePercent</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The maximum percentage of the total virtual machine instances in the scale set that can be simultaneously unhealthy, either as a result of being upgraded, or by being found in an unhealthy state by the virtual machine health checks before the rolling upgrade aborts. This constraint will be checked prior to starting any batch. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxUnhealthyUpgradedInstancePercent</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The maximum percentage of upgraded virtual machine instances that can be found to be in an unhealthy state. This check will happen after each batch is upgraded. If this percentage is ever exceeded, the rolling update aborts. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">pauseTimeBetweenBatches</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The wait time between completing the update for all virtual machines in one batch and starting the next batch. The time duration should be specified in ISO 8601 format. Changing this forces a new resource to be created.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.WindowsVirtualMachineScaleSet.scale_in_policy">
<code class="sig-name descname">scale_in_policy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.WindowsVirtualMachineScaleSet.scale_in_policy" title="Permalink to this definition">¶</a></dt>
<dd><p>The scale-in policy rule that decides which virtual machines are chosen for removal when a Virtual Machine Scale Set is scaled in. Possible values for the scale-in policy rules are <code class="docutils literal notranslate"><span class="pre">Default</span></code>, <code class="docutils literal notranslate"><span class="pre">NewestVM</span></code> and <code class="docutils literal notranslate"><span class="pre">OldestVM</span></code>, defaults to <code class="docutils literal notranslate"><span class="pre">Default</span></code>. For more information about scale in policy, please <a class="reference external" href="https://docs.microsoft.com/en-us/azure/virtual-machine-scale-sets/virtual-machine-scale-sets-scale-in-policy">refer to this doc</a>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.WindowsVirtualMachineScaleSet.secrets">
<code class="sig-name descname">secrets</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.WindowsVirtualMachineScaleSet.secrets" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more <code class="docutils literal notranslate"><span class="pre">secret</span></code> blocks as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">certificates</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - One or more <code class="docutils literal notranslate"><span class="pre">certificate</span></code> blocks as defined above.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">store</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The certificate store on the Virtual Machine where the certificate should be added.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">url</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Secret URL of a Key Vault Certificate.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">key_vault_id</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the Key Vault from which all Secrets should be sourced.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.WindowsVirtualMachineScaleSet.single_placement_group">
<code class="sig-name descname">single_placement_group</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.WindowsVirtualMachineScaleSet.single_placement_group" title="Permalink to this definition">¶</a></dt>
<dd><p>Should this Virtual Machine Scale Set be limited to a Single Placement Group, which means the number of instances will be capped at 100 Virtual Machines. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.WindowsVirtualMachineScaleSet.sku">
<code class="sig-name descname">sku</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.WindowsVirtualMachineScaleSet.sku" title="Permalink to this definition">¶</a></dt>
<dd><p>The Virtual Machine SKU for the Scale Set, such as <code class="docutils literal notranslate"><span class="pre">Standard_F2</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.WindowsVirtualMachineScaleSet.source_image_id">
<code class="sig-name descname">source_image_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.WindowsVirtualMachineScaleSet.source_image_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of an Image which each Virtual Machine in this Scale Set should be based on.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.WindowsVirtualMachineScaleSet.source_image_reference">
<code class="sig-name descname">source_image_reference</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.WindowsVirtualMachineScaleSet.source_image_reference" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">source_image_reference</span></code> block as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">offer</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">publisher</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sku</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Virtual Machine SKU for the Scale Set, such as <code class="docutils literal notranslate"><span class="pre">Standard_F2</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">version</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Internet Protocol Version which should be used for this IP Configuration. Possible values are <code class="docutils literal notranslate"><span class="pre">IPv4</span></code> and <code class="docutils literal notranslate"><span class="pre">IPv6</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">IPv4</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.WindowsVirtualMachineScaleSet.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.WindowsVirtualMachineScaleSet.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags which should be assigned to this Virtual Machine Scale Set.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.WindowsVirtualMachineScaleSet.terminate_notification">
<code class="sig-name descname">terminate_notification</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.WindowsVirtualMachineScaleSet.terminate_notification" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">terminate_notification</span></code> block as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Should the terminate notification be enabled on this Virtual Machine Scale Set? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timeout</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Length of time (in minutes, between 5 and 15) a notification to be sent to the VM on the instance metadata server till the VM gets deleted. The time duration should be specified in ISO 8601 format.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.WindowsVirtualMachineScaleSet.timezone">
<code class="sig-name descname">timezone</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.WindowsVirtualMachineScaleSet.timezone" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the time zone of the virtual machine, <a class="reference external" href="https://jackstromberg.com/2017/01/list-of-time-zones-consumed-by-azure/">the possible values are defined here</a>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.WindowsVirtualMachineScaleSet.unique_id">
<code class="sig-name descname">unique_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.WindowsVirtualMachineScaleSet.unique_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The Unique ID for this Windows Virtual Machine Scale Set.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.WindowsVirtualMachineScaleSet.upgrade_mode">
<code class="sig-name descname">upgrade_mode</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.WindowsVirtualMachineScaleSet.upgrade_mode" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies how Upgrades (e.g. changing the Image/SKU) should be performed to Virtual Machine Instances. Possible values are <code class="docutils literal notranslate"><span class="pre">Automatic</span></code>, <code class="docutils literal notranslate"><span class="pre">Manual</span></code> and <code class="docutils literal notranslate"><span class="pre">Rolling</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">Manual</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.WindowsVirtualMachineScaleSet.winrm_listeners">
<code class="sig-name descname">winrm_listeners</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.WindowsVirtualMachineScaleSet.winrm_listeners" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more <code class="docutils literal notranslate"><span class="pre">winrm_listener</span></code> blocks as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">certificateUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Secret URL of a Key Vault Certificate, which must be specified when <code class="docutils literal notranslate"><span class="pre">protocol</span></code> is set to <code class="docutils literal notranslate"><span class="pre">Https</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">protocol</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The Protocol of the WinRM Listener. Possible values are <code class="docutils literal notranslate"><span class="pre">Http</span></code> and <code class="docutils literal notranslate"><span class="pre">Https</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.WindowsVirtualMachineScaleSet.zone_balance">
<code class="sig-name descname">zone_balance</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.WindowsVirtualMachineScaleSet.zone_balance" title="Permalink to this definition">¶</a></dt>
<dd><p>Should the Virtual Machines in this Scale Set be strictly evenly distributed across Availability Zones? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.compute.WindowsVirtualMachineScaleSet.zones">
<code class="sig-name descname">zones</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.compute.WindowsVirtualMachineScaleSet.zones" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of Availability Zones in which the Virtual Machines in this Scale Set should be created in. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.compute.WindowsVirtualMachineScaleSet.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">additional_capabilities=None</em>, <em class="sig-param">additional_unattend_contents=None</em>, <em class="sig-param">admin_password=None</em>, <em class="sig-param">admin_username=None</em>, <em class="sig-param">automatic_instance_repair=None</em>, <em class="sig-param">automatic_os_upgrade_policy=None</em>, <em class="sig-param">boot_diagnostics=None</em>, <em class="sig-param">computer_name_prefix=None</em>, <em class="sig-param">custom_data=None</em>, <em class="sig-param">data_disks=None</em>, <em class="sig-param">do_not_run_extensions_on_overprovisioned_machines=None</em>, <em class="sig-param">enable_automatic_updates=None</em>, <em class="sig-param">eviction_policy=None</em>, <em class="sig-param">health_probe_id=None</em>, <em class="sig-param">identity=None</em>, <em class="sig-param">instances=None</em>, <em class="sig-param">license_type=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">max_bid_price=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">network_interfaces=None</em>, <em class="sig-param">os_disk=None</em>, <em class="sig-param">overprovision=None</em>, <em class="sig-param">plan=None</em>, <em class="sig-param">priority=None</em>, <em class="sig-param">provision_vm_agent=None</em>, <em class="sig-param">proximity_placement_group_id=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">rolling_upgrade_policy=None</em>, <em class="sig-param">scale_in_policy=None</em>, <em class="sig-param">secrets=None</em>, <em class="sig-param">single_placement_group=None</em>, <em class="sig-param">sku=None</em>, <em class="sig-param">source_image_id=None</em>, <em class="sig-param">source_image_reference=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">terminate_notification=None</em>, <em class="sig-param">timezone=None</em>, <em class="sig-param">unique_id=None</em>, <em class="sig-param">upgrade_mode=None</em>, <em class="sig-param">winrm_listeners=None</em>, <em class="sig-param">zone_balance=None</em>, <em class="sig-param">zones=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.compute.WindowsVirtualMachineScaleSet.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing WindowsVirtualMachineScaleSet resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>additional_capabilities</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">additional_capabilities</span></code> block as defined below.</p></li>
<li><p><strong>additional_unattend_contents</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">additional_unattend_content</span></code> blocks as defined below.</p></li>
<li><p><strong>admin_password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Password which should be used for the local-administrator on this Virtual Machine. Changing this forces a new resource to be created.</p></li>
<li><p><strong>admin_username</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The username of the local administrator on each Virtual Machine Scale Set instance. Changing this forces a new resource to be created.</p></li>
<li><p><strong>automatic_instance_repair</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – <p>A <code class="docutils literal notranslate"><span class="pre">automatic_instance_repair</span></code> block as defined below. To enable the automatic instance repair, this Virtual Machine Scale Set must have a valid <code class="docutils literal notranslate"><span class="pre">health_probe_id</span></code> or an <a class="reference external" href="https://docs.microsoft.com/en-us/azure/virtual-machine-scale-sets/virtual-machine-scale-sets-health-extension">Application Health Extension</a>.</p>
</p></li>
<li><p><strong>automatic_os_upgrade_policy</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">automatic_os_upgrade_policy</span></code> block as defined below. This is Required and can only be specified when <code class="docutils literal notranslate"><span class="pre">upgrade_mode</span></code> is set to <code class="docutils literal notranslate"><span class="pre">Automatic</span></code>.</p></li>
<li><p><strong>boot_diagnostics</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">boot_diagnostics</span></code> block as defined below.</p></li>
<li><p><strong>computer_name_prefix</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The prefix which should be used for the name of the Virtual Machines in this Scale Set. If unspecified this defaults to the value for the <code class="docutils literal notranslate"><span class="pre">name</span></code> field.</p></li>
<li><p><strong>custom_data</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Base64-Encoded Custom Data which should be used for this Virtual Machine Scale Set.</p></li>
<li><p><strong>data_disks</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">data_disk</span></code> blocks as defined below.</p></li>
<li><p><strong>do_not_run_extensions_on_overprovisioned_machines</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Should Virtual Machine Extensions be run on Overprovisioned Virtual Machines in the Scale Set? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>enable_automatic_updates</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Are automatic updates enabled for this Virtual Machine? Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>eviction_policy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Policy which should be used Virtual Machines are Evicted from the Scale Set. Changing this forces a new resource to be created.</p></li>
<li><p><strong>health_probe_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of a Load Balancer Probe which should be used to determine the health of an instance. Changing this forces a new resource to be created. This is Required and can only be specified when <code class="docutils literal notranslate"><span class="pre">upgrade_mode</span></code> is set to <code class="docutils literal notranslate"><span class="pre">Automatic</span></code> or <code class="docutils literal notranslate"><span class="pre">Rolling</span></code>.</p></li>
<li><p><strong>identity</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">identity</span></code> block as defined below.</p></li>
<li><p><strong>instances</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The number of Virtual Machines in the Scale Set.</p></li>
<li><p><strong>license_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>Specifies the type of on-premise license (also known as <a class="reference external" href="https://docs.microsoft.com/azure/virtual-machines/virtual-machines-windows-hybrid-use-benefit-licensing">Azure Hybrid Use Benefit</a>) which should be used for this Virtual Machine Scale Set. Possible values are <code class="docutils literal notranslate"><span class="pre">None</span></code>, <code class="docutils literal notranslate"><span class="pre">Windows_Client</span></code> and <code class="docutils literal notranslate"><span class="pre">Windows_Server</span></code>. Changing this forces a new resource to be created.</p>
</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Azure location where the Windows Virtual Machine Scale Set should exist. Changing this forces a new resource to be created.</p></li>
<li><p><strong>max_bid_price</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The maximum price you’re willing to pay for each Virtual Machine in this Scale Set, in US Dollars; which must be greater than the current spot price. If this bid price falls below the current spot price the Virtual Machines in the Scale Set will be evicted using the <code class="docutils literal notranslate"><span class="pre">eviction_policy</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">-1</span></code>, which means that each Virtual Machine in the Scale Set should not be evicted for price reasons.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Windows Virtual Machine Scale Set. Changing this forces a new resource to be created.</p></li>
<li><p><strong>network_interfaces</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">network_interface</span></code> blocks as defined below.</p></li>
<li><p><strong>os_disk</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – An <code class="docutils literal notranslate"><span class="pre">os_disk</span></code> block as defined below.</p></li>
<li><p><strong>overprovision</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Should Azure over-provision Virtual Machines in this Scale Set? This means that multiple Virtual Machines will be provisioned and Azure will keep the instances which become available first - which improves provisioning success rates and improves deployment time. You’re not billed for these over-provisioned VM’s and they don’t count towards the Subscription Quota. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>priority</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Priority of this Virtual Machine Scale Set. Possible values are <code class="docutils literal notranslate"><span class="pre">Regular</span></code> and <code class="docutils literal notranslate"><span class="pre">Spot</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">Regular</span></code>. Changing this value forces a new resource.</p></li>
<li><p><strong>provision_vm_agent</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Should the Azure VM Agent be provisioned on each Virtual Machine in the Scale Set? Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>. Changing this value forces a new resource to be created.</p></li>
<li><p><strong>proximity_placement_group_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Proximity Placement Group in which the Virtual Machine Scale Set should be assigned to. Changing this forces a new resource to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Resource Group in which the Windows Virtual Machine Scale Set should be exist. Changing this forces a new resource to be created.</p></li>
<li><p><strong>rolling_upgrade_policy</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">rolling_upgrade_policy</span></code> block as defined below. This is Required and can only be specified when <code class="docutils literal notranslate"><span class="pre">upgrade_mode</span></code> is set to <code class="docutils literal notranslate"><span class="pre">Automatic</span></code> or <code class="docutils literal notranslate"><span class="pre">Rolling</span></code>.</p></li>
<li><p><strong>scale_in_policy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The scale-in policy rule that decides which virtual machines are chosen for removal when a Virtual Machine Scale Set is scaled in. Possible values for the scale-in policy rules are <code class="docutils literal notranslate"><span class="pre">Default</span></code>, <code class="docutils literal notranslate"><span class="pre">NewestVM</span></code> and <code class="docutils literal notranslate"><span class="pre">OldestVM</span></code>, defaults to <code class="docutils literal notranslate"><span class="pre">Default</span></code>. For more information about scale in policy, please <a class="reference external" href="https://docs.microsoft.com/en-us/azure/virtual-machine-scale-sets/virtual-machine-scale-sets-scale-in-policy">refer to this doc</a>.</p>
</p></li>
<li><p><strong>secrets</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">secret</span></code> blocks as defined below.</p></li>
<li><p><strong>single_placement_group</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Should this Virtual Machine Scale Set be limited to a Single Placement Group, which means the number of instances will be capped at 100 Virtual Machines. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>sku</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Virtual Machine SKU for the Scale Set, such as <code class="docutils literal notranslate"><span class="pre">Standard_F2</span></code>.</p></li>
<li><p><strong>source_image_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of an Image which each Virtual Machine in this Scale Set should be based on.</p></li>
<li><p><strong>source_image_reference</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">source_image_reference</span></code> block as defined below.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags which should be assigned to this Virtual Machine Scale Set.</p></li>
<li><p><strong>terminate_notification</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">terminate_notification</span></code> block as defined below.</p></li>
<li><p><strong>timezone</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>Specifies the time zone of the virtual machine, <a class="reference external" href="https://jackstromberg.com/2017/01/list-of-time-zones-consumed-by-azure/">the possible values are defined here</a>.</p>
</p></li>
<li><p><strong>unique_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Unique ID for this Windows Virtual Machine Scale Set.</p></li>
<li><p><strong>upgrade_mode</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies how Upgrades (e.g. changing the Image/SKU) should be performed to Virtual Machine Instances. Possible values are <code class="docutils literal notranslate"><span class="pre">Automatic</span></code>, <code class="docutils literal notranslate"><span class="pre">Manual</span></code> and <code class="docutils literal notranslate"><span class="pre">Rolling</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">Manual</span></code>.</p></li>
<li><p><strong>winrm_listeners</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">winrm_listener</span></code> blocks as defined below.</p></li>
<li><p><strong>zone_balance</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Should the Virtual Machines in this Scale Set be strictly evenly distributed across Availability Zones? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>. Changing this forces a new resource to be created.</p></li>
<li><p><strong>zones</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of Availability Zones in which the Virtual Machines in this Scale Set should be created in. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>additional_capabilities</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">ultraSsdEnabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Should the capacity to enable Data Disks of the <code class="docutils literal notranslate"><span class="pre">UltraSSD_LRS</span></code> storage account type be supported on this Virtual Machine Scale Set? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>. Changing this forces a new resource to be created.</p></li>
</ul>
<p>The <strong>additional_unattend_contents</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">content</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The XML formatted content that is added to the unattend.xml file for the specified path and component. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">setting</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the setting to which the content applies. Possible values are <code class="docutils literal notranslate"><span class="pre">AutoLogon</span></code> and <code class="docutils literal notranslate"><span class="pre">FirstLogonCommands</span></code>. Changing this forces a new resource to be created.</p></li>
</ul>
<p>The <strong>automatic_instance_repair</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Should the automatic instance repair be enabled on this Virtual Machine Scale Set?</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">gracePeriod</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Amount of time (in minutes, between 30 and 90, defaults to 30 minutes) for which automatic repairs will be delayed. The grace period starts right after the VM is found unhealthy. The time duration should be specified in ISO 8601 format.</p></li>
</ul>
<p>The <strong>automatic_os_upgrade_policy</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">disableAutomaticRollback</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Should automatic rollbacks be disabled? Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enableAutomaticOsUpgrade</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Should OS Upgrades automatically be applied to Scale Set instances in a rolling fashion when a newer version of the OS Image becomes available? Changing this forces a new resource to be created.</p></li>
</ul>
<p>The <strong>boot_diagnostics</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">storageAccountUri</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Primary/Secondary Endpoint for the Azure Storage Account which should be used to store Boot Diagnostics, including Console Output and Screenshots from the Hypervisor.</p></li>
</ul>
<p>The <strong>data_disks</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">caching</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The type of Caching which should be used for this Data Disk. Possible values are <code class="docutils literal notranslate"><span class="pre">None</span></code>, <code class="docutils literal notranslate"><span class="pre">ReadOnly</span></code> and <code class="docutils literal notranslate"><span class="pre">ReadWrite</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">disk_encryption_set_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Disk Encryption Set which should be used to encrypt this Data Disk.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">disk_size_gb</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The size of the Data Disk which should be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">lun</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The Logical Unit Number of the Data Disk, which must be unique within the Virtual Machine.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">storage_account_type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Type of Storage Account which should back this Data Disk. Possible values include <code class="docutils literal notranslate"><span class="pre">Standard_LRS</span></code>, <code class="docutils literal notranslate"><span class="pre">StandardSSD_LRS</span></code>, <code class="docutils literal notranslate"><span class="pre">Premium_LRS</span></code> and <code class="docutils literal notranslate"><span class="pre">UltraSSD_LRS</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">write_accelerator_enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Should Write Accelerator be enabled for this Data Disk? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
</ul>
<p>The <strong>identity</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">identityIds</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of User Managed Identity ID’s which should be assigned to the Windows Virtual Machine Scale Set.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">principal_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the System Managed Service Principal.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The type of Managed Identity which should be assigned to the Windows Virtual Machine Scale Set. Possible values are <code class="docutils literal notranslate"><span class="pre">SystemAssigned</span></code>, <code class="docutils literal notranslate"><span class="pre">UserAssigned</span></code> and <code class="docutils literal notranslate"><span class="pre">SystemAssigned,</span> <span class="pre">UserAssigned</span></code>.</p></li>
</ul>
<p>The <strong>network_interfaces</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">dns_servers</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of IP Addresses of DNS Servers which should be assigned to the Network Interface.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enable_accelerated_networking</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Does this Network Interface support Accelerated Networking? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enable_ip_forwarding</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Does this Network Interface support IP Forwarding? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ip_configurations</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - One or more <code class="docutils literal notranslate"><span class="pre">ip_configuration</span></code> blocks as defined above.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">applicationGatewayBackendAddressPoolIds</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of Backend Address Pools ID’s from a Application Gateway which this Virtual Machine Scale Set should be connected to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">applicationSecurityGroupIds</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of Application Security Group ID’s which this Virtual Machine Scale Set should be connected to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">loadBalancerBackendAddressPoolIds</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of Backend Address Pools ID’s from a Load Balancer which this Virtual Machine Scale Set should be connected to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">loadBalancerInboundNatRulesIds</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A list of NAT Rule ID’s from a Load Balancer which this Virtual Machine Scale Set should be connected to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Name which should be used for this IP Configuration.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">primary</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Is this the Primary IP Configuration for this Network Interface? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">public_ip_addresses</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">public_ip_address</span></code> block as defined below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">domain_name_label</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Prefix which should be used for the Domain Name Label for each Virtual Machine Instance. Azure concatenates the Domain Name Label and Virtual Machine Index to create a unique Domain Name Label for each Virtual Machine.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">idle_timeout_in_minutes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The Idle Timeout in Minutes for the Public IP Address. Possible values are in the range <code class="docutils literal notranslate"><span class="pre">4</span></code> to <code class="docutils literal notranslate"><span class="pre">32</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ipTags</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - One or more <code class="docutils literal notranslate"><span class="pre">ip_tag</span></code> blocks as defined above.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">tag</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The IP Tag associated with the Public IP, such as <code class="docutils literal notranslate"><span class="pre">SQL</span></code> or <code class="docutils literal notranslate"><span class="pre">Storage</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Type of IP Tag, such as <code class="docutils literal notranslate"><span class="pre">FirstPartyUsage</span></code>.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Name of the Public IP Address Configuration.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">public_ip_prefix_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Public IP Address Prefix from where Public IP Addresses should be allocated. Changing this forces a new resource to be created.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">subnet_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Subnet which this IP Configuration should be connected to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">version</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Internet Protocol Version which should be used for this IP Configuration. Possible values are <code class="docutils literal notranslate"><span class="pre">IPv4</span></code> and <code class="docutils literal notranslate"><span class="pre">IPv6</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">IPv4</span></code>.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Name which should be used for this Network Interface. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">network_security_group_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of a Network Security Group which should be assigned to this Network Interface.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">primary</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Is this the Primary IP Configuration?</p></li>
</ul>
<p>The <strong>os_disk</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">caching</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Type of Caching which should be used for the Internal OS Disk. Possible values are <code class="docutils literal notranslate"><span class="pre">None</span></code>, <code class="docutils literal notranslate"><span class="pre">ReadOnly</span></code> and <code class="docutils literal notranslate"><span class="pre">ReadWrite</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">diffDiskSettings</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A <code class="docutils literal notranslate"><span class="pre">diff_disk_settings</span></code> block as defined above. Changing this forces a new resource to be created.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">option</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">disk_encryption_set_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Disk Encryption Set which should be used to encrypt this OS Disk.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">disk_size_gb</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The Size of the Internal OS Disk in GB, if you wish to vary from the size used in the image this Virtual Machine Scale Set is sourced from.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">storage_account_type</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Type of Storage Account which should back this the Internal OS Disk. Possible values include <code class="docutils literal notranslate"><span class="pre">Standard_LRS</span></code>, <code class="docutils literal notranslate"><span class="pre">StandardSSD_LRS</span></code> and <code class="docutils literal notranslate"><span class="pre">Premium_LRS</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">write_accelerator_enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Should Write Accelerator be Enabled for this OS Disk? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
</ul>
<p>The <strong>plan</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the Windows Virtual Machine Scale Set. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">product</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">publisher</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>rolling_upgrade_policy</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">maxBatchInstancePercent</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The maximum percent of total virtual machine instances that will be upgraded simultaneously by the rolling upgrade in one batch. As this is a maximum, unhealthy instances in previous or future batches can cause the percentage of instances in a batch to decrease to ensure higher reliability. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxUnhealthyInstancePercent</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The maximum percentage of the total virtual machine instances in the scale set that can be simultaneously unhealthy, either as a result of being upgraded, or by being found in an unhealthy state by the virtual machine health checks before the rolling upgrade aborts. This constraint will be checked prior to starting any batch. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxUnhealthyUpgradedInstancePercent</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The maximum percentage of upgraded virtual machine instances that can be found to be in an unhealthy state. This check will happen after each batch is upgraded. If this percentage is ever exceeded, the rolling update aborts. Changing this forces a new resource to be created.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">pauseTimeBetweenBatches</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The wait time between completing the update for all virtual machines in one batch and starting the next batch. The time duration should be specified in ISO 8601 format. Changing this forces a new resource to be created.</p></li>
</ul>
<p>The <strong>secrets</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">certificates</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - One or more <code class="docutils literal notranslate"><span class="pre">certificate</span></code> blocks as defined above.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">store</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The certificate store on the Virtual Machine where the certificate should be added.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">url</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Secret URL of a Key Vault Certificate.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">key_vault_id</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the Key Vault from which all Secrets should be sourced.</p></li>
</ul>
<p>The <strong>source_image_reference</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">offer</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">publisher</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sku</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Virtual Machine SKU for the Scale Set, such as <code class="docutils literal notranslate"><span class="pre">Standard_F2</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">version</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Internet Protocol Version which should be used for this IP Configuration. Possible values are <code class="docutils literal notranslate"><span class="pre">IPv4</span></code> and <code class="docutils literal notranslate"><span class="pre">IPv6</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">IPv4</span></code>.</p></li>
</ul>
<p>The <strong>terminate_notification</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Should the terminate notification be enabled on this Virtual Machine Scale Set? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timeout</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Length of time (in minutes, between 5 and 15) a notification to be sent to the VM on the instance metadata server till the VM gets deleted. The time duration should be specified in ISO 8601 format.</p></li>
</ul>
<p>The <strong>winrm_listeners</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">certificateUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Secret URL of a Key Vault Certificate, which must be specified when <code class="docutils literal notranslate"><span class="pre">protocol</span></code> is set to <code class="docutils literal notranslate"><span class="pre">Https</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">protocol</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The Protocol of the WinRM Listener. Possible values are <code class="docutils literal notranslate"><span class="pre">Http</span></code> and <code class="docutils literal notranslate"><span class="pre">Https</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.compute.WindowsVirtualMachineScaleSet.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.compute.WindowsVirtualMachineScaleSet.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.compute.WindowsVirtualMachineScaleSet.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.compute.WindowsVirtualMachineScaleSet.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>name</strong> (<em>str</em>) – The name of the Availability Set.</p></li>
<li><p><strong>resource_group_name</strong> (<em>str</em>) – The name of the resource group in which the Availability Set exists.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="function">
<dt id="pulumi_azure.compute.get_dedicated_host">
<code class="sig-prename descclassname">pulumi_azure.compute.</code><code class="sig-name descname">get_dedicated_host</code><span class="sig-paren">(</span><em class="sig-param">dedicated_host_group_name=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.compute.get_dedicated_host" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing Dedicated Host.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>dedicated_host_group_name</strong> (<em>str</em>) – Specifies the name of the Dedicated Host Group the Dedicated Host is located in.</p></li>
<li><p><strong>name</strong> (<em>str</em>) – Specifies the name of the Dedicated Host.</p></li>
<li><p><strong>resource_group_name</strong> (<em>str</em>) – Specifies the name of the resource group the Dedicated Host is located in.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="function">
<dt id="pulumi_azure.compute.get_dedicated_host_group">
<code class="sig-prename descclassname">pulumi_azure.compute.</code><code class="sig-name descname">get_dedicated_host_group</code><span class="sig-paren">(</span><em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.compute.get_dedicated_host_group" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing Dedicated Host Group.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>name</strong> (<em>str</em>) – Specifies the name of the Dedicated Host Group.</p></li>
<li><p><strong>resource_group_name</strong> (<em>str</em>) – Specifies the name of the resource group the Dedicated Host Group is located in.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="function">
<dt id="pulumi_azure.compute.get_disk_encryption_set">
<code class="sig-prename descclassname">pulumi_azure.compute.</code><code class="sig-name descname">get_disk_encryption_set</code><span class="sig-paren">(</span><em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.compute.get_disk_encryption_set" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing Disk Encryption Set.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>name</strong> (<em>str</em>) – The name of the Disk Encryption Set exists.</p></li>
<li><p><strong>resource_group_name</strong> (<em>str</em>) – The name of the Resource Group where the Disk Encryption Set exists.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="function">
<dt id="pulumi_azure.compute.get_image">
<code class="sig-prename descclassname">pulumi_azure.compute.</code><code class="sig-name descname">get_image</code><span class="sig-paren">(</span><em class="sig-param">name=None</em>, <em class="sig-param">name_regex=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">sort_descending=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.compute.get_image" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing Image.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>name</strong> (<em>str</em>) – The name of the Image.</p></li>
<li><p><strong>name_regex</strong> (<em>str</em>) – Regex pattern of the image to match.</p></li>
<li><p><strong>resource_group_name</strong> (<em>str</em>) – The Name of the Resource Group where this Image exists.</p></li>
<li><p><strong>sort_descending</strong> (<em>bool</em>) – By default when matching by regex, images are sorted by name in ascending order and the first match is chosen, to sort descending, set this flag.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="function">
<dt id="pulumi_azure.compute.get_managed_disk">
<code class="sig-prename descclassname">pulumi_azure.compute.</code><code class="sig-name descname">get_managed_disk</code><span class="sig-paren">(</span><em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">tags=None</em>, <em class="sig-param">zones=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.compute.get_managed_disk" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing Managed Disk.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>name</strong> (<em>str</em>) – Specifies the name of the Managed Disk.</p></li>
<li><p><strong>resource_group_name</strong> (<em>str</em>) – Specifies the name of the Resource Group where this Managed Disk exists.</p></li>
<li><p><strong>tags</strong> (<em>dict</em>) – A mapping of tags assigned to the resource.</p></li>
<li><p><strong>zones</strong> (<em>list</em>) – A list of Availability Zones where the Managed Disk exists.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="function">
<dt id="pulumi_azure.compute.get_platform_image">
<code class="sig-prename descclassname">pulumi_azure.compute.</code><code class="sig-name descname">get_platform_image</code><span class="sig-paren">(</span><em class="sig-param">location=None</em>, <em class="sig-param">offer=None</em>, <em class="sig-param">publisher=None</em>, <em class="sig-param">sku=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.compute.get_platform_image" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about a Platform Image.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>location</strong> (<em>str</em>) – Specifies the Location to pull information about this Platform Image from.</p></li>
<li><p><strong>offer</strong> (<em>str</em>) – Specifies the Offer associated with the Platform Image.</p></li>
<li><p><strong>publisher</strong> (<em>str</em>) – Specifies the Publisher associated with the Platform Image.</p></li>
<li><p><strong>sku</strong> (<em>str</em>) – Specifies the SKU of the Platform Image.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="function">
<dt id="pulumi_azure.compute.get_shared_image">
<code class="sig-prename descclassname">pulumi_azure.compute.</code><code class="sig-name descname">get_shared_image</code><span class="sig-paren">(</span><em class="sig-param">gallery_name=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.compute.get_shared_image" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing Shared Image within a Shared Image Gallery.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>gallery_name</strong> (<em>str</em>) – The name of the Shared Image Gallery in which the Shared Image exists.</p></li>
<li><p><strong>name</strong> (<em>str</em>) – The name of the Shared Image.</p></li>
<li><p><strong>resource_group_name</strong> (<em>str</em>) – The name of the Resource Group in which the Shared Image Gallery exists.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="function">
<dt id="pulumi_azure.compute.get_shared_image_gallery">
<code class="sig-prename descclassname">pulumi_azure.compute.</code><code class="sig-name descname">get_shared_image_gallery</code><span class="sig-paren">(</span><em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.compute.get_shared_image_gallery" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing Shared Image Gallery.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>name</strong> (<em>str</em>) – The name of the Shared Image Gallery.</p></li>
<li><p><strong>resource_group_name</strong> (<em>str</em>) – The name of the Resource Group in which the Shared Image Gallery exists.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="function">
<dt id="pulumi_azure.compute.get_shared_image_version">
<code class="sig-prename descclassname">pulumi_azure.compute.</code><code class="sig-name descname">get_shared_image_version</code><span class="sig-paren">(</span><em class="sig-param">gallery_name=None</em>, <em class="sig-param">image_name=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.compute.get_shared_image_version" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing Version of a Shared Image within a Shared Image Gallery.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>gallery_name</strong> (<em>str</em>) – The name of the Shared Image in which the Shared Image exists.</p></li>
<li><p><strong>image_name</strong> (<em>str</em>) – The name of the Shared Image in which this Version exists.</p></li>
<li><p><strong>name</strong> (<em>str</em>) – The name of the Image Version.</p></li>
<li><p><strong>resource_group_name</strong> (<em>str</em>) – The name of the Resource Group in which the Shared Image Gallery exists.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="function">
<dt id="pulumi_azure.compute.get_snapshot">
<code class="sig-prename descclassname">pulumi_azure.compute.</code><code class="sig-name descname">get_snapshot</code><span class="sig-paren">(</span><em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.compute.get_snapshot" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing Snapshot.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>name</strong> (<em>str</em>) – Specifies the name of the Snapshot.</p></li>
<li><p><strong>resource_group_name</strong> (<em>str</em>) – Specifies the name of the resource group the Snapshot is located in.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="function">
<dt id="pulumi_azure.compute.get_virtual_machine">
<code class="sig-prename descclassname">pulumi_azure.compute.</code><code class="sig-name descname">get_virtual_machine</code><span class="sig-paren">(</span><em class="sig-param">name=None</em>, <em class="sig-param">resource_group_name=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.compute.get_virtual_machine" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing Virtual Machine.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>name</strong> (<em>str</em>) – Specifies the name of the Virtual Machine.</p></li>
<li><p><strong>resource_group_name</strong> (<em>str</em>) – Specifies the name of the resource group the Virtual Machine is located in.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

</div>
