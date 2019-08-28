---
title: Module cloudfunctions
---

<div class="section" id="cloudfunctions">
<h1>cloudfunctions<a class="headerlink" href="#cloudfunctions" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-gcp/issues">pulumi/pulumi-gcp repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/issues">terraform-providers/terraform-provider-google repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_gcp.cloudfunctions"></span><dl class="class">
<dt id="pulumi_gcp.cloudfunctions.AwaitableGetFunctionResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.cloudfunctions.</code><code class="sig-name descname">AwaitableGetFunctionResult</code><span class="sig-paren">(</span><em class="sig-param">available_memory_mb=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">entry_point=None</em>, <em class="sig-param">environment_variables=None</em>, <em class="sig-param">event_triggers=None</em>, <em class="sig-param">https_trigger_url=None</em>, <em class="sig-param">labels=None</em>, <em class="sig-param">max_instances=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">runtime=None</em>, <em class="sig-param">service_account_email=None</em>, <em class="sig-param">source_archive_bucket=None</em>, <em class="sig-param">source_archive_object=None</em>, <em class="sig-param">source_repositories=None</em>, <em class="sig-param">timeout=None</em>, <em class="sig-param">trigger_bucket=None</em>, <em class="sig-param">trigger_http=None</em>, <em class="sig-param">trigger_topic=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.cloudfunctions.AwaitableGetFunctionResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_gcp.cloudfunctions.Function">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.cloudfunctions.</code><code class="sig-name descname">Function</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">available_memory_mb=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">entry_point=None</em>, <em class="sig-param">environment_variables=None</em>, <em class="sig-param">event_trigger=None</em>, <em class="sig-param">https_trigger_url=None</em>, <em class="sig-param">labels=None</em>, <em class="sig-param">max_instances=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">runtime=None</em>, <em class="sig-param">service_account_email=None</em>, <em class="sig-param">source_archive_bucket=None</em>, <em class="sig-param">source_archive_object=None</em>, <em class="sig-param">source_repository=None</em>, <em class="sig-param">timeout=None</em>, <em class="sig-param">trigger_http=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.cloudfunctions.Function" title="Permalink to this definition">¶</a></dt>
<dd><p>Creates a new Cloud Function. For more information see
<a class="reference external" href="https://cloud.google.com/functions/docs/">the official documentation</a>
and
<a class="reference external" href="https://cloud.google.com/functions/docs/apis">API</a>.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>available_memory_mb</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Memory (in MB), available to the function. Default value is 256MB. Allowed values are: 128MB, 256MB, 512MB, 1024MB, and 2048MB.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Description of the function.</p></li>
<li><p><strong>entry_point</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the function that will be executed when the Google Cloud Function is triggered.</p></li>
<li><p><strong>environment_variables</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A set of key/value environment variable pairs to assign to the function.</p></li>
<li><p><strong>event_trigger</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A source that fires events in response to a condition in another service. Structure is documented below. Cannot be used with <code class="docutils literal notranslate"><span class="pre">trigger_http</span></code>.</p></li>
<li><p><strong>https_trigger_url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – URL which triggers function execution. Returned only if <code class="docutils literal notranslate"><span class="pre">trigger_http</span></code> is used.</p></li>
<li><p><strong>labels</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A set of key/value label pairs to assign to the function.</p></li>
<li><p><strong>max_instances</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The limit on the maximum number of function instances that may coexist at a given time.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A user-defined name of the function. Function names must be unique globally.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Project of the function. If it is not provided, the provider project is used.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Region of function. Currently can be only “us-central1”. If it is not provided, the provider region is used.</p></li>
<li><p><strong>runtime</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The runtime in which the function is going to run. One
of <code class="docutils literal notranslate"><span class="pre">&quot;nodejs6&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;nodejs8&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;nodejs10&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;python37&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;go111&quot;</span></code>. If empty,
defaults to <code class="docutils literal notranslate"><span class="pre">&quot;nodejs6&quot;</span></code>. It’s recommended that you override the default, as
<code class="docutils literal notranslate"><span class="pre">&quot;nodejs6&quot;</span></code> is deprecated.</p></li>
<li><p><strong>service_account_email</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – If provided, the self-provided service account to run the function with.</p></li>
<li><p><strong>source_archive_bucket</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The GCS bucket containing the zip archive which contains the function.</p></li>
<li><p><strong>source_archive_object</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The source archive object (file) in archive bucket.</p></li>
<li><p><strong>source_repository</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Represents parameters related to source repository where a function is hosted.
Cannot be set alongside <code class="docutils literal notranslate"><span class="pre">source_archive_bucket</span></code> or <code class="docutils literal notranslate"><span class="pre">source_archive_object</span></code>. Structure is documented below.</p></li>
<li><p><strong>timeout</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Timeout (in seconds) for the function. Default value is 60 seconds. Cannot be more than 540 seconds.</p></li>
<li><p><strong>trigger_http</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean variable. Any HTTP request (of a supported type) to the endpoint will trigger function execution. Supported HTTP request types are: POST, PUT, GET, DELETE, and OPTIONS. Endpoint is returned as <code class="docutils literal notranslate"><span class="pre">https_trigger_url</span></code>. Cannot be used with <code class="docutils literal notranslate"><span class="pre">trigger_bucket</span></code> and <code class="docutils literal notranslate"><span class="pre">trigger_topic</span></code>.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/cloudfunctions_function.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/cloudfunctions_function.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_gcp.cloudfunctions.Function.available_memory_mb">
<code class="sig-name descname">available_memory_mb</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.cloudfunctions.Function.available_memory_mb" title="Permalink to this definition">¶</a></dt>
<dd><p>Memory (in MB), available to the function. Default value is 256MB. Allowed values are: 128MB, 256MB, 512MB, 1024MB, and 2048MB.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.cloudfunctions.Function.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.cloudfunctions.Function.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Description of the function.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.cloudfunctions.Function.entry_point">
<code class="sig-name descname">entry_point</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.cloudfunctions.Function.entry_point" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the function that will be executed when the Google Cloud Function is triggered.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.cloudfunctions.Function.environment_variables">
<code class="sig-name descname">environment_variables</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.cloudfunctions.Function.environment_variables" title="Permalink to this definition">¶</a></dt>
<dd><p>A set of key/value environment variable pairs to assign to the function.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.cloudfunctions.Function.event_trigger">
<code class="sig-name descname">event_trigger</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.cloudfunctions.Function.event_trigger" title="Permalink to this definition">¶</a></dt>
<dd><p>A source that fires events in response to a condition in another service. Structure is documented below. Cannot be used with <code class="docutils literal notranslate"><span class="pre">trigger_http</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.cloudfunctions.Function.https_trigger_url">
<code class="sig-name descname">https_trigger_url</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.cloudfunctions.Function.https_trigger_url" title="Permalink to this definition">¶</a></dt>
<dd><p>URL which triggers function execution. Returned only if <code class="docutils literal notranslate"><span class="pre">trigger_http</span></code> is used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.cloudfunctions.Function.labels">
<code class="sig-name descname">labels</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.cloudfunctions.Function.labels" title="Permalink to this definition">¶</a></dt>
<dd><p>A set of key/value label pairs to assign to the function.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.cloudfunctions.Function.max_instances">
<code class="sig-name descname">max_instances</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.cloudfunctions.Function.max_instances" title="Permalink to this definition">¶</a></dt>
<dd><p>The limit on the maximum number of function instances that may coexist at a given time.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.cloudfunctions.Function.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.cloudfunctions.Function.name" title="Permalink to this definition">¶</a></dt>
<dd><p>A user-defined name of the function. Function names must be unique globally.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.cloudfunctions.Function.project">
<code class="sig-name descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.cloudfunctions.Function.project" title="Permalink to this definition">¶</a></dt>
<dd><p>Project of the function. If it is not provided, the provider project is used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.cloudfunctions.Function.region">
<code class="sig-name descname">region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.cloudfunctions.Function.region" title="Permalink to this definition">¶</a></dt>
<dd><p>Region of function. Currently can be only “us-central1”. If it is not provided, the provider region is used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.cloudfunctions.Function.runtime">
<code class="sig-name descname">runtime</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.cloudfunctions.Function.runtime" title="Permalink to this definition">¶</a></dt>
<dd><p>The runtime in which the function is going to run. One
of <code class="docutils literal notranslate"><span class="pre">&quot;nodejs6&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;nodejs8&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;nodejs10&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;python37&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;go111&quot;</span></code>. If empty,
defaults to <code class="docutils literal notranslate"><span class="pre">&quot;nodejs6&quot;</span></code>. It’s recommended that you override the default, as
<code class="docutils literal notranslate"><span class="pre">&quot;nodejs6&quot;</span></code> is deprecated.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.cloudfunctions.Function.service_account_email">
<code class="sig-name descname">service_account_email</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.cloudfunctions.Function.service_account_email" title="Permalink to this definition">¶</a></dt>
<dd><p>If provided, the self-provided service account to run the function with.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.cloudfunctions.Function.source_archive_bucket">
<code class="sig-name descname">source_archive_bucket</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.cloudfunctions.Function.source_archive_bucket" title="Permalink to this definition">¶</a></dt>
<dd><p>The GCS bucket containing the zip archive which contains the function.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.cloudfunctions.Function.source_archive_object">
<code class="sig-name descname">source_archive_object</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.cloudfunctions.Function.source_archive_object" title="Permalink to this definition">¶</a></dt>
<dd><p>The source archive object (file) in archive bucket.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.cloudfunctions.Function.source_repository">
<code class="sig-name descname">source_repository</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.cloudfunctions.Function.source_repository" title="Permalink to this definition">¶</a></dt>
<dd><p>Represents parameters related to source repository where a function is hosted.
Cannot be set alongside <code class="docutils literal notranslate"><span class="pre">source_archive_bucket</span></code> or <code class="docutils literal notranslate"><span class="pre">source_archive_object</span></code>. Structure is documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.cloudfunctions.Function.timeout">
<code class="sig-name descname">timeout</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.cloudfunctions.Function.timeout" title="Permalink to this definition">¶</a></dt>
<dd><p>Timeout (in seconds) for the function. Default value is 60 seconds. Cannot be more than 540 seconds.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.cloudfunctions.Function.trigger_http">
<code class="sig-name descname">trigger_http</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.cloudfunctions.Function.trigger_http" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean variable. Any HTTP request (of a supported type) to the endpoint will trigger function execution. Supported HTTP request types are: POST, PUT, GET, DELETE, and OPTIONS. Endpoint is returned as <code class="docutils literal notranslate"><span class="pre">https_trigger_url</span></code>. Cannot be used with <code class="docutils literal notranslate"><span class="pre">trigger_bucket</span></code> and <code class="docutils literal notranslate"><span class="pre">trigger_topic</span></code>.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.cloudfunctions.Function.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">available_memory_mb=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">entry_point=None</em>, <em class="sig-param">environment_variables=None</em>, <em class="sig-param">event_trigger=None</em>, <em class="sig-param">https_trigger_url=None</em>, <em class="sig-param">labels=None</em>, <em class="sig-param">max_instances=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">runtime=None</em>, <em class="sig-param">service_account_email=None</em>, <em class="sig-param">source_archive_bucket=None</em>, <em class="sig-param">source_archive_object=None</em>, <em class="sig-param">source_repository=None</em>, <em class="sig-param">timeout=None</em>, <em class="sig-param">trigger_http=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.cloudfunctions.Function.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Function resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.
:param str resource_name: The unique name of the resulting resource.
:param str id: The unique provider ID of the resource to lookup.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[float] available_memory_mb: Memory (in MB), available to the function. Default value is 256MB. Allowed values are: 128MB, 256MB, 512MB, 1024MB, and 2048MB.
:param pulumi.Input[str] description: Description of the function.
:param pulumi.Input[str] entry_point: Name of the function that will be executed when the Google Cloud Function is triggered.
:param pulumi.Input[dict] environment_variables: A set of key/value environment variable pairs to assign to the function.
:param pulumi.Input[dict] event_trigger: A source that fires events in response to a condition in another service. Structure is documented below. Cannot be used with <code class="docutils literal notranslate"><span class="pre">trigger_http</span></code>.
:param pulumi.Input[str] https_trigger_url: URL which triggers function execution. Returned only if <code class="docutils literal notranslate"><span class="pre">trigger_http</span></code> is used.
:param pulumi.Input[dict] labels: A set of key/value label pairs to assign to the function.
:param pulumi.Input[float] max_instances: The limit on the maximum number of function instances that may coexist at a given time.
:param pulumi.Input[str] name: A user-defined name of the function. Function names must be unique globally.
:param pulumi.Input[str] project: Project of the function. If it is not provided, the provider project is used.
:param pulumi.Input[str] region: Region of function. Currently can be only “us-central1”. If it is not provided, the provider region is used.
:param pulumi.Input[str] runtime: The runtime in which the function is going to run. One</p>
<blockquote>
<div><p>of <code class="docutils literal notranslate"><span class="pre">&quot;nodejs6&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;nodejs8&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;nodejs10&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;python37&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;go111&quot;</span></code>. If empty,
defaults to <code class="docutils literal notranslate"><span class="pre">&quot;nodejs6&quot;</span></code>. It’s recommended that you override the default, as
<code class="docutils literal notranslate"><span class="pre">&quot;nodejs6&quot;</span></code> is deprecated.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>service_account_email</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – If provided, the self-provided service account to run the function with.</p></li>
<li><p><strong>source_archive_bucket</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The GCS bucket containing the zip archive which contains the function.</p></li>
<li><p><strong>source_archive_object</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The source archive object (file) in archive bucket.</p></li>
<li><p><strong>source_repository</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Represents parameters related to source repository where a function is hosted.
Cannot be set alongside <code class="docutils literal notranslate"><span class="pre">source_archive_bucket</span></code> or <code class="docutils literal notranslate"><span class="pre">source_archive_object</span></code>. Structure is documented below.</p></li>
<li><p><strong>timeout</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Timeout (in seconds) for the function. Default value is 60 seconds. Cannot be more than 540 seconds.</p></li>
<li><p><strong>trigger_http</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean variable. Any HTTP request (of a supported type) to the endpoint will trigger function execution. Supported HTTP request types are: POST, PUT, GET, DELETE, and OPTIONS. Endpoint is returned as <code class="docutils literal notranslate"><span class="pre">https_trigger_url</span></code>. Cannot be used with <code class="docutils literal notranslate"><span class="pre">trigger_bucket</span></code> and <code class="docutils literal notranslate"><span class="pre">trigger_topic</span></code>.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/cloudfunctions_function.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/cloudfunctions_function.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.cloudfunctions.Function.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.cloudfunctions.Function.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.cloudfunctions.Function.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.cloudfunctions.Function.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.cloudfunctions.GetFunctionResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.cloudfunctions.</code><code class="sig-name descname">GetFunctionResult</code><span class="sig-paren">(</span><em class="sig-param">available_memory_mb=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">entry_point=None</em>, <em class="sig-param">environment_variables=None</em>, <em class="sig-param">event_triggers=None</em>, <em class="sig-param">https_trigger_url=None</em>, <em class="sig-param">labels=None</em>, <em class="sig-param">max_instances=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">runtime=None</em>, <em class="sig-param">service_account_email=None</em>, <em class="sig-param">source_archive_bucket=None</em>, <em class="sig-param">source_archive_object=None</em>, <em class="sig-param">source_repositories=None</em>, <em class="sig-param">timeout=None</em>, <em class="sig-param">trigger_bucket=None</em>, <em class="sig-param">trigger_http=None</em>, <em class="sig-param">trigger_topic=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.cloudfunctions.GetFunctionResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getFunction.</p>
<dl class="attribute">
<dt id="pulumi_gcp.cloudfunctions.GetFunctionResult.available_memory_mb">
<code class="sig-name descname">available_memory_mb</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.cloudfunctions.GetFunctionResult.available_memory_mb" title="Permalink to this definition">¶</a></dt>
<dd><p>Available memory (in MB) to the function.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.cloudfunctions.GetFunctionResult.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.cloudfunctions.GetFunctionResult.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Description of the function.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.cloudfunctions.GetFunctionResult.entry_point">
<code class="sig-name descname">entry_point</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.cloudfunctions.GetFunctionResult.entry_point" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of a JavaScript function that will be executed when the Google Cloud Function is triggered.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.cloudfunctions.GetFunctionResult.event_triggers">
<code class="sig-name descname">event_triggers</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.cloudfunctions.GetFunctionResult.event_triggers" title="Permalink to this definition">¶</a></dt>
<dd><p>A source that fires events in response to a condition in another service. Structure is documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.cloudfunctions.GetFunctionResult.https_trigger_url">
<code class="sig-name descname">https_trigger_url</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.cloudfunctions.GetFunctionResult.https_trigger_url" title="Permalink to this definition">¶</a></dt>
<dd><p>If function is triggered by HTTP, trigger URL is set here.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.cloudfunctions.GetFunctionResult.labels">
<code class="sig-name descname">labels</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.cloudfunctions.GetFunctionResult.labels" title="Permalink to this definition">¶</a></dt>
<dd><p>A map of labels applied to this function.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.cloudfunctions.GetFunctionResult.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.cloudfunctions.GetFunctionResult.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Cloud Function.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.cloudfunctions.GetFunctionResult.runtime">
<code class="sig-name descname">runtime</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.cloudfunctions.GetFunctionResult.runtime" title="Permalink to this definition">¶</a></dt>
<dd><p>The runtime in which the function is running.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.cloudfunctions.GetFunctionResult.source_archive_bucket">
<code class="sig-name descname">source_archive_bucket</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.cloudfunctions.GetFunctionResult.source_archive_bucket" title="Permalink to this definition">¶</a></dt>
<dd><p>The GCS bucket containing the zip archive which contains the function.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.cloudfunctions.GetFunctionResult.source_archive_object">
<code class="sig-name descname">source_archive_object</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.cloudfunctions.GetFunctionResult.source_archive_object" title="Permalink to this definition">¶</a></dt>
<dd><p>The source archive object (file) in archive bucket.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.cloudfunctions.GetFunctionResult.timeout">
<code class="sig-name descname">timeout</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.cloudfunctions.GetFunctionResult.timeout" title="Permalink to this definition">¶</a></dt>
<dd><p>Function execution timeout (in seconds).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.cloudfunctions.GetFunctionResult.trigger_http">
<code class="sig-name descname">trigger_http</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.cloudfunctions.GetFunctionResult.trigger_http" title="Permalink to this definition">¶</a></dt>
<dd><p>If function is triggered by HTTP, this boolean is set.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.cloudfunctions.GetFunctionResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.cloudfunctions.GetFunctionResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="function">
<dt id="pulumi_gcp.cloudfunctions.get_function">
<code class="sig-prename descclassname">pulumi_gcp.cloudfunctions.</code><code class="sig-name descname">get_function</code><span class="sig-paren">(</span><em class="sig-param">name=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.cloudfunctions.get_function" title="Permalink to this definition">¶</a></dt>
<dd><p>Get information about a Google Cloud Function. For more information see
the <a class="reference external" href="https://cloud.google.com/functions/docs/">official documentation</a>
and <a class="reference external" href="https://cloud.google.com/functions/docs/apis">API</a>.</p>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/d/cloudfunctions_function.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/d/cloudfunctions_function.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

</div>
