<div class="section" id="module-pulumi_azure.batch">
<span id="batch"></span><h1>batch<a class="headerlink" href="#module-pulumi_azure.batch" title="Permalink to this headline">¶</a></h1>
<dl class="class">
<dt id="pulumi_azure.batch.Account">
<em class="property">class </em><code class="descclassname">pulumi_azure.batch.</code><code class="descname">Account</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>location=None</em>, <em>name=None</em>, <em>pool_allocation_mode=None</em>, <em>resource_group_name=None</em>, <em>storage_account_id=None</em>, <em>tags=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.batch.Account" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.batch.Account.resource_group_name">
<code class="descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.batch.Account.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to create the Batch account. Changing this forces a new resource to be created.</p>
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
<dt id="pulumi_azure.batch.GetAccountResult">
<em class="property">class </em><code class="descclassname">pulumi_azure.batch.</code><code class="descname">GetAccountResult</code><span class="sig-paren">(</span><em>location=None</em>, <em>pool_allocation_mode=None</em>, <em>storage_account_id=None</em>, <em>tags=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.batch.GetAccountResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getAccount.</p>
<dl class="attribute">
<dt id="pulumi_azure.batch.GetAccountResult.location">
<code class="descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.batch.GetAccountResult.location" title="Permalink to this definition">¶</a></dt>
<dd><p>The Azure Region in which this Batch account exists.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.batch.GetAccountResult.pool_allocation_mode">
<code class="descname">pool_allocation_mode</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.batch.GetAccountResult.pool_allocation_mode" title="Permalink to this definition">¶</a></dt>
<dd><p>The pool allocation mode configured for this Batch account.</p>
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
<dt id="pulumi_azure.batch.GetPoolResult">
<em class="property">class </em><code class="descclassname">pulumi_azure.batch.</code><code class="descname">GetPoolResult</code><span class="sig-paren">(</span><em>auto_scales=None</em>, <em>display_name=None</em>, <em>fixed_scales=None</em>, <em>max_tasks_per_node=None</em>, <em>node_agent_sku_id=None</em>, <em>storage_image_references=None</em>, <em>vm_size=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.batch.GetPoolResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getPool.</p>
<dl class="attribute">
<dt id="pulumi_azure.batch.GetPoolResult.auto_scales">
<code class="descname">auto_scales</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.batch.GetPoolResult.auto_scales" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">auto_scale</span></code> block that describes the scale settings when using auto scale.</p>
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
<dt id="pulumi_azure.batch.GetPoolResult.node_agent_sku_id">
<code class="descname">node_agent_sku_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.batch.GetPoolResult.node_agent_sku_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The Sku of the node agents in the Batch pool.</p>
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
<em class="property">class </em><code class="descclassname">pulumi_azure.batch.</code><code class="descname">Pool</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>account_name=None</em>, <em>auto_scale=None</em>, <em>display_name=None</em>, <em>fixed_scale=None</em>, <em>max_tasks_per_node=None</em>, <em>name=None</em>, <em>node_agent_sku_id=None</em>, <em>resource_group_name=None</em>, <em>start_task=None</em>, <em>stop_pending_resize_operation=None</em>, <em>storage_image_reference=None</em>, <em>vm_size=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.batch.Pool" title="Permalink to this definition">¶</a></dt>
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
<li><strong>display_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the display name of the Batch pool.</li>
<li><strong>fixed_scale</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">fixed_scale</span></code> block that describes the scale settings when using fixed scale.</li>
<li><strong>max_tasks_per_node</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Specifies the maximum number of tasks that can run concurrently on a single compute node in the pool. Defaults to <code class="docutils literal notranslate"><span class="pre">1</span></code>.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Batch pool. Changing this forces a new resource to be created.</li>
<li><strong>node_agent_sku_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the Sku of the node agents that will be created in the Batch pool.</li>
<li><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the Batch pool. Changing this forces a new resource to be created.</li>
<li><strong>start_task</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">start_task</span></code> block that describes the start task settings for the Batch pool.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<p>:param pulumi.Input[bool] stop_pending_resize_operation
:param pulumi.Input[dict] storage_image_reference: A <code class="docutils literal notranslate"><span class="pre">storage_image_reference</span></code> for the virtual machines that will compose the Batch pool.
:param pulumi.Input[str] vm_size: Specifies the size of the VM created in the Batch pool.</p>
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
<dd><p>Specifies the maximum number of tasks that can run concurrently on a single compute node in the pool. Defaults to <code class="docutils literal notranslate"><span class="pre">1</span></code>.</p>
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
<code class="descclassname">pulumi_azure.batch.</code><code class="descname">get_account</code><span class="sig-paren">(</span><em>name=None</em>, <em>resource_group_name=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.batch.get_account" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing Batch Account.</p>
</dd></dl>

<dl class="function">
<dt id="pulumi_azure.batch.get_pool">
<code class="descclassname">pulumi_azure.batch.</code><code class="descname">get_pool</code><span class="sig-paren">(</span><em>account_name=None</em>, <em>name=None</em>, <em>resource_group_name=None</em>, <em>start_task=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.batch.get_pool" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing Batch pool</p>
</dd></dl>

</div>
