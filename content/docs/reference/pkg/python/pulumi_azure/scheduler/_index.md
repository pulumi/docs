---
---

<div class="section" id="scheduler">
<h1>scheduler<a class="headerlink" href="#scheduler" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azure">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-azure/issues">pulumi/pulumi-azure repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azure/issues">terraform-providers/terraform-provider-azure repo</a>.</div></blockquote>
<span class="target" id="module-pulumi_azure.scheduler"></span><dl class="class">
<dt id="pulumi_azure.scheduler.GetJobCollectionResult">
<em class="property">class </em><code class="descclassname">pulumi_azure.scheduler.</code><code class="descname">GetJobCollectionResult</code><span class="sig-paren">(</span><em>location=None</em>, <em>name=None</em>, <em>quotas=None</em>, <em>resource_group_name=None</em>, <em>sku=None</em>, <em>state=None</em>, <em>tags=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.scheduler.GetJobCollectionResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getJobCollection.</p>
<dl class="attribute">
<dt id="pulumi_azure.scheduler.GetJobCollectionResult.location">
<code class="descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.scheduler.GetJobCollectionResult.location" title="Permalink to this definition">¶</a></dt>
<dd><p>The Azure location where the resource exists.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.scheduler.GetJobCollectionResult.quotas">
<code class="descname">quotas</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.scheduler.GetJobCollectionResult.quotas" title="Permalink to this definition">¶</a></dt>
<dd><p>The Job collection quotas as documented in the <code class="docutils literal notranslate"><span class="pre">quota</span></code> block below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.scheduler.GetJobCollectionResult.sku">
<code class="descname">sku</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.scheduler.GetJobCollectionResult.sku" title="Permalink to this definition">¶</a></dt>
<dd><p>The Job Collection’s pricing level’s SKU.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.scheduler.GetJobCollectionResult.state">
<code class="descname">state</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.scheduler.GetJobCollectionResult.state" title="Permalink to this definition">¶</a></dt>
<dd><p>The Job Collection’s state.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.scheduler.GetJobCollectionResult.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.scheduler.GetJobCollectionResult.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags assigned to the resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.scheduler.GetJobCollectionResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.scheduler.GetJobCollectionResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_azure.scheduler.Job">
<em class="property">class </em><code class="descclassname">pulumi_azure.scheduler.</code><code class="descname">Job</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>action_storage_queue=None</em>, <em>action_web=None</em>, <em>error_action_storage_queue=None</em>, <em>error_action_web=None</em>, <em>job_collection_name=None</em>, <em>name=None</em>, <em>recurrence=None</em>, <em>resource_group_name=None</em>, <em>retry=None</em>, <em>start_time=None</em>, <em>state=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.scheduler.Job" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Scheduler Job.</p>
<blockquote>
<div><strong>NOTE:</strong> Support for Scheduler Job has been deprecated by Microsoft in favour of Logic Apps (<a class="reference external" href="https://docs.microsoft.com/en-us/azure/scheduler/migrate-from-scheduler-to-logic-apps">more information can be found at this link</a>) - as such we plan to remove support for this resource as a part of version 2.0 of the AzureRM Provider.</div></blockquote>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>action_storage_queue</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">action_storage_queue</span></code> block defining a storage queue job action as described below. Note this is identical to an <code class="docutils literal notranslate"><span class="pre">error_action_storage_queue</span></code> block.</li>
<li><strong>action_web</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">action_web</span></code> block defining the job action as described below. Note this is identical to an <code class="docutils literal notranslate"><span class="pre">error_action_web</span></code> block.</li>
<li><strong>error_action_storage_queue</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">error_action_storage_queue</span></code> block defining the a web action to take on an error as described below. Note this is identical to an <code class="docutils literal notranslate"><span class="pre">action_storage_queue</span></code> block.</li>
<li><strong>error_action_web</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">error_action_web</span></code> block defining the action to take on an error as described below. Note this is identical to an <code class="docutils literal notranslate"><span class="pre">action_web</span></code> block.</li>
<li><strong>job_collection_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Scheduler Job Collection in which the Job should exist. Changing this forces a new resource to be created.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Scheduler Job. Changing this forces a new resource to be created.</li>
<li><strong>recurrence</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">recurrence</span></code> block defining a job occurrence schedule.</li>
<li><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the Scheduler Job. Changing this forces a new resource to be created.</li>
<li><strong>retry</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">retry</span></code> block defining how to retry as described below.</li>
<li><strong>start_time</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The time the first instance of the job is to start running at.</li>
<li><strong>state</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The sets or gets the current state of the job. Can be set to either <code class="docutils literal notranslate"><span class="pre">Enabled</span></code> or <code class="docutils literal notranslate"><span class="pre">Completed</span></code></li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/scheduler_job.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/scheduler_job.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_azure.scheduler.Job.action_storage_queue">
<code class="descname">action_storage_queue</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.scheduler.Job.action_storage_queue" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">action_storage_queue</span></code> block defining a storage queue job action as described below. Note this is identical to an <code class="docutils literal notranslate"><span class="pre">error_action_storage_queue</span></code> block.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.scheduler.Job.action_web">
<code class="descname">action_web</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.scheduler.Job.action_web" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">action_web</span></code> block defining the job action as described below. Note this is identical to an <code class="docutils literal notranslate"><span class="pre">error_action_web</span></code> block.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.scheduler.Job.error_action_storage_queue">
<code class="descname">error_action_storage_queue</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.scheduler.Job.error_action_storage_queue" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">error_action_storage_queue</span></code> block defining the a web action to take on an error as described below. Note this is identical to an <code class="docutils literal notranslate"><span class="pre">action_storage_queue</span></code> block.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.scheduler.Job.error_action_web">
<code class="descname">error_action_web</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.scheduler.Job.error_action_web" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">error_action_web</span></code> block defining the action to take on an error as described below. Note this is identical to an <code class="docutils literal notranslate"><span class="pre">action_web</span></code> block.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.scheduler.Job.job_collection_name">
<code class="descname">job_collection_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.scheduler.Job.job_collection_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Scheduler Job Collection in which the Job should exist. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.scheduler.Job.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.scheduler.Job.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Scheduler Job. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.scheduler.Job.recurrence">
<code class="descname">recurrence</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.scheduler.Job.recurrence" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">recurrence</span></code> block defining a job occurrence schedule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.scheduler.Job.resource_group_name">
<code class="descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.scheduler.Job.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to create the Scheduler Job. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.scheduler.Job.retry">
<code class="descname">retry</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.scheduler.Job.retry" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">retry</span></code> block defining how to retry as described below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.scheduler.Job.start_time">
<code class="descname">start_time</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.scheduler.Job.start_time" title="Permalink to this definition">¶</a></dt>
<dd><p>The time the first instance of the job is to start running at.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.scheduler.Job.state">
<code class="descname">state</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.scheduler.Job.state" title="Permalink to this definition">¶</a></dt>
<dd><p>The sets or gets the current state of the job. Can be set to either <code class="docutils literal notranslate"><span class="pre">Enabled</span></code> or <code class="docutils literal notranslate"><span class="pre">Completed</span></code></p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.scheduler.Job.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.scheduler.Job.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.scheduler.Job.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.scheduler.Job.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.scheduler.JobCollection">
<em class="property">class </em><code class="descclassname">pulumi_azure.scheduler.</code><code class="descname">JobCollection</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>location=None</em>, <em>name=None</em>, <em>quota=None</em>, <em>resource_group_name=None</em>, <em>sku=None</em>, <em>state=None</em>, <em>tags=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.scheduler.JobCollection" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Scheduler Job Collection.</p>
<blockquote>
<div><strong>NOTE:</strong> Support for Scheduler Job Collections has been deprecated by Microsoft in favour of Logic Apps (<a class="reference external" href="https://docs.microsoft.com/en-us/azure/scheduler/migrate-from-scheduler-to-logic-apps">more information can be found at this link</a>) - as such we plan to remove support for this resource as a part of version 2.0 of the AzureRM Provider.</div></blockquote>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Scheduler Job Collection. Changing this forces a new resource to be created.</li>
<li><strong>quota</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Configures the Job collection quotas as documented in the <code class="docutils literal notranslate"><span class="pre">quota</span></code> block below.</li>
<li><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the resource group in which to create the Scheduler Job Collection. Changing this forces a new resource to be created.</li>
<li><strong>sku</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Sets the Job Collection’s pricing level’s SKU. Possible values include: <code class="docutils literal notranslate"><span class="pre">Standard</span></code>, <code class="docutils literal notranslate"><span class="pre">Free</span></code>, <code class="docutils literal notranslate"><span class="pre">P10Premium</span></code>, <code class="docutils literal notranslate"><span class="pre">P20Premium</span></code>.</li>
<li><strong>state</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Sets Job Collection’s state. Possible values include: <code class="docutils literal notranslate"><span class="pre">Enabled</span></code>, <code class="docutils literal notranslate"><span class="pre">Disabled</span></code>, <code class="docutils literal notranslate"><span class="pre">Suspended</span></code>.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/scheduler_job_collection.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/r/scheduler_job_collection.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_azure.scheduler.JobCollection.location">
<code class="descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.scheduler.JobCollection.location" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the supported Azure location where the resource exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.scheduler.JobCollection.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.scheduler.JobCollection.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Scheduler Job Collection. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.scheduler.JobCollection.quota">
<code class="descname">quota</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.scheduler.JobCollection.quota" title="Permalink to this definition">¶</a></dt>
<dd><p>Configures the Job collection quotas as documented in the <code class="docutils literal notranslate"><span class="pre">quota</span></code> block below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.scheduler.JobCollection.resource_group_name">
<code class="descname">resource_group_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.scheduler.JobCollection.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the resource group in which to create the Scheduler Job Collection. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.scheduler.JobCollection.sku">
<code class="descname">sku</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.scheduler.JobCollection.sku" title="Permalink to this definition">¶</a></dt>
<dd><p>Sets the Job Collection’s pricing level’s SKU. Possible values include: <code class="docutils literal notranslate"><span class="pre">Standard</span></code>, <code class="docutils literal notranslate"><span class="pre">Free</span></code>, <code class="docutils literal notranslate"><span class="pre">P10Premium</span></code>, <code class="docutils literal notranslate"><span class="pre">P20Premium</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.scheduler.JobCollection.state">
<code class="descname">state</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.scheduler.JobCollection.state" title="Permalink to this definition">¶</a></dt>
<dd><p>Sets Job Collection’s state. Possible values include: <code class="docutils literal notranslate"><span class="pre">Enabled</span></code>, <code class="docutils literal notranslate"><span class="pre">Disabled</span></code>, <code class="docutils literal notranslate"><span class="pre">Suspended</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_azure.scheduler.JobCollection.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.scheduler.JobCollection.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_azure.scheduler.JobCollection.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.scheduler.JobCollection.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.scheduler.JobCollection.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.scheduler.JobCollection.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.scheduler.get_job_collection">
<code class="descclassname">pulumi_azure.scheduler.</code><code class="descname">get_job_collection</code><span class="sig-paren">(</span><em>name=None</em>, <em>resource_group_name=None</em>, <em>opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.scheduler.get_job_collection" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing Scheduler Job Collection.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Support for Scheduler Job Collections has been deprecated by Microsoft in favour of Logic Apps (<a class="reference external" href="https://docs.microsoft.com/en-us/azure/scheduler/migrate-from-scheduler-to-logic-apps">more information can be found at this link</a>) - as such we plan to remove support for this data source as a part of version 2.0 of the AzureRM Provider.</p>
<p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/scheduler_job_collection.html.markdown">https://github.com/terraform-providers/terraform-provider-azurerm/blob/master/website/docs/d/scheduler_job_collection.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

</div>
