---
title: Module plugins
title_tag: Module plugins | Package pulumi_newrelic | Python SDK
linktitle: plugins
notitle: true
---

<div class="section" id="plugins">
<h1>plugins<a class="headerlink" href="#plugins" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-newrelic">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-newrelic/issues">pulumi/pulumi-newrelic repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-newrelic/issues">terraform-providers/terraform-provider-newrelic repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_newrelic.plugins"></span><dl class="py class">
<dt id="pulumi_newrelic.plugins.AlertCondition">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_newrelic.plugins.</code><code class="sig-name descname">AlertCondition</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">entities</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">metric</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">metric_description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">plugin_guid</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">plugin_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policy_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">runbook_url</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">terms</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">value_function</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_newrelic.plugins.AlertCondition" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this resource to create and manage plugins alert conditions in New Relic.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_newrelic</span> <span class="k">as</span> <span class="nn">newrelic</span>

<span class="n">foo_plugin</span> <span class="o">=</span> <span class="n">newrelic</span><span class="o">.</span><span class="n">plugins</span><span class="o">.</span><span class="n">get_plugin</span><span class="p">(</span><span class="n">guid</span><span class="o">=</span><span class="s2">&quot;com.example.my-plugin&quot;</span><span class="p">)</span>
<span class="n">foo_plugin_component</span> <span class="o">=</span> <span class="n">newrelic</span><span class="o">.</span><span class="n">plugins</span><span class="o">.</span><span class="n">get_plugin_component</span><span class="p">(</span><span class="n">plugin_id</span><span class="o">=</span><span class="n">foo_plugin</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">name</span><span class="o">=</span><span class="s2">&quot;MyPlugin&quot;</span><span class="p">)</span>
<span class="n">foo_alert_policy</span> <span class="o">=</span> <span class="n">newrelic</span><span class="o">.</span><span class="n">AlertPolicy</span><span class="p">(</span><span class="s2">&quot;fooAlertPolicy&quot;</span><span class="p">)</span>
<span class="n">foo_alert_condition</span> <span class="o">=</span> <span class="n">newrelic</span><span class="o">.</span><span class="n">plugins</span><span class="o">.</span><span class="n">AlertCondition</span><span class="p">(</span><span class="s2">&quot;fooAlertCondition&quot;</span><span class="p">,</span>
    <span class="n">policy_id</span><span class="o">=</span><span class="n">foo_alert_policy</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">entities</span><span class="o">=</span><span class="p">[</span><span class="n">foo_plugin_component</span><span class="o">.</span><span class="n">id</span><span class="p">],</span>
    <span class="n">metric</span><span class="o">=</span><span class="s2">&quot;Component/Summary/Consumers[consumers]&quot;</span><span class="p">,</span>
    <span class="n">plugin_id</span><span class="o">=</span><span class="n">foo_plugin</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">plugin_guid</span><span class="o">=</span><span class="n">foo_plugin</span><span class="o">.</span><span class="n">guid</span><span class="p">,</span>
    <span class="n">value_function</span><span class="o">=</span><span class="s2">&quot;average&quot;</span><span class="p">,</span>
    <span class="n">metric_description</span><span class="o">=</span><span class="s2">&quot;Queue consumers&quot;</span><span class="p">,</span>
    <span class="n">term</span><span class="o">=</span><span class="p">[{</span>
        <span class="s2">&quot;duration&quot;</span><span class="p">:</span> <span class="mi">5</span><span class="p">,</span>
        <span class="s2">&quot;operator&quot;</span><span class="p">:</span> <span class="s2">&quot;below&quot;</span><span class="p">,</span>
        <span class="s2">&quot;priority&quot;</span><span class="p">:</span> <span class="s2">&quot;critical&quot;</span><span class="p">,</span>
        <span class="s2">&quot;threshold&quot;</span><span class="p">:</span> <span class="s2">&quot;0.75&quot;</span><span class="p">,</span>
        <span class="s2">&quot;timeFunction&quot;</span><span class="p">:</span> <span class="s2">&quot;all&quot;</span><span class="p">,</span>
    <span class="p">}])</span>
</pre></div>
</div>
<p>The <code class="docutils literal notranslate"><span class="pre">term</span></code> mapping supports the following arguments:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">duration</span></code> - (Required) In minutes, must be in the range of <code class="docutils literal notranslate"><span class="pre">5</span></code> to <code class="docutils literal notranslate"><span class="pre">120</span></code>, inclusive.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">operator</span></code> - (Optional) <code class="docutils literal notranslate"><span class="pre">above</span></code>, <code class="docutils literal notranslate"><span class="pre">below</span></code>, or <code class="docutils literal notranslate"><span class="pre">equal</span></code>.  Defaults to <code class="docutils literal notranslate"><span class="pre">equal</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">priority</span></code> - (Optional) <code class="docutils literal notranslate"><span class="pre">critical</span></code> or <code class="docutils literal notranslate"><span class="pre">warning</span></code>.  Defaults to <code class="docutils literal notranslate"><span class="pre">critical</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">threshold</span></code> - (Required) Must be 0 or greater.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">time_function</span></code> - (Required) <code class="docutils literal notranslate"><span class="pre">all</span></code> or <code class="docutils literal notranslate"><span class="pre">any</span></code>.</p></li>
</ul>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether or not this condition is enabled.</p></li>
<li><p><strong>entities</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The plugin component IDs to target.</p></li>
<li><p><strong>metric</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The plugin metric to evaluate.</p></li>
<li><p><strong>metric_description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The metric description.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The title of the condition. Must be between 1 and 64 characters, inclusive.</p></li>
<li><p><strong>plugin_guid</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The GUID of the plugin which produces the metric.</p></li>
<li><p><strong>plugin_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the installed plugin instance which produces the metric.</p></li>
<li><p><strong>policy_id</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The ID of the policy where this condition should be used.</p></li>
<li><p><strong>runbook_url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Runbook URL to display in notifications.</p></li>
<li><p><strong>terms</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of terms for this condition. See Terms below for details.</p></li>
<li><p><strong>value_function</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The value function to apply to the metric data.  One of <code class="docutils literal notranslate"><span class="pre">min</span></code>, <code class="docutils literal notranslate"><span class="pre">max</span></code>, <code class="docutils literal notranslate"><span class="pre">average</span></code>, <code class="docutils literal notranslate"><span class="pre">sample_size</span></code>, <code class="docutils literal notranslate"><span class="pre">total</span></code>, or <code class="docutils literal notranslate"><span class="pre">percent</span></code>.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>terms</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">duration</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">operator</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">priority</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">threshold</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timeFunction</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_newrelic.plugins.AlertCondition.enabled">
<code class="sig-name descname">enabled</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_newrelic.plugins.AlertCondition.enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether or not this condition is enabled.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_newrelic.plugins.AlertCondition.entities">
<code class="sig-name descname">entities</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_newrelic.plugins.AlertCondition.entities" title="Permalink to this definition">¶</a></dt>
<dd><p>The plugin component IDs to target.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_newrelic.plugins.AlertCondition.metric">
<code class="sig-name descname">metric</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_newrelic.plugins.AlertCondition.metric" title="Permalink to this definition">¶</a></dt>
<dd><p>The plugin metric to evaluate.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_newrelic.plugins.AlertCondition.metric_description">
<code class="sig-name descname">metric_description</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_newrelic.plugins.AlertCondition.metric_description" title="Permalink to this definition">¶</a></dt>
<dd><p>The metric description.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_newrelic.plugins.AlertCondition.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_newrelic.plugins.AlertCondition.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The title of the condition. Must be between 1 and 64 characters, inclusive.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_newrelic.plugins.AlertCondition.plugin_guid">
<code class="sig-name descname">plugin_guid</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_newrelic.plugins.AlertCondition.plugin_guid" title="Permalink to this definition">¶</a></dt>
<dd><p>The GUID of the plugin which produces the metric.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_newrelic.plugins.AlertCondition.plugin_id">
<code class="sig-name descname">plugin_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_newrelic.plugins.AlertCondition.plugin_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the installed plugin instance which produces the metric.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_newrelic.plugins.AlertCondition.policy_id">
<code class="sig-name descname">policy_id</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_newrelic.plugins.AlertCondition.policy_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the policy where this condition should be used.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_newrelic.plugins.AlertCondition.runbook_url">
<code class="sig-name descname">runbook_url</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_newrelic.plugins.AlertCondition.runbook_url" title="Permalink to this definition">¶</a></dt>
<dd><p>Runbook URL to display in notifications.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_newrelic.plugins.AlertCondition.terms">
<code class="sig-name descname">terms</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_newrelic.plugins.AlertCondition.terms" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of terms for this condition. See Terms below for details.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">duration</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">operator</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">priority</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">threshold</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timeFunction</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_newrelic.plugins.AlertCondition.value_function">
<code class="sig-name descname">value_function</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_newrelic.plugins.AlertCondition.value_function" title="Permalink to this definition">¶</a></dt>
<dd><p>The value function to apply to the metric data.  One of <code class="docutils literal notranslate"><span class="pre">min</span></code>, <code class="docutils literal notranslate"><span class="pre">max</span></code>, <code class="docutils literal notranslate"><span class="pre">average</span></code>, <code class="docutils literal notranslate"><span class="pre">sample_size</span></code>, <code class="docutils literal notranslate"><span class="pre">total</span></code>, or <code class="docutils literal notranslate"><span class="pre">percent</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_newrelic.plugins.AlertCondition.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">entities</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">metric</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">metric_description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">plugin_guid</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">plugin_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">policy_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">runbook_url</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">terms</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">value_function</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_newrelic.plugins.AlertCondition.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing AlertCondition resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether or not this condition is enabled.</p></li>
<li><p><strong>entities</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The plugin component IDs to target.</p></li>
<li><p><strong>metric</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The plugin metric to evaluate.</p></li>
<li><p><strong>metric_description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The metric description.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The title of the condition. Must be between 1 and 64 characters, inclusive.</p></li>
<li><p><strong>plugin_guid</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The GUID of the plugin which produces the metric.</p></li>
<li><p><strong>plugin_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the installed plugin instance which produces the metric.</p></li>
<li><p><strong>policy_id</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The ID of the policy where this condition should be used.</p></li>
<li><p><strong>runbook_url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Runbook URL to display in notifications.</p></li>
<li><p><strong>terms</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of terms for this condition. See Terms below for details.</p></li>
<li><p><strong>value_function</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The value function to apply to the metric data.  One of <code class="docutils literal notranslate"><span class="pre">min</span></code>, <code class="docutils literal notranslate"><span class="pre">max</span></code>, <code class="docutils literal notranslate"><span class="pre">average</span></code>, <code class="docutils literal notranslate"><span class="pre">sample_size</span></code>, <code class="docutils literal notranslate"><span class="pre">total</span></code>, or <code class="docutils literal notranslate"><span class="pre">percent</span></code>.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>terms</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">duration</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">operator</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">priority</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">threshold</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">timeFunction</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_newrelic.plugins.AlertCondition.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_newrelic.plugins.AlertCondition.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_newrelic.plugins.AlertCondition.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_newrelic.plugins.AlertCondition.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_newrelic.plugins.AwaitableGetPluginComponentResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_newrelic.plugins.</code><code class="sig-name descname">AwaitableGetPluginComponentResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">health_status</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">plugin_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_newrelic.plugins.AwaitableGetPluginComponentResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_newrelic.plugins.AwaitableGetPluginResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_newrelic.plugins.</code><code class="sig-name descname">AwaitableGetPluginResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">guid</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_newrelic.plugins.AwaitableGetPluginResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_newrelic.plugins.GetPluginComponentResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_newrelic.plugins.</code><code class="sig-name descname">GetPluginComponentResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">health_status</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">plugin_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_newrelic.plugins.GetPluginComponentResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getPluginComponent.</p>
<dl class="py attribute">
<dt id="pulumi_newrelic.plugins.GetPluginComponentResult.health_status">
<code class="sig-name descname">health_status</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_newrelic.plugins.GetPluginComponentResult.health_status" title="Permalink to this definition">¶</a></dt>
<dd><p>The health status of the plugin component.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_newrelic.plugins.GetPluginComponentResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_newrelic.plugins.GetPluginComponentResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the plugin component.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_newrelic.plugins.GetPluginResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_newrelic.plugins.</code><code class="sig-name descname">GetPluginResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">guid</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_newrelic.plugins.GetPluginResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getPlugin.</p>
<dl class="py attribute">
<dt id="pulumi_newrelic.plugins.GetPluginResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_newrelic.plugins.GetPluginResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the installed plugin instance.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_newrelic.plugins.Workload">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_newrelic.plugins.</code><code class="sig-name descname">Workload</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">entity_guids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">entity_search_queries</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">scope_account_ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_newrelic.plugins.Workload" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this resource to create, update, and delete a New Relic One workload.</p>
<p>A New Relic Personal API key is required to provision this resource.  Set the <code class="docutils literal notranslate"><span class="pre">provider_api_key</span></code>
attribute in the <code class="docutils literal notranslate"><span class="pre">provider</span></code> block or the <code class="docutils literal notranslate"><span class="pre">NEWRELIC_PERSONAL_API_KEY</span></code> environment
variable with your Personal API key,</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_newrelic</span> <span class="k">as</span> <span class="nn">newrelic</span>

<span class="n">foo</span> <span class="o">=</span> <span class="n">newrelic</span><span class="o">.</span><span class="n">plugins</span><span class="o">.</span><span class="n">Workload</span><span class="p">(</span><span class="s2">&quot;foo&quot;</span><span class="p">,</span>
    <span class="n">account_id</span><span class="o">=</span><span class="mi">12345678</span><span class="p">,</span>
    <span class="n">entity_guids</span><span class="o">=</span><span class="p">[</span><span class="s2">&quot;MjUyMDUyOHxBUE18QVBQTElDQVRJT058MjE1MDM3Nzk1&quot;</span><span class="p">],</span>
    <span class="n">entity_search_queries</span><span class="o">=</span><span class="p">[{</span>
        <span class="s2">&quot;query&quot;</span><span class="p">:</span> <span class="s2">&quot;name like &#39;Example application&#39;&quot;</span><span class="p">,</span>
    <span class="p">}],</span>
    <span class="n">scope_account_ids</span><span class="o">=</span><span class="p">[</span><span class="mi">12345678</span><span class="p">])</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>account_id</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The New Relic account ID where you want to create the workload.</p></li>
<li><p><strong>entity_guids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of entity GUIDs manually assigned to this workload.</p></li>
<li><p><strong>entity_search_queries</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of search queries that define a dynamic workload.  See Nested entity_search_query blocks below for details.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The workload’s name.</p></li>
<li><p><strong>scope_account_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of account IDs that will be used to get entities from.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>entity_search_queries</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">query</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The query.</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_newrelic.plugins.Workload.account_id">
<code class="sig-name descname">account_id</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_newrelic.plugins.Workload.account_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The New Relic account ID where you want to create the workload.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_newrelic.plugins.Workload.composite_entity_search_query">
<code class="sig-name descname">composite_entity_search_query</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_newrelic.plugins.Workload.composite_entity_search_query" title="Permalink to this definition">¶</a></dt>
<dd><p>The composite query used to compose a dynamic workload.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_newrelic.plugins.Workload.entity_guids">
<code class="sig-name descname">entity_guids</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_newrelic.plugins.Workload.entity_guids" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of entity GUIDs manually assigned to this workload.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_newrelic.plugins.Workload.entity_search_queries">
<code class="sig-name descname">entity_search_queries</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_newrelic.plugins.Workload.entity_search_queries" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of search queries that define a dynamic workload.  See Nested entity_search_query blocks below for details.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">query</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The query.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_newrelic.plugins.Workload.guid">
<code class="sig-name descname">guid</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_newrelic.plugins.Workload.guid" title="Permalink to this definition">¶</a></dt>
<dd><p>The unique entity identifier of the workload in New Relic.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_newrelic.plugins.Workload.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_newrelic.plugins.Workload.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The workload’s name.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_newrelic.plugins.Workload.permalink">
<code class="sig-name descname">permalink</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_newrelic.plugins.Workload.permalink" title="Permalink to this definition">¶</a></dt>
<dd><p>The URL of the workload.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_newrelic.plugins.Workload.scope_account_ids">
<code class="sig-name descname">scope_account_ids</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_newrelic.plugins.Workload.scope_account_ids" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of account IDs that will be used to get entities from.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_newrelic.plugins.Workload.workload_id">
<code class="sig-name descname">workload_id</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_newrelic.plugins.Workload.workload_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The unique entity identifier of the workload.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_newrelic.plugins.Workload.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">composite_entity_search_query</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">entity_guids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">entity_search_queries</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">guid</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">permalink</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">scope_account_ids</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">workload_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_newrelic.plugins.Workload.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Workload resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>account_id</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The New Relic account ID where you want to create the workload.</p></li>
<li><p><strong>composite_entity_search_query</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The composite query used to compose a dynamic workload.</p></li>
<li><p><strong>entity_guids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of entity GUIDs manually assigned to this workload.</p></li>
<li><p><strong>entity_search_queries</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of search queries that define a dynamic workload.  See Nested entity_search_query blocks below for details.</p></li>
<li><p><strong>guid</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique entity identifier of the workload in New Relic.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The workload’s name.</p></li>
<li><p><strong>permalink</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The URL of the workload.</p></li>
<li><p><strong>scope_account_ids</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of account IDs that will be used to get entities from.</p></li>
<li><p><strong>workload_id</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The unique entity identifier of the workload.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>entity_search_queries</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">query</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The query.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_newrelic.plugins.Workload.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_newrelic.plugins.Workload.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_newrelic.plugins.Workload.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_newrelic.plugins.Workload.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_newrelic.plugins.get_plugin">
<code class="sig-prename descclassname">pulumi_newrelic.plugins.</code><code class="sig-name descname">get_plugin</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">guid</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_newrelic.plugins.get_plugin" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing resource.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>guid</strong> (<em>str</em>) – The GUID of the plugin in New Relic.</p>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_newrelic.plugins.get_plugin_component">
<code class="sig-prename descclassname">pulumi_newrelic.plugins.</code><code class="sig-name descname">get_plugin_component</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">plugin_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_newrelic.plugins.get_plugin_component" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing resource.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>name</strong> (<em>str</em>) – The name of the plugin component.</p></li>
<li><p><strong>plugin_id</strong> (<em>float</em>) – The ID of the plugin instance this component belongs to.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

</div>
