---
title: Module core
title_tag: Module core | Package pulumi_azuredevops | Python SDK
linktitle: core
notitle: true
block_external_search_index: true
---

{{< resource-docs-alert "azuredevops" >}}

<div class="section" id="core">
<h1>core<a class="headerlink" href="#core" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azuredevops">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-azuredevops/issues">pulumi/pulumi-azuredevops repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azuredevops/issues">terraform-providers/terraform-provider-azuredevops repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_azuredevops.core"></span><dl class="py class">
<dt id="pulumi_azuredevops.core.AwaitableGetClientConfigResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azuredevops.core.</code><code class="sig-name descname">AwaitableGetClientConfigResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">organization_url</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuredevops.core.AwaitableGetClientConfigResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_azuredevops.core.AwaitableGetProjectResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azuredevops.core.</code><code class="sig-name descname">AwaitableGetProjectResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">features</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">process_template_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">version_control</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">visibility</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">work_item_template</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuredevops.core.AwaitableGetProjectResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_azuredevops.core.AwaitableGetProjectsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azuredevops.core.</code><code class="sig-name descname">AwaitableGetProjectsResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">projects</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">state</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuredevops.core.AwaitableGetProjectsResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_azuredevops.core.GetClientConfigResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azuredevops.core.</code><code class="sig-name descname">GetClientConfigResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">organization_url</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuredevops.core.GetClientConfigResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getClientConfig.</p>
<dl class="py attribute">
<dt id="pulumi_azuredevops.core.GetClientConfigResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuredevops.core.GetClientConfigResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_azuredevops.core.GetProjectResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azuredevops.core.</code><code class="sig-name descname">GetProjectResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">features</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">process_template_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">version_control</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">visibility</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">work_item_template</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuredevops.core.GetProjectResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getProject.</p>
<dl class="py attribute">
<dt id="pulumi_azuredevops.core.GetProjectResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuredevops.core.GetProjectResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_azuredevops.core.GetProjectsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azuredevops.core.</code><code class="sig-name descname">GetProjectsResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">projects</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">state</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuredevops.core.GetProjectsResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getProjects.</p>
<dl class="py attribute">
<dt id="pulumi_azuredevops.core.GetProjectsResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuredevops.core.GetProjectsResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_azuredevops.core.Project">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azuredevops.core.</code><code class="sig-name descname">Project</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">features</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">version_control</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">visibility</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">work_item_template</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuredevops.core.Project" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a project within Azure DevOps.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_azuredevops</span> <span class="k">as</span> <span class="nn">azuredevops</span>

<span class="n">project</span> <span class="o">=</span> <span class="n">azuredevops</span><span class="o">.</span><span class="n">core</span><span class="o">.</span><span class="n">Project</span><span class="p">(</span><span class="s2">&quot;project&quot;</span><span class="p">,</span>
    <span class="n">description</span><span class="o">=</span><span class="s2">&quot;Test Project Description&quot;</span><span class="p">,</span>
    <span class="n">features</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;artifacts&quot;</span><span class="p">:</span> <span class="s2">&quot;disabled&quot;</span><span class="p">,</span>
        <span class="s2">&quot;testplans&quot;</span><span class="p">:</span> <span class="s2">&quot;disabled&quot;</span><span class="p">,</span>
    <span class="p">},</span>
    <span class="n">project_name</span><span class="o">=</span><span class="s2">&quot;Test Project&quot;</span><span class="p">,</span>
    <span class="n">version_control</span><span class="o">=</span><span class="s2">&quot;Git&quot;</span><span class="p">,</span>
    <span class="n">visibility</span><span class="o">=</span><span class="s2">&quot;private&quot;</span><span class="p">,</span>
    <span class="n">work_item_template</span><span class="o">=</span><span class="s2">&quot;Agile&quot;</span><span class="p">)</span>
</pre></div>
</div>
<ul class="simple">
<li><p><a class="reference external" href="https://docs.microsoft.com/en-us/rest/api/azure/devops/core/projects?view=azure-devops-rest-5.1">Azure DevOps Service REST API 5.1 - Projects</a></p></li>
</ul>
<ul class="simple">
<li><p><strong>Project &amp; Team</strong>: Read, Write, &amp; Manage</p></li>
</ul>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Description of the Project.</p></li>
<li><p><strong>features</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Defines the status (<code class="docutils literal notranslate"><span class="pre">enabled</span></code>, <code class="docutils literal notranslate"><span class="pre">disabled</span></code>) of the project features.<span class="raw-html-m2r"><br></span>
Valid features <code class="docutils literal notranslate"><span class="pre">boards</span></code>, <code class="docutils literal notranslate"><span class="pre">repositories</span></code>, <code class="docutils literal notranslate"><span class="pre">pipelines</span></code>, <code class="docutils literal notranslate"><span class="pre">testplans</span></code>, <code class="docutils literal notranslate"><span class="pre">artifacts</span></code></p></li>
<li><p><strong>project_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Project Name.</p></li>
<li><p><strong>version_control</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the version control system. Valid values: <code class="docutils literal notranslate"><span class="pre">Git</span></code> or <code class="docutils literal notranslate"><span class="pre">Tfvc</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">Git</span></code>.</p></li>
<li><p><strong>visibility</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the visibility of the Project. Valid values: <code class="docutils literal notranslate"><span class="pre">private</span></code> or <code class="docutils literal notranslate"><span class="pre">public</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">private</span></code>.</p></li>
<li><p><strong>work_item_template</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the work item template. Defaults to <code class="docutils literal notranslate"><span class="pre">Agile</span></code>.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_azuredevops.core.Project.description">
<code class="sig-name descname">description</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuredevops.core.Project.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The Description of the Project.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azuredevops.core.Project.features">
<code class="sig-name descname">features</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuredevops.core.Project.features" title="Permalink to this definition">¶</a></dt>
<dd><p>Defines the status (<code class="docutils literal notranslate"><span class="pre">enabled</span></code>, <code class="docutils literal notranslate"><span class="pre">disabled</span></code>) of the project features.<span class="raw-html-m2r"><br></span>
Valid features <code class="docutils literal notranslate"><span class="pre">boards</span></code>, <code class="docutils literal notranslate"><span class="pre">repositories</span></code>, <code class="docutils literal notranslate"><span class="pre">pipelines</span></code>, <code class="docutils literal notranslate"><span class="pre">testplans</span></code>, <code class="docutils literal notranslate"><span class="pre">artifacts</span></code></p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azuredevops.core.Project.process_template_id">
<code class="sig-name descname">process_template_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuredevops.core.Project.process_template_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The Process Template ID used by the Project.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azuredevops.core.Project.project_name">
<code class="sig-name descname">project_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuredevops.core.Project.project_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The Project Name.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azuredevops.core.Project.version_control">
<code class="sig-name descname">version_control</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuredevops.core.Project.version_control" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the version control system. Valid values: <code class="docutils literal notranslate"><span class="pre">Git</span></code> or <code class="docutils literal notranslate"><span class="pre">Tfvc</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">Git</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azuredevops.core.Project.visibility">
<code class="sig-name descname">visibility</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuredevops.core.Project.visibility" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the visibility of the Project. Valid values: <code class="docutils literal notranslate"><span class="pre">private</span></code> or <code class="docutils literal notranslate"><span class="pre">public</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">private</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azuredevops.core.Project.work_item_template">
<code class="sig-name descname">work_item_template</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuredevops.core.Project.work_item_template" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the work item template. Defaults to <code class="docutils literal notranslate"><span class="pre">Agile</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.core.Project.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">features</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">process_template_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">version_control</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">visibility</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">work_item_template</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuredevops.core.Project.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Project resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Description of the Project.</p></li>
<li><p><strong>features</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Defines the status (<code class="docutils literal notranslate"><span class="pre">enabled</span></code>, <code class="docutils literal notranslate"><span class="pre">disabled</span></code>) of the project features.<span class="raw-html-m2r"><br></span>
Valid features <code class="docutils literal notranslate"><span class="pre">boards</span></code>, <code class="docutils literal notranslate"><span class="pre">repositories</span></code>, <code class="docutils literal notranslate"><span class="pre">pipelines</span></code>, <code class="docutils literal notranslate"><span class="pre">testplans</span></code>, <code class="docutils literal notranslate"><span class="pre">artifacts</span></code></p></li>
<li><p><strong>process_template_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Process Template ID used by the Project.</p></li>
<li><p><strong>project_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Project Name.</p></li>
<li><p><strong>version_control</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the version control system. Valid values: <code class="docutils literal notranslate"><span class="pre">Git</span></code> or <code class="docutils literal notranslate"><span class="pre">Tfvc</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">Git</span></code>.</p></li>
<li><p><strong>visibility</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the visibility of the Project. Valid values: <code class="docutils literal notranslate"><span class="pre">private</span></code> or <code class="docutils literal notranslate"><span class="pre">public</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">private</span></code>.</p></li>
<li><p><strong>work_item_template</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the work item template. Defaults to <code class="docutils literal notranslate"><span class="pre">Agile</span></code>.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.core.Project.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuredevops.core.Project.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azuredevops.core.Project.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuredevops.core.Project.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azuredevops.core.ProjectFeatures">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azuredevops.core.</code><code class="sig-name descname">ProjectFeatures</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">features</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuredevops.core.ProjectFeatures" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages features for Azure DevOps projects</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_azuredevops</span> <span class="k">as</span> <span class="nn">azuredevops</span>

<span class="n">tf_project_test_001</span> <span class="o">=</span> <span class="n">azuredevops</span><span class="o">.</span><span class="n">Core</span><span class="o">.</span><span class="n">get_project</span><span class="p">(</span><span class="n">project_name</span><span class="o">=</span><span class="s2">&quot;Test Project&quot;</span><span class="p">)</span>
<span class="n">my_project_features</span> <span class="o">=</span> <span class="n">azuredevops</span><span class="o">.</span><span class="n">core</span><span class="o">.</span><span class="n">ProjectFeatures</span><span class="p">(</span><span class="s2">&quot;my-project-features&quot;</span><span class="p">,</span>
    <span class="n">project_id</span><span class="o">=</span><span class="n">tf_project_test_001</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">features</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;testplans&quot;</span><span class="p">:</span> <span class="s2">&quot;disabled&quot;</span><span class="p">,</span>
        <span class="s2">&quot;artifacts&quot;</span><span class="p">:</span> <span class="s2">&quot;enabled&quot;</span><span class="p">,</span>
    <span class="p">})</span>
</pre></div>
</div>
<p>No official documentation available</p>
<ul class="simple">
<li><p><strong>Project &amp; Team</strong>: Read, Write, &amp; Manage</p></li>
</ul>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>features</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Defines the status (<code class="docutils literal notranslate"><span class="pre">enabled</span></code>, <code class="docutils literal notranslate"><span class="pre">disabled</span></code>) of the project features.<span class="raw-html-m2r"><br></span>
Valid features <code class="docutils literal notranslate"><span class="pre">boards</span></code>, <code class="docutils literal notranslate"><span class="pre">repositories</span></code>, <code class="docutils literal notranslate"><span class="pre">pipelines</span></code>, <code class="docutils literal notranslate"><span class="pre">testplans</span></code>, <code class="docutils literal notranslate"><span class="pre">artifacts</span></code></p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_azuredevops.core.ProjectFeatures.features">
<code class="sig-name descname">features</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuredevops.core.ProjectFeatures.features" title="Permalink to this definition">¶</a></dt>
<dd><p>Defines the status (<code class="docutils literal notranslate"><span class="pre">enabled</span></code>, <code class="docutils literal notranslate"><span class="pre">disabled</span></code>) of the project features.<span class="raw-html-m2r"><br></span>
Valid features <code class="docutils literal notranslate"><span class="pre">boards</span></code>, <code class="docutils literal notranslate"><span class="pre">repositories</span></code>, <code class="docutils literal notranslate"><span class="pre">pipelines</span></code>, <code class="docutils literal notranslate"><span class="pre">testplans</span></code>, <code class="docutils literal notranslate"><span class="pre">artifacts</span></code></p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.core.ProjectFeatures.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">features</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuredevops.core.ProjectFeatures.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ProjectFeatures resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>features</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Defines the status (<code class="docutils literal notranslate"><span class="pre">enabled</span></code>, <code class="docutils literal notranslate"><span class="pre">disabled</span></code>) of the project features.<span class="raw-html-m2r"><br></span>
Valid features <code class="docutils literal notranslate"><span class="pre">boards</span></code>, <code class="docutils literal notranslate"><span class="pre">repositories</span></code>, <code class="docutils literal notranslate"><span class="pre">pipelines</span></code>, <code class="docutils literal notranslate"><span class="pre">testplans</span></code>, <code class="docutils literal notranslate"><span class="pre">artifacts</span></code></p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.core.ProjectFeatures.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuredevops.core.ProjectFeatures.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azuredevops.core.ProjectFeatures.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuredevops.core.ProjectFeatures.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azuredevops.core.get_client_config">
<code class="sig-prename descclassname">pulumi_azuredevops.core.</code><code class="sig-name descname">get_client_config</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuredevops.core.get_client_config" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about the Azure DevOps organization configured for the provider.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_azuredevops</span> <span class="k">as</span> <span class="nn">azuredevops</span>

<span class="n">client_config</span> <span class="o">=</span> <span class="n">azuredevops</span><span class="o">.</span><span class="n">Core</span><span class="o">.</span><span class="n">get_client_config</span><span class="p">()</span>
<span class="n">pulumi</span><span class="o">.</span><span class="n">export</span><span class="p">(</span><span class="s2">&quot;orgUrl&quot;</span><span class="p">,</span> <span class="n">client_config</span><span class="o">.</span><span class="n">organization_url</span><span class="p">)</span>
</pre></div>
</div>
</dd></dl>

<dl class="py function">
<dt id="pulumi_azuredevops.core.get_project">
<code class="sig-prename descclassname">pulumi_azuredevops.core.</code><code class="sig-name descname">get_project</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">project_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuredevops.core.get_project" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing Project within Azure DevOps.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_azuredevops</span> <span class="k">as</span> <span class="nn">azuredevops</span>

<span class="n">project</span> <span class="o">=</span> <span class="n">azuredevops</span><span class="o">.</span><span class="n">Core</span><span class="o">.</span><span class="n">get_project</span><span class="p">(</span><span class="n">project_name</span><span class="o">=</span><span class="s2">&quot;Sample Project&quot;</span><span class="p">)</span>
<span class="n">pulumi</span><span class="o">.</span><span class="n">export</span><span class="p">(</span><span class="s2">&quot;id&quot;</span><span class="p">,</span> <span class="n">project</span><span class="o">.</span><span class="n">id</span><span class="p">)</span>
<span class="n">pulumi</span><span class="o">.</span><span class="n">export</span><span class="p">(</span><span class="s2">&quot;projectName&quot;</span><span class="p">,</span> <span class="n">project</span><span class="o">.</span><span class="n">project_name</span><span class="p">)</span>
<span class="n">pulumi</span><span class="o">.</span><span class="n">export</span><span class="p">(</span><span class="s2">&quot;visibility&quot;</span><span class="p">,</span> <span class="n">project</span><span class="o">.</span><span class="n">visibility</span><span class="p">)</span>
<span class="n">pulumi</span><span class="o">.</span><span class="n">export</span><span class="p">(</span><span class="s2">&quot;versionControl&quot;</span><span class="p">,</span> <span class="n">project</span><span class="o">.</span><span class="n">version_control</span><span class="p">)</span>
<span class="n">pulumi</span><span class="o">.</span><span class="n">export</span><span class="p">(</span><span class="s2">&quot;workItemTemplate&quot;</span><span class="p">,</span> <span class="n">project</span><span class="o">.</span><span class="n">work_item_template</span><span class="p">)</span>
<span class="n">pulumi</span><span class="o">.</span><span class="n">export</span><span class="p">(</span><span class="s2">&quot;processTemplateId&quot;</span><span class="p">,</span> <span class="n">project</span><span class="o">.</span><span class="n">process_template_id</span><span class="p">)</span>
</pre></div>
</div>
<ul class="simple">
<li><p><a class="reference external" href="https://docs.microsoft.com/en-us/rest/api/azure/devops/core/projects/get?view=azure-devops-rest-5.1">Azure DevOps Service REST API 5.1 - Projects - Get</a></p></li>
</ul>
</dd></dl>

<dl class="py function">
<dt id="pulumi_azuredevops.core.get_projects">
<code class="sig-prename descclassname">pulumi_azuredevops.core.</code><code class="sig-name descname">get_projects</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">project_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">state</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuredevops.core.get_projects" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about existing Projects within Azure DevOps.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_azuredevops</span> <span class="k">as</span> <span class="nn">azuredevops</span>

<span class="n">test</span> <span class="o">=</span> <span class="n">azuredevops</span><span class="o">.</span><span class="n">Core</span><span class="o">.</span><span class="n">get_projects</span><span class="p">(</span><span class="n">project_name</span><span class="o">=</span><span class="s2">&quot;contoso&quot;</span><span class="p">,</span>
    <span class="n">state</span><span class="o">=</span><span class="s2">&quot;wellFormed&quot;</span><span class="p">)</span>
<span class="n">pulumi</span><span class="o">.</span><span class="n">export</span><span class="p">(</span><span class="s2">&quot;projectId&quot;</span><span class="p">,</span> <span class="p">[</span><span class="n">__item</span><span class="p">[</span><span class="s2">&quot;project_id&quot;</span><span class="p">]</span> <span class="k">for</span> <span class="n">__item</span> <span class="ow">in</span> <span class="n">test</span><span class="o">.</span><span class="n">projects</span><span class="p">])</span>
<span class="n">pulumi</span><span class="o">.</span><span class="n">export</span><span class="p">(</span><span class="s2">&quot;projectName&quot;</span><span class="p">,</span> <span class="p">[</span><span class="n">__item</span><span class="p">[</span><span class="s2">&quot;name&quot;</span><span class="p">]</span> <span class="k">for</span> <span class="n">__item</span> <span class="ow">in</span> <span class="n">test</span><span class="o">.</span><span class="n">projects</span><span class="p">])</span>
<span class="n">pulumi</span><span class="o">.</span><span class="n">export</span><span class="p">(</span><span class="s2">&quot;projectUrl&quot;</span><span class="p">,</span> <span class="p">[</span><span class="n">__item</span><span class="p">[</span><span class="s2">&quot;projectUrl&quot;</span><span class="p">]</span> <span class="k">for</span> <span class="n">__item</span> <span class="ow">in</span> <span class="n">test</span><span class="o">.</span><span class="n">projects</span><span class="p">])</span>
<span class="n">pulumi</span><span class="o">.</span><span class="n">export</span><span class="p">(</span><span class="s2">&quot;state&quot;</span><span class="p">,</span> <span class="p">[</span><span class="n">__item</span><span class="p">[</span><span class="s2">&quot;state&quot;</span><span class="p">]</span> <span class="k">for</span> <span class="n">__item</span> <span class="ow">in</span> <span class="n">test</span><span class="o">.</span><span class="n">projects</span><span class="p">])</span>
</pre></div>
</div>
<ul class="simple">
<li><p><a class="reference external" href="https://docs.microsoft.com/en-us/rest/api/azure/devops/core/projects/get?view=azure-devops-rest-5.1">Azure DevOps Service REST API 5.1 - Projects - Get</a></p></li>
</ul>
</dd></dl>

</div>
