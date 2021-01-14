---
title: Package pulumi_mongodbatlas
title_tag: Package pulumi_mongodbatlas | Python SDK
linktitle: pulumi_mongodbatlas
notitle: true
block_external_search_index: true
---

{{< resource-docs-alert "mongodbatlas" >}}

<div class="section" id="pulumi-mongodb-atlas">
<h1>Pulumi MongoDB Atlas<a class="headerlink" href="#pulumi-mongodb-atlas" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-mongodbatlas">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-mongodbatlas/issues">pulumi/pulumi-mongodbatlas repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-mongodbatlas/issues">terraform-providers/terraform-provider-mongodbatlas repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_mongodbatlas"></span><dl class="py class">
<dt id="pulumi_mongodbatlas.AlertConfiguration">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">AlertConfiguration</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">event_type</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">matchers</span><span class="p">:</span> <span class="n">Union[Sequence[Union[AlertConfigurationMatcherArgs, Mapping[str, Any], Awaitable[Union[AlertConfigurationMatcherArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[AlertConfigurationMatcherArgs, Mapping[str, Any], Awaitable[Union[AlertConfigurationMatcherArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">metric_threshold</span><span class="p">:</span> <span class="n">Union[AlertConfigurationMetricThresholdArgs, Mapping[str, Any], Awaitable[Union[AlertConfigurationMetricThresholdArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">notifications</span><span class="p">:</span> <span class="n">Union[Sequence[Union[AlertConfigurationNotificationArgs, Mapping[str, Any], Awaitable[Union[AlertConfigurationNotificationArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[AlertConfigurationNotificationArgs, Mapping[str, Any], Awaitable[Union[AlertConfigurationNotificationArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">threshold</span><span class="p">:</span> <span class="n">Union[AlertConfigurationThresholdArgs, Mapping[str, Any], Awaitable[Union[AlertConfigurationThresholdArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.AlertConfiguration" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">AlertConfiguration</span></code> provides an Alert Configuration resource to define the conditions that trigger an alert and the methods of notification within a MongoDB Atlas project.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Groups and projects are synonymous terms. You may find <code class="docutils literal notranslate"><span class="pre">groupId</span></code> in the official documentation.</p>
</div></blockquote>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_mongodbatlas</span> <span class="k">as</span> <span class="nn">mongodbatlas</span>

<span class="n">test</span> <span class="o">=</span> <span class="n">mongodbatlas</span><span class="o">.</span><span class="n">AlertConfiguration</span><span class="p">(</span><span class="s2">&quot;test&quot;</span><span class="p">,</span>
    <span class="n">enabled</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="n">event_type</span><span class="o">=</span><span class="s2">&quot;OUTSIDE_METRIC_THRESHOLD&quot;</span><span class="p">,</span>
    <span class="n">matchers</span><span class="o">=</span><span class="p">[</span><span class="n">mongodbatlas</span><span class="o">.</span><span class="n">AlertConfigurationMatcherArgs</span><span class="p">(</span>
        <span class="n">field_name</span><span class="o">=</span><span class="s2">&quot;HOSTNAME_AND_PORT&quot;</span><span class="p">,</span>
        <span class="n">operator</span><span class="o">=</span><span class="s2">&quot;EQUALS&quot;</span><span class="p">,</span>
        <span class="n">value</span><span class="o">=</span><span class="s2">&quot;SECONDARY&quot;</span><span class="p">,</span>
    <span class="p">)],</span>
    <span class="n">metric_threshold</span><span class="o">=</span><span class="n">mongodbatlas</span><span class="o">.</span><span class="n">AlertConfigurationMetricThresholdArgs</span><span class="p">(</span>
        <span class="n">metric_name</span><span class="o">=</span><span class="s2">&quot;ASSERT_REGULAR&quot;</span><span class="p">,</span>
        <span class="n">mode</span><span class="o">=</span><span class="s2">&quot;AVERAGE&quot;</span><span class="p">,</span>
        <span class="n">operator</span><span class="o">=</span><span class="s2">&quot;LESS_THAN&quot;</span><span class="p">,</span>
        <span class="n">threshold</span><span class="o">=</span><span class="mi">99</span><span class="p">,</span>
        <span class="n">units</span><span class="o">=</span><span class="s2">&quot;RAW&quot;</span><span class="p">,</span>
    <span class="p">),</span>
    <span class="n">notifications</span><span class="o">=</span><span class="p">[</span><span class="n">mongodbatlas</span><span class="o">.</span><span class="n">AlertConfigurationNotificationArgs</span><span class="p">(</span>
        <span class="n">delay_min</span><span class="o">=</span><span class="mi">0</span><span class="p">,</span>
        <span class="n">email_enabled</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
        <span class="n">interval_min</span><span class="o">=</span><span class="mi">5</span><span class="p">,</span>
        <span class="n">roles</span><span class="o">=</span><span class="p">[</span>
            <span class="s2">&quot;GROUP_CHARTS_ADMIN&quot;</span><span class="p">,</span>
            <span class="s2">&quot;GROUP_CLUSTER_MANAGER&quot;</span><span class="p">,</span>
        <span class="p">],</span>
        <span class="n">sms_enabled</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span>
        <span class="n">type_name</span><span class="o">=</span><span class="s2">&quot;GROUP&quot;</span><span class="p">,</span>
    <span class="p">)],</span>
    <span class="n">project_id</span><span class="o">=</span><span class="s2">&quot;&lt;PROJECT-ID&gt;&quot;</span><span class="p">)</span>
</pre></div>
</div>
<blockquote>
<div><p><strong>NOTE:</strong> In order to allow for a fast pace of change to alert variables some validations have been removed from this resource in order to unblock alert creation. Impacted areas have links to the MongoDB Atlas API documentation so always check it for the most current information: <a class="reference external" href="https://docs.atlas.mongodb.com/reference/api/alert-configurations-create-config/">https://docs.atlas.mongodb.com/reference/api/alert-configurations-create-config/</a></p>
</div></blockquote>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_mongodbatlas</span> <span class="k">as</span> <span class="nn">mongodbatlas</span>

<span class="n">test</span> <span class="o">=</span> <span class="n">mongodbatlas</span><span class="o">.</span><span class="n">AlertConfiguration</span><span class="p">(</span><span class="s2">&quot;test&quot;</span><span class="p">,</span>
    <span class="n">enabled</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="n">event_type</span><span class="o">=</span><span class="s2">&quot;REPLICATION_OPLOG_WINDOW_RUNNING_OUT&quot;</span><span class="p">,</span>
    <span class="n">matchers</span><span class="o">=</span><span class="p">[</span><span class="n">mongodbatlas</span><span class="o">.</span><span class="n">AlertConfigurationMatcherArgs</span><span class="p">(</span>
        <span class="n">field_name</span><span class="o">=</span><span class="s2">&quot;HOSTNAME_AND_PORT&quot;</span><span class="p">,</span>
        <span class="n">operator</span><span class="o">=</span><span class="s2">&quot;EQUALS&quot;</span><span class="p">,</span>
        <span class="n">value</span><span class="o">=</span><span class="s2">&quot;SECONDARY&quot;</span><span class="p">,</span>
    <span class="p">)],</span>
    <span class="n">notifications</span><span class="o">=</span><span class="p">[</span><span class="n">mongodbatlas</span><span class="o">.</span><span class="n">AlertConfigurationNotificationArgs</span><span class="p">(</span>
        <span class="n">delay_min</span><span class="o">=</span><span class="mi">0</span><span class="p">,</span>
        <span class="n">email_enabled</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
        <span class="n">interval_min</span><span class="o">=</span><span class="mi">5</span><span class="p">,</span>
        <span class="n">roles</span><span class="o">=</span><span class="p">[</span>
            <span class="s2">&quot;GROUP_CHARTS_ADMIN&quot;</span><span class="p">,</span>
            <span class="s2">&quot;GROUP_CLUSTER_MANAGER&quot;</span><span class="p">,</span>
        <span class="p">],</span>
        <span class="n">sms_enabled</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span>
        <span class="n">type_name</span><span class="o">=</span><span class="s2">&quot;GROUP&quot;</span><span class="p">,</span>
    <span class="p">)],</span>
    <span class="n">project_id</span><span class="o">=</span><span class="s2">&quot;&lt;PROJECT-ID&gt;&quot;</span><span class="p">,</span>
    <span class="n">threshold</span><span class="o">=</span><span class="n">mongodbatlas</span><span class="o">.</span><span class="n">AlertConfigurationThresholdArgs</span><span class="p">(</span>
        <span class="n">operator</span><span class="o">=</span><span class="s2">&quot;LESS_THAN&quot;</span><span class="p">,</span>
        <span class="n">threshold</span><span class="o">=</span><span class="mi">1</span><span class="p">,</span>
        <span class="n">units</span><span class="o">=</span><span class="s2">&quot;HOURS&quot;</span><span class="p">,</span>
    <span class="p">))</span>
</pre></div>
</div>
<p>Alert Configuration can be imported using the <code class="docutils literal notranslate"><span class="pre">project_id-alert_configuration_id</span></code>, e.g.</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>   $ pulumi import mongodbatlas:index/alertConfiguration:AlertConfiguration <span class="nb">test</span> 5d0f1f74cf09a29120e123cd-5d0f1f74cf09a29120e1fscg

For more information see<span class="se">\ </span><span class="sb">`</span>MongoDB Atlas API Reference. &lt;https://docs.atlas.mongodb.com/reference/api/alert-configurations/&gt;<span class="sb">`</span>_
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – It is not required, but If the attribute is omitted, by default will be false, and the configuration would be disabled. You must set true to enable the configuration.</p></li>
<li><p><strong>event_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of event that will trigger an alert.</p></li>
<li><p><strong>project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project where the alert configuration will create.</p></li>
<li><p><strong>threshold</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'AlertConfigurationThresholdArgs'</em><em>]</em><em>]</em>) – Threshold value outside of which an alert will be triggered.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_mongodbatlas.AlertConfiguration.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">alert_configuration_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">created</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">event_type</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">matchers</span><span class="p">:</span> <span class="n">Union[Sequence[Union[AlertConfigurationMatcherArgs, Mapping[str, Any], Awaitable[Union[AlertConfigurationMatcherArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[AlertConfigurationMatcherArgs, Mapping[str, Any], Awaitable[Union[AlertConfigurationMatcherArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">metric_threshold</span><span class="p">:</span> <span class="n">Union[AlertConfigurationMetricThresholdArgs, Mapping[str, Any], Awaitable[Union[AlertConfigurationMetricThresholdArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">notifications</span><span class="p">:</span> <span class="n">Union[Sequence[Union[AlertConfigurationNotificationArgs, Mapping[str, Any], Awaitable[Union[AlertConfigurationNotificationArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[AlertConfigurationNotificationArgs, Mapping[str, Any], Awaitable[Union[AlertConfigurationNotificationArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">threshold</span><span class="p">:</span> <span class="n">Union[AlertConfigurationThresholdArgs, Mapping[str, Any], Awaitable[Union[AlertConfigurationThresholdArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">updated</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_mongodbatlas.alert_configuration.AlertConfiguration<a class="headerlink" href="#pulumi_mongodbatlas.AlertConfiguration.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing AlertConfiguration resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>alert_configuration_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Unique identifier for the alert configuration.</p></li>
<li><p><strong>created</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Timestamp in ISO 8601 date and time format in UTC when this alert configuration was created.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – It is not required, but If the attribute is omitted, by default will be false, and the configuration would be disabled. You must set true to enable the configuration.</p></li>
<li><p><strong>event_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of event that will trigger an alert.</p></li>
<li><p><strong>project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project where the alert configuration will create.</p></li>
<li><p><strong>threshold</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'AlertConfigurationThresholdArgs'</em><em>]</em><em>]</em>) – Threshold value outside of which an alert will be triggered.</p></li>
<li><p><strong>updated</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Timestamp in ISO 8601 date and time format in UTC when this alert configuration was last updated.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.AlertConfiguration.alert_configuration_id">
<em class="property">property </em><code class="sig-name descname">alert_configuration_id</code><a class="headerlink" href="#pulumi_mongodbatlas.AlertConfiguration.alert_configuration_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Unique identifier for the alert configuration.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.AlertConfiguration.created">
<em class="property">property </em><code class="sig-name descname">created</code><a class="headerlink" href="#pulumi_mongodbatlas.AlertConfiguration.created" title="Permalink to this definition">¶</a></dt>
<dd><p>Timestamp in ISO 8601 date and time format in UTC when this alert configuration was created.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.AlertConfiguration.enabled">
<em class="property">property </em><code class="sig-name descname">enabled</code><a class="headerlink" href="#pulumi_mongodbatlas.AlertConfiguration.enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>It is not required, but If the attribute is omitted, by default will be false, and the configuration would be disabled. You must set true to enable the configuration.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.AlertConfiguration.event_type">
<em class="property">property </em><code class="sig-name descname">event_type</code><a class="headerlink" href="#pulumi_mongodbatlas.AlertConfiguration.event_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of event that will trigger an alert.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.AlertConfiguration.project_id">
<em class="property">property </em><code class="sig-name descname">project_id</code><a class="headerlink" href="#pulumi_mongodbatlas.AlertConfiguration.project_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project where the alert configuration will create.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.AlertConfiguration.threshold">
<em class="property">property </em><code class="sig-name descname">threshold</code><a class="headerlink" href="#pulumi_mongodbatlas.AlertConfiguration.threshold" title="Permalink to this definition">¶</a></dt>
<dd><p>Threshold value outside of which an alert will be triggered.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.AlertConfiguration.updated">
<em class="property">property </em><code class="sig-name descname">updated</code><a class="headerlink" href="#pulumi_mongodbatlas.AlertConfiguration.updated" title="Permalink to this definition">¶</a></dt>
<dd><p>Timestamp in ISO 8601 date and time format in UTC when this alert configuration was last updated.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.AlertConfiguration.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.AlertConfiguration.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_mongodbatlas.AlertConfiguration.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.AlertConfiguration.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py class">
<dt id="pulumi_mongodbatlas.Auditing">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">Auditing</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">audit_authorization_success</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">audit_filter</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.Auditing" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">Auditing</span></code> provides an Auditing resource. This allows auditing to be created.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_mongodbatlas</span> <span class="k">as</span> <span class="nn">mongodbatlas</span>

<span class="n">test</span> <span class="o">=</span> <span class="n">mongodbatlas</span><span class="o">.</span><span class="n">Auditing</span><span class="p">(</span><span class="s2">&quot;test&quot;</span><span class="p">,</span>
    <span class="n">audit_authorization_success</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span>
    <span class="n">audit_filter</span><span class="o">=</span><span class="s2">&quot;{ &#39;atype&#39;: &#39;authenticate&#39;, &#39;param&#39;: {   &#39;user&#39;: &#39;auditAdmin&#39;,   &#39;db&#39;: &#39;admin&#39;,   &#39;mechanism&#39;: &#39;SCRAM-SHA-1&#39; }}&quot;</span><span class="p">,</span>
    <span class="n">enabled</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="n">project_id</span><span class="o">=</span><span class="s2">&quot;&lt;project-id&gt;&quot;</span><span class="p">)</span>
</pre></div>
</div>
<p>Auditing must be imported using auditing ID, e.g.</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>   $ pulumi import mongodbatlas:index/auditing:Auditing my_auditing 5d09d6a59ccf6445652a444a

For more information see<span class="se">\ </span><span class="sb">`</span>MongoDB Atlas API Reference. &lt;https://docs.atlas.mongodb.com/reference/api/auditing/&gt;<span class="sb">`</span>_
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>audit_authorization_success</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – JSON-formatted audit filter used by the project</p></li>
<li><p><strong>audit_filter</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Indicates whether the auditing system captures successful authentication attempts for audit filters using the “atype” : “authCheck” auditing event. For more information, see auditAuthorizationSuccess</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Denotes whether or not the project associated with the {project_id} has database auditing enabled.</p></li>
<li><p><strong>project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique ID for the project to configure auditing.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_mongodbatlas.Auditing.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">audit_authorization_success</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">audit_filter</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">configuration_type</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_mongodbatlas.auditing.Auditing<a class="headerlink" href="#pulumi_mongodbatlas.Auditing.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Auditing resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>audit_authorization_success</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – JSON-formatted audit filter used by the project</p></li>
<li><p><strong>audit_filter</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Indicates whether the auditing system captures successful authentication attempts for audit filters using the “atype” : “authCheck” auditing event. For more information, see auditAuthorizationSuccess</p></li>
<li><p><strong>configuration_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Denotes the configuration method for the audit filter. Possible values are:</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="o">*</span> <span class="n">NONE</span> <span class="o">-</span> <span class="n">auditing</span> <span class="ow">not</span> <span class="n">configured</span> <span class="k">for</span> <span class="n">the</span> <span class="n">project</span><span class="o">.</span>
<span class="o">*</span> <span class="n">FILTER_BUILDER</span> <span class="o">-</span> <span class="n">auditing</span> <span class="n">configured</span> <span class="n">via</span> <span class="n">Atlas</span> <span class="n">UI</span> <span class="nb">filter</span> <span class="n">builder</span><span class="o">.</span>
<span class="o">*</span> <span class="n">FILTER_JSON</span> <span class="o">-</span> <span class="n">auditing</span> <span class="n">configured</span> <span class="n">via</span> <span class="n">Atlas</span> <span class="n">custom</span> <span class="nb">filter</span> <span class="ow">or</span> <span class="n">API</span><span class="o">.</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Denotes whether or not the project associated with the {project_id} has database auditing enabled.</p></li>
<li><p><strong>project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique ID for the project to configure auditing.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.Auditing.audit_authorization_success">
<em class="property">property </em><code class="sig-name descname">audit_authorization_success</code><a class="headerlink" href="#pulumi_mongodbatlas.Auditing.audit_authorization_success" title="Permalink to this definition">¶</a></dt>
<dd><p>JSON-formatted audit filter used by the project</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.Auditing.audit_filter">
<em class="property">property </em><code class="sig-name descname">audit_filter</code><a class="headerlink" href="#pulumi_mongodbatlas.Auditing.audit_filter" title="Permalink to this definition">¶</a></dt>
<dd><p>Indicates whether the auditing system captures successful authentication attempts for audit filters using the “atype” : “authCheck” auditing event. For more information, see auditAuthorizationSuccess</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.Auditing.configuration_type">
<em class="property">property </em><code class="sig-name descname">configuration_type</code><a class="headerlink" href="#pulumi_mongodbatlas.Auditing.configuration_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Denotes the configuration method for the audit filter. Possible values are:</p>
<ul class="simple">
<li><p>NONE - auditing not configured for the project.</p></li>
<li><p>FILTER_BUILDER - auditing configured via Atlas UI filter builder.</p></li>
<li><p>FILTER_JSON - auditing configured via Atlas custom filter or API.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.Auditing.enabled">
<em class="property">property </em><code class="sig-name descname">enabled</code><a class="headerlink" href="#pulumi_mongodbatlas.Auditing.enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Denotes whether or not the project associated with the {project_id} has database auditing enabled.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.Auditing.project_id">
<em class="property">property </em><code class="sig-name descname">project_id</code><a class="headerlink" href="#pulumi_mongodbatlas.Auditing.project_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The unique ID for the project to configure auditing.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.Auditing.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.Auditing.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_mongodbatlas.Auditing.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.Auditing.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py class">
<dt id="pulumi_mongodbatlas.AwaitableGet509AuthenticationDatabaseUserResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">AwaitableGet509AuthenticationDatabaseUserResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">certificates</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">customer_x509_cas</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">username</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.AwaitableGet509AuthenticationDatabaseUserResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_mongodbatlas.AwaitableGetAlertConfigurationResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">AwaitableGetAlertConfigurationResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">alert_configuration_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">created</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">event_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">matchers</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">metric_threshold</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">notifications</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">threshold</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">updated</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.AwaitableGetAlertConfigurationResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_mongodbatlas.AwaitableGetAuditingResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">AwaitableGetAuditingResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">audit_authorization_success</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">audit_filter</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">configuration_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.AwaitableGetAuditingResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_mongodbatlas.AwaitableGetCloudProviderAccessResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">AwaitableGetCloudProviderAccessResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">aws_iam_roles</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.AwaitableGetCloudProviderAccessResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_mongodbatlas.AwaitableGetCloudProviderSnapshotBackupPolicyResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">AwaitableGetCloudProviderSnapshotBackupPolicyResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">cluster_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cluster_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">next_snapshot</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policies</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">reference_hour_of_day</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">reference_minute_of_hour</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">restore_window_days</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">update_snapshots</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.AwaitableGetCloudProviderSnapshotBackupPolicyResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_mongodbatlas.AwaitableGetCloudProviderSnapshotRestoreJobResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">AwaitableGetCloudProviderSnapshotRestoreJobResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">cancelled</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cluster_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">created_at</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">delivery_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">delivery_urls</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">expired</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">expires_at</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">finished_at</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">job_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">oplog_inc</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">oplog_ts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">point_in_time_utc_seconds</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">snapshot_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">target_cluster_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">target_project_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">timestamp</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.AwaitableGetCloudProviderSnapshotRestoreJobResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_mongodbatlas.AwaitableGetCloudProviderSnapshotRestoreJobsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">AwaitableGetCloudProviderSnapshotRestoreJobsResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">cluster_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">items_per_page</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">page_num</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">results</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">total_count</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.AwaitableGetCloudProviderSnapshotRestoreJobsResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_mongodbatlas.AwaitableGetCloudProviderSnapshotResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">AwaitableGetCloudProviderSnapshotResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">cluster_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">created_at</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">expires_at</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">master_key_uuid</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">mongod_version</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">snapshot_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">snapshot_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">storage_size_bytes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.AwaitableGetCloudProviderSnapshotResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_mongodbatlas.AwaitableGetCloudProviderSnapshotsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">AwaitableGetCloudProviderSnapshotsResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">cluster_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">items_per_page</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">page_num</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">results</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">total_count</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.AwaitableGetCloudProviderSnapshotsResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_mongodbatlas.AwaitableGetClusterResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">AwaitableGetClusterResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">auto_scaling_compute_enabled</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auto_scaling_compute_scale_down_enabled</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auto_scaling_disk_gb_enabled</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">backing_provider_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">backup_enabled</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">bi_connector</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cluster_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">connection_strings</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">container_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">disk_size_gb</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">encryption_at_rest_provider</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">labels</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">mongo_db_major_version</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">mongo_db_version</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">mongo_uri</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">mongo_uri_updated</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">mongo_uri_with_options</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">num_shards</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">paused</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">pit_enabled</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">provider_auto_scaling_compute_max_instance_size</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">provider_auto_scaling_compute_min_instance_size</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">provider_backup_enabled</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">provider_disk_iops</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">provider_disk_type_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">provider_encrypt_ebs_volume</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">provider_instance_size_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">provider_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">provider_region_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">provider_volume_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">replication_factor</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">replication_specs</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">snapshot_backup_policies</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">srv_address</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">state_name</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.AwaitableGetClusterResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_mongodbatlas.AwaitableGetClustersResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">AwaitableGetClustersResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">results</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.AwaitableGetClustersResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_mongodbatlas.AwaitableGetCustomDbRoleResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">AwaitableGetCustomDbRoleResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">actions</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">inherited_roles</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">role_name</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.AwaitableGetCustomDbRoleResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_mongodbatlas.AwaitableGetCustomDbRolesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">AwaitableGetCustomDbRolesResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">results</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.AwaitableGetCustomDbRolesResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_mongodbatlas.AwaitableGetDatabaseUserResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">AwaitableGetDatabaseUserResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">auth_database_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">aws_iam_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">database_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">labels</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">roles</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">scopes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">username</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">x509_type</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.AwaitableGetDatabaseUserResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_mongodbatlas.AwaitableGetDatabaseUsersResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">AwaitableGetDatabaseUsersResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">results</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.AwaitableGetDatabaseUsersResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_mongodbatlas.AwaitableGetGlobalClusterConfigResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">AwaitableGetGlobalClusterConfigResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">cluster_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_zone_mapping</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">managed_namespaces</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.AwaitableGetGlobalClusterConfigResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_mongodbatlas.AwaitableGetMaintenanceWindowResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">AwaitableGetMaintenanceWindowResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">day_of_week</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">hour_of_day</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">number_of_deferrals</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">start_asap</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.AwaitableGetMaintenanceWindowResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_mongodbatlas.AwaitableGetNetworkContainerResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">AwaitableGetNetworkContainerResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">atlas_cidr_block</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">azure_subscription_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">container_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">gcp_project_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">network_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">provider_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">provisioned</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">region</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">region_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vnet_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vpc_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.AwaitableGetNetworkContainerResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_mongodbatlas.AwaitableGetNetworkContainersResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">AwaitableGetNetworkContainersResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">provider_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">results</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.AwaitableGetNetworkContainersResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_mongodbatlas.AwaitableGetNetworkPeeringResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">AwaitableGetNetworkPeeringResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">accepter_region_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">atlas_cidr_block</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">atlas_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">aws_account_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">azure_directory_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">azure_subscription_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">connection_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">container_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">error_message</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">error_state</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">error_state_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">gcp_project_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">network_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">peering_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">provider_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">route_table_cidr_block</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vnet_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vpc_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.AwaitableGetNetworkPeeringResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_mongodbatlas.AwaitableGetNetworkPeeringsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">AwaitableGetNetworkPeeringsResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">results</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.AwaitableGetNetworkPeeringsResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_mongodbatlas.AwaitableGetPrivateEndpointInterfaceLinkResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">AwaitableGetPrivateEndpointInterfaceLinkResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">connection_status</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">delete_requested</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">error_message</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">interface_endpoint_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">private_link_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.AwaitableGetPrivateEndpointInterfaceLinkResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_mongodbatlas.AwaitableGetPrivateEndpointResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">AwaitableGetPrivateEndpointResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">endpoint_service_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">error_message</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">interface_endpoints</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">private_link_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.AwaitableGetPrivateEndpointResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_mongodbatlas.AwaitableGetPrivateLinkEndpointResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">AwaitableGetPrivateLinkEndpointResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">endpoint_service_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">error_message</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">interface_endpoints</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">private_endpoints</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">private_link_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">private_link_service_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">private_link_service_resource_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">provider_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.AwaitableGetPrivateLinkEndpointResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_mongodbatlas.AwaitableGetPrivateLinkEndpointServiceResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">AwaitableGetPrivateLinkEndpointServiceResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">connection_status</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">delete_requested</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">endpoint_service_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">error_message</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">interface_endpoint_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">private_endpoint_connection_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">private_endpoint_ip_address</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">private_endpoint_resource_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">private_link_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">provider_name</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.AwaitableGetPrivateLinkEndpointServiceResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_mongodbatlas.AwaitableGetProjectIpAccessListResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">AwaitableGetProjectIpAccessListResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">aws_security_group</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cidr_block</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">comment</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ip_address</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.AwaitableGetProjectIpAccessListResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_mongodbatlas.AwaitableGetProjectIpWhitelistResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">AwaitableGetProjectIpWhitelistResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">aws_security_group</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cidr_block</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">comment</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ip_address</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.AwaitableGetProjectIpWhitelistResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_mongodbatlas.AwaitableGetProjectResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">AwaitableGetProjectResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">cluster_count</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">created</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">org_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">teams</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.AwaitableGetProjectResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_mongodbatlas.AwaitableGetProjectsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">AwaitableGetProjectsResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">items_per_page</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">page_num</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">results</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">total_count</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.AwaitableGetProjectsResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_mongodbatlas.AwaitableGetTeamResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">AwaitableGetTeamResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">org_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">team_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">usernames</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.AwaitableGetTeamResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_mongodbatlas.AwaitableGetTeamsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">AwaitableGetTeamsResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">org_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">team_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">usernames</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.AwaitableGetTeamsResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_mongodbatlas.AwaitableGetThirdPartyIntegrationResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">AwaitableGetThirdPartyIntegrationResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">account_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">api_key</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">api_token</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">channel_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">flow_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">license_key</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">org_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">read_token</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">region</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">routing_key</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">secret</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_key</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">team_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">url</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">write_token</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.AwaitableGetThirdPartyIntegrationResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_mongodbatlas.AwaitableGetThirdPartyIntegrationsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">AwaitableGetThirdPartyIntegrationsResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">results</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.AwaitableGetThirdPartyIntegrationsResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_mongodbatlas.CloudProviderAccess">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">CloudProviderAccess</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">iam_assumed_role_arn</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">provider_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.CloudProviderAccess" title="Permalink to this definition">¶</a></dt>
<dd><p>The Cloud Provider Access resource can be imported using project ID and the provider name and mongodbatlas role id, in the format <code class="docutils literal notranslate"><span class="pre">project_id</span></code>-<code class="docutils literal notranslate"><span class="pre">provider_name</span></code>-<code class="docutils literal notranslate"><span class="pre">role_id</span></code>, e.g.</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>   $ pulumi import mongodbatlas:index/cloudProviderAccess:CloudProviderAccess my_role 1112222b3bf99403840e8934-AWS-5fc17d476f7a33224f5b224e

See <span class="sb">`</span>MongoDB Atlas API &lt;https://docs.atlas.mongodb.com/reference/api/cloud-provider-access-create-one-role/&gt;<span class="sb">`</span>_ Documentation <span class="k">for</span> more information.
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>iam_assumed_role_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <ul>
<li><p>ARN of the IAM Role that Atlas assumes when accessing resources in your AWS account. This value is required after the creation (register of the role) as part of <a class="reference external" href="https://docs.atlas.mongodb.com/security/set-up-unified-aws-access/#set-up-unified-aws-access">Set Up Unified AWS Access</a>.</p></li>
</ul>
</p></li>
<li><p><strong>project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique ID for the project to get all Cloud Provider Access</p></li>
<li><p><strong>provider_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The cloud provider for which to create a new role. Currently only AWS is supported.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_mongodbatlas.CloudProviderAccess.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">atlas_assumed_role_external_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">atlas_aws_account_arn</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">authorized_date</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">created_date</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">feature_usages</span><span class="p">:</span> <span class="n">Union[Sequence[Union[CloudProviderAccessFeatureUsageArgs, Mapping[str, Any], Awaitable[Union[CloudProviderAccessFeatureUsageArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[CloudProviderAccessFeatureUsageArgs, Mapping[str, Any], Awaitable[Union[CloudProviderAccessFeatureUsageArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">iam_assumed_role_arn</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">provider_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">role_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_mongodbatlas.cloud_provider_access.CloudProviderAccess<a class="headerlink" href="#pulumi_mongodbatlas.CloudProviderAccess.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing CloudProviderAccess resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>atlas_assumed_role_external_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Unique external ID Atlas uses when assuming the IAM role in your AWS account.</p></li>
<li><p><strong>atlas_aws_account_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – ARN associated with the Atlas AWS account used to assume IAM roles in your AWS account.</p></li>
<li><p><strong>authorized_date</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Date on which this role was authorized.</p></li>
<li><p><strong>created_date</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Date on which this role was created.</p></li>
<li><p><strong>feature_usages</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'CloudProviderAccessFeatureUsageArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – Atlas features this AWS IAM role is linked to.</p></li>
<li><p><strong>iam_assumed_role_arn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <ul>
<li><p>ARN of the IAM Role that Atlas assumes when accessing resources in your AWS account. This value is required after the creation (register of the role) as part of <a class="reference external" href="https://docs.atlas.mongodb.com/security/set-up-unified-aws-access/#set-up-unified-aws-access">Set Up Unified AWS Access</a>.</p></li>
</ul>
</p></li>
<li><p><strong>project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique ID for the project to get all Cloud Provider Access</p></li>
<li><p><strong>provider_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The cloud provider for which to create a new role. Currently only AWS is supported.</p></li>
<li><p><strong>role_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Unique ID of this role.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.CloudProviderAccess.atlas_assumed_role_external_id">
<em class="property">property </em><code class="sig-name descname">atlas_assumed_role_external_id</code><a class="headerlink" href="#pulumi_mongodbatlas.CloudProviderAccess.atlas_assumed_role_external_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Unique external ID Atlas uses when assuming the IAM role in your AWS account.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.CloudProviderAccess.atlas_aws_account_arn">
<em class="property">property </em><code class="sig-name descname">atlas_aws_account_arn</code><a class="headerlink" href="#pulumi_mongodbatlas.CloudProviderAccess.atlas_aws_account_arn" title="Permalink to this definition">¶</a></dt>
<dd><p>ARN associated with the Atlas AWS account used to assume IAM roles in your AWS account.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.CloudProviderAccess.authorized_date">
<em class="property">property </em><code class="sig-name descname">authorized_date</code><a class="headerlink" href="#pulumi_mongodbatlas.CloudProviderAccess.authorized_date" title="Permalink to this definition">¶</a></dt>
<dd><p>Date on which this role was authorized.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.CloudProviderAccess.created_date">
<em class="property">property </em><code class="sig-name descname">created_date</code><a class="headerlink" href="#pulumi_mongodbatlas.CloudProviderAccess.created_date" title="Permalink to this definition">¶</a></dt>
<dd><p>Date on which this role was created.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.CloudProviderAccess.feature_usages">
<em class="property">property </em><code class="sig-name descname">feature_usages</code><a class="headerlink" href="#pulumi_mongodbatlas.CloudProviderAccess.feature_usages" title="Permalink to this definition">¶</a></dt>
<dd><p>Atlas features this AWS IAM role is linked to.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.CloudProviderAccess.iam_assumed_role_arn">
<em class="property">property </em><code class="sig-name descname">iam_assumed_role_arn</code><a class="headerlink" href="#pulumi_mongodbatlas.CloudProviderAccess.iam_assumed_role_arn" title="Permalink to this definition">¶</a></dt>
<dd><ul class="simple">
<li><p>ARN of the IAM Role that Atlas assumes when accessing resources in your AWS account. This value is required after the creation (register of the role) as part of <a class="reference external" href="https://docs.atlas.mongodb.com/security/set-up-unified-aws-access/#set-up-unified-aws-access">Set Up Unified AWS Access</a>.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.CloudProviderAccess.project_id">
<em class="property">property </em><code class="sig-name descname">project_id</code><a class="headerlink" href="#pulumi_mongodbatlas.CloudProviderAccess.project_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The unique ID for the project to get all Cloud Provider Access</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.CloudProviderAccess.provider_name">
<em class="property">property </em><code class="sig-name descname">provider_name</code><a class="headerlink" href="#pulumi_mongodbatlas.CloudProviderAccess.provider_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The cloud provider for which to create a new role. Currently only AWS is supported.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.CloudProviderAccess.role_id">
<em class="property">property </em><code class="sig-name descname">role_id</code><a class="headerlink" href="#pulumi_mongodbatlas.CloudProviderAccess.role_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Unique ID of this role.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.CloudProviderAccess.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.CloudProviderAccess.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_mongodbatlas.CloudProviderAccess.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.CloudProviderAccess.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py class">
<dt id="pulumi_mongodbatlas.CloudProviderSnapshot">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">CloudProviderSnapshot</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cluster_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">retention_in_days</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.CloudProviderSnapshot" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">CloudProviderSnapshot</span></code> provides a resource to take a cloud backup snapshot on demand.
On-demand snapshots happen immediately, unlike scheduled snapshots which occur at regular intervals. If there is already an on-demand snapshot with a status of queued or inProgress, you must wait until Atlas has completed the on-demand snapshot before taking another.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Groups and projects are synonymous terms. You may find <code class="docutils literal notranslate"><span class="pre">groupId</span></code> in the official documentation.</p>
</div></blockquote>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_mongodbatlas</span> <span class="k">as</span> <span class="nn">mongodbatlas</span>

<span class="n">my_cluster</span> <span class="o">=</span> <span class="n">mongodbatlas</span><span class="o">.</span><span class="n">Cluster</span><span class="p">(</span><span class="s2">&quot;myCluster&quot;</span><span class="p">,</span>
    <span class="n">project_id</span><span class="o">=</span><span class="s2">&quot;5cf5a45a9ccf6400e60981b6&quot;</span><span class="p">,</span>
    <span class="n">disk_size_gb</span><span class="o">=</span><span class="mi">5</span><span class="p">,</span>
    <span class="n">provider_name</span><span class="o">=</span><span class="s2">&quot;AWS&quot;</span><span class="p">,</span>
    <span class="n">provider_region_name</span><span class="o">=</span><span class="s2">&quot;EU_WEST_2&quot;</span><span class="p">,</span>
    <span class="n">provider_instance_size_name</span><span class="o">=</span><span class="s2">&quot;M10&quot;</span><span class="p">,</span>
    <span class="n">provider_backup_enabled</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="n">provider_disk_iops</span><span class="o">=</span><span class="mi">100</span><span class="p">,</span>
    <span class="n">provider_encrypt_ebs_volume</span><span class="o">=</span><span class="kc">False</span><span class="p">)</span>
<span class="n">test_cloud_provider_snapshot</span> <span class="o">=</span> <span class="n">mongodbatlas</span><span class="o">.</span><span class="n">CloudProviderSnapshot</span><span class="p">(</span><span class="s2">&quot;testCloudProviderSnapshot&quot;</span><span class="p">,</span>
    <span class="n">project_id</span><span class="o">=</span><span class="n">my_cluster</span><span class="o">.</span><span class="n">project_id</span><span class="p">,</span>
    <span class="n">cluster_name</span><span class="o">=</span><span class="n">my_cluster</span><span class="o">.</span><span class="n">name</span><span class="p">,</span>
    <span class="n">description</span><span class="o">=</span><span class="s2">&quot;myDescription&quot;</span><span class="p">,</span>
    <span class="n">retention_in_days</span><span class="o">=</span><span class="mi">1</span><span class="p">)</span>
<span class="n">test_cloud_provider_snapshot_restore_job</span> <span class="o">=</span> <span class="n">mongodbatlas</span><span class="o">.</span><span class="n">CloudProviderSnapshotRestoreJob</span><span class="p">(</span><span class="s2">&quot;testCloudProviderSnapshotRestoreJob&quot;</span><span class="p">,</span>
    <span class="n">project_id</span><span class="o">=</span><span class="n">test_cloud_provider_snapshot</span><span class="o">.</span><span class="n">project_id</span><span class="p">,</span>
    <span class="n">cluster_name</span><span class="o">=</span><span class="n">test_cloud_provider_snapshot</span><span class="o">.</span><span class="n">cluster_name</span><span class="p">,</span>
    <span class="n">snapshot_id</span><span class="o">=</span><span class="n">test_cloud_provider_snapshot</span><span class="o">.</span><span class="n">snapshot_id</span><span class="p">,</span>
    <span class="n">delivery_type</span><span class="o">=</span><span class="n">mongodbatlas</span><span class="o">.</span><span class="n">CloudProviderSnapshotRestoreJobDeliveryTypeArgs</span><span class="p">(</span>
        <span class="n">download</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="p">))</span>
</pre></div>
</div>
<p>Cloud Backup Snapshot entries can be imported using project project_id, cluster_name and snapshot_id (Unique identifier of the snapshot), in the format <code class="docutils literal notranslate"><span class="pre">PROJECTID-CLUSTERNAME-SNAPSHOTID</span></code>, e.g.</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>   $ pulumi import mongodbatlas:index/cloudProviderSnapshot:CloudProviderSnapshot <span class="nb">test</span> 5d0f1f73cf09a29120e173cf-MyClusterTest-5d116d82014b764445b2f9b5

For more information see<span class="se">\ </span><span class="sb">`</span>MongoDB Atlas API Reference. &lt;https://docs.atlas.mongodb.com/reference/api/cloud-backup/backup/backups/&gt;<span class="sb">`</span>_
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>cluster_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Atlas cluster that contains the snapshots you want to retrieve.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Description of the on-demand snapshot.</p></li>
<li><p><strong>project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique identifier of the project for the Atlas cluster.</p></li>
<li><p><strong>retention_in_days</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The number of days that Atlas should retain the on-demand snapshot. Must be at least 1.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_mongodbatlas.CloudProviderSnapshot.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cluster_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">created_at</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">expires_at</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">master_key_uuid</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">mongod_version</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">retention_in_days</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">snapshot_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">snapshot_type</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">storage_size_bytes</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_mongodbatlas.cloud_provider_snapshot.CloudProviderSnapshot<a class="headerlink" href="#pulumi_mongodbatlas.CloudProviderSnapshot.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing CloudProviderSnapshot resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>cluster_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Atlas cluster that contains the snapshots you want to retrieve.</p></li>
<li><p><strong>created_at</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – UTC ISO 8601 formatted point in time when Atlas took the snapshot.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Description of the on-demand snapshot.</p></li>
<li><p><strong>expires_at</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – UTC ISO 8601 formatted point in time when Atlas will delete the snapshot.</p></li>
<li><p><strong>master_key_uuid</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Unique ID of the AWS KMS Customer Master Key used to encrypt the snapshot. Only visible for clusters using Encryption at Rest via Customer KMS.</p></li>
<li><p><strong>mongod_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Version of the MongoDB server.</p></li>
<li><p><strong>project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique identifier of the project for the Atlas cluster.</p></li>
<li><p><strong>retention_in_days</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The number of days that Atlas should retain the on-demand snapshot. Must be at least 1.</p></li>
<li><p><strong>snapshot_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Unique identifier of the snapshot.</p></li>
<li><p><strong>snapshot_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specified the type of snapshot. Valid values are onDemand and scheduled.</p></li>
<li><p><strong>status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Current status of the snapshot. One of the following values will be returned: queued, inProgress, completed, failed.</p></li>
<li><p><strong>storage_size_bytes</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Specifies the size of the snapshot in bytes.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the type of cluster: replicaSet or shardedCluster.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.CloudProviderSnapshot.cluster_name">
<em class="property">property </em><code class="sig-name descname">cluster_name</code><a class="headerlink" href="#pulumi_mongodbatlas.CloudProviderSnapshot.cluster_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Atlas cluster that contains the snapshots you want to retrieve.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.CloudProviderSnapshot.created_at">
<em class="property">property </em><code class="sig-name descname">created_at</code><a class="headerlink" href="#pulumi_mongodbatlas.CloudProviderSnapshot.created_at" title="Permalink to this definition">¶</a></dt>
<dd><p>UTC ISO 8601 formatted point in time when Atlas took the snapshot.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.CloudProviderSnapshot.description">
<em class="property">property </em><code class="sig-name descname">description</code><a class="headerlink" href="#pulumi_mongodbatlas.CloudProviderSnapshot.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Description of the on-demand snapshot.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.CloudProviderSnapshot.expires_at">
<em class="property">property </em><code class="sig-name descname">expires_at</code><a class="headerlink" href="#pulumi_mongodbatlas.CloudProviderSnapshot.expires_at" title="Permalink to this definition">¶</a></dt>
<dd><p>UTC ISO 8601 formatted point in time when Atlas will delete the snapshot.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.CloudProviderSnapshot.master_key_uuid">
<em class="property">property </em><code class="sig-name descname">master_key_uuid</code><a class="headerlink" href="#pulumi_mongodbatlas.CloudProviderSnapshot.master_key_uuid" title="Permalink to this definition">¶</a></dt>
<dd><p>Unique ID of the AWS KMS Customer Master Key used to encrypt the snapshot. Only visible for clusters using Encryption at Rest via Customer KMS.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.CloudProviderSnapshot.mongod_version">
<em class="property">property </em><code class="sig-name descname">mongod_version</code><a class="headerlink" href="#pulumi_mongodbatlas.CloudProviderSnapshot.mongod_version" title="Permalink to this definition">¶</a></dt>
<dd><p>Version of the MongoDB server.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.CloudProviderSnapshot.project_id">
<em class="property">property </em><code class="sig-name descname">project_id</code><a class="headerlink" href="#pulumi_mongodbatlas.CloudProviderSnapshot.project_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The unique identifier of the project for the Atlas cluster.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.CloudProviderSnapshot.retention_in_days">
<em class="property">property </em><code class="sig-name descname">retention_in_days</code><a class="headerlink" href="#pulumi_mongodbatlas.CloudProviderSnapshot.retention_in_days" title="Permalink to this definition">¶</a></dt>
<dd><p>The number of days that Atlas should retain the on-demand snapshot. Must be at least 1.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.CloudProviderSnapshot.snapshot_id">
<em class="property">property </em><code class="sig-name descname">snapshot_id</code><a class="headerlink" href="#pulumi_mongodbatlas.CloudProviderSnapshot.snapshot_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Unique identifier of the snapshot.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.CloudProviderSnapshot.snapshot_type">
<em class="property">property </em><code class="sig-name descname">snapshot_type</code><a class="headerlink" href="#pulumi_mongodbatlas.CloudProviderSnapshot.snapshot_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Specified the type of snapshot. Valid values are onDemand and scheduled.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.CloudProviderSnapshot.status">
<em class="property">property </em><code class="sig-name descname">status</code><a class="headerlink" href="#pulumi_mongodbatlas.CloudProviderSnapshot.status" title="Permalink to this definition">¶</a></dt>
<dd><p>Current status of the snapshot. One of the following values will be returned: queued, inProgress, completed, failed.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.CloudProviderSnapshot.storage_size_bytes">
<em class="property">property </em><code class="sig-name descname">storage_size_bytes</code><a class="headerlink" href="#pulumi_mongodbatlas.CloudProviderSnapshot.storage_size_bytes" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the size of the snapshot in bytes.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.CloudProviderSnapshot.type">
<em class="property">property </em><code class="sig-name descname">type</code><a class="headerlink" href="#pulumi_mongodbatlas.CloudProviderSnapshot.type" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the type of cluster: replicaSet or shardedCluster.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.CloudProviderSnapshot.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.CloudProviderSnapshot.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_mongodbatlas.CloudProviderSnapshot.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.CloudProviderSnapshot.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py class">
<dt id="pulumi_mongodbatlas.CloudProviderSnapshotBackupPolicy">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">CloudProviderSnapshotBackupPolicy</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cluster_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policies</span><span class="p">:</span> <span class="n">Union[Sequence[Union[CloudProviderSnapshotBackupPolicyPolicyArgs, Mapping[str, Any], Awaitable[Union[CloudProviderSnapshotBackupPolicyPolicyArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[CloudProviderSnapshotBackupPolicyPolicyArgs, Mapping[str, Any], Awaitable[Union[CloudProviderSnapshotBackupPolicyPolicyArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">reference_hour_of_day</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">reference_minute_of_hour</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">restore_window_days</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">update_snapshots</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.CloudProviderSnapshotBackupPolicy" title="Permalink to this definition">¶</a></dt>
<dd><p>Cloud Backup Snapshot Policy entries can be imported using project project_id and cluster_name, in the format <code class="docutils literal notranslate"><span class="pre">PROJECTID-CLUSTERNAME</span></code>, e.g.</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>   $ pulumi import mongodbatlas:index/cloudProviderSnapshotBackupPolicy:CloudProviderSnapshotBackupPolicy <span class="nb">test</span> 5d0f1f73cf09a29120e173cf-MyClusterTest

For more information see<span class="se">\ </span><span class="sb">`</span>MongoDB Atlas API Reference. &lt;https://docs.atlas.mongodb.com/reference/api/cloud-backup/schedule/modify-one-schedule/&gt;<span class="sb">`</span>_
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>cluster_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Atlas cluster that contains the snapshot backup policy you want to retrieve.</p></li>
<li><p><strong>policies</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'CloudProviderSnapshotBackupPolicyPolicyArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – Contains a document for each backup policy item in the desired updated backup policy.</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>* `policies.#.id` - (Required) Unique identifier of the backup policy that you want to update. policies.#.id is a value obtained via the Cluster resource. provider_backup_enabled of the Cluster resource must be set to true. See the example above for how to refer to the Cluster resource for policies.#.id
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique identifier of the project for the Atlas cluster.</p></li>
<li><p><strong>reference_hour_of_day</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – UTC Hour of day between 0 and 23, inclusive, representing which hour of the day that Atlas takes snapshots for backup policy items.</p></li>
<li><p><strong>reference_minute_of_hour</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – UTC Minutes after referenceHourOfDay that Atlas takes snapshots for backup policy items. Must be between 0 and 59, inclusive.</p></li>
<li><p><strong>restore_window_days</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Number of days back in time you can restore to with point-in-time accuracy. Must be a positive, non-zero integer.</p></li>
<li><p><strong>update_snapshots</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specify true to apply the retention changes in the updated backup policy to snapshots that Atlas took previously.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_mongodbatlas.CloudProviderSnapshotBackupPolicy.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cluster_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cluster_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">next_snapshot</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policies</span><span class="p">:</span> <span class="n">Union[Sequence[Union[CloudProviderSnapshotBackupPolicyPolicyArgs, Mapping[str, Any], Awaitable[Union[CloudProviderSnapshotBackupPolicyPolicyArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[CloudProviderSnapshotBackupPolicyPolicyArgs, Mapping[str, Any], Awaitable[Union[CloudProviderSnapshotBackupPolicyPolicyArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">reference_hour_of_day</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">reference_minute_of_hour</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">restore_window_days</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">update_snapshots</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_mongodbatlas.cloud_provider_snapshot_backup_policy.CloudProviderSnapshotBackupPolicy<a class="headerlink" href="#pulumi_mongodbatlas.CloudProviderSnapshotBackupPolicy.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing CloudProviderSnapshotBackupPolicy resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>cluster_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Unique identifier of the Atlas cluster.</p></li>
<li><p><strong>cluster_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Atlas cluster that contains the snapshot backup policy you want to retrieve.</p></li>
<li><p><strong>next_snapshot</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Timestamp in the number of seconds that have elapsed since the UNIX epoch when Atlas takes the next snapshot.</p></li>
<li><p><strong>policies</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'CloudProviderSnapshotBackupPolicyPolicyArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – Contains a document for each backup policy item in the desired updated backup policy.</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>* `policies.#.id` - (Required) Unique identifier of the backup policy that you want to update. policies.#.id is a value obtained via the Cluster resource. provider_backup_enabled of the Cluster resource must be set to true. See the example above for how to refer to the Cluster resource for policies.#.id
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique identifier of the project for the Atlas cluster.</p></li>
<li><p><strong>reference_hour_of_day</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – UTC Hour of day between 0 and 23, inclusive, representing which hour of the day that Atlas takes snapshots for backup policy items.</p></li>
<li><p><strong>reference_minute_of_hour</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – UTC Minutes after referenceHourOfDay that Atlas takes snapshots for backup policy items. Must be between 0 and 59, inclusive.</p></li>
<li><p><strong>restore_window_days</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Number of days back in time you can restore to with point-in-time accuracy. Must be a positive, non-zero integer.</p></li>
<li><p><strong>update_snapshots</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specify true to apply the retention changes in the updated backup policy to snapshots that Atlas took previously.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.CloudProviderSnapshotBackupPolicy.cluster_id">
<em class="property">property </em><code class="sig-name descname">cluster_id</code><a class="headerlink" href="#pulumi_mongodbatlas.CloudProviderSnapshotBackupPolicy.cluster_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Unique identifier of the Atlas cluster.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.CloudProviderSnapshotBackupPolicy.cluster_name">
<em class="property">property </em><code class="sig-name descname">cluster_name</code><a class="headerlink" href="#pulumi_mongodbatlas.CloudProviderSnapshotBackupPolicy.cluster_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Atlas cluster that contains the snapshot backup policy you want to retrieve.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.CloudProviderSnapshotBackupPolicy.next_snapshot">
<em class="property">property </em><code class="sig-name descname">next_snapshot</code><a class="headerlink" href="#pulumi_mongodbatlas.CloudProviderSnapshotBackupPolicy.next_snapshot" title="Permalink to this definition">¶</a></dt>
<dd><p>Timestamp in the number of seconds that have elapsed since the UNIX epoch when Atlas takes the next snapshot.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.CloudProviderSnapshotBackupPolicy.policies">
<em class="property">property </em><code class="sig-name descname">policies</code><a class="headerlink" href="#pulumi_mongodbatlas.CloudProviderSnapshotBackupPolicy.policies" title="Permalink to this definition">¶</a></dt>
<dd><p>Contains a document for each backup policy item in the desired updated backup policy.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">policies.#.id</span></code> - (Required) Unique identifier of the backup policy that you want to update. policies.#.id is a value obtained via the Cluster resource. provider_backup_enabled of the Cluster resource must be set to true. See the example above for how to refer to the Cluster resource for policies.#.id</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.CloudProviderSnapshotBackupPolicy.project_id">
<em class="property">property </em><code class="sig-name descname">project_id</code><a class="headerlink" href="#pulumi_mongodbatlas.CloudProviderSnapshotBackupPolicy.project_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The unique identifier of the project for the Atlas cluster.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.CloudProviderSnapshotBackupPolicy.reference_hour_of_day">
<em class="property">property </em><code class="sig-name descname">reference_hour_of_day</code><a class="headerlink" href="#pulumi_mongodbatlas.CloudProviderSnapshotBackupPolicy.reference_hour_of_day" title="Permalink to this definition">¶</a></dt>
<dd><p>UTC Hour of day between 0 and 23, inclusive, representing which hour of the day that Atlas takes snapshots for backup policy items.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.CloudProviderSnapshotBackupPolicy.reference_minute_of_hour">
<em class="property">property </em><code class="sig-name descname">reference_minute_of_hour</code><a class="headerlink" href="#pulumi_mongodbatlas.CloudProviderSnapshotBackupPolicy.reference_minute_of_hour" title="Permalink to this definition">¶</a></dt>
<dd><p>UTC Minutes after referenceHourOfDay that Atlas takes snapshots for backup policy items. Must be between 0 and 59, inclusive.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.CloudProviderSnapshotBackupPolicy.restore_window_days">
<em class="property">property </em><code class="sig-name descname">restore_window_days</code><a class="headerlink" href="#pulumi_mongodbatlas.CloudProviderSnapshotBackupPolicy.restore_window_days" title="Permalink to this definition">¶</a></dt>
<dd><p>Number of days back in time you can restore to with point-in-time accuracy. Must be a positive, non-zero integer.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.CloudProviderSnapshotBackupPolicy.update_snapshots">
<em class="property">property </em><code class="sig-name descname">update_snapshots</code><a class="headerlink" href="#pulumi_mongodbatlas.CloudProviderSnapshotBackupPolicy.update_snapshots" title="Permalink to this definition">¶</a></dt>
<dd><p>Specify true to apply the retention changes in the updated backup policy to snapshots that Atlas took previously.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.CloudProviderSnapshotBackupPolicy.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.CloudProviderSnapshotBackupPolicy.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_mongodbatlas.CloudProviderSnapshotBackupPolicy.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.CloudProviderSnapshotBackupPolicy.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py class">
<dt id="pulumi_mongodbatlas.CloudProviderSnapshotRestoreJob">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">CloudProviderSnapshotRestoreJob</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cluster_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">delivery_type</span><span class="p">:</span> <span class="n">Union[CloudProviderSnapshotRestoreJobDeliveryTypeArgs, Mapping[str, Any], Awaitable[Union[CloudProviderSnapshotRestoreJobDeliveryTypeArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">snapshot_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.CloudProviderSnapshotRestoreJob" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">CloudProviderSnapshotRestoreJob</span></code> provides a resource to create a new restore job from a cloud backup snapshot of a specified cluster. The restore job can be one of three types:</p>
<ul class="simple">
<li><p><strong>automated:</strong> Atlas automatically restores the snapshot with snapshotId to the Atlas cluster with name targetClusterName in the Atlas project with targetGroupId.</p></li>
<li><p><strong>download:</strong> Atlas provides a URL to download a .tar.gz of the snapshot with snapshotId. The contents of the archive contain the data files for your Atlas cluster.</p></li>
<li><p><strong>pointInTime:</strong>  Atlas performs a Continuous Cloud Backup restore.</p></li>
</ul>
<blockquote>
<div><p><strong>Important:</strong> If you specify <code class="docutils literal notranslate"><span class="pre">deliveryType</span></code> : <code class="docutils literal notranslate"><span class="pre">automated</span></code> or <code class="docutils literal notranslate"><span class="pre">deliveryType</span></code> : <code class="docutils literal notranslate"><span class="pre">pointInTime</span></code> in your request body to create an automated restore job, Atlas removes all existing data on the target cluster prior to the restore.</p>
<p><strong>NOTE:</strong> Groups and projects are synonymous terms. You may find <code class="docutils literal notranslate"><span class="pre">groupId</span></code> in the official documentation.</p>
</div></blockquote>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_mongodbatlas</span> <span class="k">as</span> <span class="nn">mongodbatlas</span>

<span class="n">my_cluster</span> <span class="o">=</span> <span class="n">mongodbatlas</span><span class="o">.</span><span class="n">Cluster</span><span class="p">(</span><span class="s2">&quot;myCluster&quot;</span><span class="p">,</span>
    <span class="n">project_id</span><span class="o">=</span><span class="s2">&quot;5cf5a45a9ccf6400e60981b6&quot;</span><span class="p">,</span>
    <span class="n">disk_size_gb</span><span class="o">=</span><span class="mi">5</span><span class="p">,</span>
    <span class="n">provider_name</span><span class="o">=</span><span class="s2">&quot;AWS&quot;</span><span class="p">,</span>
    <span class="n">provider_region_name</span><span class="o">=</span><span class="s2">&quot;EU_WEST_2&quot;</span><span class="p">,</span>
    <span class="n">provider_instance_size_name</span><span class="o">=</span><span class="s2">&quot;M10&quot;</span><span class="p">,</span>
    <span class="n">provider_backup_enabled</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="n">provider_disk_iops</span><span class="o">=</span><span class="mi">100</span><span class="p">,</span>
    <span class="n">provider_encrypt_ebs_volume</span><span class="o">=</span><span class="kc">False</span><span class="p">)</span>
<span class="n">test_cloud_provider_snapshot</span> <span class="o">=</span> <span class="n">mongodbatlas</span><span class="o">.</span><span class="n">CloudProviderSnapshot</span><span class="p">(</span><span class="s2">&quot;testCloudProviderSnapshot&quot;</span><span class="p">,</span>
    <span class="n">project_id</span><span class="o">=</span><span class="n">my_cluster</span><span class="o">.</span><span class="n">project_id</span><span class="p">,</span>
    <span class="n">cluster_name</span><span class="o">=</span><span class="n">my_cluster</span><span class="o">.</span><span class="n">name</span><span class="p">,</span>
    <span class="n">description</span><span class="o">=</span><span class="s2">&quot;myDescription&quot;</span><span class="p">,</span>
    <span class="n">retention_in_days</span><span class="o">=</span><span class="mi">1</span><span class="p">)</span>
<span class="n">test_cloud_provider_snapshot_restore_job</span> <span class="o">=</span> <span class="n">mongodbatlas</span><span class="o">.</span><span class="n">CloudProviderSnapshotRestoreJob</span><span class="p">(</span><span class="s2">&quot;testCloudProviderSnapshotRestoreJob&quot;</span><span class="p">,</span>
    <span class="n">project_id</span><span class="o">=</span><span class="n">test_cloud_provider_snapshot</span><span class="o">.</span><span class="n">project_id</span><span class="p">,</span>
    <span class="n">cluster_name</span><span class="o">=</span><span class="n">test_cloud_provider_snapshot</span><span class="o">.</span><span class="n">cluster_name</span><span class="p">,</span>
    <span class="n">snapshot_id</span><span class="o">=</span><span class="n">test_cloud_provider_snapshot</span><span class="o">.</span><span class="n">snapshot_id</span><span class="p">,</span>
    <span class="n">delivery_type</span><span class="o">=</span><span class="n">mongodbatlas</span><span class="o">.</span><span class="n">CloudProviderSnapshotRestoreJobDeliveryTypeArgs</span><span class="p">(</span>
        <span class="n">automated</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
        <span class="n">target_cluster_name</span><span class="o">=</span><span class="s2">&quot;MyCluster&quot;</span><span class="p">,</span>
        <span class="n">target_project_id</span><span class="o">=</span><span class="s2">&quot;5cf5a45a9ccf6400e60981b6&quot;</span><span class="p">,</span>
    <span class="p">),</span>
    <span class="n">opts</span><span class="o">=</span><span class="n">pulumi</span><span class="o">.</span><span class="n">ResourceOptions</span><span class="p">(</span><span class="n">depends_on</span><span class="o">=</span><span class="p">[</span><span class="s2">&quot;mongodbatlas_cloud_provider_snapshot.test&quot;</span><span class="p">]))</span>
</pre></div>
</div>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_mongodbatlas</span> <span class="k">as</span> <span class="nn">mongodbatlas</span>

<span class="n">my_cluster</span> <span class="o">=</span> <span class="n">mongodbatlas</span><span class="o">.</span><span class="n">Cluster</span><span class="p">(</span><span class="s2">&quot;myCluster&quot;</span><span class="p">,</span>
    <span class="n">project_id</span><span class="o">=</span><span class="s2">&quot;5cf5a45a9ccf6400e60981b6&quot;</span><span class="p">,</span>
    <span class="n">disk_size_gb</span><span class="o">=</span><span class="mi">5</span><span class="p">,</span>
    <span class="n">provider_name</span><span class="o">=</span><span class="s2">&quot;AWS&quot;</span><span class="p">,</span>
    <span class="n">provider_region_name</span><span class="o">=</span><span class="s2">&quot;EU_WEST_2&quot;</span><span class="p">,</span>
    <span class="n">provider_instance_size_name</span><span class="o">=</span><span class="s2">&quot;M10&quot;</span><span class="p">,</span>
    <span class="n">provider_backup_enabled</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="n">provider_disk_iops</span><span class="o">=</span><span class="mi">100</span><span class="p">,</span>
    <span class="n">provider_encrypt_ebs_volume</span><span class="o">=</span><span class="kc">False</span><span class="p">)</span>
<span class="n">test_cloud_provider_snapshot</span> <span class="o">=</span> <span class="n">mongodbatlas</span><span class="o">.</span><span class="n">CloudProviderSnapshot</span><span class="p">(</span><span class="s2">&quot;testCloudProviderSnapshot&quot;</span><span class="p">,</span>
    <span class="n">project_id</span><span class="o">=</span><span class="n">my_cluster</span><span class="o">.</span><span class="n">project_id</span><span class="p">,</span>
    <span class="n">cluster_name</span><span class="o">=</span><span class="n">my_cluster</span><span class="o">.</span><span class="n">name</span><span class="p">,</span>
    <span class="n">description</span><span class="o">=</span><span class="s2">&quot;myDescription&quot;</span><span class="p">,</span>
    <span class="n">retention_in_days</span><span class="o">=</span><span class="mi">1</span><span class="p">)</span>
<span class="n">test_cloud_provider_snapshot_restore_job</span> <span class="o">=</span> <span class="n">mongodbatlas</span><span class="o">.</span><span class="n">CloudProviderSnapshotRestoreJob</span><span class="p">(</span><span class="s2">&quot;testCloudProviderSnapshotRestoreJob&quot;</span><span class="p">,</span>
    <span class="n">project_id</span><span class="o">=</span><span class="n">test_cloud_provider_snapshot</span><span class="o">.</span><span class="n">project_id</span><span class="p">,</span>
    <span class="n">cluster_name</span><span class="o">=</span><span class="n">test_cloud_provider_snapshot</span><span class="o">.</span><span class="n">cluster_name</span><span class="p">,</span>
    <span class="n">snapshot_id</span><span class="o">=</span><span class="n">test_cloud_provider_snapshot</span><span class="o">.</span><span class="n">snapshot_id</span><span class="p">,</span>
    <span class="n">delivery_type</span><span class="o">=</span><span class="n">mongodbatlas</span><span class="o">.</span><span class="n">CloudProviderSnapshotRestoreJobDeliveryTypeArgs</span><span class="p">(</span>
        <span class="n">download</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="p">))</span>
</pre></div>
</div>
<p>Cloud Backup Snapshot Restore Job entries can be imported using project project_id, cluster_name and snapshot_id (Unique identifier of the snapshot), in the format <code class="docutils literal notranslate"><span class="pre">PROJECTID-CLUSTERNAME-JOBID</span></code>, e.g.</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>   $ pulumi import mongodbatlas:index/cloudProviderSnapshotRestoreJob:CloudProviderSnapshotRestoreJob <span class="nb">test</span> 5cf5a45a9ccf6400e60981b6-MyCluster-5d1b654ecf09a24b888f4c79

For more information see<span class="se">\ </span><span class="sb">`</span>MongoDB Atlas API Reference. &lt;https://docs.atlas.mongodb.com/reference/api/cloud-backup/restore/restores/&gt;<span class="sb">`</span>_
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>cluster_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Atlas cluster whose snapshot you want to restore.</p></li>
<li><p><strong>delivery_type</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'CloudProviderSnapshotRestoreJobDeliveryTypeArgs'</em><em>]</em><em>]</em>) – Type of restore job to create. Possible values are: <strong>download</strong> or <strong>automated</strong>, only one must be set it in <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique identifier of the project for the Atlas cluster whose snapshot you want to restore.</p></li>
<li><p><strong>snapshot_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Unique identifier of the snapshot to restore.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_mongodbatlas.CloudProviderSnapshotRestoreJob.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cancelled</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cluster_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">created_at</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">delivery_type</span><span class="p">:</span> <span class="n">Union[CloudProviderSnapshotRestoreJobDeliveryTypeArgs, Mapping[str, Any], Awaitable[Union[CloudProviderSnapshotRestoreJobDeliveryTypeArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">delivery_urls</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">expired</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">expires_at</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">finished_at</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">snapshot_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">snapshot_restore_job_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">timestamp</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_mongodbatlas.cloud_provider_snapshot_restore_job.CloudProviderSnapshotRestoreJob<a class="headerlink" href="#pulumi_mongodbatlas.CloudProviderSnapshotRestoreJob.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing CloudProviderSnapshotRestoreJob resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>cancelled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Indicates whether the restore job was canceled.</p></li>
<li><p><strong>cluster_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Atlas cluster whose snapshot you want to restore.</p></li>
<li><p><strong>created_at</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – UTC ISO 8601 formatted point in time when Atlas created the restore job.</p></li>
<li><p><strong>delivery_type</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'CloudProviderSnapshotRestoreJobDeliveryTypeArgs'</em><em>]</em><em>]</em>) – Type of restore job to create. Possible values are: <strong>download</strong> or <strong>automated</strong>, only one must be set it in <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>delivery_urls</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – One or more URLs for the compressed snapshot files for manual download. Only visible if deliveryType is download.</p></li>
<li><p><strong>expired</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Indicates whether the restore job expired.</p></li>
<li><p><strong>expires_at</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – UTC ISO 8601 formatted point in time when the restore job expires.</p></li>
<li><p><strong>finished_at</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – UTC ISO 8601 formatted point in time when the restore job completed.</p></li>
<li><p><strong>project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique identifier of the project for the Atlas cluster whose snapshot you want to restore.</p></li>
<li><p><strong>snapshot_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Unique identifier of the snapshot to restore.</p></li>
<li><p><strong>snapshot_restore_job_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique identifier of the restore job.</p></li>
<li><p><strong>timestamp</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Timestamp in ISO 8601 date and time format in UTC when the snapshot associated to snapshotId was taken.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.CloudProviderSnapshotRestoreJob.cancelled">
<em class="property">property </em><code class="sig-name descname">cancelled</code><a class="headerlink" href="#pulumi_mongodbatlas.CloudProviderSnapshotRestoreJob.cancelled" title="Permalink to this definition">¶</a></dt>
<dd><p>Indicates whether the restore job was canceled.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.CloudProviderSnapshotRestoreJob.cluster_name">
<em class="property">property </em><code class="sig-name descname">cluster_name</code><a class="headerlink" href="#pulumi_mongodbatlas.CloudProviderSnapshotRestoreJob.cluster_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Atlas cluster whose snapshot you want to restore.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.CloudProviderSnapshotRestoreJob.created_at">
<em class="property">property </em><code class="sig-name descname">created_at</code><a class="headerlink" href="#pulumi_mongodbatlas.CloudProviderSnapshotRestoreJob.created_at" title="Permalink to this definition">¶</a></dt>
<dd><p>UTC ISO 8601 formatted point in time when Atlas created the restore job.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.CloudProviderSnapshotRestoreJob.delivery_type">
<em class="property">property </em><code class="sig-name descname">delivery_type</code><a class="headerlink" href="#pulumi_mongodbatlas.CloudProviderSnapshotRestoreJob.delivery_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Type of restore job to create. Possible values are: <strong>download</strong> or <strong>automated</strong>, only one must be set it in <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.CloudProviderSnapshotRestoreJob.delivery_urls">
<em class="property">property </em><code class="sig-name descname">delivery_urls</code><a class="headerlink" href="#pulumi_mongodbatlas.CloudProviderSnapshotRestoreJob.delivery_urls" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more URLs for the compressed snapshot files for manual download. Only visible if deliveryType is download.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.CloudProviderSnapshotRestoreJob.expired">
<em class="property">property </em><code class="sig-name descname">expired</code><a class="headerlink" href="#pulumi_mongodbatlas.CloudProviderSnapshotRestoreJob.expired" title="Permalink to this definition">¶</a></dt>
<dd><p>Indicates whether the restore job expired.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.CloudProviderSnapshotRestoreJob.expires_at">
<em class="property">property </em><code class="sig-name descname">expires_at</code><a class="headerlink" href="#pulumi_mongodbatlas.CloudProviderSnapshotRestoreJob.expires_at" title="Permalink to this definition">¶</a></dt>
<dd><p>UTC ISO 8601 formatted point in time when the restore job expires.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.CloudProviderSnapshotRestoreJob.finished_at">
<em class="property">property </em><code class="sig-name descname">finished_at</code><a class="headerlink" href="#pulumi_mongodbatlas.CloudProviderSnapshotRestoreJob.finished_at" title="Permalink to this definition">¶</a></dt>
<dd><p>UTC ISO 8601 formatted point in time when the restore job completed.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.CloudProviderSnapshotRestoreJob.project_id">
<em class="property">property </em><code class="sig-name descname">project_id</code><a class="headerlink" href="#pulumi_mongodbatlas.CloudProviderSnapshotRestoreJob.project_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The unique identifier of the project for the Atlas cluster whose snapshot you want to restore.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.CloudProviderSnapshotRestoreJob.snapshot_id">
<em class="property">property </em><code class="sig-name descname">snapshot_id</code><a class="headerlink" href="#pulumi_mongodbatlas.CloudProviderSnapshotRestoreJob.snapshot_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Unique identifier of the snapshot to restore.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.CloudProviderSnapshotRestoreJob.snapshot_restore_job_id">
<em class="property">property </em><code class="sig-name descname">snapshot_restore_job_id</code><a class="headerlink" href="#pulumi_mongodbatlas.CloudProviderSnapshotRestoreJob.snapshot_restore_job_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The unique identifier of the restore job.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.CloudProviderSnapshotRestoreJob.timestamp">
<em class="property">property </em><code class="sig-name descname">timestamp</code><a class="headerlink" href="#pulumi_mongodbatlas.CloudProviderSnapshotRestoreJob.timestamp" title="Permalink to this definition">¶</a></dt>
<dd><p>Timestamp in ISO 8601 date and time format in UTC when the snapshot associated to snapshotId was taken.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.CloudProviderSnapshotRestoreJob.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.CloudProviderSnapshotRestoreJob.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_mongodbatlas.CloudProviderSnapshotRestoreJob.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.CloudProviderSnapshotRestoreJob.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py class">
<dt id="pulumi_mongodbatlas.Cluster">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">Cluster</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">advanced_configuration</span><span class="p">:</span> <span class="n">Union[ClusterAdvancedConfigurationArgs, Mapping[str, Any], Awaitable[Union[ClusterAdvancedConfigurationArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auto_scaling_compute_enabled</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auto_scaling_compute_scale_down_enabled</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auto_scaling_disk_gb_enabled</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">backing_provider_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">backup_enabled</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">bi_connector</span><span class="p">:</span> <span class="n">Union[ClusterBiConnectorArgs, Mapping[str, Any], Awaitable[Union[ClusterBiConnectorArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cluster_type</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">disk_size_gb</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">encryption_at_rest_provider</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">labels</span><span class="p">:</span> <span class="n">Union[Sequence[Union[ClusterLabelArgs, Mapping[str, Any], Awaitable[Union[ClusterLabelArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[ClusterLabelArgs, Mapping[str, Any], Awaitable[Union[ClusterLabelArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">mongo_db_major_version</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">num_shards</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">pit_enabled</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">provider_auto_scaling_compute_max_instance_size</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">provider_auto_scaling_compute_min_instance_size</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">provider_backup_enabled</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">provider_disk_iops</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">provider_disk_type_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">provider_encrypt_ebs_volume</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">provider_instance_size_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">provider_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">provider_region_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">provider_volume_type</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">replication_factor</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">replication_specs</span><span class="p">:</span> <span class="n">Union[Sequence[Union[ClusterReplicationSpecArgs, Mapping[str, Any], Awaitable[Union[ClusterReplicationSpecArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[ClusterReplicationSpecArgs, Mapping[str, Any], Awaitable[Union[ClusterReplicationSpecArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.Cluster" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">Cluster</span></code> provides a Cluster resource. The resource lets you create, edit and delete clusters. The resource requires your Project ID.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Groups and projects are synonymous terms. You may find group_id in the official documentation.</p>
<p><strong>NOTE:</strong> A network container is created for a cluster to reside in if one does not yet exist in the project.  To  use this automatically created container with another resource, such as peering, the <code class="docutils literal notranslate"><span class="pre">container_id</span></code> is exported after creation.</p>
<p><strong>IMPORTANT:</strong>
<span class="raw-html-m2r"><br></span> &amp;#8226; Free tier cluster creation (M0) is not supported via API or by this Provider.
<span class="raw-html-m2r"><br></span> &amp;#8226; Shared tier clusters (M2, M5) cannot be upgraded to higher tiers via API or by this Provider.
<span class="raw-html-m2r"><br></span> &amp;#8226; Changes to cluster configurations can affect costs. Before making changes, please see <a class="reference external" href="https://docs.atlas.mongodb.com/billing/">Billing</a>.        <span class="raw-html-m2r"><br></span> &amp;#8226; If your Atlas project contains a custom role that uses actions introduced in a specific MongoDB version, you cannot create a cluster with a MongoDB version less than that version unless you delete the custom role.</p>
</div></blockquote>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_mongodbatlas</span> <span class="k">as</span> <span class="nn">mongodbatlas</span>

<span class="n">cluster_test</span> <span class="o">=</span> <span class="n">mongodbatlas</span><span class="o">.</span><span class="n">Cluster</span><span class="p">(</span><span class="s2">&quot;cluster-test&quot;</span><span class="p">,</span>
    <span class="n">auto_scaling_disk_gb_enabled</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="n">cluster_type</span><span class="o">=</span><span class="s2">&quot;REPLICASET&quot;</span><span class="p">,</span>
    <span class="n">disk_size_gb</span><span class="o">=</span><span class="mi">100</span><span class="p">,</span>
    <span class="n">mongo_db_major_version</span><span class="o">=</span><span class="s2">&quot;4.2&quot;</span><span class="p">,</span>
    <span class="n">project_id</span><span class="o">=</span><span class="s2">&quot;&lt;YOUR-PROJECT-ID&gt;&quot;</span><span class="p">,</span>
    <span class="n">provider_backup_enabled</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="n">provider_disk_iops</span><span class="o">=</span><span class="mi">300</span><span class="p">,</span>
    <span class="n">provider_encrypt_ebs_volume</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="n">provider_instance_size_name</span><span class="o">=</span><span class="s2">&quot;M40&quot;</span><span class="p">,</span>
    <span class="n">provider_name</span><span class="o">=</span><span class="s2">&quot;AWS&quot;</span><span class="p">,</span>
    <span class="n">provider_volume_type</span><span class="o">=</span><span class="s2">&quot;STANDARD&quot;</span><span class="p">,</span>
    <span class="n">replication_specs</span><span class="o">=</span><span class="p">[</span><span class="n">mongodbatlas</span><span class="o">.</span><span class="n">ClusterReplicationSpecArgs</span><span class="p">(</span>
        <span class="n">num_shards</span><span class="o">=</span><span class="mi">1</span><span class="p">,</span>
        <span class="n">regions_configs</span><span class="o">=</span><span class="p">[</span><span class="n">mongodbatlas</span><span class="o">.</span><span class="n">ClusterReplicationSpecRegionsConfigArgs</span><span class="p">(</span>
            <span class="n">electable_nodes</span><span class="o">=</span><span class="mi">3</span><span class="p">,</span>
            <span class="n">priority</span><span class="o">=</span><span class="mi">7</span><span class="p">,</span>
            <span class="n">read_only_nodes</span><span class="o">=</span><span class="mi">0</span><span class="p">,</span>
            <span class="n">region_name</span><span class="o">=</span><span class="s2">&quot;US_EAST_1&quot;</span><span class="p">,</span>
        <span class="p">)],</span>
    <span class="p">)])</span>
</pre></div>
</div>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_mongodbatlas</span> <span class="k">as</span> <span class="nn">mongodbatlas</span>

<span class="n">test</span> <span class="o">=</span> <span class="n">mongodbatlas</span><span class="o">.</span><span class="n">Cluster</span><span class="p">(</span><span class="s2">&quot;test&quot;</span><span class="p">,</span>
    <span class="n">auto_scaling_disk_gb_enabled</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="n">cluster_type</span><span class="o">=</span><span class="s2">&quot;REPLICASET&quot;</span><span class="p">,</span>
    <span class="n">mongo_db_major_version</span><span class="o">=</span><span class="s2">&quot;4.2&quot;</span><span class="p">,</span>
    <span class="n">project_id</span><span class="o">=</span><span class="s2">&quot;&lt;YOUR-PROJECT-ID&gt;&quot;</span><span class="p">,</span>
    <span class="n">provider_backup_enabled</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="n">provider_disk_type_name</span><span class="o">=</span><span class="s2">&quot;P6&quot;</span><span class="p">,</span>
    <span class="n">provider_instance_size_name</span><span class="o">=</span><span class="s2">&quot;M30&quot;</span><span class="p">,</span>
    <span class="n">provider_name</span><span class="o">=</span><span class="s2">&quot;AZURE&quot;</span><span class="p">,</span>
    <span class="n">replication_specs</span><span class="o">=</span><span class="p">[</span><span class="n">mongodbatlas</span><span class="o">.</span><span class="n">ClusterReplicationSpecArgs</span><span class="p">(</span>
        <span class="n">num_shards</span><span class="o">=</span><span class="mi">1</span><span class="p">,</span>
        <span class="n">regions_configs</span><span class="o">=</span><span class="p">[</span><span class="n">mongodbatlas</span><span class="o">.</span><span class="n">ClusterReplicationSpecRegionsConfigArgs</span><span class="p">(</span>
            <span class="n">electable_nodes</span><span class="o">=</span><span class="mi">3</span><span class="p">,</span>
            <span class="n">priority</span><span class="o">=</span><span class="mi">7</span><span class="p">,</span>
            <span class="n">read_only_nodes</span><span class="o">=</span><span class="mi">0</span><span class="p">,</span>
            <span class="n">region_name</span><span class="o">=</span><span class="s2">&quot;US_EAST_1&quot;</span><span class="p">,</span>
        <span class="p">)],</span>
    <span class="p">)])</span>
</pre></div>
</div>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_mongodbatlas</span> <span class="k">as</span> <span class="nn">mongodbatlas</span>

<span class="n">test</span> <span class="o">=</span> <span class="n">mongodbatlas</span><span class="o">.</span><span class="n">Cluster</span><span class="p">(</span><span class="s2">&quot;test&quot;</span><span class="p">,</span>
    <span class="n">auto_scaling_disk_gb_enabled</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="n">cluster_type</span><span class="o">=</span><span class="s2">&quot;REPLICASET&quot;</span><span class="p">,</span>
    <span class="n">disk_size_gb</span><span class="o">=</span><span class="mi">40</span><span class="p">,</span>
    <span class="n">mongo_db_major_version</span><span class="o">=</span><span class="s2">&quot;4.2&quot;</span><span class="p">,</span>
    <span class="n">project_id</span><span class="o">=</span><span class="s2">&quot;&lt;YOUR-PROJECT-ID&gt;&quot;</span><span class="p">,</span>
    <span class="n">provider_backup_enabled</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="n">provider_instance_size_name</span><span class="o">=</span><span class="s2">&quot;M30&quot;</span><span class="p">,</span>
    <span class="n">provider_name</span><span class="o">=</span><span class="s2">&quot;GCP&quot;</span><span class="p">,</span>
    <span class="n">replication_specs</span><span class="o">=</span><span class="p">[</span><span class="n">mongodbatlas</span><span class="o">.</span><span class="n">ClusterReplicationSpecArgs</span><span class="p">(</span>
        <span class="n">num_shards</span><span class="o">=</span><span class="mi">1</span><span class="p">,</span>
        <span class="n">regions_configs</span><span class="o">=</span><span class="p">[</span><span class="n">mongodbatlas</span><span class="o">.</span><span class="n">ClusterReplicationSpecRegionsConfigArgs</span><span class="p">(</span>
            <span class="n">electable_nodes</span><span class="o">=</span><span class="mi">3</span><span class="p">,</span>
            <span class="n">priority</span><span class="o">=</span><span class="mi">7</span><span class="p">,</span>
            <span class="n">read_only_nodes</span><span class="o">=</span><span class="mi">0</span><span class="p">,</span>
            <span class="n">region_name</span><span class="o">=</span><span class="s2">&quot;US_EAST_1&quot;</span><span class="p">,</span>
        <span class="p">)],</span>
    <span class="p">)])</span>
</pre></div>
</div>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_mongodbatlas</span> <span class="k">as</span> <span class="nn">mongodbatlas</span>

<span class="n">cluster_test</span> <span class="o">=</span> <span class="n">mongodbatlas</span><span class="o">.</span><span class="n">Cluster</span><span class="p">(</span><span class="s2">&quot;cluster-test&quot;</span><span class="p">,</span>
    <span class="n">cluster_type</span><span class="o">=</span><span class="s2">&quot;REPLICASET&quot;</span><span class="p">,</span>
    <span class="n">disk_size_gb</span><span class="o">=</span><span class="mi">100</span><span class="p">,</span>
    <span class="n">num_shards</span><span class="o">=</span><span class="mi">1</span><span class="p">,</span>
    <span class="n">project_id</span><span class="o">=</span><span class="s2">&quot;&lt;YOUR-PROJECT-ID&gt;&quot;</span><span class="p">,</span>
    <span class="n">provider_backup_enabled</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="n">provider_disk_iops</span><span class="o">=</span><span class="mi">300</span><span class="p">,</span>
    <span class="n">provider_instance_size_name</span><span class="o">=</span><span class="s2">&quot;M10&quot;</span><span class="p">,</span>
    <span class="n">provider_name</span><span class="o">=</span><span class="s2">&quot;AWS&quot;</span><span class="p">,</span>
    <span class="n">provider_volume_type</span><span class="o">=</span><span class="s2">&quot;STANDARD&quot;</span><span class="p">,</span>
    <span class="n">replication_specs</span><span class="o">=</span><span class="p">[</span><span class="n">mongodbatlas</span><span class="o">.</span><span class="n">ClusterReplicationSpecArgs</span><span class="p">(</span>
        <span class="n">num_shards</span><span class="o">=</span><span class="mi">1</span><span class="p">,</span>
        <span class="n">regions_configs</span><span class="o">=</span><span class="p">[</span>
            <span class="n">mongodbatlas</span><span class="o">.</span><span class="n">ClusterReplicationSpecRegionsConfigArgs</span><span class="p">(</span>
                <span class="n">electable_nodes</span><span class="o">=</span><span class="mi">3</span><span class="p">,</span>
                <span class="n">priority</span><span class="o">=</span><span class="mi">7</span><span class="p">,</span>
                <span class="n">read_only_nodes</span><span class="o">=</span><span class="mi">0</span><span class="p">,</span>
                <span class="n">region_name</span><span class="o">=</span><span class="s2">&quot;US_EAST_1&quot;</span><span class="p">,</span>
            <span class="p">),</span>
            <span class="n">mongodbatlas</span><span class="o">.</span><span class="n">ClusterReplicationSpecRegionsConfigArgs</span><span class="p">(</span>
                <span class="n">electable_nodes</span><span class="o">=</span><span class="mi">2</span><span class="p">,</span>
                <span class="n">priority</span><span class="o">=</span><span class="mi">6</span><span class="p">,</span>
                <span class="n">read_only_nodes</span><span class="o">=</span><span class="mi">0</span><span class="p">,</span>
                <span class="n">region_name</span><span class="o">=</span><span class="s2">&quot;US_EAST_2&quot;</span><span class="p">,</span>
            <span class="p">),</span>
            <span class="n">mongodbatlas</span><span class="o">.</span><span class="n">ClusterReplicationSpecRegionsConfigArgs</span><span class="p">(</span>
                <span class="n">electable_nodes</span><span class="o">=</span><span class="mi">2</span><span class="p">,</span>
                <span class="n">priority</span><span class="o">=</span><span class="mi">5</span><span class="p">,</span>
                <span class="n">read_only_nodes</span><span class="o">=</span><span class="mi">2</span><span class="p">,</span>
                <span class="n">region_name</span><span class="o">=</span><span class="s2">&quot;US_WEST_1&quot;</span><span class="p">,</span>
            <span class="p">),</span>
        <span class="p">],</span>
    <span class="p">)])</span>
</pre></div>
</div>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_mongodbatlas</span> <span class="k">as</span> <span class="nn">mongodbatlas</span>

<span class="n">cluster_test</span> <span class="o">=</span> <span class="n">mongodbatlas</span><span class="o">.</span><span class="n">Cluster</span><span class="p">(</span><span class="s2">&quot;cluster-test&quot;</span><span class="p">,</span>
    <span class="n">cluster_type</span><span class="o">=</span><span class="s2">&quot;GEOSHARDED&quot;</span><span class="p">,</span>
    <span class="n">disk_size_gb</span><span class="o">=</span><span class="mi">80</span><span class="p">,</span>
    <span class="n">num_shards</span><span class="o">=</span><span class="mi">1</span><span class="p">,</span>
    <span class="n">project_id</span><span class="o">=</span><span class="s2">&quot;&lt;YOUR-PROJECT-ID&gt;&quot;</span><span class="p">,</span>
    <span class="n">provider_backup_enabled</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="n">provider_disk_iops</span><span class="o">=</span><span class="mi">240</span><span class="p">,</span>
    <span class="n">provider_instance_size_name</span><span class="o">=</span><span class="s2">&quot;M30&quot;</span><span class="p">,</span>
    <span class="n">provider_name</span><span class="o">=</span><span class="s2">&quot;AWS&quot;</span><span class="p">,</span>
    <span class="n">provider_volume_type</span><span class="o">=</span><span class="s2">&quot;STANDARD&quot;</span><span class="p">,</span>
    <span class="n">replication_specs</span><span class="o">=</span><span class="p">[</span>
        <span class="n">mongodbatlas</span><span class="o">.</span><span class="n">ClusterReplicationSpecArgs</span><span class="p">(</span>
            <span class="n">num_shards</span><span class="o">=</span><span class="mi">2</span><span class="p">,</span>
            <span class="n">regions_configs</span><span class="o">=</span><span class="p">[</span><span class="n">mongodbatlas</span><span class="o">.</span><span class="n">ClusterReplicationSpecRegionsConfigArgs</span><span class="p">(</span>
                <span class="n">electable_nodes</span><span class="o">=</span><span class="mi">3</span><span class="p">,</span>
                <span class="n">priority</span><span class="o">=</span><span class="mi">7</span><span class="p">,</span>
                <span class="n">read_only_nodes</span><span class="o">=</span><span class="mi">0</span><span class="p">,</span>
                <span class="n">region_name</span><span class="o">=</span><span class="s2">&quot;US_EAST_1&quot;</span><span class="p">,</span>
            <span class="p">)],</span>
            <span class="n">zone_name</span><span class="o">=</span><span class="s2">&quot;Zone 1&quot;</span><span class="p">,</span>
        <span class="p">),</span>
        <span class="n">mongodbatlas</span><span class="o">.</span><span class="n">ClusterReplicationSpecArgs</span><span class="p">(</span>
            <span class="n">num_shards</span><span class="o">=</span><span class="mi">2</span><span class="p">,</span>
            <span class="n">regions_configs</span><span class="o">=</span><span class="p">[</span><span class="n">mongodbatlas</span><span class="o">.</span><span class="n">ClusterReplicationSpecRegionsConfigArgs</span><span class="p">(</span>
                <span class="n">electable_nodes</span><span class="o">=</span><span class="mi">3</span><span class="p">,</span>
                <span class="n">priority</span><span class="o">=</span><span class="mi">7</span><span class="p">,</span>
                <span class="n">read_only_nodes</span><span class="o">=</span><span class="mi">0</span><span class="p">,</span>
                <span class="n">region_name</span><span class="o">=</span><span class="s2">&quot;EU_CENTRAL_1&quot;</span><span class="p">,</span>
            <span class="p">)],</span>
            <span class="n">zone_name</span><span class="o">=</span><span class="s2">&quot;Zone 2&quot;</span><span class="p">,</span>
        <span class="p">),</span>
    <span class="p">])</span>
</pre></div>
</div>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_mongodbatlas</span> <span class="k">as</span> <span class="nn">mongodbatlas</span>

<span class="n">cluster_test</span> <span class="o">=</span> <span class="n">mongodbatlas</span><span class="o">.</span><span class="n">Cluster</span><span class="p">(</span><span class="s2">&quot;cluster-test&quot;</span><span class="p">,</span>
    <span class="n">auto_scaling_disk_gb_enabled</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span>
    <span class="n">backing_provider_name</span><span class="o">=</span><span class="s2">&quot;AWS&quot;</span><span class="p">,</span>
    <span class="n">disk_size_gb</span><span class="o">=</span><span class="mi">2</span><span class="p">,</span>
    <span class="n">mongo_db_major_version</span><span class="o">=</span><span class="s2">&quot;4.2&quot;</span><span class="p">,</span>
    <span class="n">project_id</span><span class="o">=</span><span class="s2">&quot;&lt;YOUR-PROJECT-ID&gt;&quot;</span><span class="p">,</span>
    <span class="n">provider_instance_size_name</span><span class="o">=</span><span class="s2">&quot;M2&quot;</span><span class="p">,</span>
    <span class="n">provider_name</span><span class="o">=</span><span class="s2">&quot;TENANT&quot;</span><span class="p">,</span>
    <span class="n">provider_region_name</span><span class="o">=</span><span class="s2">&quot;US_EAST_1&quot;</span><span class="p">)</span>
</pre></div>
</div>
<p>Clusters can be imported using project ID and cluster name, in the format <code class="docutils literal notranslate"><span class="pre">PROJECTID-CLUSTERNAME</span></code>, e.g.</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>   $ pulumi import mongodbatlas:index/cluster:Cluster my_cluster 1112222b3bf99403840e8934-Cluster0

See detailed information <span class="k">for</span> arguments and attributes<span class="se">\ </span><span class="sb">`</span>MongoDB API Clusters &lt;https://docs.atlas.mongodb.com/reference/api/clusters-create-one/&gt;<span class="sb">`</span>_
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>auto_scaling_compute_enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specifies whether cluster tier auto-scaling is enabled. The default is false.</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>- Set to `true` to enable cluster tier auto-scaling. If enabled, you must specify a value for `providerSettings.autoScaling.compute.maxInstanceSize`.
- Set to `false` to disable cluster tier auto-scaling.
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>auto_scaling_compute_scale_down_enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Set to <code class="docutils literal notranslate"><span class="pre">true</span></code> to enable the cluster tier to scale down. This option is only available if <code class="docutils literal notranslate"><span class="pre">autoScaling.compute.enabled</span></code> is <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>- If this option is enabled, you must specify a value for `providerSettings.autoScaling.compute.minInstanceSize`
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>auto_scaling_disk_gb_enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specifies whether disk auto-scaling is enabled. The default is true.</p>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>- Set to `true` to enable disk auto-scaling.
- Set to `false` to disable disk auto-scaling.
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>backing_provider_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Cloud service provider on which the server for a multi-tenant cluster is provisioned.</p></li>
<li><p><strong>bi_connector</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'ClusterBiConnectorArgs'</em><em>]</em><em>]</em>) – Specifies BI Connector for Atlas configuration on this cluster. BI Connector for Atlas is only available for M10+ clusters. See BI Connector below for more details.</p></li>
<li><p><strong>cluster_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the type of the cluster that you want to modify. You cannot convert a sharded cluster deployment to a replica set deployment.</p></li>
<li><p><strong>disk_size_gb</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Capacity, in gigabytes, of the host’s root volume. Increase this number to add capacity, up to a maximum possible value of 4096 (i.e., 4 TB). This value must be a positive integer.</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="o">*</span> <span class="n">The</span> <span class="n">minimum</span> <span class="n">disk</span> <span class="n">size</span> <span class="k">for</span> <span class="n">dedicated</span> <span class="n">clusters</span> <span class="ow">is</span> <span class="mi">10</span><span class="n">GB</span> <span class="k">for</span> <span class="n">AWS</span> <span class="ow">and</span> <span class="n">GCP</span><span class="o">.</span> <span class="n">If</span> <span class="n">you</span> <span class="n">specify</span> <span class="n">diskSizeGB</span> <span class="k">with</span> <span class="n">a</span> <span class="n">lower</span> <span class="n">disk</span> <span class="n">size</span><span class="p">,</span> <span class="n">Atlas</span> <span class="n">defaults</span> <span class="n">to</span> <span class="n">the</span> <span class="n">minimum</span> <span class="n">disk</span> <span class="n">size</span> <span class="n">value</span><span class="o">.</span>
<span class="o">*</span> <span class="n">Note</span><span class="p">:</span> <span class="n">The</span> <span class="n">maximum</span> <span class="n">value</span> <span class="k">for</span> <span class="n">disk</span> <span class="n">storage</span> <span class="n">cannot</span> <span class="n">exceed</span> <span class="mi">50</span> <span class="n">times</span> <span class="n">the</span> <span class="n">maximum</span> <span class="n">RAM</span> <span class="k">for</span> <span class="n">the</span> <span class="n">selected</span> <span class="n">cluster</span><span class="o">.</span> <span class="n">If</span> <span class="n">you</span> <span class="n">require</span> <span class="n">additional</span> <span class="n">storage</span> <span class="n">space</span> <span class="n">beyond</span> <span class="n">this</span> <span class="n">limitation</span><span class="p">,</span> <span class="n">consider</span> <span class="n">upgrading</span> <span class="n">your</span> <span class="n">cluster</span> <span class="n">to</span> <span class="n">a</span> <span class="n">higher</span> <span class="n">tier</span><span class="o">.</span>
<span class="o">*</span> <span class="n">Cannot</span> <span class="n">be</span> <span class="n">used</span> <span class="k">with</span> <span class="n">clusters</span> <span class="k">with</span> <span class="n">local</span> <span class="n">NVMe</span> <span class="n">SSDs</span>
<span class="o">*</span> <span class="n">Cannot</span> <span class="n">be</span> <span class="n">used</span> <span class="k">with</span> <span class="n">Azure</span> <span class="n">clusters</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>encryption_at_rest_provider</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Possible values are AWS, GCP, AZURE or NONE.  Only needed if you desire to manage the keys, see <a class="reference external" href="https://docs.atlas.mongodb.com/security-aws-kms/">Encryption at Rest using Customer Key Management</a> for complete documentation.  You must configure encryption at rest for the Atlas project before enabling it on any cluster in the project. For complete documentation on configuring Encryption at Rest, see Encryption at Rest using Customer Key Management. Requires M10 or greater. and for legacy backups, backup_enabled, to be false or omitted. <strong>Note: Atlas encrypts all cluster storage and snapshot volumes, securing all cluster data on disk: a concept known as encryption at rest, by default</strong>.</p></li>
<li><p><strong>mongo_db_major_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Version of the cluster to deploy. Atlas supports the following MongoDB versions for M10+ clusters: <code class="docutils literal notranslate"><span class="pre">3.6</span></code>, <code class="docutils literal notranslate"><span class="pre">4.0</span></code>, or <code class="docutils literal notranslate"><span class="pre">4.2</span></code>. You must set this value to <code class="docutils literal notranslate"><span class="pre">4.2</span></code> if <code class="docutils literal notranslate"><span class="pre">provider_instance_size_name</span></code> is either M2 or M5.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the cluster as it appears in Atlas. Once the cluster is created, its name cannot be changed.</p></li>
<li><p><strong>num_shards</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Number of shards to deploy in the specified zone, minimum 1.</p></li>
<li><p><strong>pit_enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – <ul>
<li><p>Flag that indicates if the cluster uses Continuous Cloud Backup. If set to true, provider_backup_enabled must also be set to true.</p></li>
</ul>
</p></li>
<li><p><strong>project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique ID for the project to create the database user.</p></li>
<li><p><strong>provider_auto_scaling_compute_max_instance_size</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Maximum instance size to which your cluster can automatically scale (e.g., M40). Required if <code class="docutils literal notranslate"><span class="pre">autoScaling.compute.enabled</span></code> is <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>provider_auto_scaling_compute_min_instance_size</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Minimum instance size to which your cluster can automatically scale (e.g., M10). Required if <code class="docutils literal notranslate"><span class="pre">autoScaling.compute.scaleDownEnabled</span></code> is <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>provider_backup_enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Flag indicating if the cluster uses Cloud Backup for backups.</p></li>
<li><p><strong>provider_disk_iops</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The maximum input/output operations per second (IOPS) the system can perform. The possible values depend on the selected <code class="docutils literal notranslate"><span class="pre">provider_instance_size_name</span></code> and <code class="docutils literal notranslate"><span class="pre">disk_size_gb</span></code>.</p></li>
<li><p><strong>provider_disk_type_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Azure disk type of the server’s root volume. If omitted, Atlas uses the default disk type for the selected providerSettings.instanceSizeName.  Example disk types and associated storage sizes: P4 - 32GB, P6 - 64GB, P10 - 128GB, P15 - 256GB, P20 - 512GB, P30 - 1024GB, P40 - 2048GB, P50 - 4095GB.  More information and the most update to date disk types/storage sizes can be located at <a class="reference external" href="https://docs.atlas.mongodb.com/reference/api/clusters-create-one/">https://docs.atlas.mongodb.com/reference/api/clusters-create-one/</a>.</p></li>
<li><p><strong>provider_encrypt_ebs_volume</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – The default value is true.  Flag that indicates whether the Amazon EBS encryption feature encrypts the host’s root volume for both data at rest within the volume and for data moving between the volume and the cluster. Note: This setting is always enabled for clusters with local NVMe SSDs. <strong>Atlas encrypts all cluster storage and snapshot volumes, securing all cluster data on disk: a concept known as encryption at rest, by default.</strong>.</p></li>
<li><p><strong>provider_instance_size_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Atlas provides different instance sizes, each with a default storage capacity and RAM size. The instance size you select is used for all the data-bearing servers in your cluster. See <a class="reference external" href="https://docs.atlas.mongodb.com/reference/api/clusters-create-one/">Create a Cluster</a> <code class="docutils literal notranslate"><span class="pre">providerSettings.instanceSizeName</span></code> for valid values and default resources. 
<strong>Note</strong> free tier (M0) creation is not supported by the Atlas API and hence not supported by this provider.)</p></li>
<li><p><strong>provider_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Cloud service provider on which the servers are provisioned.</p></li>
<li><p><strong>provider_region_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Physical location of your MongoDB cluster. The region you choose can affect network latency for clients accessing your databases.  Requires the <strong>Atlas region name</strong>, see the reference list for <a class="reference external" href="https://docs.atlas.mongodb.com/reference/amazon-aws/">AWS</a>, <a class="reference external" href="https://docs.atlas.mongodb.com/reference/google-gcp/">GCP</a>, <a class="reference external" href="https://docs.atlas.mongodb.com/reference/microsoft-azure/">Azure</a>.
Do not specify this field when creating a multi-region cluster using the replicationSpec document or a Global Cluster with the replicationSpecs array.</p></li>
<li><p><strong>provider_volume_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of the volume. The possible values are: <code class="docutils literal notranslate"><span class="pre">STANDARD</span></code> and <code class="docutils literal notranslate"><span class="pre">PROVISIONED</span></code>.  <code class="docutils literal notranslate"><span class="pre">PROVISIONED</span></code> required if setting IOPS higher than the default instance IOPS.</p></li>
<li><p><strong>replication_factor</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Number of replica set members. Each member keeps a copy of your databases, providing high availability and data redundancy. The possible values are 3, 5, or 7. The default value is 3.</p></li>
<li><p><strong>replication_specs</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'ClusterReplicationSpecArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – Configuration for cluster regions.  See Replication Spec below for more details.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_mongodbatlas.Cluster.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">advanced_configuration</span><span class="p">:</span> <span class="n">Union[ClusterAdvancedConfigurationArgs, Mapping[str, Any], Awaitable[Union[ClusterAdvancedConfigurationArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auto_scaling_compute_enabled</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auto_scaling_compute_scale_down_enabled</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auto_scaling_disk_gb_enabled</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">backing_provider_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">backup_enabled</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">bi_connector</span><span class="p">:</span> <span class="n">Union[ClusterBiConnectorArgs, Mapping[str, Any], Awaitable[Union[ClusterBiConnectorArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cluster_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cluster_type</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">connection_strings</span><span class="p">:</span> <span class="n">Union[ClusterConnectionStringsArgs, Mapping[str, Any], Awaitable[Union[ClusterConnectionStringsArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">container_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">disk_size_gb</span><span class="p">:</span> <span class="n">Union[float, Awaitable[float], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">encryption_at_rest_provider</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">labels</span><span class="p">:</span> <span class="n">Union[Sequence[Union[ClusterLabelArgs, Mapping[str, Any], Awaitable[Union[ClusterLabelArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[ClusterLabelArgs, Mapping[str, Any], Awaitable[Union[ClusterLabelArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">mongo_db_major_version</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">mongo_db_version</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">mongo_uri</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">mongo_uri_updated</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">mongo_uri_with_options</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">num_shards</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">paused</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">pit_enabled</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">provider_auto_scaling_compute_max_instance_size</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">provider_auto_scaling_compute_min_instance_size</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">provider_backup_enabled</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">provider_disk_iops</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">provider_disk_type_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">provider_encrypt_ebs_volume</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">provider_instance_size_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">provider_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">provider_region_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">provider_volume_type</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">replication_factor</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">replication_specs</span><span class="p">:</span> <span class="n">Union[Sequence[Union[ClusterReplicationSpecArgs, Mapping[str, Any], Awaitable[Union[ClusterReplicationSpecArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[ClusterReplicationSpecArgs, Mapping[str, Any], Awaitable[Union[ClusterReplicationSpecArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">snapshot_backup_policies</span><span class="p">:</span> <span class="n">Union[Sequence[Union[ClusterSnapshotBackupPolicyArgs, Mapping[str, Any], Awaitable[Union[ClusterSnapshotBackupPolicyArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[ClusterSnapshotBackupPolicyArgs, Mapping[str, Any], Awaitable[Union[ClusterSnapshotBackupPolicyArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">srv_address</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">state_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_mongodbatlas.cluster.Cluster<a class="headerlink" href="#pulumi_mongodbatlas.Cluster.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Cluster resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>auto_scaling_compute_enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specifies whether cluster tier auto-scaling is enabled. The default is false.</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>- Set to `true` to enable cluster tier auto-scaling. If enabled, you must specify a value for `providerSettings.autoScaling.compute.maxInstanceSize`.
- Set to `false` to disable cluster tier auto-scaling.
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>auto_scaling_compute_scale_down_enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Set to <code class="docutils literal notranslate"><span class="pre">true</span></code> to enable the cluster tier to scale down. This option is only available if <code class="docutils literal notranslate"><span class="pre">autoScaling.compute.enabled</span></code> is <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>- If this option is enabled, you must specify a value for `providerSettings.autoScaling.compute.minInstanceSize`
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>auto_scaling_disk_gb_enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specifies whether disk auto-scaling is enabled. The default is true.</p>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>- Set to `true` to enable disk auto-scaling.
- Set to `false` to disable disk auto-scaling.
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>backing_provider_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Cloud service provider on which the server for a multi-tenant cluster is provisioned.</p></li>
<li><p><strong>bi_connector</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'ClusterBiConnectorArgs'</em><em>]</em><em>]</em>) – Specifies BI Connector for Atlas configuration on this cluster. BI Connector for Atlas is only available for M10+ clusters. See BI Connector below for more details.</p></li>
<li><p><strong>cluster_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The cluster ID.</p></li>
<li><p><strong>cluster_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the type of the cluster that you want to modify. You cannot convert a sharded cluster deployment to a replica set deployment.</p></li>
<li><p><strong>connection_strings</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'ClusterConnectionStringsArgs'</em><em>]</em><em>]</em>) – Set of connection strings that your applications use to connect to this cluster. More info in <a class="reference external" href="https://docs.mongodb.com/manual/reference/connection-string/">Connection-strings</a>. Use the parameters in this object to connect your applications to this cluster. To learn more about the formats of connection strings, see <a class="reference external" href="https://docs.atlas.mongodb.com/reference/faq/connection-changes/">Connection String Options</a>. NOTE: Atlas returns the contents of this object after the cluster is operational, not while it builds the cluster.</p></li>
<li><p><strong>container_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Network Peering Container ID. The id of the container either created programmatically by the user before any clusters existed in the project or when the first cluster in the region (AWS/Azure) or project (GCP) was created.</p></li>
<li><p><strong>disk_size_gb</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Capacity, in gigabytes, of the host’s root volume. Increase this number to add capacity, up to a maximum possible value of 4096 (i.e., 4 TB). This value must be a positive integer.</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="o">*</span> <span class="n">The</span> <span class="n">minimum</span> <span class="n">disk</span> <span class="n">size</span> <span class="k">for</span> <span class="n">dedicated</span> <span class="n">clusters</span> <span class="ow">is</span> <span class="mi">10</span><span class="n">GB</span> <span class="k">for</span> <span class="n">AWS</span> <span class="ow">and</span> <span class="n">GCP</span><span class="o">.</span> <span class="n">If</span> <span class="n">you</span> <span class="n">specify</span> <span class="n">diskSizeGB</span> <span class="k">with</span> <span class="n">a</span> <span class="n">lower</span> <span class="n">disk</span> <span class="n">size</span><span class="p">,</span> <span class="n">Atlas</span> <span class="n">defaults</span> <span class="n">to</span> <span class="n">the</span> <span class="n">minimum</span> <span class="n">disk</span> <span class="n">size</span> <span class="n">value</span><span class="o">.</span>
<span class="o">*</span> <span class="n">Note</span><span class="p">:</span> <span class="n">The</span> <span class="n">maximum</span> <span class="n">value</span> <span class="k">for</span> <span class="n">disk</span> <span class="n">storage</span> <span class="n">cannot</span> <span class="n">exceed</span> <span class="mi">50</span> <span class="n">times</span> <span class="n">the</span> <span class="n">maximum</span> <span class="n">RAM</span> <span class="k">for</span> <span class="n">the</span> <span class="n">selected</span> <span class="n">cluster</span><span class="o">.</span> <span class="n">If</span> <span class="n">you</span> <span class="n">require</span> <span class="n">additional</span> <span class="n">storage</span> <span class="n">space</span> <span class="n">beyond</span> <span class="n">this</span> <span class="n">limitation</span><span class="p">,</span> <span class="n">consider</span> <span class="n">upgrading</span> <span class="n">your</span> <span class="n">cluster</span> <span class="n">to</span> <span class="n">a</span> <span class="n">higher</span> <span class="n">tier</span><span class="o">.</span>
<span class="o">*</span> <span class="n">Cannot</span> <span class="n">be</span> <span class="n">used</span> <span class="k">with</span> <span class="n">clusters</span> <span class="k">with</span> <span class="n">local</span> <span class="n">NVMe</span> <span class="n">SSDs</span>
<span class="o">*</span> <span class="n">Cannot</span> <span class="n">be</span> <span class="n">used</span> <span class="k">with</span> <span class="n">Azure</span> <span class="n">clusters</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>encryption_at_rest_provider</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>Possible values are AWS, GCP, AZURE or NONE.  Only needed if you desire to manage the keys, see <a class="reference external" href="https://docs.atlas.mongodb.com/security-aws-kms/">Encryption at Rest using Customer Key Management</a> for complete documentation.  You must configure encryption at rest for the Atlas project before enabling it on any cluster in the project. For complete documentation on configuring Encryption at Rest, see Encryption at Rest using Customer Key Management. Requires M10 or greater. and for legacy backups, backup_enabled, to be false or omitted. <strong>Note: Atlas encrypts all cluster storage and snapshot volumes, securing all cluster data on disk: a concept known as encryption at rest, by default</strong>.</p>
</p></li>
<li><p><strong>mongo_db_major_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Version of the cluster to deploy. Atlas supports the following MongoDB versions for M10+ clusters: <code class="docutils literal notranslate"><span class="pre">3.6</span></code>, <code class="docutils literal notranslate"><span class="pre">4.0</span></code>, or <code class="docutils literal notranslate"><span class="pre">4.2</span></code>. You must set this value to <code class="docutils literal notranslate"><span class="pre">4.2</span></code> if <code class="docutils literal notranslate"><span class="pre">provider_instance_size_name</span></code> is either M2 or M5.</p></li>
<li><p><strong>mongo_db_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Version of MongoDB the cluster runs, in <code class="docutils literal notranslate"><span class="pre">major-version</span></code>.<code class="docutils literal notranslate"><span class="pre">minor-version</span></code> format.</p></li>
<li><p><strong>mongo_uri</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Base connection string for the cluster. Atlas only displays this field after the cluster is operational, not while it builds the cluster.</p></li>
<li><p><strong>mongo_uri_updated</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Lists when the connection string was last updated. The connection string changes, for example, if you change a replica set to a sharded cluster.</p></li>
<li><p><strong>mongo_uri_with_options</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – connection string for connecting to the Atlas cluster. Includes the replicaSet, ssl, and authSource query parameters in the connection string with values appropriate for the cluster.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the cluster as it appears in Atlas. Once the cluster is created, its name cannot be changed.</p></li>
<li><p><strong>num_shards</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Number of shards to deploy in the specified zone, minimum 1.</p></li>
<li><p><strong>paused</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Flag that indicates whether the cluster is paused or not.</p></li>
<li><p><strong>pit_enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – <ul>
<li><p>Flag that indicates if the cluster uses Continuous Cloud Backup. If set to true, provider_backup_enabled must also be set to true.</p></li>
</ul>
</p></li>
<li><p><strong>project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique ID for the project to create the database user.</p></li>
<li><p><strong>provider_auto_scaling_compute_max_instance_size</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Maximum instance size to which your cluster can automatically scale (e.g., M40). Required if <code class="docutils literal notranslate"><span class="pre">autoScaling.compute.enabled</span></code> is <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>provider_auto_scaling_compute_min_instance_size</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Minimum instance size to which your cluster can automatically scale (e.g., M10). Required if <code class="docutils literal notranslate"><span class="pre">autoScaling.compute.scaleDownEnabled</span></code> is <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>provider_backup_enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Flag indicating if the cluster uses Cloud Backup for backups.</p></li>
<li><p><strong>provider_disk_iops</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The maximum input/output operations per second (IOPS) the system can perform. The possible values depend on the selected <code class="docutils literal notranslate"><span class="pre">provider_instance_size_name</span></code> and <code class="docutils literal notranslate"><span class="pre">disk_size_gb</span></code>.</p></li>
<li><p><strong>provider_disk_type_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Azure disk type of the server’s root volume. If omitted, Atlas uses the default disk type for the selected providerSettings.instanceSizeName.  Example disk types and associated storage sizes: P4 - 32GB, P6 - 64GB, P10 - 128GB, P15 - 256GB, P20 - 512GB, P30 - 1024GB, P40 - 2048GB, P50 - 4095GB.  More information and the most update to date disk types/storage sizes can be located at <a class="reference external" href="https://docs.atlas.mongodb.com/reference/api/clusters-create-one/">https://docs.atlas.mongodb.com/reference/api/clusters-create-one/</a>.</p></li>
<li><p><strong>provider_encrypt_ebs_volume</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – The default value is true.  Flag that indicates whether the Amazon EBS encryption feature encrypts the host’s root volume for both data at rest within the volume and for data moving between the volume and the cluster. Note: This setting is always enabled for clusters with local NVMe SSDs. <strong>Atlas encrypts all cluster storage and snapshot volumes, securing all cluster data on disk: a concept known as encryption at rest, by default.</strong>.</p></li>
<li><p><strong>provider_instance_size_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>Atlas provides different instance sizes, each with a default storage capacity and RAM size. The instance size you select is used for all the data-bearing servers in your cluster. See <a class="reference external" href="https://docs.atlas.mongodb.com/reference/api/clusters-create-one/">Create a Cluster</a> <code class="docutils literal notranslate"><span class="pre">providerSettings.instanceSizeName</span></code> for valid values and default resources. 
<strong>Note</strong> free tier (M0) creation is not supported by the Atlas API and hence not supported by this provider.)</p>
</p></li>
<li><p><strong>provider_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Cloud service provider on which the servers are provisioned.</p></li>
<li><p><strong>provider_region_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>Physical location of your MongoDB cluster. The region you choose can affect network latency for clients accessing your databases.  Requires the <strong>Atlas region name</strong>, see the reference list for <a class="reference external" href="https://docs.atlas.mongodb.com/reference/amazon-aws/">AWS</a>, <a class="reference external" href="https://docs.atlas.mongodb.com/reference/google-gcp/">GCP</a>, <a class="reference external" href="https://docs.atlas.mongodb.com/reference/microsoft-azure/">Azure</a>.
Do not specify this field when creating a multi-region cluster using the replicationSpec document or a Global Cluster with the replicationSpecs array.</p>
</p></li>
<li><p><strong>provider_volume_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of the volume. The possible values are: <code class="docutils literal notranslate"><span class="pre">STANDARD</span></code> and <code class="docutils literal notranslate"><span class="pre">PROVISIONED</span></code>.  <code class="docutils literal notranslate"><span class="pre">PROVISIONED</span></code> required if setting IOPS higher than the default instance IOPS.</p></li>
<li><p><strong>replication_factor</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Number of replica set members. Each member keeps a copy of your databases, providing high availability and data redundancy. The possible values are 3, 5, or 7. The default value is 3.</p></li>
<li><p><strong>replication_specs</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'ClusterReplicationSpecArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – Configuration for cluster regions.  See Replication Spec below for more details.</p></li>
<li><p><strong>snapshot_backup_policies</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'ClusterSnapshotBackupPolicyArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – current snapshot schedule and retention settings for the cluster.</p></li>
<li><p><strong>srv_address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Connection string for connecting to the Atlas cluster. The +srv modifier forces the connection to use TLS/SSL. See the mongoURI for additional options.</p></li>
<li><p><strong>state_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Current state of the cluster. The possible states are:</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="o">-</span> <span class="n">IDLE</span>
<span class="o">-</span> <span class="n">CREATING</span>
<span class="o">-</span> <span class="n">UPDATING</span>
<span class="o">-</span> <span class="n">DELETING</span>
<span class="o">-</span> <span class="n">DELETED</span>
<span class="o">-</span> <span class="n">REPAIRING</span>
</pre></div>
</div>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.Cluster.auto_scaling_compute_enabled">
<em class="property">property </em><code class="sig-name descname">auto_scaling_compute_enabled</code><a class="headerlink" href="#pulumi_mongodbatlas.Cluster.auto_scaling_compute_enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies whether cluster tier auto-scaling is enabled. The default is false.</p>
<ul class="simple">
<li><p>Set to <code class="docutils literal notranslate"><span class="pre">true</span></code> to enable cluster tier auto-scaling. If enabled, you must specify a value for <code class="docutils literal notranslate"><span class="pre">providerSettings.autoScaling.compute.maxInstanceSize</span></code>.</p></li>
<li><p>Set to <code class="docutils literal notranslate"><span class="pre">false</span></code> to disable cluster tier auto-scaling.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.Cluster.auto_scaling_compute_scale_down_enabled">
<em class="property">property </em><code class="sig-name descname">auto_scaling_compute_scale_down_enabled</code><a class="headerlink" href="#pulumi_mongodbatlas.Cluster.auto_scaling_compute_scale_down_enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Set to <code class="docutils literal notranslate"><span class="pre">true</span></code> to enable the cluster tier to scale down. This option is only available if <code class="docutils literal notranslate"><span class="pre">autoScaling.compute.enabled</span></code> is <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p>
<ul class="simple">
<li><p>If this option is enabled, you must specify a value for <code class="docutils literal notranslate"><span class="pre">providerSettings.autoScaling.compute.minInstanceSize</span></code></p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.Cluster.auto_scaling_disk_gb_enabled">
<em class="property">property </em><code class="sig-name descname">auto_scaling_disk_gb_enabled</code><a class="headerlink" href="#pulumi_mongodbatlas.Cluster.auto_scaling_disk_gb_enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies whether disk auto-scaling is enabled. The default is true.</p>
<ul class="simple">
<li><p>Set to <code class="docutils literal notranslate"><span class="pre">true</span></code> to enable disk auto-scaling.</p></li>
<li><p>Set to <code class="docutils literal notranslate"><span class="pre">false</span></code> to disable disk auto-scaling.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.Cluster.backing_provider_name">
<em class="property">property </em><code class="sig-name descname">backing_provider_name</code><a class="headerlink" href="#pulumi_mongodbatlas.Cluster.backing_provider_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Cloud service provider on which the server for a multi-tenant cluster is provisioned.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.Cluster.bi_connector">
<em class="property">property </em><code class="sig-name descname">bi_connector</code><a class="headerlink" href="#pulumi_mongodbatlas.Cluster.bi_connector" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies BI Connector for Atlas configuration on this cluster. BI Connector for Atlas is only available for M10+ clusters. See BI Connector below for more details.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.Cluster.cluster_id">
<em class="property">property </em><code class="sig-name descname">cluster_id</code><a class="headerlink" href="#pulumi_mongodbatlas.Cluster.cluster_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The cluster ID.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.Cluster.cluster_type">
<em class="property">property </em><code class="sig-name descname">cluster_type</code><a class="headerlink" href="#pulumi_mongodbatlas.Cluster.cluster_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the type of the cluster that you want to modify. You cannot convert a sharded cluster deployment to a replica set deployment.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.Cluster.connection_strings">
<em class="property">property </em><code class="sig-name descname">connection_strings</code><a class="headerlink" href="#pulumi_mongodbatlas.Cluster.connection_strings" title="Permalink to this definition">¶</a></dt>
<dd><p>Set of connection strings that your applications use to connect to this cluster. More info in <a class="reference external" href="https://docs.mongodb.com/manual/reference/connection-string/">Connection-strings</a>. Use the parameters in this object to connect your applications to this cluster. To learn more about the formats of connection strings, see <a class="reference external" href="https://docs.atlas.mongodb.com/reference/faq/connection-changes/">Connection String Options</a>. NOTE: Atlas returns the contents of this object after the cluster is operational, not while it builds the cluster.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.Cluster.container_id">
<em class="property">property </em><code class="sig-name descname">container_id</code><a class="headerlink" href="#pulumi_mongodbatlas.Cluster.container_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The Network Peering Container ID. The id of the container either created programmatically by the user before any clusters existed in the project or when the first cluster in the region (AWS/Azure) or project (GCP) was created.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.Cluster.disk_size_gb">
<em class="property">property </em><code class="sig-name descname">disk_size_gb</code><a class="headerlink" href="#pulumi_mongodbatlas.Cluster.disk_size_gb" title="Permalink to this definition">¶</a></dt>
<dd><p>Capacity, in gigabytes, of the host’s root volume. Increase this number to add capacity, up to a maximum possible value of 4096 (i.e., 4 TB). This value must be a positive integer.</p>
<ul class="simple">
<li><p>The minimum disk size for dedicated clusters is 10GB for AWS and GCP. If you specify diskSizeGB with a lower disk size, Atlas defaults to the minimum disk size value.</p></li>
<li><p>Note: The maximum value for disk storage cannot exceed 50 times the maximum RAM for the selected cluster. If you require additional storage space beyond this limitation, consider upgrading your cluster to a higher tier.</p></li>
<li><p>Cannot be used with clusters with local NVMe SSDs</p></li>
<li><p>Cannot be used with Azure clusters</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.Cluster.encryption_at_rest_provider">
<em class="property">property </em><code class="sig-name descname">encryption_at_rest_provider</code><a class="headerlink" href="#pulumi_mongodbatlas.Cluster.encryption_at_rest_provider" title="Permalink to this definition">¶</a></dt>
<dd><p>Possible values are AWS, GCP, AZURE or NONE.  Only needed if you desire to manage the keys, see <a class="reference external" href="https://docs.atlas.mongodb.com/security-aws-kms/">Encryption at Rest using Customer Key Management</a> for complete documentation.  You must configure encryption at rest for the Atlas project before enabling it on any cluster in the project. For complete documentation on configuring Encryption at Rest, see Encryption at Rest using Customer Key Management. Requires M10 or greater. and for legacy backups, backup_enabled, to be false or omitted. <strong>Note: Atlas encrypts all cluster storage and snapshot volumes, securing all cluster data on disk: a concept known as encryption at rest, by default</strong>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.Cluster.mongo_db_major_version">
<em class="property">property </em><code class="sig-name descname">mongo_db_major_version</code><a class="headerlink" href="#pulumi_mongodbatlas.Cluster.mongo_db_major_version" title="Permalink to this definition">¶</a></dt>
<dd><p>Version of the cluster to deploy. Atlas supports the following MongoDB versions for M10+ clusters: <code class="docutils literal notranslate"><span class="pre">3.6</span></code>, <code class="docutils literal notranslate"><span class="pre">4.0</span></code>, or <code class="docutils literal notranslate"><span class="pre">4.2</span></code>. You must set this value to <code class="docutils literal notranslate"><span class="pre">4.2</span></code> if <code class="docutils literal notranslate"><span class="pre">provider_instance_size_name</span></code> is either M2 or M5.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.Cluster.mongo_db_version">
<em class="property">property </em><code class="sig-name descname">mongo_db_version</code><a class="headerlink" href="#pulumi_mongodbatlas.Cluster.mongo_db_version" title="Permalink to this definition">¶</a></dt>
<dd><p>Version of MongoDB the cluster runs, in <code class="docutils literal notranslate"><span class="pre">major-version</span></code>.<code class="docutils literal notranslate"><span class="pre">minor-version</span></code> format.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.Cluster.mongo_uri">
<em class="property">property </em><code class="sig-name descname">mongo_uri</code><a class="headerlink" href="#pulumi_mongodbatlas.Cluster.mongo_uri" title="Permalink to this definition">¶</a></dt>
<dd><p>Base connection string for the cluster. Atlas only displays this field after the cluster is operational, not while it builds the cluster.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.Cluster.mongo_uri_updated">
<em class="property">property </em><code class="sig-name descname">mongo_uri_updated</code><a class="headerlink" href="#pulumi_mongodbatlas.Cluster.mongo_uri_updated" title="Permalink to this definition">¶</a></dt>
<dd><p>Lists when the connection string was last updated. The connection string changes, for example, if you change a replica set to a sharded cluster.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.Cluster.mongo_uri_with_options">
<em class="property">property </em><code class="sig-name descname">mongo_uri_with_options</code><a class="headerlink" href="#pulumi_mongodbatlas.Cluster.mongo_uri_with_options" title="Permalink to this definition">¶</a></dt>
<dd><p>connection string for connecting to the Atlas cluster. Includes the replicaSet, ssl, and authSource query parameters in the connection string with values appropriate for the cluster.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.Cluster.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_mongodbatlas.Cluster.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the cluster as it appears in Atlas. Once the cluster is created, its name cannot be changed.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.Cluster.num_shards">
<em class="property">property </em><code class="sig-name descname">num_shards</code><a class="headerlink" href="#pulumi_mongodbatlas.Cluster.num_shards" title="Permalink to this definition">¶</a></dt>
<dd><p>Number of shards to deploy in the specified zone, minimum 1.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.Cluster.paused">
<em class="property">property </em><code class="sig-name descname">paused</code><a class="headerlink" href="#pulumi_mongodbatlas.Cluster.paused" title="Permalink to this definition">¶</a></dt>
<dd><p>Flag that indicates whether the cluster is paused or not.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.Cluster.pit_enabled">
<em class="property">property </em><code class="sig-name descname">pit_enabled</code><a class="headerlink" href="#pulumi_mongodbatlas.Cluster.pit_enabled" title="Permalink to this definition">¶</a></dt>
<dd><ul class="simple">
<li><p>Flag that indicates if the cluster uses Continuous Cloud Backup. If set to true, provider_backup_enabled must also be set to true.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.Cluster.project_id">
<em class="property">property </em><code class="sig-name descname">project_id</code><a class="headerlink" href="#pulumi_mongodbatlas.Cluster.project_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The unique ID for the project to create the database user.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.Cluster.provider_auto_scaling_compute_max_instance_size">
<em class="property">property </em><code class="sig-name descname">provider_auto_scaling_compute_max_instance_size</code><a class="headerlink" href="#pulumi_mongodbatlas.Cluster.provider_auto_scaling_compute_max_instance_size" title="Permalink to this definition">¶</a></dt>
<dd><p>Maximum instance size to which your cluster can automatically scale (e.g., M40). Required if <code class="docutils literal notranslate"><span class="pre">autoScaling.compute.enabled</span></code> is <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.Cluster.provider_auto_scaling_compute_min_instance_size">
<em class="property">property </em><code class="sig-name descname">provider_auto_scaling_compute_min_instance_size</code><a class="headerlink" href="#pulumi_mongodbatlas.Cluster.provider_auto_scaling_compute_min_instance_size" title="Permalink to this definition">¶</a></dt>
<dd><p>Minimum instance size to which your cluster can automatically scale (e.g., M10). Required if <code class="docutils literal notranslate"><span class="pre">autoScaling.compute.scaleDownEnabled</span></code> is <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.Cluster.provider_backup_enabled">
<em class="property">property </em><code class="sig-name descname">provider_backup_enabled</code><a class="headerlink" href="#pulumi_mongodbatlas.Cluster.provider_backup_enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Flag indicating if the cluster uses Cloud Backup for backups.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.Cluster.provider_disk_iops">
<em class="property">property </em><code class="sig-name descname">provider_disk_iops</code><a class="headerlink" href="#pulumi_mongodbatlas.Cluster.provider_disk_iops" title="Permalink to this definition">¶</a></dt>
<dd><p>The maximum input/output operations per second (IOPS) the system can perform. The possible values depend on the selected <code class="docutils literal notranslate"><span class="pre">provider_instance_size_name</span></code> and <code class="docutils literal notranslate"><span class="pre">disk_size_gb</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.Cluster.provider_disk_type_name">
<em class="property">property </em><code class="sig-name descname">provider_disk_type_name</code><a class="headerlink" href="#pulumi_mongodbatlas.Cluster.provider_disk_type_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Azure disk type of the server’s root volume. If omitted, Atlas uses the default disk type for the selected providerSettings.instanceSizeName.  Example disk types and associated storage sizes: P4 - 32GB, P6 - 64GB, P10 - 128GB, P15 - 256GB, P20 - 512GB, P30 - 1024GB, P40 - 2048GB, P50 - 4095GB.  More information and the most update to date disk types/storage sizes can be located at <a class="reference external" href="https://docs.atlas.mongodb.com/reference/api/clusters-create-one/">https://docs.atlas.mongodb.com/reference/api/clusters-create-one/</a>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.Cluster.provider_encrypt_ebs_volume">
<em class="property">property </em><code class="sig-name descname">provider_encrypt_ebs_volume</code><a class="headerlink" href="#pulumi_mongodbatlas.Cluster.provider_encrypt_ebs_volume" title="Permalink to this definition">¶</a></dt>
<dd><p>The default value is true.  Flag that indicates whether the Amazon EBS encryption feature encrypts the host’s root volume for both data at rest within the volume and for data moving between the volume and the cluster. Note: This setting is always enabled for clusters with local NVMe SSDs. <strong>Atlas encrypts all cluster storage and snapshot volumes, securing all cluster data on disk: a concept known as encryption at rest, by default.</strong>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.Cluster.provider_instance_size_name">
<em class="property">property </em><code class="sig-name descname">provider_instance_size_name</code><a class="headerlink" href="#pulumi_mongodbatlas.Cluster.provider_instance_size_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Atlas provides different instance sizes, each with a default storage capacity and RAM size. The instance size you select is used for all the data-bearing servers in your cluster. See <a class="reference external" href="https://docs.atlas.mongodb.com/reference/api/clusters-create-one/">Create a Cluster</a> <code class="docutils literal notranslate"><span class="pre">providerSettings.instanceSizeName</span></code> for valid values and default resources. 
<strong>Note</strong> free tier (M0) creation is not supported by the Atlas API and hence not supported by this provider.)</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.Cluster.provider_name">
<em class="property">property </em><code class="sig-name descname">provider_name</code><a class="headerlink" href="#pulumi_mongodbatlas.Cluster.provider_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Cloud service provider on which the servers are provisioned.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.Cluster.provider_region_name">
<em class="property">property </em><code class="sig-name descname">provider_region_name</code><a class="headerlink" href="#pulumi_mongodbatlas.Cluster.provider_region_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Physical location of your MongoDB cluster. The region you choose can affect network latency for clients accessing your databases.  Requires the <strong>Atlas region name</strong>, see the reference list for <a class="reference external" href="https://docs.atlas.mongodb.com/reference/amazon-aws/">AWS</a>, <a class="reference external" href="https://docs.atlas.mongodb.com/reference/google-gcp/">GCP</a>, <a class="reference external" href="https://docs.atlas.mongodb.com/reference/microsoft-azure/">Azure</a>.
Do not specify this field when creating a multi-region cluster using the replicationSpec document or a Global Cluster with the replicationSpecs array.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.Cluster.provider_volume_type">
<em class="property">property </em><code class="sig-name descname">provider_volume_type</code><a class="headerlink" href="#pulumi_mongodbatlas.Cluster.provider_volume_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of the volume. The possible values are: <code class="docutils literal notranslate"><span class="pre">STANDARD</span></code> and <code class="docutils literal notranslate"><span class="pre">PROVISIONED</span></code>.  <code class="docutils literal notranslate"><span class="pre">PROVISIONED</span></code> required if setting IOPS higher than the default instance IOPS.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.Cluster.replication_factor">
<em class="property">property </em><code class="sig-name descname">replication_factor</code><a class="headerlink" href="#pulumi_mongodbatlas.Cluster.replication_factor" title="Permalink to this definition">¶</a></dt>
<dd><p>Number of replica set members. Each member keeps a copy of your databases, providing high availability and data redundancy. The possible values are 3, 5, or 7. The default value is 3.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.Cluster.replication_specs">
<em class="property">property </em><code class="sig-name descname">replication_specs</code><a class="headerlink" href="#pulumi_mongodbatlas.Cluster.replication_specs" title="Permalink to this definition">¶</a></dt>
<dd><p>Configuration for cluster regions.  See Replication Spec below for more details.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.Cluster.snapshot_backup_policies">
<em class="property">property </em><code class="sig-name descname">snapshot_backup_policies</code><a class="headerlink" href="#pulumi_mongodbatlas.Cluster.snapshot_backup_policies" title="Permalink to this definition">¶</a></dt>
<dd><p>current snapshot schedule and retention settings for the cluster.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.Cluster.srv_address">
<em class="property">property </em><code class="sig-name descname">srv_address</code><a class="headerlink" href="#pulumi_mongodbatlas.Cluster.srv_address" title="Permalink to this definition">¶</a></dt>
<dd><p>Connection string for connecting to the Atlas cluster. The +srv modifier forces the connection to use TLS/SSL. See the mongoURI for additional options.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.Cluster.state_name">
<em class="property">property </em><code class="sig-name descname">state_name</code><a class="headerlink" href="#pulumi_mongodbatlas.Cluster.state_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Current state of the cluster. The possible states are:</p>
<ul class="simple">
<li><p>IDLE</p></li>
<li><p>CREATING</p></li>
<li><p>UPDATING</p></li>
<li><p>DELETING</p></li>
<li><p>DELETED</p></li>
<li><p>REPAIRING</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.Cluster.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.Cluster.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_mongodbatlas.Cluster.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.Cluster.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py class">
<dt id="pulumi_mongodbatlas.CustomDbRole">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">CustomDbRole</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">actions</span><span class="p">:</span> <span class="n">Union[Sequence[Union[CustomDbRoleActionArgs, Mapping[str, Any], Awaitable[Union[CustomDbRoleActionArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[CustomDbRoleActionArgs, Mapping[str, Any], Awaitable[Union[CustomDbRoleActionArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">inherited_roles</span><span class="p">:</span> <span class="n">Union[Sequence[Union[CustomDbRoleInheritedRoleArgs, Mapping[str, Any], Awaitable[Union[CustomDbRoleInheritedRoleArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[CustomDbRoleInheritedRoleArgs, Mapping[str, Any], Awaitable[Union[CustomDbRoleInheritedRoleArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">role_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.CustomDbRole" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">CustomDbRole</span></code> provides a Custom DB Role resource. The customDBRoles resource lets you retrieve, create and modify the custom MongoDB roles in your cluster. Use custom MongoDB roles to specify custom sets of actions which cannot be described by the built-in Atlas database user privileges.</p>
<blockquote>
<div><p><strong>IMPORTANT</strong> Custom roles cannot use actions unavailable to any cluster version in your project. Custom roles are defined at the project level, and must be compatible with each MongoDB version used by your project’s clusters. If you have a cluster in your project with MongoDB 3.4, you cannot create a custom role that uses actions introduced in MongoDB 3.6, such as useUUID.</p>
<p><strong>NOTE:</strong> Groups and projects are synonymous terms. You may find group_id in the official documentation.</p>
</div></blockquote>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_mongodbatlas</span> <span class="k">as</span> <span class="nn">mongodbatlas</span>

<span class="n">test_role</span> <span class="o">=</span> <span class="n">mongodbatlas</span><span class="o">.</span><span class="n">CustomDbRole</span><span class="p">(</span><span class="s2">&quot;testRole&quot;</span><span class="p">,</span>
    <span class="n">actions</span><span class="o">=</span><span class="p">[</span>
        <span class="n">mongodbatlas</span><span class="o">.</span><span class="n">CustomDbRoleActionArgs</span><span class="p">(</span>
            <span class="n">action</span><span class="o">=</span><span class="s2">&quot;UPDATE&quot;</span><span class="p">,</span>
            <span class="n">resources</span><span class="o">=</span><span class="p">[</span><span class="n">mongodbatlas</span><span class="o">.</span><span class="n">CustomDbRoleActionResourceArgs</span><span class="p">(</span>
                <span class="n">collection_name</span><span class="o">=</span><span class="s2">&quot;&quot;</span><span class="p">,</span>
                <span class="n">database_name</span><span class="o">=</span><span class="s2">&quot;anyDatabase&quot;</span><span class="p">,</span>
            <span class="p">)],</span>
        <span class="p">),</span>
        <span class="n">mongodbatlas</span><span class="o">.</span><span class="n">CustomDbRoleActionArgs</span><span class="p">(</span>
            <span class="n">action</span><span class="o">=</span><span class="s2">&quot;INSERT&quot;</span><span class="p">,</span>
            <span class="n">resources</span><span class="o">=</span><span class="p">[</span><span class="n">mongodbatlas</span><span class="o">.</span><span class="n">CustomDbRoleActionResourceArgs</span><span class="p">(</span>
                <span class="n">collection_name</span><span class="o">=</span><span class="s2">&quot;&quot;</span><span class="p">,</span>
                <span class="n">database_name</span><span class="o">=</span><span class="s2">&quot;anyDatabase&quot;</span><span class="p">,</span>
            <span class="p">)],</span>
        <span class="p">),</span>
        <span class="n">mongodbatlas</span><span class="o">.</span><span class="n">CustomDbRoleActionArgs</span><span class="p">(</span>
            <span class="n">action</span><span class="o">=</span><span class="s2">&quot;REMOVE&quot;</span><span class="p">,</span>
            <span class="n">resources</span><span class="o">=</span><span class="p">[</span><span class="n">mongodbatlas</span><span class="o">.</span><span class="n">CustomDbRoleActionResourceArgs</span><span class="p">(</span>
                <span class="n">collection_name</span><span class="o">=</span><span class="s2">&quot;&quot;</span><span class="p">,</span>
                <span class="n">database_name</span><span class="o">=</span><span class="s2">&quot;anyDatabase&quot;</span><span class="p">,</span>
            <span class="p">)],</span>
        <span class="p">),</span>
    <span class="p">],</span>
    <span class="n">project_id</span><span class="o">=</span><span class="s2">&quot;&lt;PROJECT-ID&gt;&quot;</span><span class="p">,</span>
    <span class="n">role_name</span><span class="o">=</span><span class="s2">&quot;myCustomRole&quot;</span><span class="p">)</span>
</pre></div>
</div>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_mongodbatlas</span> <span class="k">as</span> <span class="nn">mongodbatlas</span>

<span class="n">inherited_role_one</span> <span class="o">=</span> <span class="n">mongodbatlas</span><span class="o">.</span><span class="n">CustomDbRole</span><span class="p">(</span><span class="s2">&quot;inheritedRoleOne&quot;</span><span class="p">,</span>
    <span class="n">actions</span><span class="o">=</span><span class="p">[</span><span class="n">mongodbatlas</span><span class="o">.</span><span class="n">CustomDbRoleActionArgs</span><span class="p">(</span>
        <span class="n">action</span><span class="o">=</span><span class="s2">&quot;INSERT&quot;</span><span class="p">,</span>
        <span class="n">resources</span><span class="o">=</span><span class="p">[</span><span class="n">mongodbatlas</span><span class="o">.</span><span class="n">CustomDbRoleActionResourceArgs</span><span class="p">(</span>
            <span class="n">collection_name</span><span class="o">=</span><span class="s2">&quot;&quot;</span><span class="p">,</span>
            <span class="n">database_name</span><span class="o">=</span><span class="s2">&quot;anyDatabase&quot;</span><span class="p">,</span>
        <span class="p">)],</span>
    <span class="p">)],</span>
    <span class="n">project_id</span><span class="o">=</span><span class="s2">&quot;&lt;PROJECT-ID&gt;&quot;</span><span class="p">,</span>
    <span class="n">role_name</span><span class="o">=</span><span class="s2">&quot;insertRole&quot;</span><span class="p">)</span>
<span class="n">inherited_role_two</span> <span class="o">=</span> <span class="n">mongodbatlas</span><span class="o">.</span><span class="n">CustomDbRole</span><span class="p">(</span><span class="s2">&quot;inheritedRoleTwo&quot;</span><span class="p">,</span>
    <span class="n">actions</span><span class="o">=</span><span class="p">[</span><span class="n">mongodbatlas</span><span class="o">.</span><span class="n">CustomDbRoleActionArgs</span><span class="p">(</span>
        <span class="n">action</span><span class="o">=</span><span class="s2">&quot;SERVER_STATUS&quot;</span><span class="p">,</span>
        <span class="n">resources</span><span class="o">=</span><span class="p">[</span><span class="n">mongodbatlas</span><span class="o">.</span><span class="n">CustomDbRoleActionResourceArgs</span><span class="p">(</span>
            <span class="n">cluster</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
        <span class="p">)],</span>
    <span class="p">)],</span>
    <span class="n">project_id</span><span class="o">=</span><span class="n">inherited_role_one</span><span class="o">.</span><span class="n">project_id</span><span class="p">,</span>
    <span class="n">role_name</span><span class="o">=</span><span class="s2">&quot;statusServerRole&quot;</span><span class="p">)</span>
<span class="n">test_role</span> <span class="o">=</span> <span class="n">mongodbatlas</span><span class="o">.</span><span class="n">CustomDbRole</span><span class="p">(</span><span class="s2">&quot;testRole&quot;</span><span class="p">,</span>
    <span class="n">actions</span><span class="o">=</span><span class="p">[</span>
        <span class="n">mongodbatlas</span><span class="o">.</span><span class="n">CustomDbRoleActionArgs</span><span class="p">(</span>
            <span class="n">action</span><span class="o">=</span><span class="s2">&quot;UPDATE&quot;</span><span class="p">,</span>
            <span class="n">resources</span><span class="o">=</span><span class="p">[</span><span class="n">mongodbatlas</span><span class="o">.</span><span class="n">CustomDbRoleActionResourceArgs</span><span class="p">(</span>
                <span class="n">collection_name</span><span class="o">=</span><span class="s2">&quot;&quot;</span><span class="p">,</span>
                <span class="n">database_name</span><span class="o">=</span><span class="s2">&quot;anyDatabase&quot;</span><span class="p">,</span>
            <span class="p">)],</span>
        <span class="p">),</span>
        <span class="n">mongodbatlas</span><span class="o">.</span><span class="n">CustomDbRoleActionArgs</span><span class="p">(</span>
            <span class="n">action</span><span class="o">=</span><span class="s2">&quot;REMOVE&quot;</span><span class="p">,</span>
            <span class="n">resources</span><span class="o">=</span><span class="p">[</span><span class="n">mongodbatlas</span><span class="o">.</span><span class="n">CustomDbRoleActionResourceArgs</span><span class="p">(</span>
                <span class="n">collection_name</span><span class="o">=</span><span class="s2">&quot;&quot;</span><span class="p">,</span>
                <span class="n">database_name</span><span class="o">=</span><span class="s2">&quot;anyDatabase&quot;</span><span class="p">,</span>
            <span class="p">)],</span>
        <span class="p">),</span>
    <span class="p">],</span>
    <span class="n">inherited_roles</span><span class="o">=</span><span class="p">[</span>
        <span class="n">mongodbatlas</span><span class="o">.</span><span class="n">CustomDbRoleInheritedRoleArgs</span><span class="p">(</span>
            <span class="n">database_name</span><span class="o">=</span><span class="s2">&quot;admin&quot;</span><span class="p">,</span>
            <span class="n">role_name</span><span class="o">=</span><span class="n">inherited_role_one</span><span class="o">.</span><span class="n">role_name</span><span class="p">,</span>
        <span class="p">),</span>
        <span class="n">mongodbatlas</span><span class="o">.</span><span class="n">CustomDbRoleInheritedRoleArgs</span><span class="p">(</span>
            <span class="n">database_name</span><span class="o">=</span><span class="s2">&quot;admin&quot;</span><span class="p">,</span>
            <span class="n">role_name</span><span class="o">=</span><span class="n">inherited_role_two</span><span class="o">.</span><span class="n">role_name</span><span class="p">,</span>
        <span class="p">),</span>
    <span class="p">],</span>
    <span class="n">project_id</span><span class="o">=</span><span class="n">inherited_role_one</span><span class="o">.</span><span class="n">project_id</span><span class="p">,</span>
    <span class="n">role_name</span><span class="o">=</span><span class="s2">&quot;myCustomRole&quot;</span><span class="p">)</span>
</pre></div>
</div>
<p>Database users can be imported using project ID and username, in the format <code class="docutils literal notranslate"><span class="pre">PROJECTID-ROLENAME</span></code>, e.g.</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>   $ pulumi import mongodbatlas:index/customDbRole:CustomDbRole my_role 1112222b3bf99403840e8934-MyCustomRole

For more information see<span class="se">\ </span><span class="sb">`</span>MongoDB Atlas API Reference. &lt;https://docs.atlas.mongodb.com/reference/api/custom-roles/&gt;<span class="sb">`</span>_
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique ID for the project to create the database user.</p></li>
<li><p><strong>role_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the inherited role. This can either be another custom role or a built-in role.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_mongodbatlas.CustomDbRole.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">actions</span><span class="p">:</span> <span class="n">Union[Sequence[Union[CustomDbRoleActionArgs, Mapping[str, Any], Awaitable[Union[CustomDbRoleActionArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[CustomDbRoleActionArgs, Mapping[str, Any], Awaitable[Union[CustomDbRoleActionArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">inherited_roles</span><span class="p">:</span> <span class="n">Union[Sequence[Union[CustomDbRoleInheritedRoleArgs, Mapping[str, Any], Awaitable[Union[CustomDbRoleInheritedRoleArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[CustomDbRoleInheritedRoleArgs, Mapping[str, Any], Awaitable[Union[CustomDbRoleInheritedRoleArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">role_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_mongodbatlas.custom_db_role.CustomDbRole<a class="headerlink" href="#pulumi_mongodbatlas.CustomDbRole.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing CustomDbRole resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique ID for the project to create the database user.</p></li>
<li><p><strong>role_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the inherited role. This can either be another custom role or a built-in role.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.CustomDbRole.project_id">
<em class="property">property </em><code class="sig-name descname">project_id</code><a class="headerlink" href="#pulumi_mongodbatlas.CustomDbRole.project_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The unique ID for the project to create the database user.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.CustomDbRole.role_name">
<em class="property">property </em><code class="sig-name descname">role_name</code><a class="headerlink" href="#pulumi_mongodbatlas.CustomDbRole.role_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the inherited role. This can either be another custom role or a built-in role.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.CustomDbRole.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.CustomDbRole.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_mongodbatlas.CustomDbRole.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.CustomDbRole.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py class">
<dt id="pulumi_mongodbatlas.DatabaseUser">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">DatabaseUser</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auth_database_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">aws_iam_type</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">database_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">labels</span><span class="p">:</span> <span class="n">Union[Sequence[Union[DatabaseUserLabelArgs, Mapping[str, Any], Awaitable[Union[DatabaseUserLabelArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[DatabaseUserLabelArgs, Mapping[str, Any], Awaitable[Union[DatabaseUserLabelArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">password</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">roles</span><span class="p">:</span> <span class="n">Union[Sequence[Union[DatabaseUserRoleArgs, Mapping[str, Any], Awaitable[Union[DatabaseUserRoleArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[DatabaseUserRoleArgs, Mapping[str, Any], Awaitable[Union[DatabaseUserRoleArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">scopes</span><span class="p">:</span> <span class="n">Union[Sequence[Union[DatabaseUserScopeArgs, Mapping[str, Any], Awaitable[Union[DatabaseUserScopeArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[DatabaseUserScopeArgs, Mapping[str, Any], Awaitable[Union[DatabaseUserScopeArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">username</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">x509_type</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.DatabaseUser" title="Permalink to this definition">¶</a></dt>
<dd><p>Database users can be imported using project ID and username, in the format <code class="docutils literal notranslate"><span class="pre">project_id</span></code>-<code class="docutils literal notranslate"><span class="pre">username</span></code>-<code class="docutils literal notranslate"><span class="pre">auth_database_name</span></code>, e.g.</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>$ pulumi import mongodbatlas:index/databaseUser:DatabaseUser my_user 1112222b3bf99403840e8934-my_user-admin
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>auth_database_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Database against which Atlas authenticates the user. A user must provide both a username and authentication database to log into MongoDB.
Accepted values include:</p></li>
<li><p><strong>aws_iam_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – If this value is set, the new database user authenticates with AWS IAM credentials. If no value is given, Atlas uses the default value of NONE. The accepted types are:</p></li>
<li><p><strong>database_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Database on which the user has the specified role. A role on the <code class="docutils literal notranslate"><span class="pre">admin</span></code> database can include privileges that apply to the other databases.</p></li>
<li><p><strong>project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique ID for the project to create the database user.</p></li>
<li><p><strong>roles</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'DatabaseUserRoleArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – List of user’s roles and the databases / collections on which the roles apply. A role allows the user to perform particular actions on the specified database. A role on the admin database can include privileges that apply to the other databases as well. See Roles below for more details.</p></li>
<li><p><strong>username</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Username for authenticating to MongoDB.</p></li>
<li><p><strong>x509_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – X.509 method by which the provided username is authenticated. If no value is given, Atlas uses the default value of NONE. The accepted types are:</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_mongodbatlas.DatabaseUser.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auth_database_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">aws_iam_type</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">database_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">labels</span><span class="p">:</span> <span class="n">Union[Sequence[Union[DatabaseUserLabelArgs, Mapping[str, Any], Awaitable[Union[DatabaseUserLabelArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[DatabaseUserLabelArgs, Mapping[str, Any], Awaitable[Union[DatabaseUserLabelArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">password</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">roles</span><span class="p">:</span> <span class="n">Union[Sequence[Union[DatabaseUserRoleArgs, Mapping[str, Any], Awaitable[Union[DatabaseUserRoleArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[DatabaseUserRoleArgs, Mapping[str, Any], Awaitable[Union[DatabaseUserRoleArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">scopes</span><span class="p">:</span> <span class="n">Union[Sequence[Union[DatabaseUserScopeArgs, Mapping[str, Any], Awaitable[Union[DatabaseUserScopeArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[DatabaseUserScopeArgs, Mapping[str, Any], Awaitable[Union[DatabaseUserScopeArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">username</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">x509_type</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_mongodbatlas.database_user.DatabaseUser<a class="headerlink" href="#pulumi_mongodbatlas.DatabaseUser.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing DatabaseUser resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>auth_database_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Database against which Atlas authenticates the user. A user must provide both a username and authentication database to log into MongoDB.
Accepted values include:</p></li>
<li><p><strong>aws_iam_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – If this value is set, the new database user authenticates with AWS IAM credentials. If no value is given, Atlas uses the default value of NONE. The accepted types are:</p></li>
<li><p><strong>database_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Database on which the user has the specified role. A role on the <code class="docutils literal notranslate"><span class="pre">admin</span></code> database can include privileges that apply to the other databases.</p></li>
<li><p><strong>project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique ID for the project to create the database user.</p></li>
<li><p><strong>roles</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'DatabaseUserRoleArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – List of user’s roles and the databases / collections on which the roles apply. A role allows the user to perform particular actions on the specified database. A role on the admin database can include privileges that apply to the other databases as well. See Roles below for more details.</p></li>
<li><p><strong>username</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Username for authenticating to MongoDB.</p></li>
<li><p><strong>x509_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – X.509 method by which the provided username is authenticated. If no value is given, Atlas uses the default value of NONE. The accepted types are:</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.DatabaseUser.auth_database_name">
<em class="property">property </em><code class="sig-name descname">auth_database_name</code><a class="headerlink" href="#pulumi_mongodbatlas.DatabaseUser.auth_database_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Database against which Atlas authenticates the user. A user must provide both a username and authentication database to log into MongoDB.
Accepted values include:</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.DatabaseUser.aws_iam_type">
<em class="property">property </em><code class="sig-name descname">aws_iam_type</code><a class="headerlink" href="#pulumi_mongodbatlas.DatabaseUser.aws_iam_type" title="Permalink to this definition">¶</a></dt>
<dd><p>If this value is set, the new database user authenticates with AWS IAM credentials. If no value is given, Atlas uses the default value of NONE. The accepted types are:</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.DatabaseUser.database_name">
<em class="property">property </em><code class="sig-name descname">database_name</code><a class="headerlink" href="#pulumi_mongodbatlas.DatabaseUser.database_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Database on which the user has the specified role. A role on the <code class="docutils literal notranslate"><span class="pre">admin</span></code> database can include privileges that apply to the other databases.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.DatabaseUser.project_id">
<em class="property">property </em><code class="sig-name descname">project_id</code><a class="headerlink" href="#pulumi_mongodbatlas.DatabaseUser.project_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The unique ID for the project to create the database user.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.DatabaseUser.roles">
<em class="property">property </em><code class="sig-name descname">roles</code><a class="headerlink" href="#pulumi_mongodbatlas.DatabaseUser.roles" title="Permalink to this definition">¶</a></dt>
<dd><p>List of user’s roles and the databases / collections on which the roles apply. A role allows the user to perform particular actions on the specified database. A role on the admin database can include privileges that apply to the other databases as well. See Roles below for more details.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.DatabaseUser.username">
<em class="property">property </em><code class="sig-name descname">username</code><a class="headerlink" href="#pulumi_mongodbatlas.DatabaseUser.username" title="Permalink to this definition">¶</a></dt>
<dd><p>Username for authenticating to MongoDB.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.DatabaseUser.x509_type">
<em class="property">property </em><code class="sig-name descname">x509_type</code><a class="headerlink" href="#pulumi_mongodbatlas.DatabaseUser.x509_type" title="Permalink to this definition">¶</a></dt>
<dd><p>X.509 method by which the provided username is authenticated. If no value is given, Atlas uses the default value of NONE. The accepted types are:</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.DatabaseUser.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.DatabaseUser.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_mongodbatlas.DatabaseUser.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.DatabaseUser.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py class">
<dt id="pulumi_mongodbatlas.EncryptionAtRest">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">EncryptionAtRest</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">aws_kms</span><span class="p">:</span> <span class="n">Union[EncryptionAtRestAwsKmsArgs, Mapping[str, Any], Awaitable[Union[EncryptionAtRestAwsKmsArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">azure_key_vault</span><span class="p">:</span> <span class="n">Union[EncryptionAtRestAzureKeyVaultArgs, Mapping[str, Any], Awaitable[Union[EncryptionAtRestAzureKeyVaultArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">google_cloud_kms</span><span class="p">:</span> <span class="n">Union[EncryptionAtRestGoogleCloudKmsArgs, Mapping[str, Any], Awaitable[Union[EncryptionAtRestGoogleCloudKmsArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.EncryptionAtRest" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">EncryptionAtRest</span></code> Allows management of encryption at rest for an Atlas project with one of the following providers:</p>
<p><a class="reference external" href="https://docs.atlas.mongodb.com/security-aws-kms/#security-aws-kms">Amazon Web Services Key Management Service</a>
<a class="reference external" href="https://docs.atlas.mongodb.com/security-azure-kms/#security-azure-kms">Azure Key Vault</a>
<a class="reference external" href="https://docs.atlas.mongodb.com/security-gcp-kms/#security-gcp-kms">Google Cloud KMS</a></p>
<p>After configuring at least one Encryption at Rest provider for the Atlas project, Project Owners can enable Encryption at Rest for each Atlas cluster for which they require encryption. The Encryption at Rest provider does not have to match the cluster cloud service provider.</p>
<p>Atlas does not automatically rotate user-managed encryption keys. Defer to your preferred Encryption at Rest provider’s documentation and guidance for best practices on key rotation. Atlas automatically creates a 365-day key rotation alert when you configure Encryption at Rest using your Key Management in an Atlas project.</p>
<p>See <a class="reference external" href="https://docs.atlas.mongodb.com/security-kms-encryption/index.html">Encryption at Rest</a> for more information, including prerequisites and restrictions.</p>
<blockquote>
<div><p><strong>IMPORTANT</strong> Atlas encrypts all cluster storage and snapshot volumes, securing all cluster data on disk: a concept known as encryption at rest, by default.</p>
<p><strong>NOTE:</strong> Groups and projects are synonymous terms. You may find <code class="docutils literal notranslate"><span class="pre">groupId</span></code> in the official documentation.</p>
</div></blockquote>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_mongodbatlas</span> <span class="k">as</span> <span class="nn">mongodbatlas</span>

<span class="n">test</span> <span class="o">=</span> <span class="n">mongodbatlas</span><span class="o">.</span><span class="n">EncryptionAtRest</span><span class="p">(</span><span class="s2">&quot;test&quot;</span><span class="p">,</span>
    <span class="n">aws_kms</span><span class="o">=</span><span class="n">mongodbatlas</span><span class="o">.</span><span class="n">EncryptionAtRestAwsKmsArgs</span><span class="p">(</span>
        <span class="n">access_key_id</span><span class="o">=</span><span class="s2">&quot;AKIAIOSFODNN7EXAMPLE&quot;</span><span class="p">,</span>
        <span class="n">customer_master_key_id</span><span class="o">=</span><span class="s2">&quot;030gce02-586d-48d2-a966-05ea954fde0g&quot;</span><span class="p">,</span>
        <span class="n">enabled</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
        <span class="n">region</span><span class="o">=</span><span class="s2">&quot;US_EAST_1&quot;</span><span class="p">,</span>
        <span class="n">secret_access_key</span><span class="o">=</span><span class="s2">&quot;wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY&quot;</span><span class="p">,</span>
    <span class="p">),</span>
    <span class="n">azure_key_vault</span><span class="o">=</span><span class="n">mongodbatlas</span><span class="o">.</span><span class="n">EncryptionAtRestAzureKeyVaultArgs</span><span class="p">(</span>
        <span class="n">azure_environment</span><span class="o">=</span><span class="s2">&quot;AZURE&quot;</span><span class="p">,</span>
        <span class="n">client_id</span><span class="o">=</span><span class="s2">&quot;g54f9e2-89e3-40fd-8188-EXAMPLEID&quot;</span><span class="p">,</span>
        <span class="n">enabled</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
        <span class="n">key_identifier</span><span class="o">=</span><span class="s2">&quot;https://EXAMPLEKeyVault.vault.azure.net/keys/EXAMPLEKey/d891821e3d364e9eb88fbd3d11807b86&quot;</span><span class="p">,</span>
        <span class="n">key_vault_name</span><span class="o">=</span><span class="s2">&quot;EXAMPLEKeyVault&quot;</span><span class="p">,</span>
        <span class="n">resource_group_name</span><span class="o">=</span><span class="s2">&quot;ExampleRGName&quot;</span><span class="p">,</span>
        <span class="n">secret</span><span class="o">=</span><span class="s2">&quot;EXAMPLESECRET&quot;</span><span class="p">,</span>
        <span class="n">subscription_id</span><span class="o">=</span><span class="s2">&quot;0ec944e3-g725-44f9-a147-EXAMPLEID&quot;</span><span class="p">,</span>
        <span class="n">tenant_id</span><span class="o">=</span><span class="s2">&quot;e8e4b6ba-ff32-4c88-a9af-EXAMPLEID&quot;</span><span class="p">,</span>
    <span class="p">),</span>
    <span class="n">google_cloud_kms</span><span class="o">=</span><span class="n">mongodbatlas</span><span class="o">.</span><span class="n">EncryptionAtRestGoogleCloudKmsArgs</span><span class="p">(</span>
        <span class="n">enabled</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
        <span class="n">key_version_resource_id</span><span class="o">=</span><span class="s2">&quot;projects/my-project-common-0/locations/us-east4/keyRings/my-key-ring-0/cryptoKeys/my-key-0/cryptoKeyVersions/1&quot;</span><span class="p">,</span>
        <span class="n">service_account_key</span><span class="o">=</span><span class="s2">&quot;{&quot;</span><span class="nb">type</span><span class="s2">&quot;: &quot;</span><span class="n">service_account</span><span class="s2">&quot;,&quot;</span><span class="n">project_id</span><span class="s2">&quot;: &quot;</span><span class="n">my</span><span class="o">-</span><span class="n">project</span><span class="o">-</span><span class="n">common</span><span class="o">-</span><span class="mi">0</span><span class="s2">&quot;,&quot;</span><span class="n">private_key_id</span><span class="s2">&quot;: &quot;</span><span class="n">e120598ea4f88249469fcdd75a9a785c1bb3</span><span class="s2">&quot;,&quot;</span><span class="n">private_key</span><span class="s2">&quot;: &quot;</span><span class="o">-----</span><span class="n">BEGIN</span> <span class="n">PRIVATE</span> <span class="n">KEY</span><span class="o">-----</span>\<span class="n">nMIIEuwIBA</span><span class="p">(</span><span class="n">truncated</span><span class="p">)</span><span class="n">SfecnS0mT94D9</span>\<span class="n">n</span><span class="o">-----</span><span class="n">END</span> <span class="n">PRIVATE</span> <span class="n">KEY</span><span class="o">-----</span>\<span class="n">n</span><span class="s2">&quot;,&quot;</span><span class="n">client_email</span><span class="s2">&quot;: &quot;</span><span class="n">my</span><span class="o">-</span><span class="n">email</span><span class="o">-</span><span class="n">kms</span><span class="o">-</span><span class="mi">0</span><span class="nd">@my</span><span class="o">-</span><span class="n">project</span><span class="o">-</span><span class="n">common</span><span class="o">-</span><span class="mf">0.</span><span class="n">iam</span><span class="o">.</span><span class="n">gserviceaccount</span><span class="o">.</span><span class="n">com</span><span class="s2">&quot;,&quot;</span><span class="n">client_id</span><span class="s2">&quot;: &quot;</span><span class="mi">10180967717292066</span><span class="s2">&quot;,&quot;</span><span class="n">auth_uri</span><span class="s2">&quot;: &quot;</span><span class="n">https</span><span class="p">:</span><span class="o">//</span><span class="n">accounts</span><span class="o">.</span><span class="n">google</span><span class="o">.</span><span class="n">com</span><span class="o">/</span><span class="n">o</span><span class="o">/</span><span class="n">oauth2</span><span class="o">/</span><span class="n">auth</span><span class="s2">&quot;,&quot;</span><span class="n">token_uri</span><span class="s2">&quot;: &quot;</span><span class="n">https</span><span class="p">:</span><span class="o">//</span><span class="n">accounts</span><span class="o">.</span><span class="n">google</span><span class="o">.</span><span class="n">com</span><span class="o">/</span><span class="n">o</span><span class="o">/</span><span class="n">oauth2</span><span class="o">/</span><span class="n">token</span><span class="s2">&quot;,&quot;</span><span class="n">auth_provider_x509_cert_url</span><span class="s2">&quot;: &quot;</span><span class="n">https</span><span class="p">:</span><span class="o">//</span><span class="n">www</span><span class="o">.</span><span class="n">googleapis</span><span class="o">.</span><span class="n">com</span><span class="o">/</span><span class="n">oauth2</span><span class="o">/</span><span class="n">v1</span><span class="o">/</span><span class="n">certs</span><span class="s2">&quot;,&quot;</span><span class="n">client_x509_cert_url</span><span class="s2">&quot;: &quot;</span><span class="n">https</span><span class="p">:</span><span class="o">//</span><span class="n">www</span><span class="o">.</span><span class="n">googleapis</span><span class="o">.</span><span class="n">com</span><span class="o">/</span><span class="n">robot</span><span class="o">/</span><span class="n">v1</span><span class="o">/</span><span class="n">metadata</span><span class="o">/</span><span class="n">x509</span><span class="o">/</span><span class="n">my</span><span class="o">-</span><span class="n">email</span><span class="o">-</span><span class="n">kms</span><span class="o">-</span><span class="mi">0</span><span class="o">%</span><span class="mi">40</span><span class="n">my</span><span class="o">-</span><span class="n">project</span><span class="o">-</span><span class="n">common</span><span class="o">-</span><span class="mf">0.</span><span class="n">iam</span><span class="o">.</span><span class="n">gserviceaccount</span><span class="o">.</span><span class="n">com</span><span class="s2">&quot;}&quot;</span><span class="p">,</span>
    <span class="p">),</span>
    <span class="n">project_id</span><span class="o">=</span><span class="s2">&quot;&lt;PROJECT-ID&gt;&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>aws_kms</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'EncryptionAtRestAwsKmsArgs'</em><em>]</em><em>]</em>) – Specifies AWS KMS configuration details and whether Encryption at Rest is enabled for an Atlas project.</p></li>
<li><p><strong>azure_key_vault</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'EncryptionAtRestAzureKeyVaultArgs'</em><em>]</em><em>]</em>) – Specifies Azure Key Vault configuration details and whether Encryption at Rest is enabled for an Atlas project.</p></li>
<li><p><strong>google_cloud_kms</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'EncryptionAtRestGoogleCloudKmsArgs'</em><em>]</em><em>]</em>) – Specifies GCP KMS configuration details and whether Encryption at Rest is enabled for an Atlas project.</p></li>
<li><p><strong>project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique identifier for the project.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_mongodbatlas.EncryptionAtRest.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">aws_kms</span><span class="p">:</span> <span class="n">Union[EncryptionAtRestAwsKmsArgs, Mapping[str, Any], Awaitable[Union[EncryptionAtRestAwsKmsArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">azure_key_vault</span><span class="p">:</span> <span class="n">Union[EncryptionAtRestAzureKeyVaultArgs, Mapping[str, Any], Awaitable[Union[EncryptionAtRestAzureKeyVaultArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">google_cloud_kms</span><span class="p">:</span> <span class="n">Union[EncryptionAtRestGoogleCloudKmsArgs, Mapping[str, Any], Awaitable[Union[EncryptionAtRestGoogleCloudKmsArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_mongodbatlas.encryption_at_rest.EncryptionAtRest<a class="headerlink" href="#pulumi_mongodbatlas.EncryptionAtRest.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing EncryptionAtRest resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>aws_kms</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'EncryptionAtRestAwsKmsArgs'</em><em>]</em><em>]</em>) – Specifies AWS KMS configuration details and whether Encryption at Rest is enabled for an Atlas project.</p></li>
<li><p><strong>azure_key_vault</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'EncryptionAtRestAzureKeyVaultArgs'</em><em>]</em><em>]</em>) – Specifies Azure Key Vault configuration details and whether Encryption at Rest is enabled for an Atlas project.</p></li>
<li><p><strong>google_cloud_kms</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'EncryptionAtRestGoogleCloudKmsArgs'</em><em>]</em><em>]</em>) – Specifies GCP KMS configuration details and whether Encryption at Rest is enabled for an Atlas project.</p></li>
<li><p><strong>project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique identifier for the project.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.EncryptionAtRest.aws_kms">
<em class="property">property </em><code class="sig-name descname">aws_kms</code><a class="headerlink" href="#pulumi_mongodbatlas.EncryptionAtRest.aws_kms" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies AWS KMS configuration details and whether Encryption at Rest is enabled for an Atlas project.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.EncryptionAtRest.azure_key_vault">
<em class="property">property </em><code class="sig-name descname">azure_key_vault</code><a class="headerlink" href="#pulumi_mongodbatlas.EncryptionAtRest.azure_key_vault" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies Azure Key Vault configuration details and whether Encryption at Rest is enabled for an Atlas project.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.EncryptionAtRest.google_cloud_kms">
<em class="property">property </em><code class="sig-name descname">google_cloud_kms</code><a class="headerlink" href="#pulumi_mongodbatlas.EncryptionAtRest.google_cloud_kms" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies GCP KMS configuration details and whether Encryption at Rest is enabled for an Atlas project.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.EncryptionAtRest.project_id">
<em class="property">property </em><code class="sig-name descname">project_id</code><a class="headerlink" href="#pulumi_mongodbatlas.EncryptionAtRest.project_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The unique identifier for the project.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.EncryptionAtRest.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.EncryptionAtRest.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_mongodbatlas.EncryptionAtRest.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.EncryptionAtRest.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py class">
<dt id="pulumi_mongodbatlas.Get509AuthenticationDatabaseUserResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">Get509AuthenticationDatabaseUserResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">certificates</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">customer_x509_cas</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">username</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.Get509AuthenticationDatabaseUserResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by get509AuthenticationDatabaseUser.</p>
<dl class="py method">
<dt id="pulumi_mongodbatlas.Get509AuthenticationDatabaseUserResult.certificates">
<em class="property">property </em><code class="sig-name descname">certificates</code><a class="headerlink" href="#pulumi_mongodbatlas.Get509AuthenticationDatabaseUserResult.certificates" title="Permalink to this definition">¶</a></dt>
<dd><p>Array of objects where each details one unexpired database user certificate.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.Get509AuthenticationDatabaseUserResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_mongodbatlas.Get509AuthenticationDatabaseUserResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_mongodbatlas.GetAlertConfigurationResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">GetAlertConfigurationResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">alert_configuration_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">created</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">event_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">matchers</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">metric_threshold</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">notifications</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">threshold</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">updated</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.GetAlertConfigurationResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getAlertConfiguration.</p>
<dl class="py method">
<dt id="pulumi_mongodbatlas.GetAlertConfigurationResult.created">
<em class="property">property </em><code class="sig-name descname">created</code><a class="headerlink" href="#pulumi_mongodbatlas.GetAlertConfigurationResult.created" title="Permalink to this definition">¶</a></dt>
<dd><p>Timestamp in ISO 8601 date and time format in UTC when this alert configuration was created.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.GetAlertConfigurationResult.enabled">
<em class="property">property </em><code class="sig-name descname">enabled</code><a class="headerlink" href="#pulumi_mongodbatlas.GetAlertConfigurationResult.enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>If set to true, the alert configuration is enabled. If enabled is not exported it is set to false.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.GetAlertConfigurationResult.event_type">
<em class="property">property </em><code class="sig-name descname">event_type</code><a class="headerlink" href="#pulumi_mongodbatlas.GetAlertConfigurationResult.event_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of event that will trigger an alert.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.GetAlertConfigurationResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_mongodbatlas.GetAlertConfigurationResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.GetAlertConfigurationResult.threshold">
<em class="property">property </em><code class="sig-name descname">threshold</code><a class="headerlink" href="#pulumi_mongodbatlas.GetAlertConfigurationResult.threshold" title="Permalink to this definition">¶</a></dt>
<dd><p>Threshold value outside of which an alert will be triggered.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.GetAlertConfigurationResult.updated">
<em class="property">property </em><code class="sig-name descname">updated</code><a class="headerlink" href="#pulumi_mongodbatlas.GetAlertConfigurationResult.updated" title="Permalink to this definition">¶</a></dt>
<dd><p>Timestamp in ISO 8601 date and time format in UTC when this alert configuration was last updated.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_mongodbatlas.GetAuditingResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">GetAuditingResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">audit_authorization_success</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">audit_filter</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">configuration_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.GetAuditingResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getAuditing.</p>
<dl class="py method">
<dt id="pulumi_mongodbatlas.GetAuditingResult.audit_authorization_success">
<em class="property">property </em><code class="sig-name descname">audit_authorization_success</code><a class="headerlink" href="#pulumi_mongodbatlas.GetAuditingResult.audit_authorization_success" title="Permalink to this definition">¶</a></dt>
<dd><p>JSON-formatted audit filter used by the project</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.GetAuditingResult.audit_filter">
<em class="property">property </em><code class="sig-name descname">audit_filter</code><a class="headerlink" href="#pulumi_mongodbatlas.GetAuditingResult.audit_filter" title="Permalink to this definition">¶</a></dt>
<dd><p>Indicates whether the auditing system captures successful authentication attempts for audit filters using the “atype” : “authCheck” auditing event. For more information, see auditAuthorizationSuccess</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.GetAuditingResult.configuration_type">
<em class="property">property </em><code class="sig-name descname">configuration_type</code><a class="headerlink" href="#pulumi_mongodbatlas.GetAuditingResult.configuration_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Denotes the configuration method for the audit filter. Possible values are: NONE - auditing not configured for the project.m FILTER_BUILDER - auditing configured via Atlas UI filter builderm FILTER_JSON - auditing configured via Atlas custom filter or API.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.GetAuditingResult.enabled">
<em class="property">property </em><code class="sig-name descname">enabled</code><a class="headerlink" href="#pulumi_mongodbatlas.GetAuditingResult.enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Denotes whether or not the project associated with the {GROUP-ID} has database auditing enabled.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.GetAuditingResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_mongodbatlas.GetAuditingResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_mongodbatlas.GetCloudProviderAccessResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">GetCloudProviderAccessResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">aws_iam_roles</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.GetCloudProviderAccessResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getCloudProviderAccess.</p>
<dl class="py method">
<dt id="pulumi_mongodbatlas.GetCloudProviderAccessResult.aws_iam_roles">
<em class="property">property </em><code class="sig-name descname">aws_iam_roles</code><a class="headerlink" href="#pulumi_mongodbatlas.GetCloudProviderAccessResult.aws_iam_roles" title="Permalink to this definition">¶</a></dt>
<dd><p>A list where each represents a Cloud Provider Access Role.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.GetCloudProviderAccessResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_mongodbatlas.GetCloudProviderAccessResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_mongodbatlas.GetCloudProviderSnapshotBackupPolicyResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">GetCloudProviderSnapshotBackupPolicyResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">cluster_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cluster_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">next_snapshot</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policies</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">reference_hour_of_day</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">reference_minute_of_hour</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">restore_window_days</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">update_snapshots</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.GetCloudProviderSnapshotBackupPolicyResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getCloudProviderSnapshotBackupPolicy.</p>
<dl class="py method">
<dt id="pulumi_mongodbatlas.GetCloudProviderSnapshotBackupPolicyResult.cluster_id">
<em class="property">property </em><code class="sig-name descname">cluster_id</code><a class="headerlink" href="#pulumi_mongodbatlas.GetCloudProviderSnapshotBackupPolicyResult.cluster_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Unique identifier of the Atlas cluster.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.GetCloudProviderSnapshotBackupPolicyResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_mongodbatlas.GetCloudProviderSnapshotBackupPolicyResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.GetCloudProviderSnapshotBackupPolicyResult.next_snapshot">
<em class="property">property </em><code class="sig-name descname">next_snapshot</code><a class="headerlink" href="#pulumi_mongodbatlas.GetCloudProviderSnapshotBackupPolicyResult.next_snapshot" title="Permalink to this definition">¶</a></dt>
<dd><p>UTC ISO 8601 formatted point in time when Atlas will take the next snapshot.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.GetCloudProviderSnapshotBackupPolicyResult.policies">
<em class="property">property </em><code class="sig-name descname">policies</code><a class="headerlink" href="#pulumi_mongodbatlas.GetCloudProviderSnapshotBackupPolicyResult.policies" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of policy definitions for the cluster.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">policies.#.id</span></code> - Unique identifier of the backup policy.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.GetCloudProviderSnapshotBackupPolicyResult.reference_hour_of_day">
<em class="property">property </em><code class="sig-name descname">reference_hour_of_day</code><a class="headerlink" href="#pulumi_mongodbatlas.GetCloudProviderSnapshotBackupPolicyResult.reference_hour_of_day" title="Permalink to this definition">¶</a></dt>
<dd><p>UTC Hour of day between 0 and 23 representing which hour of the day that Atlas takes a snapshot.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.GetCloudProviderSnapshotBackupPolicyResult.reference_minute_of_hour">
<em class="property">property </em><code class="sig-name descname">reference_minute_of_hour</code><a class="headerlink" href="#pulumi_mongodbatlas.GetCloudProviderSnapshotBackupPolicyResult.reference_minute_of_hour" title="Permalink to this definition">¶</a></dt>
<dd><p>UTC Minute of day between 0 and 59 representing which minute of the referenceHourOfDay that Atlas takes the snapshot.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.GetCloudProviderSnapshotBackupPolicyResult.restore_window_days">
<em class="property">property </em><code class="sig-name descname">restore_window_days</code><a class="headerlink" href="#pulumi_mongodbatlas.GetCloudProviderSnapshotBackupPolicyResult.restore_window_days" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies a restore window in days for cloud backup to maintain.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_mongodbatlas.GetCloudProviderSnapshotRestoreJobResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">GetCloudProviderSnapshotRestoreJobResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">cancelled</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cluster_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">created_at</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">delivery_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">delivery_urls</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">expired</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">expires_at</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">finished_at</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">job_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">oplog_inc</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">oplog_ts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">point_in_time_utc_seconds</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">snapshot_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">target_cluster_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">target_project_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">timestamp</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.GetCloudProviderSnapshotRestoreJobResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getCloudProviderSnapshotRestoreJob.</p>
<dl class="py method">
<dt id="pulumi_mongodbatlas.GetCloudProviderSnapshotRestoreJobResult.cancelled">
<em class="property">property </em><code class="sig-name descname">cancelled</code><a class="headerlink" href="#pulumi_mongodbatlas.GetCloudProviderSnapshotRestoreJobResult.cancelled" title="Permalink to this definition">¶</a></dt>
<dd><p>Indicates whether the restore job was canceled.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.GetCloudProviderSnapshotRestoreJobResult.created_at">
<em class="property">property </em><code class="sig-name descname">created_at</code><a class="headerlink" href="#pulumi_mongodbatlas.GetCloudProviderSnapshotRestoreJobResult.created_at" title="Permalink to this definition">¶</a></dt>
<dd><p>UTC ISO 8601 formatted point in time when Atlas created the restore job.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.GetCloudProviderSnapshotRestoreJobResult.delivery_type">
<em class="property">property </em><code class="sig-name descname">delivery_type</code><a class="headerlink" href="#pulumi_mongodbatlas.GetCloudProviderSnapshotRestoreJobResult.delivery_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Type of restore job to create. Possible values are: automated and download.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.GetCloudProviderSnapshotRestoreJobResult.delivery_urls">
<em class="property">property </em><code class="sig-name descname">delivery_urls</code><a class="headerlink" href="#pulumi_mongodbatlas.GetCloudProviderSnapshotRestoreJobResult.delivery_urls" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more URLs for the compressed snapshot files for manual download. Only visible if deliveryType is download.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.GetCloudProviderSnapshotRestoreJobResult.expired">
<em class="property">property </em><code class="sig-name descname">expired</code><a class="headerlink" href="#pulumi_mongodbatlas.GetCloudProviderSnapshotRestoreJobResult.expired" title="Permalink to this definition">¶</a></dt>
<dd><p>Indicates whether the restore job expired.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.GetCloudProviderSnapshotRestoreJobResult.expires_at">
<em class="property">property </em><code class="sig-name descname">expires_at</code><a class="headerlink" href="#pulumi_mongodbatlas.GetCloudProviderSnapshotRestoreJobResult.expires_at" title="Permalink to this definition">¶</a></dt>
<dd><p>UTC ISO 8601 formatted point in time when the restore job expires.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.GetCloudProviderSnapshotRestoreJobResult.finished_at">
<em class="property">property </em><code class="sig-name descname">finished_at</code><a class="headerlink" href="#pulumi_mongodbatlas.GetCloudProviderSnapshotRestoreJobResult.finished_at" title="Permalink to this definition">¶</a></dt>
<dd><p>UTC ISO 8601 formatted point in time when the restore job completed.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.GetCloudProviderSnapshotRestoreJobResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_mongodbatlas.GetCloudProviderSnapshotRestoreJobResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.GetCloudProviderSnapshotRestoreJobResult.snapshot_id">
<em class="property">property </em><code class="sig-name descname">snapshot_id</code><a class="headerlink" href="#pulumi_mongodbatlas.GetCloudProviderSnapshotRestoreJobResult.snapshot_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Unique identifier of the source snapshot ID of the restore job.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.GetCloudProviderSnapshotRestoreJobResult.target_cluster_name">
<em class="property">property </em><code class="sig-name descname">target_cluster_name</code><a class="headerlink" href="#pulumi_mongodbatlas.GetCloudProviderSnapshotRestoreJobResult.target_cluster_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the target Atlas cluster to which the restore job restores the snapshot. Only visible if deliveryType is automated.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.GetCloudProviderSnapshotRestoreJobResult.timestamp">
<em class="property">property </em><code class="sig-name descname">timestamp</code><a class="headerlink" href="#pulumi_mongodbatlas.GetCloudProviderSnapshotRestoreJobResult.timestamp" title="Permalink to this definition">¶</a></dt>
<dd><p>Timestamp in ISO 8601 date and time format in UTC when the snapshot associated to snapshotId was taken.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_mongodbatlas.GetCloudProviderSnapshotRestoreJobsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">GetCloudProviderSnapshotRestoreJobsResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">cluster_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">items_per_page</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">page_num</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">results</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">total_count</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.GetCloudProviderSnapshotRestoreJobsResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getCloudProviderSnapshotRestoreJobs.</p>
<dl class="py method">
<dt id="pulumi_mongodbatlas.GetCloudProviderSnapshotRestoreJobsResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_mongodbatlas.GetCloudProviderSnapshotRestoreJobsResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.GetCloudProviderSnapshotRestoreJobsResult.results">
<em class="property">property </em><code class="sig-name descname">results</code><a class="headerlink" href="#pulumi_mongodbatlas.GetCloudProviderSnapshotRestoreJobsResult.results" title="Permalink to this definition">¶</a></dt>
<dd><p>Includes cloudProviderSnapshotRestoreJob object for each item detailed in the results array section.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_mongodbatlas.GetCloudProviderSnapshotResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">GetCloudProviderSnapshotResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">cluster_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">created_at</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">expires_at</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">master_key_uuid</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">mongod_version</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">snapshot_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">snapshot_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">storage_size_bytes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.GetCloudProviderSnapshotResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getCloudProviderSnapshot.</p>
<dl class="py method">
<dt id="pulumi_mongodbatlas.GetCloudProviderSnapshotResult.created_at">
<em class="property">property </em><code class="sig-name descname">created_at</code><a class="headerlink" href="#pulumi_mongodbatlas.GetCloudProviderSnapshotResult.created_at" title="Permalink to this definition">¶</a></dt>
<dd><p>UTC ISO 8601 formatted point in time when Atlas took the snapshot.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.GetCloudProviderSnapshotResult.description">
<em class="property">property </em><code class="sig-name descname">description</code><a class="headerlink" href="#pulumi_mongodbatlas.GetCloudProviderSnapshotResult.description" title="Permalink to this definition">¶</a></dt>
<dd><p>UDescription of the snapshot. Only present for on-demand snapshots.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.GetCloudProviderSnapshotResult.expires_at">
<em class="property">property </em><code class="sig-name descname">expires_at</code><a class="headerlink" href="#pulumi_mongodbatlas.GetCloudProviderSnapshotResult.expires_at" title="Permalink to this definition">¶</a></dt>
<dd><p>UTC ISO 8601 formatted point in time when Atlas will delete the snapshot.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.GetCloudProviderSnapshotResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_mongodbatlas.GetCloudProviderSnapshotResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.GetCloudProviderSnapshotResult.master_key_uuid">
<em class="property">property </em><code class="sig-name descname">master_key_uuid</code><a class="headerlink" href="#pulumi_mongodbatlas.GetCloudProviderSnapshotResult.master_key_uuid" title="Permalink to this definition">¶</a></dt>
<dd><p>Unique ID of the AWS KMS Customer Master Key used to encrypt the snapshot. Only visible for clusters using Encryption at Rest via Customer KMS.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.GetCloudProviderSnapshotResult.mongod_version">
<em class="property">property </em><code class="sig-name descname">mongod_version</code><a class="headerlink" href="#pulumi_mongodbatlas.GetCloudProviderSnapshotResult.mongod_version" title="Permalink to this definition">¶</a></dt>
<dd><p>Version of the MongoDB server.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.GetCloudProviderSnapshotResult.snapshot_type">
<em class="property">property </em><code class="sig-name descname">snapshot_type</code><a class="headerlink" href="#pulumi_mongodbatlas.GetCloudProviderSnapshotResult.snapshot_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Specified the type of snapshot. Valid values are onDemand and scheduled.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.GetCloudProviderSnapshotResult.status">
<em class="property">property </em><code class="sig-name descname">status</code><a class="headerlink" href="#pulumi_mongodbatlas.GetCloudProviderSnapshotResult.status" title="Permalink to this definition">¶</a></dt>
<dd><p>Current status of the snapshot. One of the following values: queued, inProgress, completed, failed.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.GetCloudProviderSnapshotResult.storage_size_bytes">
<em class="property">property </em><code class="sig-name descname">storage_size_bytes</code><a class="headerlink" href="#pulumi_mongodbatlas.GetCloudProviderSnapshotResult.storage_size_bytes" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the size of the snapshot in bytes.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.GetCloudProviderSnapshotResult.type">
<em class="property">property </em><code class="sig-name descname">type</code><a class="headerlink" href="#pulumi_mongodbatlas.GetCloudProviderSnapshotResult.type" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the type of cluster: replicaSet or shardedCluster.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_mongodbatlas.GetCloudProviderSnapshotsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">GetCloudProviderSnapshotsResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">cluster_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">items_per_page</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">page_num</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">results</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">total_count</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.GetCloudProviderSnapshotsResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getCloudProviderSnapshots.</p>
<dl class="py method">
<dt id="pulumi_mongodbatlas.GetCloudProviderSnapshotsResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_mongodbatlas.GetCloudProviderSnapshotsResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.GetCloudProviderSnapshotsResult.results">
<em class="property">property </em><code class="sig-name descname">results</code><a class="headerlink" href="#pulumi_mongodbatlas.GetCloudProviderSnapshotsResult.results" title="Permalink to this definition">¶</a></dt>
<dd><p>Includes cloudProviderSnapshot object for each item detailed in the results array section.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_mongodbatlas.GetClusterResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">GetClusterResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">auto_scaling_compute_enabled</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auto_scaling_compute_scale_down_enabled</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auto_scaling_disk_gb_enabled</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">backing_provider_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">backup_enabled</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">bi_connector</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cluster_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">connection_strings</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">container_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">disk_size_gb</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">encryption_at_rest_provider</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">labels</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">mongo_db_major_version</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">mongo_db_version</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">mongo_uri</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">mongo_uri_updated</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">mongo_uri_with_options</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">num_shards</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">paused</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">pit_enabled</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">provider_auto_scaling_compute_max_instance_size</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">provider_auto_scaling_compute_min_instance_size</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">provider_backup_enabled</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">provider_disk_iops</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">provider_disk_type_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">provider_encrypt_ebs_volume</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">provider_instance_size_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">provider_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">provider_region_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">provider_volume_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">replication_factor</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">replication_specs</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">snapshot_backup_policies</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">srv_address</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">state_name</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.GetClusterResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getCluster.</p>
<dl class="py method">
<dt id="pulumi_mongodbatlas.GetClusterResult.auto_scaling_compute_enabled">
<em class="property">property </em><code class="sig-name descname">auto_scaling_compute_enabled</code><a class="headerlink" href="#pulumi_mongodbatlas.GetClusterResult.auto_scaling_compute_enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>(Optional) Specifies whether cluster tier auto-scaling is enabled. The default is false.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.GetClusterResult.auto_scaling_compute_scale_down_enabled">
<em class="property">property </em><code class="sig-name descname">auto_scaling_compute_scale_down_enabled</code><a class="headerlink" href="#pulumi_mongodbatlas.GetClusterResult.auto_scaling_compute_scale_down_enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>(Optional) Set to <code class="docutils literal notranslate"><span class="pre">true</span></code> to enable the cluster tier to scale down.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.GetClusterResult.auto_scaling_disk_gb_enabled">
<em class="property">property </em><code class="sig-name descname">auto_scaling_disk_gb_enabled</code><a class="headerlink" href="#pulumi_mongodbatlas.GetClusterResult.auto_scaling_disk_gb_enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Indicates whether disk auto-scaling is enabled.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.GetClusterResult.backing_provider_name">
<em class="property">property </em><code class="sig-name descname">backing_provider_name</code><a class="headerlink" href="#pulumi_mongodbatlas.GetClusterResult.backing_provider_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Indicates Cloud service provider on which the server for a multi-tenant cluster is provisioned.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.GetClusterResult.backup_enabled">
<em class="property">property </em><code class="sig-name descname">backup_enabled</code><a class="headerlink" href="#pulumi_mongodbatlas.GetClusterResult.backup_enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Legacy Option, Indicates whether Atlas continuous backups are enabled for the cluster.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.GetClusterResult.bi_connector">
<em class="property">property </em><code class="sig-name descname">bi_connector</code><a class="headerlink" href="#pulumi_mongodbatlas.GetClusterResult.bi_connector" title="Permalink to this definition">¶</a></dt>
<dd><p>Indicates BI Connector for Atlas configuration on this cluster. BI Connector for Atlas is only available for M10+ clusters. See BI Connector below for more details.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.GetClusterResult.cluster_type">
<em class="property">property </em><code class="sig-name descname">cluster_type</code><a class="headerlink" href="#pulumi_mongodbatlas.GetClusterResult.cluster_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Indicates the type of the cluster that you want to modify. You cannot convert a sharded cluster deployment to a replica set deployment.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.GetClusterResult.connection_strings">
<em class="property">property </em><code class="sig-name descname">connection_strings</code><a class="headerlink" href="#pulumi_mongodbatlas.GetClusterResult.connection_strings" title="Permalink to this definition">¶</a></dt>
<dd><p>Set of connection strings that your applications use to connect to this cluster. More info in <a class="reference external" href="https://docs.mongodb.com/manual/reference/connection-string/">Connection-strings</a>. Use the parameters in this object to connect your applications to this cluster. To learn more about the formats of connection strings, see <a class="reference external" href="https://docs.atlas.mongodb.com/reference/faq/connection-changes/">Connection String Options</a>. NOTE: Atlas returns the contents of this object after the cluster is operational, not while it builds the cluster.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">connection_strings.standard</span></code> -   Public mongodb:// connection string for this cluster.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">connection_strings.standard_srv</span></code> - Public mongodb+srv:// connection string for this cluster. The mongodb+srv protocol tells the driver to look up the seed list of hosts in DNS. Atlas synchronizes this list with the nodes in a cluster. If the connection string uses this URI format, you don’t need to append the seed list or change the URI if the nodes change. Use this URI format if your driver supports it. If it doesn’t, use connectionStrings.standard.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">connection_strings.aws_private_link</span></code> -  <a class="reference external" href="https://docs.atlas.mongodb.com/security-private-endpoint/#private-endpoint-connection-strings">Private-endpoint-aware</a> mongodb://connection strings for each interface VPC endpoint you configured to connect to this cluster. Returned only if you created a AWS PrivateLink connection to this cluster.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">connection_strings.aws_private_link_srv</span></code> - <a class="reference external" href="https://docs.atlas.mongodb.com/security-private-endpoint/#private-endpoint-connection-strings">Private-endpoint-aware</a> mongodb+srv://connection strings for each interface VPC endpoint you configured to connect to this cluster. Returned only if you created a AWS PrivateLink connection to this cluster. Use this URI format if your driver supports it. If it doesn’t, use connectionStrings.awsPrivateLink.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">connection_strings.private</span></code> -   <a class="reference external" href="https://docs.atlas.mongodb.com/security-vpc-peering/#vpc-peering">Network-peering-endpoint-aware</a> mongodb://connection strings for each interface VPC endpoint you configured to connect to this cluster. Returned only if you created a network peering connection to this cluster.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">connection_strings.private_srv</span></code> -  <a class="reference external" href="https://docs.atlas.mongodb.com/security-vpc-peering/#vpc-peering">Network-peering-endpoint-aware</a> mongodb+srv://connection strings for each interface VPC endpoint you configured to connect to this cluster. Returned only if you created a network peering connection to this cluster.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.GetClusterResult.container_id">
<em class="property">property </em><code class="sig-name descname">container_id</code><a class="headerlink" href="#pulumi_mongodbatlas.GetClusterResult.container_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The Network Peering Container ID.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.GetClusterResult.disk_size_gb">
<em class="property">property </em><code class="sig-name descname">disk_size_gb</code><a class="headerlink" href="#pulumi_mongodbatlas.GetClusterResult.disk_size_gb" title="Permalink to this definition">¶</a></dt>
<dd><p>Indicates the size in gigabytes of the server’s root volume (AWS/GCP Only).</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.GetClusterResult.encryption_at_rest_provider">
<em class="property">property </em><code class="sig-name descname">encryption_at_rest_provider</code><a class="headerlink" href="#pulumi_mongodbatlas.GetClusterResult.encryption_at_rest_provider" title="Permalink to this definition">¶</a></dt>
<dd><p>Indicates whether Encryption at Rest is enabled or disabled.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.GetClusterResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_mongodbatlas.GetClusterResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.GetClusterResult.mongo_db_major_version">
<em class="property">property </em><code class="sig-name descname">mongo_db_major_version</code><a class="headerlink" href="#pulumi_mongodbatlas.GetClusterResult.mongo_db_major_version" title="Permalink to this definition">¶</a></dt>
<dd><p>Indicates the version of the cluster to deploy.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.GetClusterResult.mongo_db_version">
<em class="property">property </em><code class="sig-name descname">mongo_db_version</code><a class="headerlink" href="#pulumi_mongodbatlas.GetClusterResult.mongo_db_version" title="Permalink to this definition">¶</a></dt>
<dd><p>Version of MongoDB the cluster runs, in <code class="docutils literal notranslate"><span class="pre">major-version</span></code>.<code class="docutils literal notranslate"><span class="pre">minor-version</span></code> format.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.GetClusterResult.mongo_uri">
<em class="property">property </em><code class="sig-name descname">mongo_uri</code><a class="headerlink" href="#pulumi_mongodbatlas.GetClusterResult.mongo_uri" title="Permalink to this definition">¶</a></dt>
<dd><p>Base connection string for the cluster. Atlas only displays this field after the cluster is operational, not while it builds the cluster.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.GetClusterResult.mongo_uri_updated">
<em class="property">property </em><code class="sig-name descname">mongo_uri_updated</code><a class="headerlink" href="#pulumi_mongodbatlas.GetClusterResult.mongo_uri_updated" title="Permalink to this definition">¶</a></dt>
<dd><p>Lists when the connection string was last updated. The connection string changes, for example, if you change a replica set to a sharded cluster.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.GetClusterResult.mongo_uri_with_options">
<em class="property">property </em><code class="sig-name descname">mongo_uri_with_options</code><a class="headerlink" href="#pulumi_mongodbatlas.GetClusterResult.mongo_uri_with_options" title="Permalink to this definition">¶</a></dt>
<dd><p>Describes connection string for connecting to the Atlas cluster. Includes the replicaSet, ssl, and authSource query parameters in the connection string with values appropriate for the cluster.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.GetClusterResult.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_mongodbatlas.GetClusterResult.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the current plugin</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.GetClusterResult.num_shards">
<em class="property">property </em><code class="sig-name descname">num_shards</code><a class="headerlink" href="#pulumi_mongodbatlas.GetClusterResult.num_shards" title="Permalink to this definition">¶</a></dt>
<dd><p>Number of shards to deploy in the specified zone.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.GetClusterResult.paused">
<em class="property">property </em><code class="sig-name descname">paused</code><a class="headerlink" href="#pulumi_mongodbatlas.GetClusterResult.paused" title="Permalink to this definition">¶</a></dt>
<dd><p>Flag that indicates whether the cluster is paused or not.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.GetClusterResult.pit_enabled">
<em class="property">property </em><code class="sig-name descname">pit_enabled</code><a class="headerlink" href="#pulumi_mongodbatlas.GetClusterResult.pit_enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Flag that indicates if the cluster uses Continuous Cloud Backup.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.GetClusterResult.provider_auto_scaling_compute_max_instance_size">
<em class="property">property </em><code class="sig-name descname">provider_auto_scaling_compute_max_instance_size</code><a class="headerlink" href="#pulumi_mongodbatlas.GetClusterResult.provider_auto_scaling_compute_max_instance_size" title="Permalink to this definition">¶</a></dt>
<dd><p>(Optional) Maximum instance size to which your cluster can automatically scale.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.GetClusterResult.provider_auto_scaling_compute_min_instance_size">
<em class="property">property </em><code class="sig-name descname">provider_auto_scaling_compute_min_instance_size</code><a class="headerlink" href="#pulumi_mongodbatlas.GetClusterResult.provider_auto_scaling_compute_min_instance_size" title="Permalink to this definition">¶</a></dt>
<dd><p>(Optional) Minimum instance size to which your cluster can automatically scale.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.GetClusterResult.provider_backup_enabled">
<em class="property">property </em><code class="sig-name descname">provider_backup_enabled</code><a class="headerlink" href="#pulumi_mongodbatlas.GetClusterResult.provider_backup_enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Flag indicating if the cluster uses Cloud Backup Snapshots for backups.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.GetClusterResult.provider_disk_iops">
<em class="property">property </em><code class="sig-name descname">provider_disk_iops</code><a class="headerlink" href="#pulumi_mongodbatlas.GetClusterResult.provider_disk_iops" title="Permalink to this definition">¶</a></dt>
<dd><p>Indicates the maximum input/output operations per second (IOPS) the system can perform. The possible values depend on the selected providerSettings.instanceSizeName and diskSizeGB.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.GetClusterResult.provider_disk_type_name">
<em class="property">property </em><code class="sig-name descname">provider_disk_type_name</code><a class="headerlink" href="#pulumi_mongodbatlas.GetClusterResult.provider_disk_type_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Describes Azure disk type of the server’s root volume (Azure Only).</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.GetClusterResult.provider_encrypt_ebs_volume">
<em class="property">property </em><code class="sig-name descname">provider_encrypt_ebs_volume</code><a class="headerlink" href="#pulumi_mongodbatlas.GetClusterResult.provider_encrypt_ebs_volume" title="Permalink to this definition">¶</a></dt>
<dd><p>Indicates whether the Amazon EBS encryption is enabled. This feature encrypts the server’s root volume for both data at rest within the volume and data moving between the volume and the instance.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.GetClusterResult.provider_instance_size_name">
<em class="property">property </em><code class="sig-name descname">provider_instance_size_name</code><a class="headerlink" href="#pulumi_mongodbatlas.GetClusterResult.provider_instance_size_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Atlas provides different instance sizes, each with a default storage capacity and RAM size.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.GetClusterResult.provider_name">
<em class="property">property </em><code class="sig-name descname">provider_name</code><a class="headerlink" href="#pulumi_mongodbatlas.GetClusterResult.provider_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Indicates the cloud service provider on which the servers are provisioned.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.GetClusterResult.provider_region_name">
<em class="property">property </em><code class="sig-name descname">provider_region_name</code><a class="headerlink" href="#pulumi_mongodbatlas.GetClusterResult.provider_region_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Indicates Physical location of your MongoDB cluster. The region you choose can affect network latency for clients accessing your databases.  Requires the Atlas Region name, see the reference list for <a class="reference external" href="https://docs.atlas.mongodb.com/reference/amazon-aws/">AWS</a>, <a class="reference external" href="https://docs.atlas.mongodb.com/reference/google-gcp/">GCP</a>, <a class="reference external" href="https://docs.atlas.mongodb.com/reference/microsoft-azure/">Azure</a>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.GetClusterResult.provider_volume_type">
<em class="property">property </em><code class="sig-name descname">provider_volume_type</code><a class="headerlink" href="#pulumi_mongodbatlas.GetClusterResult.provider_volume_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Indicates the type of the volume. The possible values are: <code class="docutils literal notranslate"><span class="pre">STANDARD</span></code> and <code class="docutils literal notranslate"><span class="pre">PROVISIONED</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.GetClusterResult.replication_factor">
<em class="property">property </em><code class="sig-name descname">replication_factor</code><a class="headerlink" href="#pulumi_mongodbatlas.GetClusterResult.replication_factor" title="Permalink to this definition">¶</a></dt>
<dd><p>(Deprecated) Number of replica set members. Each member keeps a copy of your databases, providing high availability and data redundancy. The possible values are 3, 5, or 7. The default value is 3.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.GetClusterResult.replication_specs">
<em class="property">property </em><code class="sig-name descname">replication_specs</code><a class="headerlink" href="#pulumi_mongodbatlas.GetClusterResult.replication_specs" title="Permalink to this definition">¶</a></dt>
<dd><p>Configuration for cluster regions.  See Replication Spec below for more details.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.GetClusterResult.snapshot_backup_policies">
<em class="property">property </em><code class="sig-name descname">snapshot_backup_policies</code><a class="headerlink" href="#pulumi_mongodbatlas.GetClusterResult.snapshot_backup_policies" title="Permalink to this definition">¶</a></dt>
<dd><p>current snapshot schedule and retention settings for the cluster.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.GetClusterResult.srv_address">
<em class="property">property </em><code class="sig-name descname">srv_address</code><a class="headerlink" href="#pulumi_mongodbatlas.GetClusterResult.srv_address" title="Permalink to this definition">¶</a></dt>
<dd><p>Connection string for connecting to the Atlas cluster. The +srv modifier forces the connection to use TLS/SSL. See the mongoURI for additional options.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.GetClusterResult.state_name">
<em class="property">property </em><code class="sig-name descname">state_name</code><a class="headerlink" href="#pulumi_mongodbatlas.GetClusterResult.state_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Indicates the current state of the cluster. The possible states are:</p>
<ul class="simple">
<li><p>IDLE</p></li>
<li><p>CREATING</p></li>
<li><p>UPDATING</p></li>
<li><p>DELETING</p></li>
<li><p>DELETED</p></li>
<li><p>REPAIRING</p></li>
</ul>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_mongodbatlas.GetClustersResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">GetClustersResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">results</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.GetClustersResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getClusters.</p>
<dl class="py method">
<dt id="pulumi_mongodbatlas.GetClustersResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_mongodbatlas.GetClustersResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.GetClustersResult.results">
<em class="property">property </em><code class="sig-name descname">results</code><a class="headerlink" href="#pulumi_mongodbatlas.GetClustersResult.results" title="Permalink to this definition">¶</a></dt>
<dd><p>A list where each represents a Cluster. See Cluster below for more details.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_mongodbatlas.GetCustomDbRoleResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">GetCustomDbRoleResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">actions</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">inherited_roles</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">role_name</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.GetCustomDbRoleResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getCustomDbRole.</p>
<dl class="py method">
<dt id="pulumi_mongodbatlas.GetCustomDbRoleResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_mongodbatlas.GetCustomDbRoleResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_mongodbatlas.GetCustomDbRolesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">GetCustomDbRolesResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">results</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.GetCustomDbRolesResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getCustomDbRoles.</p>
<dl class="py method">
<dt id="pulumi_mongodbatlas.GetCustomDbRolesResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_mongodbatlas.GetCustomDbRolesResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.GetCustomDbRolesResult.results">
<em class="property">property </em><code class="sig-name descname">results</code><a class="headerlink" href="#pulumi_mongodbatlas.GetCustomDbRolesResult.results" title="Permalink to this definition">¶</a></dt>
<dd><p>A list where each represents a custom db roles.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_mongodbatlas.GetDatabaseUserResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">GetDatabaseUserResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">auth_database_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">aws_iam_type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">database_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">labels</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">roles</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">scopes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">username</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">x509_type</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.GetDatabaseUserResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getDatabaseUser.</p>
<dl class="py method">
<dt id="pulumi_mongodbatlas.GetDatabaseUserResult.aws_iam_type">
<em class="property">property </em><code class="sig-name descname">aws_iam_type</code><a class="headerlink" href="#pulumi_mongodbatlas.GetDatabaseUserResult.aws_iam_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The new database user authenticates with AWS IAM credentials. Default is <code class="docutils literal notranslate"><span class="pre">NONE</span></code>, <code class="docutils literal notranslate"><span class="pre">USER</span></code> means user has AWS IAM user credentials, <code class="docutils literal notranslate"><span class="pre">ROLE</span></code> - means user has credentials associated with an AWS IAM role.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.GetDatabaseUserResult.database_name">
<em class="property">property </em><code class="sig-name descname">database_name</code><a class="headerlink" href="#pulumi_mongodbatlas.GetDatabaseUserResult.database_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Database on which the user has the specified role. A role on the <code class="docutils literal notranslate"><span class="pre">admin</span></code> database can include privileges that apply to the other databases.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.GetDatabaseUserResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_mongodbatlas.GetDatabaseUserResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.GetDatabaseUserResult.roles">
<em class="property">property </em><code class="sig-name descname">roles</code><a class="headerlink" href="#pulumi_mongodbatlas.GetDatabaseUserResult.roles" title="Permalink to this definition">¶</a></dt>
<dd><p>List of user’s roles and the databases / collections on which the roles apply. A role allows the user to perform particular actions on the specified database. A role on the admin database can include privileges that apply to the other databases as well. See Roles below for more details.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.GetDatabaseUserResult.scopes">
<em class="property">property </em><code class="sig-name descname">scopes</code><a class="headerlink" href="#pulumi_mongodbatlas.GetDatabaseUserResult.scopes" title="Permalink to this definition">¶</a></dt>
<dd><p>Array of clusters and Atlas Data Lakes that this user has access to.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.GetDatabaseUserResult.x509_type">
<em class="property">property </em><code class="sig-name descname">x509_type</code><a class="headerlink" href="#pulumi_mongodbatlas.GetDatabaseUserResult.x509_type" title="Permalink to this definition">¶</a></dt>
<dd><p>X.509 method by which the provided username is authenticated.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_mongodbatlas.GetDatabaseUsersResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">GetDatabaseUsersResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">results</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.GetDatabaseUsersResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getDatabaseUsers.</p>
<dl class="py method">
<dt id="pulumi_mongodbatlas.GetDatabaseUsersResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_mongodbatlas.GetDatabaseUsersResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.GetDatabaseUsersResult.project_id">
<em class="property">property </em><code class="sig-name descname">project_id</code><a class="headerlink" href="#pulumi_mongodbatlas.GetDatabaseUsersResult.project_id" title="Permalink to this definition">¶</a></dt>
<dd><p>ID of the Atlas project the user belongs to.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.GetDatabaseUsersResult.results">
<em class="property">property </em><code class="sig-name descname">results</code><a class="headerlink" href="#pulumi_mongodbatlas.GetDatabaseUsersResult.results" title="Permalink to this definition">¶</a></dt>
<dd><p>A list where each represents a Database user.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_mongodbatlas.GetGlobalClusterConfigResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">GetGlobalClusterConfigResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">cluster_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_zone_mapping</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">managed_namespaces</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.GetGlobalClusterConfigResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getGlobalClusterConfig.</p>
<dl class="py method">
<dt id="pulumi_mongodbatlas.GetGlobalClusterConfigResult.custom_zone_mapping">
<em class="property">property </em><code class="sig-name descname">custom_zone_mapping</code><a class="headerlink" href="#pulumi_mongodbatlas.GetGlobalClusterConfigResult.custom_zone_mapping" title="Permalink to this definition">¶</a></dt>
<dd><p>A map of all custom zone mappings defined for the Global Cluster. Atlas automatically maps each location code to the closest geographical zone. Custom zone mappings allow administrators to override these automatic mappings. If your Global Cluster does not have any custom zone mappings, this document is empty.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.GetGlobalClusterConfigResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_mongodbatlas.GetGlobalClusterConfigResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.GetGlobalClusterConfigResult.managed_namespaces">
<em class="property">property </em><code class="sig-name descname">managed_namespaces</code><a class="headerlink" href="#pulumi_mongodbatlas.GetGlobalClusterConfigResult.managed_namespaces" title="Permalink to this definition">¶</a></dt>
<dd><p>Add a managed namespaces to a Global Cluster. For more information about managed namespaces, see <a class="reference external" href="https://docs.atlas.mongodb.com/reference/api/global-clusters/">Global Clusters</a>. See Managed Namespace below for more details.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_mongodbatlas.GetMaintenanceWindowResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">GetMaintenanceWindowResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">day_of_week</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">hour_of_day</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">number_of_deferrals</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">start_asap</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.GetMaintenanceWindowResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getMaintenanceWindow.</p>
<dl class="py method">
<dt id="pulumi_mongodbatlas.GetMaintenanceWindowResult.day_of_week">
<em class="property">property </em><code class="sig-name descname">day_of_week</code><a class="headerlink" href="#pulumi_mongodbatlas.GetMaintenanceWindowResult.day_of_week" title="Permalink to this definition">¶</a></dt>
<dd><p>Day of the week when you would like the maintenance window to start as a 1-based integer: S=1, M=2, T=3, W=4, T=5, F=6, S=7.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.GetMaintenanceWindowResult.hour_of_day">
<em class="property">property </em><code class="sig-name descname">hour_of_day</code><a class="headerlink" href="#pulumi_mongodbatlas.GetMaintenanceWindowResult.hour_of_day" title="Permalink to this definition">¶</a></dt>
<dd><p>Hour of the day when you would like the maintenance window to start. This parameter uses the 24-hour clock, where midnight is 0, noon is 12  (Time zone is UTC).</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.GetMaintenanceWindowResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_mongodbatlas.GetMaintenanceWindowResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.GetMaintenanceWindowResult.number_of_deferrals">
<em class="property">property </em><code class="sig-name descname">number_of_deferrals</code><a class="headerlink" href="#pulumi_mongodbatlas.GetMaintenanceWindowResult.number_of_deferrals" title="Permalink to this definition">¶</a></dt>
<dd><p>Number of times the current maintenance event for this project has been deferred, you can set a maximum of 2 deferrals.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.GetMaintenanceWindowResult.start_asap">
<em class="property">property </em><code class="sig-name descname">start_asap</code><a class="headerlink" href="#pulumi_mongodbatlas.GetMaintenanceWindowResult.start_asap" title="Permalink to this definition">¶</a></dt>
<dd><p>Flag indicating whether project maintenance has been directed to start immediately. If you request that maintenance begin immediately, this field returns true from the time the request was made until the time the maintenance event completes.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_mongodbatlas.GetNetworkContainerResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">GetNetworkContainerResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">atlas_cidr_block</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">azure_subscription_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">container_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">gcp_project_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">network_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">provider_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">provisioned</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">region</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">region_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vnet_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vpc_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.GetNetworkContainerResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getNetworkContainer.</p>
<dl class="py method">
<dt id="pulumi_mongodbatlas.GetNetworkContainerResult.atlas_cidr_block">
<em class="property">property </em><code class="sig-name descname">atlas_cidr_block</code><a class="headerlink" href="#pulumi_mongodbatlas.GetNetworkContainerResult.atlas_cidr_block" title="Permalink to this definition">¶</a></dt>
<dd><p>CIDR block that Atlas uses for your clusters. Atlas uses the specified CIDR block for all other Network Peering connections created in the project. The Atlas CIDR block must be at least a /24 and at most a /21 in one of the following <a class="reference external" href="https://tools.ietf.org/html/rfc1918.html#section-3">private networks</a>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.GetNetworkContainerResult.azure_subscription_id">
<em class="property">property </em><code class="sig-name descname">azure_subscription_id</code><a class="headerlink" href="#pulumi_mongodbatlas.GetNetworkContainerResult.azure_subscription_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Unique identifer of the Azure subscription in which the VNet resides.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.GetNetworkContainerResult.gcp_project_id">
<em class="property">property </em><code class="sig-name descname">gcp_project_id</code><a class="headerlink" href="#pulumi_mongodbatlas.GetNetworkContainerResult.gcp_project_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Unique identifier of the GCP project in which the Network Peering connection resides.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.GetNetworkContainerResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_mongodbatlas.GetNetworkContainerResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.GetNetworkContainerResult.network_name">
<em class="property">property </em><code class="sig-name descname">network_name</code><a class="headerlink" href="#pulumi_mongodbatlas.GetNetworkContainerResult.network_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the Network Peering connection in the Atlas project.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.GetNetworkContainerResult.provider_name">
<em class="property">property </em><code class="sig-name descname">provider_name</code><a class="headerlink" href="#pulumi_mongodbatlas.GetNetworkContainerResult.provider_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Cloud provider for this Network Peering connection. If omitted, Atlas sets this parameter to AWS.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.GetNetworkContainerResult.provisioned">
<em class="property">property </em><code class="sig-name descname">provisioned</code><a class="headerlink" href="#pulumi_mongodbatlas.GetNetworkContainerResult.provisioned" title="Permalink to this definition">¶</a></dt>
<dd><p>Indicates whether the project has Network Peering connections deployed in the container.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.GetNetworkContainerResult.region">
<em class="property">property </em><code class="sig-name descname">region</code><a class="headerlink" href="#pulumi_mongodbatlas.GetNetworkContainerResult.region" title="Permalink to this definition">¶</a></dt>
<dd><p>The Atlas Azure region name for where this container will exist.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.GetNetworkContainerResult.region_name">
<em class="property">property </em><code class="sig-name descname">region_name</code><a class="headerlink" href="#pulumi_mongodbatlas.GetNetworkContainerResult.region_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The Atlas AWS region name for where this container will exist.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.GetNetworkContainerResult.vnet_name">
<em class="property">property </em><code class="sig-name descname">vnet_name</code><a class="headerlink" href="#pulumi_mongodbatlas.GetNetworkContainerResult.vnet_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Azure VNet. This value is null until you provision an Azure VNet in the container.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.GetNetworkContainerResult.vpc_id">
<em class="property">property </em><code class="sig-name descname">vpc_id</code><a class="headerlink" href="#pulumi_mongodbatlas.GetNetworkContainerResult.vpc_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Unique identifier of the project’s VPC.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_mongodbatlas.GetNetworkContainersResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">GetNetworkContainersResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">provider_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">results</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.GetNetworkContainersResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getNetworkContainers.</p>
<dl class="py method">
<dt id="pulumi_mongodbatlas.GetNetworkContainersResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_mongodbatlas.GetNetworkContainersResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.GetNetworkContainersResult.provider_name">
<em class="property">property </em><code class="sig-name descname">provider_name</code><a class="headerlink" href="#pulumi_mongodbatlas.GetNetworkContainersResult.provider_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Cloud provider for this Network Peering connection. If omitted, Atlas sets this parameter to AWS.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.GetNetworkContainersResult.results">
<em class="property">property </em><code class="sig-name descname">results</code><a class="headerlink" href="#pulumi_mongodbatlas.GetNetworkContainersResult.results" title="Permalink to this definition">¶</a></dt>
<dd><p>A list where each represents a Network Peering Container.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_mongodbatlas.GetNetworkPeeringResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">GetNetworkPeeringResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">accepter_region_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">atlas_cidr_block</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">atlas_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">aws_account_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">azure_directory_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">azure_subscription_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">connection_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">container_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">error_message</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">error_state</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">error_state_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">gcp_project_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">network_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">peering_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">provider_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">route_table_cidr_block</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vnet_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vpc_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.GetNetworkPeeringResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getNetworkPeering.</p>
<dl class="py method">
<dt id="pulumi_mongodbatlas.GetNetworkPeeringResult.accepter_region_name">
<em class="property">property </em><code class="sig-name descname">accepter_region_name</code><a class="headerlink" href="#pulumi_mongodbatlas.GetNetworkPeeringResult.accepter_region_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the region where the peer VPC resides. For complete lists of supported regions, see <a class="reference external" href="https://docs.atlas.mongodb.com/reference/amazon-aws/">Amazon Web Services</a>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.GetNetworkPeeringResult.atlas_cidr_block">
<em class="property">property </em><code class="sig-name descname">atlas_cidr_block</code><a class="headerlink" href="#pulumi_mongodbatlas.GetNetworkPeeringResult.atlas_cidr_block" title="Permalink to this definition">¶</a></dt>
<dd><p>Unique identifier for an Azure AD directory.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.GetNetworkPeeringResult.aws_account_id">
<em class="property">property </em><code class="sig-name descname">aws_account_id</code><a class="headerlink" href="#pulumi_mongodbatlas.GetNetworkPeeringResult.aws_account_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Account ID of the owner of the peer VPC.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.GetNetworkPeeringResult.azure_directory_id">
<em class="property">property </em><code class="sig-name descname">azure_directory_id</code><a class="headerlink" href="#pulumi_mongodbatlas.GetNetworkPeeringResult.azure_directory_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Unique identifier for an Azure AD directory.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.GetNetworkPeeringResult.azure_subscription_id">
<em class="property">property </em><code class="sig-name descname">azure_subscription_id</code><a class="headerlink" href="#pulumi_mongodbatlas.GetNetworkPeeringResult.azure_subscription_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Unique identifer of the Azure subscription in which the VNet resides.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.GetNetworkPeeringResult.connection_id">
<em class="property">property </em><code class="sig-name descname">connection_id</code><a class="headerlink" href="#pulumi_mongodbatlas.GetNetworkPeeringResult.connection_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Unique identifier for the peering connection.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.GetNetworkPeeringResult.error_message">
<em class="property">property </em><code class="sig-name descname">error_message</code><a class="headerlink" href="#pulumi_mongodbatlas.GetNetworkPeeringResult.error_message" title="Permalink to this definition">¶</a></dt>
<dd><p>When <code class="docutils literal notranslate"><span class="pre">&quot;status&quot;</span> <span class="pre">:</span> <span class="pre">&quot;FAILED&quot;</span></code>, Atlas provides a description of the error.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.GetNetworkPeeringResult.error_state">
<em class="property">property </em><code class="sig-name descname">error_state</code><a class="headerlink" href="#pulumi_mongodbatlas.GetNetworkPeeringResult.error_state" title="Permalink to this definition">¶</a></dt>
<dd><p>Description of the Atlas error when <code class="docutils literal notranslate"><span class="pre">status</span></code> is <code class="docutils literal notranslate"><span class="pre">Failed</span></code>, Otherwise, Atlas returns <code class="docutils literal notranslate"><span class="pre">null</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.GetNetworkPeeringResult.error_state_name">
<em class="property">property </em><code class="sig-name descname">error_state_name</code><a class="headerlink" href="#pulumi_mongodbatlas.GetNetworkPeeringResult.error_state_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Error state, if any. The VPC peering connection error state value can be one of the following: <code class="docutils literal notranslate"><span class="pre">REJECTED</span></code>, <code class="docutils literal notranslate"><span class="pre">EXPIRED</span></code>, <code class="docutils literal notranslate"><span class="pre">INVALID_ARGUMENT</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.GetNetworkPeeringResult.gcp_project_id">
<em class="property">property </em><code class="sig-name descname">gcp_project_id</code><a class="headerlink" href="#pulumi_mongodbatlas.GetNetworkPeeringResult.gcp_project_id" title="Permalink to this definition">¶</a></dt>
<dd><p>GCP project ID of the owner of the network peer.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.GetNetworkPeeringResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_mongodbatlas.GetNetworkPeeringResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.GetNetworkPeeringResult.network_name">
<em class="property">property </em><code class="sig-name descname">network_name</code><a class="headerlink" href="#pulumi_mongodbatlas.GetNetworkPeeringResult.network_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the network peer to which Atlas connects.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.GetNetworkPeeringResult.provider_name">
<em class="property">property </em><code class="sig-name descname">provider_name</code><a class="headerlink" href="#pulumi_mongodbatlas.GetNetworkPeeringResult.provider_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Cloud provider for this VPC peering connection. If omitted, Atlas sets this parameter to AWS. (Possible Values <code class="docutils literal notranslate"><span class="pre">AWS</span></code>, <code class="docutils literal notranslate"><span class="pre">AZURE</span></code>, <code class="docutils literal notranslate"><span class="pre">GCP</span></code>).</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.GetNetworkPeeringResult.resource_group_name">
<em class="property">property </em><code class="sig-name descname">resource_group_name</code><a class="headerlink" href="#pulumi_mongodbatlas.GetNetworkPeeringResult.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of your Azure resource group.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.GetNetworkPeeringResult.route_table_cidr_block">
<em class="property">property </em><code class="sig-name descname">route_table_cidr_block</code><a class="headerlink" href="#pulumi_mongodbatlas.GetNetworkPeeringResult.route_table_cidr_block" title="Permalink to this definition">¶</a></dt>
<dd><p>Peer VPC CIDR block or subnet.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.GetNetworkPeeringResult.status">
<em class="property">property </em><code class="sig-name descname">status</code><a class="headerlink" href="#pulumi_mongodbatlas.GetNetworkPeeringResult.status" title="Permalink to this definition">¶</a></dt>
<dd><p>Status of the Atlas network peering connection: <code class="docutils literal notranslate"><span class="pre">ADDING_PEER</span></code>, <code class="docutils literal notranslate"><span class="pre">AVAILABLE</span></code>, <code class="docutils literal notranslate"><span class="pre">FAILED</span></code>, <code class="docutils literal notranslate"><span class="pre">DELETING</span></code>, <code class="docutils literal notranslate"><span class="pre">WAITING_FOR_USER</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.GetNetworkPeeringResult.status_name">
<em class="property">property </em><code class="sig-name descname">status_name</code><a class="headerlink" href="#pulumi_mongodbatlas.GetNetworkPeeringResult.status_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The VPC peering connection status value can be one of the following: <code class="docutils literal notranslate"><span class="pre">INITIATING</span></code>, <code class="docutils literal notranslate"><span class="pre">PENDING_ACCEPTANCE</span></code>, <code class="docutils literal notranslate"><span class="pre">FAILED</span></code>, <code class="docutils literal notranslate"><span class="pre">FINALIZING</span></code>, <code class="docutils literal notranslate"><span class="pre">AVAILABLE</span></code>, <code class="docutils literal notranslate"><span class="pre">TERMINATING</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.GetNetworkPeeringResult.vnet_name">
<em class="property">property </em><code class="sig-name descname">vnet_name</code><a class="headerlink" href="#pulumi_mongodbatlas.GetNetworkPeeringResult.vnet_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of your Azure VNet.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.GetNetworkPeeringResult.vpc_id">
<em class="property">property </em><code class="sig-name descname">vpc_id</code><a class="headerlink" href="#pulumi_mongodbatlas.GetNetworkPeeringResult.vpc_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Unique identifier of the peer VPC.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_mongodbatlas.GetNetworkPeeringsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">GetNetworkPeeringsResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">results</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.GetNetworkPeeringsResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getNetworkPeerings.</p>
<dl class="py method">
<dt id="pulumi_mongodbatlas.GetNetworkPeeringsResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_mongodbatlas.GetNetworkPeeringsResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.GetNetworkPeeringsResult.results">
<em class="property">property </em><code class="sig-name descname">results</code><a class="headerlink" href="#pulumi_mongodbatlas.GetNetworkPeeringsResult.results" title="Permalink to this definition">¶</a></dt>
<dd><p>A list where each represents a Network Peering Connection.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_mongodbatlas.GetPrivateEndpointInterfaceLinkResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">GetPrivateEndpointInterfaceLinkResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">connection_status</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">delete_requested</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">error_message</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">interface_endpoint_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">private_link_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.GetPrivateEndpointInterfaceLinkResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getPrivateEndpointInterfaceLink.</p>
<dl class="py method">
<dt id="pulumi_mongodbatlas.GetPrivateEndpointInterfaceLinkResult.connection_status">
<em class="property">property </em><code class="sig-name descname">connection_status</code><a class="headerlink" href="#pulumi_mongodbatlas.GetPrivateEndpointInterfaceLinkResult.connection_status" title="Permalink to this definition">¶</a></dt>
<dd><p>Status of the interface endpoint.
Returns one of the following values:</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.GetPrivateEndpointInterfaceLinkResult.delete_requested">
<em class="property">property </em><code class="sig-name descname">delete_requested</code><a class="headerlink" href="#pulumi_mongodbatlas.GetPrivateEndpointInterfaceLinkResult.delete_requested" title="Permalink to this definition">¶</a></dt>
<dd><p>Indicates if Atlas received a request to remove the interface endpoint from the private endpoint connection.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.GetPrivateEndpointInterfaceLinkResult.error_message">
<em class="property">property </em><code class="sig-name descname">error_message</code><a class="headerlink" href="#pulumi_mongodbatlas.GetPrivateEndpointInterfaceLinkResult.error_message" title="Permalink to this definition">¶</a></dt>
<dd><p>Error message pertaining to the interface endpoint. Returns null if there are no errors.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.GetPrivateEndpointInterfaceLinkResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_mongodbatlas.GetPrivateEndpointInterfaceLinkResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_mongodbatlas.GetPrivateEndpointResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">GetPrivateEndpointResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">endpoint_service_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">error_message</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">interface_endpoints</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">private_link_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.GetPrivateEndpointResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getPrivateEndpoint.</p>
<dl class="py method">
<dt id="pulumi_mongodbatlas.GetPrivateEndpointResult.endpoint_service_name">
<em class="property">property </em><code class="sig-name descname">endpoint_service_name</code><a class="headerlink" href="#pulumi_mongodbatlas.GetPrivateEndpointResult.endpoint_service_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the PrivateLink endpoint service in AWS. Returns null while the endpoint service is being created.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.GetPrivateEndpointResult.error_message">
<em class="property">property </em><code class="sig-name descname">error_message</code><a class="headerlink" href="#pulumi_mongodbatlas.GetPrivateEndpointResult.error_message" title="Permalink to this definition">¶</a></dt>
<dd><p>Error message pertaining to the AWS PrivateLink connection. Returns null if there are no errors.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.GetPrivateEndpointResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_mongodbatlas.GetPrivateEndpointResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.GetPrivateEndpointResult.interface_endpoints">
<em class="property">property </em><code class="sig-name descname">interface_endpoints</code><a class="headerlink" href="#pulumi_mongodbatlas.GetPrivateEndpointResult.interface_endpoints" title="Permalink to this definition">¶</a></dt>
<dd><p>Unique identifiers of the interface endpoints in your VPC that you added to the AWS PrivateLink connection.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.GetPrivateEndpointResult.status">
<em class="property">property </em><code class="sig-name descname">status</code><a class="headerlink" href="#pulumi_mongodbatlas.GetPrivateEndpointResult.status" title="Permalink to this definition">¶</a></dt>
<dd><p>Status of the AWS PrivateLink connection.
Returns one of the following values:</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_mongodbatlas.GetPrivateLinkEndpointResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">GetPrivateLinkEndpointResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">endpoint_service_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">error_message</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">interface_endpoints</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">private_endpoints</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">private_link_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">private_link_service_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">private_link_service_resource_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">provider_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.GetPrivateLinkEndpointResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getPrivateLinkEndpoint.</p>
<dl class="py method">
<dt id="pulumi_mongodbatlas.GetPrivateLinkEndpointResult.endpoint_service_name">
<em class="property">property </em><code class="sig-name descname">endpoint_service_name</code><a class="headerlink" href="#pulumi_mongodbatlas.GetPrivateLinkEndpointResult.endpoint_service_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the PrivateLink endpoint service in AWS. Returns null while the endpoint service is being created.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.GetPrivateLinkEndpointResult.error_message">
<em class="property">property </em><code class="sig-name descname">error_message</code><a class="headerlink" href="#pulumi_mongodbatlas.GetPrivateLinkEndpointResult.error_message" title="Permalink to this definition">¶</a></dt>
<dd><p>Error message pertaining to the AWS PrivateLink connection. Returns null if there are no errors.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.GetPrivateLinkEndpointResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_mongodbatlas.GetPrivateLinkEndpointResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.GetPrivateLinkEndpointResult.interface_endpoints">
<em class="property">property </em><code class="sig-name descname">interface_endpoints</code><a class="headerlink" href="#pulumi_mongodbatlas.GetPrivateLinkEndpointResult.interface_endpoints" title="Permalink to this definition">¶</a></dt>
<dd><p>Unique identifiers of the interface endpoints in your VPC that you added to the AWS PrivateLink connection.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.GetPrivateLinkEndpointResult.private_endpoints">
<em class="property">property </em><code class="sig-name descname">private_endpoints</code><a class="headerlink" href="#pulumi_mongodbatlas.GetPrivateLinkEndpointResult.private_endpoints" title="Permalink to this definition">¶</a></dt>
<dd><p>All private endpoints that you have added to this Azure Private Link Service.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.GetPrivateLinkEndpointResult.private_link_service_name">
<em class="property">property </em><code class="sig-name descname">private_link_service_name</code><a class="headerlink" href="#pulumi_mongodbatlas.GetPrivateLinkEndpointResult.private_link_service_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the Azure Private Link Service that Atlas manages.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.GetPrivateLinkEndpointResult.private_link_service_resource_id">
<em class="property">property </em><code class="sig-name descname">private_link_service_resource_id</code><a class="headerlink" href="#pulumi_mongodbatlas.GetPrivateLinkEndpointResult.private_link_service_resource_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Resource ID of the Azure Private Link Service that Atlas manages.
Returns one of the following values:</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.GetPrivateLinkEndpointResult.status">
<em class="property">property </em><code class="sig-name descname">status</code><a class="headerlink" href="#pulumi_mongodbatlas.GetPrivateLinkEndpointResult.status" title="Permalink to this definition">¶</a></dt>
<dd><p>Status of the AWS PrivateLink connection.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_mongodbatlas.GetPrivateLinkEndpointServiceResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">GetPrivateLinkEndpointServiceResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">connection_status</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">delete_requested</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">endpoint_service_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">error_message</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">interface_endpoint_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">private_endpoint_connection_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">private_endpoint_ip_address</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">private_endpoint_resource_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">private_link_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">provider_name</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.GetPrivateLinkEndpointServiceResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getPrivateLinkEndpointService.</p>
<dl class="py method">
<dt id="pulumi_mongodbatlas.GetPrivateLinkEndpointServiceResult.connection_status">
<em class="property">property </em><code class="sig-name descname">connection_status</code><a class="headerlink" href="#pulumi_mongodbatlas.GetPrivateLinkEndpointServiceResult.connection_status" title="Permalink to this definition">¶</a></dt>
<dd><p>Status of the interface endpoint.
Returns one of the following values:</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.GetPrivateLinkEndpointServiceResult.delete_requested">
<em class="property">property </em><code class="sig-name descname">delete_requested</code><a class="headerlink" href="#pulumi_mongodbatlas.GetPrivateLinkEndpointServiceResult.delete_requested" title="Permalink to this definition">¶</a></dt>
<dd><p>Indicates if Atlas received a request to remove the interface endpoint from the private endpoint connection.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.GetPrivateLinkEndpointServiceResult.error_message">
<em class="property">property </em><code class="sig-name descname">error_message</code><a class="headerlink" href="#pulumi_mongodbatlas.GetPrivateLinkEndpointServiceResult.error_message" title="Permalink to this definition">¶</a></dt>
<dd><p>Error message pertaining to the interface endpoint. Returns null if there are no errors.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.GetPrivateLinkEndpointServiceResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_mongodbatlas.GetPrivateLinkEndpointServiceResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.GetPrivateLinkEndpointServiceResult.interface_endpoint_id">
<em class="property">property </em><code class="sig-name descname">interface_endpoint_id</code><a class="headerlink" href="#pulumi_mongodbatlas.GetPrivateLinkEndpointServiceResult.interface_endpoint_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Unique identifier of the interface endpoint.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.GetPrivateLinkEndpointServiceResult.private_endpoint_connection_name">
<em class="property">property </em><code class="sig-name descname">private_endpoint_connection_name</code><a class="headerlink" href="#pulumi_mongodbatlas.GetPrivateLinkEndpointServiceResult.private_endpoint_connection_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the connection for this private endpoint that Atlas generates.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.GetPrivateLinkEndpointServiceResult.private_endpoint_ip_address">
<em class="property">property </em><code class="sig-name descname">private_endpoint_ip_address</code><a class="headerlink" href="#pulumi_mongodbatlas.GetPrivateLinkEndpointServiceResult.private_endpoint_ip_address" title="Permalink to this definition">¶</a></dt>
<dd><p>Private IP address of the private endpoint network interface.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.GetPrivateLinkEndpointServiceResult.private_endpoint_resource_id">
<em class="property">property </em><code class="sig-name descname">private_endpoint_resource_id</code><a class="headerlink" href="#pulumi_mongodbatlas.GetPrivateLinkEndpointServiceResult.private_endpoint_resource_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Unique identifier of the private endpoint.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_mongodbatlas.GetProjectIpAccessListResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">GetProjectIpAccessListResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">aws_security_group</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cidr_block</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">comment</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ip_address</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.GetProjectIpAccessListResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getProjectIpAccessList.</p>
<dl class="py method">
<dt id="pulumi_mongodbatlas.GetProjectIpAccessListResult.comment">
<em class="property">property </em><code class="sig-name descname">comment</code><a class="headerlink" href="#pulumi_mongodbatlas.GetProjectIpAccessListResult.comment" title="Permalink to this definition">¶</a></dt>
<dd><p>Comment to add to the access list entry.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.GetProjectIpAccessListResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_mongodbatlas.GetProjectIpAccessListResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_mongodbatlas.GetProjectIpWhitelistResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">GetProjectIpWhitelistResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">aws_security_group</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cidr_block</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">comment</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ip_address</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.GetProjectIpWhitelistResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getProjectIpWhitelist.</p>
<dl class="py method">
<dt id="pulumi_mongodbatlas.GetProjectIpWhitelistResult.comment">
<em class="property">property </em><code class="sig-name descname">comment</code><a class="headerlink" href="#pulumi_mongodbatlas.GetProjectIpWhitelistResult.comment" title="Permalink to this definition">¶</a></dt>
<dd><p>Comment to add to the whitelist entry.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.GetProjectIpWhitelistResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_mongodbatlas.GetProjectIpWhitelistResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_mongodbatlas.GetProjectResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">GetProjectResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">cluster_count</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">created</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">org_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">teams</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.GetProjectResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getProject.</p>
<dl class="py method">
<dt id="pulumi_mongodbatlas.GetProjectResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_mongodbatlas.GetProjectResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.GetProjectResult.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_mongodbatlas.GetProjectResult.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the project you want to create. (Cannot be changed via this Provider after creation.)</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.GetProjectResult.org_id">
<em class="property">property </em><code class="sig-name descname">org_id</code><a class="headerlink" href="#pulumi_mongodbatlas.GetProjectResult.org_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the organization you want to create the project within.
<em>``cluster_count`` - The number of Atlas clusters deployed in the project.</em><code class="docutils literal notranslate"><span class="pre">created</span></code> - The ISO-8601-formatted timestamp of when Atlas created the project.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">teams.#.team_id</span></code> - The unique identifier of the team you want to associate with the project. The team and project must share the same parent organization.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">teams.#.role_names</span></code> - Each string in the array represents a project role assigned to the team. Every user associated with the team inherits these roles.
The following are valid roles:</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">GROUP_OWNER</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">GROUP_READ_ONLY</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">GROUP_DATA_ACCESS_ADMIN</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">GROUP_DATA_ACCESS_READ_WRITE</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">GROUP_DATA_ACCESS_READ_ONLY</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">GROUP_CLUSTER_MANAGER</span></code></p></li>
</ul>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_mongodbatlas.GetProjectsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">GetProjectsResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">items_per_page</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">page_num</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">results</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">total_count</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.GetProjectsResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getProjects.</p>
<dl class="py method">
<dt id="pulumi_mongodbatlas.GetProjectsResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_mongodbatlas.GetProjectsResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_mongodbatlas.GetTeamResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">GetTeamResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">org_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">team_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">usernames</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.GetTeamResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getTeam.</p>
<dl class="py method">
<dt id="pulumi_mongodbatlas.GetTeamResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_mongodbatlas.GetTeamResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.GetTeamResult.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_mongodbatlas.GetTeamResult.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the team you want to create.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.GetTeamResult.team_id">
<em class="property">property </em><code class="sig-name descname">team_id</code><a class="headerlink" href="#pulumi_mongodbatlas.GetTeamResult.team_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The unique identifier for the team.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.GetTeamResult.usernames">
<em class="property">property </em><code class="sig-name descname">usernames</code><a class="headerlink" href="#pulumi_mongodbatlas.GetTeamResult.usernames" title="Permalink to this definition">¶</a></dt>
<dd><p>The users who are part of the organization.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_mongodbatlas.GetTeamsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">GetTeamsResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">org_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">team_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">usernames</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.GetTeamsResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getTeams.</p>
<dl class="py method">
<dt id="pulumi_mongodbatlas.GetTeamsResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_mongodbatlas.GetTeamsResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_mongodbatlas.GetThirdPartyIntegrationResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">GetThirdPartyIntegrationResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">account_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">api_key</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">api_token</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">channel_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">flow_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">license_key</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">org_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">read_token</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">region</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">routing_key</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">secret</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_key</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">team_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">url</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">write_token</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.GetThirdPartyIntegrationResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getThirdPartyIntegration.</p>
<dl class="py method">
<dt id="pulumi_mongodbatlas.GetThirdPartyIntegrationResult.account_id">
<em class="property">property </em><code class="sig-name descname">account_id</code><a class="headerlink" href="#pulumi_mongodbatlas.GetThirdPartyIntegrationResult.account_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Unique identifier of your New Relic account.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.GetThirdPartyIntegrationResult.api_key">
<em class="property">property </em><code class="sig-name descname">api_key</code><a class="headerlink" href="#pulumi_mongodbatlas.GetThirdPartyIntegrationResult.api_key" title="Permalink to this definition">¶</a></dt>
<dd><p>Your API Key.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.GetThirdPartyIntegrationResult.api_token">
<em class="property">property </em><code class="sig-name descname">api_token</code><a class="headerlink" href="#pulumi_mongodbatlas.GetThirdPartyIntegrationResult.api_token" title="Permalink to this definition">¶</a></dt>
<dd><p>Your API Token.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.GetThirdPartyIntegrationResult.flow_name">
<em class="property">property </em><code class="sig-name descname">flow_name</code><a class="headerlink" href="#pulumi_mongodbatlas.GetThirdPartyIntegrationResult.flow_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Your Flowdock Flow name.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.GetThirdPartyIntegrationResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_mongodbatlas.GetThirdPartyIntegrationResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.GetThirdPartyIntegrationResult.license_key">
<em class="property">property </em><code class="sig-name descname">license_key</code><a class="headerlink" href="#pulumi_mongodbatlas.GetThirdPartyIntegrationResult.license_key" title="Permalink to this definition">¶</a></dt>
<dd><p>Your License Key.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.GetThirdPartyIntegrationResult.org_name">
<em class="property">property </em><code class="sig-name descname">org_name</code><a class="headerlink" href="#pulumi_mongodbatlas.GetThirdPartyIntegrationResult.org_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Your Flowdock organization name.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">WEBHOOK</span></code></p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.GetThirdPartyIntegrationResult.read_token">
<em class="property">property </em><code class="sig-name descname">read_token</code><a class="headerlink" href="#pulumi_mongodbatlas.GetThirdPartyIntegrationResult.read_token" title="Permalink to this definition">¶</a></dt>
<dd><p>Your Insights Query Key.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">OPS_GENIE</span></code></p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.GetThirdPartyIntegrationResult.region">
<em class="property">property </em><code class="sig-name descname">region</code><a class="headerlink" href="#pulumi_mongodbatlas.GetThirdPartyIntegrationResult.region" title="Permalink to this definition">¶</a></dt>
<dd><p>Indicates which API URL to use, either US or EU. Opsgenie will use US by default.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">VICTOR_OPS</span></code></p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.GetThirdPartyIntegrationResult.routing_key">
<em class="property">property </em><code class="sig-name descname">routing_key</code><a class="headerlink" href="#pulumi_mongodbatlas.GetThirdPartyIntegrationResult.routing_key" title="Permalink to this definition">¶</a></dt>
<dd><p>An optional field for your Routing Key.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">FLOWDOCK</span></code></p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.GetThirdPartyIntegrationResult.secret">
<em class="property">property </em><code class="sig-name descname">secret</code><a class="headerlink" href="#pulumi_mongodbatlas.GetThirdPartyIntegrationResult.secret" title="Permalink to this definition">¶</a></dt>
<dd><p>An optional field for your webhook secret.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.GetThirdPartyIntegrationResult.service_key">
<em class="property">property </em><code class="sig-name descname">service_key</code><a class="headerlink" href="#pulumi_mongodbatlas.GetThirdPartyIntegrationResult.service_key" title="Permalink to this definition">¶</a></dt>
<dd><p>Your Service Key.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">DATADOG</span></code></p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.GetThirdPartyIntegrationResult.type">
<em class="property">property </em><code class="sig-name descname">type</code><a class="headerlink" href="#pulumi_mongodbatlas.GetThirdPartyIntegrationResult.type" title="Permalink to this definition">¶</a></dt>
<dd><p>Property equal to its own integration type</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.GetThirdPartyIntegrationResult.url">
<em class="property">property </em><code class="sig-name descname">url</code><a class="headerlink" href="#pulumi_mongodbatlas.GetThirdPartyIntegrationResult.url" title="Permalink to this definition">¶</a></dt>
<dd><p>Your webhook URL.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.GetThirdPartyIntegrationResult.write_token">
<em class="property">property </em><code class="sig-name descname">write_token</code><a class="headerlink" href="#pulumi_mongodbatlas.GetThirdPartyIntegrationResult.write_token" title="Permalink to this definition">¶</a></dt>
<dd><p>Your Insights Insert Key.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_mongodbatlas.GetThirdPartyIntegrationsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">GetThirdPartyIntegrationsResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">results</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.GetThirdPartyIntegrationsResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getThirdPartyIntegrations.</p>
<dl class="py method">
<dt id="pulumi_mongodbatlas.GetThirdPartyIntegrationsResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_mongodbatlas.GetThirdPartyIntegrationsResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.GetThirdPartyIntegrationsResult.project_id">
<em class="property">property </em><code class="sig-name descname">project_id</code><a class="headerlink" href="#pulumi_mongodbatlas.GetThirdPartyIntegrationsResult.project_id" title="Permalink to this definition">¶</a></dt>
<dd><p>(Required) ID of the Atlas project the Third-Party Service Integration belongs to.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.GetThirdPartyIntegrationsResult.results">
<em class="property">property </em><code class="sig-name descname">results</code><a class="headerlink" href="#pulumi_mongodbatlas.GetThirdPartyIntegrationsResult.results" title="Permalink to this definition">¶</a></dt>
<dd><p>A list where each represents a Third-Party service integration.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_mongodbatlas.GlobalClusterConfig">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">GlobalClusterConfig</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cluster_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_zone_mappings</span><span class="p">:</span> <span class="n">Union[Sequence[Union[GlobalClusterConfigCustomZoneMappingArgs, Mapping[str, Any], Awaitable[Union[GlobalClusterConfigCustomZoneMappingArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[GlobalClusterConfigCustomZoneMappingArgs, Mapping[str, Any], Awaitable[Union[GlobalClusterConfigCustomZoneMappingArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">managed_namespaces</span><span class="p">:</span> <span class="n">Union[Sequence[Union[GlobalClusterConfigManagedNamespaceArgs, Mapping[str, Any], Awaitable[Union[GlobalClusterConfigManagedNamespaceArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[GlobalClusterConfigManagedNamespaceArgs, Mapping[str, Any], Awaitable[Union[GlobalClusterConfigManagedNamespaceArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.GlobalClusterConfig" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">GlobalClusterConfig</span></code> provides a Global Cluster Configuration resource.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Groups and projects are synonymous terms. You may find group_id in the official documentation.</p>
</div></blockquote>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_mongodbatlas</span> <span class="k">as</span> <span class="nn">mongodbatlas</span>

<span class="n">test</span> <span class="o">=</span> <span class="n">mongodbatlas</span><span class="o">.</span><span class="n">Cluster</span><span class="p">(</span><span class="s2">&quot;test&quot;</span><span class="p">,</span>
    <span class="n">project_id</span><span class="o">=</span><span class="s2">&quot;&lt;YOUR-PROJECT-ID&gt;&quot;</span><span class="p">,</span>
    <span class="n">disk_size_gb</span><span class="o">=</span><span class="mi">80</span><span class="p">,</span>
    <span class="n">backup_enabled</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span>
    <span class="n">provider_backup_enabled</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="n">cluster_type</span><span class="o">=</span><span class="s2">&quot;GEOSHARDED&quot;</span><span class="p">,</span>
    <span class="n">provider_name</span><span class="o">=</span><span class="s2">&quot;AWS&quot;</span><span class="p">,</span>
    <span class="n">provider_disk_iops</span><span class="o">=</span><span class="mi">240</span><span class="p">,</span>
    <span class="n">provider_instance_size_name</span><span class="o">=</span><span class="s2">&quot;M30&quot;</span><span class="p">,</span>
    <span class="n">replication_specs</span><span class="o">=</span><span class="p">[</span>
        <span class="n">mongodbatlas</span><span class="o">.</span><span class="n">ClusterReplicationSpecArgs</span><span class="p">(</span>
            <span class="n">zone_name</span><span class="o">=</span><span class="s2">&quot;Zone 1&quot;</span><span class="p">,</span>
            <span class="n">num_shards</span><span class="o">=</span><span class="mi">1</span><span class="p">,</span>
            <span class="n">regions_configs</span><span class="o">=</span><span class="p">[</span><span class="n">mongodbatlas</span><span class="o">.</span><span class="n">ClusterReplicationSpecRegionsConfigArgs</span><span class="p">(</span>
                <span class="n">region_name</span><span class="o">=</span><span class="s2">&quot;EU_CENTRAL_1&quot;</span><span class="p">,</span>
                <span class="n">electable_nodes</span><span class="o">=</span><span class="mi">3</span><span class="p">,</span>
                <span class="n">priority</span><span class="o">=</span><span class="mi">7</span><span class="p">,</span>
                <span class="n">read_only_nodes</span><span class="o">=</span><span class="mi">0</span><span class="p">,</span>
            <span class="p">)],</span>
        <span class="p">),</span>
        <span class="n">mongodbatlas</span><span class="o">.</span><span class="n">ClusterReplicationSpecArgs</span><span class="p">(</span>
            <span class="n">zone_name</span><span class="o">=</span><span class="s2">&quot;Zone 2&quot;</span><span class="p">,</span>
            <span class="n">num_shards</span><span class="o">=</span><span class="mi">1</span><span class="p">,</span>
            <span class="n">regions_configs</span><span class="o">=</span><span class="p">[</span><span class="n">mongodbatlas</span><span class="o">.</span><span class="n">ClusterReplicationSpecRegionsConfigArgs</span><span class="p">(</span>
                <span class="n">region_name</span><span class="o">=</span><span class="s2">&quot;US_EAST_2&quot;</span><span class="p">,</span>
                <span class="n">electable_nodes</span><span class="o">=</span><span class="mi">3</span><span class="p">,</span>
                <span class="n">priority</span><span class="o">=</span><span class="mi">7</span><span class="p">,</span>
                <span class="n">read_only_nodes</span><span class="o">=</span><span class="mi">0</span><span class="p">,</span>
            <span class="p">)],</span>
        <span class="p">),</span>
    <span class="p">])</span>
<span class="n">config</span> <span class="o">=</span> <span class="n">mongodbatlas</span><span class="o">.</span><span class="n">GlobalClusterConfig</span><span class="p">(</span><span class="s2">&quot;config&quot;</span><span class="p">,</span>
    <span class="n">project_id</span><span class="o">=</span><span class="n">test</span><span class="o">.</span><span class="n">project_id</span><span class="p">,</span>
    <span class="n">cluster_name</span><span class="o">=</span><span class="n">test</span><span class="o">.</span><span class="n">name</span><span class="p">,</span>
    <span class="n">managed_namespaces</span><span class="o">=</span><span class="p">[</span><span class="n">mongodbatlas</span><span class="o">.</span><span class="n">GlobalClusterConfigManagedNamespaceArgs</span><span class="p">(</span>
        <span class="n">db</span><span class="o">=</span><span class="s2">&quot;mydata&quot;</span><span class="p">,</span>
        <span class="n">collection</span><span class="o">=</span><span class="s2">&quot;publishers&quot;</span><span class="p">,</span>
        <span class="n">custom_shard_key</span><span class="o">=</span><span class="s2">&quot;city&quot;</span><span class="p">,</span>
    <span class="p">)],</span>
    <span class="n">custom_zone_mappings</span><span class="o">=</span><span class="p">[</span><span class="n">mongodbatlas</span><span class="o">.</span><span class="n">GlobalClusterConfigCustomZoneMappingArgs</span><span class="p">(</span>
        <span class="n">location</span><span class="o">=</span><span class="s2">&quot;CA&quot;</span><span class="p">,</span>
        <span class="n">zone</span><span class="o">=</span><span class="s2">&quot;Zone 1&quot;</span><span class="p">,</span>
    <span class="p">)])</span>
</pre></div>
</div>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_mongodbatlas</span> <span class="k">as</span> <span class="nn">mongodbatlas</span>

<span class="n">cluster_test</span> <span class="o">=</span> <span class="n">mongodbatlas</span><span class="o">.</span><span class="n">Cluster</span><span class="p">(</span><span class="s2">&quot;cluster-test&quot;</span><span class="p">,</span>
    <span class="n">project_id</span><span class="o">=</span><span class="s2">&quot;&lt;YOUR-PROJECT-ID&gt;&quot;</span><span class="p">,</span>
    <span class="n">num_shards</span><span class="o">=</span><span class="mi">1</span><span class="p">,</span>
    <span class="n">replication_factor</span><span class="o">=</span><span class="mi">3</span><span class="p">,</span>
    <span class="n">backup_enabled</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="n">auto_scaling_disk_gb_enabled</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="n">mongo_db_major_version</span><span class="o">=</span><span class="s2">&quot;4.0&quot;</span><span class="p">,</span>
    <span class="n">provider_name</span><span class="o">=</span><span class="s2">&quot;AWS&quot;</span><span class="p">,</span>
    <span class="n">disk_size_gb</span><span class="o">=</span><span class="mi">100</span><span class="p">,</span>
    <span class="n">provider_disk_iops</span><span class="o">=</span><span class="mi">300</span><span class="p">,</span>
    <span class="n">provider_encrypt_ebs_volume</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span>
    <span class="n">provider_instance_size_name</span><span class="o">=</span><span class="s2">&quot;M40&quot;</span><span class="p">,</span>
    <span class="n">provider_region_name</span><span class="o">=</span><span class="s2">&quot;US_EAST_1&quot;</span><span class="p">)</span>
<span class="n">config</span> <span class="o">=</span> <span class="n">mongodbatlas</span><span class="o">.</span><span class="n">GlobalClusterConfig</span><span class="p">(</span><span class="s2">&quot;config&quot;</span><span class="p">,</span>
    <span class="n">project_id</span><span class="o">=</span><span class="n">mongodbatlas_cluster</span><span class="p">[</span><span class="s2">&quot;test&quot;</span><span class="p">][</span><span class="s2">&quot;project_id&quot;</span><span class="p">],</span>
    <span class="n">cluster_name</span><span class="o">=</span><span class="n">mongodbatlas_cluster</span><span class="p">[</span><span class="s2">&quot;test&quot;</span><span class="p">][</span><span class="s2">&quot;name&quot;</span><span class="p">],</span>
    <span class="n">managed_namespaces</span><span class="o">=</span><span class="p">[</span><span class="n">mongodbatlas</span><span class="o">.</span><span class="n">GlobalClusterConfigManagedNamespaceArgs</span><span class="p">(</span>
        <span class="n">db</span><span class="o">=</span><span class="s2">&quot;mydata&quot;</span><span class="p">,</span>
        <span class="n">collection</span><span class="o">=</span><span class="s2">&quot;publishers&quot;</span><span class="p">,</span>
        <span class="n">custom_shard_key</span><span class="o">=</span><span class="s2">&quot;city&quot;</span><span class="p">,</span>
    <span class="p">)],</span>
    <span class="n">custom_zone_mappings</span><span class="o">=</span><span class="p">[</span><span class="n">mongodbatlas</span><span class="o">.</span><span class="n">GlobalClusterConfigCustomZoneMappingArgs</span><span class="p">(</span>
        <span class="n">location</span><span class="o">=</span><span class="s2">&quot;CA&quot;</span><span class="p">,</span>
        <span class="n">zone</span><span class="o">=</span><span class="s2">&quot;Zone 1&quot;</span><span class="p">,</span>
    <span class="p">)])</span>
</pre></div>
</div>
<p>Database users can be imported using project ID and cluster name, in the format <code class="docutils literal notranslate"><span class="pre">PROJECTID-CLUSTER_NAME</span></code>, e.g.</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>   $ pulumi import mongodbatlas:index/globalClusterConfig:GlobalClusterConfig config 1112222b3bf99403840e8934-my-cluster

See detailed information <span class="k">for</span> arguments and attributes<span class="se">\ </span><span class="sb">`</span>MongoDB API Global Clusters &lt;https://docs.atlas.mongodb.com/reference/api/global-clusters/&gt;<span class="sb">`</span>_
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>custom_zone_mappings</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'GlobalClusterConfigCustomZoneMappingArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – Each element in the list maps one ISO location code to a zone in your Global Cluster. See Custom Zone Mapping below for more details.</p></li>
<li><p><strong>managed_namespaces</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'GlobalClusterConfigManagedNamespaceArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – <p>Add a managed namespaces to a Global Cluster. For more information about managed namespaces, see <a class="reference external" href="https://docs.atlas.mongodb.com/reference/api/global-clusters/">Global Clusters</a>. See Managed Namespace below for more details.</p>
</p></li>
<li><p><strong>project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique ID for the project to create the database user.</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>* `cluster_name - (Required) The name of the Global Cluster.
</pre></div>
</div>
<dl class="py method">
<dt id="pulumi_mongodbatlas.GlobalClusterConfig.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cluster_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_zone_mapping</span><span class="p">:</span> <span class="n">Union[Mapping[str, Any], Awaitable[Mapping[str, Any]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">custom_zone_mappings</span><span class="p">:</span> <span class="n">Union[Sequence[Union[GlobalClusterConfigCustomZoneMappingArgs, Mapping[str, Any], Awaitable[Union[GlobalClusterConfigCustomZoneMappingArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[GlobalClusterConfigCustomZoneMappingArgs, Mapping[str, Any], Awaitable[Union[GlobalClusterConfigCustomZoneMappingArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">managed_namespaces</span><span class="p">:</span> <span class="n">Union[Sequence[Union[GlobalClusterConfigManagedNamespaceArgs, Mapping[str, Any], Awaitable[Union[GlobalClusterConfigManagedNamespaceArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[GlobalClusterConfigManagedNamespaceArgs, Mapping[str, Any], Awaitable[Union[GlobalClusterConfigManagedNamespaceArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_mongodbatlas.global_cluster_config.GlobalClusterConfig<a class="headerlink" href="#pulumi_mongodbatlas.GlobalClusterConfig.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing GlobalClusterConfig resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>Any</strong><strong>]</strong><strong>] </strong><strong>custom_zone_mapping</strong> (<em>pulumi.Input</em><em>[</em><em>Mapping</em><em>[</em><em>str</em><em>,</em>) – A map of all custom zone mappings defined for the Global Cluster. Atlas automatically maps each location code to the closest geographical zone. Custom zone mappings allow administrators to override these automatic mappings. If your Global Cluster does not have any custom zone mappings, this document is empty.</p></li>
<li><p><strong>custom_zone_mappings</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'GlobalClusterConfigCustomZoneMappingArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – Each element in the list maps one ISO location code to a zone in your Global Cluster. See Custom Zone Mapping below for more details.</p></li>
<li><p><strong>managed_namespaces</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'GlobalClusterConfigManagedNamespaceArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – <p>Add a managed namespaces to a Global Cluster. For more information about managed namespaces, see <a class="reference external" href="https://docs.atlas.mongodb.com/reference/api/global-clusters/">Global Clusters</a>. See Managed Namespace below for more details.</p>
</p></li>
<li><p><strong>project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique ID for the project to create the database user.</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>* `cluster_name - (Required) The name of the Global Cluster.
</pre></div>
</div>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.GlobalClusterConfig.custom_zone_mapping">
<em class="property">property </em><code class="sig-name descname">custom_zone_mapping</code><a class="headerlink" href="#pulumi_mongodbatlas.GlobalClusterConfig.custom_zone_mapping" title="Permalink to this definition">¶</a></dt>
<dd><p>A map of all custom zone mappings defined for the Global Cluster. Atlas automatically maps each location code to the closest geographical zone. Custom zone mappings allow administrators to override these automatic mappings. If your Global Cluster does not have any custom zone mappings, this document is empty.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.GlobalClusterConfig.custom_zone_mappings">
<em class="property">property </em><code class="sig-name descname">custom_zone_mappings</code><a class="headerlink" href="#pulumi_mongodbatlas.GlobalClusterConfig.custom_zone_mappings" title="Permalink to this definition">¶</a></dt>
<dd><p>Each element in the list maps one ISO location code to a zone in your Global Cluster. See Custom Zone Mapping below for more details.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.GlobalClusterConfig.managed_namespaces">
<em class="property">property </em><code class="sig-name descname">managed_namespaces</code><a class="headerlink" href="#pulumi_mongodbatlas.GlobalClusterConfig.managed_namespaces" title="Permalink to this definition">¶</a></dt>
<dd><p>Add a managed namespaces to a Global Cluster. For more information about managed namespaces, see <a class="reference external" href="https://docs.atlas.mongodb.com/reference/api/global-clusters/">Global Clusters</a>. See Managed Namespace below for more details.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.GlobalClusterConfig.project_id">
<em class="property">property </em><code class="sig-name descname">project_id</code><a class="headerlink" href="#pulumi_mongodbatlas.GlobalClusterConfig.project_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The unique ID for the project to create the database user.</p>
<ul class="simple">
<li><p><a href="#id25"><span class="problematic" id="id26">`</span></a>cluster_name - (Required) The name of the Global Cluster.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.GlobalClusterConfig.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.GlobalClusterConfig.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_mongodbatlas.GlobalClusterConfig.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.GlobalClusterConfig.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py class">
<dt id="pulumi_mongodbatlas.MaintenanceWindow">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">MaintenanceWindow</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">day_of_week</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">defer</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">hour_of_day</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">number_of_deferrals</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.MaintenanceWindow" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">MaintenanceWindow</span></code> provides a resource to schedule a maintenance window for your MongoDB Atlas Project and/or set to defer a scheduled maintenance up to two times.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Groups and projects are synonymous terms. You may find <code class="docutils literal notranslate"><span class="pre">groupId</span></code> in the official documentation.</p>
</div></blockquote>
<ul class="simple">
<li><p>Urgent Maintenance Activities Cannot Wait: Urgent maintenance activities such as security patches cannot wait for your chosen window. Atlas will start those maintenance activities when needed.</p></li>
</ul>
<p>Once maintenance is scheduled for your cluster, you cannot change your maintenance window until the current maintenance efforts have completed.</p>
<ul class="simple">
<li><p>Maintenance Requires Replica Set Elections: Atlas performs maintenance the same way as the manual maintenance procedure. This requires at least one replica set election during the maintenance window per replica set.</p></li>
<li><p>Maintenance Starts As Close to the Hour As Possible: Maintenance always begins as close to the scheduled hour as possible, but in-progress cluster updates or expected system issues could delay the start time.</p></li>
</ul>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_mongodbatlas</span> <span class="k">as</span> <span class="nn">mongodbatlas</span>

<span class="n">test</span> <span class="o">=</span> <span class="n">mongodbatlas</span><span class="o">.</span><span class="n">MaintenanceWindow</span><span class="p">(</span><span class="s2">&quot;test&quot;</span><span class="p">,</span>
    <span class="n">day_of_week</span><span class="o">=</span><span class="mi">3</span><span class="p">,</span>
    <span class="n">hour_of_day</span><span class="o">=</span><span class="mi">4</span><span class="p">,</span>
    <span class="n">project_id</span><span class="o">=</span><span class="s2">&quot;&lt;your-project-id&gt;&quot;</span><span class="p">)</span>
</pre></div>
</div>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_mongodbatlas</span> <span class="k">as</span> <span class="nn">mongodbatlas</span>

<span class="n">test</span> <span class="o">=</span> <span class="n">mongodbatlas</span><span class="o">.</span><span class="n">MaintenanceWindow</span><span class="p">(</span><span class="s2">&quot;test&quot;</span><span class="p">,</span>
    <span class="n">defer</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="n">project_id</span><span class="o">=</span><span class="s2">&quot;&lt;your-project-id&gt;&quot;</span><span class="p">)</span>
</pre></div>
</div>
<p>Maintenance Window entries can be imported using project project_id, in the format <code class="docutils literal notranslate"><span class="pre">PROJECTID</span></code>, e.g.</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>   $ pulumi import mongodbatlas:index/maintenanceWindow:MaintenanceWindow <span class="nb">test</span> 5d0f1f73cf09a29120e173cf

For more information see<span class="se">\ </span><span class="sb">`</span>MongoDB Atlas API Reference. &lt;https://docs.atlas.mongodb.com/reference/api/maintenance-windows/&gt;<span class="sb">`</span>_
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>day_of_week</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Day of the week when you would like the maintenance window to start as a 1-based integer: S=1, M=2, T=3, W=4, T=5, F=6, S=7.</p></li>
<li><p><strong>defer</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Defer maintenance for the given project for one week.</p></li>
<li><p><strong>hour_of_day</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Hour of the day when you would like the maintenance window to start. This parameter uses the 24-hour clock, where midnight is 0, noon is 12 (Time zone is UTC).</p></li>
<li><p><strong>number_of_deferrals</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Number of times the current maintenance event for this project has been deferred, you can set a maximum of 2 deferrals.</p></li>
<li><p><strong>project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique identifier of the project for the Maintenance Window.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_mongodbatlas.MaintenanceWindow.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">day_of_week</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">defer</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">hour_of_day</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">number_of_deferrals</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">start_asap</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_mongodbatlas.maintenance_window.MaintenanceWindow<a class="headerlink" href="#pulumi_mongodbatlas.MaintenanceWindow.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing MaintenanceWindow resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>day_of_week</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Day of the week when you would like the maintenance window to start as a 1-based integer: S=1, M=2, T=3, W=4, T=5, F=6, S=7.</p></li>
<li><p><strong>defer</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Defer maintenance for the given project for one week.</p></li>
<li><p><strong>hour_of_day</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Hour of the day when you would like the maintenance window to start. This parameter uses the 24-hour clock, where midnight is 0, noon is 12 (Time zone is UTC).</p></li>
<li><p><strong>number_of_deferrals</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Number of times the current maintenance event for this project has been deferred, you can set a maximum of 2 deferrals.</p></li>
<li><p><strong>project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique identifier of the project for the Maintenance Window.</p></li>
<li><p><strong>start_asap</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Flag indicating whether project maintenance has been directed to start immediately. If you request that maintenance begin immediately, this field returns true from the time the request was made until the time the maintenance event completes.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.MaintenanceWindow.day_of_week">
<em class="property">property </em><code class="sig-name descname">day_of_week</code><a class="headerlink" href="#pulumi_mongodbatlas.MaintenanceWindow.day_of_week" title="Permalink to this definition">¶</a></dt>
<dd><p>Day of the week when you would like the maintenance window to start as a 1-based integer: S=1, M=2, T=3, W=4, T=5, F=6, S=7.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.MaintenanceWindow.defer">
<em class="property">property </em><code class="sig-name descname">defer</code><a class="headerlink" href="#pulumi_mongodbatlas.MaintenanceWindow.defer" title="Permalink to this definition">¶</a></dt>
<dd><p>Defer maintenance for the given project for one week.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.MaintenanceWindow.hour_of_day">
<em class="property">property </em><code class="sig-name descname">hour_of_day</code><a class="headerlink" href="#pulumi_mongodbatlas.MaintenanceWindow.hour_of_day" title="Permalink to this definition">¶</a></dt>
<dd><p>Hour of the day when you would like the maintenance window to start. This parameter uses the 24-hour clock, where midnight is 0, noon is 12 (Time zone is UTC).</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.MaintenanceWindow.number_of_deferrals">
<em class="property">property </em><code class="sig-name descname">number_of_deferrals</code><a class="headerlink" href="#pulumi_mongodbatlas.MaintenanceWindow.number_of_deferrals" title="Permalink to this definition">¶</a></dt>
<dd><p>Number of times the current maintenance event for this project has been deferred, you can set a maximum of 2 deferrals.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.MaintenanceWindow.project_id">
<em class="property">property </em><code class="sig-name descname">project_id</code><a class="headerlink" href="#pulumi_mongodbatlas.MaintenanceWindow.project_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The unique identifier of the project for the Maintenance Window.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.MaintenanceWindow.start_asap">
<em class="property">property </em><code class="sig-name descname">start_asap</code><a class="headerlink" href="#pulumi_mongodbatlas.MaintenanceWindow.start_asap" title="Permalink to this definition">¶</a></dt>
<dd><p>Flag indicating whether project maintenance has been directed to start immediately. If you request that maintenance begin immediately, this field returns true from the time the request was made until the time the maintenance event completes.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.MaintenanceWindow.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.MaintenanceWindow.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_mongodbatlas.MaintenanceWindow.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.MaintenanceWindow.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py class">
<dt id="pulumi_mongodbatlas.NetworkContainer">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">NetworkContainer</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">atlas_cidr_block</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">provider_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">region</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">region_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.NetworkContainer" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">NetworkContainer</span></code> provides a Network Peering Container resource. The resource lets you create, edit and delete network peering containers. The resource requires your Project ID.  Each cloud provider requires slightly different attributes so read the argument reference carefully.</p>
<blockquote>
<div><p>Network peering container is a general term used to describe any cloud providers’ VPC/VNet concept.  Containers only need to be created if the peering connection to the cloud provider will be created before the first cluster that requires the container.  If the cluster has been/will be created first Atlas automatically creates the required container per the “containers per cloud provider” information that follows (in this case you can obtain the container id from the cluster resource attribute <code class="docutils literal notranslate"><span class="pre">container_id</span></code>).</p>
</div></blockquote>
<p>The following is the maximum number of Network Peering containers per cloud provider:
<span class="raw-html-m2r"><br></span> &amp;#8226;  GCP -  One container per project.
<span class="raw-html-m2r"><br></span> &amp;#8226;  AWS and Azure - One container per cloud provider region.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Groups and projects are synonymous terms. You may find <strong>group_id</strong> in the official documentation.</p>
</div></blockquote>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_mongodbatlas</span> <span class="k">as</span> <span class="nn">mongodbatlas</span>

<span class="n">test</span> <span class="o">=</span> <span class="n">mongodbatlas</span><span class="o">.</span><span class="n">NetworkContainer</span><span class="p">(</span><span class="s2">&quot;test&quot;</span><span class="p">,</span>
    <span class="n">atlas_cidr_block</span><span class="o">=</span><span class="s2">&quot;10.8.0.0/21&quot;</span><span class="p">,</span>
    <span class="n">project_id</span><span class="o">=</span><span class="s2">&quot;&lt;YOUR-PROJECT-ID&gt;&quot;</span><span class="p">,</span>
    <span class="n">provider_name</span><span class="o">=</span><span class="s2">&quot;AWS&quot;</span><span class="p">,</span>
    <span class="n">region_name</span><span class="o">=</span><span class="s2">&quot;US_EAST_1&quot;</span><span class="p">)</span>
</pre></div>
</div>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_mongodbatlas</span> <span class="k">as</span> <span class="nn">mongodbatlas</span>

<span class="n">test</span> <span class="o">=</span> <span class="n">mongodbatlas</span><span class="o">.</span><span class="n">NetworkContainer</span><span class="p">(</span><span class="s2">&quot;test&quot;</span><span class="p">,</span>
    <span class="n">atlas_cidr_block</span><span class="o">=</span><span class="s2">&quot;10.8.0.0/21&quot;</span><span class="p">,</span>
    <span class="n">project_id</span><span class="o">=</span><span class="s2">&quot;&lt;YOUR-PROJECT-ID&gt;&quot;</span><span class="p">,</span>
    <span class="n">provider_name</span><span class="o">=</span><span class="s2">&quot;GCP&quot;</span><span class="p">)</span>
</pre></div>
</div>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_mongodbatlas</span> <span class="k">as</span> <span class="nn">mongodbatlas</span>

<span class="n">test</span> <span class="o">=</span> <span class="n">mongodbatlas</span><span class="o">.</span><span class="n">NetworkContainer</span><span class="p">(</span><span class="s2">&quot;test&quot;</span><span class="p">,</span>
    <span class="n">atlas_cidr_block</span><span class="o">=</span><span class="s2">&quot;10.8.0.0/21&quot;</span><span class="p">,</span>
    <span class="n">project_id</span><span class="o">=</span><span class="s2">&quot;&lt;YOUR-PROJECT-ID&gt;&quot;</span><span class="p">,</span>
    <span class="n">provider_name</span><span class="o">=</span><span class="s2">&quot;AZURE&quot;</span><span class="p">,</span>
    <span class="n">region</span><span class="o">=</span><span class="s2">&quot;US_EAST_2&quot;</span><span class="p">)</span>
</pre></div>
</div>
<p>Clusters can be imported using project ID and network peering container id, in the format <code class="docutils literal notranslate"><span class="pre">PROJECTID-CONTAINER-ID</span></code>, e.g.</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>   $ pulumi import mongodbatlas:index/networkContainer:NetworkContainer my_container 1112222b3bf99403840e8934-5cbf563d87d9d67253be590a

See detailed information <span class="k">for</span> arguments and attributes<span class="se">\ </span><span class="sb">`</span>MongoDB API Network Peering Container &lt;https://docs.atlas.mongodb.com/reference/api/vpc-create-container/&gt;<span class="sb">`</span>_
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>atlas_cidr_block</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>CIDR block that Atlas uses for the Network Peering containers in your project.  Atlas uses the specified CIDR block for all other Network Peering connections created in the project. The Atlas CIDR block must be at least a /24 and at most a /21 in one of the following <a class="reference external" href="https://tools.ietf.org/html/rfc1918.html#section-3">private networks</a>:</p>
</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="o">*</span> <span class="n">Lower</span> <span class="n">bound</span><span class="p">:</span> <span class="mf">10.0</span><span class="o">.</span><span class="mf">0.0</span> <span class="o">-</span>        <span class="n">Upper</span> <span class="n">bound</span><span class="p">:</span> <span class="mf">10.255</span><span class="o">.</span><span class="mf">255.255</span> <span class="o">-</span>   <span class="n">Prefix</span><span class="p">:</span> <span class="mi">10</span><span class="o">/</span><span class="mi">8</span>
<span class="o">*</span> <span class="n">Lower</span> <span class="n">bound</span><span class="p">:</span> <span class="mf">172.16</span><span class="o">.</span><span class="mf">0.0</span> <span class="o">-</span>      <span class="n">Upper</span> <span class="n">bound</span><span class="p">:</span><span class="mf">172.31</span><span class="o">.</span><span class="mf">255.255</span> <span class="o">-</span>    <span class="n">Prefix</span><span class="p">:</span> <span class="mf">172.16</span><span class="o">/</span><span class="mi">12</span>
<span class="o">*</span> <span class="n">Lower</span> <span class="n">bound</span><span class="p">:</span> <span class="mf">192.168</span><span class="o">.</span><span class="mf">0.0</span> <span class="o">-</span>     <span class="n">Upper</span> <span class="n">bound</span><span class="p">:</span><span class="mf">192.168</span><span class="o">.</span><span class="mf">255.255</span> <span class="o">-</span>   <span class="n">Prefix</span><span class="p">:</span> <span class="mf">192.168</span><span class="o">/</span><span class="mi">16</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Unique identifier for the Atlas project for this Network Peering Container.</p></li>
<li><p><strong>provider_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Cloud provider for this Network Peering connection.  Accepted values are GCP, AWS, AZURE. If omitted, Atlas sets this parameter to AWS.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>Atlas region where the container resides, see the reference list for Atlas Azure region names <a class="reference external" href="https://docs.atlas.mongodb.com/reference/microsoft-azure/">Azure</a>.</p>
</p></li>
<li><p><strong>region_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The Atlas AWS region name for where this container will exist, see the reference list for Atlas AWS region names <a class="reference external" href="https://docs.atlas.mongodb.com/reference/amazon-aws/">AWS</a>.</p>
</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_mongodbatlas.NetworkContainer.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">atlas_cidr_block</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">azure_subscription_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">container_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">gcp_project_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">network_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">provider_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">provisioned</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">region</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">region_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vnet_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vpc_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_mongodbatlas.network_container.NetworkContainer<a class="headerlink" href="#pulumi_mongodbatlas.NetworkContainer.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing NetworkContainer resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>atlas_cidr_block</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>CIDR block that Atlas uses for the Network Peering containers in your project.  Atlas uses the specified CIDR block for all other Network Peering connections created in the project. The Atlas CIDR block must be at least a /24 and at most a /21 in one of the following <a class="reference external" href="https://tools.ietf.org/html/rfc1918.html#section-3">private networks</a>:</p>
</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="o">*</span> <span class="n">Lower</span> <span class="n">bound</span><span class="p">:</span> <span class="mf">10.0</span><span class="o">.</span><span class="mf">0.0</span> <span class="o">-</span>        <span class="n">Upper</span> <span class="n">bound</span><span class="p">:</span> <span class="mf">10.255</span><span class="o">.</span><span class="mf">255.255</span> <span class="o">-</span>   <span class="n">Prefix</span><span class="p">:</span> <span class="mi">10</span><span class="o">/</span><span class="mi">8</span>
<span class="o">*</span> <span class="n">Lower</span> <span class="n">bound</span><span class="p">:</span> <span class="mf">172.16</span><span class="o">.</span><span class="mf">0.0</span> <span class="o">-</span>      <span class="n">Upper</span> <span class="n">bound</span><span class="p">:</span><span class="mf">172.31</span><span class="o">.</span><span class="mf">255.255</span> <span class="o">-</span>    <span class="n">Prefix</span><span class="p">:</span> <span class="mf">172.16</span><span class="o">/</span><span class="mi">12</span>
<span class="o">*</span> <span class="n">Lower</span> <span class="n">bound</span><span class="p">:</span> <span class="mf">192.168</span><span class="o">.</span><span class="mf">0.0</span> <span class="o">-</span>     <span class="n">Upper</span> <span class="n">bound</span><span class="p">:</span><span class="mf">192.168</span><span class="o">.</span><span class="mf">255.255</span> <span class="o">-</span>   <span class="n">Prefix</span><span class="p">:</span> <span class="mf">192.168</span><span class="o">/</span><span class="mi">16</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>azure_subscription_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Unique identifier of the Azure subscription in which the VNet resides.</p>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>* * `vnet_name` -        The name of the Azure VNet. Returns null. This value is populated once you create a new network peering connection with the network peering resource.
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>container_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Network Peering Container ID.</p></li>
<li><p><strong>gcp_project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Unique identifier of the GCP project in which the network peer resides. Returns null. This value is populated once you create a new network peering connection with the network peering resource.</p></li>
<li><p><strong>network_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Unique identifier of the Network Peering connection in the Atlas project. Returns null. This value is populated once you create a new network peering connection with the network peering resource.
<strong>AZURE ONLY:</strong></p></li>
<li><p><strong>project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Unique identifier for the Atlas project for this Network Peering Container.</p></li>
<li><p><strong>provider_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Cloud provider for this Network Peering connection.  Accepted values are GCP, AWS, AZURE. If omitted, Atlas sets this parameter to AWS.</p></li>
<li><p><strong>provisioned</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Indicates whether the project has Network Peering connections deployed in the container.
<strong>AWS ONLY:</strong></p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>Atlas region where the container resides, see the reference list for Atlas Azure region names <a class="reference external" href="https://docs.atlas.mongodb.com/reference/microsoft-azure/">Azure</a>.</p>
</p></li>
<li><p><strong>region_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The Atlas AWS region name for where this container will exist, see the reference list for Atlas AWS region names <a class="reference external" href="https://docs.atlas.mongodb.com/reference/amazon-aws/">AWS</a>.</p>
</p></li>
<li><p><strong>vpc_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Unique identifier of Atlas’ AWS VPC.
<strong>CGP ONLY:</strong></p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.NetworkContainer.atlas_cidr_block">
<em class="property">property </em><code class="sig-name descname">atlas_cidr_block</code><a class="headerlink" href="#pulumi_mongodbatlas.NetworkContainer.atlas_cidr_block" title="Permalink to this definition">¶</a></dt>
<dd><p>CIDR block that Atlas uses for the Network Peering containers in your project.  Atlas uses the specified CIDR block for all other Network Peering connections created in the project. The Atlas CIDR block must be at least a /24 and at most a /21 in one of the following <a class="reference external" href="https://tools.ietf.org/html/rfc1918.html#section-3">private networks</a>:</p>
<ul class="simple">
<li><p>Lower bound: 10.0.0.0 -       Upper bound: 10.255.255.255 -   Prefix: 10/8</p></li>
<li><p>Lower bound: 172.16.0.0 -     Upper bound:172.31.255.255 -    Prefix: 172.16/12</p></li>
<li><p>Lower bound: 192.168.0.0 -    Upper bound:192.168.255.255 -   Prefix: 192.168/16</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.NetworkContainer.azure_subscription_id">
<em class="property">property </em><code class="sig-name descname">azure_subscription_id</code><a class="headerlink" href="#pulumi_mongodbatlas.NetworkContainer.azure_subscription_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Unique identifier of the Azure subscription in which the VNet resides.</p>
<ul class="simple">
<li><ul>
<li><p><code class="docutils literal notranslate"><span class="pre">vnet_name</span></code> -       The name of the Azure VNet. Returns null. This value is populated once you create a new network peering connection with the network peering resource.</p></li>
</ul>
</li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.NetworkContainer.container_id">
<em class="property">property </em><code class="sig-name descname">container_id</code><a class="headerlink" href="#pulumi_mongodbatlas.NetworkContainer.container_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The Network Peering Container ID.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.NetworkContainer.gcp_project_id">
<em class="property">property </em><code class="sig-name descname">gcp_project_id</code><a class="headerlink" href="#pulumi_mongodbatlas.NetworkContainer.gcp_project_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Unique identifier of the GCP project in which the network peer resides. Returns null. This value is populated once you create a new network peering connection with the network peering resource.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.NetworkContainer.network_name">
<em class="property">property </em><code class="sig-name descname">network_name</code><a class="headerlink" href="#pulumi_mongodbatlas.NetworkContainer.network_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Unique identifier of the Network Peering connection in the Atlas project. Returns null. This value is populated once you create a new network peering connection with the network peering resource.
<strong>AZURE ONLY:</strong></p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.NetworkContainer.project_id">
<em class="property">property </em><code class="sig-name descname">project_id</code><a class="headerlink" href="#pulumi_mongodbatlas.NetworkContainer.project_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Unique identifier for the Atlas project for this Network Peering Container.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.NetworkContainer.provider_name">
<em class="property">property </em><code class="sig-name descname">provider_name</code><a class="headerlink" href="#pulumi_mongodbatlas.NetworkContainer.provider_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Cloud provider for this Network Peering connection.  Accepted values are GCP, AWS, AZURE. If omitted, Atlas sets this parameter to AWS.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.NetworkContainer.provisioned">
<em class="property">property </em><code class="sig-name descname">provisioned</code><a class="headerlink" href="#pulumi_mongodbatlas.NetworkContainer.provisioned" title="Permalink to this definition">¶</a></dt>
<dd><p>Indicates whether the project has Network Peering connections deployed in the container.
<strong>AWS ONLY:</strong></p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.NetworkContainer.region">
<em class="property">property </em><code class="sig-name descname">region</code><a class="headerlink" href="#pulumi_mongodbatlas.NetworkContainer.region" title="Permalink to this definition">¶</a></dt>
<dd><p>Atlas region where the container resides, see the reference list for Atlas Azure region names <a class="reference external" href="https://docs.atlas.mongodb.com/reference/microsoft-azure/">Azure</a>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.NetworkContainer.region_name">
<em class="property">property </em><code class="sig-name descname">region_name</code><a class="headerlink" href="#pulumi_mongodbatlas.NetworkContainer.region_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The Atlas AWS region name for where this container will exist, see the reference list for Atlas AWS region names <a class="reference external" href="https://docs.atlas.mongodb.com/reference/amazon-aws/">AWS</a>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.NetworkContainer.vpc_id">
<em class="property">property </em><code class="sig-name descname">vpc_id</code><a class="headerlink" href="#pulumi_mongodbatlas.NetworkContainer.vpc_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Unique identifier of Atlas’ AWS VPC.
<strong>CGP ONLY:</strong></p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.NetworkContainer.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.NetworkContainer.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_mongodbatlas.NetworkContainer.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.NetworkContainer.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py class">
<dt id="pulumi_mongodbatlas.NetworkPeering">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">NetworkPeering</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">accepter_region_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">atlas_cidr_block</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">atlas_gcp_project_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">atlas_vpc_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">aws_account_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">azure_directory_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">azure_subscription_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">container_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">gcp_project_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">network_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">provider_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">route_table_cidr_block</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vnet_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vpc_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.NetworkPeering" title="Permalink to this definition">¶</a></dt>
<dd><p>Clusters can be imported using project ID and network peering peering id, in the format <code class="docutils literal notranslate"><span class="pre">PROJECTID-PEERID-PROVIDERNAME</span></code>, e.g.</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>   $ pulumi import mongodbatlas:index/networkPeering:NetworkPeering my_peering 1112222b3bf99403840e8934-5cbf563d87d9d67253be590a-AWS

See detailed information <span class="k">for</span> arguments and attributes<span class="se">\ </span><span class="sb">`</span>MongoDB API Network Peering Connection &lt;https://docs.atlas.mongodb.com/reference/api/vpc-create-peering-connection/&gt;<span class="sb">`</span>_
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>accepter_region_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>Specifies the AWS region where the peer VPC resides. For complete lists of supported regions, see <a class="reference external" href="https://docs.atlas.mongodb.com/reference/amazon-aws/">Amazon Web Services</a>.</p>
</p></li>
<li><p><strong>atlas_gcp_project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Atlas GCP Project ID for the GCP VPC used by your atlas cluster that it is need to set up the reciprocal connection.</p></li>
<li><p><strong>aws_account_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – AWS Account ID of the owner of the peer VPC.</p></li>
<li><p><strong>azure_directory_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Unique identifier for an Azure AD directory.</p></li>
<li><p><strong>azure_subscription_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Unique identifier of the Azure subscription in which the VNet resides.</p></li>
<li><p><strong>container_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Unique identifier of the MongoDB Atlas container for the provider (GCP) or provider/region (AWS, AZURE). You can create an MongoDB Atlas container using the network_container resource or it can be obtained from the cluster returned values if a cluster has been created before the first container.</p></li>
<li><p><strong>gcp_project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – GCP project ID of the owner of the network peer.</p></li>
<li><p><strong>network_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the network peer to which Atlas connects.</p></li>
<li><p><strong>project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique ID for the MongoDB Atlas project to create the database user.</p></li>
<li><p><strong>provider_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Cloud provider to whom the peering connection is being made. (Possible Values <code class="docutils literal notranslate"><span class="pre">AWS</span></code>, <code class="docutils literal notranslate"><span class="pre">AZURE</span></code>, <code class="docutils literal notranslate"><span class="pre">GCP</span></code>).</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of your Azure resource group.</p></li>
<li><p><strong>route_table_cidr_block</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – AWS VPC CIDR block or subnet.</p></li>
<li><p><strong>vnet_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of your Azure VNet.</p></li>
<li><p><strong>vpc_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Unique identifier of the AWS peer VPC (Note: this is <strong>not</strong> the same as the Atlas AWS VPC that is returned by the network_container resource).</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_mongodbatlas.NetworkPeering.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">accepter_region_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">atlas_cidr_block</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">atlas_gcp_project_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">atlas_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">atlas_vpc_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">aws_account_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">azure_directory_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">azure_subscription_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">connection_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">container_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">error_message</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">error_state</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">error_state_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">gcp_project_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">network_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">peer_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">provider_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">route_table_cidr_block</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vnet_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">vpc_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_mongodbatlas.network_peering.NetworkPeering<a class="headerlink" href="#pulumi_mongodbatlas.NetworkPeering.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing NetworkPeering resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>accepter_region_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>Specifies the AWS region where the peer VPC resides. For complete lists of supported regions, see <a class="reference external" href="https://docs.atlas.mongodb.com/reference/amazon-aws/">Amazon Web Services</a>.</p>
</p></li>
<li><p><strong>atlas_gcp_project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Atlas GCP Project ID for the GCP VPC used by your atlas cluster that it is need to set up the reciprocal connection.</p></li>
<li><p><strong>aws_account_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – AWS Account ID of the owner of the peer VPC.</p></li>
<li><p><strong>azure_directory_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Unique identifier for an Azure AD directory.</p></li>
<li><p><strong>azure_subscription_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Unique identifier of the Azure subscription in which the VNet resides.</p></li>
<li><p><strong>connection_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Unique identifier of the Atlas network peering container.</p></li>
<li><p><strong>container_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Unique identifier of the MongoDB Atlas container for the provider (GCP) or provider/region (AWS, AZURE). You can create an MongoDB Atlas container using the network_container resource or it can be obtained from the cluster returned values if a cluster has been created before the first container.</p></li>
<li><p><strong>error_message</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – When <code class="docutils literal notranslate"><span class="pre">&quot;status&quot;</span> <span class="pre">:</span> <span class="pre">&quot;FAILED&quot;</span></code>, Atlas provides a description of the error.</p></li>
<li><p><strong>error_state</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Description of the Atlas error when <code class="docutils literal notranslate"><span class="pre">status</span></code> is <code class="docutils literal notranslate"><span class="pre">Failed</span></code>, Otherwise, Atlas returns <code class="docutils literal notranslate"><span class="pre">null</span></code>.</p></li>
<li><p><strong>error_state_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Error state, if any. The VPC peering connection error state value can be one of the following: <code class="docutils literal notranslate"><span class="pre">REJECTED</span></code>, <code class="docutils literal notranslate"><span class="pre">EXPIRED</span></code>, <code class="docutils literal notranslate"><span class="pre">INVALID_ARGUMENT</span></code>.</p></li>
<li><p><strong>gcp_project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – GCP project ID of the owner of the network peer.</p></li>
<li><p><strong>network_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the network peer to which Atlas connects.</p></li>
<li><p><strong>peer_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Unique identifier of the Atlas network peer.</p></li>
<li><p><strong>project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique ID for the MongoDB Atlas project to create the database user.</p></li>
<li><p><strong>provider_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Cloud provider to whom the peering connection is being made. (Possible Values <code class="docutils literal notranslate"><span class="pre">AWS</span></code>, <code class="docutils literal notranslate"><span class="pre">AZURE</span></code>, <code class="docutils literal notranslate"><span class="pre">GCP</span></code>).</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of your Azure resource group.</p></li>
<li><p><strong>route_table_cidr_block</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – AWS VPC CIDR block or subnet.</p></li>
<li><p><strong>status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Status of the Atlas network peering connection.  Azure/GCP: <code class="docutils literal notranslate"><span class="pre">ADDING_PEER</span></code>, <code class="docutils literal notranslate"><span class="pre">AVAILABLE</span></code>, <code class="docutils literal notranslate"><span class="pre">FAILED</span></code>, <code class="docutils literal notranslate"><span class="pre">DELETING</span></code> GCP Only:  <code class="docutils literal notranslate"><span class="pre">WAITING_FOR_USER</span></code>.</p></li>
<li><p><strong>status_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – (AWS Only) The VPC peering connection status value can be one of the following: <code class="docutils literal notranslate"><span class="pre">INITIATING</span></code>, <code class="docutils literal notranslate"><span class="pre">PENDING_ACCEPTANCE</span></code>, <code class="docutils literal notranslate"><span class="pre">FAILED</span></code>, <code class="docutils literal notranslate"><span class="pre">FINALIZING</span></code>, <code class="docutils literal notranslate"><span class="pre">AVAILABLE</span></code>, <code class="docutils literal notranslate"><span class="pre">TERMINATING</span></code>.</p></li>
<li><p><strong>vnet_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of your Azure VNet.</p></li>
<li><p><strong>vpc_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Unique identifier of the AWS peer VPC (Note: this is <strong>not</strong> the same as the Atlas AWS VPC that is returned by the network_container resource).</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.NetworkPeering.accepter_region_name">
<em class="property">property </em><code class="sig-name descname">accepter_region_name</code><a class="headerlink" href="#pulumi_mongodbatlas.NetworkPeering.accepter_region_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the AWS region where the peer VPC resides. For complete lists of supported regions, see <a class="reference external" href="https://docs.atlas.mongodb.com/reference/amazon-aws/">Amazon Web Services</a>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.NetworkPeering.atlas_gcp_project_id">
<em class="property">property </em><code class="sig-name descname">atlas_gcp_project_id</code><a class="headerlink" href="#pulumi_mongodbatlas.NetworkPeering.atlas_gcp_project_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The Atlas GCP Project ID for the GCP VPC used by your atlas cluster that it is need to set up the reciprocal connection.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.NetworkPeering.aws_account_id">
<em class="property">property </em><code class="sig-name descname">aws_account_id</code><a class="headerlink" href="#pulumi_mongodbatlas.NetworkPeering.aws_account_id" title="Permalink to this definition">¶</a></dt>
<dd><p>AWS Account ID of the owner of the peer VPC.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.NetworkPeering.azure_directory_id">
<em class="property">property </em><code class="sig-name descname">azure_directory_id</code><a class="headerlink" href="#pulumi_mongodbatlas.NetworkPeering.azure_directory_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Unique identifier for an Azure AD directory.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.NetworkPeering.azure_subscription_id">
<em class="property">property </em><code class="sig-name descname">azure_subscription_id</code><a class="headerlink" href="#pulumi_mongodbatlas.NetworkPeering.azure_subscription_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Unique identifier of the Azure subscription in which the VNet resides.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.NetworkPeering.connection_id">
<em class="property">property </em><code class="sig-name descname">connection_id</code><a class="headerlink" href="#pulumi_mongodbatlas.NetworkPeering.connection_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Unique identifier of the Atlas network peering container.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.NetworkPeering.container_id">
<em class="property">property </em><code class="sig-name descname">container_id</code><a class="headerlink" href="#pulumi_mongodbatlas.NetworkPeering.container_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Unique identifier of the MongoDB Atlas container for the provider (GCP) or provider/region (AWS, AZURE). You can create an MongoDB Atlas container using the network_container resource or it can be obtained from the cluster returned values if a cluster has been created before the first container.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.NetworkPeering.error_message">
<em class="property">property </em><code class="sig-name descname">error_message</code><a class="headerlink" href="#pulumi_mongodbatlas.NetworkPeering.error_message" title="Permalink to this definition">¶</a></dt>
<dd><p>When <code class="docutils literal notranslate"><span class="pre">&quot;status&quot;</span> <span class="pre">:</span> <span class="pre">&quot;FAILED&quot;</span></code>, Atlas provides a description of the error.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.NetworkPeering.error_state">
<em class="property">property </em><code class="sig-name descname">error_state</code><a class="headerlink" href="#pulumi_mongodbatlas.NetworkPeering.error_state" title="Permalink to this definition">¶</a></dt>
<dd><p>Description of the Atlas error when <code class="docutils literal notranslate"><span class="pre">status</span></code> is <code class="docutils literal notranslate"><span class="pre">Failed</span></code>, Otherwise, Atlas returns <code class="docutils literal notranslate"><span class="pre">null</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.NetworkPeering.error_state_name">
<em class="property">property </em><code class="sig-name descname">error_state_name</code><a class="headerlink" href="#pulumi_mongodbatlas.NetworkPeering.error_state_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Error state, if any. The VPC peering connection error state value can be one of the following: <code class="docutils literal notranslate"><span class="pre">REJECTED</span></code>, <code class="docutils literal notranslate"><span class="pre">EXPIRED</span></code>, <code class="docutils literal notranslate"><span class="pre">INVALID_ARGUMENT</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.NetworkPeering.gcp_project_id">
<em class="property">property </em><code class="sig-name descname">gcp_project_id</code><a class="headerlink" href="#pulumi_mongodbatlas.NetworkPeering.gcp_project_id" title="Permalink to this definition">¶</a></dt>
<dd><p>GCP project ID of the owner of the network peer.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.NetworkPeering.network_name">
<em class="property">property </em><code class="sig-name descname">network_name</code><a class="headerlink" href="#pulumi_mongodbatlas.NetworkPeering.network_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the network peer to which Atlas connects.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.NetworkPeering.peer_id">
<em class="property">property </em><code class="sig-name descname">peer_id</code><a class="headerlink" href="#pulumi_mongodbatlas.NetworkPeering.peer_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Unique identifier of the Atlas network peer.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.NetworkPeering.project_id">
<em class="property">property </em><code class="sig-name descname">project_id</code><a class="headerlink" href="#pulumi_mongodbatlas.NetworkPeering.project_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The unique ID for the MongoDB Atlas project to create the database user.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.NetworkPeering.provider_name">
<em class="property">property </em><code class="sig-name descname">provider_name</code><a class="headerlink" href="#pulumi_mongodbatlas.NetworkPeering.provider_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Cloud provider to whom the peering connection is being made. (Possible Values <code class="docutils literal notranslate"><span class="pre">AWS</span></code>, <code class="docutils literal notranslate"><span class="pre">AZURE</span></code>, <code class="docutils literal notranslate"><span class="pre">GCP</span></code>).</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.NetworkPeering.resource_group_name">
<em class="property">property </em><code class="sig-name descname">resource_group_name</code><a class="headerlink" href="#pulumi_mongodbatlas.NetworkPeering.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of your Azure resource group.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.NetworkPeering.route_table_cidr_block">
<em class="property">property </em><code class="sig-name descname">route_table_cidr_block</code><a class="headerlink" href="#pulumi_mongodbatlas.NetworkPeering.route_table_cidr_block" title="Permalink to this definition">¶</a></dt>
<dd><p>AWS VPC CIDR block or subnet.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.NetworkPeering.status">
<em class="property">property </em><code class="sig-name descname">status</code><a class="headerlink" href="#pulumi_mongodbatlas.NetworkPeering.status" title="Permalink to this definition">¶</a></dt>
<dd><p>Status of the Atlas network peering connection.  Azure/GCP: <code class="docutils literal notranslate"><span class="pre">ADDING_PEER</span></code>, <code class="docutils literal notranslate"><span class="pre">AVAILABLE</span></code>, <code class="docutils literal notranslate"><span class="pre">FAILED</span></code>, <code class="docutils literal notranslate"><span class="pre">DELETING</span></code> GCP Only:  <code class="docutils literal notranslate"><span class="pre">WAITING_FOR_USER</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.NetworkPeering.status_name">
<em class="property">property </em><code class="sig-name descname">status_name</code><a class="headerlink" href="#pulumi_mongodbatlas.NetworkPeering.status_name" title="Permalink to this definition">¶</a></dt>
<dd><p>(AWS Only) The VPC peering connection status value can be one of the following: <code class="docutils literal notranslate"><span class="pre">INITIATING</span></code>, <code class="docutils literal notranslate"><span class="pre">PENDING_ACCEPTANCE</span></code>, <code class="docutils literal notranslate"><span class="pre">FAILED</span></code>, <code class="docutils literal notranslate"><span class="pre">FINALIZING</span></code>, <code class="docutils literal notranslate"><span class="pre">AVAILABLE</span></code>, <code class="docutils literal notranslate"><span class="pre">TERMINATING</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.NetworkPeering.vnet_name">
<em class="property">property </em><code class="sig-name descname">vnet_name</code><a class="headerlink" href="#pulumi_mongodbatlas.NetworkPeering.vnet_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of your Azure VNet.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.NetworkPeering.vpc_id">
<em class="property">property </em><code class="sig-name descname">vpc_id</code><a class="headerlink" href="#pulumi_mongodbatlas.NetworkPeering.vpc_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Unique identifier of the AWS peer VPC (Note: this is <strong>not</strong> the same as the Atlas AWS VPC that is returned by the network_container resource).</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.NetworkPeering.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.NetworkPeering.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_mongodbatlas.NetworkPeering.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.NetworkPeering.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py class">
<dt id="pulumi_mongodbatlas.PrivateEndpoint">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">PrivateEndpoint</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">provider_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">region</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.PrivateEndpoint" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">PrivateEndpoint</span></code> provides a Private Endpoint resource. This represents a Private Endpoint Connection that can be created in an Atlas project.</p>
<dl class="simple">
<dt>!&gt; <strong>WARNING:</strong> This resource is deprecated and will be removed in the next major version</dt><dd><p>Please transition to privatelink_endpoint as soon as possible. [PrivateLink Endpoints] (<a class="reference external" href="https://docs.atlas.mongodb.com/reference/api/private-endpoints/">https://docs.atlas.mongodb.com/reference/api/private-endpoints/</a>)</p>
</dd>
</dl>
<blockquote>
<div><p><strong>IMPORTANT:</strong>You must have one of the following roles to successfully handle the resource:</p>
<ul class="simple">
<li><p>Organization Owner</p></li>
<li><p>Project Owner</p></li>
</ul>
<p><strong>NOTE:</strong> Groups and projects are synonymous terms. You may find group_id in the official documentation.</p>
<p><strong>NOTE:</strong> A network container is created for a private endpoint to reside in if one does not yet exist in the project.</p>
</div></blockquote>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_mongodbatlas</span> <span class="k">as</span> <span class="nn">mongodbatlas</span>

<span class="n">test</span> <span class="o">=</span> <span class="n">mongodbatlas</span><span class="o">.</span><span class="n">PrivateEndpoint</span><span class="p">(</span><span class="s2">&quot;test&quot;</span><span class="p">,</span>
    <span class="n">project_id</span><span class="o">=</span><span class="s2">&quot;&lt;PROJECT-ID&gt;&quot;</span><span class="p">,</span>
    <span class="n">provider_name</span><span class="o">=</span><span class="s2">&quot;AWS&quot;</span><span class="p">,</span>
    <span class="n">region</span><span class="o">=</span><span class="s2">&quot;us-east-1&quot;</span><span class="p">)</span>
</pre></div>
</div>
<p>Private Endpoint Connection can be imported using project ID and username, in the format <code class="docutils literal notranslate"><span class="pre">{project_id}-{private_link_id}</span></code>, e.g.</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>   $ pulumi import mongodbatlas:index/privateEndpoint:PrivateEndpoint <span class="nb">test</span> 1112222b3bf99403840e8934-3242342343112

See detailed information <span class="k">for</span> arguments and attributes<span class="se">\ </span><span class="sb">`</span>MongoDB API Private Endpoint Connection &lt;https://docs.atlas.mongodb.com/reference/api/private-endpoint-create-one-private-endpoint-connection/&gt;<span class="sb">`</span>_
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Required   Unique identifier for the project.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Cloud provider region in which you want to create the private endpoint connection.
Accepted values are:</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>* `us-east-1`
* `us-east-2`
* `us-west-1`
* `us-west-2`
* `ca-central-1`
* `sa-east-1`
* `eu-north-1`
* `eu-west-1`
* `eu-west-2`
* `eu-west-3`
* `eu-central-1`
* `me-south-1`
* `ap-northeast-1`
* `ap-northeast-2`
* `ap-south-1`
* `ap-southeast-1`
* `ap-southeast-2`
* `ap-east-1`
</pre></div>
</div>
<dl class="py method">
<dt id="pulumi_mongodbatlas.PrivateEndpoint.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">endpoint_service_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">error_message</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">interface_endpoints</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">private_link_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">provider_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">region</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_mongodbatlas.private_endpoint.PrivateEndpoint<a class="headerlink" href="#pulumi_mongodbatlas.PrivateEndpoint.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing PrivateEndpoint resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>endpoint_service_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the PrivateLink endpoint service in AWS. Returns null while the endpoint service is being created.</p></li>
<li><p><strong>error_message</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Error message pertaining to the AWS PrivateLink connection. Returns null if there are no errors.</p></li>
<li><p><strong>interface_endpoints</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – Unique identifiers of the interface endpoints in your VPC that you added to the AWS PrivateLink connection.</p></li>
<li><p><strong>private_link_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Unique identifier of the AWS PrivateLink connection.</p></li>
<li><p><strong>project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Required   Unique identifier for the project.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Cloud provider region in which you want to create the private endpoint connection.
Accepted values are:</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>* `us-east-1`
* `us-east-2`
* `us-west-1`
* `us-west-2`
* `ca-central-1`
* `sa-east-1`
* `eu-north-1`
* `eu-west-1`
* `eu-west-2`
* `eu-west-3`
* `eu-central-1`
* `me-south-1`
* `ap-northeast-1`
* `ap-northeast-2`
* `ap-south-1`
* `ap-southeast-1`
* `ap-southeast-2`
* `ap-east-1`
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Status of the AWS PrivateLink connection.
Returns one of the following values:</p>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.PrivateEndpoint.endpoint_service_name">
<em class="property">property </em><code class="sig-name descname">endpoint_service_name</code><a class="headerlink" href="#pulumi_mongodbatlas.PrivateEndpoint.endpoint_service_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the PrivateLink endpoint service in AWS. Returns null while the endpoint service is being created.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.PrivateEndpoint.error_message">
<em class="property">property </em><code class="sig-name descname">error_message</code><a class="headerlink" href="#pulumi_mongodbatlas.PrivateEndpoint.error_message" title="Permalink to this definition">¶</a></dt>
<dd><p>Error message pertaining to the AWS PrivateLink connection. Returns null if there are no errors.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.PrivateEndpoint.interface_endpoints">
<em class="property">property </em><code class="sig-name descname">interface_endpoints</code><a class="headerlink" href="#pulumi_mongodbatlas.PrivateEndpoint.interface_endpoints" title="Permalink to this definition">¶</a></dt>
<dd><p>Unique identifiers of the interface endpoints in your VPC that you added to the AWS PrivateLink connection.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.PrivateEndpoint.private_link_id">
<em class="property">property </em><code class="sig-name descname">private_link_id</code><a class="headerlink" href="#pulumi_mongodbatlas.PrivateEndpoint.private_link_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Unique identifier of the AWS PrivateLink connection.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.PrivateEndpoint.project_id">
<em class="property">property </em><code class="sig-name descname">project_id</code><a class="headerlink" href="#pulumi_mongodbatlas.PrivateEndpoint.project_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Required        Unique identifier for the project.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.PrivateEndpoint.region">
<em class="property">property </em><code class="sig-name descname">region</code><a class="headerlink" href="#pulumi_mongodbatlas.PrivateEndpoint.region" title="Permalink to this definition">¶</a></dt>
<dd><p>Cloud provider region in which you want to create the private endpoint connection.
Accepted values are:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">us-east-1</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">us-east-2</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">us-west-1</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">us-west-2</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ca-central-1</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sa-east-1</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">eu-north-1</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">eu-west-1</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">eu-west-2</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">eu-west-3</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">eu-central-1</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">me-south-1</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ap-northeast-1</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ap-northeast-2</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ap-south-1</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ap-southeast-1</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ap-southeast-2</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ap-east-1</span></code></p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.PrivateEndpoint.status">
<em class="property">property </em><code class="sig-name descname">status</code><a class="headerlink" href="#pulumi_mongodbatlas.PrivateEndpoint.status" title="Permalink to this definition">¶</a></dt>
<dd><p>Status of the AWS PrivateLink connection.
Returns one of the following values:</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.PrivateEndpoint.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.PrivateEndpoint.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_mongodbatlas.PrivateEndpoint.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.PrivateEndpoint.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py class">
<dt id="pulumi_mongodbatlas.PrivateEndpointInterfaceLink">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">PrivateEndpointInterfaceLink</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">interface_endpoint_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">private_link_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.PrivateEndpointInterfaceLink" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">PrivateEndpointInterfaceLink</span></code> provides a Private Endpoint Interface Link resource. This represents a Private Endpoint Interface Link, which adds one interface endpoint to a private endpoint connection in an Atlas project.</p>
<dl class="simple">
<dt>!&gt; <strong>WARNING:</strong> This resource is deprecated and will be removed in the next major version</dt><dd><p>Please transition to privatelink_endpoint_service as soon as possible. [PrivateLink Endpoints] (<a class="reference external" href="https://docs.atlas.mongodb.com/reference/api/private-endpoints-endpoint-create-one/">https://docs.atlas.mongodb.com/reference/api/private-endpoints-endpoint-create-one/</a>)</p>
</dd>
</dl>
<blockquote>
<div><p><strong>IMPORTANT:</strong>You must have one of the following roles to successfully handle the resource:</p>
<ul class="simple">
<li><p>Organization Owner</p></li>
<li><p>Project Owner</p></li>
</ul>
<p><strong>NOTE:</strong> Groups and projects are synonymous terms. You may find group_id in the official documentation.</p>
</div></blockquote>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_aws</span> <span class="k">as</span> <span class="nn">aws</span>
<span class="kn">import</span> <span class="nn">pulumi_mongodbatlas</span> <span class="k">as</span> <span class="nn">mongodbatlas</span>

<span class="n">test_private_endpoint</span> <span class="o">=</span> <span class="n">mongodbatlas</span><span class="o">.</span><span class="n">PrivateEndpoint</span><span class="p">(</span><span class="s2">&quot;testPrivateEndpoint&quot;</span><span class="p">,</span>
    <span class="n">project_id</span><span class="o">=</span><span class="s2">&quot;&lt;PROJECT_ID&gt;&quot;</span><span class="p">,</span>
    <span class="n">provider_name</span><span class="o">=</span><span class="s2">&quot;AWS&quot;</span><span class="p">,</span>
    <span class="n">region</span><span class="o">=</span><span class="s2">&quot;us-east-1&quot;</span><span class="p">)</span>
<span class="n">ptfe_service</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">ec2</span><span class="o">.</span><span class="n">VpcEndpoint</span><span class="p">(</span><span class="s2">&quot;ptfeService&quot;</span><span class="p">,</span>
    <span class="n">security_group_ids</span><span class="o">=</span><span class="p">[</span><span class="s2">&quot;sg-3f238186&quot;</span><span class="p">],</span>
    <span class="n">service_name</span><span class="o">=</span><span class="n">test_private_endpoint</span><span class="o">.</span><span class="n">endpoint_service_name</span><span class="p">,</span>
    <span class="n">subnet_ids</span><span class="o">=</span><span class="p">[</span><span class="s2">&quot;subnet-de0406d2&quot;</span><span class="p">],</span>
    <span class="n">vpc_endpoint_type</span><span class="o">=</span><span class="s2">&quot;Interface&quot;</span><span class="p">,</span>
    <span class="n">vpc_id</span><span class="o">=</span><span class="s2">&quot;vpc-7fc0a543&quot;</span><span class="p">)</span>
<span class="n">test_private_endpoint_interface_link</span> <span class="o">=</span> <span class="n">mongodbatlas</span><span class="o">.</span><span class="n">PrivateEndpointInterfaceLink</span><span class="p">(</span><span class="s2">&quot;testPrivateEndpointInterfaceLink&quot;</span><span class="p">,</span>
    <span class="n">interface_endpoint_id</span><span class="o">=</span><span class="n">ptfe_service</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">private_link_id</span><span class="o">=</span><span class="n">test_private_endpoint</span><span class="o">.</span><span class="n">private_link_id</span><span class="p">,</span>
    <span class="n">project_id</span><span class="o">=</span><span class="n">test_private_endpoint</span><span class="o">.</span><span class="n">project_id</span><span class="p">)</span>
</pre></div>
</div>
<p>Private Endpoint Link Connection can be imported using project ID and username, in the format <code class="docutils literal notranslate"><span class="pre">{project_id}-{private_link_id}-{interface_endpoint_id}</span></code>, e.g.</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>   $ pulumi import mongodbatlas:index/privateEndpointInterfaceLink:PrivateEndpointInterfaceLink <span class="nb">test</span> 1112222b3bf99403840e8934-3242342343112-vpce-4242342343

See detailed information <span class="k">for</span> arguments and attributes<span class="se">\ </span><span class="sb">`</span>MongoDB API Private Endpoint Link Connection &lt;https://docs.atlas.mongodb.com/reference/api/private-endpoint-create-one-interface-endpoint/&gt;<span class="sb">`</span>_
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>interface_endpoint_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Unique identifier of the interface endpoint you created in your VPC with the AWS resource.</p></li>
<li><p><strong>private_link_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Unique identifier of the AWS PrivateLink connection which is created by <code class="docutils literal notranslate"><span class="pre">PrivateEndpoint</span></code> resource.</p></li>
<li><p><strong>project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Unique identifier for the project.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_mongodbatlas.PrivateEndpointInterfaceLink.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">connection_status</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">delete_requested</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">error_message</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">interface_endpoint_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">private_link_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_mongodbatlas.private_endpoint_interface_link.PrivateEndpointInterfaceLink<a class="headerlink" href="#pulumi_mongodbatlas.PrivateEndpointInterfaceLink.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing PrivateEndpointInterfaceLink resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>connection_status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Status of the interface endpoint.
Returns one of the following values:</p></li>
<li><p><strong>delete_requested</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Indicates if Atlas received a request to remove the interface endpoint from the private endpoint connection.</p></li>
<li><p><strong>error_message</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Error message pertaining to the interface endpoint. Returns null if there are no errors.</p></li>
<li><p><strong>interface_endpoint_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Unique identifier of the interface endpoint you created in your VPC with the AWS resource.</p></li>
<li><p><strong>private_link_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Unique identifier of the AWS PrivateLink connection which is created by <code class="docutils literal notranslate"><span class="pre">PrivateEndpoint</span></code> resource.</p></li>
<li><p><strong>project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Unique identifier for the project.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.PrivateEndpointInterfaceLink.connection_status">
<em class="property">property </em><code class="sig-name descname">connection_status</code><a class="headerlink" href="#pulumi_mongodbatlas.PrivateEndpointInterfaceLink.connection_status" title="Permalink to this definition">¶</a></dt>
<dd><p>Status of the interface endpoint.
Returns one of the following values:</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.PrivateEndpointInterfaceLink.delete_requested">
<em class="property">property </em><code class="sig-name descname">delete_requested</code><a class="headerlink" href="#pulumi_mongodbatlas.PrivateEndpointInterfaceLink.delete_requested" title="Permalink to this definition">¶</a></dt>
<dd><p>Indicates if Atlas received a request to remove the interface endpoint from the private endpoint connection.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.PrivateEndpointInterfaceLink.error_message">
<em class="property">property </em><code class="sig-name descname">error_message</code><a class="headerlink" href="#pulumi_mongodbatlas.PrivateEndpointInterfaceLink.error_message" title="Permalink to this definition">¶</a></dt>
<dd><p>Error message pertaining to the interface endpoint. Returns null if there are no errors.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.PrivateEndpointInterfaceLink.interface_endpoint_id">
<em class="property">property </em><code class="sig-name descname">interface_endpoint_id</code><a class="headerlink" href="#pulumi_mongodbatlas.PrivateEndpointInterfaceLink.interface_endpoint_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Unique identifier of the interface endpoint you created in your VPC with the AWS resource.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.PrivateEndpointInterfaceLink.private_link_id">
<em class="property">property </em><code class="sig-name descname">private_link_id</code><a class="headerlink" href="#pulumi_mongodbatlas.PrivateEndpointInterfaceLink.private_link_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Unique identifier of the AWS PrivateLink connection which is created by <code class="docutils literal notranslate"><span class="pre">PrivateEndpoint</span></code> resource.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.PrivateEndpointInterfaceLink.project_id">
<em class="property">property </em><code class="sig-name descname">project_id</code><a class="headerlink" href="#pulumi_mongodbatlas.PrivateEndpointInterfaceLink.project_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Unique identifier for the project.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.PrivateEndpointInterfaceLink.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.PrivateEndpointInterfaceLink.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_mongodbatlas.PrivateEndpointInterfaceLink.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.PrivateEndpointInterfaceLink.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py class">
<dt id="pulumi_mongodbatlas.PrivateIpMode">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">PrivateIpMode</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.PrivateIpMode" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">PrivateIpMode</span></code> provides a Private IP Mode resource. This allows one to disable Connect via Peering Only mode for a MongoDB Atlas Project.</p>
<blockquote>
<div><p><strong>Deprecated Feature</strong>: <span class="raw-html-m2r"><br></span> This feature has been deprecated. Use <a class="reference external" href="https://dochub.mongodb.org/core/atlas-horizon-faq">Split Horizon connection strings</a> to connect to your cluster. These connection strings allow you to connect using both VPC/VNet Peering and whitelisted public IP addresses. To learn more about support for Split Horizon, see <a class="reference external" href="https://dochub.mongodb.org/core/atlas-horizon-faq">this FAQ</a>. You need this endpoint to <a class="reference external" href="https://docs.atlas.mongodb.com/reference/faq/connection-changes/#disable-peering-mode">disable Peering Only</a>.</p>
</div></blockquote>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_mongodbatlas</span> <span class="k">as</span> <span class="nn">mongodbatlas</span>

<span class="n">my_private_ip_mode</span> <span class="o">=</span> <span class="n">mongodbatlas</span><span class="o">.</span><span class="n">PrivateIpMode</span><span class="p">(</span><span class="s2">&quot;myPrivateIpMode&quot;</span><span class="p">,</span>
    <span class="n">enabled</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span>
    <span class="n">project_id</span><span class="o">=</span><span class="s2">&quot;&lt;YOUR PROJECT ID&gt;&quot;</span><span class="p">)</span>
</pre></div>
</div>
<p>Project must be imported using project ID, e.g.</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>   $ pulumi import mongodbatlas:index/privateIpMode:PrivateIpMode my_private_ip_mode 5d09d6a59ccf6445652a444a

For more information see<span class="se">\ </span><span class="sb">`</span>MongoDB Atlas API Reference. &lt;https://docs.atlas.mongodb.com/reference/api/get-private-ip-mode-for-project/&gt;<span class="sb">`</span>_
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Indicates whether Connect via Peering Only mode is enabled or disabled for an Atlas project</p></li>
<li><p><strong>project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique ID for the project to enable Only Private IP Mode.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_mongodbatlas.PrivateIpMode.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_mongodbatlas.private_ip_mode.PrivateIpMode<a class="headerlink" href="#pulumi_mongodbatlas.PrivateIpMode.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing PrivateIpMode resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Indicates whether Connect via Peering Only mode is enabled or disabled for an Atlas project</p></li>
<li><p><strong>project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique ID for the project to enable Only Private IP Mode.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.PrivateIpMode.enabled">
<em class="property">property </em><code class="sig-name descname">enabled</code><a class="headerlink" href="#pulumi_mongodbatlas.PrivateIpMode.enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Indicates whether Connect via Peering Only mode is enabled or disabled for an Atlas project</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.PrivateIpMode.project_id">
<em class="property">property </em><code class="sig-name descname">project_id</code><a class="headerlink" href="#pulumi_mongodbatlas.PrivateIpMode.project_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The unique ID for the project to enable Only Private IP Mode.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.PrivateIpMode.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.PrivateIpMode.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_mongodbatlas.PrivateIpMode.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.PrivateIpMode.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py class">
<dt id="pulumi_mongodbatlas.PrivateLinkEndpoint">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">PrivateLinkEndpoint</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">provider_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">region</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.PrivateLinkEndpoint" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">PrivateLinkEndpoint</span></code> provides a Private Endpoint resource. This represents a Private Endpoint Service that can be created in an Atlas project.</p>
<blockquote>
<div><p><strong>IMPORTANT:</strong>You must have one of the following roles to successfully handle the resource:</p>
<ul class="simple">
<li><p>Organization Owner</p></li>
<li><p>Project Owner</p></li>
</ul>
<p><strong>NOTE:</strong> Groups and projects are synonymous terms. You may find group_id in the official documentation.</p>
<p><strong>NOTE:</strong> A network container is created for a private endpoint to reside in if one does not yet exist in the project.</p>
</div></blockquote>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_mongodbatlas</span> <span class="k">as</span> <span class="nn">mongodbatlas</span>

<span class="n">test</span> <span class="o">=</span> <span class="n">mongodbatlas</span><span class="o">.</span><span class="n">PrivateLinkEndpoint</span><span class="p">(</span><span class="s2">&quot;test&quot;</span><span class="p">,</span>
    <span class="n">project_id</span><span class="o">=</span><span class="s2">&quot;&lt;PROJECT-ID&gt;&quot;</span><span class="p">,</span>
    <span class="n">provider_name</span><span class="o">=</span><span class="s2">&quot;AWS/AZURE&quot;</span><span class="p">,</span>
    <span class="n">region</span><span class="o">=</span><span class="s2">&quot;us-east-1&quot;</span><span class="p">)</span>
</pre></div>
</div>
<p>Private Endpoint Service can be imported using project ID and username, in the format <code class="docutils literal notranslate"><span class="pre">{project_id}-{private_link_id}-{provider_name}</span></code>, e.g.</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>   $ pulumi import mongodbatlas:index/privateLinkEndpoint:PrivateLinkEndpoint <span class="nb">test</span> 1112222b3bf99403840e8934-3242342343112-AWS

See detailed information <span class="k">for</span> arguments and attributes<span class="se">\ </span><span class="sb">`</span>MongoDB API Private Endpoint Service &lt;https://docs.atlas.mongodb.com/reference/api/private-endpoints-service-create-one//&gt;<span class="sb">`</span>_
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Required   Unique identifier for the project.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Cloud provider region in which you want to create the private endpoint connection.
Accepted values are: <a class="reference external" href="https://docs.atlas.mongodb.com/reference/amazon-aws/#amazon-aws">AWS regions</a> and <a class="reference external" href="https://docs.atlas.mongodb.com/reference/microsoft-azure/#microsoft-azure">AZURE regions</a></p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_mongodbatlas.PrivateLinkEndpoint.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">endpoint_service_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">error_message</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">interface_endpoints</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">private_endpoints</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">private_link_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">private_link_service_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">private_link_service_resource_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">provider_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">region</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">status</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_mongodbatlas.private_link_endpoint.PrivateLinkEndpoint<a class="headerlink" href="#pulumi_mongodbatlas.PrivateLinkEndpoint.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing PrivateLinkEndpoint resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>endpoint_service_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the PrivateLink endpoint service in AWS. Returns null while the endpoint service is being created.</p></li>
<li><p><strong>error_message</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Error message pertaining to the AWS PrivateLink connection. Returns null if there are no errors.</p></li>
<li><p><strong>interface_endpoints</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – Unique identifiers of the interface endpoints in your VPC that you added to the AWS PrivateLink connection.</p></li>
<li><p><strong>private_endpoints</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – All private endpoints that you have added to this Azure Private Link Service.</p></li>
<li><p><strong>private_link_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Unique identifier of the AWS PrivateLink connection.</p></li>
<li><p><strong>private_link_service_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the Azure Private Link Service that Atlas manages.</p></li>
<li><p><strong>private_link_service_resource_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Resource ID of the Azure Private Link Service that Atlas manages.
Returns one of the following values:</p></li>
<li><p><strong>project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Required   Unique identifier for the project.</p></li>
<li><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>Cloud provider region in which you want to create the private endpoint connection.
Accepted values are: <a class="reference external" href="https://docs.atlas.mongodb.com/reference/amazon-aws/#amazon-aws">AWS regions</a> and <a class="reference external" href="https://docs.atlas.mongodb.com/reference/microsoft-azure/#microsoft-azure">AZURE regions</a></p>
</p></li>
<li><p><strong>status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Status of the Private Link Service.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.PrivateLinkEndpoint.endpoint_service_name">
<em class="property">property </em><code class="sig-name descname">endpoint_service_name</code><a class="headerlink" href="#pulumi_mongodbatlas.PrivateLinkEndpoint.endpoint_service_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the PrivateLink endpoint service in AWS. Returns null while the endpoint service is being created.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.PrivateLinkEndpoint.error_message">
<em class="property">property </em><code class="sig-name descname">error_message</code><a class="headerlink" href="#pulumi_mongodbatlas.PrivateLinkEndpoint.error_message" title="Permalink to this definition">¶</a></dt>
<dd><p>Error message pertaining to the AWS PrivateLink connection. Returns null if there are no errors.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.PrivateLinkEndpoint.interface_endpoints">
<em class="property">property </em><code class="sig-name descname">interface_endpoints</code><a class="headerlink" href="#pulumi_mongodbatlas.PrivateLinkEndpoint.interface_endpoints" title="Permalink to this definition">¶</a></dt>
<dd><p>Unique identifiers of the interface endpoints in your VPC that you added to the AWS PrivateLink connection.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.PrivateLinkEndpoint.private_endpoints">
<em class="property">property </em><code class="sig-name descname">private_endpoints</code><a class="headerlink" href="#pulumi_mongodbatlas.PrivateLinkEndpoint.private_endpoints" title="Permalink to this definition">¶</a></dt>
<dd><p>All private endpoints that you have added to this Azure Private Link Service.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.PrivateLinkEndpoint.private_link_id">
<em class="property">property </em><code class="sig-name descname">private_link_id</code><a class="headerlink" href="#pulumi_mongodbatlas.PrivateLinkEndpoint.private_link_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Unique identifier of the AWS PrivateLink connection.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.PrivateLinkEndpoint.private_link_service_name">
<em class="property">property </em><code class="sig-name descname">private_link_service_name</code><a class="headerlink" href="#pulumi_mongodbatlas.PrivateLinkEndpoint.private_link_service_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the Azure Private Link Service that Atlas manages.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.PrivateLinkEndpoint.private_link_service_resource_id">
<em class="property">property </em><code class="sig-name descname">private_link_service_resource_id</code><a class="headerlink" href="#pulumi_mongodbatlas.PrivateLinkEndpoint.private_link_service_resource_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Resource ID of the Azure Private Link Service that Atlas manages.
Returns one of the following values:</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.PrivateLinkEndpoint.project_id">
<em class="property">property </em><code class="sig-name descname">project_id</code><a class="headerlink" href="#pulumi_mongodbatlas.PrivateLinkEndpoint.project_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Required        Unique identifier for the project.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.PrivateLinkEndpoint.region">
<em class="property">property </em><code class="sig-name descname">region</code><a class="headerlink" href="#pulumi_mongodbatlas.PrivateLinkEndpoint.region" title="Permalink to this definition">¶</a></dt>
<dd><p>Cloud provider region in which you want to create the private endpoint connection.
Accepted values are: <a class="reference external" href="https://docs.atlas.mongodb.com/reference/amazon-aws/#amazon-aws">AWS regions</a> and <a class="reference external" href="https://docs.atlas.mongodb.com/reference/microsoft-azure/#microsoft-azure">AZURE regions</a></p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.PrivateLinkEndpoint.status">
<em class="property">property </em><code class="sig-name descname">status</code><a class="headerlink" href="#pulumi_mongodbatlas.PrivateLinkEndpoint.status" title="Permalink to this definition">¶</a></dt>
<dd><p>Status of the Private Link Service.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.PrivateLinkEndpoint.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.PrivateLinkEndpoint.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_mongodbatlas.PrivateLinkEndpoint.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.PrivateLinkEndpoint.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py class">
<dt id="pulumi_mongodbatlas.PrivateLinkEndpointService">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">PrivateLinkEndpointService</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">endpoint_service_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">private_endpoint_ip_address</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">private_link_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">provider_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.PrivateLinkEndpointService" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">PrivateLinkEndpointService</span></code> provides a Private Endpoint Interface Link resource. This represents a Private Endpoint Interface Link, which adds one interface endpoint to a private endpoint connection in an Atlas project.</p>
<blockquote>
<div><p><strong>IMPORTANT:</strong>You must have one of the following roles to successfully handle the resource:</p>
<ul class="simple">
<li><p>Organization Owner</p></li>
<li><p>Project Owner</p></li>
</ul>
<p><strong>NOTE:</strong> Groups and projects are synonymous terms. You may find group_id in the official documentation.</p>
</div></blockquote>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_aws</span> <span class="k">as</span> <span class="nn">aws</span>
<span class="kn">import</span> <span class="nn">pulumi_mongodbatlas</span> <span class="k">as</span> <span class="nn">mongodbatlas</span>

<span class="n">test_private_link_endpoint</span> <span class="o">=</span> <span class="n">mongodbatlas</span><span class="o">.</span><span class="n">PrivateLinkEndpoint</span><span class="p">(</span><span class="s2">&quot;testPrivateLinkEndpoint&quot;</span><span class="p">,</span>
    <span class="n">project_id</span><span class="o">=</span><span class="s2">&quot;&lt;PROJECT_ID&gt;&quot;</span><span class="p">,</span>
    <span class="n">provider_name</span><span class="o">=</span><span class="s2">&quot;AWS&quot;</span><span class="p">,</span>
    <span class="n">region</span><span class="o">=</span><span class="s2">&quot;us-east-1&quot;</span><span class="p">)</span>
<span class="n">ptfe_service</span> <span class="o">=</span> <span class="n">aws</span><span class="o">.</span><span class="n">ec2</span><span class="o">.</span><span class="n">VpcEndpoint</span><span class="p">(</span><span class="s2">&quot;ptfeService&quot;</span><span class="p">,</span>
    <span class="n">security_group_ids</span><span class="o">=</span><span class="p">[</span><span class="s2">&quot;sg-3f238186&quot;</span><span class="p">],</span>
    <span class="n">service_name</span><span class="o">=</span><span class="n">test_private_link_endpoint</span><span class="o">.</span><span class="n">endpoint_service_name</span><span class="p">,</span>
    <span class="n">subnet_ids</span><span class="o">=</span><span class="p">[</span><span class="s2">&quot;subnet-de0406d2&quot;</span><span class="p">],</span>
    <span class="n">vpc_endpoint_type</span><span class="o">=</span><span class="s2">&quot;Interface&quot;</span><span class="p">,</span>
    <span class="n">vpc_id</span><span class="o">=</span><span class="s2">&quot;vpc-7fc0a543&quot;</span><span class="p">)</span>
<span class="n">test_private_link_endpoint_service</span> <span class="o">=</span> <span class="n">mongodbatlas</span><span class="o">.</span><span class="n">PrivateLinkEndpointService</span><span class="p">(</span><span class="s2">&quot;testPrivateLinkEndpointService&quot;</span><span class="p">,</span>
    <span class="n">endpoint_service_id</span><span class="o">=</span><span class="n">ptfe_service</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">private_link_id</span><span class="o">=</span><span class="n">test_private_link_endpoint</span><span class="o">.</span><span class="n">private_link_id</span><span class="p">,</span>
    <span class="n">project_id</span><span class="o">=</span><span class="n">test_private_link_endpoint</span><span class="o">.</span><span class="n">project_id</span><span class="p">,</span>
    <span class="n">provider_name</span><span class="o">=</span><span class="s2">&quot;AWS&quot;</span><span class="p">)</span>
</pre></div>
</div>
<p>Private Endpoint Link Connection can be imported using project ID and username, in the format <code class="docutils literal notranslate"><span class="pre">{project_id}--{private_link_id}--{endpoint_service_id}--{provider_name}</span></code>, e.g.</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>   $ pulumi import mongodbatlas:index/privateLinkEndpointService:PrivateLinkEndpointService <span class="nb">test</span> 1112222b3bf99403840e8934--vpce-4242342343--3242342343112--AWS

See detailed information <span class="k">for</span> arguments and attributes<span class="se">\ </span><span class="sb">`</span>MongoDB API Private Endpoint Link Connection &lt;https://docs.atlas.mongodb.com/reference/api/private-endpoints-endpoint-create-one/&gt;<span class="sb">`</span>_
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>endpoint_service_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Unique identifier of the interface endpoint you created in your VPC with the <code class="docutils literal notranslate"><span class="pre">AWS</span></code> or <code class="docutils literal notranslate"><span class="pre">AZURE</span></code> resource.</p></li>
<li><p><strong>private_endpoint_ip_address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Private IP address of the private endpoint network interface you created in your Azure VNet. Only for <code class="docutils literal notranslate"><span class="pre">AZURE</span></code>.</p></li>
<li><p><strong>private_link_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Unique identifier of the <code class="docutils literal notranslate"><span class="pre">AWS</span></code> or <code class="docutils literal notranslate"><span class="pre">AZURE</span></code> PrivateLink connection which is created by <code class="docutils literal notranslate"><span class="pre">PrivateLinkEndpoint</span></code> resource.</p></li>
<li><p><strong>project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Unique identifier for the project.</p></li>
<li><p><strong>provider_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Cloud provider for which you want to create a private endpoint. Atlas accepts <code class="docutils literal notranslate"><span class="pre">AWS</span></code> or <code class="docutils literal notranslate"><span class="pre">AZURE</span></code>.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_mongodbatlas.PrivateLinkEndpointService.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">connection_status</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">delete_requested</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">endpoint_service_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">error_message</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">interface_endpoint_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">private_endpoint_connection_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">private_endpoint_ip_address</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">private_endpoint_resource_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">private_link_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">provider_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_mongodbatlas.private_link_endpoint_service.PrivateLinkEndpointService<a class="headerlink" href="#pulumi_mongodbatlas.PrivateLinkEndpointService.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing PrivateLinkEndpointService resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>connection_status</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Status of the interface endpoint.
Returns one of the following values:</p></li>
<li><p><strong>delete_requested</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Indicates if Atlas received a request to remove the interface endpoint from the private endpoint connection.</p></li>
<li><p><strong>endpoint_service_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Unique identifier of the interface endpoint you created in your VPC with the <code class="docutils literal notranslate"><span class="pre">AWS</span></code> or <code class="docutils literal notranslate"><span class="pre">AZURE</span></code> resource.</p></li>
<li><p><strong>error_message</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Error message pertaining to the interface endpoint. Returns null if there are no errors.</p></li>
<li><p><strong>interface_endpoint_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Unique identifier of the interface endpoint.</p></li>
<li><p><strong>private_endpoint_connection_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the connection for this private endpoint that Atlas generates.</p></li>
<li><p><strong>private_endpoint_ip_address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Private IP address of the private endpoint network interface you created in your Azure VNet. Only for <code class="docutils literal notranslate"><span class="pre">AZURE</span></code>.</p></li>
<li><p><strong>private_endpoint_resource_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Unique identifier of the private endpoint.</p></li>
<li><p><strong>private_link_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Unique identifier of the <code class="docutils literal notranslate"><span class="pre">AWS</span></code> or <code class="docutils literal notranslate"><span class="pre">AZURE</span></code> PrivateLink connection which is created by <code class="docutils literal notranslate"><span class="pre">PrivateLinkEndpoint</span></code> resource.</p></li>
<li><p><strong>project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Unique identifier for the project.</p></li>
<li><p><strong>provider_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Cloud provider for which you want to create a private endpoint. Atlas accepts <code class="docutils literal notranslate"><span class="pre">AWS</span></code> or <code class="docutils literal notranslate"><span class="pre">AZURE</span></code>.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.PrivateLinkEndpointService.connection_status">
<em class="property">property </em><code class="sig-name descname">connection_status</code><a class="headerlink" href="#pulumi_mongodbatlas.PrivateLinkEndpointService.connection_status" title="Permalink to this definition">¶</a></dt>
<dd><p>Status of the interface endpoint.
Returns one of the following values:</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.PrivateLinkEndpointService.delete_requested">
<em class="property">property </em><code class="sig-name descname">delete_requested</code><a class="headerlink" href="#pulumi_mongodbatlas.PrivateLinkEndpointService.delete_requested" title="Permalink to this definition">¶</a></dt>
<dd><p>Indicates if Atlas received a request to remove the interface endpoint from the private endpoint connection.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.PrivateLinkEndpointService.endpoint_service_id">
<em class="property">property </em><code class="sig-name descname">endpoint_service_id</code><a class="headerlink" href="#pulumi_mongodbatlas.PrivateLinkEndpointService.endpoint_service_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Unique identifier of the interface endpoint you created in your VPC with the <code class="docutils literal notranslate"><span class="pre">AWS</span></code> or <code class="docutils literal notranslate"><span class="pre">AZURE</span></code> resource.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.PrivateLinkEndpointService.error_message">
<em class="property">property </em><code class="sig-name descname">error_message</code><a class="headerlink" href="#pulumi_mongodbatlas.PrivateLinkEndpointService.error_message" title="Permalink to this definition">¶</a></dt>
<dd><p>Error message pertaining to the interface endpoint. Returns null if there are no errors.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.PrivateLinkEndpointService.interface_endpoint_id">
<em class="property">property </em><code class="sig-name descname">interface_endpoint_id</code><a class="headerlink" href="#pulumi_mongodbatlas.PrivateLinkEndpointService.interface_endpoint_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Unique identifier of the interface endpoint.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.PrivateLinkEndpointService.private_endpoint_connection_name">
<em class="property">property </em><code class="sig-name descname">private_endpoint_connection_name</code><a class="headerlink" href="#pulumi_mongodbatlas.PrivateLinkEndpointService.private_endpoint_connection_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the connection for this private endpoint that Atlas generates.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.PrivateLinkEndpointService.private_endpoint_ip_address">
<em class="property">property </em><code class="sig-name descname">private_endpoint_ip_address</code><a class="headerlink" href="#pulumi_mongodbatlas.PrivateLinkEndpointService.private_endpoint_ip_address" title="Permalink to this definition">¶</a></dt>
<dd><p>Private IP address of the private endpoint network interface you created in your Azure VNet. Only for <code class="docutils literal notranslate"><span class="pre">AZURE</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.PrivateLinkEndpointService.private_endpoint_resource_id">
<em class="property">property </em><code class="sig-name descname">private_endpoint_resource_id</code><a class="headerlink" href="#pulumi_mongodbatlas.PrivateLinkEndpointService.private_endpoint_resource_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Unique identifier of the private endpoint.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.PrivateLinkEndpointService.private_link_id">
<em class="property">property </em><code class="sig-name descname">private_link_id</code><a class="headerlink" href="#pulumi_mongodbatlas.PrivateLinkEndpointService.private_link_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Unique identifier of the <code class="docutils literal notranslate"><span class="pre">AWS</span></code> or <code class="docutils literal notranslate"><span class="pre">AZURE</span></code> PrivateLink connection which is created by <code class="docutils literal notranslate"><span class="pre">PrivateLinkEndpoint</span></code> resource.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.PrivateLinkEndpointService.project_id">
<em class="property">property </em><code class="sig-name descname">project_id</code><a class="headerlink" href="#pulumi_mongodbatlas.PrivateLinkEndpointService.project_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Unique identifier for the project.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.PrivateLinkEndpointService.provider_name">
<em class="property">property </em><code class="sig-name descname">provider_name</code><a class="headerlink" href="#pulumi_mongodbatlas.PrivateLinkEndpointService.provider_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Cloud provider for which you want to create a private endpoint. Atlas accepts <code class="docutils literal notranslate"><span class="pre">AWS</span></code> or <code class="docutils literal notranslate"><span class="pre">AZURE</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.PrivateLinkEndpointService.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.PrivateLinkEndpointService.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_mongodbatlas.PrivateLinkEndpointService.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.PrivateLinkEndpointService.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py class">
<dt id="pulumi_mongodbatlas.Project">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">Project</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">org_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">teams</span><span class="p">:</span> <span class="n">Union[Sequence[Union[ProjectTeamArgs, Mapping[str, Any], Awaitable[Union[ProjectTeamArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[ProjectTeamArgs, Mapping[str, Any], Awaitable[Union[ProjectTeamArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.Project" title="Permalink to this definition">¶</a></dt>
<dd><p>Project must be imported using project ID, e.g.</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>   $ pulumi import mongodbatlas:index/project:Project my_project 5d09d6a59ccf6445652a444a

For more information see<span class="se">\ </span><span class="sb">`</span>MongoDB Atlas API Reference. &lt;https://docs.atlas.mongodb.com/reference/api/projects/&gt;<span class="sb">`</span>_ - <span class="sb">`</span>and MongoDB Atlas API - Teams &lt;https://docs.atlas.mongodb.com/reference/api/teams/&gt;<span class="sb">`</span>_ Documentation <span class="k">for</span> more information.
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the project you want to create. (Cannot be changed via this Provider after creation.)</p></li>
<li><p><strong>org_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the organization you want to create the project within.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_mongodbatlas.Project.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cluster_count</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">created</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">org_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">teams</span><span class="p">:</span> <span class="n">Union[Sequence[Union[ProjectTeamArgs, Mapping[str, Any], Awaitable[Union[ProjectTeamArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[ProjectTeamArgs, Mapping[str, Any], Awaitable[Union[ProjectTeamArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_mongodbatlas.project.Project<a class="headerlink" href="#pulumi_mongodbatlas.Project.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Project resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>cluster_count</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The number of Atlas clusters deployed in the project..</p></li>
<li><p><strong>created</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ISO-8601-formatted timestamp of when Atlas created the project..</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the project you want to create. (Cannot be changed via this Provider after creation.)</p></li>
<li><p><strong>org_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the organization you want to create the project within.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.Project.cluster_count">
<em class="property">property </em><code class="sig-name descname">cluster_count</code><a class="headerlink" href="#pulumi_mongodbatlas.Project.cluster_count" title="Permalink to this definition">¶</a></dt>
<dd><p>The number of Atlas clusters deployed in the project..</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.Project.created">
<em class="property">property </em><code class="sig-name descname">created</code><a class="headerlink" href="#pulumi_mongodbatlas.Project.created" title="Permalink to this definition">¶</a></dt>
<dd><p>The ISO-8601-formatted timestamp of when Atlas created the project..</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.Project.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_mongodbatlas.Project.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the project you want to create. (Cannot be changed via this Provider after creation.)</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.Project.org_id">
<em class="property">property </em><code class="sig-name descname">org_id</code><a class="headerlink" href="#pulumi_mongodbatlas.Project.org_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the organization you want to create the project within.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.Project.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.Project.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_mongodbatlas.Project.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.Project.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py class">
<dt id="pulumi_mongodbatlas.ProjectIpAccessList">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">ProjectIpAccessList</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">aws_security_group</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cidr_block</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">comment</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ip_address</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.ProjectIpAccessList" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">ProjectIpAccessList</span></code> provides an IP Access List entry resource. The access list grants access from IPs, CIDRs or AWS Security Groups (if VPC Peering is enabled) to clusters within the Project.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Groups and projects are synonymous terms. You may find <code class="docutils literal notranslate"><span class="pre">groupId</span></code> in the official documentation.</p>
<p><strong>IMPORTANT:</strong>
When you remove an entry from the access list, existing connections from the removed address(es) may remain open for a variable amount of time. How much time passes before Atlas closes the connection depends on several factors, including how the connection was established, the particular behavior of the application or driver using the address, and the connection protocol (e.g., TCP or UDP). This is particularly important to consider when changing an existing IP address or CIDR block as they cannot be updated via the Provider (comments can however), hence a change will force the destruction and recreation of entries.</p>
</div></blockquote>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_mongodbatlas</span> <span class="k">as</span> <span class="nn">mongodbatlas</span>

<span class="n">test</span> <span class="o">=</span> <span class="n">mongodbatlas</span><span class="o">.</span><span class="n">ProjectIpAccessList</span><span class="p">(</span><span class="s2">&quot;test&quot;</span><span class="p">,</span>
    <span class="n">cidr_block</span><span class="o">=</span><span class="s2">&quot;1.2.3.4/32&quot;</span><span class="p">,</span>
    <span class="n">comment</span><span class="o">=</span><span class="s2">&quot;cidr block for tf acc testing&quot;</span><span class="p">,</span>
    <span class="n">project_id</span><span class="o">=</span><span class="s2">&quot;&lt;PROJECT-ID&gt;&quot;</span><span class="p">)</span>
</pre></div>
</div>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_mongodbatlas</span> <span class="k">as</span> <span class="nn">mongodbatlas</span>

<span class="n">test</span> <span class="o">=</span> <span class="n">mongodbatlas</span><span class="o">.</span><span class="n">ProjectIpAccessList</span><span class="p">(</span><span class="s2">&quot;test&quot;</span><span class="p">,</span>
    <span class="n">comment</span><span class="o">=</span><span class="s2">&quot;ip address for tf acc testing&quot;</span><span class="p">,</span>
    <span class="n">ip_address</span><span class="o">=</span><span class="s2">&quot;2.3.4.5&quot;</span><span class="p">,</span>
    <span class="n">project_id</span><span class="o">=</span><span class="s2">&quot;&lt;PROJECT-ID&gt;&quot;</span><span class="p">)</span>
</pre></div>
</div>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_mongodbatlas</span> <span class="k">as</span> <span class="nn">mongodbatlas</span>

<span class="n">test_network_container</span> <span class="o">=</span> <span class="n">mongodbatlas</span><span class="o">.</span><span class="n">NetworkContainer</span><span class="p">(</span><span class="s2">&quot;testNetworkContainer&quot;</span><span class="p">,</span>
    <span class="n">project_id</span><span class="o">=</span><span class="s2">&quot;&lt;PROJECT-ID&gt;&quot;</span><span class="p">,</span>
    <span class="n">atlas_cidr_block</span><span class="o">=</span><span class="s2">&quot;192.168.208.0/21&quot;</span><span class="p">,</span>
    <span class="n">provider_name</span><span class="o">=</span><span class="s2">&quot;AWS&quot;</span><span class="p">,</span>
    <span class="n">region_name</span><span class="o">=</span><span class="s2">&quot;US_EAST_1&quot;</span><span class="p">)</span>
<span class="n">test_network_peering</span> <span class="o">=</span> <span class="n">mongodbatlas</span><span class="o">.</span><span class="n">NetworkPeering</span><span class="p">(</span><span class="s2">&quot;testNetworkPeering&quot;</span><span class="p">,</span>
    <span class="n">project_id</span><span class="o">=</span><span class="s2">&quot;&lt;PROJECT-ID&gt;&quot;</span><span class="p">,</span>
    <span class="n">container_id</span><span class="o">=</span><span class="n">test_network_container</span><span class="o">.</span><span class="n">container_id</span><span class="p">,</span>
    <span class="n">accepter_region_name</span><span class="o">=</span><span class="s2">&quot;us-east-1&quot;</span><span class="p">,</span>
    <span class="n">provider_name</span><span class="o">=</span><span class="s2">&quot;AWS&quot;</span><span class="p">,</span>
    <span class="n">route_table_cidr_block</span><span class="o">=</span><span class="s2">&quot;172.31.0.0/16&quot;</span><span class="p">,</span>
    <span class="n">vpc_id</span><span class="o">=</span><span class="s2">&quot;vpc-0d93d6f69f1578bd8&quot;</span><span class="p">,</span>
    <span class="n">aws_account_id</span><span class="o">=</span><span class="s2">&quot;232589400519&quot;</span><span class="p">)</span>
<span class="n">test_project_ip_access_list</span> <span class="o">=</span> <span class="n">mongodbatlas</span><span class="o">.</span><span class="n">ProjectIpAccessList</span><span class="p">(</span><span class="s2">&quot;testProjectIpAccessList&quot;</span><span class="p">,</span>
    <span class="n">project_id</span><span class="o">=</span><span class="s2">&quot;&lt;PROJECT-ID&gt;&quot;</span><span class="p">,</span>
    <span class="n">aws_security_group</span><span class="o">=</span><span class="s2">&quot;sg-0026348ec11780bd1&quot;</span><span class="p">,</span>
    <span class="n">comment</span><span class="o">=</span><span class="s2">&quot;TestAcc for awsSecurityGroup&quot;</span><span class="p">,</span>
    <span class="n">opts</span><span class="o">=</span><span class="n">pulumi</span><span class="o">.</span><span class="n">ResourceOptions</span><span class="p">(</span><span class="n">depends_on</span><span class="o">=</span><span class="p">[</span><span class="s2">&quot;mongodbatlas_network_peering.test&quot;</span><span class="p">]))</span>
</pre></div>
</div>
<blockquote>
<div><p><strong>IMPORTANT:</strong> In order to use AWS Security Group(s) VPC Peering must be enabled like above example.</p>
</div></blockquote>
<p>IP Access List entries can be imported using the <code class="docutils literal notranslate"><span class="pre">project_id</span></code> and <code class="docutils literal notranslate"><span class="pre">cidr_block</span></code> or <code class="docutils literal notranslate"><span class="pre">ip_address</span></code>, e.g.</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>   $ pulumi import mongodbatlas:index/projectIpAccessList:ProjectIpAccessList <span class="nb">test</span> 5d0f1f74cf09a29120e123cd-10.242.88.0/21

For more information see<span class="se">\ </span><span class="sb">`</span>MongoDB Atlas API Reference. &lt;https://docs.atlas.mongodb.com/reference/api/access-lists/&gt;<span class="sb">`</span>_
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>aws_security_group</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Unique identifier of the AWS security group to add to the access list. Your access list entry can include only one <code class="docutils literal notranslate"><span class="pre">awsSecurityGroup</span></code>, one <code class="docutils literal notranslate"><span class="pre">cidrBlock</span></code>, or one <code class="docutils literal notranslate"><span class="pre">ipAddress</span></code>.</p></li>
<li><p><strong>cidr_block</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Range of IP addresses in CIDR notation to be added to the access list. Your access list entry can include only one <code class="docutils literal notranslate"><span class="pre">awsSecurityGroup</span></code>, one <code class="docutils literal notranslate"><span class="pre">cidrBlock</span></code>, or one <code class="docutils literal notranslate"><span class="pre">ipAddress</span></code>.</p></li>
<li><p><strong>comment</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Comment to add to the access list entry.</p></li>
<li><p><strong>ip_address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Single IP address to be added to the access list. Mutually exclusive with <code class="docutils literal notranslate"><span class="pre">awsSecurityGroup</span></code> and <code class="docutils literal notranslate"><span class="pre">cidrBlock</span></code>.</p></li>
<li><p><strong>project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Unique identifier for the project to which you want to add one or more access list entries.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_mongodbatlas.ProjectIpAccessList.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">aws_security_group</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cidr_block</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">comment</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ip_address</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_mongodbatlas.project_ip_access_list.ProjectIpAccessList<a class="headerlink" href="#pulumi_mongodbatlas.ProjectIpAccessList.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ProjectIpAccessList resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>aws_security_group</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Unique identifier of the AWS security group to add to the access list. Your access list entry can include only one <code class="docutils literal notranslate"><span class="pre">awsSecurityGroup</span></code>, one <code class="docutils literal notranslate"><span class="pre">cidrBlock</span></code>, or one <code class="docutils literal notranslate"><span class="pre">ipAddress</span></code>.</p></li>
<li><p><strong>cidr_block</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Range of IP addresses in CIDR notation to be added to the access list. Your access list entry can include only one <code class="docutils literal notranslate"><span class="pre">awsSecurityGroup</span></code>, one <code class="docutils literal notranslate"><span class="pre">cidrBlock</span></code>, or one <code class="docutils literal notranslate"><span class="pre">ipAddress</span></code>.</p></li>
<li><p><strong>comment</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Comment to add to the access list entry.</p></li>
<li><p><strong>ip_address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Single IP address to be added to the access list. Mutually exclusive with <code class="docutils literal notranslate"><span class="pre">awsSecurityGroup</span></code> and <code class="docutils literal notranslate"><span class="pre">cidrBlock</span></code>.</p></li>
<li><p><strong>project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Unique identifier for the project to which you want to add one or more access list entries.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.ProjectIpAccessList.aws_security_group">
<em class="property">property </em><code class="sig-name descname">aws_security_group</code><a class="headerlink" href="#pulumi_mongodbatlas.ProjectIpAccessList.aws_security_group" title="Permalink to this definition">¶</a></dt>
<dd><p>Unique identifier of the AWS security group to add to the access list. Your access list entry can include only one <code class="docutils literal notranslate"><span class="pre">awsSecurityGroup</span></code>, one <code class="docutils literal notranslate"><span class="pre">cidrBlock</span></code>, or one <code class="docutils literal notranslate"><span class="pre">ipAddress</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.ProjectIpAccessList.cidr_block">
<em class="property">property </em><code class="sig-name descname">cidr_block</code><a class="headerlink" href="#pulumi_mongodbatlas.ProjectIpAccessList.cidr_block" title="Permalink to this definition">¶</a></dt>
<dd><p>Range of IP addresses in CIDR notation to be added to the access list. Your access list entry can include only one <code class="docutils literal notranslate"><span class="pre">awsSecurityGroup</span></code>, one <code class="docutils literal notranslate"><span class="pre">cidrBlock</span></code>, or one <code class="docutils literal notranslate"><span class="pre">ipAddress</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.ProjectIpAccessList.comment">
<em class="property">property </em><code class="sig-name descname">comment</code><a class="headerlink" href="#pulumi_mongodbatlas.ProjectIpAccessList.comment" title="Permalink to this definition">¶</a></dt>
<dd><p>Comment to add to the access list entry.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.ProjectIpAccessList.ip_address">
<em class="property">property </em><code class="sig-name descname">ip_address</code><a class="headerlink" href="#pulumi_mongodbatlas.ProjectIpAccessList.ip_address" title="Permalink to this definition">¶</a></dt>
<dd><p>Single IP address to be added to the access list. Mutually exclusive with <code class="docutils literal notranslate"><span class="pre">awsSecurityGroup</span></code> and <code class="docutils literal notranslate"><span class="pre">cidrBlock</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.ProjectIpAccessList.project_id">
<em class="property">property </em><code class="sig-name descname">project_id</code><a class="headerlink" href="#pulumi_mongodbatlas.ProjectIpAccessList.project_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Unique identifier for the project to which you want to add one or more access list entries.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.ProjectIpAccessList.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.ProjectIpAccessList.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_mongodbatlas.ProjectIpAccessList.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.ProjectIpAccessList.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py class">
<dt id="pulumi_mongodbatlas.ProjectIpWhitelist">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">ProjectIpWhitelist</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">aws_security_group</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cidr_block</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">comment</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ip_address</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.ProjectIpWhitelist" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">ProjectIpWhitelist</span></code> provides an IP Whitelist entry resource. The whitelist grants access from IPs, CIDRs or AWS Security Groups (if VPC Peering is enabled) to clusters within the Project.</p>
<blockquote>
<div><p><strong>IMPORTANT:</strong>
Recently we have made changes to modernize the terminology we use in Atlas. The term “Whitelist” has been deprecated in favor of “Access List”.  The Project IP whitelist resource has been deprecated and will be disabled in June 2021.  Please move to using the <a class="reference external" href="https://tf-registry.herokuapp.com/providers/mongodb/mongodbatlas/latest/docs/resources/project_ip_access_list">Project IP Access List</a> resource before June 2021.</p>
<p><strong>NOTE:</strong> Groups and projects are synonymous terms. You may find <code class="docutils literal notranslate"><span class="pre">groupId</span></code> in the official documentation.ß</p>
<p><strong>IMPORTANT:</strong>
When you remove an entry from the whitelist, existing connections from the removed address(es) may remain open for a variable amount of time. How much time passes before Atlas closes the connection depends on several factors, including how the connection was established, the particular behavior of the application or driver using the address, and the connection protocol (e.g., TCP or UDP). This is particularly important to consider when changing an existing IP address or CIDR block as they cannot be updated via the Provider (comments can however), hence a change will force the destruction and recreation of entries.</p>
</div></blockquote>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_mongodbatlas</span> <span class="k">as</span> <span class="nn">mongodbatlas</span>

<span class="n">test</span> <span class="o">=</span> <span class="n">mongodbatlas</span><span class="o">.</span><span class="n">ProjectIpWhitelist</span><span class="p">(</span><span class="s2">&quot;test&quot;</span><span class="p">,</span>
    <span class="n">cidr_block</span><span class="o">=</span><span class="s2">&quot;1.2.3.4/32&quot;</span><span class="p">,</span>
    <span class="n">comment</span><span class="o">=</span><span class="s2">&quot;cidr block for tf acc testing&quot;</span><span class="p">,</span>
    <span class="n">project_id</span><span class="o">=</span><span class="s2">&quot;&lt;PROJECT-ID&gt;&quot;</span><span class="p">)</span>
</pre></div>
</div>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_mongodbatlas</span> <span class="k">as</span> <span class="nn">mongodbatlas</span>

<span class="n">test</span> <span class="o">=</span> <span class="n">mongodbatlas</span><span class="o">.</span><span class="n">ProjectIpWhitelist</span><span class="p">(</span><span class="s2">&quot;test&quot;</span><span class="p">,</span>
    <span class="n">comment</span><span class="o">=</span><span class="s2">&quot;ip address for tf acc testing&quot;</span><span class="p">,</span>
    <span class="n">ip_address</span><span class="o">=</span><span class="s2">&quot;2.3.4.5&quot;</span><span class="p">,</span>
    <span class="n">project_id</span><span class="o">=</span><span class="s2">&quot;&lt;PROJECT-ID&gt;&quot;</span><span class="p">)</span>
</pre></div>
</div>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_mongodbatlas</span> <span class="k">as</span> <span class="nn">mongodbatlas</span>

<span class="n">test_network_container</span> <span class="o">=</span> <span class="n">mongodbatlas</span><span class="o">.</span><span class="n">NetworkContainer</span><span class="p">(</span><span class="s2">&quot;testNetworkContainer&quot;</span><span class="p">,</span>
    <span class="n">project_id</span><span class="o">=</span><span class="s2">&quot;&lt;PROJECT-ID&gt;&quot;</span><span class="p">,</span>
    <span class="n">atlas_cidr_block</span><span class="o">=</span><span class="s2">&quot;192.168.208.0/21&quot;</span><span class="p">,</span>
    <span class="n">provider_name</span><span class="o">=</span><span class="s2">&quot;AWS&quot;</span><span class="p">,</span>
    <span class="n">region_name</span><span class="o">=</span><span class="s2">&quot;US_EAST_1&quot;</span><span class="p">)</span>
<span class="n">test_network_peering</span> <span class="o">=</span> <span class="n">mongodbatlas</span><span class="o">.</span><span class="n">NetworkPeering</span><span class="p">(</span><span class="s2">&quot;testNetworkPeering&quot;</span><span class="p">,</span>
    <span class="n">project_id</span><span class="o">=</span><span class="s2">&quot;&lt;PROJECT-ID&gt;&quot;</span><span class="p">,</span>
    <span class="n">container_id</span><span class="o">=</span><span class="n">test_network_container</span><span class="o">.</span><span class="n">container_id</span><span class="p">,</span>
    <span class="n">accepter_region_name</span><span class="o">=</span><span class="s2">&quot;us-east-1&quot;</span><span class="p">,</span>
    <span class="n">provider_name</span><span class="o">=</span><span class="s2">&quot;AWS&quot;</span><span class="p">,</span>
    <span class="n">route_table_cidr_block</span><span class="o">=</span><span class="s2">&quot;172.31.0.0/16&quot;</span><span class="p">,</span>
    <span class="n">vpc_id</span><span class="o">=</span><span class="s2">&quot;vpc-0d93d6f69f1578bd8&quot;</span><span class="p">,</span>
    <span class="n">aws_account_id</span><span class="o">=</span><span class="s2">&quot;232589400519&quot;</span><span class="p">)</span>
<span class="n">test_project_ip_whitelist</span> <span class="o">=</span> <span class="n">mongodbatlas</span><span class="o">.</span><span class="n">ProjectIpWhitelist</span><span class="p">(</span><span class="s2">&quot;testProjectIpWhitelist&quot;</span><span class="p">,</span>
    <span class="n">project_id</span><span class="o">=</span><span class="s2">&quot;&lt;PROJECT-ID&gt;&quot;</span><span class="p">,</span>
    <span class="n">aws_security_group</span><span class="o">=</span><span class="s2">&quot;sg-0026348ec11780bd1&quot;</span><span class="p">,</span>
    <span class="n">comment</span><span class="o">=</span><span class="s2">&quot;TestAcc for awsSecurityGroup&quot;</span><span class="p">,</span>
    <span class="n">opts</span><span class="o">=</span><span class="n">pulumi</span><span class="o">.</span><span class="n">ResourceOptions</span><span class="p">(</span><span class="n">depends_on</span><span class="o">=</span><span class="p">[</span><span class="s2">&quot;mongodbatlas_network_peering.test&quot;</span><span class="p">]))</span>
</pre></div>
</div>
<blockquote>
<div><p><strong>IMPORTANT:</strong> In order to use AWS Security Group(s) VPC Peering must be enabled like above example.</p>
</div></blockquote>
<p>IP Whitelist entries can be imported using the <code class="docutils literal notranslate"><span class="pre">project_id</span></code> and <code class="docutils literal notranslate"><span class="pre">cidr_block</span></code> or <code class="docutils literal notranslate"><span class="pre">ip_address</span></code>, e.g.</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>   $ pulumi import mongodbatlas:index/projectIpWhitelist:ProjectIpWhitelist <span class="nb">test</span> 5d0f1f74cf09a29120e123cd-10.242.88.0/21

For more information see<span class="se">\ </span><span class="sb">`</span>MongoDB Atlas API Reference. &lt;https://docs.atlas.mongodb.com/reference/api/whitelist/&gt;<span class="sb">`</span>_
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>aws_security_group</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – ID of the whitelisted AWS security group. Mutually exclusive with <code class="docutils literal notranslate"><span class="pre">cidr_block</span></code> and <code class="docutils literal notranslate"><span class="pre">ip_address</span></code>.</p></li>
<li><p><strong>cidr_block</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Whitelist entry in Classless Inter-Domain Routing (CIDR) notation. Mutually exclusive with <code class="docutils literal notranslate"><span class="pre">aws_security_group</span></code> and <code class="docutils literal notranslate"><span class="pre">ip_address</span></code>.</p></li>
<li><p><strong>comment</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Comment to add to the whitelist entry.</p></li>
<li><p><strong>ip_address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Whitelisted IP address. Mutually exclusive with <code class="docutils literal notranslate"><span class="pre">aws_security_group</span></code> and <code class="docutils literal notranslate"><span class="pre">cidr_block</span></code>.</p></li>
<li><p><strong>project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which to add the whitelist entry.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_mongodbatlas.ProjectIpWhitelist.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">aws_security_group</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cidr_block</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">comment</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ip_address</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_mongodbatlas.project_ip_whitelist.ProjectIpWhitelist<a class="headerlink" href="#pulumi_mongodbatlas.ProjectIpWhitelist.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ProjectIpWhitelist resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>aws_security_group</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – ID of the whitelisted AWS security group. Mutually exclusive with <code class="docutils literal notranslate"><span class="pre">cidr_block</span></code> and <code class="docutils literal notranslate"><span class="pre">ip_address</span></code>.</p></li>
<li><p><strong>cidr_block</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Whitelist entry in Classless Inter-Domain Routing (CIDR) notation. Mutually exclusive with <code class="docutils literal notranslate"><span class="pre">aws_security_group</span></code> and <code class="docutils literal notranslate"><span class="pre">ip_address</span></code>.</p></li>
<li><p><strong>comment</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Comment to add to the whitelist entry.</p></li>
<li><p><strong>ip_address</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Whitelisted IP address. Mutually exclusive with <code class="docutils literal notranslate"><span class="pre">aws_security_group</span></code> and <code class="docutils literal notranslate"><span class="pre">cidr_block</span></code>.</p></li>
<li><p><strong>project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which to add the whitelist entry.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.ProjectIpWhitelist.aws_security_group">
<em class="property">property </em><code class="sig-name descname">aws_security_group</code><a class="headerlink" href="#pulumi_mongodbatlas.ProjectIpWhitelist.aws_security_group" title="Permalink to this definition">¶</a></dt>
<dd><p>ID of the whitelisted AWS security group. Mutually exclusive with <code class="docutils literal notranslate"><span class="pre">cidr_block</span></code> and <code class="docutils literal notranslate"><span class="pre">ip_address</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.ProjectIpWhitelist.cidr_block">
<em class="property">property </em><code class="sig-name descname">cidr_block</code><a class="headerlink" href="#pulumi_mongodbatlas.ProjectIpWhitelist.cidr_block" title="Permalink to this definition">¶</a></dt>
<dd><p>Whitelist entry in Classless Inter-Domain Routing (CIDR) notation. Mutually exclusive with <code class="docutils literal notranslate"><span class="pre">aws_security_group</span></code> and <code class="docutils literal notranslate"><span class="pre">ip_address</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.ProjectIpWhitelist.comment">
<em class="property">property </em><code class="sig-name descname">comment</code><a class="headerlink" href="#pulumi_mongodbatlas.ProjectIpWhitelist.comment" title="Permalink to this definition">¶</a></dt>
<dd><p>Comment to add to the whitelist entry.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.ProjectIpWhitelist.ip_address">
<em class="property">property </em><code class="sig-name descname">ip_address</code><a class="headerlink" href="#pulumi_mongodbatlas.ProjectIpWhitelist.ip_address" title="Permalink to this definition">¶</a></dt>
<dd><p>Whitelisted IP address. Mutually exclusive with <code class="docutils literal notranslate"><span class="pre">aws_security_group</span></code> and <code class="docutils literal notranslate"><span class="pre">cidr_block</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.ProjectIpWhitelist.project_id">
<em class="property">property </em><code class="sig-name descname">project_id</code><a class="headerlink" href="#pulumi_mongodbatlas.ProjectIpWhitelist.project_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which to add the whitelist entry.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.ProjectIpWhitelist.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.ProjectIpWhitelist.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_mongodbatlas.ProjectIpWhitelist.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.ProjectIpWhitelist.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py class">
<dt id="pulumi_mongodbatlas.Provider">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">Provider</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">private_key</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">public_key</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.Provider" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider type for the mongodbatlas package. By default, resources use package-wide configuration
settings, however an explicit <code class="docutils literal notranslate"><span class="pre">Provider</span></code> instance may be created and passed during resource
construction to achieve fine-grained programmatic control over provider settings. See the
<a class="reference external" href="https://www.pulumi.com/docs/reference/programming-model/#providers">documentation</a> for more information.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>private_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – MongoDB Atlas Programmatic Private Key</p></li>
<li><p><strong>public_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – MongoDB Atlas Programmatic Public Key</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_mongodbatlas.Provider.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.Provider.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_mongodbatlas.Provider.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.Provider.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py class">
<dt id="pulumi_mongodbatlas.Team">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">Team</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">org_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">usernames</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.Team" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">Teams</span></code> provides a Team resource. The resource lets you create, edit and delete Teams. Also, Teams can be assigned to multiple projects, and team members’ access to the project is determined by the team’s project role.</p>
<blockquote>
<div><p><strong>IMPORTANT:</strong> MongoDB Atlas Team limits: max 250 teams in an organization and max 100 teams per project.</p>
<p><strong>NOTE:</strong> Groups and projects are synonymous terms. You may find group_id in the official documentation.</p>
</div></blockquote>
<p>MongoDB Atlas Team limits: max 250 teams in an organization and max 100 teams per project.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_mongodbatlas</span> <span class="k">as</span> <span class="nn">mongodbatlas</span>

<span class="n">test</span> <span class="o">=</span> <span class="n">mongodbatlas</span><span class="o">.</span><span class="n">Teams</span><span class="p">(</span><span class="s2">&quot;test&quot;</span><span class="p">,</span>
    <span class="n">org_id</span><span class="o">=</span><span class="s2">&quot;&lt;ORGANIZATION-ID&gt;&quot;</span><span class="p">,</span>
    <span class="n">usernames</span><span class="o">=</span><span class="p">[</span>
        <span class="s2">&quot;user1@email.com&quot;</span><span class="p">,</span>
        <span class="s2">&quot;user2@email.com&quot;</span><span class="p">,</span>
        <span class="s2">&quot;user3@email.com&quot;</span><span class="p">,</span>
    <span class="p">])</span>
</pre></div>
</div>
<p>Teams can be imported using the organization ID and team id, in the format ORGID-TEAMID, e.g.</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>   $ pulumi import mongodbatlas:index/team:Team my_team 1112222b3bf99403840e8934-1112222b3bf99403840e8935

See detailed information <span class="k">for</span> arguments and attributes<span class="se">\ </span><span class="sb">`</span>MongoDB API Teams &lt;https://docs.atlas.mongodb.com/reference/api/teams-create-one/&gt;<span class="sb">`</span>_
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the team you want to create.</p></li>
<li><p><strong>org_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique identifier for the organization you want to associate the team with.</p></li>
<li><p><strong>usernames</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – The Atlas usernames (email address). You can only add Atlas users who are part of the organization. Users who have not accepted an invitation to join the organization cannot be added as team members. There is a maximum of 250 Atlas users per team.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_mongodbatlas.Team.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">org_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">team_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">usernames</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_mongodbatlas.team.Team<a class="headerlink" href="#pulumi_mongodbatlas.Team.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Team resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the team you want to create.</p></li>
<li><p><strong>org_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique identifier for the organization you want to associate the team with.</p></li>
<li><p><strong>team_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique identifier for the team.</p></li>
<li><p><strong>usernames</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – The Atlas usernames (email address). You can only add Atlas users who are part of the organization. Users who have not accepted an invitation to join the organization cannot be added as team members. There is a maximum of 250 Atlas users per team.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.Team.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_mongodbatlas.Team.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the team you want to create.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.Team.org_id">
<em class="property">property </em><code class="sig-name descname">org_id</code><a class="headerlink" href="#pulumi_mongodbatlas.Team.org_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The unique identifier for the organization you want to associate the team with.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.Team.team_id">
<em class="property">property </em><code class="sig-name descname">team_id</code><a class="headerlink" href="#pulumi_mongodbatlas.Team.team_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The unique identifier for the team.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.Team.usernames">
<em class="property">property </em><code class="sig-name descname">usernames</code><a class="headerlink" href="#pulumi_mongodbatlas.Team.usernames" title="Permalink to this definition">¶</a></dt>
<dd><p>The Atlas usernames (email address). You can only add Atlas users who are part of the organization. Users who have not accepted an invitation to join the organization cannot be added as team members. There is a maximum of 250 Atlas users per team.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.Team.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.Team.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_mongodbatlas.Team.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.Team.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py class">
<dt id="pulumi_mongodbatlas.Teams">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">Teams</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">org_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">usernames</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.Teams" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a Teams resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.</p>
<dl class="py method">
<dt id="pulumi_mongodbatlas.Teams.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">org_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">team_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">usernames</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_mongodbatlas.teams.Teams<a class="headerlink" href="#pulumi_mongodbatlas.Teams.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Teams resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.Teams.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.Teams.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_mongodbatlas.Teams.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.Teams.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py class">
<dt id="pulumi_mongodbatlas.ThirdPartyIntegration">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">ThirdPartyIntegration</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">api_key</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">api_token</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">channel_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">flow_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">license_key</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">org_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">read_token</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">region</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">routing_key</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">secret</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_key</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">team_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">url</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">write_token</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.ThirdPartyIntegration" title="Permalink to this definition">¶</a></dt>
<dd><p>Third-Party Integration Settings can be imported using project ID and the integration type, in the format <code class="docutils literal notranslate"><span class="pre">project_id</span></code>-<code class="docutils literal notranslate"><span class="pre">type</span></code>, e.g.</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>   $ pulumi import mongodbatlas:index/thirdPartyIntegration:ThirdPartyIntegration my_user 1112222b3bf99403840e8934-OPS_GENIE

See <span class="sb">`</span>MongoDB Atlas API &lt;https://docs.atlas.mongodb.com/reference/api/third-party-integration-settings-create/&gt;<span class="sb">`</span>_ Documentation <span class="k">for</span> more information.
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>account_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Unique identifier of your New Relic account.</p></li>
<li><p><strong>api_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Your API Key.</p></li>
<li><p><strong>api_token</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Your API Token.</p></li>
<li><p><strong>flow_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Your Flowdock Flow name.</p></li>
<li><p><strong>license_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Your License Key.</p></li>
<li><p><strong>org_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Your Flowdock organization name.</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>* `WEBHOOK`
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique ID for the project to get all Third-Party service integrations</p></li>
<li><p><strong>read_token</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Your Insights Query Key.</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>* `OPS_GENIE`
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Indicates which API URL to use, either US or EU. Opsgenie will use US by default.</p>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>* `VICTOR_OPS`
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>routing_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – An optional field for your Routing Key.</p>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>* `FLOWDOCK`
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>secret</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – An optional field for your webhook secret.</p></li>
<li><p><strong>service_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Your Service Key.</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>* `DATADOG`
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Third-Party Integration Settings type</p>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="o">*</span> <span class="n">PAGER_DUTY</span>
<span class="o">*</span> <span class="n">DATADOG</span>
<span class="o">*</span> <span class="n">NEW_RELIC</span>
<span class="o">*</span> <span class="n">OPS_GENIE</span>
<span class="o">*</span> <span class="n">VICTOR_OPS</span>
<span class="o">*</span> <span class="n">FLOWDOCK</span>
<span class="o">*</span> <span class="n">WEBHOOK</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Your webhook URL.</p></li>
<li><p><strong>write_token</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Your Insights Insert Key.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_mongodbatlas.ThirdPartyIntegration.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">api_key</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">api_token</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">channel_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">flow_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">license_key</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">org_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">read_token</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">region</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">routing_key</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">secret</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_key</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">team_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">url</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">write_token</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_mongodbatlas.third_party_integration.ThirdPartyIntegration<a class="headerlink" href="#pulumi_mongodbatlas.ThirdPartyIntegration.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ThirdPartyIntegration resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>account_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Unique identifier of your New Relic account.</p></li>
<li><p><strong>api_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Your API Key.</p></li>
<li><p><strong>api_token</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Your API Token.</p></li>
<li><p><strong>flow_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Your Flowdock Flow name.</p></li>
<li><p><strong>license_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Your License Key.</p></li>
<li><p><strong>org_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Your Flowdock organization name.</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>* `WEBHOOK`
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique ID for the project to get all Third-Party service integrations</p></li>
<li><p><strong>read_token</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Your Insights Query Key.</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>* `OPS_GENIE`
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>region</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Indicates which API URL to use, either US or EU. Opsgenie will use US by default.</p>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>* `VICTOR_OPS`
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>routing_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – An optional field for your Routing Key.</p>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>* `FLOWDOCK`
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>secret</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – An optional field for your webhook secret.</p></li>
<li><p><strong>service_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Your Service Key.</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>* `DATADOG`
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Third-Party Integration Settings type</p>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="o">*</span> <span class="n">PAGER_DUTY</span>
<span class="o">*</span> <span class="n">DATADOG</span>
<span class="o">*</span> <span class="n">NEW_RELIC</span>
<span class="o">*</span> <span class="n">OPS_GENIE</span>
<span class="o">*</span> <span class="n">VICTOR_OPS</span>
<span class="o">*</span> <span class="n">FLOWDOCK</span>
<span class="o">*</span> <span class="n">WEBHOOK</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Your webhook URL.</p></li>
<li><p><strong>write_token</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Your Insights Insert Key.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.ThirdPartyIntegration.account_id">
<em class="property">property </em><code class="sig-name descname">account_id</code><a class="headerlink" href="#pulumi_mongodbatlas.ThirdPartyIntegration.account_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Unique identifier of your New Relic account.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.ThirdPartyIntegration.api_key">
<em class="property">property </em><code class="sig-name descname">api_key</code><a class="headerlink" href="#pulumi_mongodbatlas.ThirdPartyIntegration.api_key" title="Permalink to this definition">¶</a></dt>
<dd><p>Your API Key.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.ThirdPartyIntegration.api_token">
<em class="property">property </em><code class="sig-name descname">api_token</code><a class="headerlink" href="#pulumi_mongodbatlas.ThirdPartyIntegration.api_token" title="Permalink to this definition">¶</a></dt>
<dd><p>Your API Token.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.ThirdPartyIntegration.flow_name">
<em class="property">property </em><code class="sig-name descname">flow_name</code><a class="headerlink" href="#pulumi_mongodbatlas.ThirdPartyIntegration.flow_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Your Flowdock Flow name.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.ThirdPartyIntegration.license_key">
<em class="property">property </em><code class="sig-name descname">license_key</code><a class="headerlink" href="#pulumi_mongodbatlas.ThirdPartyIntegration.license_key" title="Permalink to this definition">¶</a></dt>
<dd><p>Your License Key.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.ThirdPartyIntegration.org_name">
<em class="property">property </em><code class="sig-name descname">org_name</code><a class="headerlink" href="#pulumi_mongodbatlas.ThirdPartyIntegration.org_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Your Flowdock organization name.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">WEBHOOK</span></code></p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.ThirdPartyIntegration.project_id">
<em class="property">property </em><code class="sig-name descname">project_id</code><a class="headerlink" href="#pulumi_mongodbatlas.ThirdPartyIntegration.project_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The unique ID for the project to get all Third-Party service integrations</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.ThirdPartyIntegration.read_token">
<em class="property">property </em><code class="sig-name descname">read_token</code><a class="headerlink" href="#pulumi_mongodbatlas.ThirdPartyIntegration.read_token" title="Permalink to this definition">¶</a></dt>
<dd><p>Your Insights Query Key.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">OPS_GENIE</span></code></p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.ThirdPartyIntegration.region">
<em class="property">property </em><code class="sig-name descname">region</code><a class="headerlink" href="#pulumi_mongodbatlas.ThirdPartyIntegration.region" title="Permalink to this definition">¶</a></dt>
<dd><p>Indicates which API URL to use, either US or EU. Opsgenie will use US by default.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">VICTOR_OPS</span></code></p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.ThirdPartyIntegration.routing_key">
<em class="property">property </em><code class="sig-name descname">routing_key</code><a class="headerlink" href="#pulumi_mongodbatlas.ThirdPartyIntegration.routing_key" title="Permalink to this definition">¶</a></dt>
<dd><p>An optional field for your Routing Key.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">FLOWDOCK</span></code></p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.ThirdPartyIntegration.secret">
<em class="property">property </em><code class="sig-name descname">secret</code><a class="headerlink" href="#pulumi_mongodbatlas.ThirdPartyIntegration.secret" title="Permalink to this definition">¶</a></dt>
<dd><p>An optional field for your webhook secret.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.ThirdPartyIntegration.service_key">
<em class="property">property </em><code class="sig-name descname">service_key</code><a class="headerlink" href="#pulumi_mongodbatlas.ThirdPartyIntegration.service_key" title="Permalink to this definition">¶</a></dt>
<dd><p>Your Service Key.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">DATADOG</span></code></p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.ThirdPartyIntegration.type">
<em class="property">property </em><code class="sig-name descname">type</code><a class="headerlink" href="#pulumi_mongodbatlas.ThirdPartyIntegration.type" title="Permalink to this definition">¶</a></dt>
<dd><p>Third-Party Integration Settings type</p>
<ul class="simple">
<li><p>PAGER_DUTY</p></li>
<li><p>DATADOG</p></li>
<li><p>NEW_RELIC</p></li>
<li><p>OPS_GENIE</p></li>
<li><p>VICTOR_OPS</p></li>
<li><p>FLOWDOCK</p></li>
<li><p>WEBHOOK</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.ThirdPartyIntegration.url">
<em class="property">property </em><code class="sig-name descname">url</code><a class="headerlink" href="#pulumi_mongodbatlas.ThirdPartyIntegration.url" title="Permalink to this definition">¶</a></dt>
<dd><p>Your webhook URL.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.ThirdPartyIntegration.write_token">
<em class="property">property </em><code class="sig-name descname">write_token</code><a class="headerlink" href="#pulumi_mongodbatlas.ThirdPartyIntegration.write_token" title="Permalink to this definition">¶</a></dt>
<dd><p>Your Insights Insert Key.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.ThirdPartyIntegration.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.ThirdPartyIntegration.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_mongodbatlas.ThirdPartyIntegration.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.ThirdPartyIntegration.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py class">
<dt id="pulumi_mongodbatlas.X509AuthenticationDatabaseUser">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">X509AuthenticationDatabaseUser</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">customer_x509_cas</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">months_until_expiration</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">username</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.X509AuthenticationDatabaseUser" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">X509AuthenticationDatabaseUser</span></code> provides a X509 Authentication Database User resource. The X509AuthenticationDatabaseUser resource lets you manage MongoDB users who authenticate using X.509 certificates. You can manage these X.509 certificates or let Atlas do it for you.</p>
<table class="docutils align-default">
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>Management</p></th>
<th class="head"><p>Description</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>Atlas</p></td>
<td><p>Atlas manages your Certificate Authority and can generate certificates for your MongoDB users. No additional X.509 configuration is required.</p></td>
</tr>
<tr class="row-odd"><td><p>Customer</p></td>
<td><p>You must provide a Certificate Authority and generate certificates for your MongoDB users.</p></td>
</tr>
</tbody>
</table>
<blockquote>
<div><p><strong>NOTE:</strong> Groups and projects are synonymous terms. You may find group_id in the official documentation.</p>
</div></blockquote>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_mongodbatlas</span> <span class="k">as</span> <span class="nn">mongodbatlas</span>

<span class="n">user</span> <span class="o">=</span> <span class="n">mongodbatlas</span><span class="o">.</span><span class="n">DatabaseUser</span><span class="p">(</span><span class="s2">&quot;user&quot;</span><span class="p">,</span>
    <span class="n">database_name</span><span class="o">=</span><span class="s2">&quot;$external&quot;</span><span class="p">,</span>
    <span class="n">labels</span><span class="o">=</span><span class="p">[</span><span class="n">mongodbatlas</span><span class="o">.</span><span class="n">DatabaseUserLabelArgs</span><span class="p">(</span>
        <span class="n">key</span><span class="o">=</span><span class="s2">&quot;My Key&quot;</span><span class="p">,</span>
        <span class="n">value</span><span class="o">=</span><span class="s2">&quot;My Value&quot;</span><span class="p">,</span>
    <span class="p">)],</span>
    <span class="n">project_id</span><span class="o">=</span><span class="s2">&quot;&lt;PROJECT-ID&gt;&quot;</span><span class="p">,</span>
    <span class="n">roles</span><span class="o">=</span><span class="p">[</span><span class="n">mongodbatlas</span><span class="o">.</span><span class="n">DatabaseUserRoleArgs</span><span class="p">(</span>
        <span class="n">database_name</span><span class="o">=</span><span class="s2">&quot;admin&quot;</span><span class="p">,</span>
        <span class="n">role_name</span><span class="o">=</span><span class="s2">&quot;atlasAdmin&quot;</span><span class="p">,</span>
    <span class="p">)],</span>
    <span class="n">username</span><span class="o">=</span><span class="s2">&quot;myUsername&quot;</span><span class="p">,</span>
    <span class="n">x509_type</span><span class="o">=</span><span class="s2">&quot;MANAGED&quot;</span><span class="p">)</span>
<span class="n">test</span> <span class="o">=</span> <span class="n">mongodbatlas</span><span class="o">.</span><span class="n">X509AuthenticationDatabaseUser</span><span class="p">(</span><span class="s2">&quot;test&quot;</span><span class="p">,</span>
    <span class="n">months_until_expiration</span><span class="o">=</span><span class="mi">2</span><span class="p">,</span>
    <span class="n">project_id</span><span class="o">=</span><span class="n">user</span><span class="o">.</span><span class="n">project_id</span><span class="p">,</span>
    <span class="n">username</span><span class="o">=</span><span class="n">user</span><span class="o">.</span><span class="n">username</span><span class="p">)</span>
</pre></div>
</div>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_mongodbatlas</span> <span class="k">as</span> <span class="nn">mongodbatlas</span>

<span class="n">test</span> <span class="o">=</span> <span class="n">mongodbatlas</span><span class="o">.</span><span class="n">X509AuthenticationDatabaseUser</span><span class="p">(</span><span class="s2">&quot;test&quot;</span><span class="p">,</span>
    <span class="n">customer_x509_cas</span><span class="o">=</span><span class="s2">&quot;&quot;&quot;  -----BEGIN CERTIFICATE-----</span>
<span class="s2">  MIICmTCCAgICCQDZnHzklxsT9TANBgkqhkiG9w0BAQsFADCBkDELMAkGA1UEBhMC</span>
<span class="s2">  VVMxDjAMBgNVBAgMBVRleGFzMQ8wDQYDVQQHDAZBdXN0aW4xETAPBgNVBAoMCHRl</span>
<span class="s2">  c3QuY29tMQ0wCwYDVQQLDARUZXN0MREwDwYDVQQDDAh0ZXN0LmNvbTErMCkGCSqG</span>
<span class="s2">  SIb3DQEJARYcbWVsaXNzYS5wbHVua2V0dEBtb25nb2RiLmNvbTAeFw0yMDAyMDQy</span>
<span class="s2">  MDQ2MDFaFw0yMTAyMDMyMDQ2MDFaMIGQMQswCQYDVQQGEwJVUzEOMAwGA1UECAwF</span>
<span class="s2">  VGV4YXMxDzANBgNVBAcMBkF1c3RpbjERMA8GA1UECgwIdGVzdC5jb20xDTALBgNV</span>
<span class="s2">  BAsMBFRlc3QxETAPBgNVBAMMCHRlc3QuY29tMSswKQYJKoZIhvcNAQkBFhxtZWxp</span>
<span class="s2">  c3NhLnBsdW5rZXR0QG1vbmdvZGIuY29tMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCB</span>
<span class="s2">  iQKBgQCf1LRqr1zftzdYx2Aj9G76tb0noMPtj6faGLlPji1+m6Rn7RWD9L0ntWAr</span>
<span class="s2">  cURxvypa9jZ9MXFzDtLevvd3tHEmfrUT3ukNDX6+Jtc4kWm+Dh2A70Pd+deKZ2/O</span>
<span class="s2">  Fh8audEKAESGXnTbeJCeQa1XKlIkjqQHBNwES5h1b9vJtFoLJwIDAQABMA0GCSqG</span>
<span class="s2">  SIb3DQEBCwUAA4GBADMUncjEPV/MiZUcVNGmktP6BPmEqMXQWUDpdGW2+Tg2JtUA</span>
<span class="s2">  7MMILtepBkFzLO+GlpZxeAlXO0wxiNgEmCRONgh4+t2w3e7a8GFijYQ99FHrAC5A</span>
<span class="s2">  iul59bdl18gVqXia1Yeq/iK7Ohfy/Jwd7Hsm530elwkM/ZEkYDjBlZSXYdyz</span>
<span class="s2">  -----END CERTIFICATE-----&quot;</span>

<span class="s2">&quot;&quot;&quot;</span><span class="p">,</span>
    <span class="n">project_id</span><span class="o">=</span><span class="s2">&quot;&lt;PROJECT-ID&gt;&quot;</span><span class="p">)</span>
</pre></div>
</div>
<p>X.509 Certificates for a User can be imported using project ID and username, in the format <code class="docutils literal notranslate"><span class="pre">project_id-username</span></code>, e.g.</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>   $ pulumi import mongodbatlas:index/x509AuthenticationDatabaseUser:X509AuthenticationDatabaseUser <span class="nb">test</span> 1112222b3bf99403840e8934-myUsername

For more information see<span class="se">\ </span><span class="sb">`</span>MongoDB Atlas API Reference. &lt;https://docs.atlas.mongodb.com/reference/api/x509-configuration-get-certificates/&gt;<span class="sb">`</span>_ Current X.509 Configuration can be imported using project ID, in the format <span class="sb">``</span>project_id<span class="sb">``</span><span class="se">\ </span>, e.g.
</pre></div>
</div>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>   $ pulumi import mongodbatlas:index/x509AuthenticationDatabaseUser:X509AuthenticationDatabaseUser <span class="nb">test</span> 1112222b3bf99403840e8934

For more information see<span class="se">\ </span><span class="sb">`</span>MongoDB Atlas API Reference. &lt;https://docs.atlas.mongodb.com/reference/api/x509-configuration-get-certificates/&gt;<span class="sb">`</span>_
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>customer_x509_cas</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – PEM string containing one or more customer CAs for database user authentication.</p></li>
<li><p><strong>months_until_expiration</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – A number of months that the created certificate is valid for before expiry, up to 24 months. By default is 3.</p></li>
<li><p><strong>project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Identifier for the Atlas project associated with the X.509 configuration.</p></li>
<li><p><strong>username</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Username of the database user to create a certificate for.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_mongodbatlas.X509AuthenticationDatabaseUser.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">certificates</span><span class="p">:</span> <span class="n">Union[Sequence[Union[X509AuthenticationDatabaseUserCertificateArgs, Mapping[str, Any], Awaitable[Union[X509AuthenticationDatabaseUserCertificateArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[X509AuthenticationDatabaseUserCertificateArgs, Mapping[str, Any], Awaitable[Union[X509AuthenticationDatabaseUserCertificateArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">current_certificate</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">customer_x509_cas</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">months_until_expiration</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">username</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_mongodbatlas.x509_authentication_database_user.X509AuthenticationDatabaseUser<a class="headerlink" href="#pulumi_mongodbatlas.X509AuthenticationDatabaseUser.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing X509AuthenticationDatabaseUser resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>certificates</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'X509AuthenticationDatabaseUserCertificateArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – Array of objects where each details one unexpired database user certificate.</p></li>
<li><p><strong>current_certificate</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Contains the last X.509 certificate and private key created for a database user.</p></li>
<li><p><strong>customer_x509_cas</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – PEM string containing one or more customer CAs for database user authentication.</p></li>
<li><p><strong>months_until_expiration</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – A number of months that the created certificate is valid for before expiry, up to 24 months. By default is 3.</p></li>
<li><p><strong>project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Identifier for the Atlas project associated with the X.509 configuration.</p></li>
<li><p><strong>username</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Username of the database user to create a certificate for.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.X509AuthenticationDatabaseUser.certificates">
<em class="property">property </em><code class="sig-name descname">certificates</code><a class="headerlink" href="#pulumi_mongodbatlas.X509AuthenticationDatabaseUser.certificates" title="Permalink to this definition">¶</a></dt>
<dd><p>Array of objects where each details one unexpired database user certificate.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.X509AuthenticationDatabaseUser.current_certificate">
<em class="property">property </em><code class="sig-name descname">current_certificate</code><a class="headerlink" href="#pulumi_mongodbatlas.X509AuthenticationDatabaseUser.current_certificate" title="Permalink to this definition">¶</a></dt>
<dd><p>Contains the last X.509 certificate and private key created for a database user.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.X509AuthenticationDatabaseUser.customer_x509_cas">
<em class="property">property </em><code class="sig-name descname">customer_x509_cas</code><a class="headerlink" href="#pulumi_mongodbatlas.X509AuthenticationDatabaseUser.customer_x509_cas" title="Permalink to this definition">¶</a></dt>
<dd><p>PEM string containing one or more customer CAs for database user authentication.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.X509AuthenticationDatabaseUser.months_until_expiration">
<em class="property">property </em><code class="sig-name descname">months_until_expiration</code><a class="headerlink" href="#pulumi_mongodbatlas.X509AuthenticationDatabaseUser.months_until_expiration" title="Permalink to this definition">¶</a></dt>
<dd><p>A number of months that the created certificate is valid for before expiry, up to 24 months. By default is 3.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.X509AuthenticationDatabaseUser.project_id">
<em class="property">property </em><code class="sig-name descname">project_id</code><a class="headerlink" href="#pulumi_mongodbatlas.X509AuthenticationDatabaseUser.project_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Identifier for the Atlas project associated with the X.509 configuration.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.X509AuthenticationDatabaseUser.username">
<em class="property">property </em><code class="sig-name descname">username</code><a class="headerlink" href="#pulumi_mongodbatlas.X509AuthenticationDatabaseUser.username" title="Permalink to this definition">¶</a></dt>
<dd><p>Username of the database user to create a certificate for.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_mongodbatlas.X509AuthenticationDatabaseUser.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.X509AuthenticationDatabaseUser.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_mongodbatlas.X509AuthenticationDatabaseUser.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_mongodbatlas.X509AuthenticationDatabaseUser.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="py function">
<dt id="pulumi_mongodbatlas.get509_authentication_database_user">
<code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">get509_authentication_database_user</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">project_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">username</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_mongodbatlas.get509_authentication_database_user.AwaitableGet509AuthenticationDatabaseUserResult<a class="headerlink" href="#pulumi_mongodbatlas.get509_authentication_database_user" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">X509AuthenticationDatabaseUser</span></code> describe a X509 Authentication Database User. This represents a X509 Authentication Database User.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Groups and projects are synonymous terms. You may find group_id in the official documentation.</p>
</div></blockquote>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_mongodbatlas</span> <span class="k">as</span> <span class="nn">mongodbatlas</span>

<span class="n">user</span> <span class="o">=</span> <span class="n">mongodbatlas</span><span class="o">.</span><span class="n">DatabaseUser</span><span class="p">(</span><span class="s2">&quot;user&quot;</span><span class="p">,</span>
    <span class="n">database_name</span><span class="o">=</span><span class="s2">&quot;$external&quot;</span><span class="p">,</span>
    <span class="n">labels</span><span class="o">=</span><span class="p">[</span><span class="n">mongodbatlas</span><span class="o">.</span><span class="n">DatabaseUserLabelArgs</span><span class="p">(</span>
        <span class="n">key</span><span class="o">=</span><span class="s2">&quot;My Key&quot;</span><span class="p">,</span>
        <span class="n">value</span><span class="o">=</span><span class="s2">&quot;My Value&quot;</span><span class="p">,</span>
    <span class="p">)],</span>
    <span class="n">project_id</span><span class="o">=</span><span class="s2">&quot;&lt;PROJECT-ID&gt;&quot;</span><span class="p">,</span>
    <span class="n">roles</span><span class="o">=</span><span class="p">[</span><span class="n">mongodbatlas</span><span class="o">.</span><span class="n">DatabaseUserRoleArgs</span><span class="p">(</span>
        <span class="n">database_name</span><span class="o">=</span><span class="s2">&quot;admin&quot;</span><span class="p">,</span>
        <span class="n">role_name</span><span class="o">=</span><span class="s2">&quot;atlasAdmin&quot;</span><span class="p">,</span>
    <span class="p">)],</span>
    <span class="n">username</span><span class="o">=</span><span class="s2">&quot;myUsername&quot;</span><span class="p">,</span>
    <span class="n">x509_type</span><span class="o">=</span><span class="s2">&quot;MANAGED&quot;</span><span class="p">)</span>
<span class="n">test_x509_authentication_database_user</span> <span class="o">=</span> <span class="n">mongodbatlas</span><span class="o">.</span><span class="n">X509AuthenticationDatabaseUser</span><span class="p">(</span><span class="s2">&quot;testX509AuthenticationDatabaseUser&quot;</span><span class="p">,</span>
    <span class="n">months_until_expiration</span><span class="o">=</span><span class="mi">2</span><span class="p">,</span>
    <span class="n">project_id</span><span class="o">=</span><span class="n">user</span><span class="o">.</span><span class="n">project_id</span><span class="p">,</span>
    <span class="n">username</span><span class="o">=</span><span class="n">user</span><span class="o">.</span><span class="n">username</span><span class="p">)</span>
<span class="n">test509_authentication_database_user</span> <span class="o">=</span> <span class="n">pulumi</span><span class="o">.</span><span class="n">Output</span><span class="o">.</span><span class="n">all</span><span class="p">(</span><span class="n">test_x509_authentication_database_user</span><span class="o">.</span><span class="n">project_id</span><span class="p">,</span> <span class="n">test_x509_authentication_database_user</span><span class="o">.</span><span class="n">username</span><span class="p">)</span><span class="o">.</span><span class="n">apply</span><span class="p">(</span><span class="k">lambda</span> <span class="n">project_id</span><span class="p">,</span> <span class="n">username</span><span class="p">:</span> <span class="n">mongodbatlas</span><span class="o">.</span><span class="n">get509_authentication_database_user</span><span class="p">(</span><span class="n">project_id</span><span class="o">=</span><span class="n">project_id</span><span class="p">,</span>
    <span class="n">username</span><span class="o">=</span><span class="n">username</span><span class="p">))</span>
</pre></div>
</div>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_mongodbatlas</span> <span class="k">as</span> <span class="nn">mongodbatlas</span>

<span class="n">test_x509_authentication_database_user</span> <span class="o">=</span> <span class="n">mongodbatlas</span><span class="o">.</span><span class="n">X509AuthenticationDatabaseUser</span><span class="p">(</span><span class="s2">&quot;testX509AuthenticationDatabaseUser&quot;</span><span class="p">,</span>
    <span class="n">customer_x509_cas</span><span class="o">=</span><span class="s2">&quot;&quot;&quot;  -----BEGIN CERTIFICATE-----</span>
<span class="s2">  MIICmTCCAgICCQDZnHzklxsT9TANBgkqhkiG9w0BAQsFADCBkDELMAkGA1UEBhMC</span>
<span class="s2">  VVMxDjAMBgNVBAgMBVRleGFzMQ8wDQYDVQQHDAZBdXN0aW4xETAPBgNVBAoMCHRl</span>
<span class="s2">  c3QuY29tMQ0wCwYDVQQLDARUZXN0MREwDwYDVQQDDAh0ZXN0LmNvbTErMCkGCSqG</span>
<span class="s2">  SIb3DQEJARYcbWVsaXNzYS5wbHVua2V0dEBtb25nb2RiLmNvbTAeFw0yMDAyMDQy</span>
<span class="s2">  MDQ2MDFaFw0yMTAyMDMyMDQ2MDFaMIGQMQswCQYDVQQGEwJVUzEOMAwGA1UECAwF</span>
<span class="s2">  VGV4YXMxDzANBgNVBAcMBkF1c3RpbjERMA8GA1UECgwIdGVzdC5jb20xDTALBgNV</span>
<span class="s2">  BAsMBFRlc3QxETAPBgNVBAMMCHRlc3QuY29tMSswKQYJKoZIhvcNAQkBFhxtZWxp</span>
<span class="s2">  c3NhLnBsdW5rZXR0QG1vbmdvZGIuY29tMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCB</span>
<span class="s2">  iQKBgQCf1LRqr1zftzdYx2Aj9G76tb0noMPtj6faGLlPji1+m6Rn7RWD9L0ntWAr</span>
<span class="s2">  cURxvypa9jZ9MXFzDtLevvd3tHEmfrUT3ukNDX6+Jtc4kWm+Dh2A70Pd+deKZ2/O</span>
<span class="s2">  Fh8audEKAESGXnTbeJCeQa1XKlIkjqQHBNwES5h1b9vJtFoLJwIDAQABMA0GCSqG</span>
<span class="s2">  SIb3DQEBCwUAA4GBADMUncjEPV/MiZUcVNGmktP6BPmEqMXQWUDpdGW2+Tg2JtUA</span>
<span class="s2">  7MMILtepBkFzLO+GlpZxeAlXO0wxiNgEmCRONgh4+t2w3e7a8GFijYQ99FHrAC5A</span>
<span class="s2">  iul59bdl18gVqXia1Yeq/iK7Ohfy/Jwd7Hsm530elwkM/ZEkYDjBlZSXYdyz</span>
<span class="s2">  -----END CERTIFICATE-----&quot;</span>

<span class="s2">&quot;&quot;&quot;</span><span class="p">,</span>
    <span class="n">project_id</span><span class="o">=</span><span class="s2">&quot;&lt;PROJECT-ID&gt;&quot;</span><span class="p">)</span>
<span class="n">test509_authentication_database_user</span> <span class="o">=</span> <span class="n">test_x509_authentication_database_user</span><span class="o">.</span><span class="n">project_id</span><span class="o">.</span><span class="n">apply</span><span class="p">(</span><span class="k">lambda</span> <span class="n">project_id</span><span class="p">:</span> <span class="n">mongodbatlas</span><span class="o">.</span><span class="n">get509_authentication_database_user</span><span class="p">(</span><span class="n">project_id</span><span class="o">=</span><span class="n">project_id</span><span class="p">))</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>project_id</strong> (<em>str</em>) – Identifier for the Atlas project associated with the X.509 configuration.</p></li>
<li><p><strong>username</strong> (<em>str</em>) – Username of the database user to create a certificate for.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_mongodbatlas.get_alert_configuration">
<code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">get_alert_configuration</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">alert_configuration_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_mongodbatlas.get_alert_configuration.AwaitableGetAlertConfigurationResult<a class="headerlink" href="#pulumi_mongodbatlas.get_alert_configuration" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">AlertConfiguration</span></code> describes an Alert Configuration.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Groups and projects are synonymous terms. You may find <strong>group_id</strong> in the official documentation.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>alert_configuration_id</strong> (<em>str</em>) – Unique identifier for the alert configuration.</p></li>
<li><p><strong>project_id</strong> (<em>str</em>) – The ID of the project where the alert configuration will create.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_mongodbatlas.get_auditing">
<code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">get_auditing</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">project_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_mongodbatlas.get_auditing.AwaitableGetAuditingResult<a class="headerlink" href="#pulumi_mongodbatlas.get_auditing" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">Auditing</span></code> describes a Auditing.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Groups and projects are synonymous terms. You may find <strong>group_id</strong> in the official documentation.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>project_id</strong> (<em>str</em>) – The unique ID for the project to create the database user.</p>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_mongodbatlas.get_cloud_provider_access">
<code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">get_cloud_provider_access</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">project_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_mongodbatlas.get_cloud_provider_access.AwaitableGetCloudProviderAccessResult<a class="headerlink" href="#pulumi_mongodbatlas.get_cloud_provider_access" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">CloudProviderAccess</span></code> allows you to get the list of cloud provider access roles, currently only AWS is supported.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Groups and projects are synonymous terms. You may find <code class="docutils literal notranslate"><span class="pre">groupId</span></code> in the official documentation.</p>
</div></blockquote>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_mongodbatlas</span> <span class="k">as</span> <span class="nn">mongodbatlas</span>

<span class="n">test_role</span> <span class="o">=</span> <span class="n">mongodbatlas</span><span class="o">.</span><span class="n">CloudProviderAccess</span><span class="p">(</span><span class="s2">&quot;testRole&quot;</span><span class="p">,</span>
    <span class="n">project_id</span><span class="o">=</span><span class="s2">&quot;&lt;PROJECT-ID&gt;&quot;</span><span class="p">,</span>
    <span class="n">provider_name</span><span class="o">=</span><span class="s2">&quot;AWS&quot;</span><span class="p">)</span>
<span class="nb">all</span> <span class="o">=</span> <span class="n">test_role</span><span class="o">.</span><span class="n">project_id</span><span class="o">.</span><span class="n">apply</span><span class="p">(</span><span class="k">lambda</span> <span class="n">project_id</span><span class="p">:</span> <span class="n">mongodbatlas</span><span class="o">.</span><span class="n">get_cloud_provider_access</span><span class="p">(</span><span class="n">project_id</span><span class="o">=</span><span class="n">project_id</span><span class="p">))</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>project_id</strong> (<em>str</em>) – The unique ID for the project to get all Cloud Provider Access</p>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_mongodbatlas.get_cloud_provider_snapshot">
<code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">get_cloud_provider_snapshot</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">cluster_name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">snapshot_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_mongodbatlas.get_cloud_provider_snapshot.AwaitableGetCloudProviderSnapshotResult<a class="headerlink" href="#pulumi_mongodbatlas.get_cloud_provider_snapshot" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">CloudProviderSnapshot</span></code> provides an Cloud Backup Snapshot datasource. Atlas Cloud Backup Snapshots provide localized backup storage using the native snapshot functionality of the cluster’s cloud service.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Groups and projects are synonymous terms. You may find <code class="docutils literal notranslate"><span class="pre">groupId</span></code> in the official documentation.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>cluster_name</strong> (<em>str</em>) – The name of the Atlas cluster that contains the snapshot you want to retrieve.</p></li>
<li><p><strong>snapshot_id</strong> (<em>str</em>) – The unique identifier of the snapshot you want to retrieve.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_mongodbatlas.get_cloud_provider_snapshot_backup_policy">
<code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">get_cloud_provider_snapshot_backup_policy</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">cluster_name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_mongodbatlas.get_cloud_provider_snapshot_backup_policy.AwaitableGetCloudProviderSnapshotBackupPolicyResult<a class="headerlink" href="#pulumi_mongodbatlas.get_cloud_provider_snapshot_backup_policy" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">CloudProviderSnapshotBackupPolicy</span></code> provides a Cloud Backup Snapshot Backup Policy datasource. An Atlas Cloud Backup Snapshot Policy provides the current snapshot schedule and retention settings for the cluster.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Groups and projects are synonymous terms. You may find <code class="docutils literal notranslate"><span class="pre">groupId</span></code> in the official documentation.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>cluster_name</strong> (<em>str</em>) – The name of the Atlas cluster that contains the snapshots backup policy you want to retrieve.</p></li>
<li><p><strong>project_id</strong> (<em>str</em>) – The unique identifier of the project for the Atlas cluster.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_mongodbatlas.get_cloud_provider_snapshot_restore_job">
<code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">get_cloud_provider_snapshot_restore_job</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">cluster_name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">job_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_mongodbatlas.get_cloud_provider_snapshot_restore_job.AwaitableGetCloudProviderSnapshotRestoreJobResult<a class="headerlink" href="#pulumi_mongodbatlas.get_cloud_provider_snapshot_restore_job" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">CloudProviderSnapshotRestoreJob</span></code> provides a Cloud Backup Snapshot Restore Job datasource. Gets all the cloud backup snapshot restore jobs for the specified cluster.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Groups and projects are synonymous terms. You may find <code class="docutils literal notranslate"><span class="pre">groupId</span></code> in the official documentation.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>cluster_name</strong> (<em>str</em>) – The name of the Atlas cluster for which you want to retrieve the restore job.</p></li>
<li><p><strong>job_id</strong> (<em>str</em>) – The unique identifier of the restore job to retrieve.</p></li>
<li><p><strong>project_id</strong> (<em>str</em>) – The unique identifier of the project for the Atlas cluster.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_mongodbatlas.get_cloud_provider_snapshot_restore_jobs">
<code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">get_cloud_provider_snapshot_restore_jobs</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">cluster_name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">items_per_page</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>int<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">page_num</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>int<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_mongodbatlas.get_cloud_provider_snapshot_restore_jobs.AwaitableGetCloudProviderSnapshotRestoreJobsResult<a class="headerlink" href="#pulumi_mongodbatlas.get_cloud_provider_snapshot_restore_jobs" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">getCloudProviderSnapshotRestoreJobs</span></code> provides a Cloud Backup Snapshot Restore Jobs datasource. Gets all the cloud backup snapshot restore jobs for the specified cluster.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Groups and projects are synonymous terms. You may find <code class="docutils literal notranslate"><span class="pre">groupId</span></code> in the official documentation.</p>
</div></blockquote>
<p>First create a snapshot of the desired cluster. Then request that snapshot be restored in an automated fashion to the designated cluster and project.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_mongodbatlas</span> <span class="k">as</span> <span class="nn">mongodbatlas</span>

<span class="n">test_cloud_provider_snapshot</span> <span class="o">=</span> <span class="n">mongodbatlas</span><span class="o">.</span><span class="n">CloudProviderSnapshot</span><span class="p">(</span><span class="s2">&quot;testCloudProviderSnapshot&quot;</span><span class="p">,</span>
    <span class="n">cluster_name</span><span class="o">=</span><span class="s2">&quot;MyCluster&quot;</span><span class="p">,</span>
    <span class="n">description</span><span class="o">=</span><span class="s2">&quot;MyDescription&quot;</span><span class="p">,</span>
    <span class="n">project_id</span><span class="o">=</span><span class="s2">&quot;5cf5a45a9ccf6400e60981b6&quot;</span><span class="p">,</span>
    <span class="n">retention_in_days</span><span class="o">=</span><span class="mi">1</span><span class="p">)</span>
<span class="n">test_cloud_provider_snapshot_restore_job</span> <span class="o">=</span> <span class="n">mongodbatlas</span><span class="o">.</span><span class="n">CloudProviderSnapshotRestoreJob</span><span class="p">(</span><span class="s2">&quot;testCloudProviderSnapshotRestoreJob&quot;</span><span class="p">,</span>
    <span class="n">cluster_name</span><span class="o">=</span><span class="s2">&quot;MyCluster&quot;</span><span class="p">,</span>
    <span class="n">delivery_type</span><span class="o">=</span><span class="n">mongodbatlas</span><span class="o">.</span><span class="n">CloudProviderSnapshotRestoreJobDeliveryTypeArgs</span><span class="p">(</span>
        <span class="n">automated</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
        <span class="n">target_cluster_name</span><span class="o">=</span><span class="s2">&quot;MyCluster&quot;</span><span class="p">,</span>
        <span class="n">target_project_id</span><span class="o">=</span><span class="s2">&quot;5cf5a45a9ccf6400e60981b6&quot;</span><span class="p">,</span>
    <span class="p">),</span>
    <span class="n">project_id</span><span class="o">=</span><span class="s2">&quot;5cf5a45a9ccf6400e60981b6&quot;</span><span class="p">,</span>
    <span class="n">snapshot_id</span><span class="o">=</span><span class="n">test_cloud_provider_snapshot</span><span class="o">.</span><span class="n">id</span><span class="p">)</span>
<span class="n">test_cloud_provider_snapshot_restore_jobs</span> <span class="o">=</span> <span class="n">pulumi</span><span class="o">.</span><span class="n">Output</span><span class="o">.</span><span class="n">all</span><span class="p">(</span><span class="n">test_cloud_provider_snapshot_restore_job</span><span class="o">.</span><span class="n">cluster_name</span><span class="p">,</span> <span class="n">test_cloud_provider_snapshot_restore_job</span><span class="o">.</span><span class="n">project_id</span><span class="p">)</span><span class="o">.</span><span class="n">apply</span><span class="p">(</span><span class="k">lambda</span> <span class="n">cluster_name</span><span class="p">,</span> <span class="n">project_id</span><span class="p">:</span> <span class="n">mongodbatlas</span><span class="o">.</span><span class="n">get_cloud_provider_snapshot_restore_jobs</span><span class="p">(</span><span class="n">cluster_name</span><span class="o">=</span><span class="n">cluster_name</span><span class="p">,</span>
    <span class="n">items_per_page</span><span class="o">=</span><span class="mi">5</span><span class="p">,</span>
    <span class="n">page_num</span><span class="o">=</span><span class="mi">1</span><span class="p">,</span>
    <span class="n">project_id</span><span class="o">=</span><span class="n">project_id</span><span class="p">))</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>cluster_name</strong> (<em>str</em>) – The name of the Atlas cluster for which you want to retrieve restore jobs.</p></li>
<li><p><strong>items_per_page</strong> (<em>int</em>) – Number of items to return per page, up to a maximum of 500. Defaults to <code class="docutils literal notranslate"><span class="pre">100</span></code>.</p></li>
<li><p><strong>page_num</strong> (<em>int</em>) – The page to return. Defaults to <code class="docutils literal notranslate"><span class="pre">1</span></code>.</p></li>
<li><p><strong>project_id</strong> (<em>str</em>) – The unique identifier of the project for the Atlas cluster.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_mongodbatlas.get_cloud_provider_snapshots">
<code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">get_cloud_provider_snapshots</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">cluster_name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">items_per_page</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>int<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">page_num</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>int<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_mongodbatlas.get_cloud_provider_snapshots.AwaitableGetCloudProviderSnapshotsResult<a class="headerlink" href="#pulumi_mongodbatlas.get_cloud_provider_snapshots" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">getCloudProviderSnapshots</span></code> provides an Cloud Backup Snapshot datasource. Atlas Cloud Backup Snapshots provide localized backup storage using the native snapshot functionality of the cluster’s cloud service.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Groups and projects are synonymous terms. You may find <code class="docutils literal notranslate"><span class="pre">groupId</span></code> in the official documentation.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>cluster_name</strong> (<em>str</em>) – The name of the Atlas cluster that contains the snapshot you want to retrieve.</p></li>
<li><p><strong>items_per_page</strong> (<em>int</em>) – Number of items to return per page, up to a maximum of 500. Defaults to <code class="docutils literal notranslate"><span class="pre">100</span></code>.</p></li>
<li><p><strong>page_num</strong> (<em>int</em>) – The page to return. Defaults to <code class="docutils literal notranslate"><span class="pre">1</span></code>.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_mongodbatlas.get_cluster">
<code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">get_cluster</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_mongodbatlas.get_cluster.AwaitableGetClusterResult<a class="headerlink" href="#pulumi_mongodbatlas.get_cluster" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">Cluster</span></code> describes a Cluster. The. The data source requires your Project ID.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Groups and projects are synonymous terms. You may find group_id in the official documentation.</p>
<p><strong>IMPORTANT:</strong>
<span class="raw-html-m2r"><br></span> &amp;#8226; Changes to cluster configurations can affect costs. Before making changes, please see <a class="reference external" href="https://docs.atlas.mongodb.com/billing/">Billing</a>.
<span class="raw-html-m2r"><br></span> &amp;#8226; If your Atlas project contains a custom role that uses actions introduced in a specific MongoDB version, you cannot create a cluster with a MongoDB version less than that version unless you delete the custom role.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>name</strong> (<em>str</em>) – Name of the cluster as it appears in Atlas. Once the cluster is created, its name cannot be changed.</p></li>
<li><p><strong>project_id</strong> (<em>str</em>) – The unique ID for the project to create the database user.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_mongodbatlas.get_clusters">
<code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">get_clusters</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">project_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_mongodbatlas.get_clusters.AwaitableGetClustersResult<a class="headerlink" href="#pulumi_mongodbatlas.get_clusters" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">Cluster</span></code> describes all Clusters by the provided project_id. The data source requires your Project ID.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Groups and projects are synonymous terms. You may find group_id in the official documentation.</p>
<p><strong>IMPORTANT:</strong>
<span class="raw-html-m2r"><br></span> &amp;#8226; Changes to cluster configurations can affect costs. Before making changes, please see <a class="reference external" href="https://docs.atlas.mongodb.com/billing/">Billing</a>.
<span class="raw-html-m2r"><br></span> &amp;#8226; If your Atlas project contains a custom role that uses actions introduced in a specific MongoDB version, you cannot create a cluster with a MongoDB version less than that version unless you delete the custom role.</p>
</div></blockquote>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_mongodbatlas</span> <span class="k">as</span> <span class="nn">mongodbatlas</span>

<span class="n">test_cluster</span> <span class="o">=</span> <span class="n">mongodbatlas</span><span class="o">.</span><span class="n">Cluster</span><span class="p">(</span><span class="s2">&quot;testCluster&quot;</span><span class="p">,</span>
    <span class="n">project_id</span><span class="o">=</span><span class="s2">&quot;&lt;YOUR-PROJECT-ID&gt;&quot;</span><span class="p">,</span>
    <span class="n">disk_size_gb</span><span class="o">=</span><span class="mi">100</span><span class="p">,</span>
    <span class="n">cluster_type</span><span class="o">=</span><span class="s2">&quot;REPLICASET&quot;</span><span class="p">,</span>
    <span class="n">replication_specs</span><span class="o">=</span><span class="p">[</span><span class="n">mongodbatlas</span><span class="o">.</span><span class="n">ClusterReplicationSpecArgs</span><span class="p">(</span>
        <span class="n">num_shards</span><span class="o">=</span><span class="mi">1</span><span class="p">,</span>
        <span class="n">regions_configs</span><span class="o">=</span><span class="p">[</span><span class="n">mongodbatlas</span><span class="o">.</span><span class="n">ClusterReplicationSpecRegionsConfigArgs</span><span class="p">(</span>
            <span class="n">region_name</span><span class="o">=</span><span class="s2">&quot;US_EAST_1&quot;</span><span class="p">,</span>
            <span class="n">electable_nodes</span><span class="o">=</span><span class="mi">3</span><span class="p">,</span>
            <span class="n">priority</span><span class="o">=</span><span class="mi">7</span><span class="p">,</span>
            <span class="n">read_only_nodes</span><span class="o">=</span><span class="mi">0</span><span class="p">,</span>
        <span class="p">)],</span>
    <span class="p">)],</span>
    <span class="n">provider_backup_enabled</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="n">auto_scaling_disk_gb_enabled</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="n">provider_name</span><span class="o">=</span><span class="s2">&quot;AWS&quot;</span><span class="p">,</span>
    <span class="n">provider_disk_iops</span><span class="o">=</span><span class="mi">300</span><span class="p">,</span>
    <span class="n">provider_volume_type</span><span class="o">=</span><span class="s2">&quot;STANDARD&quot;</span><span class="p">,</span>
    <span class="n">provider_encrypt_ebs_volume</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="n">provider_instance_size_name</span><span class="o">=</span><span class="s2">&quot;M40&quot;</span><span class="p">)</span>
<span class="n">test_clusters</span> <span class="o">=</span> <span class="n">test_cluster</span><span class="o">.</span><span class="n">project_id</span><span class="o">.</span><span class="n">apply</span><span class="p">(</span><span class="k">lambda</span> <span class="n">project_id</span><span class="p">:</span> <span class="n">mongodbatlas</span><span class="o">.</span><span class="n">get_clusters</span><span class="p">(</span><span class="n">project_id</span><span class="o">=</span><span class="n">project_id</span><span class="p">))</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>project_id</strong> (<em>str</em>) – The unique ID for the project to get the clusters.</p>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_mongodbatlas.get_custom_db_role">
<code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">get_custom_db_role</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">inherited_roles</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>GetCustomDbRoleInheritedRoleArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">role_name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_mongodbatlas.get_custom_db_role.AwaitableGetCustomDbRoleResult<a class="headerlink" href="#pulumi_mongodbatlas.get_custom_db_role" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">CustomDbRole</span></code> describe a Custom DB Role. This represents a custom db role.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Groups and projects are synonymous terms. You may find group_id in the official documentation.</p>
</div></blockquote>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_mongodbatlas</span> <span class="k">as</span> <span class="nn">mongodbatlas</span>

<span class="n">test_role</span> <span class="o">=</span> <span class="n">mongodbatlas</span><span class="o">.</span><span class="n">CustomDbRole</span><span class="p">(</span><span class="s2">&quot;testRole&quot;</span><span class="p">,</span>
    <span class="n">actions</span><span class="o">=</span><span class="p">[</span>
        <span class="n">mongodbatlas</span><span class="o">.</span><span class="n">CustomDbRoleActionArgs</span><span class="p">(</span>
            <span class="n">action</span><span class="o">=</span><span class="s2">&quot;UPDATE&quot;</span><span class="p">,</span>
            <span class="n">resources</span><span class="o">=</span><span class="p">[</span><span class="n">mongodbatlas</span><span class="o">.</span><span class="n">CustomDbRoleActionResourceArgs</span><span class="p">(</span>
                <span class="n">collection_name</span><span class="o">=</span><span class="s2">&quot;&quot;</span><span class="p">,</span>
                <span class="n">database_name</span><span class="o">=</span><span class="s2">&quot;anyDatabase&quot;</span><span class="p">,</span>
            <span class="p">)],</span>
        <span class="p">),</span>
        <span class="n">mongodbatlas</span><span class="o">.</span><span class="n">CustomDbRoleActionArgs</span><span class="p">(</span>
            <span class="n">action</span><span class="o">=</span><span class="s2">&quot;INSERT&quot;</span><span class="p">,</span>
            <span class="n">resources</span><span class="o">=</span><span class="p">[</span><span class="n">mongodbatlas</span><span class="o">.</span><span class="n">CustomDbRoleActionResourceArgs</span><span class="p">(</span>
                <span class="n">collection_name</span><span class="o">=</span><span class="s2">&quot;&quot;</span><span class="p">,</span>
                <span class="n">database_name</span><span class="o">=</span><span class="s2">&quot;anyDatabase&quot;</span><span class="p">,</span>
            <span class="p">)],</span>
        <span class="p">),</span>
    <span class="p">],</span>
    <span class="n">project_id</span><span class="o">=</span><span class="s2">&quot;&lt;PROJECT-ID&gt;&quot;</span><span class="p">,</span>
    <span class="n">role_name</span><span class="o">=</span><span class="s2">&quot;myCustomRole&quot;</span><span class="p">)</span>
<span class="n">test</span> <span class="o">=</span> <span class="n">pulumi</span><span class="o">.</span><span class="n">Output</span><span class="o">.</span><span class="n">all</span><span class="p">(</span><span class="n">test_role</span><span class="o">.</span><span class="n">project_id</span><span class="p">,</span> <span class="n">test_role</span><span class="o">.</span><span class="n">role_name</span><span class="p">)</span><span class="o">.</span><span class="n">apply</span><span class="p">(</span><span class="k">lambda</span> <span class="n">project_id</span><span class="p">,</span> <span class="n">role_name</span><span class="p">:</span> <span class="n">mongodbatlas</span><span class="o">.</span><span class="n">get_custom_db_role</span><span class="p">(</span><span class="n">project_id</span><span class="o">=</span><span class="n">project_id</span><span class="p">,</span>
    <span class="n">role_name</span><span class="o">=</span><span class="n">role_name</span><span class="p">))</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>project_id</strong> (<em>str</em>) – The unique ID for the project to create the database user.</p></li>
<li><p><strong>role_name</strong> (<em>str</em>) – Name of the custom role.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_mongodbatlas.get_custom_db_roles">
<code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">get_custom_db_roles</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">project_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_mongodbatlas.get_custom_db_roles.AwaitableGetCustomDbRolesResult<a class="headerlink" href="#pulumi_mongodbatlas.get_custom_db_roles" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">getCustomDbRoles</span></code> describe all Custom DB Roles. This represents a custom db roles.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Groups and projects are synonymous terms. You may find <code class="docutils literal notranslate"><span class="pre">groupId</span></code> in the official documentation.</p>
</div></blockquote>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_mongodbatlas</span> <span class="k">as</span> <span class="nn">mongodbatlas</span>

<span class="n">test_database_user</span> <span class="o">=</span> <span class="n">mongodbatlas</span><span class="o">.</span><span class="n">DatabaseUser</span><span class="p">(</span><span class="s2">&quot;testDatabaseUser&quot;</span><span class="p">,</span>
    <span class="n">database_name</span><span class="o">=</span><span class="s2">&quot;admin&quot;</span><span class="p">,</span>
    <span class="n">password</span><span class="o">=</span><span class="s2">&quot;test-acc-password&quot;</span><span class="p">,</span>
    <span class="n">project_id</span><span class="o">=</span><span class="s2">&quot;&lt;PROJECT-ID&gt;&quot;</span><span class="p">,</span>
    <span class="n">roles</span><span class="o">=</span><span class="p">[</span>
        <span class="n">mongodbatlas</span><span class="o">.</span><span class="n">DatabaseUserRoleArgs</span><span class="p">(</span>
            <span class="n">database_name</span><span class="o">=</span><span class="s2">&quot;admin&quot;</span><span class="p">,</span>
            <span class="n">role_name</span><span class="o">=</span><span class="s2">&quot;readWrite&quot;</span><span class="p">,</span>
        <span class="p">),</span>
        <span class="n">mongodbatlas</span><span class="o">.</span><span class="n">DatabaseUserRoleArgs</span><span class="p">(</span>
            <span class="n">database_name</span><span class="o">=</span><span class="s2">&quot;admin&quot;</span><span class="p">,</span>
            <span class="n">role_name</span><span class="o">=</span><span class="s2">&quot;atlasAdmin&quot;</span><span class="p">,</span>
        <span class="p">),</span>
    <span class="p">],</span>
    <span class="n">username</span><span class="o">=</span><span class="s2">&quot;test-acc-username&quot;</span><span class="p">)</span>
<span class="n">test_custom_db_roles</span> <span class="o">=</span> <span class="n">mongodbatlas</span><span class="o">.</span><span class="n">get_custom_db_roles</span><span class="p">(</span><span class="n">project_id</span><span class="o">=</span><span class="n">mongodbatlas_custom_db_role</span><span class="p">[</span><span class="s2">&quot;test&quot;</span><span class="p">][</span><span class="s2">&quot;project_id&quot;</span><span class="p">])</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>project_id</strong> (<em>str</em>) – The unique ID for the project to get all custom db roles.</p>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_mongodbatlas.get_database_user">
<code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">get_database_user</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">auth_database_name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">database_name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">username</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_mongodbatlas.get_database_user.AwaitableGetDatabaseUserResult<a class="headerlink" href="#pulumi_mongodbatlas.get_database_user" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">DatabaseUser</span></code> describe a Database User. This represents a database user which will be applied to all clusters within the project.</p>
<p>Each user has a set of roles that provide access to the project’s databases. User’s roles apply to all the clusters in the project: if two clusters have a <code class="docutils literal notranslate"><span class="pre">products</span></code> database and a user has a role granting <code class="docutils literal notranslate"><span class="pre">read</span></code> access on the products database, the user has that access on both clusters.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Groups and projects are synonymous terms. You may find group_id in the official documentation.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>auth_database_name</strong> (<em>str</em>) – The user’s authentication database. A user must provide both a username and authentication database to log into MongoDB. In Atlas deployments of MongoDB, the authentication database is almost always the admin database, for X509 it is $external.</p></li>
<li><p><strong>database_name</strong> (<em>str</em>) – Database on which the user has the specified role. A role on the <code class="docutils literal notranslate"><span class="pre">admin</span></code> database can include privileges that apply to the other databases.</p></li>
<li><p><strong>project_id</strong> (<em>str</em>) – The unique ID for the project to create the database user.</p></li>
<li><p><strong>username</strong> (<em>str</em>) – Username for authenticating to MongoDB.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_mongodbatlas.get_database_users">
<code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">get_database_users</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">project_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_mongodbatlas.get_database_users.AwaitableGetDatabaseUsersResult<a class="headerlink" href="#pulumi_mongodbatlas.get_database_users" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">getDatabaseUsers</span></code> describe all Database Users. This represents a database user which will be applied to all clusters within the project.</p>
<p>Each user has a set of roles that provide access to the project’s databases. User’s roles apply to all the clusters in the project: if two clusters have a <code class="docutils literal notranslate"><span class="pre">products</span></code> database and a user has a role granting <code class="docutils literal notranslate"><span class="pre">read</span></code> access on the products database, the user has that access on both clusters.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Groups and projects are synonymous terms. You may find <code class="docutils literal notranslate"><span class="pre">groupId</span></code> in the official documentation.</p>
</div></blockquote>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_mongodbatlas</span> <span class="k">as</span> <span class="nn">mongodbatlas</span>

<span class="n">test_database_user</span> <span class="o">=</span> <span class="n">mongodbatlas</span><span class="o">.</span><span class="n">DatabaseUser</span><span class="p">(</span><span class="s2">&quot;testDatabaseUser&quot;</span><span class="p">,</span>
    <span class="n">username</span><span class="o">=</span><span class="s2">&quot;test-acc-username&quot;</span><span class="p">,</span>
    <span class="n">password</span><span class="o">=</span><span class="s2">&quot;test-acc-password&quot;</span><span class="p">,</span>
    <span class="n">project_id</span><span class="o">=</span><span class="s2">&quot;&lt;PROJECT-ID&gt;&quot;</span><span class="p">,</span>
    <span class="n">auth_database_name</span><span class="o">=</span><span class="s2">&quot;admin&quot;</span><span class="p">,</span>
    <span class="n">roles</span><span class="o">=</span><span class="p">[</span>
        <span class="n">mongodbatlas</span><span class="o">.</span><span class="n">DatabaseUserRoleArgs</span><span class="p">(</span>
            <span class="n">role_name</span><span class="o">=</span><span class="s2">&quot;readWrite&quot;</span><span class="p">,</span>
            <span class="n">database_name</span><span class="o">=</span><span class="s2">&quot;admin&quot;</span><span class="p">,</span>
        <span class="p">),</span>
        <span class="n">mongodbatlas</span><span class="o">.</span><span class="n">DatabaseUserRoleArgs</span><span class="p">(</span>
            <span class="n">role_name</span><span class="o">=</span><span class="s2">&quot;atlasAdmin&quot;</span><span class="p">,</span>
            <span class="n">database_name</span><span class="o">=</span><span class="s2">&quot;admin&quot;</span><span class="p">,</span>
        <span class="p">),</span>
    <span class="p">],</span>
    <span class="n">labels</span><span class="o">=</span><span class="p">[</span>
        <span class="n">mongodbatlas</span><span class="o">.</span><span class="n">DatabaseUserLabelArgs</span><span class="p">(</span>
            <span class="n">key</span><span class="o">=</span><span class="s2">&quot;key 1&quot;</span><span class="p">,</span>
            <span class="n">value</span><span class="o">=</span><span class="s2">&quot;value 1&quot;</span><span class="p">,</span>
        <span class="p">),</span>
        <span class="n">mongodbatlas</span><span class="o">.</span><span class="n">DatabaseUserLabelArgs</span><span class="p">(</span>
            <span class="n">key</span><span class="o">=</span><span class="s2">&quot;key 2&quot;</span><span class="p">,</span>
            <span class="n">value</span><span class="o">=</span><span class="s2">&quot;value 2&quot;</span><span class="p">,</span>
        <span class="p">),</span>
    <span class="p">])</span>
<span class="n">test_database_users</span> <span class="o">=</span> <span class="n">test_database_user</span><span class="o">.</span><span class="n">project_id</span><span class="o">.</span><span class="n">apply</span><span class="p">(</span><span class="k">lambda</span> <span class="n">project_id</span><span class="p">:</span> <span class="n">mongodbatlas</span><span class="o">.</span><span class="n">get_database_users</span><span class="p">(</span><span class="n">project_id</span><span class="o">=</span><span class="n">project_id</span><span class="p">))</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>project_id</strong> (<em>str</em>) – The unique ID for the project to get all database users.</p>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_mongodbatlas.get_global_cluster_config">
<code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">get_global_cluster_config</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">cluster_name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">managed_namespaces</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Sequence<span class="p">[</span>Union<span class="p">[</span>GetGlobalClusterConfigManagedNamespaceArgs<span class="p">, </span>Mapping<span class="p">[</span>str<span class="p">, </span>Any<span class="p">]</span><span class="p">]</span><span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_mongodbatlas.get_global_cluster_config.AwaitableGetGlobalClusterConfigResult<a class="headerlink" href="#pulumi_mongodbatlas.get_global_cluster_config" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">GlobalClusterConfig</span></code> describes all managed namespaces and custom zone mappings associated with the specified Global Cluster.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Groups and projects are synonymous terms. You may find group_id in the official documentation.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>managed_namespaces</strong> (<em>Sequence</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'GetGlobalClusterConfigManagedNamespaceArgs'</em><em>]</em><em>]</em>) – <p>Add a managed namespaces to a Global Cluster. For more information about managed namespaces, see <a class="reference external" href="https://docs.atlas.mongodb.com/reference/api/global-clusters/">Global Clusters</a>. See Managed Namespace below for more details.</p>
</p></li>
<li><p><strong>project_id</strong> (<em>str</em>) – The unique ID for the project to create the database user.</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>* `cluster_name - (Required) The name of the Global Cluster.
</pre></div>
</div>
</dd></dl>

<dl class="py function">
<dt id="pulumi_mongodbatlas.get_maintenance_window">
<code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">get_maintenance_window</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">project_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_mongodbatlas.get_maintenance_window.AwaitableGetMaintenanceWindowResult<a class="headerlink" href="#pulumi_mongodbatlas.get_maintenance_window" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">MaintenanceWindow</span></code> provides a Maintenance Window entry datasource. Gets information regarding the configured maintenance window for a MongoDB Atlas project.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Groups and projects are synonymous terms. You may find <code class="docutils literal notranslate"><span class="pre">groupId</span></code> in the official documentation.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>project_id</strong> (<em>str</em>) – The unique identifier of the project for the Maintenance Window.</p>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_mongodbatlas.get_network_container">
<code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">get_network_container</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">container_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_mongodbatlas.get_network_container.AwaitableGetNetworkContainerResult<a class="headerlink" href="#pulumi_mongodbatlas.get_network_container" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">NetworkContainer</span></code> describes a Network Peering Container. The resource requires your Project ID and container ID.</p>
<blockquote>
<div><p><strong>IMPORTANT:</strong> This resource creates one Network Peering container into which Atlas can deploy Network Peering connections. An Atlas project can have a maximum of one container for each cloud provider. You must have either the Project Owner or Organization Owner role to successfully call this endpoint.</p>
<p><strong>NOTE:</strong> Groups and projects are synonymous terms. You may find <strong>group_id</strong> in the official documentation.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>container_id</strong> (<em>str</em>) – The Network Peering Container ID.</p></li>
<li><p><strong>project_id</strong> (<em>str</em>) – The unique ID for the project to create the database user.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_mongodbatlas.get_network_containers">
<code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">get_network_containers</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">project_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">provider_name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_mongodbatlas.get_network_containers.AwaitableGetNetworkContainersResult<a class="headerlink" href="#pulumi_mongodbatlas.get_network_containers" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">getNetworkContainers</span></code> describes all Network Peering Containers. The data source requires your Project ID.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Groups and projects are synonymous terms. You may find <strong>group_id</strong> in the official documentation.</p>
</div></blockquote>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_mongodbatlas</span> <span class="k">as</span> <span class="nn">mongodbatlas</span>

<span class="n">test_network_container</span> <span class="o">=</span> <span class="n">mongodbatlas</span><span class="o">.</span><span class="n">NetworkContainer</span><span class="p">(</span><span class="s2">&quot;testNetworkContainer&quot;</span><span class="p">,</span>
    <span class="n">project_id</span><span class="o">=</span><span class="s2">&quot;&lt;YOUR-PROJECT-ID&gt;&quot;</span><span class="p">,</span>
    <span class="n">atlas_cidr_block</span><span class="o">=</span><span class="s2">&quot;10.8.0.0/21&quot;</span><span class="p">,</span>
    <span class="n">provider_name</span><span class="o">=</span><span class="s2">&quot;AWS&quot;</span><span class="p">,</span>
    <span class="n">region_name</span><span class="o">=</span><span class="s2">&quot;US_EAST_1&quot;</span><span class="p">)</span>
<span class="n">test_network_containers</span> <span class="o">=</span> <span class="n">pulumi</span><span class="o">.</span><span class="n">Output</span><span class="o">.</span><span class="n">all</span><span class="p">(</span><span class="n">test_network_container</span><span class="o">.</span><span class="n">project_id</span><span class="p">,</span> <span class="n">test_network_container</span><span class="o">.</span><span class="n">provider_name</span><span class="p">)</span><span class="o">.</span><span class="n">apply</span><span class="p">(</span><span class="k">lambda</span> <span class="n">project_id</span><span class="p">,</span> <span class="n">provider_name</span><span class="p">:</span> <span class="n">mongodbatlas</span><span class="o">.</span><span class="n">get_network_containers</span><span class="p">(</span><span class="n">project_id</span><span class="o">=</span><span class="n">project_id</span><span class="p">,</span>
    <span class="n">provider_name</span><span class="o">=</span><span class="n">provider_name</span><span class="p">))</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>project_id</strong> (<em>str</em>) – The unique ID for the project to create the database user.</p></li>
<li><p><strong>provider_name</strong> (<em>str</em>) – Cloud provider for this Network peering container. Accepted values are AWS, GCP, and Azure.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_mongodbatlas.get_network_peering">
<code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">get_network_peering</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">peering_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_mongodbatlas.get_network_peering.AwaitableGetNetworkPeeringResult<a class="headerlink" href="#pulumi_mongodbatlas.get_network_peering" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">NetworkPeering</span></code> describes a Network Peering Connection.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Groups and projects are synonymous terms. You may find <strong>group_id</strong> in the official documentation.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>peering_id</strong> (<em>str</em>) – Atlas assigned unique ID for the peering connection.</p></li>
<li><p><strong>project_id</strong> (<em>str</em>) – The unique ID for the project to create the database user.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_mongodbatlas.get_network_peerings">
<code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">get_network_peerings</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">project_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_mongodbatlas.get_network_peerings.AwaitableGetNetworkPeeringsResult<a class="headerlink" href="#pulumi_mongodbatlas.get_network_peerings" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">getNetworkPeerings</span></code> describes all Network Peering Connections.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Groups and projects are synonymous terms. You may find <strong>group_id</strong> in the official documentation.</p>
</div></blockquote>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_mongodbatlas</span> <span class="k">as</span> <span class="nn">mongodbatlas</span>

<span class="n">test_network_peering</span> <span class="o">=</span> <span class="n">mongodbatlas</span><span class="o">.</span><span class="n">NetworkPeering</span><span class="p">(</span><span class="s2">&quot;testNetworkPeering&quot;</span><span class="p">,</span>
    <span class="n">accepter_region_name</span><span class="o">=</span><span class="s2">&quot;us-east-1&quot;</span><span class="p">,</span>
    <span class="n">project_id</span><span class="o">=</span><span class="s2">&quot;&lt;YOUR-PROJEC-ID&gt;&quot;</span><span class="p">,</span>
    <span class="n">container_id</span><span class="o">=</span><span class="s2">&quot;507f1f77bcf86cd799439011&quot;</span><span class="p">,</span>
    <span class="n">provider_name</span><span class="o">=</span><span class="s2">&quot;AWS&quot;</span><span class="p">,</span>
    <span class="n">route_table_cidr_block</span><span class="o">=</span><span class="s2">&quot;192.168.0.0/24&quot;</span><span class="p">,</span>
    <span class="n">vpc_id</span><span class="o">=</span><span class="s2">&quot;vpc-abc123abc123&quot;</span><span class="p">,</span>
    <span class="n">aws_account_id</span><span class="o">=</span><span class="s2">&quot;abc123abc123&quot;</span><span class="p">)</span>
<span class="n">test_network_peerings</span> <span class="o">=</span> <span class="n">test_network_peering</span><span class="o">.</span><span class="n">project_id</span><span class="o">.</span><span class="n">apply</span><span class="p">(</span><span class="k">lambda</span> <span class="n">project_id</span><span class="p">:</span> <span class="n">mongodbatlas</span><span class="o">.</span><span class="n">get_network_peerings</span><span class="p">(</span><span class="n">project_id</span><span class="o">=</span><span class="n">project_id</span><span class="p">))</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>project_id</strong> (<em>str</em>) – The unique ID for the project to create the database user.</p>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_mongodbatlas.get_private_endpoint">
<code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">get_private_endpoint</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">private_link_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_mongodbatlas.get_private_endpoint.AwaitableGetPrivateEndpointResult<a class="headerlink" href="#pulumi_mongodbatlas.get_private_endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">PrivateEndpoint</span></code> describe a Private Endpoint. This represents a Private Endpoint Connection to retrieve details regarding a private endpoint by id in an Atlas project</p>
<dl class="simple">
<dt>!&gt; <strong>WARNING:</strong> This datasource is deprecated and will be removed in the next major version</dt><dd><p>Please transition to privatelink_endpoint as soon as possible. <a class="reference external" href="https://docs.atlas.mongodb.com/reference/api/private-endpoints-service-get-one/">PrivateLink Endpoints</a></p>
</dd>
</dl>
<blockquote>
<div><p><strong>NOTE:</strong> Groups and projects are synonymous terms. You may find group_id in the official documentation.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>private_link_id</strong> (<em>str</em>) – Unique identifier of the AWS PrivateLink connection.</p></li>
<li><p><strong>project_id</strong> (<em>str</em>) – Unique identifier for the project.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_mongodbatlas.get_private_endpoint_interface_link">
<code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">get_private_endpoint_interface_link</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">interface_endpoint_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">private_link_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_mongodbatlas.get_private_endpoint_interface_link.AwaitableGetPrivateEndpointInterfaceLinkResult<a class="headerlink" href="#pulumi_mongodbatlas.get_private_endpoint_interface_link" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">PrivateEndpointInterfaceLink</span></code> describe a Private Endpoint Link. This represents a Private Endpoint Link Connection that wants to retrieve details in an Atlas project.</p>
<dl class="simple">
<dt>!&gt; <strong>WARNING:</strong> This datasource is deprecated and will be removed in the next major version</dt><dd><p>Please transition to privatelink_endpoint_service as soon as possible. <a class="reference external" href="https://docs.atlas.mongodb.com/reference/api/private-endpoints-endpoint-get-one/">PrivateLink Endpoint Service</a></p>
</dd>
</dl>
<blockquote>
<div><p><strong>NOTE:</strong> Groups and projects are synonymous terms. You may find group_id in the official documentation.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>private_link_id</strong> (<em>str</em>) – Unique identifier of the AWS PrivateLink connection.</p></li>
<li><p><strong>project_id</strong> (<em>str</em>) – Unique identifier for the project.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_mongodbatlas.get_private_link_endpoint">
<code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">get_private_link_endpoint</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">private_link_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">provider_name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_mongodbatlas.get_private_link_endpoint.AwaitableGetPrivateLinkEndpointResult<a class="headerlink" href="#pulumi_mongodbatlas.get_private_link_endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">PrivateLinkEndpoint</span></code> describe a Private Endpoint. This represents a Private Endpoint Connection to retrieve details regarding a private endpoint by id in an Atlas project</p>
<blockquote>
<div><p><strong>NOTE:</strong> Groups and projects are synonymous terms. You may find group_id in the official documentation.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>private_link_id</strong> (<em>str</em>) – Unique identifier of the private endpoint service that you want to retrieve.</p></li>
<li><p><strong>project_id</strong> (<em>str</em>) – Unique identifier for the project.</p></li>
<li><p><strong>provider_name</strong> (<em>str</em>) – Cloud provider for which you want to retrieve a private endpoint service. Atlas accepts <code class="docutils literal notranslate"><span class="pre">AWS</span></code> or <code class="docutils literal notranslate"><span class="pre">AZURE</span></code>.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_mongodbatlas.get_private_link_endpoint_service">
<code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">get_private_link_endpoint_service</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">endpoint_service_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">private_link_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">provider_name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_mongodbatlas.get_private_link_endpoint_service.AwaitableGetPrivateLinkEndpointServiceResult<a class="headerlink" href="#pulumi_mongodbatlas.get_private_link_endpoint_service" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">PrivateLinkEndpointService</span></code> describe a Private Endpoint Link. This represents a Private Endpoint Link Connection that wants to retrieve details in an Atlas project.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Groups and projects are synonymous terms. You may find group_id in the official documentation.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>endpoint_service_id</strong> (<em>str</em>) – Unique identifier of the private endpoint service for which you want to create a private endpoint service.</p></li>
<li><p><strong>private_link_id</strong> (<em>str</em>) – Unique identifier of the <code class="docutils literal notranslate"><span class="pre">AWS</span></code> or <code class="docutils literal notranslate"><span class="pre">AZURE</span></code> PrivateLink connection.</p></li>
<li><p><strong>project_id</strong> (<em>str</em>) – Unique identifier for the project.</p></li>
<li><p><strong>provider_name</strong> (<em>str</em>) – Cloud provider for which you want to create a private endpoint. Atlas accepts <code class="docutils literal notranslate"><span class="pre">AWS</span></code> or <code class="docutils literal notranslate"><span class="pre">AZURE</span></code>.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_mongodbatlas.get_project">
<code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">get_project</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_mongodbatlas.get_project.AwaitableGetProjectResult<a class="headerlink" href="#pulumi_mongodbatlas.get_project" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">Project</span></code> describes a MongoDB Atlas Project. This represents a project that has been created.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Groups and projects are synonymous terms. You may find group_id in the official documentation.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>name</strong> (<em>str</em>) – The unique ID for the project.</p></li>
<li><p><strong>project_id</strong> (<em>str</em>) – The unique ID for the project.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_mongodbatlas.get_project_ip_access_list">
<code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">get_project_ip_access_list</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">aws_security_group</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cidr_block</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ip_address</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_mongodbatlas.get_project_ip_access_list.AwaitableGetProjectIpAccessListResult<a class="headerlink" href="#pulumi_mongodbatlas.get_project_ip_access_list" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">ProjectIpAccessList</span></code> describes an IP Access List entry resource. The access list grants access from IPs, CIDRs or AWS Security Groups (if VPC Peering is enabled) to clusters within the Project.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Groups and projects are synonymous terms. You may find <code class="docutils literal notranslate"><span class="pre">groupId</span></code> in the official documentation.</p>
<p><strong>IMPORTANT:</strong>
When you remove an entry from the access list, existing connections from the removed address(es) may remain open for a variable amount of time. How much time passes before Atlas closes the connection depends on several factors, including how the connection was established, the particular behavior of the application or driver using the address, and the connection protocol (e.g., TCP or UDP). This is particularly important to consider when changing an existing IP address or CIDR block as they cannot be updated via the Provider (comments can however), hence a change will force the destruction and recreation of entries.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>aws_security_group</strong> (<em>str</em>) – Unique identifier of the AWS security group to add to the access list.</p></li>
<li><p><strong>cidr_block</strong> (<em>str</em>) – Range of IP addresses in CIDR notation to be added to the access list.</p></li>
<li><p><strong>ip_address</strong> (<em>str</em>) – Single IP address to be added to the access list.</p></li>
<li><p><strong>project_id</strong> (<em>str</em>) – Unique identifier for the project to which you want to add one or more access list entries.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_mongodbatlas.get_project_ip_whitelist">
<code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">get_project_ip_whitelist</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">aws_security_group</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cidr_block</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ip_address</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_mongodbatlas.get_project_ip_whitelist.AwaitableGetProjectIpWhitelistResult<a class="headerlink" href="#pulumi_mongodbatlas.get_project_ip_whitelist" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">ProjectIpWhitelist</span></code> describes an IP Whitelist entry resource. The whitelist grants access from IPs, CIDRs or AWS Security Groups (if VPC Peering is enabled) to clusters within the Project.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Groups and projects are synonymous terms. You may find <code class="docutils literal notranslate"><span class="pre">groupId</span></code> in the official documentation.</p>
<p><strong>IMPORTANT:</strong>
When you remove an entry from the whitelist, existing connections from the removed address(es) may remain open for a variable amount of time. How much time passes before Atlas closes the connection depends on several factors, including how the connection was established, the particular behavior of the application or driver using the address, and the connection protocol (e.g., TCP or UDP). This is particularly important to consider when changing an existing IP address or CIDR block as they cannot be updated via the Provider (comments can however), hence a change will force the destruction and recreation of entries.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>aws_security_group</strong> (<em>str</em>) – ID of the whitelisted AWS security group. Mutually exclusive with <code class="docutils literal notranslate"><span class="pre">cidr_block</span></code> and <code class="docutils literal notranslate"><span class="pre">ip_address</span></code>.</p></li>
<li><p><strong>cidr_block</strong> (<em>str</em>) – Whitelist entry in Classless Inter-Domain Routing (CIDR) notation. Mutually exclusive with <code class="docutils literal notranslate"><span class="pre">aws_security_group</span></code> and <code class="docutils literal notranslate"><span class="pre">ip_address</span></code>.</p></li>
<li><p><strong>ip_address</strong> (<em>str</em>) – Whitelisted IP address. Mutually exclusive with <code class="docutils literal notranslate"><span class="pre">aws_security_group</span></code> and <code class="docutils literal notranslate"><span class="pre">cidr_block</span></code>.</p></li>
<li><p><strong>project_id</strong> (<em>str</em>) – The ID of the project in which to add the whitelist entry.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_mongodbatlas.get_projects">
<code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">get_projects</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">items_per_page</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>int<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">page_num</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>int<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_mongodbatlas.get_projects.AwaitableGetProjectsResult<a class="headerlink" href="#pulumi_mongodbatlas.get_projects" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">getProjects</span></code> describe all Projects. This represents projects that have been created.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Groups and projects are synonymous terms. You may find <code class="docutils literal notranslate"><span class="pre">groupId</span></code> in the official documentation.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>items_per_page</strong> (<em>int</em>) – Number of items to return per page, up to a maximum of 500. Defaults to <code class="docutils literal notranslate"><span class="pre">100</span></code>.</p></li>
<li><p><strong>page_num</strong> (<em>int</em>) – The page to return. Defaults to <code class="docutils literal notranslate"><span class="pre">1</span></code>.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_mongodbatlas.get_team">
<code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">get_team</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">org_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">team_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_mongodbatlas.get_team.AwaitableGetTeamResult<a class="headerlink" href="#pulumi_mongodbatlas.get_team" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">Teams</span></code> describes a Team. The resource requires your Organization ID, Project ID and Team ID.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Groups and projects are synonymous terms. You may find group_id in the official documentation.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>name</strong> (<em>str</em>) – The team name.</p></li>
<li><p><strong>org_id</strong> (<em>str</em>) – The unique identifier for the organization you want to associate the team with.</p></li>
<li><p><strong>team_id</strong> (<em>str</em>) – The unique identifier for the team.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_mongodbatlas.get_teams">
<code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">get_teams</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">org_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">team_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_mongodbatlas.get_teams.AwaitableGetTeamsResult<a class="headerlink" href="#pulumi_mongodbatlas.get_teams" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing resource.</p>
</dd></dl>

<dl class="py function">
<dt id="pulumi_mongodbatlas.get_third_party_integration">
<code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">get_third_party_integration</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">project_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_mongodbatlas.get_third_party_integration.AwaitableGetThirdPartyIntegrationResult<a class="headerlink" href="#pulumi_mongodbatlas.get_third_party_integration" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">ThirdPartyIntegration</span></code> describe a Third-Party Integration Settings for the given type.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Groups and projects are synonymous terms. You may find <code class="docutils literal notranslate"><span class="pre">groupId</span></code> in the official documentation.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>project_id</strong> (<em>str</em>) – The unique ID for the project to get all Third-Party service integrations</p></li>
<li><p><strong>type</strong> (<em>str</em>) – Third-Party service integration type</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="o">*</span> <span class="n">PAGER_DUTY</span>
<span class="o">*</span> <span class="n">DATADOG</span>
<span class="o">*</span> <span class="n">NEW_RELIC</span>
<span class="o">*</span> <span class="n">OPS_GENIE</span>
<span class="o">*</span> <span class="n">VICTOR_OPS</span>
<span class="o">*</span> <span class="n">FLOWDOCK</span>
<span class="o">*</span> <span class="n">WEBHOOK</span>
</pre></div>
</div>
</dd></dl>

<dl class="py function">
<dt id="pulumi_mongodbatlas.get_third_party_integrations">
<code class="sig-prename descclassname">pulumi_mongodbatlas.</code><code class="sig-name descname">get_third_party_integrations</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">project_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_mongodbatlas.get_third_party_integrations.AwaitableGetThirdPartyIntegrationsResult<a class="headerlink" href="#pulumi_mongodbatlas.get_third_party_integrations" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">getThirdPartyIntegrations</span></code> describe all Third-Party Integration Settings. This represents two Third-Party services <code class="docutils literal notranslate"><span class="pre">PAGER_DUTY</span></code> and <code class="docutils literal notranslate"><span class="pre">FLOWDOCK</span></code>
applied across the project.</p>
<blockquote>
<div><p><strong>NOTE:</strong> Groups and projects are synonymous terms. You may find <code class="docutils literal notranslate"><span class="pre">groupId</span></code> in the official documentation.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>project_id</strong> (<em>str</em>) – The unique ID for the project to get all Third-Party service integrations</p>
</dd>
</dl>
</dd></dl>

</div>
