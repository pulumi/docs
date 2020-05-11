---
title: Module sentinel
title_tag: Module sentinel | Package pulumi_azure | Python SDK
linktitle: sentinel
notitle: true
---

<div class="section" id="sentinel">
<h1>sentinel<a class="headerlink" href="#sentinel" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-azure/issues">pulumi/pulumi-azure repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/issues">terraform-providers/terraform-provider-azurerm repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_azure.sentinel"></span><dl class="py class">
<dt id="pulumi_azure.sentinel.AlertRuleMsSecurityIncident">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.sentinel.</code><code class="sig-name descname">AlertRuleMsSecurityIncident</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">display_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">log_analytics_workspace_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">product_filter</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">severity_filters</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">text_whitelists</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.sentinel.AlertRuleMsSecurityIncident" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Sentinel MS Security Incident Alert Rule.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_azure</span> <span class="k">as</span> <span class="nn">azure</span>

<span class="n">example_resource_group</span> <span class="o">=</span> <span class="n">azure</span><span class="o">.</span><span class="n">core</span><span class="o">.</span><span class="n">ResourceGroup</span><span class="p">(</span><span class="s2">&quot;exampleResourceGroup&quot;</span><span class="p">,</span> <span class="n">location</span><span class="o">=</span><span class="s2">&quot;West Europe&quot;</span><span class="p">)</span>
<span class="n">example_analytics_workspace</span> <span class="o">=</span> <span class="n">azure</span><span class="o">.</span><span class="n">operationalinsights</span><span class="o">.</span><span class="n">AnalyticsWorkspace</span><span class="p">(</span><span class="s2">&quot;exampleAnalyticsWorkspace&quot;</span><span class="p">,</span>
    <span class="n">location</span><span class="o">=</span><span class="n">example_resource_group</span><span class="o">.</span><span class="n">location</span><span class="p">,</span>
    <span class="n">resource_group_name</span><span class="o">=</span><span class="n">example_resource_group</span><span class="o">.</span><span class="n">name</span><span class="p">,</span>
    <span class="n">sku</span><span class="o">=</span><span class="s2">&quot;pergb2018&quot;</span><span class="p">)</span>
<span class="n">example_alert_rule_ms_security_incident</span> <span class="o">=</span> <span class="n">azure</span><span class="o">.</span><span class="n">sentinel</span><span class="o">.</span><span class="n">AlertRuleMsSecurityIncident</span><span class="p">(</span><span class="s2">&quot;exampleAlertRuleMsSecurityIncident&quot;</span><span class="p">,</span>
    <span class="n">log_analytics_workspace_id</span><span class="o">=</span><span class="n">example_analytics_workspace</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">product_filter</span><span class="o">=</span><span class="s2">&quot;Microsoft Cloud App Security&quot;</span><span class="p">,</span>
    <span class="n">display_name</span><span class="o">=</span><span class="s2">&quot;example rule&quot;</span><span class="p">,</span>
    <span class="n">severity_filters</span><span class="o">=</span><span class="p">[</span><span class="s2">&quot;High&quot;</span><span class="p">])</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of this Sentinel MS Security Incident Alert Rule.</p></li>
<li><p><strong>display_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The friendly name of this Sentinel MS Security Incident Alert Rule.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Should this Sentinel MS Security Incident Alert Rule be enabled? Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>log_analytics_workspace_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Log Analytics Workspace this Sentinel MS Security Incident Alert Rule belongs to. Changing this forces a new Sentinel MS Security Incident Alert Rule to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name which should be used for this Sentinel MS Security Incident Alert Rule. Changing this forces a new Sentinel MS Security Incident Alert Rule to be created.</p></li>
<li><p><strong>product_filter</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Microsoft Security Service from where the alert will be generated. Possible values are <code class="docutils literal notranslate"><span class="pre">Azure</span> <span class="pre">Active</span> <span class="pre">Directory</span> <span class="pre">Identity</span> <span class="pre">Protection</span></code>, <code class="docutils literal notranslate"><span class="pre">Azure</span> <span class="pre">Advanced</span> <span class="pre">Threat</span> <span class="pre">Protection</span></code>, <code class="docutils literal notranslate"><span class="pre">Azure</span> <span class="pre">Security</span> <span class="pre">Center</span></code>, <code class="docutils literal notranslate"><span class="pre">Azure</span> <span class="pre">Security</span> <span class="pre">Center</span> <span class="pre">for</span> <span class="pre">IoT</span></code> and <code class="docutils literal notranslate"><span class="pre">Microsoft</span> <span class="pre">Cloud</span> <span class="pre">App</span> <span class="pre">Security</span></code>.</p></li>
<li><p><strong>severity_filters</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Only create incidents from alerts when alert severity level is contained in this list. Possible values are <code class="docutils literal notranslate"><span class="pre">High</span></code>, <code class="docutils literal notranslate"><span class="pre">Medium</span></code>, <code class="docutils literal notranslate"><span class="pre">Low</span></code> and <code class="docutils literal notranslate"><span class="pre">Informational</span></code>.</p></li>
<li><p><strong>text_whitelists</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Only create incidents from alerts when alert name contain text in this list. No filter will happen if this field is absent.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_azure.sentinel.AlertRuleMsSecurityIncident.description">
<code class="sig-name descname">description</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.sentinel.AlertRuleMsSecurityIncident.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description of this Sentinel MS Security Incident Alert Rule.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.sentinel.AlertRuleMsSecurityIncident.display_name">
<code class="sig-name descname">display_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.sentinel.AlertRuleMsSecurityIncident.display_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The friendly name of this Sentinel MS Security Incident Alert Rule.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.sentinel.AlertRuleMsSecurityIncident.enabled">
<code class="sig-name descname">enabled</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.sentinel.AlertRuleMsSecurityIncident.enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Should this Sentinel MS Security Incident Alert Rule be enabled? Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.sentinel.AlertRuleMsSecurityIncident.log_analytics_workspace_id">
<code class="sig-name descname">log_analytics_workspace_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.sentinel.AlertRuleMsSecurityIncident.log_analytics_workspace_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Log Analytics Workspace this Sentinel MS Security Incident Alert Rule belongs to. Changing this forces a new Sentinel MS Security Incident Alert Rule to be created.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.sentinel.AlertRuleMsSecurityIncident.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.sentinel.AlertRuleMsSecurityIncident.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name which should be used for this Sentinel MS Security Incident Alert Rule. Changing this forces a new Sentinel MS Security Incident Alert Rule to be created.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.sentinel.AlertRuleMsSecurityIncident.product_filter">
<code class="sig-name descname">product_filter</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.sentinel.AlertRuleMsSecurityIncident.product_filter" title="Permalink to this definition">¶</a></dt>
<dd><p>The Microsoft Security Service from where the alert will be generated. Possible values are <code class="docutils literal notranslate"><span class="pre">Azure</span> <span class="pre">Active</span> <span class="pre">Directory</span> <span class="pre">Identity</span> <span class="pre">Protection</span></code>, <code class="docutils literal notranslate"><span class="pre">Azure</span> <span class="pre">Advanced</span> <span class="pre">Threat</span> <span class="pre">Protection</span></code>, <code class="docutils literal notranslate"><span class="pre">Azure</span> <span class="pre">Security</span> <span class="pre">Center</span></code>, <code class="docutils literal notranslate"><span class="pre">Azure</span> <span class="pre">Security</span> <span class="pre">Center</span> <span class="pre">for</span> <span class="pre">IoT</span></code> and <code class="docutils literal notranslate"><span class="pre">Microsoft</span> <span class="pre">Cloud</span> <span class="pre">App</span> <span class="pre">Security</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.sentinel.AlertRuleMsSecurityIncident.severity_filters">
<code class="sig-name descname">severity_filters</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.sentinel.AlertRuleMsSecurityIncident.severity_filters" title="Permalink to this definition">¶</a></dt>
<dd><p>Only create incidents from alerts when alert severity level is contained in this list. Possible values are <code class="docutils literal notranslate"><span class="pre">High</span></code>, <code class="docutils literal notranslate"><span class="pre">Medium</span></code>, <code class="docutils literal notranslate"><span class="pre">Low</span></code> and <code class="docutils literal notranslate"><span class="pre">Informational</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.sentinel.AlertRuleMsSecurityIncident.text_whitelists">
<code class="sig-name descname">text_whitelists</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.sentinel.AlertRuleMsSecurityIncident.text_whitelists" title="Permalink to this definition">¶</a></dt>
<dd><p>Only create incidents from alerts when alert name contain text in this list. No filter will happen if this field is absent.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azure.sentinel.AlertRuleMsSecurityIncident.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">display_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">log_analytics_workspace_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">product_filter</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">severity_filters</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">text_whitelists</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.sentinel.AlertRuleMsSecurityIncident.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing AlertRuleMsSecurityIncident resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of this Sentinel MS Security Incident Alert Rule.</p></li>
<li><p><strong>display_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The friendly name of this Sentinel MS Security Incident Alert Rule.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Should this Sentinel MS Security Incident Alert Rule be enabled? Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>log_analytics_workspace_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Log Analytics Workspace this Sentinel MS Security Incident Alert Rule belongs to. Changing this forces a new Sentinel MS Security Incident Alert Rule to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name which should be used for this Sentinel MS Security Incident Alert Rule. Changing this forces a new Sentinel MS Security Incident Alert Rule to be created.</p></li>
<li><p><strong>product_filter</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Microsoft Security Service from where the alert will be generated. Possible values are <code class="docutils literal notranslate"><span class="pre">Azure</span> <span class="pre">Active</span> <span class="pre">Directory</span> <span class="pre">Identity</span> <span class="pre">Protection</span></code>, <code class="docutils literal notranslate"><span class="pre">Azure</span> <span class="pre">Advanced</span> <span class="pre">Threat</span> <span class="pre">Protection</span></code>, <code class="docutils literal notranslate"><span class="pre">Azure</span> <span class="pre">Security</span> <span class="pre">Center</span></code>, <code class="docutils literal notranslate"><span class="pre">Azure</span> <span class="pre">Security</span> <span class="pre">Center</span> <span class="pre">for</span> <span class="pre">IoT</span></code> and <code class="docutils literal notranslate"><span class="pre">Microsoft</span> <span class="pre">Cloud</span> <span class="pre">App</span> <span class="pre">Security</span></code>.</p></li>
<li><p><strong>severity_filters</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Only create incidents from alerts when alert severity level is contained in this list. Possible values are <code class="docutils literal notranslate"><span class="pre">High</span></code>, <code class="docutils literal notranslate"><span class="pre">Medium</span></code>, <code class="docutils literal notranslate"><span class="pre">Low</span></code> and <code class="docutils literal notranslate"><span class="pre">Informational</span></code>.</p></li>
<li><p><strong>text_whitelists</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Only create incidents from alerts when alert name contain text in this list. No filter will happen if this field is absent.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azure.sentinel.AlertRuleMsSecurityIncident.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.sentinel.AlertRuleMsSecurityIncident.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.sentinel.AlertRuleMsSecurityIncident.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.sentinel.AlertRuleMsSecurityIncident.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.sentinel.AlertRuleScheduled">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.sentinel.</code><code class="sig-name descname">AlertRuleScheduled</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">display_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">log_analytics_workspace_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">query</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">query_frequency</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">query_period</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">severity</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">suppression_duration</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">suppression_enabled</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tactics</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">trigger_operator</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">trigger_threshold</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.sentinel.AlertRuleScheduled" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Sentinel Scheduled Alert Rule.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_azure</span> <span class="k">as</span> <span class="nn">azure</span>

<span class="n">example_resource_group</span> <span class="o">=</span> <span class="n">azure</span><span class="o">.</span><span class="n">core</span><span class="o">.</span><span class="n">ResourceGroup</span><span class="p">(</span><span class="s2">&quot;exampleResourceGroup&quot;</span><span class="p">,</span> <span class="n">location</span><span class="o">=</span><span class="s2">&quot;West Europe&quot;</span><span class="p">)</span>
<span class="n">example_analytics_workspace</span> <span class="o">=</span> <span class="n">azure</span><span class="o">.</span><span class="n">operationalinsights</span><span class="o">.</span><span class="n">AnalyticsWorkspace</span><span class="p">(</span><span class="s2">&quot;exampleAnalyticsWorkspace&quot;</span><span class="p">,</span>
    <span class="n">location</span><span class="o">=</span><span class="n">example_resource_group</span><span class="o">.</span><span class="n">location</span><span class="p">,</span>
    <span class="n">resource_group_name</span><span class="o">=</span><span class="n">example_resource_group</span><span class="o">.</span><span class="n">name</span><span class="p">,</span>
    <span class="n">sku</span><span class="o">=</span><span class="s2">&quot;pergb2018&quot;</span><span class="p">)</span>
<span class="n">example_alert_rule_scheduled</span> <span class="o">=</span> <span class="n">azure</span><span class="o">.</span><span class="n">sentinel</span><span class="o">.</span><span class="n">AlertRuleScheduled</span><span class="p">(</span><span class="s2">&quot;exampleAlertRuleScheduled&quot;</span><span class="p">,</span>
    <span class="n">log_analytics_workspace_id</span><span class="o">=</span><span class="n">example_analytics_workspace</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">display_name</span><span class="o">=</span><span class="s2">&quot;example&quot;</span><span class="p">,</span>
    <span class="n">severity</span><span class="o">=</span><span class="s2">&quot;High&quot;</span><span class="p">,</span>
    <span class="n">query</span><span class="o">=</span><span class="s2">&quot;&quot;&quot;AzureActivity |</span>
<span class="s2">  where OperationName == &quot;Create or Update Virtual Machine&quot; or OperationName ==&quot;Create Deployment&quot; |</span>
<span class="s2">  where ActivityStatus == &quot;Succeeded&quot; |</span>
<span class="s2">  make-series dcount(ResourceId) default=0 on EventSubmissionTimestamp in range(ago(7d), now(), 1d) by Caller</span>
<span class="s2">&quot;&quot;&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of this Sentinel Scheduled Alert Rule.</p></li>
<li><p><strong>display_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The friendly name of this Sentinel Scheduled Alert Rule.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Should the Sentinel Scheduled Alert Rule be enabled? Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>log_analytics_workspace_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Log Analytics Workspace this Sentinel Scheduled Alert Rule belongs to. Changing this forces a new Sentinel Scheduled Alert Rule to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name which should be used for this Sentinel Scheduled Alert Rule. Changing this forces a new Sentinel Scheduled Alert Rule to be created.</p></li>
<li><p><strong>query</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The query of this Sentinel Scheduled Alert Rule.</p></li>
<li><p><strong>query_frequency</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ISO 8601 timespan duration between two consecutive queries. Defaults to <code class="docutils literal notranslate"><span class="pre">PT5H</span></code>.</p></li>
<li><p><strong>query_period</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ISO 8601 timespan duration, which determine the time period of the data covered by the query. For example, it can query the past 10 minutes of data, or the past 6 hours of data. Defaults to <code class="docutils literal notranslate"><span class="pre">PT5H</span></code>.</p></li>
<li><p><strong>severity</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The alert severity of this Sentinel Scheduled Alert Rule. Possible values are <code class="docutils literal notranslate"><span class="pre">High</span></code>, <code class="docutils literal notranslate"><span class="pre">Medium</span></code>, <code class="docutils literal notranslate"><span class="pre">Low</span></code> and <code class="docutils literal notranslate"><span class="pre">Informational</span></code>.</p></li>
<li><p><strong>suppression_duration</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – If <code class="docutils literal notranslate"><span class="pre">suppression_enabled</span></code> is <code class="docutils literal notranslate"><span class="pre">true</span></code>, this is ISO 8601 timespan duration, which specifies the amount of time the query should stop running after alert is generated. Defaults to <code class="docutils literal notranslate"><span class="pre">PT5H</span></code>.</p></li>
<li><p><strong>suppression_enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Should the Sentinel Scheduled Alert Rulea stop running query after alert is generated? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>tactics</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of categories of attacks by which to classify the rule. Possible values are <code class="docutils literal notranslate"><span class="pre">Collection</span></code>, <code class="docutils literal notranslate"><span class="pre">CommandAndControl</span></code>, <code class="docutils literal notranslate"><span class="pre">CredentialAccess</span></code>, <code class="docutils literal notranslate"><span class="pre">DefenseEvasion</span></code>, <code class="docutils literal notranslate"><span class="pre">Discovery</span></code>, <code class="docutils literal notranslate"><span class="pre">Execution</span></code>, <code class="docutils literal notranslate"><span class="pre">Exfiltration</span></code>, <code class="docutils literal notranslate"><span class="pre">Impact</span></code>, <code class="docutils literal notranslate"><span class="pre">InitialAccess</span></code>, <code class="docutils literal notranslate"><span class="pre">LateralMovement</span></code>, <code class="docutils literal notranslate"><span class="pre">Persistence</span></code> and <code class="docutils literal notranslate"><span class="pre">PrivilegeEscalation</span></code>.</p></li>
<li><p><strong>trigger_operator</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The alert trigger operator, combined with <code class="docutils literal notranslate"><span class="pre">trigger_threshold</span></code>, setting alert threshold of this Sentinel Scheduled Alert Rule. Possible values are <code class="docutils literal notranslate"><span class="pre">Equal</span></code>, <code class="docutils literal notranslate"><span class="pre">GreaterThan</span></code>, <code class="docutils literal notranslate"><span class="pre">LessThan</span></code>, <code class="docutils literal notranslate"><span class="pre">NotEqual</span></code>.</p></li>
<li><p><strong>trigger_threshold</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The baseline number of query results generated, combined with <code class="docutils literal notranslate"><span class="pre">trigger_operator</span></code>, setting alert threshold of this Sentinel Scheduled Alert Rule.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_azure.sentinel.AlertRuleScheduled.description">
<code class="sig-name descname">description</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.sentinel.AlertRuleScheduled.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description of this Sentinel Scheduled Alert Rule.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.sentinel.AlertRuleScheduled.display_name">
<code class="sig-name descname">display_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.sentinel.AlertRuleScheduled.display_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The friendly name of this Sentinel Scheduled Alert Rule.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.sentinel.AlertRuleScheduled.enabled">
<code class="sig-name descname">enabled</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.sentinel.AlertRuleScheduled.enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Should the Sentinel Scheduled Alert Rule be enabled? Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.sentinel.AlertRuleScheduled.log_analytics_workspace_id">
<code class="sig-name descname">log_analytics_workspace_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.sentinel.AlertRuleScheduled.log_analytics_workspace_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the Log Analytics Workspace this Sentinel Scheduled Alert Rule belongs to. Changing this forces a new Sentinel Scheduled Alert Rule to be created.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.sentinel.AlertRuleScheduled.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.sentinel.AlertRuleScheduled.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name which should be used for this Sentinel Scheduled Alert Rule. Changing this forces a new Sentinel Scheduled Alert Rule to be created.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.sentinel.AlertRuleScheduled.query">
<code class="sig-name descname">query</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.sentinel.AlertRuleScheduled.query" title="Permalink to this definition">¶</a></dt>
<dd><p>The query of this Sentinel Scheduled Alert Rule.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.sentinel.AlertRuleScheduled.query_frequency">
<code class="sig-name descname">query_frequency</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.sentinel.AlertRuleScheduled.query_frequency" title="Permalink to this definition">¶</a></dt>
<dd><p>The ISO 8601 timespan duration between two consecutive queries. Defaults to <code class="docutils literal notranslate"><span class="pre">PT5H</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.sentinel.AlertRuleScheduled.query_period">
<code class="sig-name descname">query_period</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.sentinel.AlertRuleScheduled.query_period" title="Permalink to this definition">¶</a></dt>
<dd><p>The ISO 8601 timespan duration, which determine the time period of the data covered by the query. For example, it can query the past 10 minutes of data, or the past 6 hours of data. Defaults to <code class="docutils literal notranslate"><span class="pre">PT5H</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.sentinel.AlertRuleScheduled.severity">
<code class="sig-name descname">severity</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.sentinel.AlertRuleScheduled.severity" title="Permalink to this definition">¶</a></dt>
<dd><p>The alert severity of this Sentinel Scheduled Alert Rule. Possible values are <code class="docutils literal notranslate"><span class="pre">High</span></code>, <code class="docutils literal notranslate"><span class="pre">Medium</span></code>, <code class="docutils literal notranslate"><span class="pre">Low</span></code> and <code class="docutils literal notranslate"><span class="pre">Informational</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.sentinel.AlertRuleScheduled.suppression_duration">
<code class="sig-name descname">suppression_duration</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.sentinel.AlertRuleScheduled.suppression_duration" title="Permalink to this definition">¶</a></dt>
<dd><p>If <code class="docutils literal notranslate"><span class="pre">suppression_enabled</span></code> is <code class="docutils literal notranslate"><span class="pre">true</span></code>, this is ISO 8601 timespan duration, which specifies the amount of time the query should stop running after alert is generated. Defaults to <code class="docutils literal notranslate"><span class="pre">PT5H</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.sentinel.AlertRuleScheduled.suppression_enabled">
<code class="sig-name descname">suppression_enabled</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.sentinel.AlertRuleScheduled.suppression_enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Should the Sentinel Scheduled Alert Rulea stop running query after alert is generated? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.sentinel.AlertRuleScheduled.tactics">
<code class="sig-name descname">tactics</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.sentinel.AlertRuleScheduled.tactics" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of categories of attacks by which to classify the rule. Possible values are <code class="docutils literal notranslate"><span class="pre">Collection</span></code>, <code class="docutils literal notranslate"><span class="pre">CommandAndControl</span></code>, <code class="docutils literal notranslate"><span class="pre">CredentialAccess</span></code>, <code class="docutils literal notranslate"><span class="pre">DefenseEvasion</span></code>, <code class="docutils literal notranslate"><span class="pre">Discovery</span></code>, <code class="docutils literal notranslate"><span class="pre">Execution</span></code>, <code class="docutils literal notranslate"><span class="pre">Exfiltration</span></code>, <code class="docutils literal notranslate"><span class="pre">Impact</span></code>, <code class="docutils literal notranslate"><span class="pre">InitialAccess</span></code>, <code class="docutils literal notranslate"><span class="pre">LateralMovement</span></code>, <code class="docutils literal notranslate"><span class="pre">Persistence</span></code> and <code class="docutils literal notranslate"><span class="pre">PrivilegeEscalation</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.sentinel.AlertRuleScheduled.trigger_operator">
<code class="sig-name descname">trigger_operator</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.sentinel.AlertRuleScheduled.trigger_operator" title="Permalink to this definition">¶</a></dt>
<dd><p>The alert trigger operator, combined with <code class="docutils literal notranslate"><span class="pre">trigger_threshold</span></code>, setting alert threshold of this Sentinel Scheduled Alert Rule. Possible values are <code class="docutils literal notranslate"><span class="pre">Equal</span></code>, <code class="docutils literal notranslate"><span class="pre">GreaterThan</span></code>, <code class="docutils literal notranslate"><span class="pre">LessThan</span></code>, <code class="docutils literal notranslate"><span class="pre">NotEqual</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.sentinel.AlertRuleScheduled.trigger_threshold">
<code class="sig-name descname">trigger_threshold</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.sentinel.AlertRuleScheduled.trigger_threshold" title="Permalink to this definition">¶</a></dt>
<dd><p>The baseline number of query results generated, combined with <code class="docutils literal notranslate"><span class="pre">trigger_operator</span></code>, setting alert threshold of this Sentinel Scheduled Alert Rule.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azure.sentinel.AlertRuleScheduled.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">display_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">log_analytics_workspace_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">query</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">query_frequency</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">query_period</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">severity</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">suppression_duration</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">suppression_enabled</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tactics</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">trigger_operator</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">trigger_threshold</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.sentinel.AlertRuleScheduled.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing AlertRuleScheduled resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of this Sentinel Scheduled Alert Rule.</p></li>
<li><p><strong>display_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The friendly name of this Sentinel Scheduled Alert Rule.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Should the Sentinel Scheduled Alert Rule be enabled? Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>log_analytics_workspace_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the Log Analytics Workspace this Sentinel Scheduled Alert Rule belongs to. Changing this forces a new Sentinel Scheduled Alert Rule to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name which should be used for this Sentinel Scheduled Alert Rule. Changing this forces a new Sentinel Scheduled Alert Rule to be created.</p></li>
<li><p><strong>query</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The query of this Sentinel Scheduled Alert Rule.</p></li>
<li><p><strong>query_frequency</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ISO 8601 timespan duration between two consecutive queries. Defaults to <code class="docutils literal notranslate"><span class="pre">PT5H</span></code>.</p></li>
<li><p><strong>query_period</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ISO 8601 timespan duration, which determine the time period of the data covered by the query. For example, it can query the past 10 minutes of data, or the past 6 hours of data. Defaults to <code class="docutils literal notranslate"><span class="pre">PT5H</span></code>.</p></li>
<li><p><strong>severity</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The alert severity of this Sentinel Scheduled Alert Rule. Possible values are <code class="docutils literal notranslate"><span class="pre">High</span></code>, <code class="docutils literal notranslate"><span class="pre">Medium</span></code>, <code class="docutils literal notranslate"><span class="pre">Low</span></code> and <code class="docutils literal notranslate"><span class="pre">Informational</span></code>.</p></li>
<li><p><strong>suppression_duration</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – If <code class="docutils literal notranslate"><span class="pre">suppression_enabled</span></code> is <code class="docutils literal notranslate"><span class="pre">true</span></code>, this is ISO 8601 timespan duration, which specifies the amount of time the query should stop running after alert is generated. Defaults to <code class="docutils literal notranslate"><span class="pre">PT5H</span></code>.</p></li>
<li><p><strong>suppression_enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Should the Sentinel Scheduled Alert Rulea stop running query after alert is generated? Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>tactics</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of categories of attacks by which to classify the rule. Possible values are <code class="docutils literal notranslate"><span class="pre">Collection</span></code>, <code class="docutils literal notranslate"><span class="pre">CommandAndControl</span></code>, <code class="docutils literal notranslate"><span class="pre">CredentialAccess</span></code>, <code class="docutils literal notranslate"><span class="pre">DefenseEvasion</span></code>, <code class="docutils literal notranslate"><span class="pre">Discovery</span></code>, <code class="docutils literal notranslate"><span class="pre">Execution</span></code>, <code class="docutils literal notranslate"><span class="pre">Exfiltration</span></code>, <code class="docutils literal notranslate"><span class="pre">Impact</span></code>, <code class="docutils literal notranslate"><span class="pre">InitialAccess</span></code>, <code class="docutils literal notranslate"><span class="pre">LateralMovement</span></code>, <code class="docutils literal notranslate"><span class="pre">Persistence</span></code> and <code class="docutils literal notranslate"><span class="pre">PrivilegeEscalation</span></code>.</p></li>
<li><p><strong>trigger_operator</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The alert trigger operator, combined with <code class="docutils literal notranslate"><span class="pre">trigger_threshold</span></code>, setting alert threshold of this Sentinel Scheduled Alert Rule. Possible values are <code class="docutils literal notranslate"><span class="pre">Equal</span></code>, <code class="docutils literal notranslate"><span class="pre">GreaterThan</span></code>, <code class="docutils literal notranslate"><span class="pre">LessThan</span></code>, <code class="docutils literal notranslate"><span class="pre">NotEqual</span></code>.</p></li>
<li><p><strong>trigger_threshold</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The baseline number of query results generated, combined with <code class="docutils literal notranslate"><span class="pre">trigger_operator</span></code>, setting alert threshold of this Sentinel Scheduled Alert Rule.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azure.sentinel.AlertRuleScheduled.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.sentinel.AlertRuleScheduled.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.sentinel.AlertRuleScheduled.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.sentinel.AlertRuleScheduled.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.sentinel.AwaitableGetAlertRuleResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.sentinel.</code><code class="sig-name descname">AwaitableGetAlertRuleResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">log_analytics_workspace_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.sentinel.AwaitableGetAlertRuleResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_azure.sentinel.GetAlertRuleResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.sentinel.</code><code class="sig-name descname">GetAlertRuleResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">log_analytics_workspace_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.sentinel.GetAlertRuleResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getAlertRule.</p>
<dl class="py attribute">
<dt id="pulumi_azure.sentinel.GetAlertRuleResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.sentinel.GetAlertRuleResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="py function">
<dt id="pulumi_azure.sentinel.get_alert_rule">
<code class="sig-prename descclassname">pulumi_azure.sentinel.</code><code class="sig-name descname">get_alert_rule</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">log_analytics_workspace_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.sentinel.get_alert_rule" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing Sentinel Alert Rule.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_azure</span> <span class="k">as</span> <span class="nn">azure</span>

<span class="n">example_analytics_workspace</span> <span class="o">=</span> <span class="n">azure</span><span class="o">.</span><span class="n">operationalinsights</span><span class="o">.</span><span class="n">get_analytics_workspace</span><span class="p">(</span><span class="n">name</span><span class="o">=</span><span class="s2">&quot;example&quot;</span><span class="p">,</span>
    <span class="n">resource_group_name</span><span class="o">=</span><span class="s2">&quot;example-resources&quot;</span><span class="p">)</span>
<span class="n">example_alert_rule</span> <span class="o">=</span> <span class="n">azure</span><span class="o">.</span><span class="n">sentinel</span><span class="o">.</span><span class="n">get_alert_rule</span><span class="p">(</span><span class="n">name</span><span class="o">=</span><span class="s2">&quot;existing&quot;</span><span class="p">,</span>
    <span class="n">log_analytics_workspace_id</span><span class="o">=</span><span class="n">example_analytics_workspace</span><span class="o">.</span><span class="n">id</span><span class="p">)</span>
<span class="n">pulumi</span><span class="o">.</span><span class="n">export</span><span class="p">(</span><span class="s2">&quot;id&quot;</span><span class="p">,</span> <span class="n">example_alert_rule</span><span class="o">.</span><span class="n">id</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>log_analytics_workspace_id</strong> (<em>str</em>) – The ID of the Log Analytics Workspace this Sentinel Alert Rule belongs to.</p></li>
<li><p><strong>name</strong> (<em>str</em>) – The name which should be used for this Sentinel Alert Rule.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

</div>
