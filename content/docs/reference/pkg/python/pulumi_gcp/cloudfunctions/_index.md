---
title: Module cloudfunctions
title_tag: Module cloudfunctions | Package pulumi_gcp | Python SDK
linktitle: cloudfunctions
notitle: true
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
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.cloudfunctions.</code><code class="sig-name descname">AwaitableGetFunctionResult</code><span class="sig-paren">(</span><em class="sig-param">available_memory_mb=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">entry_point=None</em>, <em class="sig-param">environment_variables=None</em>, <em class="sig-param">event_triggers=None</em>, <em class="sig-param">https_trigger_url=None</em>, <em class="sig-param">labels=None</em>, <em class="sig-param">max_instances=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">runtime=None</em>, <em class="sig-param">service_account_email=None</em>, <em class="sig-param">source_archive_bucket=None</em>, <em class="sig-param">source_archive_object=None</em>, <em class="sig-param">source_repositories=None</em>, <em class="sig-param">timeout=None</em>, <em class="sig-param">trigger_http=None</em>, <em class="sig-param">vpc_connector=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.cloudfunctions.AwaitableGetFunctionResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_gcp.cloudfunctions.Function">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.cloudfunctions.</code><code class="sig-name descname">Function</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">available_memory_mb=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">entry_point=None</em>, <em class="sig-param">environment_variables=None</em>, <em class="sig-param">event_trigger=None</em>, <em class="sig-param">https_trigger_url=None</em>, <em class="sig-param">labels=None</em>, <em class="sig-param">max_instances=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">runtime=None</em>, <em class="sig-param">service_account_email=None</em>, <em class="sig-param">source_archive_bucket=None</em>, <em class="sig-param">source_archive_object=None</em>, <em class="sig-param">source_repository=None</em>, <em class="sig-param">timeout=None</em>, <em class="sig-param">trigger_http=None</em>, <em class="sig-param">vpc_connector=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.cloudfunctions.Function" title="Permalink to this definition">¶</a></dt>
<dd><p>Creates a new Cloud Function. For more information see
<a class="reference external" href="https://cloud.google.com/functions/docs/">the official documentation</a>
and
<a class="reference external" href="https://cloud.google.com/functions/docs/apis">API</a>.</p>
<blockquote>
<div><p><strong>Warning:</strong> As of November 1, 2019, newly created Functions are
private-by-default and will require <a class="reference external" href="https://cloud.google.com/functions/docs/reference/iam/roles">appropriate IAM permissions</a>
to be invoked. See below examples for how to set up the appropriate permissions,
or view the <a class="reference external" href="https://www.terraform.io/docs/providers/google/r/cloudfunctions_cloud_function_iam.html">Cloud Functions IAM resources</a>
for Cloud Functions.</p>
</div></blockquote>
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
<li><p><strong>runtime</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The runtime in which the function is going to run.
Eg. <code class="docutils literal notranslate"><span class="pre">&quot;nodejs8&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;nodejs10&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;python37&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;go111&quot;</span></code>.</p></li>
<li><p><strong>service_account_email</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – If provided, the self-provided service account to run the function with.</p></li>
<li><p><strong>source_archive_bucket</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The GCS bucket containing the zip archive which contains the function.</p></li>
<li><p><strong>source_archive_object</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The source archive object (file) in archive bucket.</p></li>
<li><p><strong>source_repository</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Represents parameters related to source repository where a function is hosted.
Cannot be set alongside <code class="docutils literal notranslate"><span class="pre">source_archive_bucket</span></code> or <code class="docutils literal notranslate"><span class="pre">source_archive_object</span></code>. Structure is documented below.</p></li>
<li><p><strong>timeout</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Timeout (in seconds) for the function. Default value is 60 seconds. Cannot be more than 540 seconds.</p></li>
<li><p><strong>trigger_http</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean variable. Any HTTP request (of a supported type) to the endpoint will trigger function execution. Supported HTTP request types are: POST, PUT, GET, DELETE, and OPTIONS. Endpoint is returned as <code class="docutils literal notranslate"><span class="pre">https_trigger_url</span></code>. Cannot be used with <code class="docutils literal notranslate"><span class="pre">trigger_bucket</span></code> and <code class="docutils literal notranslate"><span class="pre">trigger_topic</span></code>.</p></li>
<li><p><strong>vpc_connector</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The VPC Network Connector that this cloud function can connect to. It can be either the fully-qualified URI, or the short name of the network connector resource. The format of this field is <code class="docutils literal notranslate"><span class="pre">projects/*/locations/*/connectors/*</span></code>.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>event_trigger</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">eventType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">failurePolicy</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">retry</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">resource</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>source_repository</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">deployedUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">url</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
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
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">eventType</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">failurePolicy</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">retry</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">resource</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
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
<dd><p>The runtime in which the function is going to run.
Eg. <code class="docutils literal notranslate"><span class="pre">&quot;nodejs8&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;nodejs10&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;python37&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;go111&quot;</span></code>.</p>
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
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">deployedUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">url</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
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

<dl class="attribute">
<dt id="pulumi_gcp.cloudfunctions.Function.vpc_connector">
<code class="sig-name descname">vpc_connector</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.cloudfunctions.Function.vpc_connector" title="Permalink to this definition">¶</a></dt>
<dd><p>The VPC Network Connector that this cloud function can connect to. It can be either the fully-qualified URI, or the short name of the network connector resource. The format of this field is <code class="docutils literal notranslate"><span class="pre">projects/*/locations/*/connectors/*</span></code>.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.cloudfunctions.Function.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">available_memory_mb=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">entry_point=None</em>, <em class="sig-param">environment_variables=None</em>, <em class="sig-param">event_trigger=None</em>, <em class="sig-param">https_trigger_url=None</em>, <em class="sig-param">labels=None</em>, <em class="sig-param">max_instances=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">runtime=None</em>, <em class="sig-param">service_account_email=None</em>, <em class="sig-param">source_archive_bucket=None</em>, <em class="sig-param">source_archive_object=None</em>, <em class="sig-param">source_repository=None</em>, <em class="sig-param">timeout=None</em>, <em class="sig-param">trigger_http=None</em>, <em class="sig-param">vpc_connector=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.cloudfunctions.Function.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Function resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
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
<li><p><strong>runtime</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The runtime in which the function is going to run.
Eg. <code class="docutils literal notranslate"><span class="pre">&quot;nodejs8&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;nodejs10&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;python37&quot;</span></code>, <code class="docutils literal notranslate"><span class="pre">&quot;go111&quot;</span></code>.</p></li>
<li><p><strong>service_account_email</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – If provided, the self-provided service account to run the function with.</p></li>
<li><p><strong>source_archive_bucket</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The GCS bucket containing the zip archive which contains the function.</p></li>
<li><p><strong>source_archive_object</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The source archive object (file) in archive bucket.</p></li>
<li><p><strong>source_repository</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Represents parameters related to source repository where a function is hosted.
Cannot be set alongside <code class="docutils literal notranslate"><span class="pre">source_archive_bucket</span></code> or <code class="docutils literal notranslate"><span class="pre">source_archive_object</span></code>. Structure is documented below.</p></li>
<li><p><strong>timeout</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Timeout (in seconds) for the function. Default value is 60 seconds. Cannot be more than 540 seconds.</p></li>
<li><p><strong>trigger_http</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean variable. Any HTTP request (of a supported type) to the endpoint will trigger function execution. Supported HTTP request types are: POST, PUT, GET, DELETE, and OPTIONS. Endpoint is returned as <code class="docutils literal notranslate"><span class="pre">https_trigger_url</span></code>. Cannot be used with <code class="docutils literal notranslate"><span class="pre">trigger_bucket</span></code> and <code class="docutils literal notranslate"><span class="pre">trigger_topic</span></code>.</p></li>
<li><p><strong>vpc_connector</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The VPC Network Connector that this cloud function can connect to. It can be either the fully-qualified URI, or the short name of the network connector resource. The format of this field is <code class="docutils literal notranslate"><span class="pre">projects/*/locations/*/connectors/*</span></code>.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>event_trigger</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">eventType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">failurePolicy</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">retry</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">resource</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>source_repository</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">deployedUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">url</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
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
<dt id="pulumi_gcp.cloudfunctions.FunctionIamBinding">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.cloudfunctions.</code><code class="sig-name descname">FunctionIamBinding</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">cloud_function=None</em>, <em class="sig-param">condition=None</em>, <em class="sig-param">members=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">role=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.cloudfunctions.FunctionIamBinding" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a FunctionIamBinding resource with the given unique name, props, and options.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>cloud_function</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Used to find the parent resource to bind the IAM policy to</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs.
If it is not provided, the project will be parsed from the identifier of the parent resource. If no project is provided in the parent identifier and no project is specified, the provider project is used.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The location of this cloud function. Used to find the parent resource to bind the IAM policy to. If not specified,
the value will be parsed from the identifier of the parent resource. If no region is provided in the parent identifier and no
region is specified, it is taken from the provider configuration.</p></li>
<li><p><strong>role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The role that should be applied. Only one
<code class="docutils literal notranslate"><span class="pre">cloudfunctions.FunctionIamBinding</span></code> can be used per role. Note that custom roles must be of the format
<code class="docutils literal notranslate"><span class="pre">[projects|organizations]/{parent-name}/roles/{role-name}</span></code>.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>condition</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">description</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">expression</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">title</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/cloudfunctions_function_iam_binding.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/cloudfunctions_function_iam_binding.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_gcp.cloudfunctions.FunctionIamBinding.cloud_function">
<code class="sig-name descname">cloud_function</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.cloudfunctions.FunctionIamBinding.cloud_function" title="Permalink to this definition">¶</a></dt>
<dd><p>Used to find the parent resource to bind the IAM policy to</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.cloudfunctions.FunctionIamBinding.etag">
<code class="sig-name descname">etag</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.cloudfunctions.FunctionIamBinding.etag" title="Permalink to this definition">¶</a></dt>
<dd><p>(Computed) The etag of the IAM policy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.cloudfunctions.FunctionIamBinding.project">
<code class="sig-name descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.cloudfunctions.FunctionIamBinding.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs.
If it is not provided, the project will be parsed from the identifier of the parent resource. If no project is provided in the parent identifier and no project is specified, the provider project is used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.cloudfunctions.FunctionIamBinding.region">
<code class="sig-name descname">region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.cloudfunctions.FunctionIamBinding.region" title="Permalink to this definition">¶</a></dt>
<dd><p>The location of this cloud function. Used to find the parent resource to bind the IAM policy to. If not specified,
the value will be parsed from the identifier of the parent resource. If no region is provided in the parent identifier and no
region is specified, it is taken from the provider configuration.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.cloudfunctions.FunctionIamBinding.role">
<code class="sig-name descname">role</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.cloudfunctions.FunctionIamBinding.role" title="Permalink to this definition">¶</a></dt>
<dd><p>The role that should be applied. Only one
<code class="docutils literal notranslate"><span class="pre">cloudfunctions.FunctionIamBinding</span></code> can be used per role. Note that custom roles must be of the format
<code class="docutils literal notranslate"><span class="pre">[projects|organizations]/{parent-name}/roles/{role-name}</span></code>.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.cloudfunctions.FunctionIamBinding.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">cloud_function=None</em>, <em class="sig-param">condition=None</em>, <em class="sig-param">etag=None</em>, <em class="sig-param">members=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">role=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.cloudfunctions.FunctionIamBinding.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing FunctionIamBinding resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>cloud_function</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Used to find the parent resource to bind the IAM policy to</p></li>
<li><p><strong>etag</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – (Computed) The etag of the IAM policy.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs.
If it is not provided, the project will be parsed from the identifier of the parent resource. If no project is provided in the parent identifier and no project is specified, the provider project is used.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The location of this cloud function. Used to find the parent resource to bind the IAM policy to. If not specified,
the value will be parsed from the identifier of the parent resource. If no region is provided in the parent identifier and no
region is specified, it is taken from the provider configuration.</p></li>
<li><p><strong>role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The role that should be applied. Only one
<code class="docutils literal notranslate"><span class="pre">cloudfunctions.FunctionIamBinding</span></code> can be used per role. Note that custom roles must be of the format
<code class="docutils literal notranslate"><span class="pre">[projects|organizations]/{parent-name}/roles/{role-name}</span></code>.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>condition</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">description</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">expression</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">title</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/cloudfunctions_function_iam_binding.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/cloudfunctions_function_iam_binding.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.cloudfunctions.FunctionIamBinding.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.cloudfunctions.FunctionIamBinding.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.cloudfunctions.FunctionIamBinding.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.cloudfunctions.FunctionIamBinding.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.cloudfunctions.FunctionIamMember">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.cloudfunctions.</code><code class="sig-name descname">FunctionIamMember</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">cloud_function=None</em>, <em class="sig-param">condition=None</em>, <em class="sig-param">member=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">role=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.cloudfunctions.FunctionIamMember" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a FunctionIamMember resource with the given unique name, props, and options.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>cloud_function</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Used to find the parent resource to bind the IAM policy to</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs.
If it is not provided, the project will be parsed from the identifier of the parent resource. If no project is provided in the parent identifier and no project is specified, the provider project is used.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The location of this cloud function. Used to find the parent resource to bind the IAM policy to. If not specified,
the value will be parsed from the identifier of the parent resource. If no region is provided in the parent identifier and no
region is specified, it is taken from the provider configuration.</p></li>
<li><p><strong>role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The role that should be applied. Only one
<code class="docutils literal notranslate"><span class="pre">cloudfunctions.FunctionIamBinding</span></code> can be used per role. Note that custom roles must be of the format
<code class="docutils literal notranslate"><span class="pre">[projects|organizations]/{parent-name}/roles/{role-name}</span></code>.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>condition</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">description</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">expression</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">title</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/cloudfunctions_function_iam_member.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/cloudfunctions_function_iam_member.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_gcp.cloudfunctions.FunctionIamMember.cloud_function">
<code class="sig-name descname">cloud_function</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.cloudfunctions.FunctionIamMember.cloud_function" title="Permalink to this definition">¶</a></dt>
<dd><p>Used to find the parent resource to bind the IAM policy to</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.cloudfunctions.FunctionIamMember.etag">
<code class="sig-name descname">etag</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.cloudfunctions.FunctionIamMember.etag" title="Permalink to this definition">¶</a></dt>
<dd><p>(Computed) The etag of the IAM policy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.cloudfunctions.FunctionIamMember.project">
<code class="sig-name descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.cloudfunctions.FunctionIamMember.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs.
If it is not provided, the project will be parsed from the identifier of the parent resource. If no project is provided in the parent identifier and no project is specified, the provider project is used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.cloudfunctions.FunctionIamMember.region">
<code class="sig-name descname">region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.cloudfunctions.FunctionIamMember.region" title="Permalink to this definition">¶</a></dt>
<dd><p>The location of this cloud function. Used to find the parent resource to bind the IAM policy to. If not specified,
the value will be parsed from the identifier of the parent resource. If no region is provided in the parent identifier and no
region is specified, it is taken from the provider configuration.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.cloudfunctions.FunctionIamMember.role">
<code class="sig-name descname">role</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.cloudfunctions.FunctionIamMember.role" title="Permalink to this definition">¶</a></dt>
<dd><p>The role that should be applied. Only one
<code class="docutils literal notranslate"><span class="pre">cloudfunctions.FunctionIamBinding</span></code> can be used per role. Note that custom roles must be of the format
<code class="docutils literal notranslate"><span class="pre">[projects|organizations]/{parent-name}/roles/{role-name}</span></code>.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.cloudfunctions.FunctionIamMember.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">cloud_function=None</em>, <em class="sig-param">condition=None</em>, <em class="sig-param">etag=None</em>, <em class="sig-param">member=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">role=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.cloudfunctions.FunctionIamMember.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing FunctionIamMember resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>cloud_function</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Used to find the parent resource to bind the IAM policy to</p></li>
<li><p><strong>etag</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – (Computed) The etag of the IAM policy.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs.
If it is not provided, the project will be parsed from the identifier of the parent resource. If no project is provided in the parent identifier and no project is specified, the provider project is used.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The location of this cloud function. Used to find the parent resource to bind the IAM policy to. If not specified,
the value will be parsed from the identifier of the parent resource. If no region is provided in the parent identifier and no
region is specified, it is taken from the provider configuration.</p></li>
<li><p><strong>role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The role that should be applied. Only one
<code class="docutils literal notranslate"><span class="pre">cloudfunctions.FunctionIamBinding</span></code> can be used per role. Note that custom roles must be of the format
<code class="docutils literal notranslate"><span class="pre">[projects|organizations]/{parent-name}/roles/{role-name}</span></code>.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>condition</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">description</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">expression</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">title</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/cloudfunctions_function_iam_member.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/cloudfunctions_function_iam_member.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.cloudfunctions.FunctionIamMember.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.cloudfunctions.FunctionIamMember.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.cloudfunctions.FunctionIamMember.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.cloudfunctions.FunctionIamMember.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.cloudfunctions.FunctionIamPolicy">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.cloudfunctions.</code><code class="sig-name descname">FunctionIamPolicy</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">cloud_function=None</em>, <em class="sig-param">policy_data=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.cloudfunctions.FunctionIamPolicy" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a FunctionIamPolicy resource with the given unique name, props, and options.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>cloud_function</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Used to find the parent resource to bind the IAM policy to</p></li>
<li><p><strong>policy_data</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The policy data generated by
a <code class="docutils literal notranslate"><span class="pre">organizations.getIAMPolicy</span></code> data source.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs.
If it is not provided, the project will be parsed from the identifier of the parent resource. If no project is provided in the parent identifier and no project is specified, the provider project is used.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The location of this cloud function. Used to find the parent resource to bind the IAM policy to. If not specified,
the value will be parsed from the identifier of the parent resource. If no region is provided in the parent identifier and no
region is specified, it is taken from the provider configuration.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/cloudfunctions_function_iam_policy.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/cloudfunctions_function_iam_policy.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_gcp.cloudfunctions.FunctionIamPolicy.cloud_function">
<code class="sig-name descname">cloud_function</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.cloudfunctions.FunctionIamPolicy.cloud_function" title="Permalink to this definition">¶</a></dt>
<dd><p>Used to find the parent resource to bind the IAM policy to</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.cloudfunctions.FunctionIamPolicy.etag">
<code class="sig-name descname">etag</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.cloudfunctions.FunctionIamPolicy.etag" title="Permalink to this definition">¶</a></dt>
<dd><p>(Computed) The etag of the IAM policy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.cloudfunctions.FunctionIamPolicy.policy_data">
<code class="sig-name descname">policy_data</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.cloudfunctions.FunctionIamPolicy.policy_data" title="Permalink to this definition">¶</a></dt>
<dd><p>The policy data generated by
a <code class="docutils literal notranslate"><span class="pre">organizations.getIAMPolicy</span></code> data source.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.cloudfunctions.FunctionIamPolicy.project">
<code class="sig-name descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.cloudfunctions.FunctionIamPolicy.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs.
If it is not provided, the project will be parsed from the identifier of the parent resource. If no project is provided in the parent identifier and no project is specified, the provider project is used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.cloudfunctions.FunctionIamPolicy.region">
<code class="sig-name descname">region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.cloudfunctions.FunctionIamPolicy.region" title="Permalink to this definition">¶</a></dt>
<dd><p>The location of this cloud function. Used to find the parent resource to bind the IAM policy to. If not specified,
the value will be parsed from the identifier of the parent resource. If no region is provided in the parent identifier and no
region is specified, it is taken from the provider configuration.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.cloudfunctions.FunctionIamPolicy.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">cloud_function=None</em>, <em class="sig-param">etag=None</em>, <em class="sig-param">policy_data=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">region=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.cloudfunctions.FunctionIamPolicy.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing FunctionIamPolicy resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>cloud_function</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Used to find the parent resource to bind the IAM policy to</p></li>
<li><p><strong>etag</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – (Computed) The etag of the IAM policy.</p></li>
<li><p><strong>policy_data</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The policy data generated by
a <code class="docutils literal notranslate"><span class="pre">organizations.getIAMPolicy</span></code> data source.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs.
If it is not provided, the project will be parsed from the identifier of the parent resource. If no project is provided in the parent identifier and no project is specified, the provider project is used.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The location of this cloud function. Used to find the parent resource to bind the IAM policy to. If not specified,
the value will be parsed from the identifier of the parent resource. If no region is provided in the parent identifier and no
region is specified, it is taken from the provider configuration.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/cloudfunctions_function_iam_policy.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/cloudfunctions_function_iam_policy.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.cloudfunctions.FunctionIamPolicy.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.cloudfunctions.FunctionIamPolicy.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.cloudfunctions.FunctionIamPolicy.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.cloudfunctions.FunctionIamPolicy.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.cloudfunctions.</code><code class="sig-name descname">GetFunctionResult</code><span class="sig-paren">(</span><em class="sig-param">available_memory_mb=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">entry_point=None</em>, <em class="sig-param">environment_variables=None</em>, <em class="sig-param">event_triggers=None</em>, <em class="sig-param">https_trigger_url=None</em>, <em class="sig-param">labels=None</em>, <em class="sig-param">max_instances=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">runtime=None</em>, <em class="sig-param">service_account_email=None</em>, <em class="sig-param">source_archive_bucket=None</em>, <em class="sig-param">source_archive_object=None</em>, <em class="sig-param">source_repositories=None</em>, <em class="sig-param">timeout=None</em>, <em class="sig-param">trigger_http=None</em>, <em class="sig-param">vpc_connector=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.cloudfunctions.GetFunctionResult" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.cloudfunctions.GetFunctionResult.service_account_email">
<code class="sig-name descname">service_account_email</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.cloudfunctions.GetFunctionResult.service_account_email" title="Permalink to this definition">¶</a></dt>
<dd><p>The service account email to be assumed by the cloud function.</p>
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
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>name</strong> (<em>str</em>) – The name of a Cloud Function.</p></li>
<li><p><strong>project</strong> (<em>str</em>) – The project in which the resource belongs. If it
is not provided, the provider project is used.</p></li>
<li><p><strong>region</strong> (<em>str</em>) – The region in which the resource belongs. If it
is not provided, the provider region is used.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/d/cloudfunctions_function.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/d/cloudfunctions_function.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

</div>
