---
title: Module iot
title_tag: Module iot | Package pulumi_gcp | Python SDK
linktitle: iot
notitle: true
---

<div class="section" id="iot">
<h1>iot<a class="headerlink" href="#iot" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-gcp/issues">pulumi/pulumi-gcp repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/issues">terraform-providers/terraform-provider-google repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_gcp.iot"></span><dl class="py class">
<dt id="pulumi_gcp.iot.Registry">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.iot.</code><code class="sig-name descname">Registry</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">credentials</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">event_notification_configs</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">http_config</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">log_level</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">mqtt_config</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">region</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">state_notification_config</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.iot.Registry" title="Permalink to this definition">¶</a></dt>
<dd><p>A Google Cloud IoT Core device registry.</p>
<p>To get more information about DeviceRegistry, see:</p>
<ul class="simple">
<li><p><a class="reference external" href="https://cloud.google.com/iot/docs/reference/cloudiot/rest/">API documentation</a></p></li>
<li><p>How-to Guides</p>
<ul>
<li><p><a class="reference external" href="https://cloud.google.com/iot/docs/">Official Documentation</a></p></li>
</ul>
</li>
</ul>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_gcp</span> <span class="k">as</span> <span class="nn">gcp</span>

<span class="n">test_registry</span> <span class="o">=</span> <span class="n">gcp</span><span class="o">.</span><span class="n">iot</span><span class="o">.</span><span class="n">Registry</span><span class="p">(</span><span class="s2">&quot;test-registry&quot;</span><span class="p">)</span>
</pre></div>
</div>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_gcp</span> <span class="k">as</span> <span class="nn">gcp</span>

<span class="n">default_telemetry</span> <span class="o">=</span> <span class="n">gcp</span><span class="o">.</span><span class="n">pubsub</span><span class="o">.</span><span class="n">Topic</span><span class="p">(</span><span class="s2">&quot;default-telemetry&quot;</span><span class="p">)</span>
<span class="n">test_registry</span> <span class="o">=</span> <span class="n">gcp</span><span class="o">.</span><span class="n">iot</span><span class="o">.</span><span class="n">Registry</span><span class="p">(</span><span class="s2">&quot;test-registry&quot;</span><span class="p">,</span> <span class="n">event_notification_configs</span><span class="o">=</span><span class="p">[{</span>
    <span class="s2">&quot;pubsub_topic_name&quot;</span><span class="p">:</span> <span class="n">default_telemetry</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="s2">&quot;subfolderMatches&quot;</span><span class="p">:</span> <span class="s2">&quot;&quot;</span><span class="p">,</span>
<span class="p">}])</span>
</pre></div>
</div>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_gcp</span> <span class="k">as</span> <span class="nn">gcp</span>

<span class="n">default_devicestatus</span> <span class="o">=</span> <span class="n">gcp</span><span class="o">.</span><span class="n">pubsub</span><span class="o">.</span><span class="n">Topic</span><span class="p">(</span><span class="s2">&quot;default-devicestatus&quot;</span><span class="p">)</span>
<span class="n">default_telemetry</span> <span class="o">=</span> <span class="n">gcp</span><span class="o">.</span><span class="n">pubsub</span><span class="o">.</span><span class="n">Topic</span><span class="p">(</span><span class="s2">&quot;default-telemetry&quot;</span><span class="p">)</span>
<span class="n">additional_telemetry</span> <span class="o">=</span> <span class="n">gcp</span><span class="o">.</span><span class="n">pubsub</span><span class="o">.</span><span class="n">Topic</span><span class="p">(</span><span class="s2">&quot;additional-telemetry&quot;</span><span class="p">)</span>
<span class="n">test_registry</span> <span class="o">=</span> <span class="n">gcp</span><span class="o">.</span><span class="n">iot</span><span class="o">.</span><span class="n">Registry</span><span class="p">(</span><span class="s2">&quot;test-registry&quot;</span><span class="p">,</span>
    <span class="n">event_notification_configs</span><span class="o">=</span><span class="p">[</span>
        <span class="p">{</span>
            <span class="s2">&quot;pubsub_topic_name&quot;</span><span class="p">:</span> <span class="n">additional_telemetry</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
            <span class="s2">&quot;subfolderMatches&quot;</span><span class="p">:</span> <span class="s2">&quot;test/path&quot;</span><span class="p">,</span>
        <span class="p">},</span>
        <span class="p">{</span>
            <span class="s2">&quot;pubsub_topic_name&quot;</span><span class="p">:</span> <span class="n">default_telemetry</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
            <span class="s2">&quot;subfolderMatches&quot;</span><span class="p">:</span> <span class="s2">&quot;&quot;</span><span class="p">,</span>
        <span class="p">},</span>
    <span class="p">],</span>
    <span class="n">state_notification_config</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;pubsub_topic_name&quot;</span><span class="p">:</span> <span class="n">default_devicestatus</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="p">},</span>
    <span class="n">mqtt_config</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;mqtt_enabled_state&quot;</span><span class="p">:</span> <span class="s2">&quot;MQTT_ENABLED&quot;</span><span class="p">,</span>
    <span class="p">},</span>
    <span class="n">http_config</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;http_enabled_state&quot;</span><span class="p">:</span> <span class="s2">&quot;HTTP_ENABLED&quot;</span><span class="p">,</span>
    <span class="p">},</span>
    <span class="n">log_level</span><span class="o">=</span><span class="s2">&quot;INFO&quot;</span><span class="p">,</span>
    <span class="n">credentials</span><span class="o">=</span><span class="p">[{</span>
        <span class="s2">&quot;publicKeyCertificate&quot;</span><span class="p">:</span> <span class="p">{</span>
            <span class="s2">&quot;format&quot;</span><span class="p">:</span> <span class="s2">&quot;X509_CERTIFICATE_PEM&quot;</span><span class="p">,</span>
            <span class="s2">&quot;certificate&quot;</span><span class="p">:</span> <span class="p">(</span><span class="k">lambda</span> <span class="n">path</span><span class="p">:</span> <span class="nb">open</span><span class="p">(</span><span class="n">path</span><span class="p">)</span><span class="o">.</span><span class="n">read</span><span class="p">())(</span><span class="s2">&quot;test-fixtures/rsa_cert.pem&quot;</span><span class="p">),</span>
        <span class="p">},</span>
    <span class="p">}])</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>credentials</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of public key certificates to authenticate devices.
The structure is documented below.</p></li>
<li><p><strong>event_notification_configs</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of configurations for event notifications, such as PubSub topics
to publish device events to.  Structure is documented below.</p></li>
<li><p><strong>http_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Activate or deactivate HTTP.
The structure is documented below.</p></li>
<li><p><strong>log_level</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The default logging verbosity for activity from devices in this
registry. Specifies which events should be written to logs. For
example, if the LogLevel is ERROR, only events that terminate in
errors will be logged. LogLevel is inclusive; enabling INFO logging
will also enable ERROR logging.</p></li>
<li><p><strong>mqtt_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Activate or deactivate MQTT.
The structure is documented below.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A unique name for the resource, required by device registry.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region in which the created registry should reside.
If it is not provided, the provider region is used.</p></li>
<li><p><strong>state_notification_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A PubSub topic to publish device state updates.
The structure is documented below.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>credentials</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">publicKeyCertificate</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A public key certificate format and data.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">certificate</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The certificate data.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">format</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The field allows only <code class="docutils literal notranslate"><span class="pre">X509_CERTIFICATE_PEM</span></code>.</p></li>
</ul>
</li>
</ul>
<p>The <strong>event_notification_configs</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">pubsub_topic_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - PubSub topic name to publish device events.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subfolderMatches</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - If the subfolder name matches this string exactly, this
configuration will be used. The string must not include the
leading ‘/’ character. If empty, all strings are matched. Empty
value can only be used for the last <code class="docutils literal notranslate"><span class="pre">event_notification_configs</span></code>
item.</p></li>
</ul>
<p>The <strong>http_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">http_enabled_state</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The field allows <code class="docutils literal notranslate"><span class="pre">HTTP_ENABLED</span></code> or <code class="docutils literal notranslate"><span class="pre">HTTP_DISABLED</span></code>.</p></li>
</ul>
<p>The <strong>mqtt_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">mqtt_enabled_state</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The field allows <code class="docutils literal notranslate"><span class="pre">MQTT_ENABLED</span></code> or <code class="docutils literal notranslate"><span class="pre">MQTT_DISABLED</span></code>.</p></li>
</ul>
<p>The <strong>state_notification_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">pubsub_topic_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - PubSub topic name to publish device events.</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_gcp.iot.Registry.credentials">
<code class="sig-name descname">credentials</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.iot.Registry.credentials" title="Permalink to this definition">¶</a></dt>
<dd><p>List of public key certificates to authenticate devices.
The structure is documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">publicKeyCertificate</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - A public key certificate format and data.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">certificate</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The certificate data.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">format</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The field allows only <code class="docutils literal notranslate"><span class="pre">X509_CERTIFICATE_PEM</span></code>.</p></li>
</ul>
</li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.iot.Registry.event_notification_configs">
<code class="sig-name descname">event_notification_configs</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.iot.Registry.event_notification_configs" title="Permalink to this definition">¶</a></dt>
<dd><p>List of configurations for event notifications, such as PubSub topics
to publish device events to.  Structure is documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">pubsub_topic_name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - PubSub topic name to publish device events.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subfolderMatches</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - If the subfolder name matches this string exactly, this
configuration will be used. The string must not include the
leading ‘/’ character. If empty, all strings are matched. Empty
value can only be used for the last <code class="docutils literal notranslate"><span class="pre">event_notification_configs</span></code>
item.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.iot.Registry.http_config">
<code class="sig-name descname">http_config</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.iot.Registry.http_config" title="Permalink to this definition">¶</a></dt>
<dd><p>Activate or deactivate HTTP.
The structure is documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">http_enabled_state</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The field allows <code class="docutils literal notranslate"><span class="pre">HTTP_ENABLED</span></code> or <code class="docutils literal notranslate"><span class="pre">HTTP_DISABLED</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.iot.Registry.log_level">
<code class="sig-name descname">log_level</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.iot.Registry.log_level" title="Permalink to this definition">¶</a></dt>
<dd><p>The default logging verbosity for activity from devices in this
registry. Specifies which events should be written to logs. For
example, if the LogLevel is ERROR, only events that terminate in
errors will be logged. LogLevel is inclusive; enabling INFO logging
will also enable ERROR logging.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.iot.Registry.mqtt_config">
<code class="sig-name descname">mqtt_config</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.iot.Registry.mqtt_config" title="Permalink to this definition">¶</a></dt>
<dd><p>Activate or deactivate MQTT.
The structure is documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">mqtt_enabled_state</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The field allows <code class="docutils literal notranslate"><span class="pre">MQTT_ENABLED</span></code> or <code class="docutils literal notranslate"><span class="pre">MQTT_DISABLED</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.iot.Registry.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.iot.Registry.name" title="Permalink to this definition">¶</a></dt>
<dd><p>A unique name for the resource, required by device registry.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.iot.Registry.project">
<code class="sig-name descname">project</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.iot.Registry.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.iot.Registry.region">
<code class="sig-name descname">region</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.iot.Registry.region" title="Permalink to this definition">¶</a></dt>
<dd><p>The region in which the created registry should reside.
If it is not provided, the provider region is used.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_gcp.iot.Registry.state_notification_config">
<code class="sig-name descname">state_notification_config</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.iot.Registry.state_notification_config" title="Permalink to this definition">¶</a></dt>
<dd><p>A PubSub topic to publish device state updates.
The structure is documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">pubsub_topic_name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - PubSub topic name to publish device events.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gcp.iot.Registry.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">credentials</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">event_notification_configs</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">http_config</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">log_level</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">mqtt_config</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">region</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">state_notification_config</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.iot.Registry.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Registry resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>credentials</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of public key certificates to authenticate devices.
The structure is documented below.</p></li>
<li><p><strong>event_notification_configs</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – List of configurations for event notifications, such as PubSub topics
to publish device events to.  Structure is documented below.</p></li>
<li><p><strong>http_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Activate or deactivate HTTP.
The structure is documented below.</p></li>
<li><p><strong>log_level</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The default logging verbosity for activity from devices in this
registry. Specifies which events should be written to logs. For
example, if the LogLevel is ERROR, only events that terminate in
errors will be logged. LogLevel is inclusive; enabling INFO logging
will also enable ERROR logging.</p></li>
<li><p><strong>mqtt_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Activate or deactivate MQTT.
The structure is documented below.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A unique name for the resource, required by device registry.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs.
If it is not provided, the provider project is used.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The region in which the created registry should reside.
If it is not provided, the provider region is used.</p></li>
<li><p><strong>state_notification_config</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A PubSub topic to publish device state updates.
The structure is documented below.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>credentials</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">publicKeyCertificate</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - A public key certificate format and data.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">certificate</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The certificate data.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">format</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The field allows only <code class="docutils literal notranslate"><span class="pre">X509_CERTIFICATE_PEM</span></code>.</p></li>
</ul>
</li>
</ul>
<p>The <strong>event_notification_configs</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">pubsub_topic_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - PubSub topic name to publish device events.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">subfolderMatches</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - If the subfolder name matches this string exactly, this
configuration will be used. The string must not include the
leading ‘/’ character. If empty, all strings are matched. Empty
value can only be used for the last <code class="docutils literal notranslate"><span class="pre">event_notification_configs</span></code>
item.</p></li>
</ul>
<p>The <strong>http_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">http_enabled_state</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The field allows <code class="docutils literal notranslate"><span class="pre">HTTP_ENABLED</span></code> or <code class="docutils literal notranslate"><span class="pre">HTTP_DISABLED</span></code>.</p></li>
</ul>
<p>The <strong>mqtt_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">mqtt_enabled_state</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The field allows <code class="docutils literal notranslate"><span class="pre">MQTT_ENABLED</span></code> or <code class="docutils literal notranslate"><span class="pre">MQTT_DISABLED</span></code>.</p></li>
</ul>
<p>The <strong>state_notification_config</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">pubsub_topic_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - PubSub topic name to publish device events.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gcp.iot.Registry.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.iot.Registry.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.iot.Registry.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.iot.Registry.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
