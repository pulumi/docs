---
title: Module policy
title_tag: Module policy | Package pulumi_azuredevops | Python SDK
linktitle: policy
notitle: true
block_external_search_index: true
---

{{< resource-docs-alert "azuredevops" >}}

<div class="section" id="policy">
<h1>policy<a class="headerlink" href="#policy" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azuredevops">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-azuredevops/issues">pulumi/pulumi-azuredevops repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azuredevops/issues">terraform-providers/terraform-provider-azuredevops repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_azuredevops.policy"></span><dl class="py class">
<dt id="pulumi_azuredevops.policy.BranchPolicyBuildValidation">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azuredevops.policy.</code><code class="sig-name descname">BranchPolicyBuildValidation</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">blocking</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">settings</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuredevops.policy.BranchPolicyBuildValidation" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a build validation branch policy within Azure DevOps.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_azuredevops</span> <span class="k">as</span> <span class="nn">azuredevops</span>

<span class="n">project</span> <span class="o">=</span> <span class="n">azuredevops</span><span class="o">.</span><span class="n">core</span><span class="o">.</span><span class="n">Project</span><span class="p">(</span><span class="s2">&quot;project&quot;</span><span class="p">,</span> <span class="n">project_name</span><span class="o">=</span><span class="s2">&quot;Sample Project&quot;</span><span class="p">)</span>
<span class="n">git</span> <span class="o">=</span> <span class="n">azuredevops</span><span class="o">.</span><span class="n">repository</span><span class="o">.</span><span class="n">Git</span><span class="p">(</span><span class="s2">&quot;git&quot;</span><span class="p">,</span>
    <span class="n">project_id</span><span class="o">=</span><span class="n">project</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">initialization</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;initType&quot;</span><span class="p">:</span> <span class="s2">&quot;Clean&quot;</span><span class="p">,</span>
    <span class="p">})</span>
<span class="n">build_definition</span> <span class="o">=</span> <span class="n">azuredevops</span><span class="o">.</span><span class="n">build</span><span class="o">.</span><span class="n">BuildDefinition</span><span class="p">(</span><span class="s2">&quot;buildDefinition&quot;</span><span class="p">,</span>
    <span class="n">project_id</span><span class="o">=</span><span class="n">project</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">repository</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;repoType&quot;</span><span class="p">:</span> <span class="s2">&quot;TfsGit&quot;</span><span class="p">,</span>
        <span class="s2">&quot;repoId&quot;</span><span class="p">:</span> <span class="n">git</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
        <span class="s2">&quot;ymlPath&quot;</span><span class="p">:</span> <span class="s2">&quot;azure-pipelines.yml&quot;</span><span class="p">,</span>
    <span class="p">})</span>
<span class="n">branch_policy_build_validation</span> <span class="o">=</span> <span class="n">azuredevops</span><span class="o">.</span><span class="n">policy</span><span class="o">.</span><span class="n">BranchPolicyBuildValidation</span><span class="p">(</span><span class="s2">&quot;branchPolicyBuildValidation&quot;</span><span class="p">,</span>
    <span class="n">project_id</span><span class="o">=</span><span class="n">project</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">enabled</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="n">blocking</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="n">settings</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;display_name&quot;</span><span class="p">:</span> <span class="s2">&quot;Don&#39;t break the build!&quot;</span><span class="p">,</span>
        <span class="s2">&quot;buildDefinitionId&quot;</span><span class="p">:</span> <span class="n">build_definition</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
        <span class="s2">&quot;validDuration&quot;</span><span class="p">:</span> <span class="mi">720</span><span class="p">,</span>
        <span class="s2">&quot;scope&quot;</span><span class="p">:</span> <span class="p">[</span>
            <span class="p">{</span>
                <span class="s2">&quot;repositoryId&quot;</span><span class="p">:</span> <span class="n">git</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
                <span class="s2">&quot;repositoryRef&quot;</span><span class="p">:</span> <span class="n">git</span><span class="o">.</span><span class="n">default_branch</span><span class="p">,</span>
                <span class="s2">&quot;matchType&quot;</span><span class="p">:</span> <span class="s2">&quot;Exact&quot;</span><span class="p">,</span>
            <span class="p">},</span>
            <span class="p">{</span>
                <span class="s2">&quot;repositoryId&quot;</span><span class="p">:</span> <span class="n">git</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
                <span class="s2">&quot;repositoryRef&quot;</span><span class="p">:</span> <span class="s2">&quot;refs/heads/releases&quot;</span><span class="p">,</span>
                <span class="s2">&quot;matchType&quot;</span><span class="p">:</span> <span class="s2">&quot;Prefix&quot;</span><span class="p">,</span>
            <span class="p">},</span>
        <span class="p">],</span>
    <span class="p">})</span>
</pre></div>
</div>
<ul class="simple">
<li><p><a class="reference external" href="https://docs.microsoft.com/en-us/rest/api/azure/devops/policy/configurations/create?view=azure-devops-rest-5.1">Azure DevOps Service REST API 5.1 - Policy Configurations</a></p></li>
</ul>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>blocking</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – A flag indicating if the policy should be blocking. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – A flag indicating if the policy should be enabled. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the policy will be created.</p></li>
<li><p><strong>settings</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Configuration for the policy. This block must be defined exactly once.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>settings</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">buildDefinitionId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The ID of the build to monitor for the policy.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">display_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The display name for the policy.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">manualQueueOnly</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - If set to true, the build will need to be manually queued. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">queueOnSourceUpdateOnly</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - True if the build should queue on source updates only. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">scopes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Controls which repositories and branches the policy will be enabled for. This block must be defined at least once.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">matchType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The match type to use when applying the policy. Supported values are <code class="docutils literal notranslate"><span class="pre">Exact</span></code> (default) or <code class="docutils literal notranslate"><span class="pre">Prefix</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">repositoryId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The repository ID. Needed only if the scope of the policy will be limited to a single repository.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">repositoryRef</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ref pattern to use for the match. If <code class="docutils literal notranslate"><span class="pre">match_type</span></code> is <code class="docutils literal notranslate"><span class="pre">Exact</span></code>, this should be a qualified ref such as <code class="docutils literal notranslate"><span class="pre">refs/heads/master</span></code>. If <code class="docutils literal notranslate"><span class="pre">match_type</span></code> is <code class="docutils literal notranslate"><span class="pre">Prefix</span></code>, this should be a ref path such as <code class="docutils literal notranslate"><span class="pre">refs/heads/releases</span></code>.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">validDuration</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of minutes for which the build is valid. If <code class="docutils literal notranslate"><span class="pre">0</span></code>, the build will not expire. Defaults to <code class="docutils literal notranslate"><span class="pre">720</span></code> (12 hours).</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_azuredevops.policy.BranchPolicyBuildValidation.blocking">
<code class="sig-name descname">blocking</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuredevops.policy.BranchPolicyBuildValidation.blocking" title="Permalink to this definition">¶</a></dt>
<dd><p>A flag indicating if the policy should be blocking. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azuredevops.policy.BranchPolicyBuildValidation.enabled">
<code class="sig-name descname">enabled</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuredevops.policy.BranchPolicyBuildValidation.enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>A flag indicating if the policy should be enabled. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azuredevops.policy.BranchPolicyBuildValidation.project_id">
<code class="sig-name descname">project_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuredevops.policy.BranchPolicyBuildValidation.project_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the policy will be created.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azuredevops.policy.BranchPolicyBuildValidation.settings">
<code class="sig-name descname">settings</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuredevops.policy.BranchPolicyBuildValidation.settings" title="Permalink to this definition">¶</a></dt>
<dd><p>Configuration for the policy. This block must be defined exactly once.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">buildDefinitionId</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The ID of the build to monitor for the policy.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">display_name</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The display name for the policy.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">manualQueueOnly</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - If set to true, the build will need to be manually queued. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">queueOnSourceUpdateOnly</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - True if the build should queue on source updates only. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">scopes</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - Controls which repositories and branches the policy will be enabled for. This block must be defined at least once.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">matchType</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The match type to use when applying the policy. Supported values are <code class="docutils literal notranslate"><span class="pre">Exact</span></code> (default) or <code class="docutils literal notranslate"><span class="pre">Prefix</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">repositoryId</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The repository ID. Needed only if the scope of the policy will be limited to a single repository.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">repositoryRef</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ref pattern to use for the match. If <code class="docutils literal notranslate"><span class="pre">match_type</span></code> is <code class="docutils literal notranslate"><span class="pre">Exact</span></code>, this should be a qualified ref such as <code class="docutils literal notranslate"><span class="pre">refs/heads/master</span></code>. If <code class="docutils literal notranslate"><span class="pre">match_type</span></code> is <code class="docutils literal notranslate"><span class="pre">Prefix</span></code>, this should be a ref path such as <code class="docutils literal notranslate"><span class="pre">refs/heads/releases</span></code>.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">validDuration</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The number of minutes for which the build is valid. If <code class="docutils literal notranslate"><span class="pre">0</span></code>, the build will not expire. Defaults to <code class="docutils literal notranslate"><span class="pre">720</span></code> (12 hours).</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.policy.BranchPolicyBuildValidation.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">blocking</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">settings</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuredevops.policy.BranchPolicyBuildValidation.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing BranchPolicyBuildValidation resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>blocking</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – A flag indicating if the policy should be blocking. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – A flag indicating if the policy should be enabled. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the policy will be created.</p></li>
<li><p><strong>settings</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Configuration for the policy. This block must be defined exactly once.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>settings</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">buildDefinitionId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The ID of the build to monitor for the policy.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">display_name</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The display name for the policy.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">manualQueueOnly</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - If set to true, the build will need to be manually queued. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">queueOnSourceUpdateOnly</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - True if the build should queue on source updates only. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">scopes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Controls which repositories and branches the policy will be enabled for. This block must be defined at least once.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">matchType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The match type to use when applying the policy. Supported values are <code class="docutils literal notranslate"><span class="pre">Exact</span></code> (default) or <code class="docutils literal notranslate"><span class="pre">Prefix</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">repositoryId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The repository ID. Needed only if the scope of the policy will be limited to a single repository.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">repositoryRef</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ref pattern to use for the match. If <code class="docutils literal notranslate"><span class="pre">match_type</span></code> is <code class="docutils literal notranslate"><span class="pre">Exact</span></code>, this should be a qualified ref such as <code class="docutils literal notranslate"><span class="pre">refs/heads/master</span></code>. If <code class="docutils literal notranslate"><span class="pre">match_type</span></code> is <code class="docutils literal notranslate"><span class="pre">Prefix</span></code>, this should be a ref path such as <code class="docutils literal notranslate"><span class="pre">refs/heads/releases</span></code>.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">validDuration</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of minutes for which the build is valid. If <code class="docutils literal notranslate"><span class="pre">0</span></code>, the build will not expire. Defaults to <code class="docutils literal notranslate"><span class="pre">720</span></code> (12 hours).</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.policy.BranchPolicyBuildValidation.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuredevops.policy.BranchPolicyBuildValidation.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azuredevops.policy.BranchPolicyBuildValidation.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuredevops.policy.BranchPolicyBuildValidation.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azuredevops.policy.BranchPolicyMinReviewers">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azuredevops.policy.</code><code class="sig-name descname">BranchPolicyMinReviewers</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">blocking</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">settings</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuredevops.policy.BranchPolicyMinReviewers" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a minimum reviewer branch policy within Azure DevOps.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_azuredevops</span> <span class="k">as</span> <span class="nn">azuredevops</span>

<span class="n">project</span> <span class="o">=</span> <span class="n">azuredevops</span><span class="o">.</span><span class="n">core</span><span class="o">.</span><span class="n">Project</span><span class="p">(</span><span class="s2">&quot;project&quot;</span><span class="p">,</span> <span class="n">project_name</span><span class="o">=</span><span class="s2">&quot;Sample Project&quot;</span><span class="p">)</span>
<span class="n">git</span> <span class="o">=</span> <span class="n">azuredevops</span><span class="o">.</span><span class="n">repository</span><span class="o">.</span><span class="n">Git</span><span class="p">(</span><span class="s2">&quot;git&quot;</span><span class="p">,</span>
    <span class="n">project_id</span><span class="o">=</span><span class="n">project</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">initialization</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;initType&quot;</span><span class="p">:</span> <span class="s2">&quot;Clean&quot;</span><span class="p">,</span>
    <span class="p">})</span>
<span class="n">branch_policy_min_reviewers</span> <span class="o">=</span> <span class="n">azuredevops</span><span class="o">.</span><span class="n">policy</span><span class="o">.</span><span class="n">BranchPolicyMinReviewers</span><span class="p">(</span><span class="s2">&quot;branchPolicyMinReviewers&quot;</span><span class="p">,</span>
    <span class="n">project_id</span><span class="o">=</span><span class="n">project</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">enabled</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="n">blocking</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="n">settings</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;reviewerCount&quot;</span><span class="p">:</span> <span class="mi">2</span><span class="p">,</span>
        <span class="s2">&quot;submitterCanVote&quot;</span><span class="p">:</span> <span class="kc">False</span><span class="p">,</span>
        <span class="s2">&quot;scope&quot;</span><span class="p">:</span> <span class="p">[</span>
            <span class="p">{</span>
                <span class="s2">&quot;repositoryId&quot;</span><span class="p">:</span> <span class="n">git</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
                <span class="s2">&quot;repositoryRef&quot;</span><span class="p">:</span> <span class="n">git</span><span class="o">.</span><span class="n">default_branch</span><span class="p">,</span>
                <span class="s2">&quot;matchType&quot;</span><span class="p">:</span> <span class="s2">&quot;Exact&quot;</span><span class="p">,</span>
            <span class="p">},</span>
            <span class="p">{</span>
                <span class="s2">&quot;repositoryId&quot;</span><span class="p">:</span> <span class="n">git</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
                <span class="s2">&quot;repositoryRef&quot;</span><span class="p">:</span> <span class="s2">&quot;refs/heads/releases&quot;</span><span class="p">,</span>
                <span class="s2">&quot;matchType&quot;</span><span class="p">:</span> <span class="s2">&quot;Prefix&quot;</span><span class="p">,</span>
            <span class="p">},</span>
        <span class="p">],</span>
    <span class="p">})</span>
</pre></div>
</div>
<ul class="simple">
<li><p><a class="reference external" href="https://docs.microsoft.com/en-us/rest/api/azure/devops/policy/configurations/create?view=azure-devops-rest-5.1">Azure DevOps Service REST API 5.1 - Policy Configurations</a></p></li>
</ul>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>blocking</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – A flag indicating if the policy should be blocking. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – A flag indicating if the policy should be enabled. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the policy will be created.</p></li>
<li><p><strong>settings</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Configuration for the policy. This block must be defined exactly once.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>settings</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">reviewerCount</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of reviewrs needed to approve.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">scopes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Controls which repositories and branches the policy will be enabled for. This block must be defined at least once.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">matchType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The match type to use when applying the policy. Supported values are <code class="docutils literal notranslate"><span class="pre">Exact</span></code> (default) or <code class="docutils literal notranslate"><span class="pre">Prefix</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">repositoryId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The repository ID. Needed only if the scope of the policy will be limited to a single repository.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">repositoryRef</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ref pattern to use for the match. If <code class="docutils literal notranslate"><span class="pre">match_type</span></code> is <code class="docutils literal notranslate"><span class="pre">Exact</span></code>, this should be a qualified ref such as <code class="docutils literal notranslate"><span class="pre">refs/heads/master</span></code>. If <code class="docutils literal notranslate"><span class="pre">match_type</span></code> is <code class="docutils literal notranslate"><span class="pre">Prefix</span></code>, this should be a ref path such as <code class="docutils literal notranslate"><span class="pre">refs/heads/releases</span></code>.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">submitterCanVote</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Controls whether or not the submitter’s vote counts. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_azuredevops.policy.BranchPolicyMinReviewers.blocking">
<code class="sig-name descname">blocking</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuredevops.policy.BranchPolicyMinReviewers.blocking" title="Permalink to this definition">¶</a></dt>
<dd><p>A flag indicating if the policy should be blocking. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azuredevops.policy.BranchPolicyMinReviewers.enabled">
<code class="sig-name descname">enabled</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuredevops.policy.BranchPolicyMinReviewers.enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>A flag indicating if the policy should be enabled. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azuredevops.policy.BranchPolicyMinReviewers.project_id">
<code class="sig-name descname">project_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuredevops.policy.BranchPolicyMinReviewers.project_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the policy will be created.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azuredevops.policy.BranchPolicyMinReviewers.settings">
<code class="sig-name descname">settings</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuredevops.policy.BranchPolicyMinReviewers.settings" title="Permalink to this definition">¶</a></dt>
<dd><p>Configuration for the policy. This block must be defined exactly once.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">reviewerCount</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>) - The number of reviewrs needed to approve.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">scopes</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>) - Controls which repositories and branches the policy will be enabled for. This block must be defined at least once.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">matchType</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The match type to use when applying the policy. Supported values are <code class="docutils literal notranslate"><span class="pre">Exact</span></code> (default) or <code class="docutils literal notranslate"><span class="pre">Prefix</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">repositoryId</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The repository ID. Needed only if the scope of the policy will be limited to a single repository.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">repositoryRef</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ref pattern to use for the match. If <code class="docutils literal notranslate"><span class="pre">match_type</span></code> is <code class="docutils literal notranslate"><span class="pre">Exact</span></code>, this should be a qualified ref such as <code class="docutils literal notranslate"><span class="pre">refs/heads/master</span></code>. If <code class="docutils literal notranslate"><span class="pre">match_type</span></code> is <code class="docutils literal notranslate"><span class="pre">Prefix</span></code>, this should be a ref path such as <code class="docutils literal notranslate"><span class="pre">refs/heads/releases</span></code>.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">submitterCanVote</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>) - Controls whether or not the submitter’s vote counts. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.policy.BranchPolicyMinReviewers.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">blocking</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">settings</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuredevops.policy.BranchPolicyMinReviewers.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing BranchPolicyMinReviewers resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>blocking</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – A flag indicating if the policy should be blocking. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – A flag indicating if the policy should be enabled. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the policy will be created.</p></li>
<li><p><strong>settings</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Configuration for the policy. This block must be defined exactly once.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>settings</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">reviewerCount</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>) - The number of reviewrs needed to approve.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">scopes</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>) - Controls which repositories and branches the policy will be enabled for. This block must be defined at least once.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">matchType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The match type to use when applying the policy. Supported values are <code class="docutils literal notranslate"><span class="pre">Exact</span></code> (default) or <code class="docutils literal notranslate"><span class="pre">Prefix</span></code>.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">repositoryId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The repository ID. Needed only if the scope of the policy will be limited to a single repository.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">repositoryRef</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ref pattern to use for the match. If <code class="docutils literal notranslate"><span class="pre">match_type</span></code> is <code class="docutils literal notranslate"><span class="pre">Exact</span></code>, this should be a qualified ref such as <code class="docutils literal notranslate"><span class="pre">refs/heads/master</span></code>. If <code class="docutils literal notranslate"><span class="pre">match_type</span></code> is <code class="docutils literal notranslate"><span class="pre">Prefix</span></code>, this should be a ref path such as <code class="docutils literal notranslate"><span class="pre">refs/heads/releases</span></code>.</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">submitterCanVote</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>) - Controls whether or not the submitter’s vote counts. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.policy.BranchPolicyMinReviewers.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuredevops.policy.BranchPolicyMinReviewers.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azuredevops.policy.BranchPolicyMinReviewers.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuredevops.policy.BranchPolicyMinReviewers.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
