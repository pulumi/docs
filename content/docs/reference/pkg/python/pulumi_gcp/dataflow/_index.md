---
title: Module dataflow
title_tag: Module dataflow | Package pulumi_gcp | Python SDK
linktitle: dataflow
notitle: true
---

<div class="section" id="dataflow">
<h1>dataflow<a class="headerlink" href="#dataflow" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-gcp/issues">pulumi/pulumi-gcp repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/issues">terraform-providers/terraform-provider-google repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_gcp.dataflow"></span><dl class="py class">
<dt id="pulumi_gcp.dataflow.Job">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.dataflow.</code><code class="sig-name descname">Job</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">additional_experiments</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ip_configuration</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">labels</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">machine_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">max_workers</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">network</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">on_delete</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">parameters</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">region</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_account_email</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">subnetwork</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">temp_gcs_location</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">template_gcs_path</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.dataflow.Job" title="Permalink to this definition">¶</a></dt>
<dd><p>Creates a job on Dataflow, which is an implementation of Apache Beam running on Google Compute Engine. For more information see
the official documentation for
<a class="reference external" href="https://beam.apache.org">Beam</a> and <a class="reference external" href="https://cloud.google.com/dataflow/">Dataflow</a>.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_gcp</span> <span class="k">as</span> <span class="nn">gcp</span>

<span class="n">big_data_job</span> <span class="o">=</span> <span class="n">gcp</span><span class="o">.</span><span class="n">dataflow</span><span class="o">.</span><span class="n">Job</span><span class="p">(</span><span class="s2">&quot;bigDataJob&quot;</span><span class="p">,</span>
    <span class="n">parameters</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;baz&quot;</span><span class="p">:</span> <span class="s2">&quot;qux&quot;</span><span class="p">,</span>
        <span class="s2">&quot;foo&quot;</span><span class="p">:</span> <span class="s2">&quot;bar&quot;</span><span class="p">,</span>
    <span class="p">},</span>
    <span class="n">temp_gcs_location</span><span class="o">=</span><span class="s2">&quot;gs://my-bucket/tmp_dir&quot;</span><span class="p">,</span>
    <span class="n">template_gcs_path</span><span class="o">=</span><span class="s2">&quot;gs://my-bucket/templates/template_file&quot;</span><span class="p">)</span>
</pre></div>
</div>
<p>There are many types of Dataflow jobs.  Some Dataflow jobs run constantly, getting new data from (e.g.) a GCS bucket, and outputting data continuously.  Some jobs process a set amount of data then terminate.  All jobs can fail while running due to programming errors or other issues.  In this way, Dataflow jobs are different from most other Google resources.</p>
<p>The Dataflow resource is considered ‘existing’ while it is in a nonterminal state.  If it reaches a terminal state (e.g. ‘FAILED’, ‘COMPLETE’, ‘CANCELLED’), it will be recreated on the next ‘apply’.  This is as expected for jobs which run continuously, but may surprise users who use this resource for other kinds of Dataflow jobs.</p>
<p>A Dataflow job which is ‘destroyed’ may be “cancelled” or “drained”.  If “cancelled”, the job terminates - any data written remains where it is, but no new data will be processed.  If “drained”, no new data will enter the pipeline, but any data currently in the pipeline will finish being processed.  The default is “cancelled”, but if a user sets <code class="docutils literal notranslate"><span class="pre">on_delete</span></code> to <code class="docutils literal notranslate"><span class="pre">&quot;drain&quot;</span></code> in the configuration, you may experience a long wait for your <code class="docutils literal notranslate"><span class="pre">pulumi</span> <span class="pre">destroy</span></code> to complete.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>additional_experiments</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of experiments that should be used by the job. An example value is <code class="docutils literal notranslate"><span class="pre">[&quot;enable_stackdriver_agent_metrics&quot;]</span></code>.</p></li>
<li><p><strong>ip_configuration</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The configuration for VM IPs.  Options are <code class="docutils literal notranslate"><span class="pre">&quot;WORKER_IP_PUBLIC&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;WORKER_IP_PRIVATE&quot;</span></code>.</p></li>
<li><p><strong>labels</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – User labels to be specified for the job. Keys and values should follow the restrictions
specified in the <a class="reference external" href="https://cloud.google.com/compute/docs/labeling-resources#restrictions">labeling restrictions</a> page.
<strong>NOTE</strong>: Google-provided Dataflow templates often provide default labels that begin with <code class="docutils literal notranslate"><span class="pre">goog-dataflow-provided</span></code>.
Unless explicitly set in config, these labels will be ignored to prevent diffs on re-apply.</p></li>
<li><p><strong>machine_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The machine type to use for the job.</p></li>
<li><p><strong>max_workers</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The number of workers permitted to work on the job.  More workers may improve processing speed at additional cost.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A unique name for the resource, required by Dataflow.</p></li>
<li><p><strong>network</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The network to which VMs will be assigned. If it is not provided, “default” will be used.</p></li>
<li><p><strong>on_delete</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – One of “drain” or “cancel”.  Specifies behavior of deletion during <code class="docutils literal notranslate"><span class="pre">pulumi</span> <span class="pre">destroy</span></code>.  See above note.</p></li>
<li><p><strong>parameters</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Key/Value pairs to be passed to the Dataflow job (as used in the template).</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The project in which the resource belongs. If it is not provided, the provider project is used.</p></li>
<li><p><strong>service_account_email</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Service Account email used to create the job.</p></li>
<li><p><strong>subnetwork</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The subnetwork to which VMs will be assigned. Should be of the form “regions/REGION/subnetworks/SUBNETWORK”.</p></li>
<li><p><strong>temp_gcs_location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A writeable location on GCS for the Dataflow job to dump its temporary data.</p></li>
<li><p><strong>template_gcs_path</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The GCS path to the Dataflow job template.</p></li>
<li><p><strong>zone</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The zone in which the created job should run. If it is not provided, the provider zone is used.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_gcp.dataflow.Job.additional_experiments">
<code class="sig-name descname">additional_experiments</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.dataflow.Job.additional_experiments" title="Permalink to this definition">¶</a></dt>
<dd><p>List of experiments that should be used by the job. An example value is <code class="docutils literal notranslate"><span class="pre">[&quot;enable_stackdriver_agent_metrics&quot;]</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.dataflow.Job.ip_configuration">
<code class="sig-name descname">ip_configuration</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.dataflow.Job.ip_configuration" title="Permalink to this definition">¶</a></dt>
<dd><p>The configuration for VM IPs.  Options are <code class="docutils literal notranslate"><span class="pre">&quot;WORKER_IP_PUBLIC&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;WORKER_IP_PRIVATE&quot;</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.dataflow.Job.job_id">
<code class="sig-name descname">job_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.dataflow.Job.job_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The unique ID of this job.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.dataflow.Job.labels">
<code class="sig-name descname">labels</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.dataflow.Job.labels" title="Permalink to this definition">¶</a></dt>
<dd><p>User labels to be specified for the job. Keys and values should follow the restrictions
specified in the <a class="reference external" href="https://cloud.google.com/compute/docs/labeling-resources#restrictions">labeling restrictions</a> page.
<strong>NOTE</strong>: Google-provided Dataflow templates often provide default labels that begin with <code class="docutils literal notranslate"><span class="pre">goog-dataflow-provided</span></code>.
Unless explicitly set in config, these labels will be ignored to prevent diffs on re-apply.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.dataflow.Job.machine_type">
<code class="sig-name descname">machine_type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.dataflow.Job.machine_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The machine type to use for the job.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.dataflow.Job.max_workers">
<code class="sig-name descname">max_workers</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.dataflow.Job.max_workers" title="Permalink to this definition">¶</a></dt>
<dd><p>The number of workers permitted to work on the job.  More workers may improve processing speed at additional cost.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.dataflow.Job.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.dataflow.Job.name" title="Permalink to this definition">¶</a></dt>
<dd><p>A unique name for the resource, required by Dataflow.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.dataflow.Job.network">
<code class="sig-name descname">network</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.dataflow.Job.network" title="Permalink to this definition">¶</a></dt>
<dd><p>The network to which VMs will be assigned. If it is not provided, “default” will be used.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.dataflow.Job.on_delete">
<code class="sig-name descname">on_delete</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.dataflow.Job.on_delete" title="Permalink to this definition">¶</a></dt>
<dd><p>One of “drain” or “cancel”.  Specifies behavior of deletion during <code class="docutils literal notranslate"><span class="pre">pulumi</span> <span class="pre">destroy</span></code>.  See above note.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.dataflow.Job.parameters">
<code class="sig-name descname">parameters</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.dataflow.Job.parameters" title="Permalink to this definition">¶</a></dt>
<dd><p>Key/Value pairs to be passed to the Dataflow job (as used in the template).</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.dataflow.Job.project">
<code class="sig-name descname">project</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.dataflow.Job.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The project in which the resource belongs. If it is not provided, the provider project is used.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.dataflow.Job.service_account_email">
<code class="sig-name descname">service_account_email</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.dataflow.Job.service_account_email" title="Permalink to this definition">¶</a></dt>
<dd><p>The Service Account email used to create the job.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.dataflow.Job.state">
<code class="sig-name descname">state</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.dataflow.Job.state" title="Permalink to this definition">¶</a></dt>
<dd><p>The current state of the resource, selected from the <a class="reference external" href="https://cloud.google.com/dataflow/docs/reference/rest/v1b3/projects.jobs#Job.JobState">JobState enum</a></p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.dataflow.Job.subnetwork">
<code class="sig-name descname">subnetwork</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.dataflow.Job.subnetwork" title="Permalink to this definition">¶</a></dt>
<dd><p>The subnetwork to which VMs will be assigned. Should be of the form “regions/REGION/subnetworks/SUBNETWORK”.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.dataflow.Job.temp_gcs_location">
<code class="sig-name descname">temp_gcs_location</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.dataflow.Job.temp_gcs_location" title="Permalink to this definition">¶</a></dt>
<dd><p>A writeable location on GCS for the Dataflow job to dump its temporary data.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.dataflow.Job.template_gcs_path">
<code class="sig-name descname">template_gcs_path</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.dataflow.Job.template_gcs_path" title="Permalink to this definition">¶</a></dt>
<dd><p>The GCS path to the Dataflow job template.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.dataflow.Job.type">
<code class="sig-name descname">type</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.dataflow.Job.type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of this job, selected from the <a class="reference external" href="https://cloud.google.com/dataflow/docs/reference/rest/v1b3/projects.jobs#Job.JobType">JobType enum</a></p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.dataflow.Job.zone">
<code class="sig-name descname">zone</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.dataflow.Job.zone" title="Permalink to this definition">¶</a></dt>
<dd><p>The zone in which the created job should run. If it is not provided, the provider zone is used.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gcp.dataflow.Job.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">additional_experiments</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ip_configuration</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">job_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">labels</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">machine_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">max_workers</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">network</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">on_delete</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">parameters</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">region</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_account_email</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">state</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">subnetwork</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">temp_gcs_location</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">template_gcs_path</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zone</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.dataflow.Job.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Job resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>additional_experiments</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of experiments that should be used by the job. An example value is <code class="docutils literal notranslate"><span class="pre">[&quot;enable_stackdriver_agent_metrics&quot;]</span></code>.</p></li>
<li><p><strong>ip_configuration</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The configuration for VM IPs.  Options are <code class="docutils literal notranslate"><span class="pre">&quot;WORKER_IP_PUBLIC&quot;</span></code> or <code class="docutils literal notranslate"><span class="pre">&quot;WORKER_IP_PRIVATE&quot;</span></code>.</p></li>
<li><p><strong>job_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique ID of this job.</p></li>
<li><p><strong>labels</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – <p>User labels to be specified for the job. Keys and values should follow the restrictions
specified in the <a class="reference external" href="https://cloud.google.com/compute/docs/labeling-resources#restrictions">labeling restrictions</a> page.
<strong>NOTE</strong>: Google-provided Dataflow templates often provide default labels that begin with <code class="docutils literal notranslate"><span class="pre">goog-dataflow-provided</span></code>.
Unless explicitly set in config, these labels will be ignored to prevent diffs on re-apply.</p>
</p></li>
<li><p><strong>machine_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The machine type to use for the job.</p></li>
<li><p><strong>max_workers</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The number of workers permitted to work on the job.  More workers may improve processing speed at additional cost.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A unique name for the resource, required by Dataflow.</p></li>
<li><p><strong>network</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The network to which VMs will be assigned. If it is not provided, “default” will be used.</p></li>
<li><p><strong>on_delete</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – One of “drain” or “cancel”.  Specifies behavior of deletion during <code class="docutils literal notranslate"><span class="pre">pulumi</span> <span class="pre">destroy</span></code>.  See above note.</p></li>
<li><p><strong>parameters</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Key/Value pairs to be passed to the Dataflow job (as used in the template).</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The project in which the resource belongs. If it is not provided, the provider project is used.</p></li>
<li><p><strong>service_account_email</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Service Account email used to create the job.</p></li>
<li><p><strong>state</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The current state of the resource, selected from the <a class="reference external" href="https://cloud.google.com/dataflow/docs/reference/rest/v1b3/projects.jobs#Job.JobState">JobState enum</a></p>
</p></li>
<li><p><strong>subnetwork</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The subnetwork to which VMs will be assigned. Should be of the form “regions/REGION/subnetworks/SUBNETWORK”.</p></li>
<li><p><strong>temp_gcs_location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A writeable location on GCS for the Dataflow job to dump its temporary data.</p></li>
<li><p><strong>template_gcs_path</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The GCS path to the Dataflow job template.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The type of this job, selected from the <a class="reference external" href="https://cloud.google.com/dataflow/docs/reference/rest/v1b3/projects.jobs#Job.JobType">JobType enum</a></p>
</p></li>
<li><p><strong>zone</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The zone in which the created job should run. If it is not provided, the provider zone is used.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gcp.dataflow.Job.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.dataflow.Job.translate_output_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py method">
<dt id="pulumi_gcp.dataflow.Job.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.dataflow.Job.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

</div>
