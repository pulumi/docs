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
<dd><p>Create a Job resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[dict] app_engine_http_target: App Engine HTTP target. If the job providers a App Engine HTTP target the cron will send a request to the service</p>
<blockquote>
<div><p>instance</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>attempt_deadline</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The deadline for job attempts. If the request handler does not respond by this deadline then the request is cancelled
and the attempt is marked as a DEADLINE_EXCEEDED failure. The failed attempt can be viewed in execution logs. Cloud
Scheduler will retry the job according to the RetryConfig. The allowed duration for this deadline is: * For HTTP
targets, between 15 seconds and 30 minutes. * For App Engine HTTP targets, between 15 seconds and 24 hours. A duration
in seconds with up to nine fractional digits, terminated by ‘s’. Example: “3.5s”</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A human-readable description for the job. This string must not contain more than 500 characters.</p></li>
<li><p><strong>http_target</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – HTTP target. If the job providers a http_target the cron will send a request to the targeted url</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the job.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p></li>
<li><p><strong>pubsub_target</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Pub/Sub target If the job providers a Pub/Sub target the cron will publish a message to the provided topic</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Region where the scheduler job resides</p></li>
<li><p><strong>retry_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – By default, if a job does not complete successfully, meaning that an acknowledgement is not received from the handler,
then it will be retried with exponential backoff according to the settings</p></li>
<li><p><strong>schedule</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Describes the schedule on which the job will be executed.</p></li>
<li><p><strong>time_zone</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the time zone to be used in interpreting schedule. The value of this field must be a time zone name from the
tz database.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>app_engine_http_target</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">appEngineRouting</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">instance</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">service</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">version</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">body</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">headers</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">httpMethod</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">relativeUri</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>http_target</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">body</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">headers</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">httpMethod</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">oauthToken</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">scope</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">service_account_email</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">oidcToken</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">audience</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">service_account_email</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">uri</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>pubsub_target</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">attributes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">data</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">topicName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>retry_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">maxBackoffDuration</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxDoublings</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxRetryDuration</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">minBackoffDuration</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">retryCount</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_gcp.cloudscheduler.Job.app_engine_http_target">
<code class="sig-name descname">app_engine_http_target</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.cloudscheduler.Job.app_engine_http_target" title="Permalink to this definition">¶</a></dt>
<dd><p>App Engine HTTP target. If the job providers a App Engine HTTP target the cron will send a request to the service
instance</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">appEngineRouting</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">instance</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">service</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">version</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">body</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">headers</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">httpMethod</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">relativeUri</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.cloudscheduler.Job.attempt_deadline">
<code class="sig-name descname">attempt_deadline</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.cloudscheduler.Job.attempt_deadline" title="Permalink to this definition">¶</a></dt>
<dd><p>The deadline for job attempts. If the request handler does not respond by this deadline then the request is cancelled
and the attempt is marked as a DEADLINE_EXCEEDED failure. The failed attempt can be viewed in execution logs. Cloud
Scheduler will retry the job according to the RetryConfig. The allowed duration for this deadline is: * For HTTP
targets, between 15 seconds and 30 minutes. * For App Engine HTTP targets, between 15 seconds and 24 hours. A duration
in seconds with up to nine fractional digits, terminated by ‘s’. Example: “3.5s”</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.cloudscheduler.Job.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.cloudscheduler.Job.description" title="Permalink to this definition">¶</a></dt>
<dd><p>A human-readable description for the job. This string must not contain more than 500 characters.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.cloudscheduler.Job.http_target">
<code class="sig-name descname">http_target</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.cloudscheduler.Job.http_target" title="Permalink to this definition">¶</a></dt>
<dd><p>HTTP target. If the job providers a http_target the cron will send a request to the targeted url</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">body</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">headers</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">httpMethod</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">oauthToken</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">scope</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">service_account_email</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">oidcToken</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">audience</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">service_account_email</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">uri</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
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
<dd><p>Pub/Sub target If the job providers a Pub/Sub target the cron will publish a message to the provided topic</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">attributes</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">data</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">topicName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
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
<dd><p>By default, if a job does not complete successfully, meaning that an acknowledgement is not received from the handler,
then it will be retried with exponential backoff according to the settings</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">maxBackoffDuration</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxDoublings</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxRetryDuration</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">minBackoffDuration</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">retryCount</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
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
<dd><p>Specifies the time zone to be used in interpreting schedule. The value of this field must be a time zone name from the
tz database.</p>
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
<li><p><strong>app_engine_http_target</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – App Engine HTTP target. If the job providers a App Engine HTTP target the cron will send a request to the service
instance</p></li>
<li><p><strong>attempt_deadline</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The deadline for job attempts. If the request handler does not respond by this deadline then the request is cancelled
and the attempt is marked as a DEADLINE_EXCEEDED failure. The failed attempt can be viewed in execution logs. Cloud
Scheduler will retry the job according to the RetryConfig. The allowed duration for this deadline is: * For HTTP
targets, between 15 seconds and 30 minutes. * For App Engine HTTP targets, between 15 seconds and 24 hours. A duration
in seconds with up to nine fractional digits, terminated by ‘s’. Example: “3.5s”</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A human-readable description for the job. This string must not contain more than 500 characters.</p></li>
<li><p><strong>http_target</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – HTTP target. If the job providers a http_target the cron will send a request to the targeted url</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the job.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p></li>
<li><p><strong>pubsub_target</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Pub/Sub target If the job providers a Pub/Sub target the cron will publish a message to the provided topic</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Region where the scheduler job resides</p></li>
<li><p><strong>retry_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – By default, if a job does not complete successfully, meaning that an acknowledgement is not received from the handler,
then it will be retried with exponential backoff according to the settings</p></li>
<li><p><strong>schedule</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Describes the schedule on which the job will be executed.</p></li>
<li><p><strong>time_zone</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the time zone to be used in interpreting schedule. The value of this field must be a time zone name from the
tz database.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>app_engine_http_target</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">appEngineRouting</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">instance</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">service</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">version</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">body</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">headers</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">httpMethod</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">relativeUri</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>http_target</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">body</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">headers</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">httpMethod</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">oauthToken</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">scope</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">service_account_email</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">oidcToken</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">audience</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">service_account_email</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">uri</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>pubsub_target</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">attributes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">data</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">topicName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>retry_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">maxBackoffDuration</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxDoublings</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxRetryDuration</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">minBackoffDuration</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">retryCount</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
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
