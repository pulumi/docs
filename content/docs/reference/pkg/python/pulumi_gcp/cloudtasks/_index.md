---
title: Module cloudtasks
title_tag: Module cloudtasks | Package pulumi_gcp | Python SDK
linktitle: cloudtasks
notitle: true
---

<div class="section" id="cloudtasks">
<h1>cloudtasks<a class="headerlink" href="#cloudtasks" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-gcp/issues">pulumi/pulumi-gcp repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/issues">terraform-providers/terraform-provider-google repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_gcp.cloudtasks"></span><dl class="py class">
<dt id="pulumi_gcp.cloudtasks.Queue">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.cloudtasks.</code><code class="sig-name descname">Queue</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">app_engine_routing_override</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">location</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">rate_limits</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">retry_config</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.cloudtasks.Queue" title="Permalink to this definition">¶</a></dt>
<dd><p>A named resource to which messages are sent by publishers.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>app_engine_routing_override</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Overrides for task-level appEngineRouting. These settings apply only
to App Engine tasks in this queue  Structure is documented below.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The location of the queue</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The queue name.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p></li>
<li><p><strong>rate_limits</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Rate limits for task dispatches.
The queue’s actual dispatch rate is the result of:</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="o">*</span> <span class="n">Number</span> <span class="n">of</span> <span class="n">tasks</span> <span class="ow">in</span> <span class="n">the</span> <span class="n">queue</span>
<span class="o">*</span> <span class="n">User</span><span class="o">-</span><span class="n">specified</span> <span class="n">throttling</span><span class="p">:</span> <span class="n">rateLimits</span><span class="p">,</span> <span class="n">retryConfig</span><span class="p">,</span> <span class="ow">and</span> <span class="n">the</span> <span class="n">queue</span><span class="s1">&#39;s state.</span>
<span class="o">*</span> <span class="n">System</span> <span class="n">throttling</span> <span class="n">due</span> <span class="n">to</span> <span class="mi">429</span> <span class="p">(</span><span class="n">Too</span> <span class="n">Many</span> <span class="n">Requests</span><span class="p">)</span> <span class="ow">or</span> <span class="mi">503</span> <span class="p">(</span><span class="n">Service</span>
<span class="n">Unavailable</span><span class="p">)</span> <span class="n">responses</span> <span class="kn">from</span> <span class="nn">the</span> <span class="n">worker</span><span class="p">,</span> <span class="n">high</span> <span class="n">error</span> <span class="n">rates</span><span class="p">,</span> <span class="ow">or</span> <span class="n">to</span>
<span class="n">smooth</span> <span class="n">sudden</span> <span class="n">large</span> <span class="n">traffic</span> <span class="n">spikes</span><span class="o">.</span>  <span class="n">Structure</span> <span class="ow">is</span> <span class="n">documented</span> <span class="n">below</span><span class="o">.</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>retry_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Settings that determine the retry behavior.  Structure is documented below.</p>
</dd>
</dl>
<p>The <strong>app_engine_routing_override</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">host</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - -
The host that the task is sent to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">instance</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - App instance.
By default, the task is sent to an instance which is available when the task is attempted.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">service</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - App service.
By default, the task is sent to the service which is the default service when the task is attempted.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">version</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - App version.
By default, the task is sent to the version which is the default version when the task is attempted.</p></li>
</ul>
<p>The <strong>rate_limits</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">maxBurstSize</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - -
The max burst size.
Max burst size limits how fast tasks in queue are processed when many tasks are
in the queue and the rate is high. This field allows the queue to have a high
rate so processing starts shortly after a task is enqueued, but still limits
resource usage when many tasks are enqueued in a short period of time.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxConcurrentDispatches</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The maximum number of concurrent tasks that Cloud Tasks allows to
be dispatched for this queue. After this threshold has been
reached, Cloud Tasks stops dispatching tasks until the number of
concurrent requests decreases.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxDispatchesPerSecond</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The maximum rate at which tasks are dispatched from this queue.
If unspecified when the queue is created, Cloud Tasks will pick the default.</p></li>
</ul>
<p>The <strong>retry_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">maxAttempts</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Number of attempts per task.
Cloud Tasks will attempt the task maxAttempts times (that is, if
the first attempt fails, then there will be maxAttempts - 1
retries). Must be &gt;= -1.
If unspecified when the queue is created, Cloud Tasks will pick
the default.
-1 indicates unlimited attempts.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxBackoff</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A task will be scheduled for retry between minBackoff and
maxBackoff duration after it fails, if the queue’s RetryConfig
specifies that the task should be retried.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxDoublings</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The time between retries will double maxDoublings times.
A task’s retry interval starts at minBackoff, then doubles maxDoublings times,
then increases linearly, and finally retries retries at intervals of maxBackoff
up to maxAttempts times.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxRetryDuration</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - If positive, maxRetryDuration specifies the time limit for
retrying a failed task, measured from when the task was first
attempted. Once maxRetryDuration time has passed and the task has
been attempted maxAttempts times, no further attempts will be
made and the task will be deleted.
If zero, then the task age is unlimited.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">minBackoff</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A task will be scheduled for retry between minBackoff and
maxBackoff duration after it fails, if the queue’s RetryConfig
specifies that the task should be retried.</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_gcp.cloudtasks.Queue.app_engine_routing_override">
<code class="sig-name descname">app_engine_routing_override</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.cloudtasks.Queue.app_engine_routing_override" title="Permalink to this definition">¶</a></dt>
<dd><p>Overrides for task-level appEngineRouting. These settings apply only
to App Engine tasks in this queue  Structure is documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">host</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - -
The host that the task is sent to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">instance</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - App instance.
By default, the task is sent to an instance which is available when the task is attempted.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">service</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - App service.
By default, the task is sent to the service which is the default service when the task is attempted.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">version</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - App version.
By default, the task is sent to the version which is the default version when the task is attempted.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.cloudtasks.Queue.location">
<code class="sig-name descname">location</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.cloudtasks.Queue.location" title="Permalink to this definition">¶</a></dt>
<dd><p>The location of the queue</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.cloudtasks.Queue.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.cloudtasks.Queue.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The queue name.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.cloudtasks.Queue.project">
<code class="sig-name descname">project</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.cloudtasks.Queue.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.cloudtasks.Queue.rate_limits">
<code class="sig-name descname">rate_limits</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.cloudtasks.Queue.rate_limits" title="Permalink to this definition">¶</a></dt>
<dd><p>Rate limits for task dispatches.
The queue’s actual dispatch rate is the result of:</p>
<ul class="simple">
<li><p>Number of tasks in the queue</p></li>
<li><p>User-specified throttling: rateLimits, retryConfig, and the queue’s state.</p></li>
<li><p>System throttling due to 429 (Too Many Requests) or 503 (Service
Unavailable) responses from the worker, high error rates, or to
smooth sudden large traffic spikes.  Structure is documented below.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">maxBurstSize</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - -
The max burst size.
Max burst size limits how fast tasks in queue are processed when many tasks are
in the queue and the rate is high. This field allows the queue to have a high
rate so processing starts shortly after a task is enqueued, but still limits
resource usage when many tasks are enqueued in a short period of time.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxConcurrentDispatches</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The maximum number of concurrent tasks that Cloud Tasks allows to
be dispatched for this queue. After this threshold has been
reached, Cloud Tasks stops dispatching tasks until the number of
concurrent requests decreases.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxDispatchesPerSecond</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The maximum rate at which tasks are dispatched from this queue.
If unspecified when the queue is created, Cloud Tasks will pick the default.</p></li>
</ul>
</li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.cloudtasks.Queue.retry_config">
<code class="sig-name descname">retry_config</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.cloudtasks.Queue.retry_config" title="Permalink to this definition">¶</a></dt>
<dd><p>Settings that determine the retry behavior.  Structure is documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">maxAttempts</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - Number of attempts per task.
Cloud Tasks will attempt the task maxAttempts times (that is, if
the first attempt fails, then there will be maxAttempts - 1
retries). Must be &gt;= -1.
If unspecified when the queue is created, Cloud Tasks will pick
the default.
-1 indicates unlimited attempts.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxBackoff</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - A task will be scheduled for retry between minBackoff and
maxBackoff duration after it fails, if the queue’s RetryConfig
specifies that the task should be retried.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxDoublings</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The time between retries will double maxDoublings times.
A task’s retry interval starts at minBackoff, then doubles maxDoublings times,
then increases linearly, and finally retries retries at intervals of maxBackoff
up to maxAttempts times.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxRetryDuration</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - If positive, maxRetryDuration specifies the time limit for
retrying a failed task, measured from when the task was first
attempted. Once maxRetryDuration time has passed and the task has
been attempted maxAttempts times, no further attempts will be
made and the task will be deleted.
If zero, then the task age is unlimited.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">minBackoff</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - A task will be scheduled for retry between minBackoff and
maxBackoff duration after it fails, if the queue’s RetryConfig
specifies that the task should be retried.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gcp.cloudtasks.Queue.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">app_engine_routing_override</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">location</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">rate_limits</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">retry_config</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.cloudtasks.Queue.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Queue resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>app_engine_routing_override</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Overrides for task-level appEngineRouting. These settings apply only
to App Engine tasks in this queue  Structure is documented below.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The location of the queue</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The queue name.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p></li>
<li><p><strong>rate_limits</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Rate limits for task dispatches.
The queue’s actual dispatch rate is the result of:</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="o">*</span> <span class="n">Number</span> <span class="n">of</span> <span class="n">tasks</span> <span class="ow">in</span> <span class="n">the</span> <span class="n">queue</span>
<span class="o">*</span> <span class="n">User</span><span class="o">-</span><span class="n">specified</span> <span class="n">throttling</span><span class="p">:</span> <span class="n">rateLimits</span><span class="p">,</span> <span class="n">retryConfig</span><span class="p">,</span> <span class="ow">and</span> <span class="n">the</span> <span class="n">queue</span><span class="s1">&#39;s state.</span>
<span class="o">*</span> <span class="n">System</span> <span class="n">throttling</span> <span class="n">due</span> <span class="n">to</span> <span class="mi">429</span> <span class="p">(</span><span class="n">Too</span> <span class="n">Many</span> <span class="n">Requests</span><span class="p">)</span> <span class="ow">or</span> <span class="mi">503</span> <span class="p">(</span><span class="n">Service</span>
<span class="n">Unavailable</span><span class="p">)</span> <span class="n">responses</span> <span class="kn">from</span> <span class="nn">the</span> <span class="n">worker</span><span class="p">,</span> <span class="n">high</span> <span class="n">error</span> <span class="n">rates</span><span class="p">,</span> <span class="ow">or</span> <span class="n">to</span>
<span class="n">smooth</span> <span class="n">sudden</span> <span class="n">large</span> <span class="n">traffic</span> <span class="n">spikes</span><span class="o">.</span>  <span class="n">Structure</span> <span class="ow">is</span> <span class="n">documented</span> <span class="n">below</span><span class="o">.</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>retry_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Settings that determine the retry behavior.  Structure is documented below.</p>
</dd>
</dl>
<p>The <strong>app_engine_routing_override</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">host</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - -
The host that the task is sent to.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">instance</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - App instance.
By default, the task is sent to an instance which is available when the task is attempted.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">service</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - App service.
By default, the task is sent to the service which is the default service when the task is attempted.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">version</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - App version.
By default, the task is sent to the version which is the default version when the task is attempted.</p></li>
</ul>
<p>The <strong>rate_limits</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">maxBurstSize</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - -
The max burst size.
Max burst size limits how fast tasks in queue are processed when many tasks are
in the queue and the rate is high. This field allows the queue to have a high
rate so processing starts shortly after a task is enqueued, but still limits
resource usage when many tasks are enqueued in a short period of time.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxConcurrentDispatches</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The maximum number of concurrent tasks that Cloud Tasks allows to
be dispatched for this queue. After this threshold has been
reached, Cloud Tasks stops dispatching tasks until the number of
concurrent requests decreases.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxDispatchesPerSecond</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The maximum rate at which tasks are dispatched from this queue.
If unspecified when the queue is created, Cloud Tasks will pick the default.</p></li>
</ul>
<p>The <strong>retry_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">maxAttempts</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - Number of attempts per task.
Cloud Tasks will attempt the task maxAttempts times (that is, if
the first attempt fails, then there will be maxAttempts - 1
retries). Must be &gt;= -1.
If unspecified when the queue is created, Cloud Tasks will pick
the default.
-1 indicates unlimited attempts.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxBackoff</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A task will be scheduled for retry between minBackoff and
maxBackoff duration after it fails, if the queue’s RetryConfig
specifies that the task should be retried.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxDoublings</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The time between retries will double maxDoublings times.
A task’s retry interval starts at minBackoff, then doubles maxDoublings times,
then increases linearly, and finally retries retries at intervals of maxBackoff
up to maxAttempts times.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxRetryDuration</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - If positive, maxRetryDuration specifies the time limit for
retrying a failed task, measured from when the task was first
attempted. Once maxRetryDuration time has passed and the task has
been attempted maxAttempts times, no further attempts will be
made and the task will be deleted.
If zero, then the task age is unlimited.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">minBackoff</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - A task will be scheduled for retry between minBackoff and
maxBackoff duration after it fails, if the queue’s RetryConfig
specifies that the task should be retried.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gcp.cloudtasks.Queue.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.cloudtasks.Queue.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.cloudtasks.Queue.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.cloudtasks.Queue.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
