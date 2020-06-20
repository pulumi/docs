---
title: Module build
title_tag: Module build | Package pulumi_azuredevops | Python SDK
linktitle: build
notitle: true
block_external_search_index: true
---

{{< resource-docs-alert "azuredevops" >}}

<div class="section" id="build">
<h1>build<a class="headerlink" href="#build" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azuredevops">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-azuredevops/issues">pulumi/pulumi-azuredevops repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azuredevops/issues">terraform-providers/terraform-provider-azuredevops repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_azuredevops.build"></span><dl class="py class">
<dt id="pulumi_azuredevops.build.BuildDefinition">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azuredevops.build.</code><code class="sig-name descname">BuildDefinition</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">agent_pool_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ci_trigger</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">path</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">pull_request_trigger</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">repository</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">variable_groups</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">variables</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuredevops.build.BuildDefinition" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Build Definition within Azure DevOps.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_azuredevops</span> <span class="k">as</span> <span class="nn">azuredevops</span>

<span class="n">project</span> <span class="o">=</span> <span class="n">azuredevops</span><span class="o">.</span><span class="n">core</span><span class="o">.</span><span class="n">Project</span><span class="p">(</span><span class="s2">&quot;project&quot;</span><span class="p">,</span>
    <span class="n">project_name</span><span class="o">=</span><span class="s2">&quot;Sample Project&quot;</span><span class="p">,</span>
    <span class="n">visibility</span><span class="o">=</span><span class="s2">&quot;private&quot;</span><span class="p">,</span>
    <span class="n">version_control</span><span class="o">=</span><span class="s2">&quot;Git&quot;</span><span class="p">,</span>
    <span class="n">work_item_template</span><span class="o">=</span><span class="s2">&quot;Agile&quot;</span><span class="p">)</span>
<span class="n">repository</span> <span class="o">=</span> <span class="n">azuredevops</span><span class="o">.</span><span class="n">repository</span><span class="o">.</span><span class="n">Git</span><span class="p">(</span><span class="s2">&quot;repository&quot;</span><span class="p">,</span>
    <span class="n">project_id</span><span class="o">=</span><span class="n">project</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">initialization</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;initType&quot;</span><span class="p">:</span> <span class="s2">&quot;Clean&quot;</span><span class="p">,</span>
    <span class="p">})</span>
<span class="nb">vars</span> <span class="o">=</span> <span class="n">azuredevops</span><span class="o">.</span><span class="n">pipeline</span><span class="o">.</span><span class="n">VariableGroup</span><span class="p">(</span><span class="s2">&quot;vars&quot;</span><span class="p">,</span>
    <span class="n">project_id</span><span class="o">=</span><span class="n">project</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">description</span><span class="o">=</span><span class="s2">&quot;Managed by Terraform&quot;</span><span class="p">,</span>
    <span class="n">allow_access</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="n">variable</span><span class="o">=</span><span class="p">[{</span>
        <span class="s2">&quot;name&quot;</span><span class="p">:</span> <span class="s2">&quot;FOO&quot;</span><span class="p">,</span>
        <span class="s2">&quot;value&quot;</span><span class="p">:</span> <span class="s2">&quot;BAR&quot;</span><span class="p">,</span>
    <span class="p">}])</span>
<span class="n">build</span> <span class="o">=</span> <span class="n">azuredevops</span><span class="o">.</span><span class="n">build</span><span class="o">.</span><span class="n">BuildDefinition</span><span class="p">(</span><span class="s2">&quot;build&quot;</span><span class="p">,</span>
    <span class="n">project_id</span><span class="o">=</span><span class="n">project</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">path</span><span class="o">=</span><span class="s2">&quot;\ExampleFolder&quot;</span><span class="p">,</span>
    <span class="n">ci_trigger</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;useYaml&quot;</span><span class="p">:</span> <span class="kc">True</span><span class="p">,</span>
    <span class="p">},</span>
    <span class="n">repository</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;repoType&quot;</span><span class="p">:</span> <span class="s2">&quot;TfsGit&quot;</span><span class="p">,</span>
        <span class="s2">&quot;repoId&quot;</span><span class="p">:</span> <span class="n">repository</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
        <span class="s2">&quot;branchName&quot;</span><span class="p">:</span> <span class="n">repository</span><span class="o">.</span><span class="n">default_branch</span><span class="p">,</span>
        <span class="s2">&quot;ymlPath&quot;</span><span class="p">:</span> <span class="s2">&quot;azure-pipelines.yml&quot;</span><span class="p">,</span>
    <span class="p">},</span>
    <span class="n">variable_groups</span><span class="o">=</span><span class="p">[</span><span class="nb">vars</span><span class="o">.</span><span class="n">id</span><span class="p">],</span>
    <span class="n">variable</span><span class="o">=</span><span class="p">[</span>
        <span class="p">{</span>
            <span class="s2">&quot;name&quot;</span><span class="p">:</span> <span class="s2">&quot;PipelineVariable&quot;</span><span class="p">,</span>
            <span class="s2">&quot;value&quot;</span><span class="p">:</span> <span class="s2">&quot;Go Microsoft!&quot;</span><span class="p">,</span>
        <span class="p">},</span>
        <span class="p">{</span>
            <span class="s2">&quot;name&quot;</span><span class="p">:</span> <span class="s2">&quot;PipelineSecret&quot;</span><span class="p">,</span>
            <span class="s2">&quot;secretValue&quot;</span><span class="p">:</span> <span class="s2">&quot;ZGV2cw&quot;</span><span class="p">,</span>
            <span class="s2">&quot;isSecret&quot;</span><span class="p">:</span> <span class="kc">True</span><span class="p">,</span>
        <span class="p">},</span>
    <span class="p">])</span>
</pre></div>
</div>
<ul class="simple">
<li><p><a class="reference external" href="https://docs.microsoft.com/en-us/rest/api/azure/devops/build/definitions?view=azure-devops-rest-5.1">Azure DevOps Service REST API 5.1 - Build Definitions</a></p></li>
</ul>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>agent_pool_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The agent pool that should execute the build. Defaults to <code class="docutils literal notranslate"><span class="pre">Hosted</span> <span class="pre">Ubuntu</span> <span class="pre">1604</span></code>.</p></li>
<li><p><strong>ci_trigger</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Continuous Integration Integration trigger.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the build definition.</p></li>
<li><p><strong>project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The project ID or project name.</p></li>
<li><p><strong>pull_request_trigger</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Pull Request Integration Integration trigger.</p></li>
<li><p><strong>repository</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">repository</span></code> block as documented below.</p></li>
<li><p><strong>variable_groups</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of variable group IDs (integers) to link to the build definition.</p></li>
<li><p><strong>variables</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of <code class="docutils literal notranslate"><span class="pre">variable</span></code> blocks, as documented below.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>ci_trigger</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">override</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Override the azure-pipeline file and use a this configuration for all builds.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">batch</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - If you set batch to true, when a pipeline is running, the system waits until the run is completed, then starts another run with all changes that have not yet been built. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">branchFilters</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The branches to include and exclude from the trigger.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">excludes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - List of branch patterns to exclude.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">includes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - List of branch patterns to include.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxConcurrentBuildsPerBranch</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of max builds per branch. Defaults to <code class="docutils literal notranslate"><span class="pre">1</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">pathFilters</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Specify file paths to include or exclude. Note that the wildcard syntax is different between branches/tags and file paths.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">excludes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - List of branch patterns to exclude.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">includes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - List of branch patterns to include.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">pollingInterval</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - How often the external repository is polled. Defaults to <code class="docutils literal notranslate"><span class="pre">0</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">pollingJobId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - This is the ID of the polling job that polls the external repository. Once the build definition is saved/updated, this value is set.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">useYaml</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Use the azure-pipeline file for the build configuration. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
</ul>
<p>The <strong>pull_request_trigger</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">commentRequired</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">forks</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Set permissions for Forked repositories.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Build pull requests form forms of this repository.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">shareSecrets</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Make secrets available to builds of forks.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">initialBranch</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">override</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Override the azure-pipeline file and use a this configuration for all builds.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">autoCancel</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - . Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">branchFilters</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The branches to include and exclude from the trigger.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">excludes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - List of branch patterns to exclude.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">includes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - List of branch patterns to include.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">pathFilters</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Specify file paths to include or exclude. Note that the wildcard syntax is different between branches/tags and file paths.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">excludes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - List of branch patterns to exclude.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">includes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - List of branch patterns to include.</p></li>
</ul>
</li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">useYaml</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Use the azure-pipeline file for the build configuration. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
</ul>
<p>The <strong>repository</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">branchName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The branch name for which builds are triggered. Defaults to <code class="docutils literal notranslate"><span class="pre">master</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">repoId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The id of the repository. For <code class="docutils literal notranslate"><span class="pre">TfsGit</span></code> repos, this is simply the ID of the repository. For <code class="docutils literal notranslate"><span class="pre">Github</span></code> repos, this will take the form of <code class="docutils literal notranslate"><span class="pre">&lt;GitHub</span> <span class="pre">Org&gt;/&lt;Repo</span> <span class="pre">Name&gt;</span></code>. For <code class="docutils literal notranslate"><span class="pre">Bitbucket</span></code> repos, this will take the form of <code class="docutils literal notranslate"><span class="pre">&lt;Workspace</span> <span class="pre">ID&gt;/&lt;Repo</span> <span class="pre">Name&gt;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">repoType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The repository type. Valid values: <code class="docutils literal notranslate"><span class="pre">GitHub</span></code> or <code class="docutils literal notranslate"><span class="pre">TfsGit</span></code> or <code class="docutils literal notranslate"><span class="pre">Bitbucket</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">Github</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">serviceConnectionId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The service connection ID. Used if the <code class="docutils literal notranslate"><span class="pre">repo_type</span></code> is <code class="docutils literal notranslate"><span class="pre">GitHub</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ymlPath</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The path of the Yaml file describing the build definition.</p></li>
</ul>
<p>The <strong>variables</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">allowOverride</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - True if the variable can be overridden. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">isSecret</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - True if the variable is a secret. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the variable.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">secretValue</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The secret value of the variable. Used when <code class="docutils literal notranslate"><span class="pre">is_secret</span></code> set to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The value of the variable.</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_azuredevops.build.BuildDefinition.agent_pool_name">
<code class="sig-name descname">agent_pool_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuredevops.build.BuildDefinition.agent_pool_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The agent pool that should execute the build. Defaults to <code class="docutils literal notranslate"><span class="pre">Hosted</span> <span class="pre">Ubuntu</span> <span class="pre">1604</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azuredevops.build.BuildDefinition.ci_trigger">
<code class="sig-name descname">ci_trigger</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuredevops.build.BuildDefinition.ci_trigger" title="Permalink to this definition">¶</a></dt>
<dd><p>Continuous Integration Integration trigger.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">override</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - Override the azure-pipeline file and use a this configuration for all builds.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">batch</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - If you set batch to true, when a pipeline is running, the system waits until the run is completed, then starts another run with all changes that have not yet been built. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">branchFilters</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - The branches to include and exclude from the trigger.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">excludes</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - List of branch patterns to exclude.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">includes</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - List of branch patterns to include.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxConcurrentBuildsPerBranch</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The number of max builds per branch. Defaults to <code class="docutils literal notranslate"><span class="pre">1</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">pathFilters</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - Specify file paths to include or exclude. Note that the wildcard syntax is different between branches/tags and file paths.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">excludes</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - List of branch patterns to exclude.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">includes</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - List of branch patterns to include.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">pollingInterval</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - How often the external repository is polled. Defaults to <code class="docutils literal notranslate"><span class="pre">0</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">pollingJobId</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - This is the ID of the polling job that polls the external repository. Once the build definition is saved/updated, this value is set.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">useYaml</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Use the azure-pipeline file for the build configuration. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azuredevops.build.BuildDefinition.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuredevops.build.BuildDefinition.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the build definition.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azuredevops.build.BuildDefinition.project_id">
<code class="sig-name descname">project_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuredevops.build.BuildDefinition.project_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The project ID or project name.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azuredevops.build.BuildDefinition.pull_request_trigger">
<code class="sig-name descname">pull_request_trigger</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuredevops.build.BuildDefinition.pull_request_trigger" title="Permalink to this definition">¶</a></dt>
<dd><p>Pull Request Integration Integration trigger.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">commentRequired</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">forks</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - Set permissions for Forked repositories.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Build pull requests form forms of this repository.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">shareSecrets</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Make secrets available to builds of forks.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">initialBranch</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">override</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>) - Override the azure-pipeline file and use a this configuration for all builds.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">autoCancel</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - . Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">branchFilters</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - The branches to include and exclude from the trigger.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">excludes</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - List of branch patterns to exclude.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">includes</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - List of branch patterns to include.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">pathFilters</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - Specify file paths to include or exclude. Note that the wildcard syntax is different between branches/tags and file paths.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">excludes</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - List of branch patterns to exclude.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">includes</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - List of branch patterns to include.</p></li>
</ul>
</li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">useYaml</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Use the azure-pipeline file for the build configuration. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azuredevops.build.BuildDefinition.repository">
<code class="sig-name descname">repository</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuredevops.build.BuildDefinition.repository" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">repository</span></code> block as documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">branchName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The branch name for which builds are triggered. Defaults to <code class="docutils literal notranslate"><span class="pre">master</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">repoId</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The id of the repository. For <code class="docutils literal notranslate"><span class="pre">TfsGit</span></code> repos, this is simply the ID of the repository. For <code class="docutils literal notranslate"><span class="pre">Github</span></code> repos, this will take the form of <code class="docutils literal notranslate"><span class="pre">&lt;GitHub</span> <span class="pre">Org&gt;/&lt;Repo</span> <span class="pre">Name&gt;</span></code>. For <code class="docutils literal notranslate"><span class="pre">Bitbucket</span></code> repos, this will take the form of <code class="docutils literal notranslate"><span class="pre">&lt;Workspace</span> <span class="pre">ID&gt;/&lt;Repo</span> <span class="pre">Name&gt;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">repoType</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The repository type. Valid values: <code class="docutils literal notranslate"><span class="pre">GitHub</span></code> or <code class="docutils literal notranslate"><span class="pre">TfsGit</span></code> or <code class="docutils literal notranslate"><span class="pre">Bitbucket</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">Github</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">serviceConnectionId</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The service connection ID. Used if the <code class="docutils literal notranslate"><span class="pre">repo_type</span></code> is <code class="docutils literal notranslate"><span class="pre">GitHub</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ymlPath</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The path of the Yaml file describing the build definition.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azuredevops.build.BuildDefinition.revision">
<code class="sig-name descname">revision</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuredevops.build.BuildDefinition.revision" title="Permalink to this definition">¶</a></dt>
<dd><p>The revision of the build definition</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azuredevops.build.BuildDefinition.variable_groups">
<code class="sig-name descname">variable_groups</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuredevops.build.BuildDefinition.variable_groups" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of variable group IDs (integers) to link to the build definition.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azuredevops.build.BuildDefinition.variables">
<code class="sig-name descname">variables</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuredevops.build.BuildDefinition.variables" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of <code class="docutils literal notranslate"><span class="pre">variable</span></code> blocks, as documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">allowOverride</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - True if the variable can be overridden. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">isSecret</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - True if the variable is a secret. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the variable.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">secretValue</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The secret value of the variable. Used when <code class="docutils literal notranslate"><span class="pre">is_secret</span></code> set to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The value of the variable.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.build.BuildDefinition.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">agent_pool_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ci_trigger</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">path</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">pull_request_trigger</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">repository</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">revision</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">variable_groups</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">variables</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuredevops.build.BuildDefinition.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing BuildDefinition resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>agent_pool_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The agent pool that should execute the build. Defaults to <code class="docutils literal notranslate"><span class="pre">Hosted</span> <span class="pre">Ubuntu</span> <span class="pre">1604</span></code>.</p></li>
<li><p><strong>ci_trigger</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Continuous Integration Integration trigger.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the build definition.</p></li>
<li><p><strong>project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The project ID or project name.</p></li>
<li><p><strong>pull_request_trigger</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Pull Request Integration Integration trigger.</p></li>
<li><p><strong>repository</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">repository</span></code> block as documented below.</p></li>
<li><p><strong>revision</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The revision of the build definition</p></li>
<li><p><strong>variable_groups</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of variable group IDs (integers) to link to the build definition.</p></li>
<li><p><strong>variables</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of <code class="docutils literal notranslate"><span class="pre">variable</span></code> blocks, as documented below.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>ci_trigger</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">override</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Override the azure-pipeline file and use a this configuration for all builds.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">batch</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - If you set batch to true, when a pipeline is running, the system waits until the run is completed, then starts another run with all changes that have not yet been built. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">branchFilters</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The branches to include and exclude from the trigger.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">excludes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - List of branch patterns to exclude.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">includes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - List of branch patterns to include.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">maxConcurrentBuildsPerBranch</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of max builds per branch. Defaults to <code class="docutils literal notranslate"><span class="pre">1</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">pathFilters</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Specify file paths to include or exclude. Note that the wildcard syntax is different between branches/tags and file paths.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">excludes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - List of branch patterns to exclude.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">includes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - List of branch patterns to include.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">pollingInterval</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - How often the external repository is polled. Defaults to <code class="docutils literal notranslate"><span class="pre">0</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">pollingJobId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - This is the ID of the polling job that polls the external repository. Once the build definition is saved/updated, this value is set.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">useYaml</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Use the azure-pipeline file for the build configuration. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
</ul>
<p>The <strong>pull_request_trigger</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">commentRequired</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">forks</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Set permissions for Forked repositories.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">enabled</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Build pull requests form forms of this repository.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">shareSecrets</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Make secrets available to builds of forks.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">initialBranch</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">override</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>) - Override the azure-pipeline file and use a this configuration for all builds.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">autoCancel</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - . Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">branchFilters</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - The branches to include and exclude from the trigger.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">excludes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - List of branch patterns to exclude.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">includes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - List of branch patterns to include.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">pathFilters</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Specify file paths to include or exclude. Note that the wildcard syntax is different between branches/tags and file paths.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">excludes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - List of branch patterns to exclude.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">includes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - List of branch patterns to include.</p></li>
</ul>
</li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">useYaml</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Use the azure-pipeline file for the build configuration. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
</ul>
<p>The <strong>repository</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">branchName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The branch name for which builds are triggered. Defaults to <code class="docutils literal notranslate"><span class="pre">master</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">repoId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The id of the repository. For <code class="docutils literal notranslate"><span class="pre">TfsGit</span></code> repos, this is simply the ID of the repository. For <code class="docutils literal notranslate"><span class="pre">Github</span></code> repos, this will take the form of <code class="docutils literal notranslate"><span class="pre">&lt;GitHub</span> <span class="pre">Org&gt;/&lt;Repo</span> <span class="pre">Name&gt;</span></code>. For <code class="docutils literal notranslate"><span class="pre">Bitbucket</span></code> repos, this will take the form of <code class="docutils literal notranslate"><span class="pre">&lt;Workspace</span> <span class="pre">ID&gt;/&lt;Repo</span> <span class="pre">Name&gt;</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">repoType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The repository type. Valid values: <code class="docutils literal notranslate"><span class="pre">GitHub</span></code> or <code class="docutils literal notranslate"><span class="pre">TfsGit</span></code> or <code class="docutils literal notranslate"><span class="pre">Bitbucket</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">Github</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">serviceConnectionId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The service connection ID. Used if the <code class="docutils literal notranslate"><span class="pre">repo_type</span></code> is <code class="docutils literal notranslate"><span class="pre">GitHub</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ymlPath</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The path of the Yaml file describing the build definition.</p></li>
</ul>
<p>The <strong>variables</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">allowOverride</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - True if the variable can be overridden. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">isSecret</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - True if the variable is a secret. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the variable.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">secretValue</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The secret value of the variable. Used when <code class="docutils literal notranslate"><span class="pre">is_secret</span></code> set to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">value</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The value of the variable.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.build.BuildDefinition.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuredevops.build.BuildDefinition.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azuredevops.build.BuildDefinition.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuredevops.build.BuildDefinition.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
