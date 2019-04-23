<div class="section" id="module-pulumi_gcp.dataproc">
<span id="dataproc"></span><h1>dataproc<a class="headerlink" href="#module-pulumi_gcp.dataproc" title="Permalink to this headline">¶</a></h1>
<dl class="class">
<dt id="pulumi_gcp.dataproc.Cluster">
<em class="property">class </em><code class="descclassname">pulumi_gcp.dataproc.</code><code class="descname">Cluster</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>cluster_config=None</em>, <em>labels=None</em>, <em>name=None</em>, <em>project=None</em>, <em>region=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.dataproc.Cluster" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Cloud Dataproc cluster resource within GCP. For more information see
<a class="reference external" href="https://cloud.google.com/dataproc/">the official dataproc documentation</a>.</p>
<p>!&gt; <strong>Warning:</strong> Due to limitations of the API, all arguments except
<code class="docutils literal notranslate"><span class="pre">labels</span></code>,<code class="docutils literal notranslate"><span class="pre">cluster_config.worker_config.num_instances</span></code> and <code class="docutils literal notranslate"><span class="pre">cluster_config.preemptible_worker_config.num_instances</span></code> are non-updateable. Changing others will cause recreation of the
whole cluster!</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>cluster_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Allows you to configure various aspects of the cluster.
Structure defined below.</li>
<li><strong>labels</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The list of labels (key/value pairs) to be applied to
instances in the cluster. GCP generates some itself including <code class="docutils literal notranslate"><span class="pre">goog-dataproc-cluster-name</span></code>
which is the name of the cluster.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the cluster, unique within the project and
zone.</li>
<li><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the <code class="docutils literal notranslate"><span class="pre">cluster</span></code> will exist. If it
is not provided, the provider project is used.</li>
<li><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region in which the cluster and associated nodes will be created in.
Defaults to <code class="docutils literal notranslate"><span class="pre">global</span></code>.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_gcp.dataproc.Cluster.cluster_config">
<code class="descname">cluster_config</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.dataproc.Cluster.cluster_config" title="Permalink to this definition">¶</a></dt>
<dd><p>Allows you to configure various aspects of the cluster.
Structure defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.dataproc.Cluster.labels">
<code class="descname">labels</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.dataproc.Cluster.labels" title="Permalink to this definition">¶</a></dt>
<dd><p>The list of labels (key/value pairs) to be applied to
instances in the cluster. GCP generates some itself including <code class="docutils literal notranslate"><span class="pre">goog-dataproc-cluster-name</span></code>
which is the name of the cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.dataproc.Cluster.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.dataproc.Cluster.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the cluster, unique within the project and
zone.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.dataproc.Cluster.project">
<code class="descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.dataproc.Cluster.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the <code class="docutils literal notranslate"><span class="pre">cluster</span></code> will exist. If it
is not provided, the provider project is used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.dataproc.Cluster.region">
<code class="descname">region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.dataproc.Cluster.region" title="Permalink to this definition">¶</a></dt>
<dd><p>The region in which the cluster and associated nodes will be created in.
Defaults to <code class="docutils literal notranslate"><span class="pre">global</span></code>.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.dataproc.Cluster.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.dataproc.Cluster.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.dataproc.Cluster.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.dataproc.Cluster.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.dataproc.Job">
<em class="property">class </em><code class="descclassname">pulumi_gcp.dataproc.</code><code class="descname">Job</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>force_delete=None</em>, <em>hadoop_config=None</em>, <em>hive_config=None</em>, <em>labels=None</em>, <em>pig_config=None</em>, <em>placement=None</em>, <em>project=None</em>, <em>pyspark_config=None</em>, <em>reference=None</em>, <em>region=None</em>, <em>scheduling=None</em>, <em>spark_config=None</em>, <em>sparksql_config=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.dataproc.Job" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a job resource within a Dataproc cluster within GCE. For more information see
<a class="reference external" href="https://cloud.google.com/dataproc/">the official dataproc documentation</a>.</p>
<p>!&gt; <strong>Note:</strong> This resource does not support ‘update’ and changing any attributes will cause the resource to be recreated.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>force_delete</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – By default, you can only delete inactive jobs within
Dataproc. Setting this to true, and calling destroy, will ensure that the
job is first cancelled before issuing the delete.</li>
<li><strong>labels</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – The list of labels (key/value pairs) to add to the job.</li>
<li><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The project in which the <code class="docutils literal notranslate"><span class="pre">cluster</span></code> can be found and jobs
subsequently run against. If it is not provided, the provider project is used.</li>
<li><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Cloud Dataproc region. This essentially determines which clusters are available
for this job to be submitted to. If not specified, defaults to <code class="docutils literal notranslate"><span class="pre">global</span></code>.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_gcp.dataproc.Job.driver_controls_files_uri">
<code class="descname">driver_controls_files_uri</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.dataproc.Job.driver_controls_files_uri" title="Permalink to this definition">¶</a></dt>
<dd><p>If present, the location of miscellaneous control files which may be used as part of job setup and handling. If not present, control files may be placed in the same location as driver_output_uri.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.dataproc.Job.driver_output_resource_uri">
<code class="descname">driver_output_resource_uri</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.dataproc.Job.driver_output_resource_uri" title="Permalink to this definition">¶</a></dt>
<dd><p>A URI pointing to the location of the stdout of the job’s driver program.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.dataproc.Job.force_delete">
<code class="descname">force_delete</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.dataproc.Job.force_delete" title="Permalink to this definition">¶</a></dt>
<dd><p>By default, you can only delete inactive jobs within
Dataproc. Setting this to true, and calling destroy, will ensure that the
job is first cancelled before issuing the delete.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.dataproc.Job.labels">
<code class="descname">labels</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.dataproc.Job.labels" title="Permalink to this definition">¶</a></dt>
<dd><p>The list of labels (key/value pairs) to add to the job.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.dataproc.Job.project">
<code class="descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.dataproc.Job.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The project in which the <code class="docutils literal notranslate"><span class="pre">cluster</span></code> can be found and jobs
subsequently run against. If it is not provided, the provider project is used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.dataproc.Job.region">
<code class="descname">region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.dataproc.Job.region" title="Permalink to this definition">¶</a></dt>
<dd><p>The Cloud Dataproc region. This essentially determines which clusters are available
for this job to be submitted to. If not specified, defaults to <code class="docutils literal notranslate"><span class="pre">global</span></code>.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.dataproc.Job.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.dataproc.Job.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.dataproc.Job.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.dataproc.Job.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
