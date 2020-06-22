---
title: Module pipeline
title_tag: Module pipeline | Package pulumi_azuredevops | Python SDK
linktitle: pipeline
notitle: true
block_external_search_index: true
---

{{< resource-docs-alert "azuredevops" >}}

<div class="section" id="pipeline">
<h1>pipeline<a class="headerlink" href="#pipeline" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azuredevops">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-azuredevops/issues">pulumi/pulumi-azuredevops repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azuredevops/issues">terraform-providers/terraform-provider-azuredevops repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_azuredevops.pipeline"></span><dl class="py class">
<dt id="pulumi_azuredevops.pipeline.VariableGroup">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azuredevops.pipeline.</code><code class="sig-name descname">VariableGroup</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">allow_access</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">key_vault</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">variables</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuredevops.pipeline.VariableGroup" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages variable groups within Azure DevOps.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_azuredevops</span> <span class="k">as</span> <span class="nn">azuredevops</span>

<span class="n">project</span> <span class="o">=</span> <span class="n">azuredevops</span><span class="o">.</span><span class="n">core</span><span class="o">.</span><span class="n">Project</span><span class="p">(</span><span class="s2">&quot;project&quot;</span><span class="p">,</span> <span class="n">project_name</span><span class="o">=</span><span class="s2">&quot;Test Project&quot;</span><span class="p">)</span>
<span class="n">variablegroup</span> <span class="o">=</span> <span class="n">azuredevops</span><span class="o">.</span><span class="n">pipeline</span><span class="o">.</span><span class="n">VariableGroup</span><span class="p">(</span><span class="s2">&quot;variablegroup&quot;</span><span class="p">,</span>
    <span class="n">project_id</span><span class="o">=</span><span class="n">project</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">description</span><span class="o">=</span><span class="s2">&quot;Test Variable Group Description&quot;</span><span class="p">,</span>
    <span class="n">allow_access</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="n">variable</span><span class="o">=</span><span class="p">[</span>
        <span class="p">{</span>
            <span class="s2">&quot;name&quot;</span><span class="p">:</span> <span class="s2">&quot;key&quot;</span><span class="p">,</span>
            <span class="s2">&quot;value&quot;</span><span class="p">:</span> <span class="s2">&quot;value&quot;</span><span class="p">,</span>
        <span class="p">},</span>
        <span class="p">{</span>
            <span class="s2">&quot;name&quot;</span><span class="p">:</span> <span class="s2">&quot;Account Password&quot;</span><span class="p">,</span>
            <span class="s2">&quot;value&quot;</span><span class="p">:</span> <span class="s2">&quot;p@ssword123&quot;</span><span class="p">,</span>
            <span class="s2">&quot;isSecret&quot;</span><span class="p">:</span> <span class="kc">True</span><span class="p">,</span>
        <span class="p">},</span>
    <span class="p">])</span>
</pre></div>
</div>
<ul class="simple">
<li><p><a class="reference external" href="https://docs.microsoft.com/en-us/rest/api/azure/devops/distributedtask/variablegroups?view=azure-devops-rest-5.1">Azure DevOps Service REST API 5.1 - Variable Groups</a></p></li>
<li><p><a class="reference external" href="https://docs.microsoft.com/en-us/rest/api/azure/devops/build/authorizedresources?view=azure-devops-rest-5.1">Azure DevOps Service REST API 5.1 - Authorized Resources</a></p></li>
</ul>
<ul class="simple">
<li><p><strong>Variable Groups</strong>: Read, Create, &amp; Manage</p></li>
</ul>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>allow_access</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean that indicate if this variable group is shared by all pipelines of this project.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the Variable Group.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Variable Group.</p></li>
<li><p><strong>project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The project ID or project name.</p></li>
<li><p><strong>variables</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">variable</span></code> blocks as documented below.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>key_vault</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the Variable Group.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">serviceEndpointId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>variables</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">contentType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">expires</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">isSecret</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - A boolean flag describing if the variable value is sensitive. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The key value used for the variable. Must be unique within the Variable Group.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">secretValue</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The secret value of the variable. If omitted, it will default to empty string. Used when <code class="docutils literal notranslate"><span class="pre">is_secret</span></code> set to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The value of the variable. If omitted, it will default to empty string.</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_azuredevops.pipeline.VariableGroup.allow_access">
<code class="sig-name descname">allow_access</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuredevops.pipeline.VariableGroup.allow_access" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean that indicate if this variable group is shared by all pipelines of this project.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azuredevops.pipeline.VariableGroup.description">
<code class="sig-name descname">description</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuredevops.pipeline.VariableGroup.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description of the Variable Group.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azuredevops.pipeline.VariableGroup.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuredevops.pipeline.VariableGroup.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Variable Group.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azuredevops.pipeline.VariableGroup.project_id">
<code class="sig-name descname">project_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuredevops.pipeline.VariableGroup.project_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The project ID or project name.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azuredevops.pipeline.VariableGroup.variables">
<code class="sig-name descname">variables</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuredevops.pipeline.VariableGroup.variables" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more <code class="docutils literal notranslate"><span class="pre">variable</span></code> blocks as documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">contentType</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">expires</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">isSecret</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - A boolean flag describing if the variable value is sensitive. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The key value used for the variable. Must be unique within the Variable Group.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">secretValue</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The secret value of the variable. If omitted, it will default to empty string. Used when <code class="docutils literal notranslate"><span class="pre">is_secret</span></code> set to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The value of the variable. If omitted, it will default to empty string.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.pipeline.VariableGroup.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">allow_access</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">key_vault</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">variables</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuredevops.pipeline.VariableGroup.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing VariableGroup resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>allow_access</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean that indicate if this variable group is shared by all pipelines of this project.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the Variable Group.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Variable Group.</p></li>
<li><p><strong>project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The project ID or project name.</p></li>
<li><p><strong>variables</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">variable</span></code> blocks as documented below.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>key_vault</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the Variable Group.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">serviceEndpointId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>variables</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">contentType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">expires</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">isSecret</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - A boolean flag describing if the variable value is sensitive. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The key value used for the variable. Must be unique within the Variable Group.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">secretValue</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The secret value of the variable. If omitted, it will default to empty string. Used when <code class="docutils literal notranslate"><span class="pre">is_secret</span></code> set to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The value of the variable. If omitted, it will default to empty string.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.pipeline.VariableGroup.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuredevops.pipeline.VariableGroup.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azuredevops.pipeline.VariableGroup.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuredevops.pipeline.VariableGroup.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
