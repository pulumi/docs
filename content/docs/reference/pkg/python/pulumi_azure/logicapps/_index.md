---
title: Module logicapps
title_tag: Module logicapps | Package pulumi_azure | Python SDK
linktitle: logicapps
notitle: true
block_external_search_index: true
---

{{< resource-docs-alert "azure" >}}

<div class="section" id="logicapps">
<h1>logicapps<a class="headerlink" href="#logicapps" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-azure/issues">pulumi/pulumi-azure repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azurerm/issues">terraform-providers/terraform-provider-azurerm repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_azure.logicapps"></span><dl class="py class">
<dt id="pulumi_azure.logicapps.ActionCustom">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.logicapps.</code><code class="sig-name descname">ActionCustom</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">body</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">logic_app_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.logicapps.ActionCustom" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Custom Action within a Logic App Workflow</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_azure</span> <span class="k">as</span> <span class="nn">azure</span>

<span class="n">example_resource_group</span> <span class="o">=</span> <span class="n">azure</span><span class="o">.</span><span class="n">core</span><span class="o">.</span><span class="n">ResourceGroup</span><span class="p">(</span><span class="s2">&quot;exampleResourceGroup&quot;</span><span class="p">,</span> <span class="n">location</span><span class="o">=</span><span class="s2">&quot;East US&quot;</span><span class="p">)</span>
<span class="n">example_workflow</span> <span class="o">=</span> <span class="n">azure</span><span class="o">.</span><span class="n">logicapps</span><span class="o">.</span><span class="n">Workflow</span><span class="p">(</span><span class="s2">&quot;exampleWorkflow&quot;</span><span class="p">,</span>
    <span class="n">location</span><span class="o">=</span><span class="n">example_resource_group</span><span class="o">.</span><span class="n">location</span><span class="p">,</span>
    <span class="n">resource_group_name</span><span class="o">=</span><span class="n">example_resource_group</span><span class="o">.</span><span class="n">name</span><span class="p">)</span>
<span class="n">example_action_custom</span> <span class="o">=</span> <span class="n">azure</span><span class="o">.</span><span class="n">logicapps</span><span class="o">.</span><span class="n">ActionCustom</span><span class="p">(</span><span class="s2">&quot;exampleActionCustom&quot;</span><span class="p">,</span>
    <span class="n">logic_app_id</span><span class="o">=</span><span class="n">example_workflow</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">body</span><span class="o">=</span><span class="s2">&quot;&quot;&quot;{</span>
<span class="s2">    &quot;description&quot;: &quot;A variable to configure the auto expiration age in days. Configured in negative number. Default is -30 (30 days old).&quot;,</span>
<span class="s2">    &quot;inputs&quot;: {</span>
<span class="s2">        &quot;variables&quot;: [</span>
<span class="s2">            {</span>
<span class="s2">                &quot;name&quot;: &quot;ExpirationAgeInDays&quot;,</span>
<span class="s2">                &quot;type&quot;: &quot;Integer&quot;,</span>
<span class="s2">                &quot;value&quot;: -30</span>
<span class="s2">            }</span>
<span class="s2">        ]</span>
<span class="s2">    },</span>
<span class="s2">    &quot;runAfter&quot;: </span><span class="si">{}</span><span class="s2">,</span>
<span class="s2">    &quot;type&quot;: &quot;InitializeVariable&quot;</span>
<span class="s2">}</span>
<span class="s2">&quot;&quot;&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>body</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the JSON Blob defining the Body of this Custom Action.</p></li>
<li><p><strong>logic_app_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the ID of the Logic App Workflow. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the HTTP Action to be created within the Logic App Workflow. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_azure.logicapps.ActionCustom.body">
<code class="sig-name descname">body</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.logicapps.ActionCustom.body" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the JSON Blob defining the Body of this Custom Action.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.logicapps.ActionCustom.logic_app_id">
<code class="sig-name descname">logic_app_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.logicapps.ActionCustom.logic_app_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the ID of the Logic App Workflow. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.logicapps.ActionCustom.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.logicapps.ActionCustom.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the HTTP Action to be created within the Logic App Workflow. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azure.logicapps.ActionCustom.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">body</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">logic_app_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.logicapps.ActionCustom.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ActionCustom resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>body</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the JSON Blob defining the Body of this Custom Action.</p></li>
<li><p><strong>logic_app_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the ID of the Logic App Workflow. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the HTTP Action to be created within the Logic App Workflow. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azure.logicapps.ActionCustom.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.logicapps.ActionCustom.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.logicapps.ActionCustom.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.logicapps.ActionCustom.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.logicapps.ActionHttp">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.logicapps.</code><code class="sig-name descname">ActionHttp</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">body</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">headers</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">logic_app_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">method</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">run_afters</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">uri</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.logicapps.ActionHttp" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an HTTP Action within a Logic App Workflow</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_azure</span> <span class="k">as</span> <span class="nn">azure</span>

<span class="n">example_resource_group</span> <span class="o">=</span> <span class="n">azure</span><span class="o">.</span><span class="n">core</span><span class="o">.</span><span class="n">ResourceGroup</span><span class="p">(</span><span class="s2">&quot;exampleResourceGroup&quot;</span><span class="p">,</span> <span class="n">location</span><span class="o">=</span><span class="s2">&quot;East US&quot;</span><span class="p">)</span>
<span class="n">example_workflow</span> <span class="o">=</span> <span class="n">azure</span><span class="o">.</span><span class="n">logicapps</span><span class="o">.</span><span class="n">Workflow</span><span class="p">(</span><span class="s2">&quot;exampleWorkflow&quot;</span><span class="p">,</span>
    <span class="n">location</span><span class="o">=</span><span class="n">example_resource_group</span><span class="o">.</span><span class="n">location</span><span class="p">,</span>
    <span class="n">resource_group_name</span><span class="o">=</span><span class="n">example_resource_group</span><span class="o">.</span><span class="n">name</span><span class="p">)</span>
<span class="n">example_action_http</span> <span class="o">=</span> <span class="n">azure</span><span class="o">.</span><span class="n">logicapps</span><span class="o">.</span><span class="n">ActionHttp</span><span class="p">(</span><span class="s2">&quot;exampleActionHttp&quot;</span><span class="p">,</span>
    <span class="n">logic_app_id</span><span class="o">=</span><span class="n">example_workflow</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">method</span><span class="o">=</span><span class="s2">&quot;GET&quot;</span><span class="p">,</span>
    <span class="n">uri</span><span class="o">=</span><span class="s2">&quot;http://example.com/some-webhook&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>body</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the HTTP Body that should be sent to the <code class="docutils literal notranslate"><span class="pre">uri</span></code> when this HTTP Action is triggered.</p></li>
<li><p><strong>headers</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Specifies a Map of Key-Value Pairs that should be sent to the <code class="docutils literal notranslate"><span class="pre">uri</span></code> when this HTTP Action is triggered.</p></li>
<li><p><strong>logic_app_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the ID of the Logic App Workflow. Changing this forces a new resource to be created.</p></li>
<li><p><strong>method</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the HTTP Method which should be used for this HTTP Action. Possible values include <code class="docutils literal notranslate"><span class="pre">DELETE</span></code>, <code class="docutils literal notranslate"><span class="pre">GET</span></code>, <code class="docutils literal notranslate"><span class="pre">PATCH</span></code>, <code class="docutils literal notranslate"><span class="pre">POST</span></code> and <code class="docutils literal notranslate"><span class="pre">PUT</span></code>.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the HTTP Action to be created within the Logic App Workflow. Changing this forces a new resource to be created.</p></li>
<li><p><strong>run_afters</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Specifies the place of the HTTP Action in the Logic App Workflow. If not specified, the HTTP Action is right after the Trigger. A <code class="docutils literal notranslate"><span class="pre">run_after</span></code> block is as defined below.</p></li>
<li><p><strong>uri</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the URI which will be called when this HTTP Action is triggered.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>run_afters</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">actionName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the name of the precedent HTTP Action.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">actionResult</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the expected result of the precedent HTTP Action, only after which the current HTTP Action will be triggered. Possible values include <code class="docutils literal notranslate"><span class="pre">Succeeded</span></code>, <code class="docutils literal notranslate"><span class="pre">Failed</span></code>, <code class="docutils literal notranslate"><span class="pre">Skipped</span></code> and <code class="docutils literal notranslate"><span class="pre">TimedOut</span></code>.</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_azure.logicapps.ActionHttp.body">
<code class="sig-name descname">body</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.logicapps.ActionHttp.body" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the HTTP Body that should be sent to the <code class="docutils literal notranslate"><span class="pre">uri</span></code> when this HTTP Action is triggered.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.logicapps.ActionHttp.headers">
<code class="sig-name descname">headers</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.logicapps.ActionHttp.headers" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies a Map of Key-Value Pairs that should be sent to the <code class="docutils literal notranslate"><span class="pre">uri</span></code> when this HTTP Action is triggered.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.logicapps.ActionHttp.logic_app_id">
<code class="sig-name descname">logic_app_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.logicapps.ActionHttp.logic_app_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the ID of the Logic App Workflow. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.logicapps.ActionHttp.method">
<code class="sig-name descname">method</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.logicapps.ActionHttp.method" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the HTTP Method which should be used for this HTTP Action. Possible values include <code class="docutils literal notranslate"><span class="pre">DELETE</span></code>, <code class="docutils literal notranslate"><span class="pre">GET</span></code>, <code class="docutils literal notranslate"><span class="pre">PATCH</span></code>, <code class="docutils literal notranslate"><span class="pre">POST</span></code> and <code class="docutils literal notranslate"><span class="pre">PUT</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.logicapps.ActionHttp.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.logicapps.ActionHttp.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the HTTP Action to be created within the Logic App Workflow. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.logicapps.ActionHttp.run_afters">
<code class="sig-name descname">run_afters</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.logicapps.ActionHttp.run_afters" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the place of the HTTP Action in the Logic App Workflow. If not specified, the HTTP Action is right after the Trigger. A <code class="docutils literal notranslate"><span class="pre">run_after</span></code> block is as defined below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">actionName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the name of the precedent HTTP Action.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">actionResult</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Specifies the expected result of the precedent HTTP Action, only after which the current HTTP Action will be triggered. Possible values include <code class="docutils literal notranslate"><span class="pre">Succeeded</span></code>, <code class="docutils literal notranslate"><span class="pre">Failed</span></code>, <code class="docutils literal notranslate"><span class="pre">Skipped</span></code> and <code class="docutils literal notranslate"><span class="pre">TimedOut</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.logicapps.ActionHttp.uri">
<code class="sig-name descname">uri</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.logicapps.ActionHttp.uri" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the URI which will be called when this HTTP Action is triggered.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azure.logicapps.ActionHttp.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">body</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">headers</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">logic_app_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">method</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">run_afters</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">uri</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.logicapps.ActionHttp.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ActionHttp resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>body</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the HTTP Body that should be sent to the <code class="docutils literal notranslate"><span class="pre">uri</span></code> when this HTTP Action is triggered.</p></li>
<li><p><strong>headers</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Specifies a Map of Key-Value Pairs that should be sent to the <code class="docutils literal notranslate"><span class="pre">uri</span></code> when this HTTP Action is triggered.</p></li>
<li><p><strong>logic_app_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the ID of the Logic App Workflow. Changing this forces a new resource to be created.</p></li>
<li><p><strong>method</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the HTTP Method which should be used for this HTTP Action. Possible values include <code class="docutils literal notranslate"><span class="pre">DELETE</span></code>, <code class="docutils literal notranslate"><span class="pre">GET</span></code>, <code class="docutils literal notranslate"><span class="pre">PATCH</span></code>, <code class="docutils literal notranslate"><span class="pre">POST</span></code> and <code class="docutils literal notranslate"><span class="pre">PUT</span></code>.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the HTTP Action to be created within the Logic App Workflow. Changing this forces a new resource to be created.</p></li>
<li><p><strong>run_afters</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Specifies the place of the HTTP Action in the Logic App Workflow. If not specified, the HTTP Action is right after the Trigger. A <code class="docutils literal notranslate"><span class="pre">run_after</span></code> block is as defined below.</p></li>
<li><p><strong>uri</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the URI which will be called when this HTTP Action is triggered.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>run_afters</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">actionName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the name of the precedent HTTP Action.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">actionResult</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Specifies the expected result of the precedent HTTP Action, only after which the current HTTP Action will be triggered. Possible values include <code class="docutils literal notranslate"><span class="pre">Succeeded</span></code>, <code class="docutils literal notranslate"><span class="pre">Failed</span></code>, <code class="docutils literal notranslate"><span class="pre">Skipped</span></code> and <code class="docutils literal notranslate"><span class="pre">TimedOut</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azure.logicapps.ActionHttp.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.logicapps.ActionHttp.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.logicapps.ActionHttp.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.logicapps.ActionHttp.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.logicapps.AwaitableGetIntegrationAccountResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.logicapps.</code><code class="sig-name descname">AwaitableGetIntegrationAccountResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">location</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sku_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.logicapps.AwaitableGetIntegrationAccountResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_azure.logicapps.AwaitableGetWorkflowResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.logicapps.</code><code class="sig-name descname">AwaitableGetWorkflowResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">access_endpoint</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">connector_endpoint_ip_addresses</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">connector_outbound_ip_addresses</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">location</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">logic_app_integration_account_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">parameters</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">workflow_endpoint_ip_addresses</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">workflow_outbound_ip_addresses</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">workflow_schema</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">workflow_version</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.logicapps.AwaitableGetWorkflowResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_azure.logicapps.GetIntegrationAccountResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.logicapps.</code><code class="sig-name descname">GetIntegrationAccountResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">location</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sku_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.logicapps.GetIntegrationAccountResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getIntegrationAccount.</p>
<dl class="py attribute">
<dt id="pulumi_azure.logicapps.GetIntegrationAccountResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.logicapps.GetIntegrationAccountResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.logicapps.GetIntegrationAccountResult.location">
<code class="sig-name descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.logicapps.GetIntegrationAccountResult.location" title="Permalink to this definition">¶</a></dt>
<dd><p>The Azure Region where the Logic App Integration Account exists.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.logicapps.GetIntegrationAccountResult.sku_name">
<code class="sig-name descname">sku_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.logicapps.GetIntegrationAccountResult.sku_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The sku name of the Logic App Integration Account.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.logicapps.GetIntegrationAccountResult.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.logicapps.GetIntegrationAccountResult.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags assigned to the Logic App Integration Account.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_azure.logicapps.GetWorkflowResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.logicapps.</code><code class="sig-name descname">GetWorkflowResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">access_endpoint</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">connector_endpoint_ip_addresses</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">connector_outbound_ip_addresses</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">location</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">logic_app_integration_account_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">parameters</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">workflow_endpoint_ip_addresses</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">workflow_outbound_ip_addresses</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">workflow_schema</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">workflow_version</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.logicapps.GetWorkflowResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getWorkflow.</p>
<dl class="py attribute">
<dt id="pulumi_azure.logicapps.GetWorkflowResult.access_endpoint">
<code class="sig-name descname">access_endpoint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.logicapps.GetWorkflowResult.access_endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>The Access Endpoint for the Logic App Workflow</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.logicapps.GetWorkflowResult.connector_endpoint_ip_addresses">
<code class="sig-name descname">connector_endpoint_ip_addresses</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.logicapps.GetWorkflowResult.connector_endpoint_ip_addresses" title="Permalink to this definition">¶</a></dt>
<dd><p>The list of access endpoint ip addresses of connector.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.logicapps.GetWorkflowResult.connector_outbound_ip_addresses">
<code class="sig-name descname">connector_outbound_ip_addresses</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.logicapps.GetWorkflowResult.connector_outbound_ip_addresses" title="Permalink to this definition">¶</a></dt>
<dd><p>The list of outgoing ip addresses of connector.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.logicapps.GetWorkflowResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.logicapps.GetWorkflowResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.logicapps.GetWorkflowResult.location">
<code class="sig-name descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.logicapps.GetWorkflowResult.location" title="Permalink to this definition">¶</a></dt>
<dd><p>The Azure location where the Logic App Workflow exists.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.logicapps.GetWorkflowResult.logic_app_integration_account_id">
<code class="sig-name descname">logic_app_integration_account_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.logicapps.GetWorkflowResult.logic_app_integration_account_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the integration account linked by this Logic App Workflow.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.logicapps.GetWorkflowResult.parameters">
<code class="sig-name descname">parameters</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.logicapps.GetWorkflowResult.parameters" title="Permalink to this definition">¶</a></dt>
<dd><p>A map of Key-Value pairs.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.logicapps.GetWorkflowResult.tags">
<code class="sig-name descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.logicapps.GetWorkflowResult.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags assigned to the resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.logicapps.GetWorkflowResult.workflow_endpoint_ip_addresses">
<code class="sig-name descname">workflow_endpoint_ip_addresses</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.logicapps.GetWorkflowResult.workflow_endpoint_ip_addresses" title="Permalink to this definition">¶</a></dt>
<dd><p>The list of access endpoint ip addresses of workflow.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.logicapps.GetWorkflowResult.workflow_outbound_ip_addresses">
<code class="sig-name descname">workflow_outbound_ip_addresses</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.logicapps.GetWorkflowResult.workflow_outbound_ip_addresses" title="Permalink to this definition">¶</a></dt>
<dd><p>The list of outgoing ip addresses of workflow.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.logicapps.GetWorkflowResult.workflow_schema">
<code class="sig-name descname">workflow_schema</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.logicapps.GetWorkflowResult.workflow_schema" title="Permalink to this definition">¶</a></dt>
<dd><p>The Schema used for this Logic App Workflow.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.logicapps.GetWorkflowResult.workflow_version">
<code class="sig-name descname">workflow_version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.logicapps.GetWorkflowResult.workflow_version" title="Permalink to this definition">¶</a></dt>
<dd><p>The version of the Schema used for this Logic App Workflow. Defaults to <code class="docutils literal notranslate"><span class="pre">1.0.0.0</span></code>.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_azure.logicapps.IntegrationAccount">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.logicapps.</code><code class="sig-name descname">IntegrationAccount</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">location</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sku_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.logicapps.IntegrationAccount" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Logic App Integration Account.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_azure</span> <span class="k">as</span> <span class="nn">azure</span>

<span class="n">example_resource_group</span> <span class="o">=</span> <span class="n">azure</span><span class="o">.</span><span class="n">core</span><span class="o">.</span><span class="n">ResourceGroup</span><span class="p">(</span><span class="s2">&quot;exampleResourceGroup&quot;</span><span class="p">,</span> <span class="n">location</span><span class="o">=</span><span class="s2">&quot;West Europe&quot;</span><span class="p">)</span>
<span class="n">example_integration_account</span> <span class="o">=</span> <span class="n">azure</span><span class="o">.</span><span class="n">logicapps</span><span class="o">.</span><span class="n">IntegrationAccount</span><span class="p">(</span><span class="s2">&quot;exampleIntegrationAccount&quot;</span><span class="p">,</span>
    <span class="n">resource_group_name</span><span class="o">=</span><span class="n">example_resource_group</span><span class="o">.</span><span class="n">name</span><span class="p">,</span>
    <span class="n">location</span><span class="o">=</span><span class="n">example_resource_group</span><span class="o">.</span><span class="n">location</span><span class="p">,</span>
    <span class="n">sku_name</span><span class="o">=</span><span class="s2">&quot;Standard&quot;</span><span class="p">,</span>
    <span class="n">tags</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;foo&quot;</span><span class="p">:</span> <span class="s2">&quot;bar&quot;</span><span class="p">,</span>
    <span class="p">})</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Azure Region where the Logic App Integration Account should exist. Changing this forces a new Logic App Integration Account to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name which should be used for this Logic App Integration Account. Changing this forces a new Logic App Integration Account to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Resource Group where the Logic App Integration Account should exist. Changing this forces a new Logic App Integration Account to be created.</p></li>
<li><p><strong>sku_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The sku name of the Logic App Integration Account. Possible Values are <code class="docutils literal notranslate"><span class="pre">Basic</span></code>, <code class="docutils literal notranslate"><span class="pre">Free</span></code> and <code class="docutils literal notranslate"><span class="pre">Standard</span></code>.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags which should be assigned to the Logic App Integration Account.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_azure.logicapps.IntegrationAccount.location">
<code class="sig-name descname">location</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.logicapps.IntegrationAccount.location" title="Permalink to this definition">¶</a></dt>
<dd><p>The Azure Region where the Logic App Integration Account should exist. Changing this forces a new Logic App Integration Account to be created.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.logicapps.IntegrationAccount.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.logicapps.IntegrationAccount.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name which should be used for this Logic App Integration Account. Changing this forces a new Logic App Integration Account to be created.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.logicapps.IntegrationAccount.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.logicapps.IntegrationAccount.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Resource Group where the Logic App Integration Account should exist. Changing this forces a new Logic App Integration Account to be created.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.logicapps.IntegrationAccount.sku_name">
<code class="sig-name descname">sku_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.logicapps.IntegrationAccount.sku_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The sku name of the Logic App Integration Account. Possible Values are <code class="docutils literal notranslate"><span class="pre">Basic</span></code>, <code class="docutils literal notranslate"><span class="pre">Free</span></code> and <code class="docutils literal notranslate"><span class="pre">Standard</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.logicapps.IntegrationAccount.tags">
<code class="sig-name descname">tags</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.logicapps.IntegrationAccount.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags which should be assigned to the Logic App Integration Account.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azure.logicapps.IntegrationAccount.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">location</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sku_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.logicapps.IntegrationAccount.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing IntegrationAccount resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Azure Region where the Logic App Integration Account should exist. Changing this forces a new Logic App Integration Account to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name which should be used for this Logic App Integration Account. Changing this forces a new Logic App Integration Account to be created.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Resource Group where the Logic App Integration Account should exist. Changing this forces a new Logic App Integration Account to be created.</p></li>
<li><p><strong>sku_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The sku name of the Logic App Integration Account. Possible Values are <code class="docutils literal notranslate"><span class="pre">Basic</span></code>, <code class="docutils literal notranslate"><span class="pre">Free</span></code> and <code class="docutils literal notranslate"><span class="pre">Standard</span></code>.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags which should be assigned to the Logic App Integration Account.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azure.logicapps.IntegrationAccount.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.logicapps.IntegrationAccount.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.logicapps.IntegrationAccount.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.logicapps.IntegrationAccount.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.logicapps.TriggerCustom">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.logicapps.</code><code class="sig-name descname">TriggerCustom</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">body</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">logic_app_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.logicapps.TriggerCustom" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Custom Trigger within a Logic App Workflow</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_azure</span> <span class="k">as</span> <span class="nn">azure</span>

<span class="n">example_resource_group</span> <span class="o">=</span> <span class="n">azure</span><span class="o">.</span><span class="n">core</span><span class="o">.</span><span class="n">ResourceGroup</span><span class="p">(</span><span class="s2">&quot;exampleResourceGroup&quot;</span><span class="p">,</span> <span class="n">location</span><span class="o">=</span><span class="s2">&quot;East US&quot;</span><span class="p">)</span>
<span class="n">example_workflow</span> <span class="o">=</span> <span class="n">azure</span><span class="o">.</span><span class="n">logicapps</span><span class="o">.</span><span class="n">Workflow</span><span class="p">(</span><span class="s2">&quot;exampleWorkflow&quot;</span><span class="p">,</span>
    <span class="n">location</span><span class="o">=</span><span class="n">example_resource_group</span><span class="o">.</span><span class="n">location</span><span class="p">,</span>
    <span class="n">resource_group_name</span><span class="o">=</span><span class="n">example_resource_group</span><span class="o">.</span><span class="n">name</span><span class="p">)</span>
<span class="n">example_trigger_custom</span> <span class="o">=</span> <span class="n">azure</span><span class="o">.</span><span class="n">logicapps</span><span class="o">.</span><span class="n">TriggerCustom</span><span class="p">(</span><span class="s2">&quot;exampleTriggerCustom&quot;</span><span class="p">,</span>
    <span class="n">logic_app_id</span><span class="o">=</span><span class="n">example_workflow</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">body</span><span class="o">=</span><span class="s2">&quot;&quot;&quot;{</span>
<span class="s2">  &quot;recurrence&quot;: {</span>
<span class="s2">    &quot;frequency&quot;: &quot;Day&quot;,</span>
<span class="s2">    &quot;interval&quot;: 1</span>
<span class="s2">  },</span>
<span class="s2">  &quot;type&quot;: &quot;Recurrence&quot;</span>
<span class="s2">}</span>
<span class="s2">&quot;&quot;&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>body</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the JSON Blob defining the Body of this Custom Trigger.</p></li>
<li><p><strong>logic_app_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the ID of the Logic App Workflow. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the HTTP Trigger to be created within the Logic App Workflow. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_azure.logicapps.TriggerCustom.body">
<code class="sig-name descname">body</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.logicapps.TriggerCustom.body" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the JSON Blob defining the Body of this Custom Trigger.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.logicapps.TriggerCustom.logic_app_id">
<code class="sig-name descname">logic_app_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.logicapps.TriggerCustom.logic_app_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the ID of the Logic App Workflow. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.logicapps.TriggerCustom.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.logicapps.TriggerCustom.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the HTTP Trigger to be created within the Logic App Workflow. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azure.logicapps.TriggerCustom.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">body</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">logic_app_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.logicapps.TriggerCustom.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing TriggerCustom resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>body</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the JSON Blob defining the Body of this Custom Trigger.</p></li>
<li><p><strong>logic_app_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the ID of the Logic App Workflow. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the HTTP Trigger to be created within the Logic App Workflow. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azure.logicapps.TriggerCustom.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.logicapps.TriggerCustom.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.logicapps.TriggerCustom.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.logicapps.TriggerCustom.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.logicapps.TriggerHttpRequest">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.logicapps.</code><code class="sig-name descname">TriggerHttpRequest</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">logic_app_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">method</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">relative_path</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">schema</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.logicapps.TriggerHttpRequest" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a HTTP Request Trigger within a Logic App Workflow</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_azure</span> <span class="k">as</span> <span class="nn">azure</span>

<span class="n">example_resource_group</span> <span class="o">=</span> <span class="n">azure</span><span class="o">.</span><span class="n">core</span><span class="o">.</span><span class="n">ResourceGroup</span><span class="p">(</span><span class="s2">&quot;exampleResourceGroup&quot;</span><span class="p">,</span> <span class="n">location</span><span class="o">=</span><span class="s2">&quot;East US&quot;</span><span class="p">)</span>
<span class="n">example_workflow</span> <span class="o">=</span> <span class="n">azure</span><span class="o">.</span><span class="n">logicapps</span><span class="o">.</span><span class="n">Workflow</span><span class="p">(</span><span class="s2">&quot;exampleWorkflow&quot;</span><span class="p">,</span>
    <span class="n">location</span><span class="o">=</span><span class="n">example_resource_group</span><span class="o">.</span><span class="n">location</span><span class="p">,</span>
    <span class="n">resource_group_name</span><span class="o">=</span><span class="n">example_resource_group</span><span class="o">.</span><span class="n">name</span><span class="p">)</span>
<span class="n">example_trigger_http_request</span> <span class="o">=</span> <span class="n">azure</span><span class="o">.</span><span class="n">logicapps</span><span class="o">.</span><span class="n">TriggerHttpRequest</span><span class="p">(</span><span class="s2">&quot;exampleTriggerHttpRequest&quot;</span><span class="p">,</span>
    <span class="n">logic_app_id</span><span class="o">=</span><span class="n">example_workflow</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">schema</span><span class="o">=</span><span class="s2">&quot;&quot;&quot;{</span>
<span class="s2">    &quot;type&quot;: &quot;object&quot;,</span>
<span class="s2">    &quot;properties&quot;: {</span>
<span class="s2">        &quot;hello&quot;: {</span>
<span class="s2">            &quot;type&quot;: &quot;string&quot;</span>
<span class="s2">        }</span>
<span class="s2">    }</span>
<span class="s2">}</span>
<span class="s2">&quot;&quot;&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>logic_app_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the ID of the Logic App Workflow. Changing this forces a new resource to be created.</p></li>
<li><p><strong>method</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the HTTP Method which the request be using. Possible values include <code class="docutils literal notranslate"><span class="pre">DELETE</span></code>, <code class="docutils literal notranslate"><span class="pre">GET</span></code>, <code class="docutils literal notranslate"><span class="pre">PATCH</span></code>, <code class="docutils literal notranslate"><span class="pre">POST</span></code> or <code class="docutils literal notranslate"><span class="pre">PUT</span></code>.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the HTTP Request Trigger to be created within the Logic App Workflow. Changing this forces a new resource to be created.</p></li>
<li><p><strong>relative_path</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the Relative Path used for this Request.</p></li>
<li><p><strong>schema</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A JSON Blob defining the Schema of the incoming request. This needs to be valid JSON.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_azure.logicapps.TriggerHttpRequest.logic_app_id">
<code class="sig-name descname">logic_app_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.logicapps.TriggerHttpRequest.logic_app_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the ID of the Logic App Workflow. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.logicapps.TriggerHttpRequest.method">
<code class="sig-name descname">method</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.logicapps.TriggerHttpRequest.method" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the HTTP Method which the request be using. Possible values include <code class="docutils literal notranslate"><span class="pre">DELETE</span></code>, <code class="docutils literal notranslate"><span class="pre">GET</span></code>, <code class="docutils literal notranslate"><span class="pre">PATCH</span></code>, <code class="docutils literal notranslate"><span class="pre">POST</span></code> or <code class="docutils literal notranslate"><span class="pre">PUT</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.logicapps.TriggerHttpRequest.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.logicapps.TriggerHttpRequest.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the HTTP Request Trigger to be created within the Logic App Workflow. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.logicapps.TriggerHttpRequest.relative_path">
<code class="sig-name descname">relative_path</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.logicapps.TriggerHttpRequest.relative_path" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the Relative Path used for this Request.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.logicapps.TriggerHttpRequest.schema">
<code class="sig-name descname">schema</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.logicapps.TriggerHttpRequest.schema" title="Permalink to this definition">¶</a></dt>
<dd><p>A JSON Blob defining the Schema of the incoming request. This needs to be valid JSON.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azure.logicapps.TriggerHttpRequest.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">logic_app_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">method</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">relative_path</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">schema</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.logicapps.TriggerHttpRequest.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing TriggerHttpRequest resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>logic_app_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the ID of the Logic App Workflow. Changing this forces a new resource to be created.</p></li>
<li><p><strong>method</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the HTTP Method which the request be using. Possible values include <code class="docutils literal notranslate"><span class="pre">DELETE</span></code>, <code class="docutils literal notranslate"><span class="pre">GET</span></code>, <code class="docutils literal notranslate"><span class="pre">PATCH</span></code>, <code class="docutils literal notranslate"><span class="pre">POST</span></code> or <code class="docutils literal notranslate"><span class="pre">PUT</span></code>.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the HTTP Request Trigger to be created within the Logic App Workflow. Changing this forces a new resource to be created.</p></li>
<li><p><strong>relative_path</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the Relative Path used for this Request.</p></li>
<li><p><strong>schema</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A JSON Blob defining the Schema of the incoming request. This needs to be valid JSON.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azure.logicapps.TriggerHttpRequest.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.logicapps.TriggerHttpRequest.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.logicapps.TriggerHttpRequest.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.logicapps.TriggerHttpRequest.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.logicapps.TriggerRecurrence">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.logicapps.</code><code class="sig-name descname">TriggerRecurrence</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">frequency</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">interval</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">logic_app_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">start_time</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.logicapps.TriggerRecurrence" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Recurrence Trigger within a Logic App Workflow</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_azure</span> <span class="k">as</span> <span class="nn">azure</span>

<span class="n">example_resource_group</span> <span class="o">=</span> <span class="n">azure</span><span class="o">.</span><span class="n">core</span><span class="o">.</span><span class="n">ResourceGroup</span><span class="p">(</span><span class="s2">&quot;exampleResourceGroup&quot;</span><span class="p">,</span> <span class="n">location</span><span class="o">=</span><span class="s2">&quot;East US&quot;</span><span class="p">)</span>
<span class="n">example_workflow</span> <span class="o">=</span> <span class="n">azure</span><span class="o">.</span><span class="n">logicapps</span><span class="o">.</span><span class="n">Workflow</span><span class="p">(</span><span class="s2">&quot;exampleWorkflow&quot;</span><span class="p">,</span>
    <span class="n">location</span><span class="o">=</span><span class="n">example_resource_group</span><span class="o">.</span><span class="n">location</span><span class="p">,</span>
    <span class="n">resource_group_name</span><span class="o">=</span><span class="n">example_resource_group</span><span class="o">.</span><span class="n">name</span><span class="p">)</span>
<span class="n">example_trigger_recurrence</span> <span class="o">=</span> <span class="n">azure</span><span class="o">.</span><span class="n">logicapps</span><span class="o">.</span><span class="n">TriggerRecurrence</span><span class="p">(</span><span class="s2">&quot;exampleTriggerRecurrence&quot;</span><span class="p">,</span>
    <span class="n">logic_app_id</span><span class="o">=</span><span class="n">example_workflow</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">frequency</span><span class="o">=</span><span class="s2">&quot;Day&quot;</span><span class="p">,</span>
    <span class="n">interval</span><span class="o">=</span><span class="mi">1</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>frequency</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the Frequency at which this Trigger should be run. Possible values include <code class="docutils literal notranslate"><span class="pre">Month</span></code>, <code class="docutils literal notranslate"><span class="pre">Week</span></code>, <code class="docutils literal notranslate"><span class="pre">Day</span></code>, <code class="docutils literal notranslate"><span class="pre">Hour</span></code>, <code class="docutils literal notranslate"><span class="pre">Minute</span></code> and <code class="docutils literal notranslate"><span class="pre">Second</span></code>.</p></li>
<li><p><strong>interval</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Specifies interval used for the Frequency, for example a value of <code class="docutils literal notranslate"><span class="pre">4</span></code> for <code class="docutils literal notranslate"><span class="pre">interval</span></code> and <code class="docutils literal notranslate"><span class="pre">hour</span></code> for <code class="docutils literal notranslate"><span class="pre">frequency</span></code> would run the Trigger every 4 hours.</p></li>
<li><p><strong>logic_app_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the ID of the Logic App Workflow. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Recurrence Triggers to be created within the Logic App Workflow. Changing this forces a new resource to be created.</p></li>
<li><p><strong>start_time</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the start date and time for this trigger in RFC3339 format: <code class="docutils literal notranslate"><span class="pre">2000-01-02T03:04:05Z</span></code>.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_azure.logicapps.TriggerRecurrence.frequency">
<code class="sig-name descname">frequency</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.logicapps.TriggerRecurrence.frequency" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the Frequency at which this Trigger should be run. Possible values include <code class="docutils literal notranslate"><span class="pre">Month</span></code>, <code class="docutils literal notranslate"><span class="pre">Week</span></code>, <code class="docutils literal notranslate"><span class="pre">Day</span></code>, <code class="docutils literal notranslate"><span class="pre">Hour</span></code>, <code class="docutils literal notranslate"><span class="pre">Minute</span></code> and <code class="docutils literal notranslate"><span class="pre">Second</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.logicapps.TriggerRecurrence.interval">
<code class="sig-name descname">interval</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.logicapps.TriggerRecurrence.interval" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies interval used for the Frequency, for example a value of <code class="docutils literal notranslate"><span class="pre">4</span></code> for <code class="docutils literal notranslate"><span class="pre">interval</span></code> and <code class="docutils literal notranslate"><span class="pre">hour</span></code> for <code class="docutils literal notranslate"><span class="pre">frequency</span></code> would run the Trigger every 4 hours.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.logicapps.TriggerRecurrence.logic_app_id">
<code class="sig-name descname">logic_app_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.logicapps.TriggerRecurrence.logic_app_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the ID of the Logic App Workflow. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.logicapps.TriggerRecurrence.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.logicapps.TriggerRecurrence.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Recurrence Triggers to be created within the Logic App Workflow. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.logicapps.TriggerRecurrence.start_time">
<code class="sig-name descname">start_time</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.logicapps.TriggerRecurrence.start_time" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the start date and time for this trigger in RFC3339 format: <code class="docutils literal notranslate"><span class="pre">2000-01-02T03:04:05Z</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azure.logicapps.TriggerRecurrence.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">frequency</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">interval</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">logic_app_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">start_time</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.logicapps.TriggerRecurrence.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing TriggerRecurrence resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>frequency</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the Frequency at which this Trigger should be run. Possible values include <code class="docutils literal notranslate"><span class="pre">Month</span></code>, <code class="docutils literal notranslate"><span class="pre">Week</span></code>, <code class="docutils literal notranslate"><span class="pre">Day</span></code>, <code class="docutils literal notranslate"><span class="pre">Hour</span></code>, <code class="docutils literal notranslate"><span class="pre">Minute</span></code> and <code class="docutils literal notranslate"><span class="pre">Second</span></code>.</p></li>
<li><p><strong>interval</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Specifies interval used for the Frequency, for example a value of <code class="docutils literal notranslate"><span class="pre">4</span></code> for <code class="docutils literal notranslate"><span class="pre">interval</span></code> and <code class="docutils literal notranslate"><span class="pre">hour</span></code> for <code class="docutils literal notranslate"><span class="pre">frequency</span></code> would run the Trigger every 4 hours.</p></li>
<li><p><strong>logic_app_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the ID of the Logic App Workflow. Changing this forces a new resource to be created.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Recurrence Triggers to be created within the Logic App Workflow. Changing this forces a new resource to be created.</p></li>
<li><p><strong>start_time</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the start date and time for this trigger in RFC3339 format: <code class="docutils literal notranslate"><span class="pre">2000-01-02T03:04:05Z</span></code>.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azure.logicapps.TriggerRecurrence.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.logicapps.TriggerRecurrence.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.logicapps.TriggerRecurrence.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.logicapps.TriggerRecurrence.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.logicapps.Workflow">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azure.logicapps.</code><code class="sig-name descname">Workflow</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">location</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">logic_app_integration_account_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">parameters</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">workflow_schema</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">workflow_version</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.logicapps.Workflow" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Logic App Workflow.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_azure</span> <span class="k">as</span> <span class="nn">azure</span>

<span class="n">example_resource_group</span> <span class="o">=</span> <span class="n">azure</span><span class="o">.</span><span class="n">core</span><span class="o">.</span><span class="n">ResourceGroup</span><span class="p">(</span><span class="s2">&quot;exampleResourceGroup&quot;</span><span class="p">,</span> <span class="n">location</span><span class="o">=</span><span class="s2">&quot;East US&quot;</span><span class="p">)</span>
<span class="n">example_workflow</span> <span class="o">=</span> <span class="n">azure</span><span class="o">.</span><span class="n">logicapps</span><span class="o">.</span><span class="n">Workflow</span><span class="p">(</span><span class="s2">&quot;exampleWorkflow&quot;</span><span class="p">,</span>
    <span class="n">location</span><span class="o">=</span><span class="n">example_resource_group</span><span class="o">.</span><span class="n">location</span><span class="p">,</span>
    <span class="n">resource_group_name</span><span class="o">=</span><span class="n">example_resource_group</span><span class="o">.</span><span class="n">name</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the Logic App Workflow exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>logic_app_integration_account_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the integration account linked by this Logic App Workflow.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Logic App Workflow. Changing this forces a new resource to be created.</p></li>
<li><p><strong>parameters</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of Key-Value pairs.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Resource Group in which the Logic App Workflow should be created. Changing this forces a new resource to be created.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
<li><p><strong>workflow_schema</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the Schema to use for this Logic App Workflow. Defaults to <code class="docutils literal notranslate"><span class="pre">https://schema.management.azure.com/providers/Microsoft.Logic/schemas/2016-06-01/workflowdefinition.json#</span></code>. Changing this forces a new resource to be created.</p></li>
<li><p><strong>workflow_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the version of the Schema used for this Logic App Workflow. Defaults to <code class="docutils literal notranslate"><span class="pre">1.0.0.0</span></code>. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_azure.logicapps.Workflow.access_endpoint">
<code class="sig-name descname">access_endpoint</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.logicapps.Workflow.access_endpoint" title="Permalink to this definition">¶</a></dt>
<dd><p>The Access Endpoint for the Logic App Workflow.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.logicapps.Workflow.connector_endpoint_ip_addresses">
<code class="sig-name descname">connector_endpoint_ip_addresses</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.logicapps.Workflow.connector_endpoint_ip_addresses" title="Permalink to this definition">¶</a></dt>
<dd><p>The list of access endpoint ip addresses of connector.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.logicapps.Workflow.connector_outbound_ip_addresses">
<code class="sig-name descname">connector_outbound_ip_addresses</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.logicapps.Workflow.connector_outbound_ip_addresses" title="Permalink to this definition">¶</a></dt>
<dd><p>The list of outgoing ip addresses of connector.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.logicapps.Workflow.location">
<code class="sig-name descname">location</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.logicapps.Workflow.location" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the supported Azure location where the Logic App Workflow exists. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.logicapps.Workflow.logic_app_integration_account_id">
<code class="sig-name descname">logic_app_integration_account_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.logicapps.Workflow.logic_app_integration_account_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the integration account linked by this Logic App Workflow.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.logicapps.Workflow.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.logicapps.Workflow.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the name of the Logic App Workflow. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.logicapps.Workflow.parameters">
<code class="sig-name descname">parameters</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.logicapps.Workflow.parameters" title="Permalink to this definition">¶</a></dt>
<dd><p>A map of Key-Value pairs.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.logicapps.Workflow.resource_group_name">
<code class="sig-name descname">resource_group_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.logicapps.Workflow.resource_group_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Resource Group in which the Logic App Workflow should be created. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.logicapps.Workflow.tags">
<code class="sig-name descname">tags</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.logicapps.Workflow.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping of tags to assign to the resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.logicapps.Workflow.workflow_endpoint_ip_addresses">
<code class="sig-name descname">workflow_endpoint_ip_addresses</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.logicapps.Workflow.workflow_endpoint_ip_addresses" title="Permalink to this definition">¶</a></dt>
<dd><p>The list of access endpoint ip addresses of workflow.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.logicapps.Workflow.workflow_outbound_ip_addresses">
<code class="sig-name descname">workflow_outbound_ip_addresses</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.logicapps.Workflow.workflow_outbound_ip_addresses" title="Permalink to this definition">¶</a></dt>
<dd><p>The list of outgoing ip addresses of workflow.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.logicapps.Workflow.workflow_schema">
<code class="sig-name descname">workflow_schema</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.logicapps.Workflow.workflow_schema" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the Schema to use for this Logic App Workflow. Defaults to <code class="docutils literal notranslate"><span class="pre">https://schema.management.azure.com/providers/Microsoft.Logic/schemas/2016-06-01/workflowdefinition.json#</span></code>. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azure.logicapps.Workflow.workflow_version">
<code class="sig-name descname">workflow_version</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azure.logicapps.Workflow.workflow_version" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the version of the Schema used for this Logic App Workflow. Defaults to <code class="docutils literal notranslate"><span class="pre">1.0.0.0</span></code>. Changing this forces a new resource to be created.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azure.logicapps.Workflow.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">access_endpoint</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">connector_endpoint_ip_addresses</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">connector_outbound_ip_addresses</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">location</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">logic_app_integration_account_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">parameters</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">workflow_endpoint_ip_addresses</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">workflow_outbound_ip_addresses</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">workflow_schema</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">workflow_version</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.logicapps.Workflow.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Workflow resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>access_endpoint</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Access Endpoint for the Logic App Workflow.</p></li>
<li><p><strong>connector_endpoint_ip_addresses</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The list of access endpoint ip addresses of connector.</p></li>
<li><p><strong>connector_outbound_ip_addresses</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The list of outgoing ip addresses of connector.</p></li>
<li><p><strong>location</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the supported Azure location where the Logic App Workflow exists. Changing this forces a new resource to be created.</p></li>
<li><p><strong>logic_app_integration_account_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the integration account linked by this Logic App Workflow.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the name of the Logic App Workflow. Changing this forces a new resource to be created.</p></li>
<li><p><strong>parameters</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A map of Key-Value pairs.</p></li>
<li><p><strong>resource_group_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Resource Group in which the Logic App Workflow should be created. Changing this forces a new resource to be created.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping of tags to assign to the resource.</p></li>
<li><p><strong>workflow_endpoint_ip_addresses</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The list of access endpoint ip addresses of workflow.</p></li>
<li><p><strong>workflow_outbound_ip_addresses</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The list of outgoing ip addresses of workflow.</p></li>
<li><p><strong>workflow_schema</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the Schema to use for this Logic App Workflow. Defaults to <code class="docutils literal notranslate"><span class="pre">https://schema.management.azure.com/providers/Microsoft.Logic/schemas/2016-06-01/workflowdefinition.json#</span></code>. Changing this forces a new resource to be created.</p></li>
<li><p><strong>workflow_version</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the version of the Schema used for this Logic App Workflow. Defaults to <code class="docutils literal notranslate"><span class="pre">1.0.0.0</span></code>. Changing this forces a new resource to be created.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azure.logicapps.Workflow.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.logicapps.Workflow.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.logicapps.Workflow.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.logicapps.Workflow.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azure.logicapps.get_integration_account">
<code class="sig-prename descclassname">pulumi_azure.logicapps.</code><code class="sig-name descname">get_integration_account</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.logicapps.get_integration_account" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing Logic App Integration Account.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_azure</span> <span class="k">as</span> <span class="nn">azure</span>

<span class="n">example</span> <span class="o">=</span> <span class="n">azure</span><span class="o">.</span><span class="n">logicapps</span><span class="o">.</span><span class="n">get_integration_account</span><span class="p">(</span><span class="n">name</span><span class="o">=</span><span class="s2">&quot;example-account&quot;</span><span class="p">,</span>
    <span class="n">resource_group_name</span><span class="o">=</span><span class="s2">&quot;example-resource-group&quot;</span><span class="p">)</span>
<span class="n">pulumi</span><span class="o">.</span><span class="n">export</span><span class="p">(</span><span class="s2">&quot;id&quot;</span><span class="p">,</span> <span class="n">example</span><span class="o">.</span><span class="n">id</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>name</strong> (<em>str</em>) – The name of this Logic App Integration Account.</p></li>
<li><p><strong>resource_group_name</strong> (<em>str</em>) – The name of the Resource Group where the Logic App Integration Account exists.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_azure.logicapps.get_workflow">
<code class="sig-prename descclassname">pulumi_azure.logicapps.</code><code class="sig-name descname">get_workflow</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azure.logicapps.get_workflow" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing Logic App Workflow.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_azure</span> <span class="k">as</span> <span class="nn">azure</span>

<span class="n">example</span> <span class="o">=</span> <span class="n">azure</span><span class="o">.</span><span class="n">logicapps</span><span class="o">.</span><span class="n">get_workflow</span><span class="p">(</span><span class="n">name</span><span class="o">=</span><span class="s2">&quot;workflow1&quot;</span><span class="p">,</span>
    <span class="n">resource_group_name</span><span class="o">=</span><span class="s2">&quot;my-resource-group&quot;</span><span class="p">)</span>
<span class="n">pulumi</span><span class="o">.</span><span class="n">export</span><span class="p">(</span><span class="s2">&quot;accessEndpoint&quot;</span><span class="p">,</span> <span class="n">example</span><span class="o">.</span><span class="n">access_endpoint</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>name</strong> (<em>str</em>) – The name of the Logic App Workflow.</p></li>
<li><p><strong>resource_group_name</strong> (<em>str</em>) – The name of the Resource Group in which the Logic App Workflow exists.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

</div>
