---
title: Module dataflow
---

<div class="section" id="dataflow">
<h1>dataflow<a class="headerlink" href="#dataflow" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-gcp/issues">pulumi/pulumi-gcp repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/issues">terraform-providers/terraform-provider-google repo</a>.</div></blockquote>
<span class="target" id="module-pulumi_gcp.dataflow"></span><dl class="class">
<dt id="pulumi_gcp.dataflow.Job">
<em class="property">class </em><code class="descclassname">pulumi_gcp.dataflow.</code><code class="descname">Job</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>labels=None</em>, <em>machine_type=None</em>, <em>max_workers=None</em>, <em>name=None</em>, <em>network=None</em>, <em>on_delete=None</em>, <em>parameters=None</em>, <em>project=None</em>, <em>region=None</em>, <em>service_account_email=None</em>, <em>subnetwork=None</em>, <em>temp_gcs_location=None</em>, <em>template_gcs_path=None</em>, <em>zone=None</em>, <em>__props__=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.dataflow.Job" title="Permalink to this definition">¶</a></dt>
<dd><p>Creates a job on Dataflow, which is an implementation of Apache Beam running on Google Compute Engine. For more information see
the official documentation for
<a class="reference external" href="https://beam.apache.org">Beam</a> and <a class="reference external" href="https://cloud.google.com/dataflow/">Dataflow</a>.</p>
<p>There are many types of Dataflow jobs.  Some Dataflow jobs run constantly, getting new data from (e.g.) a GCS bucket, and outputting data continuously.  Some jobs process a set amount of data then terminate.  All jobs can fail while running due to programming errors or other issues.  In this way, Dataflow jobs are different from most other resources.</p>
<p>The Dataflow resource is considered ‘existing’ while it is in a nonterminal state.  If it reaches a terminal state (e.g. ‘FAILED’, ‘COMPLETE’, ‘CANCELLED’), it will be recreated on the next ‘apply’.  This is as expected for jobs which run continously, but may surprise users who use this resource for other kinds of Dataflow jobs.</p>
<p>A Dataflow job which is ‘destroyed’ may be “cancelled” or “drained”.  If “cancelled”, the job terminates - any data written remains where it is, but no new data will be processed.  If “drained”, no new data will enter the pipeline, but any data currently in the pipeline will finish being processed.  The default is “cancelled”, but if a user sets <code class="docutils literal notranslate"><span class="pre">on_delete</span></code> to <code class="docutils literal notranslate"><span class="pre">&quot;drain&quot;</span></code> in the configuration, you may experience a long wait for your destroy to complete.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>labels</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – User labels to be specified for the job. Keys and values should follow the restrictions specified in the <a class="reference external" href="https://cloud.google.com/compute/docs/labeling-resources#restrictions">labeling restrictions</a> page.</li>
<li><strong>machine_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The machine type to use for the job.</li>
<li><strong>max_workers</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The number of workers permitted to work on the job.  More workers may improve processing speed at additional cost.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A unique name for the resource, required by Dataflow.</li>
<li><strong>network</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The network to which VMs will be assigned. If it is not provided, “default” will be used.</li>
<li><strong>on_delete</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – One of “drain” or “cancel”.  Specifies behavior of deletion during a destroy.  See above note.</li>
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
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/dataflow_job.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/dataflow_job.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_gcp.dataflow.Job.labels">
<code class="descname">labels</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.dataflow.Job.labels" title="Permalink to this definition">¶</a></dt>
<dd><p>User labels to be specified for the job. Keys and values should follow the restrictions specified in the <a class="reference external" href="https://cloud.google.com/compute/docs/labeling-resources#restrictions">labeling restrictions</a> page.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.dataflow.Job.machine_type">
<code class="descname">machine_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.dataflow.Job.machine_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The machine type to use for the job.</p>
</dd></dl>

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
<dd><p>One of “drain” or “cancel”.  Specifies behavior of deletion during a destroy.  See above note.</p>
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

<dl class="staticmethod">
<dt id="pulumi_gcp.dataflow.Job.get">
<em class="property">static </em><code class="descname">get</code><span class="sig-paren">(</span><em>resource_name</em>, <em>id</em>, <em>opts=None</em>, <em>labels=None</em>, <em>machine_type=None</em>, <em>max_workers=None</em>, <em>name=None</em>, <em>network=None</em>, <em>on_delete=None</em>, <em>parameters=None</em>, <em>project=None</em>, <em>region=None</em>, <em>service_account_email=None</em>, <em>state=None</em>, <em>subnetwork=None</em>, <em>temp_gcs_location=None</em>, <em>template_gcs_path=None</em>, <em>zone=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.dataflow.Job.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Job resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.
:param str resource_name: The unique name of the resulting resource.
:param str id: The unique provider ID of the resource to lookup.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[dict] labels: User labels to be specified for the job. Keys and values should follow the restrictions specified in the <a class="reference external" href="https://cloud.google.com/compute/docs/labeling-resources#restrictions">labeling restrictions</a> page.
:param pulumi.Input[str] machine_type: The machine type to use for the job.
:param pulumi.Input[float] max_workers: The number of workers permitted to work on the job.  More workers may improve processing speed at additional cost.
:param pulumi.Input[str] name: A unique name for the resource, required by Dataflow.
:param pulumi.Input[str] network: The network to which VMs will be assigned. If it is not provided, “default” will be used.
:param pulumi.Input[str] on_delete: One of “drain” or “cancel”.  Specifies behavior of deletion during a destroy.  See above note.
:param pulumi.Input[dict] parameters: Key/Value pairs to be passed to the Dataflow job (as used in the template).
:param pulumi.Input[str] project: The project in which the resource belongs. If it is not provided, the provider project is used.
:param pulumi.Input[str] service_account_email: The Service Account email used to create the job.
:param pulumi.Input[str] state: The current state of the resource, selected from the <a class="reference external" href="https://cloud.google.com/dataflow/docs/reference/rest/v1b3/projects.jobs#Job.JobState">JobState enum</a>
:param pulumi.Input[str] subnetwork: The subnetwork to which VMs will be assigned. Should be of the form “regions/REGION/subnetworks/SUBNETWORK”.
:param pulumi.Input[str] temp_gcs_location: A writeable location on GCS for the Dataflow job to dump its temporary data.
:param pulumi.Input[str] template_gcs_path: The GCS path to the Dataflow job template.
:param pulumi.Input[str] zone: The zone in which the created job should run. If it is not provided, the provider zone is used.</p>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/dataflow_job.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/dataflow_job.html.markdown</a>.</div></blockquote>
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
