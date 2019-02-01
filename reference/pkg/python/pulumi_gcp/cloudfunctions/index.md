<div class="section" id="module-pulumi_gcp.cloudfunctions">
<span id="cloudfunctions"></span><h1>cloudfunctions<a class="headerlink" href="#module-pulumi_gcp.cloudfunctions" title="Permalink to this headline">¶</a></h1>
<dl class="class">
<dt id="pulumi_gcp.cloudfunctions.Function">
<em class="property">class </em><code class="descclassname">pulumi_gcp.cloudfunctions.</code><code class="descname">Function</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>available_memory_mb=None</em>, <em>description=None</em>, <em>entry_point=None</em>, <em>environment_variables=None</em>, <em>event_trigger=None</em>, <em>https_trigger_url=None</em>, <em>labels=None</em>, <em>name=None</em>, <em>project=None</em>, <em>region=None</em>, <em>retry_on_failure=None</em>, <em>runtime=None</em>, <em>source_archive_bucket=None</em>, <em>source_archive_object=None</em>, <em>timeout=None</em>, <em>trigger_bucket=None</em>, <em>trigger_http=None</em>, <em>trigger_topic=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.cloudfunctions.Function" title="Permalink to this definition">¶</a></dt>
<dd><p>Creates a new Cloud Function. For more information see
[the official documentation](<a class="reference external" href="https://cloud.google.com/functions/docs/">https://cloud.google.com/functions/docs/</a>)
and
[API](<a class="reference external" href="https://cloud.google.com/functions/docs/apis">https://cloud.google.com/functions/docs/apis</a>).</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>available_memory_mb</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Memory (in MB), available to the function. Default value is 256MB. Allowed values are: 128MB, 256MB, 512MB, 1024MB, and 2048MB.</li>
<li><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Description of the function.</li>
<li><strong>entry_point</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of a JavaScript function that will be executed when the Google Cloud Function is triggered.</li>
<li><strong>environment_variables</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A set of key/value environment variable pairs to assign to the function.</li>
<li><strong>event_trigger</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A source that fires events in response to a condition in another service. Structure is documented below. Cannot be used with <cite>trigger_http</cite>.</li>
<li><strong>https_trigger_url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – URL which triggers function execution. Returned only if <cite>trigger_http</cite> is used.</li>
<li><strong>labels</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A set of key/value label pairs to assign to the function.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A user-defined name of the function. Function names must be unique globally.</li>
<li><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Project of the function. If it is not provided, the provider project is used.</li>
<li><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Region of function. Currently can be only “us-central1”. If it is not provided, the provider region is used.</li>
<li><strong>retry_on_failure</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the function should be retried on failure. This only applies to bucket and topic triggers, not HTTPS triggers.
Deprecated. Use <cite>event_trigger.failure_policy.retry</cite> instead.</li>
<li><strong>runtime</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The runtime in which the function is going to run. If empty, defaults to <cite>“nodejs6”</cite>.</li>
<li><strong>source_archive_bucket</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The GCS bucket containing the zip archive which contains the function.</li>
<li><strong>source_archive_object</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The source archive object (file) in archive bucket.</li>
<li><strong>timeout</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Timeout (in seconds) for the function. Default value is 60 seconds. Cannot be more than 540 seconds.</li>
<li><strong>trigger_bucket</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Google Cloud Storage bucket name. Every change in files in this bucket will trigger function execution. Cannot be used with <cite>trigger_http</cite> and <cite>trigger_topic</cite>.
Deprecated. Use <cite>event_trigger</cite> instead.</li>
<li><strong>trigger_http</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean variable. Any HTTP request (of a supported type) to the endpoint will trigger function execution. Supported HTTP request types are: POST, PUT, GET, DELETE, and OPTIONS. Endpoint is returned as <cite>https_trigger_url</cite>. Cannot be used with <cite>trigger_bucket</cite> and <cite>trigger_topic</cite>.</li>
<li><strong>trigger_topic</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of Pub/Sub topic. Every message published in this topic will trigger function execution with message contents passed as input data. Cannot be used with <cite>trigger_http</cite> and <cite>trigger_bucket</cite>.
Deprecated. Use <cite>event_trigger</cite> instead.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_gcp.cloudfunctions.Function.available_memory_mb">
<code class="descname">available_memory_mb</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.cloudfunctions.Function.available_memory_mb" title="Permalink to this definition">¶</a></dt>
<dd><p>Memory (in MB), available to the function. Default value is 256MB. Allowed values are: 128MB, 256MB, 512MB, 1024MB, and 2048MB.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.cloudfunctions.Function.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.cloudfunctions.Function.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Description of the function.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.cloudfunctions.Function.entry_point">
<code class="descname">entry_point</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.cloudfunctions.Function.entry_point" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of a JavaScript function that will be executed when the Google Cloud Function is triggered.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.cloudfunctions.Function.environment_variables">
<code class="descname">environment_variables</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.cloudfunctions.Function.environment_variables" title="Permalink to this definition">¶</a></dt>
<dd><p>A set of key/value environment variable pairs to assign to the function.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.cloudfunctions.Function.event_trigger">
<code class="descname">event_trigger</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.cloudfunctions.Function.event_trigger" title="Permalink to this definition">¶</a></dt>
<dd><p>A source that fires events in response to a condition in another service. Structure is documented below. Cannot be used with <cite>trigger_http</cite>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.cloudfunctions.Function.https_trigger_url">
<code class="descname">https_trigger_url</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.cloudfunctions.Function.https_trigger_url" title="Permalink to this definition">¶</a></dt>
<dd><p>URL which triggers function execution. Returned only if <cite>trigger_http</cite> is used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.cloudfunctions.Function.labels">
<code class="descname">labels</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.cloudfunctions.Function.labels" title="Permalink to this definition">¶</a></dt>
<dd><p>A set of key/value label pairs to assign to the function.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.cloudfunctions.Function.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.cloudfunctions.Function.name" title="Permalink to this definition">¶</a></dt>
<dd><p>A user-defined name of the function. Function names must be unique globally.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.cloudfunctions.Function.project">
<code class="descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.cloudfunctions.Function.project" title="Permalink to this definition">¶</a></dt>
<dd><p>Project of the function. If it is not provided, the provider project is used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.cloudfunctions.Function.region">
<code class="descname">region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.cloudfunctions.Function.region" title="Permalink to this definition">¶</a></dt>
<dd><p>Region of function. Currently can be only “us-central1”. If it is not provided, the provider region is used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.cloudfunctions.Function.retry_on_failure">
<code class="descname">retry_on_failure</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.cloudfunctions.Function.retry_on_failure" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the function should be retried on failure. This only applies to bucket and topic triggers, not HTTPS triggers.
Deprecated. Use <cite>event_trigger.failure_policy.retry</cite> instead.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.cloudfunctions.Function.runtime">
<code class="descname">runtime</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.cloudfunctions.Function.runtime" title="Permalink to this definition">¶</a></dt>
<dd><p>The runtime in which the function is going to run. If empty, defaults to <cite>“nodejs6”</cite>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.cloudfunctions.Function.source_archive_bucket">
<code class="descname">source_archive_bucket</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.cloudfunctions.Function.source_archive_bucket" title="Permalink to this definition">¶</a></dt>
<dd><p>The GCS bucket containing the zip archive which contains the function.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.cloudfunctions.Function.source_archive_object">
<code class="descname">source_archive_object</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.cloudfunctions.Function.source_archive_object" title="Permalink to this definition">¶</a></dt>
<dd><p>The source archive object (file) in archive bucket.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.cloudfunctions.Function.timeout">
<code class="descname">timeout</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.cloudfunctions.Function.timeout" title="Permalink to this definition">¶</a></dt>
<dd><p>Timeout (in seconds) for the function. Default value is 60 seconds. Cannot be more than 540 seconds.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.cloudfunctions.Function.trigger_bucket">
<code class="descname">trigger_bucket</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.cloudfunctions.Function.trigger_bucket" title="Permalink to this definition">¶</a></dt>
<dd><p>Google Cloud Storage bucket name. Every change in files in this bucket will trigger function execution. Cannot be used with <cite>trigger_http</cite> and <cite>trigger_topic</cite>.
Deprecated. Use <cite>event_trigger</cite> instead.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.cloudfunctions.Function.trigger_http">
<code class="descname">trigger_http</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.cloudfunctions.Function.trigger_http" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean variable. Any HTTP request (of a supported type) to the endpoint will trigger function execution. Supported HTTP request types are: POST, PUT, GET, DELETE, and OPTIONS. Endpoint is returned as <cite>https_trigger_url</cite>. Cannot be used with <cite>trigger_bucket</cite> and <cite>trigger_topic</cite>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.cloudfunctions.Function.trigger_topic">
<code class="descname">trigger_topic</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.cloudfunctions.Function.trigger_topic" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of Pub/Sub topic. Every message published in this topic will trigger function execution with message contents passed as input data. Cannot be used with <cite>trigger_http</cite> and <cite>trigger_bucket</cite>.
Deprecated. Use <cite>event_trigger</cite> instead.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.cloudfunctions.Function.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.cloudfunctions.Function.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.cloudfunctions.Function.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.cloudfunctions.Function.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.cloudfunctions.GetFunctionResult">
<em class="property">class </em><code class="descclassname">pulumi_gcp.cloudfunctions.</code><code class="descname">GetFunctionResult</code><span class="sig-paren">(</span><em>available_memory_mb=None</em>, <em>description=None</em>, <em>entry_point=None</em>, <em>environment_variables=None</em>, <em>event_triggers=None</em>, <em>https_trigger_url=None</em>, <em>labels=None</em>, <em>retry_on_failure=None</em>, <em>runtime=None</em>, <em>source_archive_bucket=None</em>, <em>source_archive_object=None</em>, <em>timeout=None</em>, <em>trigger_bucket=None</em>, <em>trigger_http=None</em>, <em>trigger_topic=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.cloudfunctions.GetFunctionResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getFunction.</p>
<dl class="attribute">
<dt id="pulumi_gcp.cloudfunctions.GetFunctionResult.available_memory_mb">
<code class="descname">available_memory_mb</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.cloudfunctions.GetFunctionResult.available_memory_mb" title="Permalink to this definition">¶</a></dt>
<dd><p>Available memory (in MB) to the function.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.cloudfunctions.GetFunctionResult.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.cloudfunctions.GetFunctionResult.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Description of the function.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.cloudfunctions.GetFunctionResult.entry_point">
<code class="descname">entry_point</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.cloudfunctions.GetFunctionResult.entry_point" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of a JavaScript function that will be executed when the Google Cloud Function is triggered.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.cloudfunctions.GetFunctionResult.event_triggers">
<code class="descname">event_triggers</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.cloudfunctions.GetFunctionResult.event_triggers" title="Permalink to this definition">¶</a></dt>
<dd><p>A source that fires events in response to a condition in another service. Structure is documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.cloudfunctions.GetFunctionResult.https_trigger_url">
<code class="descname">https_trigger_url</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.cloudfunctions.GetFunctionResult.https_trigger_url" title="Permalink to this definition">¶</a></dt>
<dd><p>If function is triggered by HTTP, trigger URL is set here.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.cloudfunctions.GetFunctionResult.labels">
<code class="descname">labels</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.cloudfunctions.GetFunctionResult.labels" title="Permalink to this definition">¶</a></dt>
<dd><p>A map of labels applied to this function.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.cloudfunctions.GetFunctionResult.runtime">
<code class="descname">runtime</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.cloudfunctions.GetFunctionResult.runtime" title="Permalink to this definition">¶</a></dt>
<dd><p>The runtime in which the function is running.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.cloudfunctions.GetFunctionResult.source_archive_bucket">
<code class="descname">source_archive_bucket</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.cloudfunctions.GetFunctionResult.source_archive_bucket" title="Permalink to this definition">¶</a></dt>
<dd><p>The GCS bucket containing the zip archive which contains the function.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.cloudfunctions.GetFunctionResult.source_archive_object">
<code class="descname">source_archive_object</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.cloudfunctions.GetFunctionResult.source_archive_object" title="Permalink to this definition">¶</a></dt>
<dd><p>The source archive object (file) in archive bucket.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.cloudfunctions.GetFunctionResult.timeout">
<code class="descname">timeout</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.cloudfunctions.GetFunctionResult.timeout" title="Permalink to this definition">¶</a></dt>
<dd><p>Function execution timeout (in seconds).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.cloudfunctions.GetFunctionResult.trigger_bucket">
<code class="descname">trigger_bucket</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.cloudfunctions.GetFunctionResult.trigger_bucket" title="Permalink to this definition">¶</a></dt>
<dd><p>If function is triggered by bucket, bucket name is set here. Deprecated. Use <cite>event_trigger</cite> instead.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.cloudfunctions.GetFunctionResult.trigger_http">
<code class="descname">trigger_http</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.cloudfunctions.GetFunctionResult.trigger_http" title="Permalink to this definition">¶</a></dt>
<dd><p>If function is triggered by HTTP, this boolean is set.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.cloudfunctions.GetFunctionResult.trigger_topic">
<code class="descname">trigger_topic</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.cloudfunctions.GetFunctionResult.trigger_topic" title="Permalink to this definition">¶</a></dt>
<dd><p>If function is triggered by Pub/Sub topic, name of topic is set here. Deprecated. Use <cite>event_trigger</cite> instead.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.cloudfunctions.GetFunctionResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.cloudfunctions.GetFunctionResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="function">
<dt id="pulumi_gcp.cloudfunctions.get_function">
<code class="descclassname">pulumi_gcp.cloudfunctions.</code><code class="descname">get_function</code><span class="sig-paren">(</span><em>name=None</em>, <em>project=None</em>, <em>region=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.cloudfunctions.get_function" title="Permalink to this definition">¶</a></dt>
<dd><p>Get information about a Google Cloud Function. For more information see
the [official documentation](<a class="reference external" href="https://cloud.google.com/functions/docs/">https://cloud.google.com/functions/docs/</a>)
and [API](<a class="reference external" href="https://cloud.google.com/functions/docs/apis">https://cloud.google.com/functions/docs/apis</a>).</p>
</dd></dl>

</div>
