<div class="section" id="module-pulumi_gcp.dataflow">
<span id="dataflow"></span><h1>dataflow<a class="headerlink" href="#module-pulumi_gcp.dataflow" title="Permalink to this headline">¶</a></h1>
<dl class="class">
<dt id="pulumi_gcp.dataflow.Job">
<em class="property">class </em><code class="descclassname">pulumi_gcp.dataflow.</code><code class="descname">Job</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>max_workers=None</em>, <em>name=None</em>, <em>network=None</em>, <em>on_delete=None</em>, <em>parameters=None</em>, <em>project=None</em>, <em>region=None</em>, <em>service_account_email=None</em>, <em>subnetwork=None</em>, <em>temp_gcs_location=None</em>, <em>template_gcs_path=None</em>, <em>zone=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.dataflow.Job" title="Permalink to this definition">¶</a></dt>
<dd><p>Creates a job on Dataflow, which is an implementation of Apache Beam running on Google Compute Engine. For more information see
the official documentation for
<a class="reference external" href="https://beam.apache.org">Beam</a> and <a class="reference external" href="https://cloud.google.com/dataflow/">Dataflow</a>.</p>
<p>There are many types of Dataflow jobs.  Some Dataflow jobs run constantly, getting new data from (e.g.) a GCS bucket, and outputting data continuously.  Some jobs process a set amount of data then terminate.  All jobs can fail while running due to programming errors or other issues.  In this way, Dataflow jobs are different from most other Terraform / Google resources.</p>
<p>The Dataflow resource is considered ‘existing’ while it is in a nonterminal state.  If it reaches a terminal state (e.g. ‘FAILED’, ‘COMPLETE’, ‘CANCELLED’), it will be recreated on the next ‘apply’.  This is as expected for jobs which run continously, but may surprise users who use this resource for other kinds of Dataflow jobs.</p>
<p>A Dataflow job which is ‘destroyed’ may be “cancelled” or “drained”.  If “cancelled”, the job terminates - any data written remains where it is, but no new data will be processed.  If “drained”, no new data will enter the pipeline, but any data currently in the pipeline will finish being processed.  The default is “cancelled”, but if a user sets <code class="docutils literal notranslate"><span class="pre">on_delete</span></code> to <code class="docutils literal notranslate"><span class="pre">&quot;drain&quot;</span></code> in the configuration, you may experience a long wait for your <code class="docutils literal notranslate"><span class="pre">terraform</span> <span class="pre">destroy</span></code> to complete.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>max_workers</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The number of workers permitted to work on the job.  More workers may improve processing speed at additional cost.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A unique name for the resource, required by Dataflow.</li>
<li><strong>network</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The network to which VMs will be assigned. If it is not provided, “default” will be used.</li>
<li><strong>on_delete</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – One of “drain” or “cancel”.  Specifies behavior of deletion during <code class="docutils literal notranslate"><span class="pre">terraform</span> <span class="pre">destroy</span></code>.  See above note.</li>
<li><strong>parameters</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Key/Value pairs to be passed to the Dataflow job (as used in the template).</li>
<li><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The project in which the resource belongs. If it is not provided, the provider project is used.</li>
<li><strong>service_account_email</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Service Account email used to create the job.</li>
<li><strong>subnetwork</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The subnetwork to which VMs will be assigned. Should be of the form “regions/REGION/subnetworks/SUBNETWORK”.</li>
<li><strong>temp_gcs_location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A writeable location on GCS for the Dataflow job to dump its temporary data.</li>
<li><strong>template_gcs_path</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The GCS path to the Dataflow job template.</li>
<li><strong>zone</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The zone in which the created job should run. If it is not provided, the provider zone is used.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_gcp.dataflow.Job.max_workers">
<code class="descname">max_workers</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.dataflow.Job.max_workers" title="Permalink to this definition">¶</a></dt>
<dd><p>The number of workers permitted to work on the job.  More workers may improve processing speed at additional cost.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.dataflow.Job.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.dataflow.Job.name" title="Permalink to this definition">¶</a></dt>
<dd><p>A unique name for the resource, required by Dataflow.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.dataflow.Job.network">
<code class="descname">network</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.dataflow.Job.network" title="Permalink to this definition">¶</a></dt>
<dd><p>The network to which VMs will be assigned. If it is not provided, “default” will be used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.dataflow.Job.on_delete">
<code class="descname">on_delete</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.dataflow.Job.on_delete" title="Permalink to this definition">¶</a></dt>
<dd><p>One of “drain” or “cancel”.  Specifies behavior of deletion during <code class="docutils literal notranslate"><span class="pre">terraform</span> <span class="pre">destroy</span></code>.  See above note.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.dataflow.Job.parameters">
<code class="descname">parameters</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.dataflow.Job.parameters" title="Permalink to this definition">¶</a></dt>
<dd><p>Key/Value pairs to be passed to the Dataflow job (as used in the template).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.dataflow.Job.project">
<code class="descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.dataflow.Job.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The project in which the resource belongs. If it is not provided, the provider project is used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.dataflow.Job.service_account_email">
<code class="descname">service_account_email</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.dataflow.Job.service_account_email" title="Permalink to this definition">¶</a></dt>
<dd><p>The Service Account email used to create the job.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.dataflow.Job.state">
<code class="descname">state</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.dataflow.Job.state" title="Permalink to this definition">¶</a></dt>
<dd><p>The current state of the resource, selected from the <a class="reference external" href="https://cloud.google.com/dataflow/docs/reference/rest/v1b3/projects.jobs#Job.JobState">JobState enum</a></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.dataflow.Job.subnetwork">
<code class="descname">subnetwork</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.dataflow.Job.subnetwork" title="Permalink to this definition">¶</a></dt>
<dd><p>The subnetwork to which VMs will be assigned. Should be of the form “regions/REGION/subnetworks/SUBNETWORK”.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.dataflow.Job.temp_gcs_location">
<code class="descname">temp_gcs_location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.dataflow.Job.temp_gcs_location" title="Permalink to this definition">¶</a></dt>
<dd><p>A writeable location on GCS for the Dataflow job to dump its temporary data.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.dataflow.Job.template_gcs_path">
<code class="descname">template_gcs_path</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.dataflow.Job.template_gcs_path" title="Permalink to this definition">¶</a></dt>
<dd><p>The GCS path to the Dataflow job template.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.dataflow.Job.zone">
<code class="descname">zone</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.dataflow.Job.zone" title="Permalink to this definition">¶</a></dt>
<dd><p>The zone in which the created job should run. If it is not provided, the provider zone is used.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.dataflow.Job.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.dataflow.Job.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.dataflow.Job.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.dataflow.Job.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

</div>
