---
title: Module repository
title_tag: Module repository | Package pulumi_azuredevops | Python SDK
linktitle: repository
notitle: true
block_external_search_index: true
---

{{< resource-docs-alert "azuredevops" >}}

<div class="section" id="repository">
<h1>repository<a class="headerlink" href="#repository" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azuredevops">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-azuredevops/issues">pulumi/pulumi-azuredevops repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azuredevops/issues">terraform-providers/terraform-provider-azuredevops repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_azuredevops.repository"></span><dl class="py class">
<dt id="pulumi_azuredevops.repository.AwaitableGetRepositoriesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azuredevops.repository.</code><code class="sig-name descname">AwaitableGetRepositoriesResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">include_hidden</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">repositories</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuredevops.repository.AwaitableGetRepositoriesResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_azuredevops.repository.GetRepositoriesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azuredevops.repository.</code><code class="sig-name descname">GetRepositoriesResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">include_hidden</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">repositories</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuredevops.repository.GetRepositoriesResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getRepositories.</p>
<dl class="py attribute">
<dt id="pulumi_azuredevops.repository.GetRepositoriesResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuredevops.repository.GetRepositoriesResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_azuredevops.repository.Git">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azuredevops.repository.</code><code class="sig-name descname">Git</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">default_branch</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">initialization</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">parent_repository_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuredevops.repository.Git" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a git repository within Azure DevOps.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_azuredevops</span> <span class="k">as</span> <span class="nn">azuredevops</span>

<span class="n">project</span> <span class="o">=</span> <span class="n">azuredevops</span><span class="o">.</span><span class="n">core</span><span class="o">.</span><span class="n">Project</span><span class="p">(</span><span class="s2">&quot;project&quot;</span><span class="p">,</span>
    <span class="n">project_name</span><span class="o">=</span><span class="s2">&quot;Sample Project&quot;</span><span class="p">,</span>
    <span class="n">visibility</span><span class="o">=</span><span class="s2">&quot;private&quot;</span><span class="p">,</span>
    <span class="n">version_control</span><span class="o">=</span><span class="s2">&quot;Git&quot;</span><span class="p">,</span>
    <span class="n">work_item_template</span><span class="o">=</span><span class="s2">&quot;Agile&quot;</span><span class="p">)</span>
<span class="n">repo</span> <span class="o">=</span> <span class="n">azuredevops</span><span class="o">.</span><span class="n">repository</span><span class="o">.</span><span class="n">Git</span><span class="p">(</span><span class="s2">&quot;repo&quot;</span><span class="p">,</span>
    <span class="n">project_id</span><span class="o">=</span><span class="n">project</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">initialization</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;initType&quot;</span><span class="p">:</span> <span class="s2">&quot;Clean&quot;</span><span class="p">,</span>
    <span class="p">})</span>
</pre></div>
</div>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_azuredevops</span> <span class="k">as</span> <span class="nn">azuredevops</span>

<span class="n">repo</span> <span class="o">=</span> <span class="n">azuredevops</span><span class="o">.</span><span class="n">repository</span><span class="o">.</span><span class="n">Git</span><span class="p">(</span><span class="s2">&quot;repo&quot;</span><span class="p">,</span>
    <span class="n">project_id</span><span class="o">=</span><span class="n">azuredevops_project</span><span class="p">[</span><span class="s2">&quot;project&quot;</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">],</span>
    <span class="n">parent_id</span><span class="o">=</span><span class="n">azuredevops_git_repository</span><span class="p">[</span><span class="s2">&quot;parent&quot;</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">])</span>
</pre></div>
</div>
<ul class="simple">
<li><p><a class="reference external" href="https://docs.microsoft.com/en-us/rest/api/azure/devops/git/repositories?view=azure-devops-rest-5.1">Azure DevOps Service REST API 5.1 - Agent Pools</a></p></li>
</ul>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>default_branch</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ref of the default branch.</p></li>
<li><p><strong>initialization</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – An <code class="docutils literal notranslate"><span class="pre">initialization</span></code> block as documented below.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the git repository.</p></li>
<li><p><strong>project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The project ID or project name.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>initialization</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">initType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The type of repository to create. Valid values: <code class="docutils literal notranslate"><span class="pre">Uninitialized</span></code>, <code class="docutils literal notranslate"><span class="pre">Clean</span></code>, or <code class="docutils literal notranslate"><span class="pre">Import</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">Uninitialized</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sourceType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Type type of the source repository. Used if the <code class="docutils literal notranslate"><span class="pre">init_type</span></code> is <code class="docutils literal notranslate"><span class="pre">Import</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sourceUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The URL of the source repository. Used if the <code class="docutils literal notranslate"><span class="pre">init_type</span></code> is <code class="docutils literal notranslate"><span class="pre">Import</span></code>.</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_azuredevops.repository.Git.default_branch">
<code class="sig-name descname">default_branch</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuredevops.repository.Git.default_branch" title="Permalink to this definition">¶</a></dt>
<dd><p>The ref of the default branch.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azuredevops.repository.Git.initialization">
<code class="sig-name descname">initialization</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuredevops.repository.Git.initialization" title="Permalink to this definition">¶</a></dt>
<dd><p>An <code class="docutils literal notranslate"><span class="pre">initialization</span></code> block as documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">initType</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The type of repository to create. Valid values: <code class="docutils literal notranslate"><span class="pre">Uninitialized</span></code>, <code class="docutils literal notranslate"><span class="pre">Clean</span></code>, or <code class="docutils literal notranslate"><span class="pre">Import</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">Uninitialized</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sourceType</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - Type type of the source repository. Used if the <code class="docutils literal notranslate"><span class="pre">init_type</span></code> is <code class="docutils literal notranslate"><span class="pre">Import</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sourceUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The URL of the source repository. Used if the <code class="docutils literal notranslate"><span class="pre">init_type</span></code> is <code class="docutils literal notranslate"><span class="pre">Import</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azuredevops.repository.Git.is_fork">
<code class="sig-name descname">is_fork</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuredevops.repository.Git.is_fork" title="Permalink to this definition">¶</a></dt>
<dd><p>True if the repository was created as a fork.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azuredevops.repository.Git.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuredevops.repository.Git.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the git repository.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azuredevops.repository.Git.project_id">
<code class="sig-name descname">project_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuredevops.repository.Git.project_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The project ID or project name.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azuredevops.repository.Git.remote_url">
<code class="sig-name descname">remote_url</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuredevops.repository.Git.remote_url" title="Permalink to this definition">¶</a></dt>
<dd><p>Git HTTPS URL of the repository</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azuredevops.repository.Git.size">
<code class="sig-name descname">size</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuredevops.repository.Git.size" title="Permalink to this definition">¶</a></dt>
<dd><p>Size in bytes.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azuredevops.repository.Git.ssh_url">
<code class="sig-name descname">ssh_url</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuredevops.repository.Git.ssh_url" title="Permalink to this definition">¶</a></dt>
<dd><p>Git SSH URL of the repository.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azuredevops.repository.Git.url">
<code class="sig-name descname">url</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuredevops.repository.Git.url" title="Permalink to this definition">¶</a></dt>
<dd><p>REST API URL of the repository.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azuredevops.repository.Git.web_url">
<code class="sig-name descname">web_url</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuredevops.repository.Git.web_url" title="Permalink to this definition">¶</a></dt>
<dd><p>Web link to the repository.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.repository.Git.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">default_branch</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">initialization</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">is_fork</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">parent_repository_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">remote_url</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">size</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ssh_url</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">url</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">web_url</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuredevops.repository.Git.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Git resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>default_branch</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ref of the default branch.</p></li>
<li><p><strong>initialization</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – An <code class="docutils literal notranslate"><span class="pre">initialization</span></code> block as documented below.</p></li>
<li><p><strong>is_fork</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – True if the repository was created as a fork.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the git repository.</p></li>
<li><p><strong>project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The project ID or project name.</p></li>
<li><p><strong>remote_url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Git HTTPS URL of the repository</p></li>
<li><p><strong>size</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Size in bytes.</p></li>
<li><p><strong>ssh_url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Git SSH URL of the repository.</p></li>
<li><p><strong>url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – REST API URL of the repository.</p></li>
<li><p><strong>web_url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Web link to the repository.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>initialization</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">initType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The type of repository to create. Valid values: <code class="docutils literal notranslate"><span class="pre">Uninitialized</span></code>, <code class="docutils literal notranslate"><span class="pre">Clean</span></code>, or <code class="docutils literal notranslate"><span class="pre">Import</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">Uninitialized</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sourceType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - Type type of the source repository. Used if the <code class="docutils literal notranslate"><span class="pre">init_type</span></code> is <code class="docutils literal notranslate"><span class="pre">Import</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">sourceUrl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The URL of the source repository. Used if the <code class="docutils literal notranslate"><span class="pre">init_type</span></code> is <code class="docutils literal notranslate"><span class="pre">Import</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.repository.Git.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuredevops.repository.Git.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azuredevops.repository.Git.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuredevops.repository.Git.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azuredevops.repository.get_repositories">
<code class="sig-prename descclassname">pulumi_azuredevops.repository.</code><code class="sig-name descname">get_repositories</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">include_hidden</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuredevops.repository.get_repositories" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing Git Repositories within Azure DevOps.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_azuredevops</span> <span class="k">as</span> <span class="nn">azuredevops</span>

<span class="n">project</span> <span class="o">=</span> <span class="n">azuredevops</span><span class="o">.</span><span class="n">Core</span><span class="o">.</span><span class="n">get_project</span><span class="p">(</span><span class="n">project_name</span><span class="o">=</span><span class="s2">&quot;contoso-project&quot;</span><span class="p">)</span>
<span class="n">all_repos</span> <span class="o">=</span> <span class="n">azuredevops</span><span class="o">.</span><span class="n">Repository</span><span class="o">.</span><span class="n">get_repositories</span><span class="p">(</span><span class="n">project_id</span><span class="o">=</span><span class="n">project</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">include_hidden</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
<span class="n">single_repo</span> <span class="o">=</span> <span class="n">azuredevops</span><span class="o">.</span><span class="n">Repository</span><span class="o">.</span><span class="n">get_repositories</span><span class="p">(</span><span class="n">project_id</span><span class="o">=</span><span class="n">project</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">name</span><span class="o">=</span><span class="s2">&quot;contoso-repo&quot;</span><span class="p">)</span>
</pre></div>
</div>
<ul class="simple">
<li><p><a class="reference external" href="https://docs.microsoft.com/en-us/rest/api/azure/devops/git/?view=azure-devops-rest-5.1">Azure DevOps Service REST API 5.1 - Git API</a></p></li>
</ul>
</dd></dl>

</div>
