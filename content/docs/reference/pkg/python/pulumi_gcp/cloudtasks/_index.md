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
<span class="target" id="module-pulumi_gcp.cloudtasks"></span><dl class="class">
<dt id="pulumi_gcp.cloudtasks.Queue">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.cloudtasks.</code><code class="sig-name descname">Queue</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">app_engine_routing_override=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">rate_limits=None</em>, <em class="sig-param">retry_config=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.cloudtasks.Queue" title="Permalink to this definition">¶</a></dt>
<dd><p>A named resource to which messages are sent by publishers.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>app_engine_routing_override</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Overrides for task-level appEngineRouting. These settings apply only to App Engine tasks in this queue</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The location of the queue</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The queue name.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p></li>
<li><p><strong>rate_limits</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Rate limits for task dispatches. The queue’s actual dispatch rate is the result of: * Number of tasks in the queue *
User-specified throttling: rateLimits, retryConfig, and the queue’s state. * System throttling due to 429 (Too Many
Requests) or 503 (Service Unavailable) responses from the worker, high error rates, or to smooth sudden large traffic
spikes.</p></li>
<li><p><strong>retry_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Settings that determine the retry behavior.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>app_engine_routing_override</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">host</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">instance</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">service</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">version</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>rate_limits</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">maxBurstSize</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxConcurrentDispatches</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxDispatchesPerSecond</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
<p>The <strong>retry_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">maxAttempts</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxBackoff</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxDoublings</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxRetryDuration</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">minBackoff</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<dl class="attribute">
<dt id="pulumi_gcp.cloudtasks.Queue.app_engine_routing_override">
<code class="sig-name descname">app_engine_routing_override</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.cloudtasks.Queue.app_engine_routing_override" title="Permalink to this definition">¶</a></dt>
<dd><p>Overrides for task-level appEngineRouting. These settings apply only to App Engine tasks in this queue</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">host</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">instance</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">service</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">version</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.cloudtasks.Queue.location">
<code class="sig-name descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.cloudtasks.Queue.location" title="Permalink to this definition">¶</a></dt>
<dd><p>The location of the queue</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.cloudtasks.Queue.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.cloudtasks.Queue.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The queue name.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.cloudtasks.Queue.project">
<code class="sig-name descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.cloudtasks.Queue.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.cloudtasks.Queue.rate_limits">
<code class="sig-name descname">rate_limits</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.cloudtasks.Queue.rate_limits" title="Permalink to this definition">¶</a></dt>
<dd><p>Rate limits for task dispatches. The queue’s actual dispatch rate is the result of: * Number of tasks in the queue *
User-specified throttling: rateLimits, retryConfig, and the queue’s state. * System throttling due to 429 (Too Many
Requests) or 503 (Service Unavailable) responses from the worker, high error rates, or to smooth sudden large traffic
spikes.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">maxBurstSize</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxConcurrentDispatches</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxDispatchesPerSecond</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.cloudtasks.Queue.retry_config">
<code class="sig-name descname">retry_config</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.cloudtasks.Queue.retry_config" title="Permalink to this definition">¶</a></dt>
<dd><p>Settings that determine the retry behavior.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">maxAttempts</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxBackoff</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxDoublings</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxRetryDuration</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">minBackoff</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.cloudtasks.Queue.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">app_engine_routing_override=None</em>, <em class="sig-param">location=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">rate_limits=None</em>, <em class="sig-param">retry_config=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.cloudtasks.Queue.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Queue resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>app_engine_routing_override</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Overrides for task-level appEngineRouting. These settings apply only to App Engine tasks in this queue</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The location of the queue</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The queue name.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p></li>
<li><p><strong>rate_limits</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Rate limits for task dispatches. The queue’s actual dispatch rate is the result of: * Number of tasks in the queue *
User-specified throttling: rateLimits, retryConfig, and the queue’s state. * System throttling due to 429 (Too Many
Requests) or 503 (Service Unavailable) responses from the worker, high error rates, or to smooth sudden large traffic
spikes.</p></li>
<li><p><strong>retry_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Settings that determine the retry behavior.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>app_engine_routing_override</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">host</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">instance</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">service</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">version</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>rate_limits</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">maxBurstSize</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxConcurrentDispatches</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxDispatchesPerSecond</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
<p>The <strong>retry_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">maxAttempts</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxBackoff</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxDoublings</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxRetryDuration</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">minBackoff</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.cloudtasks.Queue.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.cloudtasks.Queue.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.cloudtasks.Queue.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.cloudtasks.Queue.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
