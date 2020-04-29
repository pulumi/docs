---
title: Module cloudscheduler
title_tag: Module cloudscheduler | Package pulumi_gcp | Python SDK
linktitle: cloudscheduler
notitle: true
---

<div class="section" id="cloudscheduler">
<h1>cloudscheduler<a class="headerlink" href="#cloudscheduler" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-gcp/issues">pulumi/pulumi-gcp repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/issues">terraform-providers/terraform-provider-google repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_gcp.cloudscheduler"></span><dl class="class">
<dt id="pulumi_gcp.cloudscheduler.Job">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.cloudscheduler.</code><code class="sig-name descname">Job</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">app_engine_http_target=None</em>, <em class="sig-param">attempt_deadline=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">http_target=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">pubsub_target=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">retry_config=None</em>, <em class="sig-param">schedule=None</em>, <em class="sig-param">time_zone=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.cloudscheduler.Job" title="Permalink to this definition">¶</a></dt>
<dd><p>A scheduled job that can publish a pubsub message or a http request
every X interval of time, using crontab format string.</p>
<p>To use Cloud Scheduler your project must contain an App Engine app
that is located in one of the supported regions. If your project
does not have an App Engine app, you must create one.</p>
<p>To get more information about Job, see:</p>
<ul class="simple">
<li><p><a class="reference external" href="https://cloud.google.com/scheduler/docs/reference/rest/">API documentation</a></p></li>
<li><p>How-to Guides</p>
<ul>
<li><p><a class="reference external" href="https://cloud.google.com/scheduler/">Official Documentation</a></p></li>
</ul>
</li>
</ul>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>app_engine_http_target</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – App Engine HTTP target.
If the job providers a App Engine HTTP target the cron will
send a request to the service instance  Structure is documented below.</p></li>
<li><p><strong>attempt_deadline</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The deadline for job attempts. If the request handler does not respond by this deadline then the request is
cancelled and the attempt is marked as a DEADLINE_EXCEEDED failure. The failed attempt can be viewed in
execution logs. Cloud Scheduler will retry the job according to the RetryConfig.
The allowed duration for this deadline is:</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="o">*</span> <span class="n">For</span> <span class="n">HTTP</span> <span class="n">targets</span><span class="p">,</span> <span class="n">between</span> <span class="mi">15</span> <span class="n">seconds</span> <span class="ow">and</span> <span class="mi">30</span> <span class="n">minutes</span><span class="o">.</span>
<span class="o">*</span> <span class="n">For</span> <span class="n">App</span> <span class="n">Engine</span> <span class="n">HTTP</span> <span class="n">targets</span><span class="p">,</span> <span class="n">between</span> <span class="mi">15</span> <span class="n">seconds</span> <span class="ow">and</span> <span class="mi">24</span> <span class="n">hours</span><span class="o">.</span>
<span class="n">A</span> <span class="n">duration</span> <span class="ow">in</span> <span class="n">seconds</span> <span class="k">with</span> <span class="n">up</span> <span class="n">to</span> <span class="n">nine</span> <span class="n">fractional</span> <span class="n">digits</span><span class="p">,</span> <span class="n">terminated</span> <span class="n">by</span> <span class="s1">&#39;s&#39;</span><span class="o">.</span> <span class="n">Example</span><span class="p">:</span> <span class="s2">&quot;3.5s&quot;</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A human-readable description for the job.
This string must not contain more than 500 characters.</p></li>
<li><p><strong>http_target</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – HTTP target.
If the job providers a http_target the cron will
send a request to the targeted url  Structure is documented below.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the job.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p></li>
<li><p><strong>pubsub_target</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Pub/Sub target
If the job providers a Pub/Sub target the cron will publish
a message to the provided topic  Structure is documented below.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Region where the scheduler job resides</p></li>
<li><p><strong>retry_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – By default, if a job does not complete successfully,
meaning that an acknowledgement is not received from the handler,
then it will be retried with exponential backoff according to the settings  Structure is documented below.</p></li>
<li><p><strong>schedule</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Describes the schedule on which the job will be executed.</p></li>
<li><p><strong>time_zone</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the time zone to be used in interpreting schedule.
The value of this field must be a time zone name from the tz database.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>app_engine_http_target</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">appEngineRouting</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - App Engine Routing setting for the job.  Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">instance</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - App instance.
By default, the job is sent to an instance which is available when the job is attempted.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">service</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - App service.
By default, the job is sent to the service which is the default service when the job is attempted.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">version</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - App version.
By default, the job is sent to the version which is the default version when the job is attempted.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">body</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - HTTP request body.
A request body is allowed only if the HTTP method is POST, PUT, or PATCH.
It is an error to set body on a job with an incompatible HttpMethod.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">headers</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - This map contains the header field names and values.
Repeated headers are not supported, but a header value can contain commas.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">httpMethod</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Which HTTP method to use for the request.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">relativeUri</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The relative URI.
The relative URL must begin with “/” and must be a valid HTTP relative URL.
It can contain a path, query string arguments, and # fragments.
If the relative URL is empty, then the root path “/” will be used.
No spaces are allowed, and the maximum length allowed is 2083 characters</p></li>
</ul>
<p>The <strong>http_target</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">body</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - HTTP request body.
A request body is allowed only if the HTTP method is POST, PUT, or PATCH.
It is an error to set body on a job with an incompatible HttpMethod.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">headers</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - This map contains the header field names and values.
Repeated headers are not supported, but a header value can contain commas.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">httpMethod</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Which HTTP method to use for the request.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">oauthToken</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Contains information needed for generating an OAuth token.
This type of authorization should be used when sending requests to a GCP endpoint.  Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">scope</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - OAuth scope to be used for generating OAuth access token. If not specified,
“<a class="reference external" href="https://www.googleapis.com/auth/cloud-platform">https://www.googleapis.com/auth/cloud-platform</a>” will be used.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">service_account_email</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Service account email to be used for generating OAuth token.
The service account must be within the same project as the job.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">oidcToken</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Contains information needed for generating an OpenID Connect token.
This type of authorization should be used when sending requests to third party endpoints or Cloud Run.  Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">audience</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Audience to be used when generating OIDC token. If not specified,
the URI specified in target will be used.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">service_account_email</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Service account email to be used for generating OAuth token.
The service account must be within the same project as the job.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">uri</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The full URI path that the request will be sent to.</p></li>
</ul>
<p>The <strong>pubsub_target</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">attributes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Attributes for PubsubMessage.
Pubsub message must contain either non-empty data, or at least one attribute.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">data</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The message payload for PubsubMessage.
Pubsub message must contain either non-empty data, or at least one attribute.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">topicName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The full resource name for the Cloud Pub/Sub topic to which
messages will be published when a job is delivered. ~&gt;<strong>NOTE</strong>:
The topic name must be in the same format as required by PubSub’s
PublishRequest.name, e.g. <code class="docutils literal notranslate"><span class="pre">projects/my-project/topics/my-topic</span></code>.</p></li>
</ul>
<p>The <strong>retry_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">maxBackoffDuration</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The maximum amount of time to wait before retrying a job after it fails.
A duration in seconds with up to nine fractional digits, terminated by ‘s’.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxDoublings</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The time between retries will double maxDoublings times.
A job’s retry interval starts at minBackoffDuration,
then doubles maxDoublings times, then increases linearly,
and finally retries retries at intervals of maxBackoffDuration up to retryCount times.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxRetryDuration</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The time limit for retrying a failed job, measured from time when an execution was first attempted.
If specified with retryCount, the job will be retried until both limits are reached.
A duration in seconds with up to nine fractional digits, terminated by ‘s’.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">minBackoffDuration</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The minimum amount of time to wait before retrying a job after it fails.
A duration in seconds with up to nine fractional digits, terminated by ‘s’.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">retryCount</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of attempts that the system will make to run a
job using the exponential backoff procedure described by maxDoublings.
Values greater than 5 and negative values are not allowed.</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_gcp.cloudscheduler.Job.app_engine_http_target">
<code class="sig-name descname">app_engine_http_target</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.cloudscheduler.Job.app_engine_http_target" title="Permalink to this definition">¶</a></dt>
<dd><p>App Engine HTTP target.
If the job providers a App Engine HTTP target the cron will
send a request to the service instance  Structure is documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">appEngineRouting</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - App Engine Routing setting for the job.  Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">instance</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - App instance.
By default, the job is sent to an instance which is available when the job is attempted.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">service</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - App service.
By default, the job is sent to the service which is the default service when the job is attempted.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">version</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - App version.
By default, the job is sent to the version which is the default version when the job is attempted.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">body</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - HTTP request body.
A request body is allowed only if the HTTP method is POST, PUT, or PATCH.
It is an error to set body on a job with an incompatible HttpMethod.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">headers</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - This map contains the header field names and values.
Repeated headers are not supported, but a header value can contain commas.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">httpMethod</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Which HTTP method to use for the request.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">relativeUri</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The relative URI.
The relative URL must begin with “/” and must be a valid HTTP relative URL.
It can contain a path, query string arguments, and # fragments.
If the relative URL is empty, then the root path “/” will be used.
No spaces are allowed, and the maximum length allowed is 2083 characters</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.cloudscheduler.Job.attempt_deadline">
<code class="sig-name descname">attempt_deadline</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.cloudscheduler.Job.attempt_deadline" title="Permalink to this definition">¶</a></dt>
<dd><p>The deadline for job attempts. If the request handler does not respond by this deadline then the request is
cancelled and the attempt is marked as a DEADLINE_EXCEEDED failure. The failed attempt can be viewed in
execution logs. Cloud Scheduler will retry the job according to the RetryConfig.
The allowed duration for this deadline is:</p>
<ul class="simple">
<li><p>For HTTP targets, between 15 seconds and 30 minutes.</p></li>
<li><p>For App Engine HTTP targets, between 15 seconds and 24 hours.
A duration in seconds with up to nine fractional digits, terminated by ‘s’. Example: “3.5s”</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.cloudscheduler.Job.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.cloudscheduler.Job.description" title="Permalink to this definition">¶</a></dt>
<dd><p>A human-readable description for the job.
This string must not contain more than 500 characters.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.cloudscheduler.Job.http_target">
<code class="sig-name descname">http_target</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.cloudscheduler.Job.http_target" title="Permalink to this definition">¶</a></dt>
<dd><p>HTTP target.
If the job providers a http_target the cron will
send a request to the targeted url  Structure is documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">body</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - HTTP request body.
A request body is allowed only if the HTTP method is POST, PUT, or PATCH.
It is an error to set body on a job with an incompatible HttpMethod.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">headers</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - This map contains the header field names and values.
Repeated headers are not supported, but a header value can contain commas.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">httpMethod</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Which HTTP method to use for the request.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">oauthToken</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - Contains information needed for generating an OAuth token.
This type of authorization should be used when sending requests to a GCP endpoint.  Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">scope</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - OAuth scope to be used for generating OAuth access token. If not specified,
“<a class="reference external" href="https://www.googleapis.com/auth/cloud-platform">https://www.googleapis.com/auth/cloud-platform</a>” will be used.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">service_account_email</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Service account email to be used for generating OAuth token.
The service account must be within the same project as the job.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">oidcToken</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - Contains information needed for generating an OpenID Connect token.
This type of authorization should be used when sending requests to third party endpoints or Cloud Run.  Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">audience</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Audience to be used when generating OIDC token. If not specified,
the URI specified in target will be used.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">service_account_email</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Service account email to be used for generating OAuth token.
The service account must be within the same project as the job.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">uri</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The full URI path that the request will be sent to.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.cloudscheduler.Job.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.cloudscheduler.Job.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the job.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.cloudscheduler.Job.project">
<code class="sig-name descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.cloudscheduler.Job.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.cloudscheduler.Job.pubsub_target">
<code class="sig-name descname">pubsub_target</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.cloudscheduler.Job.pubsub_target" title="Permalink to this definition">¶</a></dt>
<dd><p>Pub/Sub target
If the job providers a Pub/Sub target the cron will publish
a message to the provided topic  Structure is documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">attributes</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - Attributes for PubsubMessage.
Pubsub message must contain either non-empty data, or at least one attribute.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">data</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The message payload for PubsubMessage.
Pubsub message must contain either non-empty data, or at least one attribute.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">topicName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The full resource name for the Cloud Pub/Sub topic to which
messages will be published when a job is delivered. ~&gt;<strong>NOTE</strong>:
The topic name must be in the same format as required by PubSub’s
PublishRequest.name, e.g. <code class="docutils literal notranslate"><span class="pre">projects/my-project/topics/my-topic</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.cloudscheduler.Job.region">
<code class="sig-name descname">region</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.cloudscheduler.Job.region" title="Permalink to this definition">¶</a></dt>
<dd><p>Region where the scheduler job resides</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.cloudscheduler.Job.retry_config">
<code class="sig-name descname">retry_config</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.cloudscheduler.Job.retry_config" title="Permalink to this definition">¶</a></dt>
<dd><p>By default, if a job does not complete successfully,
meaning that an acknowledgement is not received from the handler,
then it will be retried with exponential backoff according to the settings  Structure is documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">maxBackoffDuration</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The maximum amount of time to wait before retrying a job after it fails.
A duration in seconds with up to nine fractional digits, terminated by ‘s’.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxDoublings</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The time between retries will double maxDoublings times.
A job’s retry interval starts at minBackoffDuration,
then doubles maxDoublings times, then increases linearly,
and finally retries retries at intervals of maxBackoffDuration up to retryCount times.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxRetryDuration</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The time limit for retrying a failed job, measured from time when an execution was first attempted.
If specified with retryCount, the job will be retried until both limits are reached.
A duration in seconds with up to nine fractional digits, terminated by ‘s’.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">minBackoffDuration</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The minimum amount of time to wait before retrying a job after it fails.
A duration in seconds with up to nine fractional digits, terminated by ‘s’.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">retryCount</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The number of attempts that the system will make to run a
job using the exponential backoff procedure described by maxDoublings.
Values greater than 5 and negative values are not allowed.</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.cloudscheduler.Job.schedule">
<code class="sig-name descname">schedule</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.cloudscheduler.Job.schedule" title="Permalink to this definition">¶</a></dt>
<dd><p>Describes the schedule on which the job will be executed.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.cloudscheduler.Job.time_zone">
<code class="sig-name descname">time_zone</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.cloudscheduler.Job.time_zone" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the time zone to be used in interpreting schedule.
The value of this field must be a time zone name from the tz database.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.cloudscheduler.Job.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">app_engine_http_target=None</em>, <em class="sig-param">attempt_deadline=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">http_target=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">pubsub_target=None</em>, <em class="sig-param">region=None</em>, <em class="sig-param">retry_config=None</em>, <em class="sig-param">schedule=None</em>, <em class="sig-param">time_zone=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.cloudscheduler.Job.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Job resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>app_engine_http_target</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – App Engine HTTP target.
If the job providers a App Engine HTTP target the cron will
send a request to the service instance  Structure is documented below.</p></li>
<li><p><strong>attempt_deadline</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The deadline for job attempts. If the request handler does not respond by this deadline then the request is
cancelled and the attempt is marked as a DEADLINE_EXCEEDED failure. The failed attempt can be viewed in
execution logs. Cloud Scheduler will retry the job according to the RetryConfig.
The allowed duration for this deadline is:</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="o">*</span> <span class="n">For</span> <span class="n">HTTP</span> <span class="n">targets</span><span class="p">,</span> <span class="n">between</span> <span class="mi">15</span> <span class="n">seconds</span> <span class="ow">and</span> <span class="mi">30</span> <span class="n">minutes</span><span class="o">.</span>
<span class="o">*</span> <span class="n">For</span> <span class="n">App</span> <span class="n">Engine</span> <span class="n">HTTP</span> <span class="n">targets</span><span class="p">,</span> <span class="n">between</span> <span class="mi">15</span> <span class="n">seconds</span> <span class="ow">and</span> <span class="mi">24</span> <span class="n">hours</span><span class="o">.</span>
<span class="n">A</span> <span class="n">duration</span> <span class="ow">in</span> <span class="n">seconds</span> <span class="k">with</span> <span class="n">up</span> <span class="n">to</span> <span class="n">nine</span> <span class="n">fractional</span> <span class="n">digits</span><span class="p">,</span> <span class="n">terminated</span> <span class="n">by</span> <span class="s1">&#39;s&#39;</span><span class="o">.</span> <span class="n">Example</span><span class="p">:</span> <span class="s2">&quot;3.5s&quot;</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A human-readable description for the job.
This string must not contain more than 500 characters.</p></li>
<li><p><strong>http_target</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – HTTP target.
If the job providers a http_target the cron will
send a request to the targeted url  Structure is documented below.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the job.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p></li>
<li><p><strong>pubsub_target</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Pub/Sub target
If the job providers a Pub/Sub target the cron will publish
a message to the provided topic  Structure is documented below.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Region where the scheduler job resides</p></li>
<li><p><strong>retry_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – By default, if a job does not complete successfully,
meaning that an acknowledgement is not received from the handler,
then it will be retried with exponential backoff according to the settings  Structure is documented below.</p></li>
<li><p><strong>schedule</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Describes the schedule on which the job will be executed.</p></li>
<li><p><strong>time_zone</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the time zone to be used in interpreting schedule.
The value of this field must be a time zone name from the tz database.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>app_engine_http_target</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">appEngineRouting</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - App Engine Routing setting for the job.  Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">instance</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - App instance.
By default, the job is sent to an instance which is available when the job is attempted.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">service</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - App service.
By default, the job is sent to the service which is the default service when the job is attempted.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">version</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - App version.
By default, the job is sent to the version which is the default version when the job is attempted.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">body</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - HTTP request body.
A request body is allowed only if the HTTP method is POST, PUT, or PATCH.
It is an error to set body on a job with an incompatible HttpMethod.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">headers</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - This map contains the header field names and values.
Repeated headers are not supported, but a header value can contain commas.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">httpMethod</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Which HTTP method to use for the request.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">relativeUri</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The relative URI.
The relative URL must begin with “/” and must be a valid HTTP relative URL.
It can contain a path, query string arguments, and # fragments.
If the relative URL is empty, then the root path “/” will be used.
No spaces are allowed, and the maximum length allowed is 2083 characters</p></li>
</ul>
<p>The <strong>http_target</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">body</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - HTTP request body.
A request body is allowed only if the HTTP method is POST, PUT, or PATCH.
It is an error to set body on a job with an incompatible HttpMethod.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">headers</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - This map contains the header field names and values.
Repeated headers are not supported, but a header value can contain commas.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">httpMethod</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Which HTTP method to use for the request.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">oauthToken</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Contains information needed for generating an OAuth token.
This type of authorization should be used when sending requests to a GCP endpoint.  Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">scope</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - OAuth scope to be used for generating OAuth access token. If not specified,
“<a class="reference external" href="https://www.googleapis.com/auth/cloud-platform">https://www.googleapis.com/auth/cloud-platform</a>” will be used.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">service_account_email</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Service account email to be used for generating OAuth token.
The service account must be within the same project as the job.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">oidcToken</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Contains information needed for generating an OpenID Connect token.
This type of authorization should be used when sending requests to third party endpoints or Cloud Run.  Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">audience</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Audience to be used when generating OIDC token. If not specified,
the URI specified in target will be used.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">service_account_email</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Service account email to be used for generating OAuth token.
The service account must be within the same project as the job.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">uri</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The full URI path that the request will be sent to.</p></li>
</ul>
<p>The <strong>pubsub_target</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">attributes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Attributes for PubsubMessage.
Pubsub message must contain either non-empty data, or at least one attribute.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">data</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The message payload for PubsubMessage.
Pubsub message must contain either non-empty data, or at least one attribute.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">topicName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The full resource name for the Cloud Pub/Sub topic to which
messages will be published when a job is delivered. ~&gt;<strong>NOTE</strong>:
The topic name must be in the same format as required by PubSub’s
PublishRequest.name, e.g. <code class="docutils literal notranslate"><span class="pre">projects/my-project/topics/my-topic</span></code>.</p></li>
</ul>
<p>The <strong>retry_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">maxBackoffDuration</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The maximum amount of time to wait before retrying a job after it fails.
A duration in seconds with up to nine fractional digits, terminated by ‘s’.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxDoublings</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The time between retries will double maxDoublings times.
A job’s retry interval starts at minBackoffDuration,
then doubles maxDoublings times, then increases linearly,
and finally retries retries at intervals of maxBackoffDuration up to retryCount times.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxRetryDuration</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The time limit for retrying a failed job, measured from time when an execution was first attempted.
If specified with retryCount, the job will be retried until both limits are reached.
A duration in seconds with up to nine fractional digits, terminated by ‘s’.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">minBackoffDuration</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The minimum amount of time to wait before retrying a job after it fails.
A duration in seconds with up to nine fractional digits, terminated by ‘s’.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">retryCount</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of attempts that the system will make to run a
job using the exponential backoff procedure described by maxDoublings.
Values greater than 5 and negative values are not allowed.</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.cloudscheduler.Job.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.cloudscheduler.Job.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.cloudscheduler.Job.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.cloudscheduler.Job.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
