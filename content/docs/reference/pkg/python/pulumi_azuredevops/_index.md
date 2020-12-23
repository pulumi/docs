---
title: Package pulumi_azuredevops
title_tag: Package pulumi_azuredevops | Python SDK
linktitle: pulumi_azuredevops
notitle: true
block_external_search_index: true
---

{{< resource-docs-alert "azuredevops" >}}

<div class="section" id="pulumi-azure-devops">
<h1>Pulumi Azure DevOps<a class="headerlink" href="#pulumi-azure-devops" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azuredevops">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-azuredevops/issues">pulumi/pulumi-azuredevops repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azuredevops/issues">terraform-providers/terraform-provider-azuredevops repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_azuredevops"></span><dl class="py class">
<dt id="pulumi_azuredevops.AreaPermissions">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azuredevops.</code><code class="sig-name descname">AreaPermissions</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">path</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">permissions</span><span class="p">:</span> <span class="n">Union[Mapping[str, Union[str, Awaitable[str], Output[T]]], Awaitable[Mapping[str, Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">principal</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">replace</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuredevops.AreaPermissions" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages permissions for an Area (Component)</p>
<blockquote>
<div><p><strong>Note</strong> Permissions can be assigned to group principals and not to single user principals.</p>
</div></blockquote>
<p>Permission for Areas within Azure DevOps can be applied on two different levels.
Those levels are reflected by specifying (or omitting) values for the arguments <code class="docutils literal notranslate"><span class="pre">project_id</span></code> and <code class="docutils literal notranslate"><span class="pre">path</span></code>.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_azuredevops</span> <span class="k">as</span> <span class="nn">azuredevops</span>

<span class="n">project</span> <span class="o">=</span> <span class="n">azuredevops</span><span class="o">.</span><span class="n">Project</span><span class="p">(</span><span class="s2">&quot;project&quot;</span><span class="p">,</span>
    <span class="n">work_item_template</span><span class="o">=</span><span class="s2">&quot;Agile&quot;</span><span class="p">,</span>
    <span class="n">version_control</span><span class="o">=</span><span class="s2">&quot;Git&quot;</span><span class="p">,</span>
    <span class="n">visibility</span><span class="o">=</span><span class="s2">&quot;private&quot;</span><span class="p">,</span>
    <span class="n">description</span><span class="o">=</span><span class="s2">&quot;Managed by Terraform&quot;</span><span class="p">)</span>
<span class="n">project_readers</span> <span class="o">=</span> <span class="n">project</span><span class="o">.</span><span class="n">id</span><span class="o">.</span><span class="n">apply</span><span class="p">(</span><span class="k">lambda</span> <span class="nb">id</span><span class="p">:</span> <span class="n">azuredevops</span><span class="o">.</span><span class="n">get_group</span><span class="p">(</span><span class="n">project_id</span><span class="o">=</span><span class="nb">id</span><span class="p">,</span>
    <span class="n">name</span><span class="o">=</span><span class="s2">&quot;Readers&quot;</span><span class="p">))</span>
<span class="n">root_permissions</span> <span class="o">=</span> <span class="n">azuredevops</span><span class="o">.</span><span class="n">AreaPermissions</span><span class="p">(</span><span class="s2">&quot;root-permissions&quot;</span><span class="p">,</span>
    <span class="n">project_id</span><span class="o">=</span><span class="n">project</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">principal</span><span class="o">=</span><span class="n">project_readers</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">path</span><span class="o">=</span><span class="s2">&quot;/&quot;</span><span class="p">,</span>
    <span class="n">permissions</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;CREATE_CHILDREN&quot;</span><span class="p">:</span> <span class="s2">&quot;Deny&quot;</span><span class="p">,</span>
        <span class="s2">&quot;GENERIC_READ&quot;</span><span class="p">:</span> <span class="s2">&quot;Allow&quot;</span><span class="p">,</span>
        <span class="s2">&quot;DELETE&quot;</span><span class="p">:</span> <span class="s2">&quot;Deny&quot;</span><span class="p">,</span>
        <span class="s2">&quot;WORK_ITEM_READ&quot;</span><span class="p">:</span> <span class="s2">&quot;Allow&quot;</span><span class="p">,</span>
    <span class="p">})</span>
</pre></div>
</div>
<ul class="simple">
<li><p><a class="reference external" href="https://docs.microsoft.com/en-us/rest/api/azure/devops/security/?view=azure-devops-rest-5.1">Azure DevOps Service REST API 5.1 - Security</a></p></li>
</ul>
<ul class="simple">
<li><p><strong>Project &amp; Team</strong>: vso.security_manage - Grants the ability to read, write, and manage security permissions.</p></li>
</ul>
<p>The resource does not support import.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>path</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the branch to assign the permissions.</p></li>
<li><p><strong>pulumi.Input</strong><strong>[</strong><strong>str</strong><strong>]</strong><strong>]</strong><strong>] </strong><strong>permissions</strong> (<em>pulumi.Input</em><em>[</em><em>Mapping</em><em>[</em><em>str</em><em>,</em>) – the permissions to assign. The following permissions are available.</p></li>
<li><p><strong>principal</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The <strong>group</strong> principal to assign the permissions.</p></li>
<li><p><strong>project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project to assign the permissions.</p></li>
<li><p><strong>replace</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Replace (<code class="docutils literal notranslate"><span class="pre">true</span></code>) or merge (<code class="docutils literal notranslate"><span class="pre">false</span></code>) the permissions. Default: <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_azuredevops.AreaPermissions.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">path</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">permissions</span><span class="p">:</span> <span class="n">Union[Mapping[str, Union[str, Awaitable[str], Output[T]]], Awaitable[Mapping[str, Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">principal</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">replace</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_azuredevops.area_permissions.AreaPermissions<a class="headerlink" href="#pulumi_azuredevops.AreaPermissions.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing AreaPermissions resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>path</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the branch to assign the permissions.</p></li>
<li><p><strong>pulumi.Input</strong><strong>[</strong><strong>str</strong><strong>]</strong><strong>]</strong><strong>] </strong><strong>permissions</strong> (<em>pulumi.Input</em><em>[</em><em>Mapping</em><em>[</em><em>str</em><em>,</em>) – the permissions to assign. The following permissions are available.</p></li>
<li><p><strong>principal</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The <strong>group</strong> principal to assign the permissions.</p></li>
<li><p><strong>project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project to assign the permissions.</p></li>
<li><p><strong>replace</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Replace (<code class="docutils literal notranslate"><span class="pre">true</span></code>) or merge (<code class="docutils literal notranslate"><span class="pre">false</span></code>) the permissions. Default: <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.AreaPermissions.path">
<em class="property">property </em><code class="sig-name descname">path</code><a class="headerlink" href="#pulumi_azuredevops.AreaPermissions.path" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the branch to assign the permissions.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.AreaPermissions.permissions">
<em class="property">property </em><code class="sig-name descname">permissions</code><a class="headerlink" href="#pulumi_azuredevops.AreaPermissions.permissions" title="Permalink to this definition">¶</a></dt>
<dd><p>the permissions to assign. The following permissions are available.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.AreaPermissions.principal">
<em class="property">property </em><code class="sig-name descname">principal</code><a class="headerlink" href="#pulumi_azuredevops.AreaPermissions.principal" title="Permalink to this definition">¶</a></dt>
<dd><p>The <strong>group</strong> principal to assign the permissions.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.AreaPermissions.project_id">
<em class="property">property </em><code class="sig-name descname">project_id</code><a class="headerlink" href="#pulumi_azuredevops.AreaPermissions.project_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project to assign the permissions.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.AreaPermissions.replace">
<em class="property">property </em><code class="sig-name descname">replace</code><a class="headerlink" href="#pulumi_azuredevops.AreaPermissions.replace" title="Permalink to this definition">¶</a></dt>
<dd><p>Replace (<code class="docutils literal notranslate"><span class="pre">true</span></code>) or merge (<code class="docutils literal notranslate"><span class="pre">false</span></code>) the permissions. Default: <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.AreaPermissions.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuredevops.AreaPermissions.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azuredevops.AreaPermissions.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuredevops.AreaPermissions.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azuredevops.AwaitableGetAgentQueueResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azuredevops.</code><code class="sig-name descname">AwaitableGetAgentQueueResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">agent_pool_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuredevops.AwaitableGetAgentQueueResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_azuredevops.AwaitableGetAreaResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azuredevops.</code><code class="sig-name descname">AwaitableGetAreaResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">childrens</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">fetch_children</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">has_children</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">path</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuredevops.AwaitableGetAreaResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_azuredevops.AwaitableGetClientConfigResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azuredevops.</code><code class="sig-name descname">AwaitableGetClientConfigResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">organization_url</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuredevops.AwaitableGetClientConfigResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_azuredevops.AwaitableGetGitRepositoryResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azuredevops.</code><code class="sig-name descname">AwaitableGetGitRepositoryResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">default_branch</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">is_fork</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">remote_url</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">size</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ssh_url</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">url</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">web_url</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuredevops.AwaitableGetGitRepositoryResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_azuredevops.AwaitableGetGroupResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azuredevops.</code><code class="sig-name descname">AwaitableGetGroupResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">descriptor</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">origin</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">origin_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuredevops.AwaitableGetGroupResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_azuredevops.AwaitableGetIterationResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azuredevops.</code><code class="sig-name descname">AwaitableGetIterationResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">childrens</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">fetch_children</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">has_children</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">path</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuredevops.AwaitableGetIterationResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_azuredevops.AwaitableGetPoolResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azuredevops.</code><code class="sig-name descname">AwaitableGetPoolResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">auto_provision</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">pool_type</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuredevops.AwaitableGetPoolResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_azuredevops.AwaitableGetPoolsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azuredevops.</code><code class="sig-name descname">AwaitableGetPoolsResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">agent_pools</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuredevops.AwaitableGetPoolsResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_azuredevops.AwaitableGetProjectResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azuredevops.</code><code class="sig-name descname">AwaitableGetProjectResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">features</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">process_template_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">version_control</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">visibility</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">work_item_template</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuredevops.AwaitableGetProjectResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_azuredevops.AwaitableGetProjectsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azuredevops.</code><code class="sig-name descname">AwaitableGetProjectsResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">projects</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">state</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuredevops.AwaitableGetProjectsResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_azuredevops.AwaitableGetRepositoriesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azuredevops.</code><code class="sig-name descname">AwaitableGetRepositoriesResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">include_hidden</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">repositories</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuredevops.AwaitableGetRepositoriesResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_azuredevops.AwaitableGetUsersResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azuredevops.</code><code class="sig-name descname">AwaitableGetUsersResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">origin</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">origin_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">principal_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">subject_types</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">users</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuredevops.AwaitableGetUsersResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_azuredevops.BranchPolicyAutoReviewers">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azuredevops.</code><code class="sig-name descname">BranchPolicyAutoReviewers</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">blocking</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">settings</span><span class="p">:</span> <span class="n">Union[BranchPolicyAutoReviewersSettingsArgs, Mapping[str, Any], Awaitable[Union[BranchPolicyAutoReviewersSettingsArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuredevops.BranchPolicyAutoReviewers" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages required reviewer policy branch policy within Azure DevOps.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_azuredevops</span> <span class="k">as</span> <span class="nn">azuredevops</span>

<span class="n">project</span> <span class="o">=</span> <span class="n">azuredevops</span><span class="o">.</span><span class="n">Project</span><span class="p">(</span><span class="s2">&quot;project&quot;</span><span class="p">)</span>
<span class="n">git</span> <span class="o">=</span> <span class="n">azuredevops</span><span class="o">.</span><span class="n">Git</span><span class="p">(</span><span class="s2">&quot;git&quot;</span><span class="p">,</span>
    <span class="n">project_id</span><span class="o">=</span><span class="n">project</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">initialization</span><span class="o">=</span><span class="n">azuredevops</span><span class="o">.</span><span class="n">GitInitializationArgs</span><span class="p">(</span>
        <span class="n">init_type</span><span class="o">=</span><span class="s2">&quot;Clean&quot;</span><span class="p">,</span>
    <span class="p">))</span>
<span class="n">user</span> <span class="o">=</span> <span class="n">azuredevops</span><span class="o">.</span><span class="n">User</span><span class="p">(</span><span class="s2">&quot;user&quot;</span><span class="p">,</span>
    <span class="n">principal_name</span><span class="o">=</span><span class="s2">&quot;mail@email.com&quot;</span><span class="p">,</span>
    <span class="n">account_license_type</span><span class="o">=</span><span class="s2">&quot;basic&quot;</span><span class="p">)</span>
<span class="n">branch_policy_auto_reviewers</span> <span class="o">=</span> <span class="n">azuredevops</span><span class="o">.</span><span class="n">BranchPolicyAutoReviewers</span><span class="p">(</span><span class="s2">&quot;branchPolicyAutoReviewers&quot;</span><span class="p">,</span>
    <span class="n">project_id</span><span class="o">=</span><span class="n">project</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">enabled</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="n">blocking</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="n">settings</span><span class="o">=</span><span class="n">azuredevops</span><span class="o">.</span><span class="n">BranchPolicyAutoReviewersSettingsArgs</span><span class="p">(</span>
        <span class="n">auto_reviewer_ids</span><span class="o">=</span><span class="p">[</span><span class="n">user</span><span class="o">.</span><span class="n">id</span><span class="p">],</span>
        <span class="n">submitter_can_vote</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span>
        <span class="n">message</span><span class="o">=</span><span class="s2">&quot;Auto reviewer&quot;</span><span class="p">,</span>
        <span class="n">path_filters</span><span class="o">=</span><span class="p">[</span><span class="s2">&quot;*/src/*.ts&quot;</span><span class="p">],</span>
        <span class="n">scopes</span><span class="o">=</span><span class="p">[</span><span class="n">azuredevops</span><span class="o">.</span><span class="n">BranchPolicyAutoReviewersSettingsScopeArgs</span><span class="p">(</span>
            <span class="n">repository_id</span><span class="o">=</span><span class="n">git</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
            <span class="n">repository_ref</span><span class="o">=</span><span class="n">git</span><span class="o">.</span><span class="n">default_branch</span><span class="p">,</span>
            <span class="n">match_type</span><span class="o">=</span><span class="s2">&quot;Exact&quot;</span><span class="p">,</span>
        <span class="p">)],</span>
    <span class="p">))</span>
</pre></div>
</div>
<ul class="simple">
<li><p><a class="reference external" href="https://docs.microsoft.com/en-us/rest/api/azure/devops/policy/configurations/create?view=azure-devops-rest-5.1">Azure DevOps Service REST API 5.1 - Policy Configurations</a></p></li>
</ul>
<p>Azure DevOps Branch Policies can be imported using the project ID and policy configuration ID</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>$ pulumi import azuredevops:index/branchPolicyAutoReviewers:BranchPolicyAutoReviewers p aa4a9756-8a86-4588-86d7-b3ee2d88b033/60
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>blocking</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – A flag indicating if the policy should be blocking. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – A flag indicating if the policy should be enabled. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the policy will be created.</p></li>
<li><p><strong>settings</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'BranchPolicyAutoReviewersSettingsArgs'</em><em>]</em><em>]</em>) – Configuration for the policy. This block must be defined exactly once.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_azuredevops.BranchPolicyAutoReviewers.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">blocking</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">settings</span><span class="p">:</span> <span class="n">Union[BranchPolicyAutoReviewersSettingsArgs, Mapping[str, Any], Awaitable[Union[BranchPolicyAutoReviewersSettingsArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_azuredevops.branch_policy_auto_reviewers.BranchPolicyAutoReviewers<a class="headerlink" href="#pulumi_azuredevops.BranchPolicyAutoReviewers.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing BranchPolicyAutoReviewers resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>blocking</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – A flag indicating if the policy should be blocking. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – A flag indicating if the policy should be enabled. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the policy will be created.</p></li>
<li><p><strong>settings</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'BranchPolicyAutoReviewersSettingsArgs'</em><em>]</em><em>]</em>) – Configuration for the policy. This block must be defined exactly once.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.BranchPolicyAutoReviewers.blocking">
<em class="property">property </em><code class="sig-name descname">blocking</code><a class="headerlink" href="#pulumi_azuredevops.BranchPolicyAutoReviewers.blocking" title="Permalink to this definition">¶</a></dt>
<dd><p>A flag indicating if the policy should be blocking. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.BranchPolicyAutoReviewers.enabled">
<em class="property">property </em><code class="sig-name descname">enabled</code><a class="headerlink" href="#pulumi_azuredevops.BranchPolicyAutoReviewers.enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>A flag indicating if the policy should be enabled. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.BranchPolicyAutoReviewers.project_id">
<em class="property">property </em><code class="sig-name descname">project_id</code><a class="headerlink" href="#pulumi_azuredevops.BranchPolicyAutoReviewers.project_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the policy will be created.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.BranchPolicyAutoReviewers.settings">
<em class="property">property </em><code class="sig-name descname">settings</code><a class="headerlink" href="#pulumi_azuredevops.BranchPolicyAutoReviewers.settings" title="Permalink to this definition">¶</a></dt>
<dd><p>Configuration for the policy. This block must be defined exactly once.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.BranchPolicyAutoReviewers.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuredevops.BranchPolicyAutoReviewers.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azuredevops.BranchPolicyAutoReviewers.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuredevops.BranchPolicyAutoReviewers.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azuredevops.BranchPolicyBuildValidation">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azuredevops.</code><code class="sig-name descname">BranchPolicyBuildValidation</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">blocking</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">settings</span><span class="p">:</span> <span class="n">Union[BranchPolicyBuildValidationSettingsArgs, Mapping[str, Any], Awaitable[Union[BranchPolicyBuildValidationSettingsArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuredevops.BranchPolicyBuildValidation" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a build validation branch policy within Azure DevOps.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_azuredevops</span> <span class="k">as</span> <span class="nn">azuredevops</span>

<span class="n">project</span> <span class="o">=</span> <span class="n">azuredevops</span><span class="o">.</span><span class="n">Project</span><span class="p">(</span><span class="s2">&quot;project&quot;</span><span class="p">)</span>
<span class="n">git</span> <span class="o">=</span> <span class="n">azuredevops</span><span class="o">.</span><span class="n">Git</span><span class="p">(</span><span class="s2">&quot;git&quot;</span><span class="p">,</span>
    <span class="n">project_id</span><span class="o">=</span><span class="n">project</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">initialization</span><span class="o">=</span><span class="n">azuredevops</span><span class="o">.</span><span class="n">GitInitializationArgs</span><span class="p">(</span>
        <span class="n">init_type</span><span class="o">=</span><span class="s2">&quot;Clean&quot;</span><span class="p">,</span>
    <span class="p">))</span>
<span class="n">build_definition</span> <span class="o">=</span> <span class="n">azuredevops</span><span class="o">.</span><span class="n">BuildDefinition</span><span class="p">(</span><span class="s2">&quot;buildDefinition&quot;</span><span class="p">,</span>
    <span class="n">project_id</span><span class="o">=</span><span class="n">project</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">repository</span><span class="o">=</span><span class="n">azuredevops</span><span class="o">.</span><span class="n">BuildDefinitionRepositoryArgs</span><span class="p">(</span>
        <span class="n">repo_type</span><span class="o">=</span><span class="s2">&quot;TfsGit&quot;</span><span class="p">,</span>
        <span class="n">repo_id</span><span class="o">=</span><span class="n">git</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
        <span class="n">yml_path</span><span class="o">=</span><span class="s2">&quot;azure-pipelines.yml&quot;</span><span class="p">,</span>
    <span class="p">))</span>
<span class="n">branch_policy_build_validation</span> <span class="o">=</span> <span class="n">azuredevops</span><span class="o">.</span><span class="n">BranchPolicyBuildValidation</span><span class="p">(</span><span class="s2">&quot;branchPolicyBuildValidation&quot;</span><span class="p">,</span>
    <span class="n">project_id</span><span class="o">=</span><span class="n">project</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">enabled</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="n">blocking</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="n">settings</span><span class="o">=</span><span class="n">azuredevops</span><span class="o">.</span><span class="n">BranchPolicyBuildValidationSettingsArgs</span><span class="p">(</span>
        <span class="n">display_name</span><span class="o">=</span><span class="s2">&quot;Don&#39;t break the build!&quot;</span><span class="p">,</span>
        <span class="n">build_definition_id</span><span class="o">=</span><span class="n">build_definition</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
        <span class="n">valid_duration</span><span class="o">=</span><span class="mi">720</span><span class="p">,</span>
        <span class="n">filename_patterns</span><span class="o">=</span><span class="p">[</span>
            <span class="s2">&quot;/WebApp/*&quot;</span><span class="p">,</span>
            <span class="s2">&quot;!/WebApp/Tests/*&quot;</span><span class="p">,</span>
            <span class="s2">&quot;*.cs&quot;</span><span class="p">,</span>
        <span class="p">],</span>
        <span class="n">scopes</span><span class="o">=</span><span class="p">[</span>
            <span class="n">azuredevops</span><span class="o">.</span><span class="n">BranchPolicyBuildValidationSettingsScopeArgs</span><span class="p">(</span>
                <span class="n">repository_id</span><span class="o">=</span><span class="n">git</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
                <span class="n">repository_ref</span><span class="o">=</span><span class="n">git</span><span class="o">.</span><span class="n">default_branch</span><span class="p">,</span>
                <span class="n">match_type</span><span class="o">=</span><span class="s2">&quot;Exact&quot;</span><span class="p">,</span>
            <span class="p">),</span>
            <span class="n">azuredevops</span><span class="o">.</span><span class="n">BranchPolicyBuildValidationSettingsScopeArgs</span><span class="p">(</span>
                <span class="n">repository_id</span><span class="o">=</span><span class="n">git</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
                <span class="n">repository_ref</span><span class="o">=</span><span class="s2">&quot;refs/heads/releases&quot;</span><span class="p">,</span>
                <span class="n">match_type</span><span class="o">=</span><span class="s2">&quot;Prefix&quot;</span><span class="p">,</span>
            <span class="p">),</span>
        <span class="p">],</span>
    <span class="p">))</span>
</pre></div>
</div>
<ul class="simple">
<li><p><a class="reference external" href="https://docs.microsoft.com/en-us/rest/api/azure/devops/policy/configurations/create?view=azure-devops-rest-5.1">Azure DevOps Service REST API 5.1 - Policy Configurations</a></p></li>
</ul>
<p>Azure DevOps Branch Policies can be imported using the project ID and policy configuration ID</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>$ pulumi import azuredevops:index/branchPolicyBuildValidation:BranchPolicyBuildValidation p aa4a9756-8a86-4588-86d7-b3ee2d88b033/60
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>blocking</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – A flag indicating if the policy should be blocking. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – A flag indicating if the policy should be enabled. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the policy will be created.</p></li>
<li><p><strong>settings</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'BranchPolicyBuildValidationSettingsArgs'</em><em>]</em><em>]</em>) – Configuration for the policy. This block must be defined exactly once.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_azuredevops.BranchPolicyBuildValidation.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">blocking</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">settings</span><span class="p">:</span> <span class="n">Union[BranchPolicyBuildValidationSettingsArgs, Mapping[str, Any], Awaitable[Union[BranchPolicyBuildValidationSettingsArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_azuredevops.branch_policy_build_validation.BranchPolicyBuildValidation<a class="headerlink" href="#pulumi_azuredevops.BranchPolicyBuildValidation.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing BranchPolicyBuildValidation resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>blocking</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – A flag indicating if the policy should be blocking. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – A flag indicating if the policy should be enabled. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the policy will be created.</p></li>
<li><p><strong>settings</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'BranchPolicyBuildValidationSettingsArgs'</em><em>]</em><em>]</em>) – Configuration for the policy. This block must be defined exactly once.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.BranchPolicyBuildValidation.blocking">
<em class="property">property </em><code class="sig-name descname">blocking</code><a class="headerlink" href="#pulumi_azuredevops.BranchPolicyBuildValidation.blocking" title="Permalink to this definition">¶</a></dt>
<dd><p>A flag indicating if the policy should be blocking. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.BranchPolicyBuildValidation.enabled">
<em class="property">property </em><code class="sig-name descname">enabled</code><a class="headerlink" href="#pulumi_azuredevops.BranchPolicyBuildValidation.enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>A flag indicating if the policy should be enabled. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.BranchPolicyBuildValidation.project_id">
<em class="property">property </em><code class="sig-name descname">project_id</code><a class="headerlink" href="#pulumi_azuredevops.BranchPolicyBuildValidation.project_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the policy will be created.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.BranchPolicyBuildValidation.settings">
<em class="property">property </em><code class="sig-name descname">settings</code><a class="headerlink" href="#pulumi_azuredevops.BranchPolicyBuildValidation.settings" title="Permalink to this definition">¶</a></dt>
<dd><p>Configuration for the policy. This block must be defined exactly once.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.BranchPolicyBuildValidation.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuredevops.BranchPolicyBuildValidation.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azuredevops.BranchPolicyBuildValidation.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuredevops.BranchPolicyBuildValidation.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azuredevops.BranchPolicyCommentResolution">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azuredevops.</code><code class="sig-name descname">BranchPolicyCommentResolution</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">blocking</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">settings</span><span class="p">:</span> <span class="n">Union[BranchPolicyCommentResolutionSettingsArgs, Mapping[str, Any], Awaitable[Union[BranchPolicyCommentResolutionSettingsArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuredevops.BranchPolicyCommentResolution" title="Permalink to this definition">¶</a></dt>
<dd><p>Configure a comment resolution policy for your branch within Azure DevOps project.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_azuredevops</span> <span class="k">as</span> <span class="nn">azuredevops</span>

<span class="n">project</span> <span class="o">=</span> <span class="n">azuredevops</span><span class="o">.</span><span class="n">Project</span><span class="p">(</span><span class="s2">&quot;project&quot;</span><span class="p">)</span>
<span class="n">git</span> <span class="o">=</span> <span class="n">azuredevops</span><span class="o">.</span><span class="n">Git</span><span class="p">(</span><span class="s2">&quot;git&quot;</span><span class="p">,</span>
    <span class="n">project_id</span><span class="o">=</span><span class="n">project</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">initialization</span><span class="o">=</span><span class="n">azuredevops</span><span class="o">.</span><span class="n">GitInitializationArgs</span><span class="p">(</span>
        <span class="n">init_type</span><span class="o">=</span><span class="s2">&quot;Clean&quot;</span><span class="p">,</span>
    <span class="p">))</span>
<span class="n">branch_policy_comment_resolution</span> <span class="o">=</span> <span class="n">azuredevops</span><span class="o">.</span><span class="n">BranchPolicyCommentResolution</span><span class="p">(</span><span class="s2">&quot;branchPolicyCommentResolution&quot;</span><span class="p">,</span>
    <span class="n">project_id</span><span class="o">=</span><span class="n">project</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">enabled</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="n">blocking</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="n">settings</span><span class="o">=</span><span class="n">azuredevops</span><span class="o">.</span><span class="n">BranchPolicyCommentResolutionSettingsArgs</span><span class="p">(</span>
        <span class="n">scopes</span><span class="o">=</span><span class="p">[</span>
            <span class="n">azuredevops</span><span class="o">.</span><span class="n">BranchPolicyCommentResolutionSettingsScopeArgs</span><span class="p">(</span>
                <span class="n">repository_id</span><span class="o">=</span><span class="n">git</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
                <span class="n">repository_ref</span><span class="o">=</span><span class="n">git</span><span class="o">.</span><span class="n">default_branch</span><span class="p">,</span>
                <span class="n">match_type</span><span class="o">=</span><span class="s2">&quot;Exact&quot;</span><span class="p">,</span>
            <span class="p">),</span>
            <span class="n">azuredevops</span><span class="o">.</span><span class="n">BranchPolicyCommentResolutionSettingsScopeArgs</span><span class="p">(</span>
                <span class="n">repository_id</span><span class="o">=</span><span class="n">git</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
                <span class="n">repository_ref</span><span class="o">=</span><span class="s2">&quot;refs/heads/releases&quot;</span><span class="p">,</span>
                <span class="n">match_type</span><span class="o">=</span><span class="s2">&quot;Prefix&quot;</span><span class="p">,</span>
            <span class="p">),</span>
        <span class="p">],</span>
    <span class="p">))</span>
</pre></div>
</div>
<ul class="simple">
<li><p><a class="reference external" href="https://docs.microsoft.com/en-us/rest/api/azure/devops/policy/configurations/create?view=azure-devops-rest-5.1">Azure DevOps Service REST API 5.1 - Policy Configurations</a></p></li>
</ul>
<p>Azure DevOps Branch Policies can be imported using the project ID and policy configuration ID</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>$ pulumi import azuredevops:index/branchPolicyCommentResolution:BranchPolicyCommentResolution p <span class="m">00000000</span>-0000-0000-0000-000000000000/0
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>blocking</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – A flag indicating if the policy should be blocking. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – A flag indicating if the policy should be enabled. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the policy will be created.</p></li>
<li><p><strong>settings</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'BranchPolicyCommentResolutionSettingsArgs'</em><em>]</em><em>]</em>) – Configuration for the policy. This block must be defined exactly once.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_azuredevops.BranchPolicyCommentResolution.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">blocking</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">settings</span><span class="p">:</span> <span class="n">Union[BranchPolicyCommentResolutionSettingsArgs, Mapping[str, Any], Awaitable[Union[BranchPolicyCommentResolutionSettingsArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_azuredevops.branch_policy_comment_resolution.BranchPolicyCommentResolution<a class="headerlink" href="#pulumi_azuredevops.BranchPolicyCommentResolution.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing BranchPolicyCommentResolution resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>blocking</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – A flag indicating if the policy should be blocking. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – A flag indicating if the policy should be enabled. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the policy will be created.</p></li>
<li><p><strong>settings</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'BranchPolicyCommentResolutionSettingsArgs'</em><em>]</em><em>]</em>) – Configuration for the policy. This block must be defined exactly once.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.BranchPolicyCommentResolution.blocking">
<em class="property">property </em><code class="sig-name descname">blocking</code><a class="headerlink" href="#pulumi_azuredevops.BranchPolicyCommentResolution.blocking" title="Permalink to this definition">¶</a></dt>
<dd><p>A flag indicating if the policy should be blocking. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.BranchPolicyCommentResolution.enabled">
<em class="property">property </em><code class="sig-name descname">enabled</code><a class="headerlink" href="#pulumi_azuredevops.BranchPolicyCommentResolution.enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>A flag indicating if the policy should be enabled. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.BranchPolicyCommentResolution.project_id">
<em class="property">property </em><code class="sig-name descname">project_id</code><a class="headerlink" href="#pulumi_azuredevops.BranchPolicyCommentResolution.project_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the policy will be created.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.BranchPolicyCommentResolution.settings">
<em class="property">property </em><code class="sig-name descname">settings</code><a class="headerlink" href="#pulumi_azuredevops.BranchPolicyCommentResolution.settings" title="Permalink to this definition">¶</a></dt>
<dd><p>Configuration for the policy. This block must be defined exactly once.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.BranchPolicyCommentResolution.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuredevops.BranchPolicyCommentResolution.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azuredevops.BranchPolicyCommentResolution.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuredevops.BranchPolicyCommentResolution.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azuredevops.BranchPolicyMinReviewers">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azuredevops.</code><code class="sig-name descname">BranchPolicyMinReviewers</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">blocking</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">settings</span><span class="p">:</span> <span class="n">Union[BranchPolicyMinReviewersSettingsArgs, Mapping[str, Any], Awaitable[Union[BranchPolicyMinReviewersSettingsArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuredevops.BranchPolicyMinReviewers" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a minimum reviewer branch policy within Azure DevOps.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_azuredevops</span> <span class="k">as</span> <span class="nn">azuredevops</span>

<span class="n">project</span> <span class="o">=</span> <span class="n">azuredevops</span><span class="o">.</span><span class="n">Project</span><span class="p">(</span><span class="s2">&quot;project&quot;</span><span class="p">)</span>
<span class="n">git</span> <span class="o">=</span> <span class="n">azuredevops</span><span class="o">.</span><span class="n">Git</span><span class="p">(</span><span class="s2">&quot;git&quot;</span><span class="p">,</span>
    <span class="n">project_id</span><span class="o">=</span><span class="n">project</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">initialization</span><span class="o">=</span><span class="n">azuredevops</span><span class="o">.</span><span class="n">GitInitializationArgs</span><span class="p">(</span>
        <span class="n">init_type</span><span class="o">=</span><span class="s2">&quot;Clean&quot;</span><span class="p">,</span>
    <span class="p">))</span>
<span class="n">branch_policy_min_reviewers</span> <span class="o">=</span> <span class="n">azuredevops</span><span class="o">.</span><span class="n">BranchPolicyMinReviewers</span><span class="p">(</span><span class="s2">&quot;branchPolicyMinReviewers&quot;</span><span class="p">,</span>
    <span class="n">project_id</span><span class="o">=</span><span class="n">project</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">enabled</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="n">blocking</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="n">settings</span><span class="o">=</span><span class="n">azuredevops</span><span class="o">.</span><span class="n">BranchPolicyMinReviewersSettingsArgs</span><span class="p">(</span>
        <span class="n">reviewer_count</span><span class="o">=</span><span class="mi">2</span><span class="p">,</span>
        <span class="n">submitter_can_vote</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span>
        <span class="n">scopes</span><span class="o">=</span><span class="p">[</span>
            <span class="n">azuredevops</span><span class="o">.</span><span class="n">BranchPolicyMinReviewersSettingsScopeArgs</span><span class="p">(</span>
                <span class="n">repository_id</span><span class="o">=</span><span class="n">git</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
                <span class="n">repository_ref</span><span class="o">=</span><span class="n">git</span><span class="o">.</span><span class="n">default_branch</span><span class="p">,</span>
                <span class="n">match_type</span><span class="o">=</span><span class="s2">&quot;Exact&quot;</span><span class="p">,</span>
            <span class="p">),</span>
            <span class="n">azuredevops</span><span class="o">.</span><span class="n">BranchPolicyMinReviewersSettingsScopeArgs</span><span class="p">(</span>
                <span class="n">repository_id</span><span class="o">=</span><span class="n">git</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
                <span class="n">repository_ref</span><span class="o">=</span><span class="s2">&quot;refs/heads/releases&quot;</span><span class="p">,</span>
                <span class="n">match_type</span><span class="o">=</span><span class="s2">&quot;Prefix&quot;</span><span class="p">,</span>
            <span class="p">),</span>
        <span class="p">],</span>
    <span class="p">))</span>
</pre></div>
</div>
<ul class="simple">
<li><p><a class="reference external" href="https://docs.microsoft.com/en-us/rest/api/azure/devops/policy/configurations/create?view=azure-devops-rest-5.1">Azure DevOps Service REST API 5.1 - Policy Configurations</a></p></li>
</ul>
<p>Azure DevOps Branch Policies can be imported using the project ID and policy configuration ID</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>$ pulumi import azuredevops:index/branchPolicyMinReviewers:BranchPolicyMinReviewers p aa4a9756-8a86-4588-86d7-b3ee2d88b033/60
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>blocking</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – A flag indicating if the policy should be blocking. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – A flag indicating if the policy should be enabled. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the policy will be created.</p></li>
<li><p><strong>settings</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'BranchPolicyMinReviewersSettingsArgs'</em><em>]</em><em>]</em>) – Configuration for the policy. This block must be defined exactly once.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_azuredevops.BranchPolicyMinReviewers.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">blocking</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">settings</span><span class="p">:</span> <span class="n">Union[BranchPolicyMinReviewersSettingsArgs, Mapping[str, Any], Awaitable[Union[BranchPolicyMinReviewersSettingsArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_azuredevops.branch_policy_min_reviewers.BranchPolicyMinReviewers<a class="headerlink" href="#pulumi_azuredevops.BranchPolicyMinReviewers.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing BranchPolicyMinReviewers resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>blocking</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – A flag indicating if the policy should be blocking. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – A flag indicating if the policy should be enabled. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the policy will be created.</p></li>
<li><p><strong>settings</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'BranchPolicyMinReviewersSettingsArgs'</em><em>]</em><em>]</em>) – Configuration for the policy. This block must be defined exactly once.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.BranchPolicyMinReviewers.blocking">
<em class="property">property </em><code class="sig-name descname">blocking</code><a class="headerlink" href="#pulumi_azuredevops.BranchPolicyMinReviewers.blocking" title="Permalink to this definition">¶</a></dt>
<dd><p>A flag indicating if the policy should be blocking. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.BranchPolicyMinReviewers.enabled">
<em class="property">property </em><code class="sig-name descname">enabled</code><a class="headerlink" href="#pulumi_azuredevops.BranchPolicyMinReviewers.enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>A flag indicating if the policy should be enabled. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.BranchPolicyMinReviewers.project_id">
<em class="property">property </em><code class="sig-name descname">project_id</code><a class="headerlink" href="#pulumi_azuredevops.BranchPolicyMinReviewers.project_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the policy will be created.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.BranchPolicyMinReviewers.settings">
<em class="property">property </em><code class="sig-name descname">settings</code><a class="headerlink" href="#pulumi_azuredevops.BranchPolicyMinReviewers.settings" title="Permalink to this definition">¶</a></dt>
<dd><p>Configuration for the policy. This block must be defined exactly once.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.BranchPolicyMinReviewers.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuredevops.BranchPolicyMinReviewers.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azuredevops.BranchPolicyMinReviewers.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuredevops.BranchPolicyMinReviewers.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azuredevops.BranchPolicyWorkItemLinking">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azuredevops.</code><code class="sig-name descname">BranchPolicyWorkItemLinking</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">blocking</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">settings</span><span class="p">:</span> <span class="n">Union[BranchPolicyWorkItemLinkingSettingsArgs, Mapping[str, Any], Awaitable[Union[BranchPolicyWorkItemLinkingSettingsArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuredevops.BranchPolicyWorkItemLinking" title="Permalink to this definition">¶</a></dt>
<dd><p>Require associations between branches and a work item within Azure DevOps.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_azuredevops</span> <span class="k">as</span> <span class="nn">azuredevops</span>

<span class="n">project</span> <span class="o">=</span> <span class="n">azuredevops</span><span class="o">.</span><span class="n">Project</span><span class="p">(</span><span class="s2">&quot;project&quot;</span><span class="p">)</span>
<span class="n">git</span> <span class="o">=</span> <span class="n">azuredevops</span><span class="o">.</span><span class="n">Git</span><span class="p">(</span><span class="s2">&quot;git&quot;</span><span class="p">,</span>
    <span class="n">project_id</span><span class="o">=</span><span class="n">project</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">initialization</span><span class="o">=</span><span class="n">azuredevops</span><span class="o">.</span><span class="n">GitInitializationArgs</span><span class="p">(</span>
        <span class="n">init_type</span><span class="o">=</span><span class="s2">&quot;Clean&quot;</span><span class="p">,</span>
    <span class="p">))</span>
<span class="n">branch_policy_work_item_linking</span> <span class="o">=</span> <span class="n">azuredevops</span><span class="o">.</span><span class="n">BranchPolicyWorkItemLinking</span><span class="p">(</span><span class="s2">&quot;branchPolicyWorkItemLinking&quot;</span><span class="p">,</span>
    <span class="n">project_id</span><span class="o">=</span><span class="n">project</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">enabled</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="n">blocking</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="n">settings</span><span class="o">=</span><span class="n">azuredevops</span><span class="o">.</span><span class="n">BranchPolicyWorkItemLinkingSettingsArgs</span><span class="p">(</span>
        <span class="n">scopes</span><span class="o">=</span><span class="p">[</span>
            <span class="n">azuredevops</span><span class="o">.</span><span class="n">BranchPolicyWorkItemLinkingSettingsScopeArgs</span><span class="p">(</span>
                <span class="n">repository_id</span><span class="o">=</span><span class="n">git</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
                <span class="n">repository_ref</span><span class="o">=</span><span class="n">git</span><span class="o">.</span><span class="n">default_branch</span><span class="p">,</span>
                <span class="n">match_type</span><span class="o">=</span><span class="s2">&quot;Exact&quot;</span><span class="p">,</span>
            <span class="p">),</span>
            <span class="n">azuredevops</span><span class="o">.</span><span class="n">BranchPolicyWorkItemLinkingSettingsScopeArgs</span><span class="p">(</span>
                <span class="n">repository_id</span><span class="o">=</span><span class="n">git</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
                <span class="n">repository_ref</span><span class="o">=</span><span class="s2">&quot;refs/heads/releases&quot;</span><span class="p">,</span>
                <span class="n">match_type</span><span class="o">=</span><span class="s2">&quot;Prefix&quot;</span><span class="p">,</span>
            <span class="p">),</span>
        <span class="p">],</span>
    <span class="p">))</span>
</pre></div>
</div>
<ul class="simple">
<li><p><a class="reference external" href="https://docs.microsoft.com/en-us/rest/api/azure/devops/policy/configurations/create?view=azure-devops-rest-5.1">Azure DevOps Service REST API 5.1 - Policy Configurations</a></p></li>
</ul>
<p>Azure DevOps Branch Policies can be imported using the project ID and policy configuration ID</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>$ pulumi import azuredevops:index/branchPolicyWorkItemLinking:BranchPolicyWorkItemLinking p <span class="m">00000000</span>-0000-0000-0000-000000000000/0
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>blocking</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – A flag indicating if the policy should be blocking. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – A flag indicating if the policy should be enabled. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the policy will be created.</p></li>
<li><p><strong>settings</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'BranchPolicyWorkItemLinkingSettingsArgs'</em><em>]</em><em>]</em>) – Configuration for the policy. This block must be defined exactly once.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_azuredevops.BranchPolicyWorkItemLinking.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">blocking</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">settings</span><span class="p">:</span> <span class="n">Union[BranchPolicyWorkItemLinkingSettingsArgs, Mapping[str, Any], Awaitable[Union[BranchPolicyWorkItemLinkingSettingsArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_azuredevops.branch_policy_work_item_linking.BranchPolicyWorkItemLinking<a class="headerlink" href="#pulumi_azuredevops.BranchPolicyWorkItemLinking.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing BranchPolicyWorkItemLinking resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>blocking</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – A flag indicating if the policy should be blocking. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – A flag indicating if the policy should be enabled. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the policy will be created.</p></li>
<li><p><strong>settings</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'BranchPolicyWorkItemLinkingSettingsArgs'</em><em>]</em><em>]</em>) – Configuration for the policy. This block must be defined exactly once.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.BranchPolicyWorkItemLinking.blocking">
<em class="property">property </em><code class="sig-name descname">blocking</code><a class="headerlink" href="#pulumi_azuredevops.BranchPolicyWorkItemLinking.blocking" title="Permalink to this definition">¶</a></dt>
<dd><p>A flag indicating if the policy should be blocking. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.BranchPolicyWorkItemLinking.enabled">
<em class="property">property </em><code class="sig-name descname">enabled</code><a class="headerlink" href="#pulumi_azuredevops.BranchPolicyWorkItemLinking.enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>A flag indicating if the policy should be enabled. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.BranchPolicyWorkItemLinking.project_id">
<em class="property">property </em><code class="sig-name descname">project_id</code><a class="headerlink" href="#pulumi_azuredevops.BranchPolicyWorkItemLinking.project_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the policy will be created.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.BranchPolicyWorkItemLinking.settings">
<em class="property">property </em><code class="sig-name descname">settings</code><a class="headerlink" href="#pulumi_azuredevops.BranchPolicyWorkItemLinking.settings" title="Permalink to this definition">¶</a></dt>
<dd><p>Configuration for the policy. This block must be defined exactly once.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.BranchPolicyWorkItemLinking.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuredevops.BranchPolicyWorkItemLinking.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azuredevops.BranchPolicyWorkItemLinking.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuredevops.BranchPolicyWorkItemLinking.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azuredevops.BuildDefinition">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azuredevops.</code><code class="sig-name descname">BuildDefinition</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">agent_pool_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ci_trigger</span><span class="p">:</span> <span class="n">Union[BuildDefinitionCiTriggerArgs, Mapping[str, Any], Awaitable[Union[BuildDefinitionCiTriggerArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">path</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">pull_request_trigger</span><span class="p">:</span> <span class="n">Union[BuildDefinitionPullRequestTriggerArgs, Mapping[str, Any], Awaitable[Union[BuildDefinitionPullRequestTriggerArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">repository</span><span class="p">:</span> <span class="n">Union[BuildDefinitionRepositoryArgs, Mapping[str, Any], Awaitable[Union[BuildDefinitionRepositoryArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">variable_groups</span><span class="p">:</span> <span class="n">Union[Sequence[Union[int, Awaitable[int], Output[T]]], Awaitable[Sequence[Union[int, Awaitable[int], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">variables</span><span class="p">:</span> <span class="n">Union[Sequence[Union[BuildDefinitionVariableArgs, Mapping[str, Any], Awaitable[Union[BuildDefinitionVariableArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[BuildDefinitionVariableArgs, Mapping[str, Any], Awaitable[Union[BuildDefinitionVariableArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuredevops.BuildDefinition" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Build Definition within Azure DevOps.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_azuredevops</span> <span class="k">as</span> <span class="nn">azuredevops</span>

<span class="n">project</span> <span class="o">=</span> <span class="n">azuredevops</span><span class="o">.</span><span class="n">Project</span><span class="p">(</span><span class="s2">&quot;project&quot;</span><span class="p">,</span>
    <span class="n">visibility</span><span class="o">=</span><span class="s2">&quot;private&quot;</span><span class="p">,</span>
    <span class="n">version_control</span><span class="o">=</span><span class="s2">&quot;Git&quot;</span><span class="p">,</span>
    <span class="n">work_item_template</span><span class="o">=</span><span class="s2">&quot;Agile&quot;</span><span class="p">)</span>
<span class="n">repository</span> <span class="o">=</span> <span class="n">azuredevops</span><span class="o">.</span><span class="n">Git</span><span class="p">(</span><span class="s2">&quot;repository&quot;</span><span class="p">,</span>
    <span class="n">project_id</span><span class="o">=</span><span class="n">project</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">initialization</span><span class="o">=</span><span class="n">azuredevops</span><span class="o">.</span><span class="n">GitInitializationArgs</span><span class="p">(</span>
        <span class="n">init_type</span><span class="o">=</span><span class="s2">&quot;Clean&quot;</span><span class="p">,</span>
    <span class="p">))</span>
<span class="nb">vars</span> <span class="o">=</span> <span class="n">azuredevops</span><span class="o">.</span><span class="n">VariableGroup</span><span class="p">(</span><span class="s2">&quot;vars&quot;</span><span class="p">,</span>
    <span class="n">project_id</span><span class="o">=</span><span class="n">project</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">description</span><span class="o">=</span><span class="s2">&quot;Managed by Terraform&quot;</span><span class="p">,</span>
    <span class="n">allow_access</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="n">variables</span><span class="o">=</span><span class="p">[</span><span class="n">azuredevops</span><span class="o">.</span><span class="n">VariableGroupVariableArgs</span><span class="p">(</span>
        <span class="n">name</span><span class="o">=</span><span class="s2">&quot;FOO&quot;</span><span class="p">,</span>
        <span class="n">value</span><span class="o">=</span><span class="s2">&quot;BAR&quot;</span><span class="p">,</span>
    <span class="p">)])</span>
<span class="n">build</span> <span class="o">=</span> <span class="n">azuredevops</span><span class="o">.</span><span class="n">BuildDefinition</span><span class="p">(</span><span class="s2">&quot;build&quot;</span><span class="p">,</span>
    <span class="n">project_id</span><span class="o">=</span><span class="n">project</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">path</span><span class="o">=</span><span class="s2">&quot;\ExampleFolder&quot;</span><span class="p">,</span>
    <span class="n">ci_trigger</span><span class="o">=</span><span class="n">azuredevops</span><span class="o">.</span><span class="n">BuildDefinitionCiTriggerArgs</span><span class="p">(</span>
        <span class="n">use_yaml</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="p">),</span>
    <span class="n">repository</span><span class="o">=</span><span class="n">azuredevops</span><span class="o">.</span><span class="n">BuildDefinitionRepositoryArgs</span><span class="p">(</span>
        <span class="n">repo_type</span><span class="o">=</span><span class="s2">&quot;TfsGit&quot;</span><span class="p">,</span>
        <span class="n">repo_id</span><span class="o">=</span><span class="n">repository</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
        <span class="n">branch_name</span><span class="o">=</span><span class="n">repository</span><span class="o">.</span><span class="n">default_branch</span><span class="p">,</span>
        <span class="n">yml_path</span><span class="o">=</span><span class="s2">&quot;azure-pipelines.yml&quot;</span><span class="p">,</span>
    <span class="p">),</span>
    <span class="n">variable_groups</span><span class="o">=</span><span class="p">[</span><span class="nb">vars</span><span class="o">.</span><span class="n">id</span><span class="p">],</span>
    <span class="n">variables</span><span class="o">=</span><span class="p">[</span>
        <span class="n">azuredevops</span><span class="o">.</span><span class="n">BuildDefinitionVariableArgs</span><span class="p">(</span>
            <span class="n">name</span><span class="o">=</span><span class="s2">&quot;PipelineVariable&quot;</span><span class="p">,</span>
            <span class="n">value</span><span class="o">=</span><span class="s2">&quot;Go Microsoft!&quot;</span><span class="p">,</span>
        <span class="p">),</span>
        <span class="n">azuredevops</span><span class="o">.</span><span class="n">BuildDefinitionVariableArgs</span><span class="p">(</span>
            <span class="n">name</span><span class="o">=</span><span class="s2">&quot;PipelineSecret&quot;</span><span class="p">,</span>
            <span class="n">secret_value</span><span class="o">=</span><span class="s2">&quot;ZGV2cw&quot;</span><span class="p">,</span>
            <span class="n">is_secret</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
        <span class="p">),</span>
    <span class="p">])</span>
</pre></div>
</div>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_azuredevops</span> <span class="k">as</span> <span class="nn">azuredevops</span>

<span class="n">sample_dotnetcore_app_release</span> <span class="o">=</span> <span class="n">azuredevops</span><span class="o">.</span><span class="n">BuildDefinition</span><span class="p">(</span><span class="s2">&quot;sampleDotnetcoreAppRelease&quot;</span><span class="p">,</span>
    <span class="n">project_id</span><span class="o">=</span><span class="n">azuredevops_project</span><span class="p">[</span><span class="s2">&quot;project&quot;</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">],</span>
    <span class="n">path</span><span class="o">=</span><span class="s2">&quot;\ExampleFolder&quot;</span><span class="p">,</span>
    <span class="n">ci_trigger</span><span class="o">=</span><span class="n">azuredevops</span><span class="o">.</span><span class="n">BuildDefinitionCiTriggerArgs</span><span class="p">(</span>
        <span class="n">use_yaml</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="p">),</span>
    <span class="n">repository</span><span class="o">=</span><span class="n">azuredevops</span><span class="o">.</span><span class="n">BuildDefinitionRepositoryArgs</span><span class="p">(</span>
        <span class="n">repo_type</span><span class="o">=</span><span class="s2">&quot;GitHubEnterprise&quot;</span><span class="p">,</span>
        <span class="n">repo_id</span><span class="o">=</span><span class="s2">&quot;&lt;GitHub Org&gt;/&lt;Repo Name&gt;&quot;</span><span class="p">,</span>
        <span class="n">github_enterprise_url</span><span class="o">=</span><span class="s2">&quot;https://github.company.com&quot;</span><span class="p">,</span>
        <span class="n">branch_name</span><span class="o">=</span><span class="s2">&quot;master&quot;</span><span class="p">,</span>
        <span class="n">yml_path</span><span class="o">=</span><span class="s2">&quot;azure-pipelines.yml&quot;</span><span class="p">,</span>
        <span class="n">service_connection_id</span><span class="o">=</span><span class="s2">&quot;...&quot;</span><span class="p">,</span>
    <span class="p">))</span>
</pre></div>
</div>
<ul class="simple">
<li><p><a class="reference external" href="https://docs.microsoft.com/en-us/rest/api/azure/devops/build/definitions?view=azure-devops-rest-5.1">Azure DevOps Service REST API 5.1 - Build Definitions</a></p></li>
</ul>
<p>Azure DevOps Build Definitions can be imported using the project name/definitions Id or by the project Guid/definitions Id, e.g.</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>   $ pulumi import azuredevops:index/buildDefinition:BuildDefinition build <span class="s2">&quot;Test Project&quot;</span>/10

or
</pre></div>
</div>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>$ pulumi import azuredevops:index/buildDefinition:BuildDefinition build <span class="m">00000000</span>-0000-0000-0000-000000000000/0
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>agent_pool_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The agent pool that should execute the build.</p></li>
<li><p><strong>ci_trigger</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'BuildDefinitionCiTriggerArgs'</em><em>]</em><em>]</em>) – Continuous Integration trigger.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the build definition.</p></li>
<li><p><strong>path</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The folder path of the build definition.</p></li>
<li><p><strong>project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The project ID or project name.</p></li>
<li><p><strong>pull_request_trigger</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'BuildDefinitionPullRequestTriggerArgs'</em><em>]</em><em>]</em>) – Pull Request Integration Integration trigger.</p></li>
<li><p><strong>repository</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'BuildDefinitionRepositoryArgs'</em><em>]</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">repository</span></code> block as documented below.</p></li>
<li><p><strong>variable_groups</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>int</em><em>]</em><em>]</em><em>]</em>) – A list of variable group IDs (integers) to link to the build definition.</p></li>
<li><p><strong>variables</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'BuildDefinitionVariableArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – A list of <code class="docutils literal notranslate"><span class="pre">variable</span></code> blocks, as documented below.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_azuredevops.BuildDefinition.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">agent_pool_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ci_trigger</span><span class="p">:</span> <span class="n">Union[BuildDefinitionCiTriggerArgs, Mapping[str, Any], Awaitable[Union[BuildDefinitionCiTriggerArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">path</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">pull_request_trigger</span><span class="p">:</span> <span class="n">Union[BuildDefinitionPullRequestTriggerArgs, Mapping[str, Any], Awaitable[Union[BuildDefinitionPullRequestTriggerArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">repository</span><span class="p">:</span> <span class="n">Union[BuildDefinitionRepositoryArgs, Mapping[str, Any], Awaitable[Union[BuildDefinitionRepositoryArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">revision</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">variable_groups</span><span class="p">:</span> <span class="n">Union[Sequence[Union[int, Awaitable[int], Output[T]]], Awaitable[Sequence[Union[int, Awaitable[int], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">variables</span><span class="p">:</span> <span class="n">Union[Sequence[Union[BuildDefinitionVariableArgs, Mapping[str, Any], Awaitable[Union[BuildDefinitionVariableArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[BuildDefinitionVariableArgs, Mapping[str, Any], Awaitable[Union[BuildDefinitionVariableArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_azuredevops.build_definition.BuildDefinition<a class="headerlink" href="#pulumi_azuredevops.BuildDefinition.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing BuildDefinition resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>agent_pool_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The agent pool that should execute the build.</p></li>
<li><p><strong>ci_trigger</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'BuildDefinitionCiTriggerArgs'</em><em>]</em><em>]</em>) – Continuous Integration trigger.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the build definition.</p></li>
<li><p><strong>path</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The folder path of the build definition.</p></li>
<li><p><strong>project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The project ID or project name.</p></li>
<li><p><strong>pull_request_trigger</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'BuildDefinitionPullRequestTriggerArgs'</em><em>]</em><em>]</em>) – Pull Request Integration Integration trigger.</p></li>
<li><p><strong>repository</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'BuildDefinitionRepositoryArgs'</em><em>]</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">repository</span></code> block as documented below.</p></li>
<li><p><strong>revision</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The revision of the build definition</p></li>
<li><p><strong>variable_groups</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>int</em><em>]</em><em>]</em><em>]</em>) – A list of variable group IDs (integers) to link to the build definition.</p></li>
<li><p><strong>variables</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'BuildDefinitionVariableArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – A list of <code class="docutils literal notranslate"><span class="pre">variable</span></code> blocks, as documented below.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.BuildDefinition.agent_pool_name">
<em class="property">property </em><code class="sig-name descname">agent_pool_name</code><a class="headerlink" href="#pulumi_azuredevops.BuildDefinition.agent_pool_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The agent pool that should execute the build.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.BuildDefinition.ci_trigger">
<em class="property">property </em><code class="sig-name descname">ci_trigger</code><a class="headerlink" href="#pulumi_azuredevops.BuildDefinition.ci_trigger" title="Permalink to this definition">¶</a></dt>
<dd><p>Continuous Integration trigger.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.BuildDefinition.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_azuredevops.BuildDefinition.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the build definition.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.BuildDefinition.path">
<em class="property">property </em><code class="sig-name descname">path</code><a class="headerlink" href="#pulumi_azuredevops.BuildDefinition.path" title="Permalink to this definition">¶</a></dt>
<dd><p>The folder path of the build definition.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.BuildDefinition.project_id">
<em class="property">property </em><code class="sig-name descname">project_id</code><a class="headerlink" href="#pulumi_azuredevops.BuildDefinition.project_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The project ID or project name.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.BuildDefinition.pull_request_trigger">
<em class="property">property </em><code class="sig-name descname">pull_request_trigger</code><a class="headerlink" href="#pulumi_azuredevops.BuildDefinition.pull_request_trigger" title="Permalink to this definition">¶</a></dt>
<dd><p>Pull Request Integration Integration trigger.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.BuildDefinition.repository">
<em class="property">property </em><code class="sig-name descname">repository</code><a class="headerlink" href="#pulumi_azuredevops.BuildDefinition.repository" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">repository</span></code> block as documented below.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.BuildDefinition.revision">
<em class="property">property </em><code class="sig-name descname">revision</code><a class="headerlink" href="#pulumi_azuredevops.BuildDefinition.revision" title="Permalink to this definition">¶</a></dt>
<dd><p>The revision of the build definition</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.BuildDefinition.variable_groups">
<em class="property">property </em><code class="sig-name descname">variable_groups</code><a class="headerlink" href="#pulumi_azuredevops.BuildDefinition.variable_groups" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of variable group IDs (integers) to link to the build definition.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.BuildDefinition.variables">
<em class="property">property </em><code class="sig-name descname">variables</code><a class="headerlink" href="#pulumi_azuredevops.BuildDefinition.variables" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of <code class="docutils literal notranslate"><span class="pre">variable</span></code> blocks, as documented below.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.BuildDefinition.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuredevops.BuildDefinition.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azuredevops.BuildDefinition.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuredevops.BuildDefinition.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azuredevops.GetAgentQueueResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azuredevops.</code><code class="sig-name descname">GetAgentQueueResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">agent_pool_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuredevops.GetAgentQueueResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getAgentQueue.</p>
<dl class="py method">
<dt id="pulumi_azuredevops.GetAgentQueueResult.agent_pool_id">
<em class="property">property </em><code class="sig-name descname">agent_pool_id</code><a class="headerlink" href="#pulumi_azuredevops.GetAgentQueueResult.agent_pool_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Agent pool identifier to which the agent queue belongs.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.GetAgentQueueResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_azuredevops.GetAgentQueueResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.GetAgentQueueResult.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_azuredevops.GetAgentQueueResult.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the agent queue.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.GetAgentQueueResult.project_id">
<em class="property">property </em><code class="sig-name descname">project_id</code><a class="headerlink" href="#pulumi_azuredevops.GetAgentQueueResult.project_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Project identifier to which the agent queue belongs.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_azuredevops.GetAreaResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azuredevops.</code><code class="sig-name descname">GetAreaResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">childrens</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">fetch_children</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">has_children</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">path</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuredevops.GetAreaResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getArea.</p>
<dl class="py method">
<dt id="pulumi_azuredevops.GetAreaResult.childrens">
<em class="property">property </em><code class="sig-name descname">childrens</code><a class="headerlink" href="#pulumi_azuredevops.GetAreaResult.childrens" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of <code class="docutils literal notranslate"><span class="pre">children</span></code> blocks as defined below, empty if <code class="docutils literal notranslate"><span class="pre">has_children</span> <span class="pre">==</span> <span class="pre">false</span></code></p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.GetAreaResult.has_children">
<em class="property">property </em><code class="sig-name descname">has_children</code><a class="headerlink" href="#pulumi_azuredevops.GetAreaResult.has_children" title="Permalink to this definition">¶</a></dt>
<dd><p>Indicator if the child Area node has child nodes</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.GetAreaResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_azuredevops.GetAreaResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.GetAreaResult.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_azuredevops.GetAreaResult.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the child Area node</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.GetAreaResult.path">
<em class="property">property </em><code class="sig-name descname">path</code><a class="headerlink" href="#pulumi_azuredevops.GetAreaResult.path" title="Permalink to this definition">¶</a></dt>
<dd><p>The complete path (in relative URL format) of the child Area</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.GetAreaResult.project_id">
<em class="property">property </em><code class="sig-name descname">project_id</code><a class="headerlink" href="#pulumi_azuredevops.GetAreaResult.project_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The project ID of the child Area node</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_azuredevops.GetClientConfigResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azuredevops.</code><code class="sig-name descname">GetClientConfigResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">organization_url</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuredevops.GetClientConfigResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getClientConfig.</p>
<dl class="py method">
<dt id="pulumi_azuredevops.GetClientConfigResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_azuredevops.GetClientConfigResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_azuredevops.GetGitRepositoryResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azuredevops.</code><code class="sig-name descname">GetGitRepositoryResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">default_branch</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">is_fork</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">remote_url</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">size</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ssh_url</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">url</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">web_url</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuredevops.GetGitRepositoryResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getGitRepository.</p>
<dl class="py method">
<dt id="pulumi_azuredevops.GetGitRepositoryResult.default_branch">
<em class="property">property </em><code class="sig-name descname">default_branch</code><a class="headerlink" href="#pulumi_azuredevops.GetGitRepositoryResult.default_branch" title="Permalink to this definition">¶</a></dt>
<dd><p>The ref of the default branch.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.GetGitRepositoryResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_azuredevops.GetGitRepositoryResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.GetGitRepositoryResult.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_azuredevops.GetGitRepositoryResult.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Git repository name.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.GetGitRepositoryResult.project_id">
<em class="property">property </em><code class="sig-name descname">project_id</code><a class="headerlink" href="#pulumi_azuredevops.GetGitRepositoryResult.project_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Project identifier to which the Git repository belongs.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.GetGitRepositoryResult.remote_url">
<em class="property">property </em><code class="sig-name descname">remote_url</code><a class="headerlink" href="#pulumi_azuredevops.GetGitRepositoryResult.remote_url" title="Permalink to this definition">¶</a></dt>
<dd><p>HTTPS Url to clone the Git repository</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.GetGitRepositoryResult.size">
<em class="property">property </em><code class="sig-name descname">size</code><a class="headerlink" href="#pulumi_azuredevops.GetGitRepositoryResult.size" title="Permalink to this definition">¶</a></dt>
<dd><p>Compressed size (bytes) of the repository.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.GetGitRepositoryResult.ssh_url">
<em class="property">property </em><code class="sig-name descname">ssh_url</code><a class="headerlink" href="#pulumi_azuredevops.GetGitRepositoryResult.ssh_url" title="Permalink to this definition">¶</a></dt>
<dd><p>SSH Url to clone the Git repository</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.GetGitRepositoryResult.url">
<em class="property">property </em><code class="sig-name descname">url</code><a class="headerlink" href="#pulumi_azuredevops.GetGitRepositoryResult.url" title="Permalink to this definition">¶</a></dt>
<dd><p>Details REST API endpoint for the Git Repository.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.GetGitRepositoryResult.web_url">
<em class="property">property </em><code class="sig-name descname">web_url</code><a class="headerlink" href="#pulumi_azuredevops.GetGitRepositoryResult.web_url" title="Permalink to this definition">¶</a></dt>
<dd><p>Url of the Git repository web view</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_azuredevops.GetGroupResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azuredevops.</code><code class="sig-name descname">GetGroupResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">descriptor</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">origin</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">origin_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuredevops.GetGroupResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getGroup.</p>
<dl class="py method">
<dt id="pulumi_azuredevops.GetGroupResult.descriptor">
<em class="property">property </em><code class="sig-name descname">descriptor</code><a class="headerlink" href="#pulumi_azuredevops.GetGroupResult.descriptor" title="Permalink to this definition">¶</a></dt>
<dd><p>The Descriptor is the primary way to reference the graph subject. This field will uniquely identify the same graph subject across both Accounts and Organizations.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.GetGroupResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_azuredevops.GetGroupResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.GetGroupResult.origin">
<em class="property">property </em><code class="sig-name descname">origin</code><a class="headerlink" href="#pulumi_azuredevops.GetGroupResult.origin" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of source provider for the origin identifier (ex:AD, AAD, MSA)</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.GetGroupResult.origin_id">
<em class="property">property </em><code class="sig-name descname">origin_id</code><a class="headerlink" href="#pulumi_azuredevops.GetGroupResult.origin_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The unique identifier from the system of origin. Typically a sid, object id or Guid. Linking and unlinking operations can cause this value to change for a user because the user is not backed by a different provider and has a different unique id in the new provider.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_azuredevops.GetIterationResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azuredevops.</code><code class="sig-name descname">GetIterationResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">childrens</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">fetch_children</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">has_children</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">path</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuredevops.GetIterationResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getIteration.</p>
<dl class="py method">
<dt id="pulumi_azuredevops.GetIterationResult.childrens">
<em class="property">property </em><code class="sig-name descname">childrens</code><a class="headerlink" href="#pulumi_azuredevops.GetIterationResult.childrens" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of <code class="docutils literal notranslate"><span class="pre">children</span></code> blocks as defined below, empty if <code class="docutils literal notranslate"><span class="pre">has_children</span> <span class="pre">==</span> <span class="pre">false</span></code></p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.GetIterationResult.has_children">
<em class="property">property </em><code class="sig-name descname">has_children</code><a class="headerlink" href="#pulumi_azuredevops.GetIterationResult.has_children" title="Permalink to this definition">¶</a></dt>
<dd><p>Indicator if the child Iteration node has child nodes</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.GetIterationResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_azuredevops.GetIterationResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.GetIterationResult.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_azuredevops.GetIterationResult.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the child Iteration node</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.GetIterationResult.path">
<em class="property">property </em><code class="sig-name descname">path</code><a class="headerlink" href="#pulumi_azuredevops.GetIterationResult.path" title="Permalink to this definition">¶</a></dt>
<dd><p>The complete path (in relative URL format) of the child Iteration</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.GetIterationResult.project_id">
<em class="property">property </em><code class="sig-name descname">project_id</code><a class="headerlink" href="#pulumi_azuredevops.GetIterationResult.project_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The project ID of the child Iteration node</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_azuredevops.GetPoolResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azuredevops.</code><code class="sig-name descname">GetPoolResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">auto_provision</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">pool_type</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuredevops.GetPoolResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getPool.</p>
<dl class="py method">
<dt id="pulumi_azuredevops.GetPoolResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_azuredevops.GetPoolResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_azuredevops.GetPoolsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azuredevops.</code><code class="sig-name descname">GetPoolsResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">agent_pools</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuredevops.GetPoolsResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getPools.</p>
<dl class="py method">
<dt id="pulumi_azuredevops.GetPoolsResult.agent_pools">
<em class="property">property </em><code class="sig-name descname">agent_pools</code><a class="headerlink" href="#pulumi_azuredevops.GetPoolsResult.agent_pools" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of existing agent pools in your Azure DevOps Organization with the following details about every agent pool:</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.GetPoolsResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_azuredevops.GetPoolsResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_azuredevops.GetProjectResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azuredevops.</code><code class="sig-name descname">GetProjectResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">features</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">process_template_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">version_control</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">visibility</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">work_item_template</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuredevops.GetProjectResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getProject.</p>
<dl class="py method">
<dt id="pulumi_azuredevops.GetProjectResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_azuredevops.GetProjectResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_azuredevops.GetProjectsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azuredevops.</code><code class="sig-name descname">GetProjectsResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">projects</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">state</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuredevops.GetProjectsResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getProjects.</p>
<dl class="py method">
<dt id="pulumi_azuredevops.GetProjectsResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_azuredevops.GetProjectsResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.GetProjectsResult.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_azuredevops.GetProjectsResult.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Project name.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.GetProjectsResult.projects">
<em class="property">property </em><code class="sig-name descname">projects</code><a class="headerlink" href="#pulumi_azuredevops.GetProjectsResult.projects" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of existing projects in your Azure DevOps Organization with details about every project which includes:</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.GetProjectsResult.state">
<em class="property">property </em><code class="sig-name descname">state</code><a class="headerlink" href="#pulumi_azuredevops.GetProjectsResult.state" title="Permalink to this definition">¶</a></dt>
<dd><p>Project state.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_azuredevops.GetRepositoriesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azuredevops.</code><code class="sig-name descname">GetRepositoriesResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">include_hidden</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">repositories</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuredevops.GetRepositoriesResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getRepositories.</p>
<dl class="py method">
<dt id="pulumi_azuredevops.GetRepositoriesResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_azuredevops.GetRepositoriesResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.GetRepositoriesResult.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_azuredevops.GetRepositoriesResult.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Git repository name.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.GetRepositoriesResult.project_id">
<em class="property">property </em><code class="sig-name descname">project_id</code><a class="headerlink" href="#pulumi_azuredevops.GetRepositoriesResult.project_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Project identifier to which the Git repository belongs.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.GetRepositoriesResult.repositories">
<em class="property">property </em><code class="sig-name descname">repositories</code><a class="headerlink" href="#pulumi_azuredevops.GetRepositoriesResult.repositories" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of existing projects in your Azure DevOps Organization with details about every project which includes:</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_azuredevops.GetUsersResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azuredevops.</code><code class="sig-name descname">GetUsersResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">origin</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">origin_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">principal_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">subject_types</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">users</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuredevops.GetUsersResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getUsers.</p>
<dl class="py method">
<dt id="pulumi_azuredevops.GetUsersResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_azuredevops.GetUsersResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.GetUsersResult.origin">
<em class="property">property </em><code class="sig-name descname">origin</code><a class="headerlink" href="#pulumi_azuredevops.GetUsersResult.origin" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of source provider for the origin identifier (ex:AD, AAD, MSA)</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.GetUsersResult.origin_id">
<em class="property">property </em><code class="sig-name descname">origin_id</code><a class="headerlink" href="#pulumi_azuredevops.GetUsersResult.origin_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The unique identifier from the system of origin. Typically a sid, object id or Guid. Linking and unlinking operations can cause this value to change for a user because the user is not backed by a different provider and has a different unique id in the new provider.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.GetUsersResult.principal_name">
<em class="property">property </em><code class="sig-name descname">principal_name</code><a class="headerlink" href="#pulumi_azuredevops.GetUsersResult.principal_name" title="Permalink to this definition">¶</a></dt>
<dd><p>This is the PrincipalName of this graph member from the source provider. The source provider may change this field over time and it is not guaranteed to be immutable for the life of the graph member by VSTS.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.GetUsersResult.users">
<em class="property">property </em><code class="sig-name descname">users</code><a class="headerlink" href="#pulumi_azuredevops.GetUsersResult.users" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of existing users in your Azure DevOps Organization with details about every single user which includes:</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_azuredevops.Git">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azuredevops.</code><code class="sig-name descname">Git</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">default_branch</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">initialization</span><span class="p">:</span> <span class="n">Union[GitInitializationArgs, Mapping[str, Any], Awaitable[Union[GitInitializationArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">parent_repository_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuredevops.Git" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a git repository within Azure DevOps.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_azuredevops</span> <span class="k">as</span> <span class="nn">azuredevops</span>

<span class="n">project</span> <span class="o">=</span> <span class="n">azuredevops</span><span class="o">.</span><span class="n">Project</span><span class="p">(</span><span class="s2">&quot;project&quot;</span><span class="p">,</span>
    <span class="n">visibility</span><span class="o">=</span><span class="s2">&quot;private&quot;</span><span class="p">,</span>
    <span class="n">version_control</span><span class="o">=</span><span class="s2">&quot;Git&quot;</span><span class="p">,</span>
    <span class="n">work_item_template</span><span class="o">=</span><span class="s2">&quot;Agile&quot;</span><span class="p">)</span>
<span class="n">repo</span> <span class="o">=</span> <span class="n">azuredevops</span><span class="o">.</span><span class="n">Git</span><span class="p">(</span><span class="s2">&quot;repo&quot;</span><span class="p">,</span>
    <span class="n">project_id</span><span class="o">=</span><span class="n">project</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">initialization</span><span class="o">=</span><span class="n">azuredevops</span><span class="o">.</span><span class="n">GitInitializationArgs</span><span class="p">(</span>
        <span class="n">init_type</span><span class="o">=</span><span class="s2">&quot;Clean&quot;</span><span class="p">,</span>
    <span class="p">))</span>
</pre></div>
</div>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_azuredevops</span> <span class="k">as</span> <span class="nn">azuredevops</span>

<span class="n">repo</span> <span class="o">=</span> <span class="n">azuredevops</span><span class="o">.</span><span class="n">Git</span><span class="p">(</span><span class="s2">&quot;repo&quot;</span><span class="p">,</span>
    <span class="n">project_id</span><span class="o">=</span><span class="n">azuredevops_project</span><span class="p">[</span><span class="s2">&quot;project&quot;</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">],</span>
    <span class="n">parent_repository_id</span><span class="o">=</span><span class="n">azuredevops_git_repository</span><span class="p">[</span><span class="s2">&quot;parent&quot;</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">],</span>
    <span class="n">initialization</span><span class="o">=</span><span class="n">azuredevops</span><span class="o">.</span><span class="n">GitInitializationArgs</span><span class="p">(</span>
        <span class="n">init_type</span><span class="o">=</span><span class="s2">&quot;Clean&quot;</span><span class="p">,</span>
    <span class="p">))</span>
</pre></div>
</div>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_azuredevops</span> <span class="k">as</span> <span class="nn">azuredevops</span>

<span class="n">repo</span> <span class="o">=</span> <span class="n">azuredevops</span><span class="o">.</span><span class="n">Git</span><span class="p">(</span><span class="s2">&quot;repo&quot;</span><span class="p">,</span>
    <span class="n">project_id</span><span class="o">=</span><span class="n">azuredevops_project</span><span class="p">[</span><span class="s2">&quot;project&quot;</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">],</span>
    <span class="n">initialization</span><span class="o">=</span><span class="n">azuredevops</span><span class="o">.</span><span class="n">GitInitializationArgs</span><span class="p">(</span>
        <span class="n">init_type</span><span class="o">=</span><span class="s2">&quot;Import&quot;</span><span class="p">,</span>
        <span class="n">source_type</span><span class="o">=</span><span class="s2">&quot;Git&quot;</span><span class="p">,</span>
        <span class="n">source_url</span><span class="o">=</span><span class="s2">&quot;https://github.com/microsoft/terraform-provider-azuredevops.git&quot;</span><span class="p">,</span>
    <span class="p">))</span>
</pre></div>
</div>
<ul class="simple">
<li><p><a class="reference external" href="https://docs.microsoft.com/en-us/rest/api/azure/devops/git/repositories?view=azure-devops-rest-5.1">Azure DevOps Service REST API 5.1 - Git Repositories</a></p></li>
</ul>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>default_branch</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ref of the default branch. Will be used as the branch name for initialized repositories.</p></li>
<li><p><strong>initialization</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'GitInitializationArgs'</em><em>]</em><em>]</em>) – An <code class="docutils literal notranslate"><span class="pre">initialization</span></code> block as documented below.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the git repository.</p></li>
<li><p><strong>parent_repository_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of a Git project from which a fork is to be created.</p></li>
<li><p><strong>project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The project ID or project name.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_azuredevops.Git.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">default_branch</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">initialization</span><span class="p">:</span> <span class="n">Union[GitInitializationArgs, Mapping[str, Any], Awaitable[Union[GitInitializationArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">is_fork</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">parent_repository_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">remote_url</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">size</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ssh_url</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">url</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">web_url</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_azuredevops.git.Git<a class="headerlink" href="#pulumi_azuredevops.Git.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Git resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>default_branch</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ref of the default branch. Will be used as the branch name for initialized repositories.</p></li>
<li><p><strong>initialization</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'GitInitializationArgs'</em><em>]</em><em>]</em>) – An <code class="docutils literal notranslate"><span class="pre">initialization</span></code> block as documented below.</p></li>
<li><p><strong>is_fork</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – True if the repository was created as a fork.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the git repository.</p></li>
<li><p><strong>parent_repository_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of a Git project from which a fork is to be created.</p></li>
<li><p><strong>project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The project ID or project name.</p></li>
<li><p><strong>remote_url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Git HTTPS URL of the repository</p></li>
<li><p><strong>size</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Size in bytes.</p></li>
<li><p><strong>ssh_url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Git SSH URL of the repository.</p></li>
<li><p><strong>url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – REST API URL of the repository.</p></li>
<li><p><strong>web_url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Web link to the repository.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.Git.default_branch">
<em class="property">property </em><code class="sig-name descname">default_branch</code><a class="headerlink" href="#pulumi_azuredevops.Git.default_branch" title="Permalink to this definition">¶</a></dt>
<dd><p>The ref of the default branch. Will be used as the branch name for initialized repositories.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.Git.initialization">
<em class="property">property </em><code class="sig-name descname">initialization</code><a class="headerlink" href="#pulumi_azuredevops.Git.initialization" title="Permalink to this definition">¶</a></dt>
<dd><p>An <code class="docutils literal notranslate"><span class="pre">initialization</span></code> block as documented below.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.Git.is_fork">
<em class="property">property </em><code class="sig-name descname">is_fork</code><a class="headerlink" href="#pulumi_azuredevops.Git.is_fork" title="Permalink to this definition">¶</a></dt>
<dd><p>True if the repository was created as a fork.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.Git.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_azuredevops.Git.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the git repository.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.Git.parent_repository_id">
<em class="property">property </em><code class="sig-name descname">parent_repository_id</code><a class="headerlink" href="#pulumi_azuredevops.Git.parent_repository_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of a Git project from which a fork is to be created.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.Git.project_id">
<em class="property">property </em><code class="sig-name descname">project_id</code><a class="headerlink" href="#pulumi_azuredevops.Git.project_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The project ID or project name.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.Git.remote_url">
<em class="property">property </em><code class="sig-name descname">remote_url</code><a class="headerlink" href="#pulumi_azuredevops.Git.remote_url" title="Permalink to this definition">¶</a></dt>
<dd><p>Git HTTPS URL of the repository</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.Git.size">
<em class="property">property </em><code class="sig-name descname">size</code><a class="headerlink" href="#pulumi_azuredevops.Git.size" title="Permalink to this definition">¶</a></dt>
<dd><p>Size in bytes.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.Git.ssh_url">
<em class="property">property </em><code class="sig-name descname">ssh_url</code><a class="headerlink" href="#pulumi_azuredevops.Git.ssh_url" title="Permalink to this definition">¶</a></dt>
<dd><p>Git SSH URL of the repository.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.Git.url">
<em class="property">property </em><code class="sig-name descname">url</code><a class="headerlink" href="#pulumi_azuredevops.Git.url" title="Permalink to this definition">¶</a></dt>
<dd><p>REST API URL of the repository.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.Git.web_url">
<em class="property">property </em><code class="sig-name descname">web_url</code><a class="headerlink" href="#pulumi_azuredevops.Git.web_url" title="Permalink to this definition">¶</a></dt>
<dd><p>Web link to the repository.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.Git.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuredevops.Git.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azuredevops.Git.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuredevops.Git.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azuredevops.GitPermissions">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azuredevops.</code><code class="sig-name descname">GitPermissions</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">branch_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">permissions</span><span class="p">:</span> <span class="n">Union[Mapping[str, Union[str, Awaitable[str], Output[T]]], Awaitable[Mapping[str, Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">principal</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">replace</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">repository_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuredevops.GitPermissions" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages permissions for Git repositories.</p>
<blockquote>
<div><p><strong>Note</strong> Permissions can be assigned to group principals and not to single user principals.</p>
</div></blockquote>
<p>Permission for Git Repositories within Azure DevOps can be applied on three different levels.
Those levels are reflected by specifying (or omitting) values for the arguments <code class="docutils literal notranslate"><span class="pre">project_id</span></code>, <code class="docutils literal notranslate"><span class="pre">repository_id</span></code> and <code class="docutils literal notranslate"><span class="pre">branch_name</span></code>.</p>
<p>Permissions for all Git Repositories inside a project (existing or newly created ones) are specified, if only the argument <code class="docutils literal notranslate"><span class="pre">project_id</span></code> has a value.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_azuredevops</span> <span class="k">as</span> <span class="nn">azuredevops</span>

<span class="n">project_git_root_permissions</span> <span class="o">=</span> <span class="n">azuredevops</span><span class="o">.</span><span class="n">GitPermissions</span><span class="p">(</span><span class="s2">&quot;project-git-root-permissions&quot;</span><span class="p">,</span>
    <span class="n">project_id</span><span class="o">=</span><span class="n">azuredevops_project</span><span class="p">[</span><span class="s2">&quot;project&quot;</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">],</span>
    <span class="n">principal</span><span class="o">=</span><span class="n">data</span><span class="p">[</span><span class="s2">&quot;azuredevops_group&quot;</span><span class="p">][</span><span class="s2">&quot;project-readers&quot;</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">],</span>
    <span class="n">permissions</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;CreateRepository&quot;</span><span class="p">:</span> <span class="s2">&quot;Deny&quot;</span><span class="p">,</span>
        <span class="s2">&quot;DeleteRepository&quot;</span><span class="p">:</span> <span class="s2">&quot;Deny&quot;</span><span class="p">,</span>
        <span class="s2">&quot;RenameRepository&quot;</span><span class="p">:</span> <span class="s2">&quot;NotSet&quot;</span><span class="p">,</span>
    <span class="p">})</span>
</pre></div>
</div>
<p>Permissions for a specific Git Repository and all existing or newly created branches are specified if the arguments <code class="docutils literal notranslate"><span class="pre">project_id</span></code> and <code class="docutils literal notranslate"><span class="pre">repository_id</span></code> are set.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_azuredevops</span> <span class="k">as</span> <span class="nn">azuredevops</span>

<span class="n">project_git_repo_permissions</span> <span class="o">=</span> <span class="n">azuredevops</span><span class="o">.</span><span class="n">GitPermissions</span><span class="p">(</span><span class="s2">&quot;project-git-repo-permissions&quot;</span><span class="p">,</span>
    <span class="n">project_id</span><span class="o">=</span><span class="n">data</span><span class="p">[</span><span class="s2">&quot;azuredevops_git_repository&quot;</span><span class="p">][</span><span class="s2">&quot;git-repo&quot;</span><span class="p">][</span><span class="s2">&quot;project_id&quot;</span><span class="p">],</span>
    <span class="n">repository_id</span><span class="o">=</span><span class="n">data</span><span class="p">[</span><span class="s2">&quot;azuredevops_git_repository&quot;</span><span class="p">][</span><span class="s2">&quot;git-repo&quot;</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">],</span>
    <span class="n">principal</span><span class="o">=</span><span class="n">data</span><span class="p">[</span><span class="s2">&quot;azuredevops_group&quot;</span><span class="p">][</span><span class="s2">&quot;project-administrators&quot;</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">],</span>
    <span class="n">permissions</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;RemoveOthersLocks&quot;</span><span class="p">:</span> <span class="s2">&quot;Allow&quot;</span><span class="p">,</span>
        <span class="s2">&quot;ManagePermissions&quot;</span><span class="p">:</span> <span class="s2">&quot;Deny&quot;</span><span class="p">,</span>
        <span class="s2">&quot;CreateTag&quot;</span><span class="p">:</span> <span class="s2">&quot;Deny&quot;</span><span class="p">,</span>
        <span class="s2">&quot;CreateBranch&quot;</span><span class="p">:</span> <span class="s2">&quot;NotSet&quot;</span><span class="p">,</span>
    <span class="p">})</span>
</pre></div>
</div>
<p>Permissions for a specific branch inside a Git Repository are specified if all above mentioned the arguments are set.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_azuredevops</span> <span class="k">as</span> <span class="nn">azuredevops</span>

<span class="n">project_git_branch_permissions</span> <span class="o">=</span> <span class="n">azuredevops</span><span class="o">.</span><span class="n">GitPermissions</span><span class="p">(</span><span class="s2">&quot;project-git-branch-permissions&quot;</span><span class="p">,</span>
    <span class="n">project_id</span><span class="o">=</span><span class="n">data</span><span class="p">[</span><span class="s2">&quot;azuredevops_git_repository&quot;</span><span class="p">][</span><span class="s2">&quot;git-repo&quot;</span><span class="p">][</span><span class="s2">&quot;project_id&quot;</span><span class="p">],</span>
    <span class="n">repository_id</span><span class="o">=</span><span class="n">data</span><span class="p">[</span><span class="s2">&quot;azuredevops_git_repository&quot;</span><span class="p">][</span><span class="s2">&quot;git-repo&quot;</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">],</span>
    <span class="n">branch_name</span><span class="o">=</span><span class="s2">&quot;refs/heads/master&quot;</span><span class="p">,</span>
    <span class="n">principal</span><span class="o">=</span><span class="n">data</span><span class="p">[</span><span class="s2">&quot;azuredevops_group&quot;</span><span class="p">][</span><span class="s2">&quot;project-contributors&quot;</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">],</span>
    <span class="n">permissions</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;RemoveOthersLocks&quot;</span><span class="p">:</span> <span class="s2">&quot;Allow&quot;</span><span class="p">,</span>
        <span class="s2">&quot;ForcePush&quot;</span><span class="p">:</span> <span class="s2">&quot;Deny&quot;</span><span class="p">,</span>
    <span class="p">})</span>
</pre></div>
</div>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_azuredevops</span> <span class="k">as</span> <span class="nn">azuredevops</span>

<span class="n">project</span> <span class="o">=</span> <span class="n">azuredevops</span><span class="o">.</span><span class="n">Project</span><span class="p">(</span><span class="s2">&quot;project&quot;</span><span class="p">,</span>
    <span class="n">description</span><span class="o">=</span><span class="s2">&quot;Test Project Description&quot;</span><span class="p">,</span>
    <span class="n">visibility</span><span class="o">=</span><span class="s2">&quot;private&quot;</span><span class="p">,</span>
    <span class="n">version_control</span><span class="o">=</span><span class="s2">&quot;Git&quot;</span><span class="p">,</span>
    <span class="n">work_item_template</span><span class="o">=</span><span class="s2">&quot;Agile&quot;</span><span class="p">)</span>
<span class="n">project_readers</span> <span class="o">=</span> <span class="n">project</span><span class="o">.</span><span class="n">id</span><span class="o">.</span><span class="n">apply</span><span class="p">(</span><span class="k">lambda</span> <span class="nb">id</span><span class="p">:</span> <span class="n">azuredevops</span><span class="o">.</span><span class="n">get_group</span><span class="p">(</span><span class="n">project_id</span><span class="o">=</span><span class="nb">id</span><span class="p">,</span>
    <span class="n">name</span><span class="o">=</span><span class="s2">&quot;Readers&quot;</span><span class="p">))</span>
<span class="n">project_contributors</span> <span class="o">=</span> <span class="n">project</span><span class="o">.</span><span class="n">id</span><span class="o">.</span><span class="n">apply</span><span class="p">(</span><span class="k">lambda</span> <span class="nb">id</span><span class="p">:</span> <span class="n">azuredevops</span><span class="o">.</span><span class="n">get_group</span><span class="p">(</span><span class="n">project_id</span><span class="o">=</span><span class="nb">id</span><span class="p">,</span>
    <span class="n">name</span><span class="o">=</span><span class="s2">&quot;Contributors&quot;</span><span class="p">))</span>
<span class="n">project_administrators</span> <span class="o">=</span> <span class="n">project</span><span class="o">.</span><span class="n">id</span><span class="o">.</span><span class="n">apply</span><span class="p">(</span><span class="k">lambda</span> <span class="nb">id</span><span class="p">:</span> <span class="n">azuredevops</span><span class="o">.</span><span class="n">get_group</span><span class="p">(</span><span class="n">project_id</span><span class="o">=</span><span class="nb">id</span><span class="p">,</span>
    <span class="n">name</span><span class="o">=</span><span class="s2">&quot;Project administrators&quot;</span><span class="p">))</span>
<span class="n">project_git_root_permissions</span> <span class="o">=</span> <span class="n">azuredevops</span><span class="o">.</span><span class="n">GitPermissions</span><span class="p">(</span><span class="s2">&quot;project-git-root-permissions&quot;</span><span class="p">,</span>
    <span class="n">project_id</span><span class="o">=</span><span class="n">project</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">principal</span><span class="o">=</span><span class="n">project_readers</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">permissions</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;CreateRepository&quot;</span><span class="p">:</span> <span class="s2">&quot;Deny&quot;</span><span class="p">,</span>
        <span class="s2">&quot;DeleteRepository&quot;</span><span class="p">:</span> <span class="s2">&quot;Deny&quot;</span><span class="p">,</span>
        <span class="s2">&quot;RenameRepository&quot;</span><span class="p">:</span> <span class="s2">&quot;NotSet&quot;</span><span class="p">,</span>
    <span class="p">})</span>
<span class="n">git_repo</span> <span class="o">=</span> <span class="n">azuredevops</span><span class="o">.</span><span class="n">Git</span><span class="p">(</span><span class="s2">&quot;git-repo&quot;</span><span class="p">,</span>
    <span class="n">project_id</span><span class="o">=</span><span class="n">project</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">default_branch</span><span class="o">=</span><span class="s2">&quot;refs/heads/master&quot;</span><span class="p">,</span>
    <span class="n">initialization</span><span class="o">=</span><span class="n">azuredevops</span><span class="o">.</span><span class="n">GitInitializationArgs</span><span class="p">(</span>
        <span class="n">init_type</span><span class="o">=</span><span class="s2">&quot;Clean&quot;</span><span class="p">,</span>
    <span class="p">))</span>
<span class="n">project_git_repo_permissions</span> <span class="o">=</span> <span class="n">azuredevops</span><span class="o">.</span><span class="n">GitPermissions</span><span class="p">(</span><span class="s2">&quot;project-git-repo-permissions&quot;</span><span class="p">,</span>
    <span class="n">project_id</span><span class="o">=</span><span class="n">git_repo</span><span class="o">.</span><span class="n">project_id</span><span class="p">,</span>
    <span class="n">repository_id</span><span class="o">=</span><span class="n">git_repo</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">principal</span><span class="o">=</span><span class="n">project_administrators</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">permissions</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;RemoveOthersLocks&quot;</span><span class="p">:</span> <span class="s2">&quot;Allow&quot;</span><span class="p">,</span>
        <span class="s2">&quot;ManagePermissions&quot;</span><span class="p">:</span> <span class="s2">&quot;Deny&quot;</span><span class="p">,</span>
        <span class="s2">&quot;CreateTag&quot;</span><span class="p">:</span> <span class="s2">&quot;Deny&quot;</span><span class="p">,</span>
        <span class="s2">&quot;CreateBranch&quot;</span><span class="p">:</span> <span class="s2">&quot;NotSet&quot;</span><span class="p">,</span>
    <span class="p">})</span>
<span class="n">project_git_branch_permissions</span> <span class="o">=</span> <span class="n">azuredevops</span><span class="o">.</span><span class="n">GitPermissions</span><span class="p">(</span><span class="s2">&quot;project-git-branch-permissions&quot;</span><span class="p">,</span>
    <span class="n">project_id</span><span class="o">=</span><span class="n">git_repo</span><span class="o">.</span><span class="n">project_id</span><span class="p">,</span>
    <span class="n">repository_id</span><span class="o">=</span><span class="n">git_repo</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">branch_name</span><span class="o">=</span><span class="s2">&quot;master&quot;</span><span class="p">,</span>
    <span class="n">principal</span><span class="o">=</span><span class="n">project_contributors</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">permissions</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;RemoveOthersLocks&quot;</span><span class="p">:</span> <span class="s2">&quot;Allow&quot;</span><span class="p">,</span>
        <span class="s2">&quot;ForcePush&quot;</span><span class="p">:</span> <span class="s2">&quot;Deny&quot;</span><span class="p">,</span>
    <span class="p">})</span>
</pre></div>
</div>
<ul class="simple">
<li><p><a class="reference external" href="https://docs.microsoft.com/en-us/rest/api/azure/devops/security/?view=azure-devops-rest-5.1">Azure DevOps Service REST API 5.1 - Security</a></p></li>
</ul>
<ul class="simple">
<li><p><strong>Project &amp; Team</strong>: vso.security_manage - Grants the ability to read, write, and manage security permissions.</p></li>
</ul>
<p>The resource does not support import.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>branch_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the branch to assign the permissions.</p></li>
<li><p><strong>pulumi.Input</strong><strong>[</strong><strong>str</strong><strong>]</strong><strong>]</strong><strong>] </strong><strong>permissions</strong> (<em>pulumi.Input</em><em>[</em><em>Mapping</em><em>[</em><em>str</em><em>,</em>) – the permissions to assign. The follwing permissions are available</p></li>
<li><p><strong>principal</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The <strong>group</strong> principal to assign the permissions.</p></li>
<li><p><strong>project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project to assign the permissions.</p></li>
<li><p><strong>replace</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Replace (<code class="docutils literal notranslate"><span class="pre">true</span></code>) or merge (<code class="docutils literal notranslate"><span class="pre">false</span></code>) the permissions. Default: <code class="docutils literal notranslate"><span class="pre">true</span></code></p></li>
<li><p><strong>repository_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the GIT repository to assign the permissions</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_azuredevops.GitPermissions.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">branch_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">permissions</span><span class="p">:</span> <span class="n">Union[Mapping[str, Union[str, Awaitable[str], Output[T]]], Awaitable[Mapping[str, Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">principal</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">replace</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">repository_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_azuredevops.git_permissions.GitPermissions<a class="headerlink" href="#pulumi_azuredevops.GitPermissions.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing GitPermissions resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>branch_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the branch to assign the permissions.</p></li>
<li><p><strong>pulumi.Input</strong><strong>[</strong><strong>str</strong><strong>]</strong><strong>]</strong><strong>] </strong><strong>permissions</strong> (<em>pulumi.Input</em><em>[</em><em>Mapping</em><em>[</em><em>str</em><em>,</em>) – the permissions to assign. The follwing permissions are available</p></li>
<li><p><strong>principal</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The <strong>group</strong> principal to assign the permissions.</p></li>
<li><p><strong>project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project to assign the permissions.</p></li>
<li><p><strong>replace</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Replace (<code class="docutils literal notranslate"><span class="pre">true</span></code>) or merge (<code class="docutils literal notranslate"><span class="pre">false</span></code>) the permissions. Default: <code class="docutils literal notranslate"><span class="pre">true</span></code></p></li>
<li><p><strong>repository_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the GIT repository to assign the permissions</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.GitPermissions.branch_name">
<em class="property">property </em><code class="sig-name descname">branch_name</code><a class="headerlink" href="#pulumi_azuredevops.GitPermissions.branch_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the branch to assign the permissions.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.GitPermissions.permissions">
<em class="property">property </em><code class="sig-name descname">permissions</code><a class="headerlink" href="#pulumi_azuredevops.GitPermissions.permissions" title="Permalink to this definition">¶</a></dt>
<dd><p>the permissions to assign. The follwing permissions are available</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.GitPermissions.principal">
<em class="property">property </em><code class="sig-name descname">principal</code><a class="headerlink" href="#pulumi_azuredevops.GitPermissions.principal" title="Permalink to this definition">¶</a></dt>
<dd><p>The <strong>group</strong> principal to assign the permissions.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.GitPermissions.project_id">
<em class="property">property </em><code class="sig-name descname">project_id</code><a class="headerlink" href="#pulumi_azuredevops.GitPermissions.project_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project to assign the permissions.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.GitPermissions.replace">
<em class="property">property </em><code class="sig-name descname">replace</code><a class="headerlink" href="#pulumi_azuredevops.GitPermissions.replace" title="Permalink to this definition">¶</a></dt>
<dd><p>Replace (<code class="docutils literal notranslate"><span class="pre">true</span></code>) or merge (<code class="docutils literal notranslate"><span class="pre">false</span></code>) the permissions. Default: <code class="docutils literal notranslate"><span class="pre">true</span></code></p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.GitPermissions.repository_id">
<em class="property">property </em><code class="sig-name descname">repository_id</code><a class="headerlink" href="#pulumi_azuredevops.GitPermissions.repository_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the GIT repository to assign the permissions</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.GitPermissions.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuredevops.GitPermissions.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azuredevops.GitPermissions.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuredevops.GitPermissions.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azuredevops.Group">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azuredevops.</code><code class="sig-name descname">Group</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">display_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">mail</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">members</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">origin_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">scope</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuredevops.Group" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a group within Azure DevOps.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_azuredevops</span> <span class="k">as</span> <span class="nn">azuredevops</span>

<span class="n">project</span> <span class="o">=</span> <span class="n">azuredevops</span><span class="o">.</span><span class="n">Project</span><span class="p">(</span><span class="s2">&quot;project&quot;</span><span class="p">)</span>
<span class="n">tf_project_readers</span> <span class="o">=</span> <span class="n">project</span><span class="o">.</span><span class="n">id</span><span class="o">.</span><span class="n">apply</span><span class="p">(</span><span class="k">lambda</span> <span class="nb">id</span><span class="p">:</span> <span class="n">azuredevops</span><span class="o">.</span><span class="n">get_group</span><span class="p">(</span><span class="n">project_id</span><span class="o">=</span><span class="nb">id</span><span class="p">,</span>
    <span class="n">name</span><span class="o">=</span><span class="s2">&quot;Readers&quot;</span><span class="p">))</span>
<span class="n">tf_project_contributors</span> <span class="o">=</span> <span class="n">project</span><span class="o">.</span><span class="n">id</span><span class="o">.</span><span class="n">apply</span><span class="p">(</span><span class="k">lambda</span> <span class="nb">id</span><span class="p">:</span> <span class="n">azuredevops</span><span class="o">.</span><span class="n">get_group</span><span class="p">(</span><span class="n">project_id</span><span class="o">=</span><span class="nb">id</span><span class="p">,</span>
    <span class="n">name</span><span class="o">=</span><span class="s2">&quot;Contributors&quot;</span><span class="p">))</span>
<span class="n">group</span> <span class="o">=</span> <span class="n">azuredevops</span><span class="o">.</span><span class="n">Group</span><span class="p">(</span><span class="s2">&quot;group&quot;</span><span class="p">,</span>
    <span class="n">scope</span><span class="o">=</span><span class="n">project</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">display_name</span><span class="o">=</span><span class="s2">&quot;Test group&quot;</span><span class="p">,</span>
    <span class="n">description</span><span class="o">=</span><span class="s2">&quot;Test description&quot;</span><span class="p">,</span>
    <span class="n">members</span><span class="o">=</span><span class="p">[</span>
        <span class="n">tf_project_readers</span><span class="o">.</span><span class="n">descriptor</span><span class="p">,</span>
        <span class="n">tf_project_contributors</span><span class="o">.</span><span class="n">descriptor</span><span class="p">,</span>
    <span class="p">])</span>
</pre></div>
</div>
<ul class="simple">
<li><p><a class="reference external" href="https://docs.microsoft.com/en-us/rest/api/azure/devops/graph/groups?view=azure-devops-rest-5.1">Azure DevOps Service REST API 5.1 - Groups</a></p></li>
</ul>
<ul class="simple">
<li><p><strong>Project &amp; Team</strong>: Read, Write, &amp; Manage</p></li>
</ul>
<p>Azure DevOps Projects can be imported using the group identity descriptor, e.g.</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>$ pulumi import azuredevops:index/group:Group id aadgp.Uy0xLTktMTU1MTM3NDI0NS0xMjA0NDAwOTY5LTI0MDI5ODY0MTMtMjE3OTQwODYxNi0zLTIxNjc2NjQyNTMtMzI1Nzg0NDI4OS0yMjU4MjcwOTc0LTI2MDYxODY2NDU
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Description of the Project.</p></li>
<li><p><strong>display_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of a new Azure DevOps group that is not backed by an external provider. The <code class="docutils literal notranslate"><span class="pre">origin_id</span></code> and <code class="docutils literal notranslate"><span class="pre">mail</span></code> arguments cannot be used simultaneously with <code class="docutils literal notranslate"><span class="pre">display_name</span></code>.</p></li>
<li><p><strong>mail</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The mail address as a reference to an existing group from an external AD or AAD backed provider. The <code class="docutils literal notranslate"><span class="pre">scope</span></code>, <code class="docutils literal notranslate"><span class="pre">origin_id</span></code> and <code class="docutils literal notranslate"><span class="pre">display_name</span></code> arguments cannot be used simultaneously with <code class="docutils literal notranslate"><span class="pre">mail</span></code>.</p></li>
<li><p><strong>members</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – &gt; NOTE: It’s possible to define group members both within the <code class="docutils literal notranslate"><span class="pre">Group</span></code> resource via the members block and by using the <code class="docutils literal notranslate"><span class="pre">GroupMembership</span></code> resource. However it’s not possible to use both methods to manage group members, since there’ll be conflicts.</p></li>
<li><p><strong>origin_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The OriginID as a reference to a group from an external AD or AAD backed provider. The <code class="docutils literal notranslate"><span class="pre">scope</span></code>, <code class="docutils literal notranslate"><span class="pre">mail</span></code> and <code class="docutils literal notranslate"><span class="pre">display_name</span></code> arguments cannot be used simultaneously with <code class="docutils literal notranslate"><span class="pre">origin_id</span></code>.</p></li>
<li><p><strong>scope</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The scope of the group. A descriptor referencing the scope (collection, project) in which the group should be created. If omitted, will be created in the scope of the enclosing account or organization.x</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_azuredevops.Group.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">descriptor</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">display_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">domain</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">mail</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">members</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">origin</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">origin_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">principal_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">scope</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">subject_kind</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">url</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_azuredevops.group.Group<a class="headerlink" href="#pulumi_azuredevops.Group.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Group resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Description of the Project.</p></li>
<li><p><strong>descriptor</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The identity (subject) descriptor of the Group.</p></li>
<li><p><strong>display_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of a new Azure DevOps group that is not backed by an external provider. The <code class="docutils literal notranslate"><span class="pre">origin_id</span></code> and <code class="docutils literal notranslate"><span class="pre">mail</span></code> arguments cannot be used simultaneously with <code class="docutils literal notranslate"><span class="pre">display_name</span></code>.</p></li>
<li><p><strong>domain</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – This represents the name of the container of origin for a graph member.</p></li>
<li><p><strong>mail</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The mail address as a reference to an existing group from an external AD or AAD backed provider. The <code class="docutils literal notranslate"><span class="pre">scope</span></code>, <code class="docutils literal notranslate"><span class="pre">origin_id</span></code> and <code class="docutils literal notranslate"><span class="pre">display_name</span></code> arguments cannot be used simultaneously with <code class="docutils literal notranslate"><span class="pre">mail</span></code>.</p></li>
<li><p><strong>members</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – &gt; NOTE: It’s possible to define group members both within the <code class="docutils literal notranslate"><span class="pre">Group</span></code> resource via the members block and by using the <code class="docutils literal notranslate"><span class="pre">GroupMembership</span></code> resource. However it’s not possible to use both methods to manage group members, since there’ll be conflicts.</p></li>
<li><p><strong>origin</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of source provider for the origin identifier (ex:AD, AAD, MSA)</p></li>
<li><p><strong>origin_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The OriginID as a reference to a group from an external AD or AAD backed provider. The <code class="docutils literal notranslate"><span class="pre">scope</span></code>, <code class="docutils literal notranslate"><span class="pre">mail</span></code> and <code class="docutils literal notranslate"><span class="pre">display_name</span></code> arguments cannot be used simultaneously with <code class="docutils literal notranslate"><span class="pre">origin_id</span></code>.</p></li>
<li><p><strong>principal_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – This is the PrincipalName of this graph member from the source provider.</p></li>
<li><p><strong>scope</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The scope of the group. A descriptor referencing the scope (collection, project) in which the group should be created. If omitted, will be created in the scope of the enclosing account or organization.x</p></li>
<li><p><strong>subject_kind</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – This field identifies the type of the graph subject (ex: Group, Scope, User).</p></li>
<li><p><strong>url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – This url is the full route to the source resource of this graph subject.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.Group.description">
<em class="property">property </em><code class="sig-name descname">description</code><a class="headerlink" href="#pulumi_azuredevops.Group.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The Description of the Project.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.Group.descriptor">
<em class="property">property </em><code class="sig-name descname">descriptor</code><a class="headerlink" href="#pulumi_azuredevops.Group.descriptor" title="Permalink to this definition">¶</a></dt>
<dd><p>The identity (subject) descriptor of the Group.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.Group.display_name">
<em class="property">property </em><code class="sig-name descname">display_name</code><a class="headerlink" href="#pulumi_azuredevops.Group.display_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of a new Azure DevOps group that is not backed by an external provider. The <code class="docutils literal notranslate"><span class="pre">origin_id</span></code> and <code class="docutils literal notranslate"><span class="pre">mail</span></code> arguments cannot be used simultaneously with <code class="docutils literal notranslate"><span class="pre">display_name</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.Group.domain">
<em class="property">property </em><code class="sig-name descname">domain</code><a class="headerlink" href="#pulumi_azuredevops.Group.domain" title="Permalink to this definition">¶</a></dt>
<dd><p>This represents the name of the container of origin for a graph member.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.Group.mail">
<em class="property">property </em><code class="sig-name descname">mail</code><a class="headerlink" href="#pulumi_azuredevops.Group.mail" title="Permalink to this definition">¶</a></dt>
<dd><p>The mail address as a reference to an existing group from an external AD or AAD backed provider. The <code class="docutils literal notranslate"><span class="pre">scope</span></code>, <code class="docutils literal notranslate"><span class="pre">origin_id</span></code> and <code class="docutils literal notranslate"><span class="pre">display_name</span></code> arguments cannot be used simultaneously with <code class="docutils literal notranslate"><span class="pre">mail</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.Group.members">
<em class="property">property </em><code class="sig-name descname">members</code><a class="headerlink" href="#pulumi_azuredevops.Group.members" title="Permalink to this definition">¶</a></dt>
<dd><blockquote>
<div><p>NOTE: It’s possible to define group members both within the <code class="docutils literal notranslate"><span class="pre">Group</span></code> resource via the members block and by using the <code class="docutils literal notranslate"><span class="pre">GroupMembership</span></code> resource. However it’s not possible to use both methods to manage group members, since there’ll be conflicts.</p>
</div></blockquote>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.Group.origin">
<em class="property">property </em><code class="sig-name descname">origin</code><a class="headerlink" href="#pulumi_azuredevops.Group.origin" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of source provider for the origin identifier (ex:AD, AAD, MSA)</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.Group.origin_id">
<em class="property">property </em><code class="sig-name descname">origin_id</code><a class="headerlink" href="#pulumi_azuredevops.Group.origin_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The OriginID as a reference to a group from an external AD or AAD backed provider. The <code class="docutils literal notranslate"><span class="pre">scope</span></code>, <code class="docutils literal notranslate"><span class="pre">mail</span></code> and <code class="docutils literal notranslate"><span class="pre">display_name</span></code> arguments cannot be used simultaneously with <code class="docutils literal notranslate"><span class="pre">origin_id</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.Group.principal_name">
<em class="property">property </em><code class="sig-name descname">principal_name</code><a class="headerlink" href="#pulumi_azuredevops.Group.principal_name" title="Permalink to this definition">¶</a></dt>
<dd><p>This is the PrincipalName of this graph member from the source provider.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.Group.scope">
<em class="property">property </em><code class="sig-name descname">scope</code><a class="headerlink" href="#pulumi_azuredevops.Group.scope" title="Permalink to this definition">¶</a></dt>
<dd><p>The scope of the group. A descriptor referencing the scope (collection, project) in which the group should be created. If omitted, will be created in the scope of the enclosing account or organization.x</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.Group.subject_kind">
<em class="property">property </em><code class="sig-name descname">subject_kind</code><a class="headerlink" href="#pulumi_azuredevops.Group.subject_kind" title="Permalink to this definition">¶</a></dt>
<dd><p>This field identifies the type of the graph subject (ex: Group, Scope, User).</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.Group.url">
<em class="property">property </em><code class="sig-name descname">url</code><a class="headerlink" href="#pulumi_azuredevops.Group.url" title="Permalink to this definition">¶</a></dt>
<dd><p>This url is the full route to the source resource of this graph subject.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.Group.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuredevops.Group.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azuredevops.Group.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuredevops.Group.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azuredevops.GroupMembership">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azuredevops.</code><code class="sig-name descname">GroupMembership</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">group</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">members</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">mode</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuredevops.GroupMembership" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages group membership within Azure DevOps.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_azuredevops</span> <span class="k">as</span> <span class="nn">azuredevops</span>

<span class="n">project</span> <span class="o">=</span> <span class="n">azuredevops</span><span class="o">.</span><span class="n">Project</span><span class="p">(</span><span class="s2">&quot;project&quot;</span><span class="p">)</span>
<span class="n">user</span> <span class="o">=</span> <span class="n">azuredevops</span><span class="o">.</span><span class="n">User</span><span class="p">(</span><span class="s2">&quot;user&quot;</span><span class="p">,</span> <span class="n">principal_name</span><span class="o">=</span><span class="s2">&quot;foo@contoso.com&quot;</span><span class="p">)</span>
<span class="n">group</span> <span class="o">=</span> <span class="n">project</span><span class="o">.</span><span class="n">id</span><span class="o">.</span><span class="n">apply</span><span class="p">(</span><span class="k">lambda</span> <span class="nb">id</span><span class="p">:</span> <span class="n">azuredevops</span><span class="o">.</span><span class="n">get_group</span><span class="p">(</span><span class="n">project_id</span><span class="o">=</span><span class="nb">id</span><span class="p">,</span>
    <span class="n">name</span><span class="o">=</span><span class="s2">&quot;Build Administrators&quot;</span><span class="p">))</span>
<span class="n">membership</span> <span class="o">=</span> <span class="n">azuredevops</span><span class="o">.</span><span class="n">GroupMembership</span><span class="p">(</span><span class="s2">&quot;membership&quot;</span><span class="p">,</span>
    <span class="n">group</span><span class="o">=</span><span class="n">group</span><span class="o">.</span><span class="n">descriptor</span><span class="p">,</span>
    <span class="n">members</span><span class="o">=</span><span class="p">[</span><span class="n">user</span><span class="o">.</span><span class="n">descriptor</span><span class="p">])</span>
</pre></div>
</div>
<ul class="simple">
<li><p><a class="reference external" href="https://docs.microsoft.com/en-us/rest/api/azure/devops/graph/memberships?view=azure-devops-rest-5.0">Azure DevOps Service REST API 5.1 - Memberships</a></p></li>
</ul>
<ul class="simple">
<li><p><strong>Deployment Groups</strong>: Read &amp; Manage</p></li>
</ul>
<p>Not supported.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>group</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The descriptor of the group being managed.</p></li>
<li><p><strong>members</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – A list of user or group descriptors that will become members of the group.</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="o">&gt;</span> <span class="n">NOTE</span><span class="p">:</span> <span class="n">It</span><span class="s1">&#39;s possible to define group members both within the `GroupMembership resource` via the members block and by using the `Group` resource. However it&#39;</span><span class="n">s</span> <span class="ow">not</span> <span class="n">possible</span> <span class="n">to</span> <span class="n">use</span> <span class="n">both</span> <span class="n">methods</span> <span class="n">to</span> <span class="n">manage</span> <span class="n">group</span> <span class="n">members</span><span class="p">,</span> <span class="n">since</span> <span class="n">there</span><span class="s1">&#39;ll be conflicts.</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>mode</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The mode how the resource manages group members.</p>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>- `mode == add`: the resource will ensure that all specified members will be part of the referenced group
- `mode == overwrite`: the resource will replace all existing members with the members specified within the `members` block
&gt; NOTE: To clear all members from a group, specify an empty list of descriptors in the `members` attribute and set the `mode` member to `overwrite`.
</pre></div>
</div>
<dl class="py method">
<dt id="pulumi_azuredevops.GroupMembership.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">group</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">members</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">mode</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_azuredevops.group_membership.GroupMembership<a class="headerlink" href="#pulumi_azuredevops.GroupMembership.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing GroupMembership resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>group</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The descriptor of the group being managed.</p></li>
<li><p><strong>members</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – A list of user or group descriptors that will become members of the group.</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="o">&gt;</span> <span class="n">NOTE</span><span class="p">:</span> <span class="n">It</span><span class="s1">&#39;s possible to define group members both within the `GroupMembership resource` via the members block and by using the `Group` resource. However it&#39;</span><span class="n">s</span> <span class="ow">not</span> <span class="n">possible</span> <span class="n">to</span> <span class="n">use</span> <span class="n">both</span> <span class="n">methods</span> <span class="n">to</span> <span class="n">manage</span> <span class="n">group</span> <span class="n">members</span><span class="p">,</span> <span class="n">since</span> <span class="n">there</span><span class="s1">&#39;ll be conflicts.</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>mode</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The mode how the resource manages group members.</p>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>- `mode == add`: the resource will ensure that all specified members will be part of the referenced group
- `mode == overwrite`: the resource will replace all existing members with the members specified within the `members` block
&gt; NOTE: To clear all members from a group, specify an empty list of descriptors in the `members` attribute and set the `mode` member to `overwrite`.
</pre></div>
</div>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.GroupMembership.group">
<em class="property">property </em><code class="sig-name descname">group</code><a class="headerlink" href="#pulumi_azuredevops.GroupMembership.group" title="Permalink to this definition">¶</a></dt>
<dd><p>The descriptor of the group being managed.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.GroupMembership.members">
<em class="property">property </em><code class="sig-name descname">members</code><a class="headerlink" href="#pulumi_azuredevops.GroupMembership.members" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of user or group descriptors that will become members of the group.</p>
<blockquote>
<div><p>NOTE: It’s possible to define group members both within the <code class="docutils literal notranslate"><span class="pre">GroupMembership</span> <span class="pre">resource</span></code> via the members block and by using the <code class="docutils literal notranslate"><span class="pre">Group</span></code> resource. However it’s not possible to use both methods to manage group members, since there’ll be conflicts.</p>
</div></blockquote>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.GroupMembership.mode">
<em class="property">property </em><code class="sig-name descname">mode</code><a class="headerlink" href="#pulumi_azuredevops.GroupMembership.mode" title="Permalink to this definition">¶</a></dt>
<dd><p>The mode how the resource manages group members.</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">mode</span> <span class="pre">==</span> <span class="pre">add</span></code>: the resource will ensure that all specified members will be part of the referenced group</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">mode</span> <span class="pre">==</span> <span class="pre">overwrite</span></code>: the resource will replace all existing members with the members specified within the <code class="docutils literal notranslate"><span class="pre">members</span></code> block
..</p>
<blockquote>
<div><p>NOTE: To clear all members from a group, specify an empty list of descriptors in the <code class="docutils literal notranslate"><span class="pre">members</span></code> attribute and set the <code class="docutils literal notranslate"><span class="pre">mode</span></code> member to <code class="docutils literal notranslate"><span class="pre">overwrite</span></code>.</p>
</div></blockquote>
</li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.GroupMembership.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuredevops.GroupMembership.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azuredevops.GroupMembership.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuredevops.GroupMembership.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azuredevops.IterativePermissions">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azuredevops.</code><code class="sig-name descname">IterativePermissions</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">path</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">permissions</span><span class="p">:</span> <span class="n">Union[Mapping[str, Union[str, Awaitable[str], Output[T]]], Awaitable[Mapping[str, Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">principal</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">replace</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuredevops.IterativePermissions" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages permissions for an Iteration (Sprint)</p>
<blockquote>
<div><p><strong>Note</strong> Permissions can be assigned to group principals and not to single user principals.</p>
</div></blockquote>
<p>Permission for Iterations within Azure DevOps can be applied on two different levels.
Those levels are reflected by specifying (or omitting) values for the arguments <code class="docutils literal notranslate"><span class="pre">project_id</span></code> and <code class="docutils literal notranslate"><span class="pre">path</span></code>.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_azuredevops</span> <span class="k">as</span> <span class="nn">azuredevops</span>

<span class="n">project</span> <span class="o">=</span> <span class="n">azuredevops</span><span class="o">.</span><span class="n">Project</span><span class="p">(</span><span class="s2">&quot;project&quot;</span><span class="p">,</span>
    <span class="n">work_item_template</span><span class="o">=</span><span class="s2">&quot;Agile&quot;</span><span class="p">,</span>
    <span class="n">version_control</span><span class="o">=</span><span class="s2">&quot;Git&quot;</span><span class="p">,</span>
    <span class="n">visibility</span><span class="o">=</span><span class="s2">&quot;private&quot;</span><span class="p">,</span>
    <span class="n">description</span><span class="o">=</span><span class="s2">&quot;Managed by Terraform&quot;</span><span class="p">)</span>
<span class="n">project_readers</span> <span class="o">=</span> <span class="n">project</span><span class="o">.</span><span class="n">id</span><span class="o">.</span><span class="n">apply</span><span class="p">(</span><span class="k">lambda</span> <span class="nb">id</span><span class="p">:</span> <span class="n">azuredevops</span><span class="o">.</span><span class="n">get_group</span><span class="p">(</span><span class="n">project_id</span><span class="o">=</span><span class="nb">id</span><span class="p">,</span>
    <span class="n">name</span><span class="o">=</span><span class="s2">&quot;Readers&quot;</span><span class="p">))</span>
<span class="n">root_permissions</span> <span class="o">=</span> <span class="n">azuredevops</span><span class="o">.</span><span class="n">IterativePermissions</span><span class="p">(</span><span class="s2">&quot;root-permissions&quot;</span><span class="p">,</span>
    <span class="n">project_id</span><span class="o">=</span><span class="n">project</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">principal</span><span class="o">=</span><span class="n">azuredevops_group</span><span class="p">[</span><span class="s2">&quot;project-readers&quot;</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">],</span>
    <span class="n">permissions</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;CREATE_CHILDREN&quot;</span><span class="p">:</span> <span class="s2">&quot;Deny&quot;</span><span class="p">,</span>
        <span class="s2">&quot;GENERIC_READ&quot;</span><span class="p">:</span> <span class="s2">&quot;NotSet&quot;</span><span class="p">,</span>
        <span class="s2">&quot;DELETE&quot;</span><span class="p">:</span> <span class="s2">&quot;Deny&quot;</span><span class="p">,</span>
    <span class="p">})</span>
<span class="n">iteration_permissions</span> <span class="o">=</span> <span class="n">azuredevops</span><span class="o">.</span><span class="n">IterativePermissions</span><span class="p">(</span><span class="s2">&quot;iteration-permissions&quot;</span><span class="p">,</span>
    <span class="n">project_id</span><span class="o">=</span><span class="n">project</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">principal</span><span class="o">=</span><span class="n">azuredevops_group</span><span class="p">[</span><span class="s2">&quot;project-readers&quot;</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">],</span>
    <span class="n">path</span><span class="o">=</span><span class="s2">&quot;Iteration 1&quot;</span><span class="p">,</span>
    <span class="n">permissions</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;CREATE_CHILDREN&quot;</span><span class="p">:</span> <span class="s2">&quot;Allow&quot;</span><span class="p">,</span>
        <span class="s2">&quot;GENERIC_READ&quot;</span><span class="p">:</span> <span class="s2">&quot;NotSet&quot;</span><span class="p">,</span>
        <span class="s2">&quot;DELETE&quot;</span><span class="p">:</span> <span class="s2">&quot;Allow&quot;</span><span class="p">,</span>
    <span class="p">})</span>
</pre></div>
</div>
<ul class="simple">
<li><p><a class="reference external" href="https://docs.microsoft.com/en-us/rest/api/azure/devops/security/?view=azure-devops-rest-5.1">Azure DevOps Service REST API 5.1 - Security</a></p></li>
</ul>
<ul class="simple">
<li><p><strong>Project &amp; Team</strong>: vso.security_manage - Grants the ability to read, write, and manage security permissions.</p></li>
</ul>
<p>The resource does not support import.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>path</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the branch to assign the permissions.</p></li>
<li><p><strong>pulumi.Input</strong><strong>[</strong><strong>str</strong><strong>]</strong><strong>]</strong><strong>] </strong><strong>permissions</strong> (<em>pulumi.Input</em><em>[</em><em>Mapping</em><em>[</em><em>str</em><em>,</em>) – the permissions to assign. The following permissions are available.</p></li>
<li><p><strong>principal</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The <strong>group</strong> principal to assign the permissions.</p></li>
<li><p><strong>project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project to assign the permissions.</p></li>
<li><p><strong>replace</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Replace (<code class="docutils literal notranslate"><span class="pre">true</span></code>) or merge (<code class="docutils literal notranslate"><span class="pre">false</span></code>) the permissions. Default: <code class="docutils literal notranslate"><span class="pre">true</span></code></p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_azuredevops.IterativePermissions.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">path</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">permissions</span><span class="p">:</span> <span class="n">Union[Mapping[str, Union[str, Awaitable[str], Output[T]]], Awaitable[Mapping[str, Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">principal</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">replace</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_azuredevops.iterative_permissions.IterativePermissions<a class="headerlink" href="#pulumi_azuredevops.IterativePermissions.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing IterativePermissions resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>path</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the branch to assign the permissions.</p></li>
<li><p><strong>pulumi.Input</strong><strong>[</strong><strong>str</strong><strong>]</strong><strong>]</strong><strong>] </strong><strong>permissions</strong> (<em>pulumi.Input</em><em>[</em><em>Mapping</em><em>[</em><em>str</em><em>,</em>) – the permissions to assign. The following permissions are available.</p></li>
<li><p><strong>principal</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The <strong>group</strong> principal to assign the permissions.</p></li>
<li><p><strong>project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project to assign the permissions.</p></li>
<li><p><strong>replace</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Replace (<code class="docutils literal notranslate"><span class="pre">true</span></code>) or merge (<code class="docutils literal notranslate"><span class="pre">false</span></code>) the permissions. Default: <code class="docutils literal notranslate"><span class="pre">true</span></code></p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.IterativePermissions.path">
<em class="property">property </em><code class="sig-name descname">path</code><a class="headerlink" href="#pulumi_azuredevops.IterativePermissions.path" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the branch to assign the permissions.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.IterativePermissions.permissions">
<em class="property">property </em><code class="sig-name descname">permissions</code><a class="headerlink" href="#pulumi_azuredevops.IterativePermissions.permissions" title="Permalink to this definition">¶</a></dt>
<dd><p>the permissions to assign. The following permissions are available.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.IterativePermissions.principal">
<em class="property">property </em><code class="sig-name descname">principal</code><a class="headerlink" href="#pulumi_azuredevops.IterativePermissions.principal" title="Permalink to this definition">¶</a></dt>
<dd><p>The <strong>group</strong> principal to assign the permissions.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.IterativePermissions.project_id">
<em class="property">property </em><code class="sig-name descname">project_id</code><a class="headerlink" href="#pulumi_azuredevops.IterativePermissions.project_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project to assign the permissions.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.IterativePermissions.replace">
<em class="property">property </em><code class="sig-name descname">replace</code><a class="headerlink" href="#pulumi_azuredevops.IterativePermissions.replace" title="Permalink to this definition">¶</a></dt>
<dd><p>Replace (<code class="docutils literal notranslate"><span class="pre">true</span></code>) or merge (<code class="docutils literal notranslate"><span class="pre">false</span></code>) the permissions. Default: <code class="docutils literal notranslate"><span class="pre">true</span></code></p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.IterativePermissions.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuredevops.IterativePermissions.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azuredevops.IterativePermissions.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuredevops.IterativePermissions.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azuredevops.Pool">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azuredevops.</code><code class="sig-name descname">Pool</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auto_provision</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">pool_type</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuredevops.Pool" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an agent pool within Azure DevOps.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_azuredevops</span> <span class="k">as</span> <span class="nn">azuredevops</span>

<span class="n">pool</span> <span class="o">=</span> <span class="n">azuredevops</span><span class="o">.</span><span class="n">Pool</span><span class="p">(</span><span class="s2">&quot;pool&quot;</span><span class="p">,</span> <span class="n">auto_provision</span><span class="o">=</span><span class="kc">False</span><span class="p">)</span>
</pre></div>
</div>
<ul class="simple">
<li><p><a class="reference external" href="https://docs.microsoft.com/en-us/rest/api/azure/devops/distributedtask/pools?view=azure-devops-rest-5.1">Azure DevOps Service REST API 5.1 - Agent Pools</a></p></li>
</ul>
<p>Azure DevOps Agent Pools can be imported using the agent pool ID, e.g.</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>$ pulumi import azuredevops:index/pool:Pool azuredevops_agent_pool.pool <span class="m">42</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>auto_provision</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specifies whether or not a queue should be automatically provisioned for each project collection. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the agent pool.</p></li>
<li><p><strong>pool_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies whether the agent pool type is Automation or Deployment. Defaults to <code class="docutils literal notranslate"><span class="pre">automation</span></code>.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_azuredevops.Pool.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auto_provision</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">pool_type</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_azuredevops.pool.Pool<a class="headerlink" href="#pulumi_azuredevops.Pool.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Pool resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>auto_provision</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specifies whether or not a queue should be automatically provisioned for each project collection. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the agent pool.</p></li>
<li><p><strong>pool_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies whether the agent pool type is Automation or Deployment. Defaults to <code class="docutils literal notranslate"><span class="pre">automation</span></code>.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.Pool.auto_provision">
<em class="property">property </em><code class="sig-name descname">auto_provision</code><a class="headerlink" href="#pulumi_azuredevops.Pool.auto_provision" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies whether or not a queue should be automatically provisioned for each project collection. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.Pool.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_azuredevops.Pool.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the agent pool.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.Pool.pool_type">
<em class="property">property </em><code class="sig-name descname">pool_type</code><a class="headerlink" href="#pulumi_azuredevops.Pool.pool_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies whether the agent pool type is Automation or Deployment. Defaults to <code class="docutils literal notranslate"><span class="pre">automation</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.Pool.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuredevops.Pool.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azuredevops.Pool.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuredevops.Pool.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azuredevops.Project">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azuredevops.</code><code class="sig-name descname">Project</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">features</span><span class="p">:</span> <span class="n">Union[Mapping[str, Union[str, Awaitable[str], Output[T]]], Awaitable[Mapping[str, Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">version_control</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">visibility</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">work_item_template</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuredevops.Project" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a project within Azure DevOps.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_azuredevops</span> <span class="k">as</span> <span class="nn">azuredevops</span>

<span class="n">project</span> <span class="o">=</span> <span class="n">azuredevops</span><span class="o">.</span><span class="n">Project</span><span class="p">(</span><span class="s2">&quot;project&quot;</span><span class="p">,</span>
    <span class="n">description</span><span class="o">=</span><span class="s2">&quot;Test Project Description&quot;</span><span class="p">,</span>
    <span class="n">features</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;artifacts&quot;</span><span class="p">:</span> <span class="s2">&quot;disabled&quot;</span><span class="p">,</span>
        <span class="s2">&quot;testplans&quot;</span><span class="p">:</span> <span class="s2">&quot;disabled&quot;</span><span class="p">,</span>
    <span class="p">},</span>
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
<p>Azure DevOps Projects can be imported using the project name or by the project Guid, e.g.</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>   $ pulumi import azuredevops:index/project:Project project <span class="s2">&quot;Test Project&quot;</span>

or
</pre></div>
</div>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>$ pulumi import azuredevops:index/project:Project project <span class="m">00000000</span>-0000-0000-0000-000000000000
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Description of the Project.</p></li>
<li><p><strong>pulumi.Input</strong><strong>[</strong><strong>str</strong><strong>]</strong><strong>]</strong><strong>] </strong><strong>features</strong> (<em>pulumi.Input</em><em>[</em><em>Mapping</em><em>[</em><em>str</em><em>,</em>) – Defines the status (<code class="docutils literal notranslate"><span class="pre">enabled</span></code>, <code class="docutils literal notranslate"><span class="pre">disabled</span></code>) of the project features.<span class="raw-html-m2r"><br></span>
Valid features <code class="docutils literal notranslate"><span class="pre">boards</span></code>, <code class="docutils literal notranslate"><span class="pre">repositories</span></code>, <code class="docutils literal notranslate"><span class="pre">pipelines</span></code>, <code class="docutils literal notranslate"><span class="pre">testplans</span></code>, <code class="docutils literal notranslate"><span class="pre">artifacts</span></code></p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Project Name.</p></li>
<li><p><strong>version_control</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the version control system. Valid values: <code class="docutils literal notranslate"><span class="pre">Git</span></code> or <code class="docutils literal notranslate"><span class="pre">Tfvc</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">Git</span></code>.</p></li>
<li><p><strong>visibility</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the visibility of the Project. Valid values: <code class="docutils literal notranslate"><span class="pre">private</span></code> or <code class="docutils literal notranslate"><span class="pre">public</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">private</span></code>.</p></li>
<li><p><strong>work_item_template</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the work item template. Defaults to <code class="docutils literal notranslate"><span class="pre">Agile</span></code>.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_azuredevops.Project.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">features</span><span class="p">:</span> <span class="n">Union[Mapping[str, Union[str, Awaitable[str], Output[T]]], Awaitable[Mapping[str, Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">process_template_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">version_control</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">visibility</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">work_item_template</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_azuredevops.project.Project<a class="headerlink" href="#pulumi_azuredevops.Project.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Project resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Description of the Project.</p></li>
<li><p><strong>pulumi.Input</strong><strong>[</strong><strong>str</strong><strong>]</strong><strong>]</strong><strong>] </strong><strong>features</strong> (<em>pulumi.Input</em><em>[</em><em>Mapping</em><em>[</em><em>str</em><em>,</em>) – Defines the status (<code class="docutils literal notranslate"><span class="pre">enabled</span></code>, <code class="docutils literal notranslate"><span class="pre">disabled</span></code>) of the project features.<span class="raw-html-m2r"><br></span>
Valid features <code class="docutils literal notranslate"><span class="pre">boards</span></code>, <code class="docutils literal notranslate"><span class="pre">repositories</span></code>, <code class="docutils literal notranslate"><span class="pre">pipelines</span></code>, <code class="docutils literal notranslate"><span class="pre">testplans</span></code>, <code class="docutils literal notranslate"><span class="pre">artifacts</span></code></p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Project Name.</p></li>
<li><p><strong>process_template_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Process Template ID used by the Project.</p></li>
<li><p><strong>version_control</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the version control system. Valid values: <code class="docutils literal notranslate"><span class="pre">Git</span></code> or <code class="docutils literal notranslate"><span class="pre">Tfvc</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">Git</span></code>.</p></li>
<li><p><strong>visibility</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the visibility of the Project. Valid values: <code class="docutils literal notranslate"><span class="pre">private</span></code> or <code class="docutils literal notranslate"><span class="pre">public</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">private</span></code>.</p></li>
<li><p><strong>work_item_template</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Specifies the work item template. Defaults to <code class="docutils literal notranslate"><span class="pre">Agile</span></code>.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.Project.description">
<em class="property">property </em><code class="sig-name descname">description</code><a class="headerlink" href="#pulumi_azuredevops.Project.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The Description of the Project.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.Project.features">
<em class="property">property </em><code class="sig-name descname">features</code><a class="headerlink" href="#pulumi_azuredevops.Project.features" title="Permalink to this definition">¶</a></dt>
<dd><p>Defines the status (<code class="docutils literal notranslate"><span class="pre">enabled</span></code>, <code class="docutils literal notranslate"><span class="pre">disabled</span></code>) of the project features.<span class="raw-html-m2r"><br></span>
Valid features <code class="docutils literal notranslate"><span class="pre">boards</span></code>, <code class="docutils literal notranslate"><span class="pre">repositories</span></code>, <code class="docutils literal notranslate"><span class="pre">pipelines</span></code>, <code class="docutils literal notranslate"><span class="pre">testplans</span></code>, <code class="docutils literal notranslate"><span class="pre">artifacts</span></code></p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.Project.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_azuredevops.Project.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The Project Name.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.Project.process_template_id">
<em class="property">property </em><code class="sig-name descname">process_template_id</code><a class="headerlink" href="#pulumi_azuredevops.Project.process_template_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The Process Template ID used by the Project.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.Project.version_control">
<em class="property">property </em><code class="sig-name descname">version_control</code><a class="headerlink" href="#pulumi_azuredevops.Project.version_control" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the version control system. Valid values: <code class="docutils literal notranslate"><span class="pre">Git</span></code> or <code class="docutils literal notranslate"><span class="pre">Tfvc</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">Git</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.Project.visibility">
<em class="property">property </em><code class="sig-name descname">visibility</code><a class="headerlink" href="#pulumi_azuredevops.Project.visibility" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the visibility of the Project. Valid values: <code class="docutils literal notranslate"><span class="pre">private</span></code> or <code class="docutils literal notranslate"><span class="pre">public</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">private</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.Project.work_item_template">
<em class="property">property </em><code class="sig-name descname">work_item_template</code><a class="headerlink" href="#pulumi_azuredevops.Project.work_item_template" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies the work item template. Defaults to <code class="docutils literal notranslate"><span class="pre">Agile</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.Project.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuredevops.Project.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azuredevops.Project.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuredevops.Project.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azuredevops.ProjectFeatures">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azuredevops.</code><code class="sig-name descname">ProjectFeatures</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">features</span><span class="p">:</span> <span class="n">Union[Mapping[str, Union[str, Awaitable[str], Output[T]]], Awaitable[Mapping[str, Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuredevops.ProjectFeatures" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages features for Azure DevOps projects</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_azuredevops</span> <span class="k">as</span> <span class="nn">azuredevops</span>

<span class="n">tf_project_test_001</span> <span class="o">=</span> <span class="n">azuredevops</span><span class="o">.</span><span class="n">get_project</span><span class="p">(</span><span class="n">name</span><span class="o">=</span><span class="s2">&quot;Test Project&quot;</span><span class="p">)</span>
<span class="n">my_project_features</span> <span class="o">=</span> <span class="n">azuredevops</span><span class="o">.</span><span class="n">ProjectFeatures</span><span class="p">(</span><span class="s2">&quot;my-project-features&quot;</span><span class="p">,</span>
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
<p>Azure DevOps feature settings can be imported using the project id, e.g.</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>$ pulumi import azuredevops:index/projectFeatures:ProjectFeatures project_id 2785562e-8f45-4534-a10e-b9ca1666b17e
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>pulumi.Input</strong><strong>[</strong><strong>str</strong><strong>]</strong><strong>]</strong><strong>] </strong><strong>features</strong> (<em>pulumi.Input</em><em>[</em><em>Mapping</em><em>[</em><em>str</em><em>,</em>) – Defines the status (<code class="docutils literal notranslate"><span class="pre">enabled</span></code>, <code class="docutils literal notranslate"><span class="pre">disabled</span></code>) of the project features.<span class="raw-html-m2r"><br></span>
Valid features <code class="docutils literal notranslate"><span class="pre">boards</span></code>, <code class="docutils literal notranslate"><span class="pre">repositories</span></code>, <code class="docutils literal notranslate"><span class="pre">pipelines</span></code>, <code class="docutils literal notranslate"><span class="pre">testplans</span></code>, <code class="docutils literal notranslate"><span class="pre">artifacts</span></code></p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_azuredevops.ProjectFeatures.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">features</span><span class="p">:</span> <span class="n">Union[Mapping[str, Union[str, Awaitable[str], Output[T]]], Awaitable[Mapping[str, Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_azuredevops.project_features.ProjectFeatures<a class="headerlink" href="#pulumi_azuredevops.ProjectFeatures.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ProjectFeatures resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>pulumi.Input</strong><strong>[</strong><strong>str</strong><strong>]</strong><strong>]</strong><strong>] </strong><strong>features</strong> (<em>pulumi.Input</em><em>[</em><em>Mapping</em><em>[</em><em>str</em><em>,</em>) – Defines the status (<code class="docutils literal notranslate"><span class="pre">enabled</span></code>, <code class="docutils literal notranslate"><span class="pre">disabled</span></code>) of the project features.<span class="raw-html-m2r"><br></span>
Valid features <code class="docutils literal notranslate"><span class="pre">boards</span></code>, <code class="docutils literal notranslate"><span class="pre">repositories</span></code>, <code class="docutils literal notranslate"><span class="pre">pipelines</span></code>, <code class="docutils literal notranslate"><span class="pre">testplans</span></code>, <code class="docutils literal notranslate"><span class="pre">artifacts</span></code></p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.ProjectFeatures.features">
<em class="property">property </em><code class="sig-name descname">features</code><a class="headerlink" href="#pulumi_azuredevops.ProjectFeatures.features" title="Permalink to this definition">¶</a></dt>
<dd><p>Defines the status (<code class="docutils literal notranslate"><span class="pre">enabled</span></code>, <code class="docutils literal notranslate"><span class="pre">disabled</span></code>) of the project features.<span class="raw-html-m2r"><br></span>
Valid features <code class="docutils literal notranslate"><span class="pre">boards</span></code>, <code class="docutils literal notranslate"><span class="pre">repositories</span></code>, <code class="docutils literal notranslate"><span class="pre">pipelines</span></code>, <code class="docutils literal notranslate"><span class="pre">testplans</span></code>, <code class="docutils literal notranslate"><span class="pre">artifacts</span></code></p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.ProjectFeatures.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuredevops.ProjectFeatures.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azuredevops.ProjectFeatures.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuredevops.ProjectFeatures.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azuredevops.ProjectPermissions">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azuredevops.</code><code class="sig-name descname">ProjectPermissions</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">permissions</span><span class="p">:</span> <span class="n">Union[Mapping[str, Union[str, Awaitable[str], Output[T]]], Awaitable[Mapping[str, Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">principal</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">replace</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuredevops.ProjectPermissions" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages permissions for a AzureDevOps project</p>
<blockquote>
<div><p><strong>Note</strong> Permissions can be assigned to group principals and not to single user principals.</p>
</div></blockquote>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_azuredevops</span> <span class="k">as</span> <span class="nn">azuredevops</span>

<span class="n">project</span> <span class="o">=</span> <span class="n">azuredevops</span><span class="o">.</span><span class="n">Project</span><span class="p">(</span><span class="s2">&quot;project&quot;</span><span class="p">,</span>
    <span class="n">description</span><span class="o">=</span><span class="s2">&quot;Test Project Description&quot;</span><span class="p">,</span>
    <span class="n">visibility</span><span class="o">=</span><span class="s2">&quot;private&quot;</span><span class="p">,</span>
    <span class="n">version_control</span><span class="o">=</span><span class="s2">&quot;Git&quot;</span><span class="p">,</span>
    <span class="n">work_item_template</span><span class="o">=</span><span class="s2">&quot;Agile&quot;</span><span class="p">)</span>
<span class="n">project_readers</span> <span class="o">=</span> <span class="n">project</span><span class="o">.</span><span class="n">id</span><span class="o">.</span><span class="n">apply</span><span class="p">(</span><span class="k">lambda</span> <span class="nb">id</span><span class="p">:</span> <span class="n">azuredevops</span><span class="o">.</span><span class="n">get_group</span><span class="p">(</span><span class="n">project_id</span><span class="o">=</span><span class="nb">id</span><span class="p">,</span>
    <span class="n">name</span><span class="o">=</span><span class="s2">&quot;Readers&quot;</span><span class="p">))</span>
<span class="n">project_perm</span> <span class="o">=</span> <span class="n">azuredevops</span><span class="o">.</span><span class="n">ProjectPermissions</span><span class="p">(</span><span class="s2">&quot;project-perm&quot;</span><span class="p">,</span>
    <span class="n">project_id</span><span class="o">=</span><span class="n">project</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">principal</span><span class="o">=</span><span class="n">project_readers</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">permissions</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;DELETE&quot;</span><span class="p">:</span> <span class="s2">&quot;Deny&quot;</span><span class="p">,</span>
        <span class="s2">&quot;EDIT_BUILD_STATUS&quot;</span><span class="p">:</span> <span class="s2">&quot;NotSet&quot;</span><span class="p">,</span>
        <span class="s2">&quot;WORK_ITEM_MOVE&quot;</span><span class="p">:</span> <span class="s2">&quot;Allow&quot;</span><span class="p">,</span>
        <span class="s2">&quot;DELETE_TEST_RESULTS&quot;</span><span class="p">:</span> <span class="s2">&quot;Deny&quot;</span><span class="p">,</span>
    <span class="p">})</span>
</pre></div>
</div>
<ul class="simple">
<li><p><a class="reference external" href="https://docs.microsoft.com/en-us/rest/api/azure/devops/security/?view=azure-devops-rest-5.1">Azure DevOps Service REST API 5.1 - Security</a></p></li>
</ul>
<ul class="simple">
<li><p><strong>Project &amp; Team</strong>: vso.security_manage - Grants the ability to read, write, and manage security permissions.</p></li>
</ul>
<p>The resource does not support import.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>pulumi.Input</strong><strong>[</strong><strong>str</strong><strong>]</strong><strong>]</strong><strong>] </strong><strong>permissions</strong> (<em>pulumi.Input</em><em>[</em><em>Mapping</em><em>[</em><em>str</em><em>,</em>) – the permissions to assign. The following permissions are available</p></li>
<li><p><strong>principal</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The <strong>group</strong> principal to assign the permissions.</p></li>
<li><p><strong>project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project to assign the permissions.</p></li>
<li><p><strong>replace</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Replace (<code class="docutils literal notranslate"><span class="pre">true</span></code>) or merge (<code class="docutils literal notranslate"><span class="pre">false</span></code>) the permissions. Default: <code class="docutils literal notranslate"><span class="pre">true</span></code></p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_azuredevops.ProjectPermissions.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">permissions</span><span class="p">:</span> <span class="n">Union[Mapping[str, Union[str, Awaitable[str], Output[T]]], Awaitable[Mapping[str, Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">principal</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">replace</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_azuredevops.project_permissions.ProjectPermissions<a class="headerlink" href="#pulumi_azuredevops.ProjectPermissions.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ProjectPermissions resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>pulumi.Input</strong><strong>[</strong><strong>str</strong><strong>]</strong><strong>]</strong><strong>] </strong><strong>permissions</strong> (<em>pulumi.Input</em><em>[</em><em>Mapping</em><em>[</em><em>str</em><em>,</em>) – the permissions to assign. The following permissions are available</p></li>
<li><p><strong>principal</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The <strong>group</strong> principal to assign the permissions.</p></li>
<li><p><strong>project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project to assign the permissions.</p></li>
<li><p><strong>replace</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Replace (<code class="docutils literal notranslate"><span class="pre">true</span></code>) or merge (<code class="docutils literal notranslate"><span class="pre">false</span></code>) the permissions. Default: <code class="docutils literal notranslate"><span class="pre">true</span></code></p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.ProjectPermissions.permissions">
<em class="property">property </em><code class="sig-name descname">permissions</code><a class="headerlink" href="#pulumi_azuredevops.ProjectPermissions.permissions" title="Permalink to this definition">¶</a></dt>
<dd><p>the permissions to assign. The following permissions are available</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.ProjectPermissions.principal">
<em class="property">property </em><code class="sig-name descname">principal</code><a class="headerlink" href="#pulumi_azuredevops.ProjectPermissions.principal" title="Permalink to this definition">¶</a></dt>
<dd><p>The <strong>group</strong> principal to assign the permissions.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.ProjectPermissions.project_id">
<em class="property">property </em><code class="sig-name descname">project_id</code><a class="headerlink" href="#pulumi_azuredevops.ProjectPermissions.project_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project to assign the permissions.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.ProjectPermissions.replace">
<em class="property">property </em><code class="sig-name descname">replace</code><a class="headerlink" href="#pulumi_azuredevops.ProjectPermissions.replace" title="Permalink to this definition">¶</a></dt>
<dd><p>Replace (<code class="docutils literal notranslate"><span class="pre">true</span></code>) or merge (<code class="docutils literal notranslate"><span class="pre">false</span></code>) the permissions. Default: <code class="docutils literal notranslate"><span class="pre">true</span></code></p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.ProjectPermissions.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuredevops.ProjectPermissions.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azuredevops.ProjectPermissions.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuredevops.ProjectPermissions.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azuredevops.Provider">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azuredevops.</code><code class="sig-name descname">Provider</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">org_service_url</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">personal_access_token</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuredevops.Provider" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider type for the azuredevops package. By default, resources use package-wide configuration
settings, however an explicit <code class="docutils literal notranslate"><span class="pre">Provider</span></code> instance may be created and passed during resource
construction to achieve fine-grained programmatic control over provider settings. See the
<a class="reference external" href="https://www.pulumi.com/docs/reference/programming-model/#providers">documentation</a> for more information.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>org_service_url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The url of the Azure DevOps instance which should be used.</p></li>
<li><p><strong>personal_access_token</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The personal access token which should be used.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_azuredevops.Provider.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuredevops.Provider.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azuredevops.Provider.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuredevops.Provider.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azuredevops.Queue">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azuredevops.</code><code class="sig-name descname">Queue</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">agent_pool_id</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuredevops.Queue" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages an agent queue within Azure DevOps. In the UI, this is equivalent to adding an
Organization defined pool to a project.</p>
<p>The created queue is not authorized for use by all pipelines in the project. However,
the <code class="docutils literal notranslate"><span class="pre">ResourceAuthorization</span></code> resource can be used to grant authorization.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_azuredevops</span> <span class="k">as</span> <span class="nn">azuredevops</span>

<span class="n">project</span> <span class="o">=</span> <span class="n">azuredevops</span><span class="o">.</span><span class="n">Project</span><span class="p">(</span><span class="s2">&quot;project&quot;</span><span class="p">)</span>
<span class="n">pool</span> <span class="o">=</span> <span class="n">azuredevops</span><span class="o">.</span><span class="n">get_pool</span><span class="p">(</span><span class="n">name</span><span class="o">=</span><span class="s2">&quot;contoso-pool&quot;</span><span class="p">)</span>
<span class="n">queue</span> <span class="o">=</span> <span class="n">azuredevops</span><span class="o">.</span><span class="n">Queue</span><span class="p">(</span><span class="s2">&quot;queue&quot;</span><span class="p">,</span>
    <span class="n">project_id</span><span class="o">=</span><span class="n">project</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">agent_pool_id</span><span class="o">=</span><span class="n">pool</span><span class="o">.</span><span class="n">id</span><span class="p">)</span>
<span class="c1"># Grant acccess to queue to all pipelines in the project</span>
<span class="n">auth</span> <span class="o">=</span> <span class="n">azuredevops</span><span class="o">.</span><span class="n">ResourceAuthorization</span><span class="p">(</span><span class="s2">&quot;auth&quot;</span><span class="p">,</span>
    <span class="n">project_id</span><span class="o">=</span><span class="n">project</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">resource_id</span><span class="o">=</span><span class="n">queue</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="nb">type</span><span class="o">=</span><span class="s2">&quot;queue&quot;</span><span class="p">,</span>
    <span class="n">authorized</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
</pre></div>
</div>
<ul class="simple">
<li><p><a class="reference external" href="https://docs.microsoft.com/en-us/rest/api/azure/devops/distributedtask/queues?view=azure-devops-rest-5.1">Azure DevOps Service REST API 5.1 - Agent Queues</a></p></li>
</ul>
<p>Azure DevOps Agent Pools can be imported using the project ID and agent queue ID, e.g.</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>$ pulumi import azuredevops:index/queue:Queue q 44cbf614-4dfd-4032-9fae-87b0da3bec30/1381
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>agent_pool_id</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The ID of the organization agent pool.</p></li>
<li><p><strong>project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which to create the resource.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_azuredevops.Queue.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">agent_pool_id</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_azuredevops.queue.Queue<a class="headerlink" href="#pulumi_azuredevops.Queue.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Queue resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>agent_pool_id</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The ID of the organization agent pool.</p></li>
<li><p><strong>project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which to create the resource.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.Queue.agent_pool_id">
<em class="property">property </em><code class="sig-name descname">agent_pool_id</code><a class="headerlink" href="#pulumi_azuredevops.Queue.agent_pool_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the organization agent pool.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.Queue.project_id">
<em class="property">property </em><code class="sig-name descname">project_id</code><a class="headerlink" href="#pulumi_azuredevops.Queue.project_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which to create the resource.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.Queue.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuredevops.Queue.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azuredevops.Queue.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuredevops.Queue.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azuredevops.ResourceAuthorization">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azuredevops.</code><code class="sig-name descname">ResourceAuthorization</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">authorized</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">definition_id</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuredevops.ResourceAuthorization" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages authorization of resources, e.g. for access in build pipelines.</p>
<p>Currently supported resources: service endpoint (aka service connection, endpoint).</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_azuredevops</span> <span class="k">as</span> <span class="nn">azuredevops</span>

<span class="n">project</span> <span class="o">=</span> <span class="n">azuredevops</span><span class="o">.</span><span class="n">Project</span><span class="p">(</span><span class="s2">&quot;project&quot;</span><span class="p">)</span>
<span class="n">bitbucket_account</span> <span class="o">=</span> <span class="n">azuredevops</span><span class="o">.</span><span class="n">ServiceEndpointBitBucket</span><span class="p">(</span><span class="s2">&quot;bitbucketAccount&quot;</span><span class="p">,</span>
    <span class="n">project_id</span><span class="o">=</span><span class="n">project</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">username</span><span class="o">=</span><span class="s2">&quot;xxxx&quot;</span><span class="p">,</span>
    <span class="n">password</span><span class="o">=</span><span class="s2">&quot;xxxx&quot;</span><span class="p">,</span>
    <span class="n">service_endpoint_name</span><span class="o">=</span><span class="s2">&quot;test-bitbucket&quot;</span><span class="p">,</span>
    <span class="n">description</span><span class="o">=</span><span class="s2">&quot;test&quot;</span><span class="p">)</span>
<span class="n">auth</span> <span class="o">=</span> <span class="n">azuredevops</span><span class="o">.</span><span class="n">ResourceAuthorization</span><span class="p">(</span><span class="s2">&quot;auth&quot;</span><span class="p">,</span>
    <span class="n">project_id</span><span class="o">=</span><span class="n">project</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">resource_id</span><span class="o">=</span><span class="n">bitbucket_account</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">authorized</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
</pre></div>
</div>
<ul class="simple">
<li><p><a class="reference external" href="https://docs.microsoft.com/en-us/rest/api/azure/devops/build/resources/authorize%20definition%20resources?view=azure-devops-rest-5.1">Azure DevOps Service REST API 5.1 - Authorize Definition Resource</a></p></li>
</ul>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>authorized</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Set to true to allow public access in the project. Type: boolean.</p></li>
<li><p><strong>definition_id</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The ID of the build definition to authorize. Type: string.</p></li>
<li><p><strong>project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The project ID or project name. Type: string.</p></li>
<li><p><strong>resource_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the resource to authorize. Type: string.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of the resource to authorize. Type: string. Valid values: <code class="docutils literal notranslate"><span class="pre">endpoint</span></code>, <code class="docutils literal notranslate"><span class="pre">queue</span></code>, <code class="docutils literal notranslate"><span class="pre">variablegroup</span></code>. Default value: <code class="docutils literal notranslate"><span class="pre">endpoint</span></code>.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_azuredevops.ResourceAuthorization.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">authorized</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">definition_id</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">type</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_azuredevops.resource_authorization.ResourceAuthorization<a class="headerlink" href="#pulumi_azuredevops.ResourceAuthorization.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ResourceAuthorization resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>authorized</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Set to true to allow public access in the project. Type: boolean.</p></li>
<li><p><strong>definition_id</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The ID of the build definition to authorize. Type: string.</p></li>
<li><p><strong>project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The project ID or project name. Type: string.</p></li>
<li><p><strong>resource_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the resource to authorize. Type: string.</p></li>
<li><p><strong>type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of the resource to authorize. Type: string. Valid values: <code class="docutils literal notranslate"><span class="pre">endpoint</span></code>, <code class="docutils literal notranslate"><span class="pre">queue</span></code>, <code class="docutils literal notranslate"><span class="pre">variablegroup</span></code>. Default value: <code class="docutils literal notranslate"><span class="pre">endpoint</span></code>.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.ResourceAuthorization.authorized">
<em class="property">property </em><code class="sig-name descname">authorized</code><a class="headerlink" href="#pulumi_azuredevops.ResourceAuthorization.authorized" title="Permalink to this definition">¶</a></dt>
<dd><p>Set to true to allow public access in the project. Type: boolean.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.ResourceAuthorization.definition_id">
<em class="property">property </em><code class="sig-name descname">definition_id</code><a class="headerlink" href="#pulumi_azuredevops.ResourceAuthorization.definition_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the build definition to authorize. Type: string.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.ResourceAuthorization.project_id">
<em class="property">property </em><code class="sig-name descname">project_id</code><a class="headerlink" href="#pulumi_azuredevops.ResourceAuthorization.project_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The project ID or project name. Type: string.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.ResourceAuthorization.resource_id">
<em class="property">property </em><code class="sig-name descname">resource_id</code><a class="headerlink" href="#pulumi_azuredevops.ResourceAuthorization.resource_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the resource to authorize. Type: string.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.ResourceAuthorization.type">
<em class="property">property </em><code class="sig-name descname">type</code><a class="headerlink" href="#pulumi_azuredevops.ResourceAuthorization.type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of the resource to authorize. Type: string. Valid values: <code class="docutils literal notranslate"><span class="pre">endpoint</span></code>, <code class="docutils literal notranslate"><span class="pre">queue</span></code>, <code class="docutils literal notranslate"><span class="pre">variablegroup</span></code>. Default value: <code class="docutils literal notranslate"><span class="pre">endpoint</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.ResourceAuthorization.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuredevops.ResourceAuthorization.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azuredevops.ResourceAuthorization.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuredevops.ResourceAuthorization.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azuredevops.ServiceEndpointAws">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azuredevops.</code><code class="sig-name descname">ServiceEndpointAws</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">access_key_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">authorization</span><span class="p">:</span> <span class="n">Union[Mapping[str, Union[str, Awaitable[str], Output[T]]], Awaitable[Mapping[str, Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">external_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">role_session_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">role_to_assume</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">secret_access_key</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_endpoint_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">session_token</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuredevops.ServiceEndpointAws" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a AWS service endpoint within Azure DevOps. Using this service endpoint requires you to first install <a class="reference external" href="https://marketplace.visualstudio.com/items?itemName=AmazonWebServices.aws-vsts-tools">AWS Toolkit for Azure DevOps</a>.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_azuredevops</span> <span class="k">as</span> <span class="nn">azuredevops</span>

<span class="n">project</span> <span class="o">=</span> <span class="n">azuredevops</span><span class="o">.</span><span class="n">Project</span><span class="p">(</span><span class="s2">&quot;project&quot;</span><span class="p">,</span>
    <span class="n">visibility</span><span class="o">=</span><span class="s2">&quot;private&quot;</span><span class="p">,</span>
    <span class="n">version_control</span><span class="o">=</span><span class="s2">&quot;Git&quot;</span><span class="p">,</span>
    <span class="n">work_item_template</span><span class="o">=</span><span class="s2">&quot;Agile&quot;</span><span class="p">)</span>
<span class="n">serviceendpoint</span> <span class="o">=</span> <span class="n">azuredevops</span><span class="o">.</span><span class="n">ServiceEndpointAws</span><span class="p">(</span><span class="s2">&quot;serviceendpoint&quot;</span><span class="p">,</span>
    <span class="n">project_id</span><span class="o">=</span><span class="n">project</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">service_endpoint_name</span><span class="o">=</span><span class="s2">&quot;Sample AWS&quot;</span><span class="p">,</span>
    <span class="n">description</span><span class="o">=</span><span class="s2">&quot;Managed by AzureDevOps&quot;</span><span class="p">,</span>
    <span class="n">access_key_id</span><span class="o">=</span><span class="s2">&quot;00000000-0000-0000-0000-000000000000&quot;</span><span class="p">,</span>
    <span class="n">secret_access_key</span><span class="o">=</span><span class="s2">&quot;accesskey&quot;</span><span class="p">)</span>
</pre></div>
</div>
<ul class="simple">
<li><p><a class="reference external" href="https://github.com/aws/aws-toolkit-azure-devops">aws-toolkit-azure-devops</a></p></li>
<li><p><a class="reference external" href="https://docs.microsoft.com/en-us/rest/api/azure/devops/serviceendpoint/endpoints?view=azure-devops-rest-5.1">Azure DevOps Service REST API 5.1 - Agent Pools</a></p></li>
</ul>
<p>Azure DevOps Service Endpoint AWS can be imported using <strong>projectID/serviceEndpointID</strong> or <strong>projectName/serviceEndpointID</strong></p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>$ pulumi import azuredevops:index/serviceEndpointAws:ServiceEndpointAws azuredevops_serviceendpoint_aws.serviceendpoint <span class="m">00000000</span>-0000-0000-0000-000000000000/00000000-0000-0000-0000-000000000000
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>access_key_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The AWS access key ID for signing programmatic requests.</p></li>
<li><p><strong>external_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A unique identifier that is used by third parties when assuming roles in their customers’ accounts, aka cross-account role access.</p></li>
<li><p><strong>project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The project ID or project name.</p></li>
<li><p><strong>role_session_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Optional identifier for the assumed role session.</p></li>
<li><p><strong>role_to_assume</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Amazon Resource Name (ARN) of the role to assume.</p></li>
<li><p><strong>secret_access_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The AWS secret access key for signing programmatic requests.</p></li>
<li><p><strong>service_endpoint_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Service Endpoint name.</p></li>
<li><p><strong>session_token</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The AWS session token for signing programmatic requests.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_azuredevops.ServiceEndpointAws.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">access_key_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">authorization</span><span class="p">:</span> <span class="n">Union[Mapping[str, Union[str, Awaitable[str], Output[T]]], Awaitable[Mapping[str, Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">external_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">role_session_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">role_to_assume</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">secret_access_key</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">secret_access_key_hash</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_endpoint_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">session_token</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">session_token_hash</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_azuredevops.service_endpoint_aws.ServiceEndpointAws<a class="headerlink" href="#pulumi_azuredevops.ServiceEndpointAws.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ServiceEndpointAws resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>access_key_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The AWS access key ID for signing programmatic requests.</p></li>
<li><p><strong>external_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A unique identifier that is used by third parties when assuming roles in their customers’ accounts, aka cross-account role access.</p></li>
<li><p><strong>project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The project ID or project name.</p></li>
<li><p><strong>role_session_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Optional identifier for the assumed role session.</p></li>
<li><p><strong>role_to_assume</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Amazon Resource Name (ARN) of the role to assume.</p></li>
<li><p><strong>secret_access_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The AWS secret access key for signing programmatic requests.</p></li>
<li><p><strong>secret_access_key_hash</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A bcrypted hash of the attribute ‘secret_access_key’</p></li>
<li><p><strong>service_endpoint_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Service Endpoint name.</p></li>
<li><p><strong>session_token</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The AWS session token for signing programmatic requests.</p></li>
<li><p><strong>session_token_hash</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A bcrypted hash of the attribute ‘session_token’</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.ServiceEndpointAws.access_key_id">
<em class="property">property </em><code class="sig-name descname">access_key_id</code><a class="headerlink" href="#pulumi_azuredevops.ServiceEndpointAws.access_key_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The AWS access key ID for signing programmatic requests.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.ServiceEndpointAws.external_id">
<em class="property">property </em><code class="sig-name descname">external_id</code><a class="headerlink" href="#pulumi_azuredevops.ServiceEndpointAws.external_id" title="Permalink to this definition">¶</a></dt>
<dd><p>A unique identifier that is used by third parties when assuming roles in their customers’ accounts, aka cross-account role access.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.ServiceEndpointAws.project_id">
<em class="property">property </em><code class="sig-name descname">project_id</code><a class="headerlink" href="#pulumi_azuredevops.ServiceEndpointAws.project_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The project ID or project name.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.ServiceEndpointAws.role_session_name">
<em class="property">property </em><code class="sig-name descname">role_session_name</code><a class="headerlink" href="#pulumi_azuredevops.ServiceEndpointAws.role_session_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Optional identifier for the assumed role session.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.ServiceEndpointAws.role_to_assume">
<em class="property">property </em><code class="sig-name descname">role_to_assume</code><a class="headerlink" href="#pulumi_azuredevops.ServiceEndpointAws.role_to_assume" title="Permalink to this definition">¶</a></dt>
<dd><p>The Amazon Resource Name (ARN) of the role to assume.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.ServiceEndpointAws.secret_access_key">
<em class="property">property </em><code class="sig-name descname">secret_access_key</code><a class="headerlink" href="#pulumi_azuredevops.ServiceEndpointAws.secret_access_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The AWS secret access key for signing programmatic requests.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.ServiceEndpointAws.secret_access_key_hash">
<em class="property">property </em><code class="sig-name descname">secret_access_key_hash</code><a class="headerlink" href="#pulumi_azuredevops.ServiceEndpointAws.secret_access_key_hash" title="Permalink to this definition">¶</a></dt>
<dd><p>A bcrypted hash of the attribute ‘secret_access_key’</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.ServiceEndpointAws.service_endpoint_name">
<em class="property">property </em><code class="sig-name descname">service_endpoint_name</code><a class="headerlink" href="#pulumi_azuredevops.ServiceEndpointAws.service_endpoint_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The Service Endpoint name.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.ServiceEndpointAws.session_token">
<em class="property">property </em><code class="sig-name descname">session_token</code><a class="headerlink" href="#pulumi_azuredevops.ServiceEndpointAws.session_token" title="Permalink to this definition">¶</a></dt>
<dd><p>The AWS session token for signing programmatic requests.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.ServiceEndpointAws.session_token_hash">
<em class="property">property </em><code class="sig-name descname">session_token_hash</code><a class="headerlink" href="#pulumi_azuredevops.ServiceEndpointAws.session_token_hash" title="Permalink to this definition">¶</a></dt>
<dd><p>A bcrypted hash of the attribute ‘session_token’</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.ServiceEndpointAws.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuredevops.ServiceEndpointAws.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azuredevops.ServiceEndpointAws.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuredevops.ServiceEndpointAws.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azuredevops.ServiceEndpointAzureEcr">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azuredevops.</code><code class="sig-name descname">ServiceEndpointAzureEcr</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">authorization</span><span class="p">:</span> <span class="n">Union[Mapping[str, Union[str, Awaitable[str], Output[T]]], Awaitable[Mapping[str, Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">azurecr_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">azurecr_spn_tenantid</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">azurecr_subscription_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">azurecr_subscription_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_endpoint_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuredevops.ServiceEndpointAzureEcr" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Azure Container Registry service endpoint within Azure DevOps.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_azuredevops</span> <span class="k">as</span> <span class="nn">azuredevops</span>

<span class="n">project</span> <span class="o">=</span> <span class="n">azuredevops</span><span class="o">.</span><span class="n">Project</span><span class="p">(</span><span class="s2">&quot;project&quot;</span><span class="p">,</span>
    <span class="n">visibility</span><span class="o">=</span><span class="s2">&quot;private&quot;</span><span class="p">,</span>
    <span class="n">version_control</span><span class="o">=</span><span class="s2">&quot;Git&quot;</span><span class="p">,</span>
    <span class="n">work_item_template</span><span class="o">=</span><span class="s2">&quot;Agile&quot;</span><span class="p">)</span>
<span class="c1"># azure container registry service connection</span>
<span class="n">azurecr</span> <span class="o">=</span> <span class="n">azuredevops</span><span class="o">.</span><span class="n">ServiceEndpointAzureEcr</span><span class="p">(</span><span class="s2">&quot;azurecr&quot;</span><span class="p">,</span>
    <span class="n">project_id</span><span class="o">=</span><span class="n">project</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">service_endpoint_name</span><span class="o">=</span><span class="s2">&quot;Sample AzureCR&quot;</span><span class="p">,</span>
    <span class="n">resource_group</span><span class="o">=</span><span class="s2">&quot;sample-rg&quot;</span><span class="p">,</span>
    <span class="n">azurecr_spn_tenantid</span><span class="o">=</span><span class="s2">&quot;00000000-0000-0000-0000-000000000000&quot;</span><span class="p">,</span>
    <span class="n">azurecr_name</span><span class="o">=</span><span class="s2">&quot;sampleAcr&quot;</span><span class="p">,</span>
    <span class="n">azurecr_subscription_id</span><span class="o">=</span><span class="s2">&quot;00000000-0000-0000-0000-000000000000&quot;</span><span class="p">,</span>
    <span class="n">azurecr_subscription_name</span><span class="o">=</span><span class="s2">&quot;sampleSub&quot;</span><span class="p">)</span>
</pre></div>
</div>
<ul class="simple">
<li><p><a class="reference external" href="https://docs.microsoft.com/en-us/rest/api/azure/devops/serviceendpoint/endpoints?view=azure-devops-rest-5.1">Azure DevOps Service REST API 5.1 - Service Endpoints</a></p></li>
<li><p><a class="reference external" href="https://docs.microsoft.com/en-us/rest/api/containerregistry/">Azure Container Registry REST API</a></p></li>
</ul>
<p>Azure DevOps Service Endpoint Azure Container Registry can be imported using <strong>projectID/serviceEndpointID</strong> or <strong>projectName/serviceEndpointID</strong></p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>$ pulumi import azuredevops:index/serviceEndpointAzureEcr:ServiceEndpointAzureEcr azuredevops_serviceendpoint_azurecr.serviceendpoint <span class="m">00000000</span>-0000-0000-0000-000000000000/00000000-0000-0000-0000-000000000000
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>azurecr_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Azure container registry name.</p></li>
<li><p><strong>azurecr_spn_tenantid</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The tenant id of the service principal.</p></li>
<li><p><strong>azurecr_subscription_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The subscription id of the Azure targets.</p></li>
<li><p><strong>azurecr_subscription_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The subscription name of the Azure targets.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name you will use to refer to this service connection in task inputs.</p></li>
<li><p><strong>project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The project ID or project name.</p></li>
<li><p><strong>resource_group</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The resource group to which the container registry belongs.</p></li>
<li><p><strong>service_endpoint_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name you will use to refer to this service connection in task inputs.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_azuredevops.ServiceEndpointAzureEcr.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">authorization</span><span class="p">:</span> <span class="n">Union[Mapping[str, Union[str, Awaitable[str], Output[T]]], Awaitable[Mapping[str, Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">azurecr_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">azurecr_spn_tenantid</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">azurecr_subscription_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">azurecr_subscription_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_endpoint_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_azuredevops.service_endpoint_azure_ecr.ServiceEndpointAzureEcr<a class="headerlink" href="#pulumi_azuredevops.ServiceEndpointAzureEcr.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ServiceEndpointAzureEcr resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>azurecr_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Azure container registry name.</p></li>
<li><p><strong>azurecr_spn_tenantid</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The tenant id of the service principal.</p></li>
<li><p><strong>azurecr_subscription_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The subscription id of the Azure targets.</p></li>
<li><p><strong>azurecr_subscription_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The subscription name of the Azure targets.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name you will use to refer to this service connection in task inputs.</p></li>
<li><p><strong>project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The project ID or project name.</p></li>
<li><p><strong>resource_group</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The resource group to which the container registry belongs.</p></li>
<li><p><strong>service_endpoint_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name you will use to refer to this service connection in task inputs.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.ServiceEndpointAzureEcr.azurecr_name">
<em class="property">property </em><code class="sig-name descname">azurecr_name</code><a class="headerlink" href="#pulumi_azuredevops.ServiceEndpointAzureEcr.azurecr_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The Azure container registry name.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.ServiceEndpointAzureEcr.azurecr_spn_tenantid">
<em class="property">property </em><code class="sig-name descname">azurecr_spn_tenantid</code><a class="headerlink" href="#pulumi_azuredevops.ServiceEndpointAzureEcr.azurecr_spn_tenantid" title="Permalink to this definition">¶</a></dt>
<dd><p>The tenant id of the service principal.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.ServiceEndpointAzureEcr.azurecr_subscription_id">
<em class="property">property </em><code class="sig-name descname">azurecr_subscription_id</code><a class="headerlink" href="#pulumi_azuredevops.ServiceEndpointAzureEcr.azurecr_subscription_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The subscription id of the Azure targets.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.ServiceEndpointAzureEcr.azurecr_subscription_name">
<em class="property">property </em><code class="sig-name descname">azurecr_subscription_name</code><a class="headerlink" href="#pulumi_azuredevops.ServiceEndpointAzureEcr.azurecr_subscription_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The subscription name of the Azure targets.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.ServiceEndpointAzureEcr.description">
<em class="property">property </em><code class="sig-name descname">description</code><a class="headerlink" href="#pulumi_azuredevops.ServiceEndpointAzureEcr.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The name you will use to refer to this service connection in task inputs.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.ServiceEndpointAzureEcr.project_id">
<em class="property">property </em><code class="sig-name descname">project_id</code><a class="headerlink" href="#pulumi_azuredevops.ServiceEndpointAzureEcr.project_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The project ID or project name.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.ServiceEndpointAzureEcr.resource_group">
<em class="property">property </em><code class="sig-name descname">resource_group</code><a class="headerlink" href="#pulumi_azuredevops.ServiceEndpointAzureEcr.resource_group" title="Permalink to this definition">¶</a></dt>
<dd><p>The resource group to which the container registry belongs.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.ServiceEndpointAzureEcr.service_endpoint_name">
<em class="property">property </em><code class="sig-name descname">service_endpoint_name</code><a class="headerlink" href="#pulumi_azuredevops.ServiceEndpointAzureEcr.service_endpoint_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name you will use to refer to this service connection in task inputs.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.ServiceEndpointAzureEcr.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuredevops.ServiceEndpointAzureEcr.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azuredevops.ServiceEndpointAzureEcr.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuredevops.ServiceEndpointAzureEcr.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azuredevops.ServiceEndpointAzureRM">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azuredevops.</code><code class="sig-name descname">ServiceEndpointAzureRM</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">authorization</span><span class="p">:</span> <span class="n">Union[Mapping[str, Union[str, Awaitable[str], Output[T]]], Awaitable[Mapping[str, Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">azurerm_spn_tenantid</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">azurerm_subscription_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">azurerm_subscription_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">credentials</span><span class="p">:</span> <span class="n">Union[ServiceEndpointAzureRMCredentialsArgs, Mapping[str, Any], Awaitable[Union[ServiceEndpointAzureRMCredentialsArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_endpoint_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuredevops.ServiceEndpointAzureRM" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages Manual or Automatic AzureRM service endpoint within Azure DevOps.</p>
<p>Before to create a service end point in Azure DevOps, you need to create a Service Principal in your Azure subscription.</p>
<p>For detailed steps to create a service principal with Azure cli see the <a class="reference external" href="https://docs.microsoft.com/en-us/cli/azure/create-an-azure-service-principal-azure-cli?view=azure-cli-latest">documentation</a></p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_azuredevops</span> <span class="k">as</span> <span class="nn">azuredevops</span>

<span class="n">project</span> <span class="o">=</span> <span class="n">azuredevops</span><span class="o">.</span><span class="n">Project</span><span class="p">(</span><span class="s2">&quot;project&quot;</span><span class="p">,</span>
    <span class="n">visibility</span><span class="o">=</span><span class="s2">&quot;private&quot;</span><span class="p">,</span>
    <span class="n">version_control</span><span class="o">=</span><span class="s2">&quot;Git&quot;</span><span class="p">,</span>
    <span class="n">work_item_template</span><span class="o">=</span><span class="s2">&quot;Agile&quot;</span><span class="p">)</span>
<span class="n">endpointazure</span> <span class="o">=</span> <span class="n">azuredevops</span><span class="o">.</span><span class="n">ServiceEndpointAzureRM</span><span class="p">(</span><span class="s2">&quot;endpointazure&quot;</span><span class="p">,</span>
    <span class="n">project_id</span><span class="o">=</span><span class="n">project</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">service_endpoint_name</span><span class="o">=</span><span class="s2">&quot;Sample AzureRM&quot;</span><span class="p">,</span>
    <span class="n">description</span><span class="o">=</span><span class="s2">&quot;Managed by Terraform&quot;</span><span class="p">,</span>
    <span class="n">credentials</span><span class="o">=</span><span class="n">azuredevops</span><span class="o">.</span><span class="n">ServiceEndpointAzureRMCredentialsArgs</span><span class="p">(</span>
        <span class="n">serviceprincipalid</span><span class="o">=</span><span class="s2">&quot;00000000-0000-0000-0000-000000000000&quot;</span><span class="p">,</span>
        <span class="n">serviceprincipalkey</span><span class="o">=</span><span class="s2">&quot;xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx&quot;</span><span class="p">,</span>
    <span class="p">),</span>
    <span class="n">azurerm_spn_tenantid</span><span class="o">=</span><span class="s2">&quot;00000000-0000-0000-0000-000000000000&quot;</span><span class="p">,</span>
    <span class="n">azurerm_subscription_id</span><span class="o">=</span><span class="s2">&quot;00000000-0000-0000-0000-000000000000&quot;</span><span class="p">,</span>
    <span class="n">azurerm_subscription_name</span><span class="o">=</span><span class="s2">&quot;Sample Subscription&quot;</span><span class="p">)</span>
</pre></div>
</div>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_azuredevops</span> <span class="k">as</span> <span class="nn">azuredevops</span>

<span class="n">project</span> <span class="o">=</span> <span class="n">azuredevops</span><span class="o">.</span><span class="n">Project</span><span class="p">(</span><span class="s2">&quot;project&quot;</span><span class="p">,</span>
    <span class="n">visibility</span><span class="o">=</span><span class="s2">&quot;private&quot;</span><span class="p">,</span>
    <span class="n">version_control</span><span class="o">=</span><span class="s2">&quot;Git&quot;</span><span class="p">,</span>
    <span class="n">work_item_template</span><span class="o">=</span><span class="s2">&quot;Agile&quot;</span><span class="p">)</span>
<span class="n">endpointazure</span> <span class="o">=</span> <span class="n">azuredevops</span><span class="o">.</span><span class="n">ServiceEndpointAzureRM</span><span class="p">(</span><span class="s2">&quot;endpointazure&quot;</span><span class="p">,</span>
    <span class="n">project_id</span><span class="o">=</span><span class="n">project</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">service_endpoint_name</span><span class="o">=</span><span class="s2">&quot;Sample AzureRM&quot;</span><span class="p">,</span>
    <span class="n">description</span><span class="o">=</span><span class="s2">&quot;Managed by Terraform&quot;</span><span class="p">,</span>
    <span class="n">azurerm_spn_tenantid</span><span class="o">=</span><span class="s2">&quot;00000000-0000-0000-0000-000000000000&quot;</span><span class="p">,</span>
    <span class="n">azurerm_subscription_id</span><span class="o">=</span><span class="s2">&quot;00000000-0000-0000-0000-000000000000&quot;</span><span class="p">,</span>
    <span class="n">azurerm_subscription_name</span><span class="o">=</span><span class="s2">&quot;Microsoft Azure DEMO&quot;</span><span class="p">)</span>
</pre></div>
</div>
<ul class="simple">
<li><p><a class="reference external" href="https://docs.microsoft.com/en-us/rest/api/azure/devops/serviceendpoint/endpoints?view=azure-devops-rest-5.1">Azure DevOps Service REST API 5.1 - Service End points</a></p></li>
</ul>
<p>Azure DevOps Service Endpoint Azure Resource Manage can be imported using <strong>projectID/serviceEndpointID</strong> or <strong>projectName/serviceEndpointID</strong></p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>$ pulumi import azuredevops:index/serviceEndpointAzureRM:ServiceEndpointAzureRM azuredevops_serviceendpoint_azurerm.serviceendpoint <span class="m">00000000</span>-0000-0000-0000-000000000000/00000000-0000-0000-0000-000000000000
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>azurerm_spn_tenantid</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The tenant id if the service principal.</p></li>
<li><p><strong>azurerm_subscription_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The subscription Id of the Azure targets.</p></li>
<li><p><strong>azurerm_subscription_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The subscription Name of the targets.</p></li>
<li><p><strong>credentials</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'ServiceEndpointAzureRMCredentialsArgs'</em><em>]</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">credentials</span></code> block.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Service connection description.</p></li>
<li><p><strong>project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The project ID or project name.</p></li>
<li><p><strong>resource_group</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The resource group used for scope of automatic service endpoint.</p></li>
<li><p><strong>service_endpoint_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Service Endpoint name.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_azuredevops.ServiceEndpointAzureRM.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">authorization</span><span class="p">:</span> <span class="n">Union[Mapping[str, Union[str, Awaitable[str], Output[T]]], Awaitable[Mapping[str, Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">azurerm_spn_tenantid</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">azurerm_subscription_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">azurerm_subscription_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">credentials</span><span class="p">:</span> <span class="n">Union[ServiceEndpointAzureRMCredentialsArgs, Mapping[str, Any], Awaitable[Union[ServiceEndpointAzureRMCredentialsArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">resource_group</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_endpoint_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_azuredevops.service_endpoint_azure_rm.ServiceEndpointAzureRM<a class="headerlink" href="#pulumi_azuredevops.ServiceEndpointAzureRM.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ServiceEndpointAzureRM resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>azurerm_spn_tenantid</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The tenant id if the service principal.</p></li>
<li><p><strong>azurerm_subscription_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The subscription Id of the Azure targets.</p></li>
<li><p><strong>azurerm_subscription_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The subscription Name of the targets.</p></li>
<li><p><strong>credentials</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'ServiceEndpointAzureRMCredentialsArgs'</em><em>]</em><em>]</em>) – A <code class="docutils literal notranslate"><span class="pre">credentials</span></code> block.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Service connection description.</p></li>
<li><p><strong>project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The project ID or project name.</p></li>
<li><p><strong>resource_group</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The resource group used for scope of automatic service endpoint.</p></li>
<li><p><strong>service_endpoint_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Service Endpoint name.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.ServiceEndpointAzureRM.azurerm_spn_tenantid">
<em class="property">property </em><code class="sig-name descname">azurerm_spn_tenantid</code><a class="headerlink" href="#pulumi_azuredevops.ServiceEndpointAzureRM.azurerm_spn_tenantid" title="Permalink to this definition">¶</a></dt>
<dd><p>The tenant id if the service principal.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.ServiceEndpointAzureRM.azurerm_subscription_id">
<em class="property">property </em><code class="sig-name descname">azurerm_subscription_id</code><a class="headerlink" href="#pulumi_azuredevops.ServiceEndpointAzureRM.azurerm_subscription_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The subscription Id of the Azure targets.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.ServiceEndpointAzureRM.azurerm_subscription_name">
<em class="property">property </em><code class="sig-name descname">azurerm_subscription_name</code><a class="headerlink" href="#pulumi_azuredevops.ServiceEndpointAzureRM.azurerm_subscription_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The subscription Name of the targets.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.ServiceEndpointAzureRM.credentials">
<em class="property">property </em><code class="sig-name descname">credentials</code><a class="headerlink" href="#pulumi_azuredevops.ServiceEndpointAzureRM.credentials" title="Permalink to this definition">¶</a></dt>
<dd><p>A <code class="docutils literal notranslate"><span class="pre">credentials</span></code> block.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.ServiceEndpointAzureRM.description">
<em class="property">property </em><code class="sig-name descname">description</code><a class="headerlink" href="#pulumi_azuredevops.ServiceEndpointAzureRM.description" title="Permalink to this definition">¶</a></dt>
<dd><p>Service connection description.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.ServiceEndpointAzureRM.project_id">
<em class="property">property </em><code class="sig-name descname">project_id</code><a class="headerlink" href="#pulumi_azuredevops.ServiceEndpointAzureRM.project_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The project ID or project name.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.ServiceEndpointAzureRM.resource_group">
<em class="property">property </em><code class="sig-name descname">resource_group</code><a class="headerlink" href="#pulumi_azuredevops.ServiceEndpointAzureRM.resource_group" title="Permalink to this definition">¶</a></dt>
<dd><p>The resource group used for scope of automatic service endpoint.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.ServiceEndpointAzureRM.service_endpoint_name">
<em class="property">property </em><code class="sig-name descname">service_endpoint_name</code><a class="headerlink" href="#pulumi_azuredevops.ServiceEndpointAzureRM.service_endpoint_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The Service Endpoint name.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.ServiceEndpointAzureRM.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuredevops.ServiceEndpointAzureRM.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azuredevops.ServiceEndpointAzureRM.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuredevops.ServiceEndpointAzureRM.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azuredevops.ServiceEndpointBitBucket">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azuredevops.</code><code class="sig-name descname">ServiceEndpointBitBucket</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">authorization</span><span class="p">:</span> <span class="n">Union[Mapping[str, Union[str, Awaitable[str], Output[T]]], Awaitable[Mapping[str, Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">password</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_endpoint_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">username</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuredevops.ServiceEndpointBitBucket" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Bitbucket service endpoint within Azure DevOps.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_azuredevops</span> <span class="k">as</span> <span class="nn">azuredevops</span>

<span class="n">project</span> <span class="o">=</span> <span class="n">azuredevops</span><span class="o">.</span><span class="n">Project</span><span class="p">(</span><span class="s2">&quot;project&quot;</span><span class="p">,</span>
    <span class="n">visibility</span><span class="o">=</span><span class="s2">&quot;private&quot;</span><span class="p">,</span>
    <span class="n">version_control</span><span class="o">=</span><span class="s2">&quot;Git&quot;</span><span class="p">,</span>
    <span class="n">work_item_template</span><span class="o">=</span><span class="s2">&quot;Agile&quot;</span><span class="p">)</span>
<span class="n">serviceendpoint</span> <span class="o">=</span> <span class="n">azuredevops</span><span class="o">.</span><span class="n">ServiceEndpointBitBucket</span><span class="p">(</span><span class="s2">&quot;serviceendpoint&quot;</span><span class="p">,</span>
    <span class="n">project_id</span><span class="o">=</span><span class="n">project</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">username</span><span class="o">=</span><span class="s2">&quot;username&quot;</span><span class="p">,</span>
    <span class="n">password</span><span class="o">=</span><span class="s2">&quot;password&quot;</span><span class="p">,</span>
    <span class="n">service_endpoint_name</span><span class="o">=</span><span class="s2">&quot;Sample Bitbucket&quot;</span><span class="p">,</span>
    <span class="n">description</span><span class="o">=</span><span class="s2">&quot;Managed by Terraform&quot;</span><span class="p">)</span>
</pre></div>
</div>
<ul class="simple">
<li><p><a class="reference external" href="https://docs.microsoft.com/en-us/rest/api/azure/devops/serviceendpoint/endpoints?view=azure-devops-rest-5.1">Azure DevOps Service REST API 5.1 - Agent Pools</a></p></li>
</ul>
<p>Azure DevOps Service Endpoint Bitbucket can be imported using <strong>projectID/serviceEndpointID</strong> or <strong>projectName/serviceEndpointID</strong></p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>$ pulumi import azuredevops:index/serviceEndpointBitBucket:ServiceEndpointBitBucket azuredevops_serviceendpoint_bitbucket.serviceendpoint <span class="m">00000000</span>-0000-0000-0000-000000000000/00000000-0000-0000-0000-000000000000
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Bitbucket account password.</p></li>
<li><p><strong>project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The project ID or project name.</p></li>
<li><p><strong>service_endpoint_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Service Endpoint name.</p></li>
<li><p><strong>username</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Bitbucket account username.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_azuredevops.ServiceEndpointBitBucket.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">authorization</span><span class="p">:</span> <span class="n">Union[Mapping[str, Union[str, Awaitable[str], Output[T]]], Awaitable[Mapping[str, Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">password</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">password_hash</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_endpoint_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">username</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_azuredevops.service_endpoint_bit_bucket.ServiceEndpointBitBucket<a class="headerlink" href="#pulumi_azuredevops.ServiceEndpointBitBucket.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ServiceEndpointBitBucket resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Bitbucket account password.</p></li>
<li><p><strong>password_hash</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A bcrypted hash of the attribute ‘password’</p></li>
<li><p><strong>project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The project ID or project name.</p></li>
<li><p><strong>service_endpoint_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Service Endpoint name.</p></li>
<li><p><strong>username</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Bitbucket account username.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.ServiceEndpointBitBucket.password">
<em class="property">property </em><code class="sig-name descname">password</code><a class="headerlink" href="#pulumi_azuredevops.ServiceEndpointBitBucket.password" title="Permalink to this definition">¶</a></dt>
<dd><p>Bitbucket account password.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.ServiceEndpointBitBucket.password_hash">
<em class="property">property </em><code class="sig-name descname">password_hash</code><a class="headerlink" href="#pulumi_azuredevops.ServiceEndpointBitBucket.password_hash" title="Permalink to this definition">¶</a></dt>
<dd><p>A bcrypted hash of the attribute ‘password’</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.ServiceEndpointBitBucket.project_id">
<em class="property">property </em><code class="sig-name descname">project_id</code><a class="headerlink" href="#pulumi_azuredevops.ServiceEndpointBitBucket.project_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The project ID or project name.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.ServiceEndpointBitBucket.service_endpoint_name">
<em class="property">property </em><code class="sig-name descname">service_endpoint_name</code><a class="headerlink" href="#pulumi_azuredevops.ServiceEndpointBitBucket.service_endpoint_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The Service Endpoint name.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.ServiceEndpointBitBucket.username">
<em class="property">property </em><code class="sig-name descname">username</code><a class="headerlink" href="#pulumi_azuredevops.ServiceEndpointBitBucket.username" title="Permalink to this definition">¶</a></dt>
<dd><p>Bitbucket account username.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.ServiceEndpointBitBucket.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuredevops.ServiceEndpointBitBucket.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azuredevops.ServiceEndpointBitBucket.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuredevops.ServiceEndpointBitBucket.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azuredevops.ServiceEndpointDockerRegistry">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azuredevops.</code><code class="sig-name descname">ServiceEndpointDockerRegistry</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">authorization</span><span class="p">:</span> <span class="n">Union[Mapping[str, Union[str, Awaitable[str], Output[T]]], Awaitable[Mapping[str, Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">docker_email</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">docker_password</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">docker_registry</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">docker_username</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">registry_type</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_endpoint_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuredevops.ServiceEndpointDockerRegistry" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Docker Registry service endpoint within Azure DevOps.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_azuredevops</span> <span class="k">as</span> <span class="nn">azuredevops</span>

<span class="n">project</span> <span class="o">=</span> <span class="n">azuredevops</span><span class="o">.</span><span class="n">Project</span><span class="p">(</span><span class="s2">&quot;project&quot;</span><span class="p">,</span>
    <span class="n">visibility</span><span class="o">=</span><span class="s2">&quot;private&quot;</span><span class="p">,</span>
    <span class="n">version_control</span><span class="o">=</span><span class="s2">&quot;Git&quot;</span><span class="p">,</span>
    <span class="n">work_item_template</span><span class="o">=</span><span class="s2">&quot;Agile&quot;</span><span class="p">)</span>
<span class="c1"># dockerhub registry service connection</span>
<span class="n">dockerhubregistry</span> <span class="o">=</span> <span class="n">azuredevops</span><span class="o">.</span><span class="n">ServiceEndpointDockerRegistry</span><span class="p">(</span><span class="s2">&quot;dockerhubregistry&quot;</span><span class="p">,</span>
    <span class="n">project_id</span><span class="o">=</span><span class="n">project</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">service_endpoint_name</span><span class="o">=</span><span class="s2">&quot;Sample Docker Hub&quot;</span><span class="p">,</span>
    <span class="n">docker_username</span><span class="o">=</span><span class="s2">&quot;sample&quot;</span><span class="p">,</span>
    <span class="n">docker_email</span><span class="o">=</span><span class="s2">&quot;email@example.com&quot;</span><span class="p">,</span>
    <span class="n">docker_password</span><span class="o">=</span><span class="s2">&quot;12345&quot;</span><span class="p">,</span>
    <span class="n">registry_type</span><span class="o">=</span><span class="s2">&quot;DockerHub&quot;</span><span class="p">)</span>
<span class="c1"># other docker registry service connection</span>
<span class="n">otherregistry</span> <span class="o">=</span> <span class="n">azuredevops</span><span class="o">.</span><span class="n">ServiceEndpointDockerRegistry</span><span class="p">(</span><span class="s2">&quot;otherregistry&quot;</span><span class="p">,</span>
    <span class="n">project_id</span><span class="o">=</span><span class="n">project</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">service_endpoint_name</span><span class="o">=</span><span class="s2">&quot;Sample Docker Registry&quot;</span><span class="p">,</span>
    <span class="n">docker_registry</span><span class="o">=</span><span class="s2">&quot;https://sample.azurecr.io/v1&quot;</span><span class="p">,</span>
    <span class="n">docker_username</span><span class="o">=</span><span class="s2">&quot;sample&quot;</span><span class="p">,</span>
    <span class="n">docker_password</span><span class="o">=</span><span class="s2">&quot;12345&quot;</span><span class="p">,</span>
    <span class="n">registry_type</span><span class="o">=</span><span class="s2">&quot;Others&quot;</span><span class="p">)</span>
</pre></div>
</div>
<ul class="simple">
<li><p><a class="reference external" href="https://docs.microsoft.com/en-us/rest/api/azure/devops/serviceendpoint/endpoints?view=azure-devops-rest-5.1">Azure DevOps Service REST API 5.1 - Service Endpoints</a></p></li>
<li><p><a class="reference external" href="https://docs.microsoft.com/en-us/azure/devops/pipelines/library/service-endpoints?view=azure-devops&amp;tabs=yaml#sep-docreg">Docker Registry Service Connection</a></p></li>
</ul>
<p>Azure DevOps Service Endpoint Docker Registry can be imported using <strong>projectID/serviceEndpointID</strong> or <strong>projectName/serviceEndpointID</strong></p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>$ pulumi import azuredevops:index/serviceEndpointDockerRegistry:ServiceEndpointDockerRegistry azuredevops_serviceendpoint_dockerregistry.serviceendpoint <span class="m">00000000</span>-0000-0000-0000-000000000000/00000000-0000-0000-0000-000000000000
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name you will use to refer to this service connection in task inputs.</p></li>
<li><p><strong>docker_email</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The email for Docker account user.</p></li>
<li><p><strong>docker_password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The password for the account user identified above.</p></li>
<li><p><strong>docker_registry</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The URL of the Docker registry. (Default: “<a class="reference external" href="https://index.docker.io/v1/">https://index.docker.io/v1/</a>”)</p></li>
<li><p><strong>docker_username</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The identifier of the Docker account user.</p></li>
<li><p><strong>project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The project ID or project name.</p></li>
<li><p><strong>registry_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Can be “DockerHub” or “Others” (Default “DockerHub”)</p></li>
<li><p><strong>service_endpoint_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name you will use to refer to this service connection in task inputs.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_azuredevops.ServiceEndpointDockerRegistry.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">authorization</span><span class="p">:</span> <span class="n">Union[Mapping[str, Union[str, Awaitable[str], Output[T]]], Awaitable[Mapping[str, Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">docker_email</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">docker_password</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">docker_password_hash</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">docker_registry</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">docker_username</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">registry_type</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_endpoint_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_azuredevops.service_endpoint_docker_registry.ServiceEndpointDockerRegistry<a class="headerlink" href="#pulumi_azuredevops.ServiceEndpointDockerRegistry.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ServiceEndpointDockerRegistry resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name you will use to refer to this service connection in task inputs.</p></li>
<li><p><strong>docker_email</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The email for Docker account user.</p></li>
<li><p><strong>docker_password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The password for the account user identified above.</p></li>
<li><p><strong>docker_password_hash</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A bcrypted hash of the attribute ‘docker_password’</p></li>
<li><p><strong>docker_registry</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The URL of the Docker registry. (Default: “<a class="reference external" href="https://index.docker.io/v1/">https://index.docker.io/v1/</a>”)</p></li>
<li><p><strong>docker_username</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The identifier of the Docker account user.</p></li>
<li><p><strong>project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The project ID or project name.</p></li>
<li><p><strong>registry_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Can be “DockerHub” or “Others” (Default “DockerHub”)</p></li>
<li><p><strong>service_endpoint_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name you will use to refer to this service connection in task inputs.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.ServiceEndpointDockerRegistry.description">
<em class="property">property </em><code class="sig-name descname">description</code><a class="headerlink" href="#pulumi_azuredevops.ServiceEndpointDockerRegistry.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The name you will use to refer to this service connection in task inputs.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.ServiceEndpointDockerRegistry.docker_email">
<em class="property">property </em><code class="sig-name descname">docker_email</code><a class="headerlink" href="#pulumi_azuredevops.ServiceEndpointDockerRegistry.docker_email" title="Permalink to this definition">¶</a></dt>
<dd><p>The email for Docker account user.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.ServiceEndpointDockerRegistry.docker_password">
<em class="property">property </em><code class="sig-name descname">docker_password</code><a class="headerlink" href="#pulumi_azuredevops.ServiceEndpointDockerRegistry.docker_password" title="Permalink to this definition">¶</a></dt>
<dd><p>The password for the account user identified above.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.ServiceEndpointDockerRegistry.docker_password_hash">
<em class="property">property </em><code class="sig-name descname">docker_password_hash</code><a class="headerlink" href="#pulumi_azuredevops.ServiceEndpointDockerRegistry.docker_password_hash" title="Permalink to this definition">¶</a></dt>
<dd><p>A bcrypted hash of the attribute ‘docker_password’</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.ServiceEndpointDockerRegistry.docker_registry">
<em class="property">property </em><code class="sig-name descname">docker_registry</code><a class="headerlink" href="#pulumi_azuredevops.ServiceEndpointDockerRegistry.docker_registry" title="Permalink to this definition">¶</a></dt>
<dd><p>The URL of the Docker registry. (Default: “<a class="reference external" href="https://index.docker.io/v1/">https://index.docker.io/v1/</a>”)</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.ServiceEndpointDockerRegistry.docker_username">
<em class="property">property </em><code class="sig-name descname">docker_username</code><a class="headerlink" href="#pulumi_azuredevops.ServiceEndpointDockerRegistry.docker_username" title="Permalink to this definition">¶</a></dt>
<dd><p>The identifier of the Docker account user.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.ServiceEndpointDockerRegistry.project_id">
<em class="property">property </em><code class="sig-name descname">project_id</code><a class="headerlink" href="#pulumi_azuredevops.ServiceEndpointDockerRegistry.project_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The project ID or project name.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.ServiceEndpointDockerRegistry.registry_type">
<em class="property">property </em><code class="sig-name descname">registry_type</code><a class="headerlink" href="#pulumi_azuredevops.ServiceEndpointDockerRegistry.registry_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Can be “DockerHub” or “Others” (Default “DockerHub”)</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.ServiceEndpointDockerRegistry.service_endpoint_name">
<em class="property">property </em><code class="sig-name descname">service_endpoint_name</code><a class="headerlink" href="#pulumi_azuredevops.ServiceEndpointDockerRegistry.service_endpoint_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name you will use to refer to this service connection in task inputs.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.ServiceEndpointDockerRegistry.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuredevops.ServiceEndpointDockerRegistry.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azuredevops.ServiceEndpointDockerRegistry.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuredevops.ServiceEndpointDockerRegistry.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azuredevops.ServiceEndpointGitHub">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azuredevops.</code><code class="sig-name descname">ServiceEndpointGitHub</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auth_oauth</span><span class="p">:</span> <span class="n">Union[ServiceEndpointGitHubAuthOauthArgs, Mapping[str, Any], Awaitable[Union[ServiceEndpointGitHubAuthOauthArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auth_personal</span><span class="p">:</span> <span class="n">Union[ServiceEndpointGitHubAuthPersonalArgs, Mapping[str, Any], Awaitable[Union[ServiceEndpointGitHubAuthPersonalArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">authorization</span><span class="p">:</span> <span class="n">Union[Mapping[str, Union[str, Awaitable[str], Output[T]]], Awaitable[Mapping[str, Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_endpoint_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuredevops.ServiceEndpointGitHub" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a GitHub service endpoint within Azure DevOps.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_azuredevops</span> <span class="k">as</span> <span class="nn">azuredevops</span>

<span class="n">project</span> <span class="o">=</span> <span class="n">azuredevops</span><span class="o">.</span><span class="n">Project</span><span class="p">(</span><span class="s2">&quot;project&quot;</span><span class="p">,</span>
    <span class="n">visibility</span><span class="o">=</span><span class="s2">&quot;private&quot;</span><span class="p">,</span>
    <span class="n">version_control</span><span class="o">=</span><span class="s2">&quot;Git&quot;</span><span class="p">,</span>
    <span class="n">work_item_template</span><span class="o">=</span><span class="s2">&quot;Agile&quot;</span><span class="p">)</span>
<span class="n">serviceendpoint_gh1</span> <span class="o">=</span> <span class="n">azuredevops</span><span class="o">.</span><span class="n">ServiceEndpointGitHub</span><span class="p">(</span><span class="s2">&quot;serviceendpointGh1&quot;</span><span class="p">,</span>
    <span class="n">project_id</span><span class="o">=</span><span class="n">project</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">service_endpoint_name</span><span class="o">=</span><span class="s2">&quot;Sample GithHub Personal Access Token&quot;</span><span class="p">,</span>
    <span class="n">auth_personal</span><span class="o">=</span><span class="n">azuredevops</span><span class="o">.</span><span class="n">ServiceEndpointGitHubAuthPersonalArgs</span><span class="p">(</span>
        <span class="n">personal_access_token</span><span class="o">=</span><span class="s2">&quot;xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx&quot;</span><span class="p">,</span>
    <span class="p">))</span>
</pre></div>
</div>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_azuredevops</span> <span class="k">as</span> <span class="nn">azuredevops</span>

<span class="n">serviceendpoint_gh2</span> <span class="o">=</span> <span class="n">azuredevops</span><span class="o">.</span><span class="n">ServiceEndpointGitHub</span><span class="p">(</span><span class="s2">&quot;serviceendpointGh2&quot;</span><span class="p">,</span>
    <span class="n">project_id</span><span class="o">=</span><span class="n">azuredevops_project</span><span class="p">[</span><span class="s2">&quot;project&quot;</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">],</span>
    <span class="n">service_endpoint_name</span><span class="o">=</span><span class="s2">&quot;Sample GithHub Grant&quot;</span><span class="p">,</span>
    <span class="n">auth_oauth</span><span class="o">=</span><span class="n">azuredevops</span><span class="o">.</span><span class="n">ServiceEndpointGitHubAuthOauthArgs</span><span class="p">(</span>
        <span class="n">oauth_configuration_id</span><span class="o">=</span><span class="s2">&quot;00000000-0000-0000-0000-000000000000&quot;</span><span class="p">,</span>
    <span class="p">))</span>
</pre></div>
</div>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_azuredevops</span> <span class="k">as</span> <span class="nn">azuredevops</span>

<span class="n">serviceendpoint_gh3</span> <span class="o">=</span> <span class="n">azuredevops</span><span class="o">.</span><span class="n">ServiceEndpointGitHub</span><span class="p">(</span><span class="s2">&quot;serviceendpointGh3&quot;</span><span class="p">,</span>
    <span class="n">project_id</span><span class="o">=</span><span class="n">azuredevops_project</span><span class="p">[</span><span class="s2">&quot;project&quot;</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">],</span>
    <span class="n">service_endpoint_name</span><span class="o">=</span><span class="s2">&quot;Sample GithHub Apps: Azure Pipelines&quot;</span><span class="p">,</span>
    <span class="n">description</span><span class="o">=</span><span class="s2">&quot;&quot;</span><span class="p">)</span>
</pre></div>
</div>
<ul class="simple">
<li><p><a class="reference external" href="https://docs.microsoft.com/en-us/rest/api/azure/devops/serviceendpoint/endpoints?view=azure-devops-rest-5.1">Azure DevOps Service REST API 5.1 - Service Endpoints</a></p></li>
</ul>
<p>Azure DevOps Service Endpoint GitHub can be imported using <strong>projectID/serviceEndpointID</strong> or <strong>projectName/serviceEndpointID</strong></p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>$ pulumi import azuredevops:index/serviceEndpointGitHub:ServiceEndpointGitHub azuredevops_serviceendpoint_github.serviceendpoint <span class="m">00000000</span>-0000-0000-0000-000000000000/00000000-0000-0000-0000-000000000000
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>auth_oauth</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'ServiceEndpointGitHubAuthOauthArgs'</em><em>]</em><em>]</em>) – An <code class="docutils literal notranslate"><span class="pre">auth_oauth</span></code> block as documented below. Allows connecting using an Oauth token.</p></li>
<li><p><strong>auth_personal</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'ServiceEndpointGitHubAuthPersonalArgs'</em><em>]</em><em>]</em>) – An <code class="docutils literal notranslate"><span class="pre">auth_personal</span></code> block as documented below. Allows connecting using a personal access token.</p></li>
<li><p><strong>project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The project ID or project name.</p></li>
<li><p><strong>service_endpoint_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Service Endpoint name.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_azuredevops.ServiceEndpointGitHub.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auth_oauth</span><span class="p">:</span> <span class="n">Union[ServiceEndpointGitHubAuthOauthArgs, Mapping[str, Any], Awaitable[Union[ServiceEndpointGitHubAuthOauthArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auth_personal</span><span class="p">:</span> <span class="n">Union[ServiceEndpointGitHubAuthPersonalArgs, Mapping[str, Any], Awaitable[Union[ServiceEndpointGitHubAuthPersonalArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">authorization</span><span class="p">:</span> <span class="n">Union[Mapping[str, Union[str, Awaitable[str], Output[T]]], Awaitable[Mapping[str, Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_endpoint_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_azuredevops.service_endpoint_git_hub.ServiceEndpointGitHub<a class="headerlink" href="#pulumi_azuredevops.ServiceEndpointGitHub.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ServiceEndpointGitHub resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>auth_oauth</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'ServiceEndpointGitHubAuthOauthArgs'</em><em>]</em><em>]</em>) – An <code class="docutils literal notranslate"><span class="pre">auth_oauth</span></code> block as documented below. Allows connecting using an Oauth token.</p></li>
<li><p><strong>auth_personal</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'ServiceEndpointGitHubAuthPersonalArgs'</em><em>]</em><em>]</em>) – An <code class="docutils literal notranslate"><span class="pre">auth_personal</span></code> block as documented below. Allows connecting using a personal access token.</p></li>
<li><p><strong>project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The project ID or project name.</p></li>
<li><p><strong>service_endpoint_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Service Endpoint name.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.ServiceEndpointGitHub.auth_oauth">
<em class="property">property </em><code class="sig-name descname">auth_oauth</code><a class="headerlink" href="#pulumi_azuredevops.ServiceEndpointGitHub.auth_oauth" title="Permalink to this definition">¶</a></dt>
<dd><p>An <code class="docutils literal notranslate"><span class="pre">auth_oauth</span></code> block as documented below. Allows connecting using an Oauth token.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.ServiceEndpointGitHub.auth_personal">
<em class="property">property </em><code class="sig-name descname">auth_personal</code><a class="headerlink" href="#pulumi_azuredevops.ServiceEndpointGitHub.auth_personal" title="Permalink to this definition">¶</a></dt>
<dd><p>An <code class="docutils literal notranslate"><span class="pre">auth_personal</span></code> block as documented below. Allows connecting using a personal access token.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.ServiceEndpointGitHub.project_id">
<em class="property">property </em><code class="sig-name descname">project_id</code><a class="headerlink" href="#pulumi_azuredevops.ServiceEndpointGitHub.project_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The project ID or project name.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.ServiceEndpointGitHub.service_endpoint_name">
<em class="property">property </em><code class="sig-name descname">service_endpoint_name</code><a class="headerlink" href="#pulumi_azuredevops.ServiceEndpointGitHub.service_endpoint_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The Service Endpoint name.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.ServiceEndpointGitHub.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuredevops.ServiceEndpointGitHub.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azuredevops.ServiceEndpointGitHub.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuredevops.ServiceEndpointGitHub.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azuredevops.ServiceEndpointKubernetes">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azuredevops.</code><code class="sig-name descname">ServiceEndpointKubernetes</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">apiserver_url</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">authorization</span><span class="p">:</span> <span class="n">Union[Mapping[str, Union[str, Awaitable[str], Output[T]]], Awaitable[Mapping[str, Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">authorization_type</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">azure_subscriptions</span><span class="p">:</span> <span class="n">Union[Sequence[Union[ServiceEndpointKubernetesAzureSubscriptionArgs, Mapping[str, Any], Awaitable[Union[ServiceEndpointKubernetesAzureSubscriptionArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[ServiceEndpointKubernetesAzureSubscriptionArgs, Mapping[str, Any], Awaitable[Union[ServiceEndpointKubernetesAzureSubscriptionArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kubeconfigs</span><span class="p">:</span> <span class="n">Union[Sequence[Union[ServiceEndpointKubernetesKubeconfigArgs, Mapping[str, Any], Awaitable[Union[ServiceEndpointKubernetesKubeconfigArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[ServiceEndpointKubernetesKubeconfigArgs, Mapping[str, Any], Awaitable[Union[ServiceEndpointKubernetesKubeconfigArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_accounts</span><span class="p">:</span> <span class="n">Union[Sequence[Union[ServiceEndpointKubernetesServiceAccountArgs, Mapping[str, Any], Awaitable[Union[ServiceEndpointKubernetesServiceAccountArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[ServiceEndpointKubernetesServiceAccountArgs, Mapping[str, Any], Awaitable[Union[ServiceEndpointKubernetesServiceAccountArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_endpoint_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuredevops.ServiceEndpointKubernetes" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a Kubernetes service endpoint within Azure DevOps.</p>
<ul class="simple">
<li><p><a class="reference external" href="https://docs.microsoft.com/en-us/rest/api/azure/devops/serviceendpoint/endpoints?view=azure-devops-rest-5.1">Azure DevOps Service REST API 5.1 - Endpoints</a></p></li>
</ul>
<p>Azure DevOps Service Endpoint Kubernetes can be imported using <strong>projectID/serviceEndpointID</strong> or <strong>projectName/serviceEndpointID</strong></p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>$ pulumi import azuredevops:index/serviceEndpointKubernetes:ServiceEndpointKubernetes azuredevops_serviceendpoint_kubernetes.serviceendpoint <span class="m">00000000</span>-0000-0000-0000-000000000000/00000000-0000-0000-0000-000000000000
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>apiserver_url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Service Endpoint description.</p></li>
<li><p><strong>authorization_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The authentication method used to authenticate on the Kubernetes cluster. The value should be one of AzureSubscription, Kubeconfig, ServiceAccount.</p></li>
<li><p><strong>azure_subscriptions</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'ServiceEndpointKubernetesAzureSubscriptionArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – The configuration for authorization_type=”AzureSubscription”.</p></li>
<li><p><strong>kubeconfigs</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'ServiceEndpointKubernetesKubeconfigArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – The configuration for authorization_type=”Kubeconfig”.</p></li>
<li><p><strong>project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The project ID or project name.</p></li>
<li><p><strong>service_accounts</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'ServiceEndpointKubernetesServiceAccountArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – The configuration for authorization_type=”ServiceAccount”. This type uses the credentials of a service account currently deployed to the cluster.</p></li>
<li><p><strong>service_endpoint_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Service Endpoint name.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_azuredevops.ServiceEndpointKubernetes.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">apiserver_url</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">authorization</span><span class="p">:</span> <span class="n">Union[Mapping[str, Union[str, Awaitable[str], Output[T]]], Awaitable[Mapping[str, Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">authorization_type</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">azure_subscriptions</span><span class="p">:</span> <span class="n">Union[Sequence[Union[ServiceEndpointKubernetesAzureSubscriptionArgs, Mapping[str, Any], Awaitable[Union[ServiceEndpointKubernetesAzureSubscriptionArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[ServiceEndpointKubernetesAzureSubscriptionArgs, Mapping[str, Any], Awaitable[Union[ServiceEndpointKubernetesAzureSubscriptionArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kubeconfigs</span><span class="p">:</span> <span class="n">Union[Sequence[Union[ServiceEndpointKubernetesKubeconfigArgs, Mapping[str, Any], Awaitable[Union[ServiceEndpointKubernetesKubeconfigArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[ServiceEndpointKubernetesKubeconfigArgs, Mapping[str, Any], Awaitable[Union[ServiceEndpointKubernetesKubeconfigArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_accounts</span><span class="p">:</span> <span class="n">Union[Sequence[Union[ServiceEndpointKubernetesServiceAccountArgs, Mapping[str, Any], Awaitable[Union[ServiceEndpointKubernetesServiceAccountArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[ServiceEndpointKubernetesServiceAccountArgs, Mapping[str, Any], Awaitable[Union[ServiceEndpointKubernetesServiceAccountArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">service_endpoint_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_azuredevops.service_endpoint_kubernetes.ServiceEndpointKubernetes<a class="headerlink" href="#pulumi_azuredevops.ServiceEndpointKubernetes.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ServiceEndpointKubernetes resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>apiserver_url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Service Endpoint description.</p></li>
<li><p><strong>authorization_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The authentication method used to authenticate on the Kubernetes cluster. The value should be one of AzureSubscription, Kubeconfig, ServiceAccount.</p></li>
<li><p><strong>azure_subscriptions</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'ServiceEndpointKubernetesAzureSubscriptionArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – The configuration for authorization_type=”AzureSubscription”.</p></li>
<li><p><strong>kubeconfigs</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'ServiceEndpointKubernetesKubeconfigArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – The configuration for authorization_type=”Kubeconfig”.</p></li>
<li><p><strong>project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The project ID or project name.</p></li>
<li><p><strong>service_accounts</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'ServiceEndpointKubernetesServiceAccountArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – The configuration for authorization_type=”ServiceAccount”. This type uses the credentials of a service account currently deployed to the cluster.</p></li>
<li><p><strong>service_endpoint_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Service Endpoint name.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.ServiceEndpointKubernetes.apiserver_url">
<em class="property">property </em><code class="sig-name descname">apiserver_url</code><a class="headerlink" href="#pulumi_azuredevops.ServiceEndpointKubernetes.apiserver_url" title="Permalink to this definition">¶</a></dt>
<dd><p>The Service Endpoint description.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.ServiceEndpointKubernetes.authorization_type">
<em class="property">property </em><code class="sig-name descname">authorization_type</code><a class="headerlink" href="#pulumi_azuredevops.ServiceEndpointKubernetes.authorization_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The authentication method used to authenticate on the Kubernetes cluster. The value should be one of AzureSubscription, Kubeconfig, ServiceAccount.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.ServiceEndpointKubernetes.azure_subscriptions">
<em class="property">property </em><code class="sig-name descname">azure_subscriptions</code><a class="headerlink" href="#pulumi_azuredevops.ServiceEndpointKubernetes.azure_subscriptions" title="Permalink to this definition">¶</a></dt>
<dd><p>The configuration for authorization_type=”AzureSubscription”.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.ServiceEndpointKubernetes.kubeconfigs">
<em class="property">property </em><code class="sig-name descname">kubeconfigs</code><a class="headerlink" href="#pulumi_azuredevops.ServiceEndpointKubernetes.kubeconfigs" title="Permalink to this definition">¶</a></dt>
<dd><p>The configuration for authorization_type=”Kubeconfig”.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.ServiceEndpointKubernetes.project_id">
<em class="property">property </em><code class="sig-name descname">project_id</code><a class="headerlink" href="#pulumi_azuredevops.ServiceEndpointKubernetes.project_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The project ID or project name.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.ServiceEndpointKubernetes.service_accounts">
<em class="property">property </em><code class="sig-name descname">service_accounts</code><a class="headerlink" href="#pulumi_azuredevops.ServiceEndpointKubernetes.service_accounts" title="Permalink to this definition">¶</a></dt>
<dd><p>The configuration for authorization_type=”ServiceAccount”. This type uses the credentials of a service account currently deployed to the cluster.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.ServiceEndpointKubernetes.service_endpoint_name">
<em class="property">property </em><code class="sig-name descname">service_endpoint_name</code><a class="headerlink" href="#pulumi_azuredevops.ServiceEndpointKubernetes.service_endpoint_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The Service Endpoint name.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.ServiceEndpointKubernetes.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuredevops.ServiceEndpointKubernetes.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azuredevops.ServiceEndpointKubernetes.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuredevops.ServiceEndpointKubernetes.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azuredevops.User">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azuredevops.</code><code class="sig-name descname">User</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_license_type</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">licensing_source</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">origin</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">origin_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">principal_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuredevops.User" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a user entitlement within Azure DevOps.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_azuredevops</span> <span class="k">as</span> <span class="nn">azuredevops</span>

<span class="n">user</span> <span class="o">=</span> <span class="n">azuredevops</span><span class="o">.</span><span class="n">User</span><span class="p">(</span><span class="s2">&quot;user&quot;</span><span class="p">,</span> <span class="n">principal_name</span><span class="o">=</span><span class="s2">&quot;foo@contoso.com&quot;</span><span class="p">)</span>
</pre></div>
</div>
<ul class="simple">
<li><p><a class="reference external" href="https://docs.microsoft.com/en-us/rest/api/azure/devops/memberentitlementmanagement/user%20entitlements/add?view=azure-devops-rest-5.1">Azure DevOps Service REST API 5.1 - User Entitlements - Add</a></p></li>
</ul>
<ul class="simple">
<li><p><strong>Member Entitlement Management</strong>: Read &amp; Write</p></li>
</ul>
<p>The resources allows the import via the UUID of a user entitlement or by using the principal name of a user owning an entitlement.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>account_license_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Type of Account License. Valid values: <code class="docutils literal notranslate"><span class="pre">advanced</span></code>, <code class="docutils literal notranslate"><span class="pre">earlyAdopter</span></code>, <code class="docutils literal notranslate"><span class="pre">express</span></code>, <code class="docutils literal notranslate"><span class="pre">none</span></code>, <code class="docutils literal notranslate"><span class="pre">professional</span></code>, or <code class="docutils literal notranslate"><span class="pre">stakeholder</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">express</span></code>. In addition the value <code class="docutils literal notranslate"><span class="pre">basic</span></code> is allowed which is an alias for <code class="docutils literal notranslate"><span class="pre">express</span></code> and reflects the name of the <code class="docutils literal notranslate"><span class="pre">express</span></code> license used in the Azure DevOps web interface.</p></li>
<li><p><strong>licensing_source</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The source of the licensing (e.g. Account. MSDN etc.) Valid values: <code class="docutils literal notranslate"><span class="pre">account</span></code> (Default), <code class="docutils literal notranslate"><span class="pre">auto</span></code>, <code class="docutils literal notranslate"><span class="pre">msdn</span></code>, <code class="docutils literal notranslate"><span class="pre">none</span></code>, <code class="docutils literal notranslate"><span class="pre">profile</span></code>, <code class="docutils literal notranslate"><span class="pre">trail</span></code></p></li>
<li><p><strong>origin</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of source provider for the origin identifier.</p></li>
<li><p><strong>origin_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique identifier from the system of origin. Typically a sid, object id or Guid. e.g. Used for member of other tenant on Azure Active Directory.</p></li>
<li><p><strong>principal_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The principal name is the PrincipalName of a graph member from the source provider. Usually, e-mail address.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_azuredevops.User.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">account_license_type</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">descriptor</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">licensing_source</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">origin</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">origin_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">principal_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_azuredevops.user.User<a class="headerlink" href="#pulumi_azuredevops.User.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing User resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>account_license_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Type of Account License. Valid values: <code class="docutils literal notranslate"><span class="pre">advanced</span></code>, <code class="docutils literal notranslate"><span class="pre">earlyAdopter</span></code>, <code class="docutils literal notranslate"><span class="pre">express</span></code>, <code class="docutils literal notranslate"><span class="pre">none</span></code>, <code class="docutils literal notranslate"><span class="pre">professional</span></code>, or <code class="docutils literal notranslate"><span class="pre">stakeholder</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">express</span></code>. In addition the value <code class="docutils literal notranslate"><span class="pre">basic</span></code> is allowed which is an alias for <code class="docutils literal notranslate"><span class="pre">express</span></code> and reflects the name of the <code class="docutils literal notranslate"><span class="pre">express</span></code> license used in the Azure DevOps web interface.</p></li>
<li><p><strong>descriptor</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The descriptor is the primary way to reference the graph subject while the system is running. This field will uniquely identify the user graph subject.</p></li>
<li><p><strong>licensing_source</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The source of the licensing (e.g. Account. MSDN etc.) Valid values: <code class="docutils literal notranslate"><span class="pre">account</span></code> (Default), <code class="docutils literal notranslate"><span class="pre">auto</span></code>, <code class="docutils literal notranslate"><span class="pre">msdn</span></code>, <code class="docutils literal notranslate"><span class="pre">none</span></code>, <code class="docutils literal notranslate"><span class="pre">profile</span></code>, <code class="docutils literal notranslate"><span class="pre">trail</span></code></p></li>
<li><p><strong>origin</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of source provider for the origin identifier.</p></li>
<li><p><strong>origin_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique identifier from the system of origin. Typically a sid, object id or Guid. e.g. Used for member of other tenant on Azure Active Directory.</p></li>
<li><p><strong>principal_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The principal name is the PrincipalName of a graph member from the source provider. Usually, e-mail address.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.User.account_license_type">
<em class="property">property </em><code class="sig-name descname">account_license_type</code><a class="headerlink" href="#pulumi_azuredevops.User.account_license_type" title="Permalink to this definition">¶</a></dt>
<dd><p>Type of Account License. Valid values: <code class="docutils literal notranslate"><span class="pre">advanced</span></code>, <code class="docutils literal notranslate"><span class="pre">earlyAdopter</span></code>, <code class="docutils literal notranslate"><span class="pre">express</span></code>, <code class="docutils literal notranslate"><span class="pre">none</span></code>, <code class="docutils literal notranslate"><span class="pre">professional</span></code>, or <code class="docutils literal notranslate"><span class="pre">stakeholder</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">express</span></code>. In addition the value <code class="docutils literal notranslate"><span class="pre">basic</span></code> is allowed which is an alias for <code class="docutils literal notranslate"><span class="pre">express</span></code> and reflects the name of the <code class="docutils literal notranslate"><span class="pre">express</span></code> license used in the Azure DevOps web interface.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.User.descriptor">
<em class="property">property </em><code class="sig-name descname">descriptor</code><a class="headerlink" href="#pulumi_azuredevops.User.descriptor" title="Permalink to this definition">¶</a></dt>
<dd><p>The descriptor is the primary way to reference the graph subject while the system is running. This field will uniquely identify the user graph subject.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.User.licensing_source">
<em class="property">property </em><code class="sig-name descname">licensing_source</code><a class="headerlink" href="#pulumi_azuredevops.User.licensing_source" title="Permalink to this definition">¶</a></dt>
<dd><p>The source of the licensing (e.g. Account. MSDN etc.) Valid values: <code class="docutils literal notranslate"><span class="pre">account</span></code> (Default), <code class="docutils literal notranslate"><span class="pre">auto</span></code>, <code class="docutils literal notranslate"><span class="pre">msdn</span></code>, <code class="docutils literal notranslate"><span class="pre">none</span></code>, <code class="docutils literal notranslate"><span class="pre">profile</span></code>, <code class="docutils literal notranslate"><span class="pre">trail</span></code></p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.User.origin">
<em class="property">property </em><code class="sig-name descname">origin</code><a class="headerlink" href="#pulumi_azuredevops.User.origin" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of source provider for the origin identifier.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.User.origin_id">
<em class="property">property </em><code class="sig-name descname">origin_id</code><a class="headerlink" href="#pulumi_azuredevops.User.origin_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The unique identifier from the system of origin. Typically a sid, object id or Guid. e.g. Used for member of other tenant on Azure Active Directory.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.User.principal_name">
<em class="property">property </em><code class="sig-name descname">principal_name</code><a class="headerlink" href="#pulumi_azuredevops.User.principal_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The principal name is the PrincipalName of a graph member from the source provider. Usually, e-mail address.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.User.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuredevops.User.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azuredevops.User.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuredevops.User.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azuredevops.VariableGroup">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azuredevops.</code><code class="sig-name descname">VariableGroup</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">allow_access</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">key_vault</span><span class="p">:</span> <span class="n">Union[VariableGroupKeyVaultArgs, Mapping[str, Any], Awaitable[Union[VariableGroupKeyVaultArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">variables</span><span class="p">:</span> <span class="n">Union[Sequence[Union[VariableGroupVariableArgs, Mapping[str, Any], Awaitable[Union[VariableGroupVariableArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[VariableGroupVariableArgs, Mapping[str, Any], Awaitable[Union[VariableGroupVariableArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuredevops.VariableGroup" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages variable groups within Azure DevOps.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_azuredevops</span> <span class="k">as</span> <span class="nn">azuredevops</span>

<span class="n">project</span> <span class="o">=</span> <span class="n">azuredevops</span><span class="o">.</span><span class="n">Project</span><span class="p">(</span><span class="s2">&quot;project&quot;</span><span class="p">)</span>
<span class="n">variablegroup</span> <span class="o">=</span> <span class="n">azuredevops</span><span class="o">.</span><span class="n">VariableGroup</span><span class="p">(</span><span class="s2">&quot;variablegroup&quot;</span><span class="p">,</span>
    <span class="n">project_id</span><span class="o">=</span><span class="n">project</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">description</span><span class="o">=</span><span class="s2">&quot;Test Variable Group Description&quot;</span><span class="p">,</span>
    <span class="n">allow_access</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="n">variables</span><span class="o">=</span><span class="p">[</span>
        <span class="n">azuredevops</span><span class="o">.</span><span class="n">VariableGroupVariableArgs</span><span class="p">(</span>
            <span class="n">name</span><span class="o">=</span><span class="s2">&quot;key&quot;</span><span class="p">,</span>
            <span class="n">value</span><span class="o">=</span><span class="s2">&quot;value&quot;</span><span class="p">,</span>
        <span class="p">),</span>
        <span class="n">azuredevops</span><span class="o">.</span><span class="n">VariableGroupVariableArgs</span><span class="p">(</span>
            <span class="n">name</span><span class="o">=</span><span class="s2">&quot;Account Password&quot;</span><span class="p">,</span>
            <span class="n">secret_value</span><span class="o">=</span><span class="s2">&quot;p@ssword123&quot;</span><span class="p">,</span>
            <span class="n">is_secret</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
        <span class="p">),</span>
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
<p><strong>Variable groups containing secret values cannot be imported.</strong> Azure DevOps Variable groups can be imported using the project name/variable group ID or by the project Guid/variable group ID, e.g.</p>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>   $ pulumi import azuredevops:index/variableGroup:VariableGroup variablegroup <span class="s2">&quot;Test Project/10&quot;</span>

or
</pre></div>
</div>
<div class="highlight-sh notranslate"><div class="highlight"><pre><span></span>   $ pulumi import azuredevops:index/variableGroup:VariableGroup variablegroup <span class="m">00000000</span>-0000-0000-0000-000000000000/0

*Note that <span class="k">for</span> secret variables, the import <span class="nb">command</span> retrieve blank value in the tfstate.*
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>allow_access</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean that indicate if this variable group is shared by all pipelines of this project.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the Variable Group.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Variable Group.</p></li>
<li><p><strong>project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The project ID or project name.</p></li>
<li><p><strong>variables</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'VariableGroupVariableArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">variable</span></code> blocks as documented below.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_azuredevops.VariableGroup.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">allow_access</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">key_vault</span><span class="p">:</span> <span class="n">Union[VariableGroupKeyVaultArgs, Mapping[str, Any], Awaitable[Union[VariableGroupKeyVaultArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">variables</span><span class="p">:</span> <span class="n">Union[Sequence[Union[VariableGroupVariableArgs, Mapping[str, Any], Awaitable[Union[VariableGroupVariableArgs, Mapping[str, Any]]], Output[T]]], Awaitable[Sequence[Union[VariableGroupVariableArgs, Mapping[str, Any], Awaitable[Union[VariableGroupVariableArgs, Mapping[str, Any]]], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_azuredevops.variable_group.VariableGroup<a class="headerlink" href="#pulumi_azuredevops.VariableGroup.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing VariableGroup resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>allow_access</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean that indicate if this variable group is shared by all pipelines of this project.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the Variable Group.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Variable Group.</p></li>
<li><p><strong>project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The project ID or project name.</p></li>
<li><p><strong>variables</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'VariableGroupVariableArgs'</em><em>]</em><em>]</em><em>]</em><em>]</em>) – One or more <code class="docutils literal notranslate"><span class="pre">variable</span></code> blocks as documented below.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.VariableGroup.allow_access">
<em class="property">property </em><code class="sig-name descname">allow_access</code><a class="headerlink" href="#pulumi_azuredevops.VariableGroup.allow_access" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean that indicate if this variable group is shared by all pipelines of this project.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.VariableGroup.description">
<em class="property">property </em><code class="sig-name descname">description</code><a class="headerlink" href="#pulumi_azuredevops.VariableGroup.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description of the Variable Group.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.VariableGroup.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_azuredevops.VariableGroup.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Variable Group.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.VariableGroup.project_id">
<em class="property">property </em><code class="sig-name descname">project_id</code><a class="headerlink" href="#pulumi_azuredevops.VariableGroup.project_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The project ID or project name.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.VariableGroup.variables">
<em class="property">property </em><code class="sig-name descname">variables</code><a class="headerlink" href="#pulumi_azuredevops.VariableGroup.variables" title="Permalink to this definition">¶</a></dt>
<dd><p>One or more <code class="docutils literal notranslate"><span class="pre">variable</span></code> blocks as documented below.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.VariableGroup.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuredevops.VariableGroup.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azuredevops.VariableGroup.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuredevops.VariableGroup.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azuredevops.WorkItemQueryPermissions">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azuredevops.</code><code class="sig-name descname">WorkItemQueryPermissions</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">path</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">permissions</span><span class="p">:</span> <span class="n">Union[Mapping[str, Union[str, Awaitable[str], Output[T]]], Awaitable[Mapping[str, Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">principal</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">replace</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuredevops.WorkItemQueryPermissions" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages permissions for Work Item Queries.</p>
<blockquote>
<div><p><strong>Note</strong> Permissions can be assigned to group principals and not to single user principals.</p>
</div></blockquote>
<p>Permission for Work Item Queries within Azure DevOps can be applied on two different levels.
Those levels are reflected by specifying (or omitting) values for the arguments <code class="docutils literal notranslate"><span class="pre">project_id</span></code> and <code class="docutils literal notranslate"><span class="pre">path</span></code>.</p>
<p>Permissions for all Work Item Queries inside a project (existing or newly created ones) are specified, if only the argument <code class="docutils literal notranslate"><span class="pre">project_id</span></code> has a value.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_azuredevops</span> <span class="k">as</span> <span class="nn">azuredevops</span>

<span class="n">project_wiq_root_permissions</span> <span class="o">=</span> <span class="n">azuredevops</span><span class="o">.</span><span class="n">WorkItemQueryPermissions</span><span class="p">(</span><span class="s2">&quot;project-wiq-root-permissions&quot;</span><span class="p">,</span>
    <span class="n">project_id</span><span class="o">=</span><span class="n">azuredevops_project</span><span class="p">[</span><span class="s2">&quot;project&quot;</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">],</span>
    <span class="n">principal</span><span class="o">=</span><span class="n">data</span><span class="p">[</span><span class="s2">&quot;azuredevops_group&quot;</span><span class="p">][</span><span class="s2">&quot;project-readers&quot;</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">],</span>
    <span class="n">permissions</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;CreateRepository&quot;</span><span class="p">:</span> <span class="s2">&quot;Deny&quot;</span><span class="p">,</span>
        <span class="s2">&quot;DeleteRepository&quot;</span><span class="p">:</span> <span class="s2">&quot;Deny&quot;</span><span class="p">,</span>
        <span class="s2">&quot;RenameRepository&quot;</span><span class="p">:</span> <span class="s2">&quot;NotSet&quot;</span><span class="p">,</span>
    <span class="p">})</span>
</pre></div>
</div>
<p>Permissions for a specific folder inside Shared Queries are specified if the arguments <code class="docutils literal notranslate"><span class="pre">project_id</span></code> and <code class="docutils literal notranslate"><span class="pre">path</span></code> are set.</p>
<blockquote>
<div><p><strong>Note</strong> To set permissions for the Shared Queries folder itself use <code class="docutils literal notranslate"><span class="pre">/</span></code> as path value</p>
</div></blockquote>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_azuredevops</span> <span class="k">as</span> <span class="nn">azuredevops</span>

<span class="n">wiq_folder_permissions</span> <span class="o">=</span> <span class="n">azuredevops</span><span class="o">.</span><span class="n">WorkItemQueryPermissions</span><span class="p">(</span><span class="s2">&quot;wiq-folder-permissions&quot;</span><span class="p">,</span>
    <span class="n">project_id</span><span class="o">=</span><span class="n">azuredevops_project</span><span class="p">[</span><span class="s2">&quot;project&quot;</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">],</span>
    <span class="n">path</span><span class="o">=</span><span class="s2">&quot;/Team&quot;</span><span class="p">,</span>
    <span class="n">principal</span><span class="o">=</span><span class="n">data</span><span class="p">[</span><span class="s2">&quot;azuredevops_group&quot;</span><span class="p">][</span><span class="s2">&quot;project-readers&quot;</span><span class="p">][</span><span class="s2">&quot;id&quot;</span><span class="p">],</span>
    <span class="n">permissions</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;Contribute&quot;</span><span class="p">:</span> <span class="s2">&quot;Allow&quot;</span><span class="p">,</span>
        <span class="s2">&quot;Delete&quot;</span><span class="p">:</span> <span class="s2">&quot;Deny&quot;</span><span class="p">,</span>
        <span class="s2">&quot;Read&quot;</span><span class="p">:</span> <span class="s2">&quot;NotSet&quot;</span><span class="p">,</span>
    <span class="p">})</span>
</pre></div>
</div>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_azuredevops</span> <span class="k">as</span> <span class="nn">azuredevops</span>

<span class="n">project</span> <span class="o">=</span> <span class="n">azuredevops</span><span class="o">.</span><span class="n">Project</span><span class="p">(</span><span class="s2">&quot;project&quot;</span><span class="p">,</span>
    <span class="n">description</span><span class="o">=</span><span class="s2">&quot;Test Project Description&quot;</span><span class="p">,</span>
    <span class="n">visibility</span><span class="o">=</span><span class="s2">&quot;private&quot;</span><span class="p">,</span>
    <span class="n">version_control</span><span class="o">=</span><span class="s2">&quot;Git&quot;</span><span class="p">,</span>
    <span class="n">work_item_template</span><span class="o">=</span><span class="s2">&quot;Agile&quot;</span><span class="p">)</span>
<span class="n">project_readers</span> <span class="o">=</span> <span class="n">project</span><span class="o">.</span><span class="n">id</span><span class="o">.</span><span class="n">apply</span><span class="p">(</span><span class="k">lambda</span> <span class="nb">id</span><span class="p">:</span> <span class="n">azuredevops</span><span class="o">.</span><span class="n">get_group</span><span class="p">(</span><span class="n">project_id</span><span class="o">=</span><span class="nb">id</span><span class="p">,</span>
    <span class="n">name</span><span class="o">=</span><span class="s2">&quot;Readers&quot;</span><span class="p">))</span>
<span class="n">project_contributors</span> <span class="o">=</span> <span class="n">project</span><span class="o">.</span><span class="n">id</span><span class="o">.</span><span class="n">apply</span><span class="p">(</span><span class="k">lambda</span> <span class="nb">id</span><span class="p">:</span> <span class="n">azuredevops</span><span class="o">.</span><span class="n">get_group</span><span class="p">(</span><span class="n">project_id</span><span class="o">=</span><span class="nb">id</span><span class="p">,</span>
    <span class="n">name</span><span class="o">=</span><span class="s2">&quot;Contributors&quot;</span><span class="p">))</span>
<span class="n">wiq_project_permissions</span> <span class="o">=</span> <span class="n">azuredevops</span><span class="o">.</span><span class="n">WorkItemQueryPermissions</span><span class="p">(</span><span class="s2">&quot;wiq-project-permissions&quot;</span><span class="p">,</span>
    <span class="n">project_id</span><span class="o">=</span><span class="n">project</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">principal</span><span class="o">=</span><span class="n">project_readers</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">permissions</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;Read&quot;</span><span class="p">:</span> <span class="s2">&quot;Allow&quot;</span><span class="p">,</span>
        <span class="s2">&quot;Delete&quot;</span><span class="p">:</span> <span class="s2">&quot;Deny&quot;</span><span class="p">,</span>
        <span class="s2">&quot;Contribute&quot;</span><span class="p">:</span> <span class="s2">&quot;Deny&quot;</span><span class="p">,</span>
        <span class="s2">&quot;ManagePermissions&quot;</span><span class="p">:</span> <span class="s2">&quot;Deny&quot;</span><span class="p">,</span>
    <span class="p">})</span>
<span class="n">wiq_sharedqueries_permissions</span> <span class="o">=</span> <span class="n">azuredevops</span><span class="o">.</span><span class="n">WorkItemQueryPermissions</span><span class="p">(</span><span class="s2">&quot;wiq-sharedqueries-permissions&quot;</span><span class="p">,</span>
    <span class="n">project_id</span><span class="o">=</span><span class="n">project</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">path</span><span class="o">=</span><span class="s2">&quot;/&quot;</span><span class="p">,</span>
    <span class="n">principal</span><span class="o">=</span><span class="n">project_contributors</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">permissions</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;Read&quot;</span><span class="p">:</span> <span class="s2">&quot;Allow&quot;</span><span class="p">,</span>
        <span class="s2">&quot;Delete&quot;</span><span class="p">:</span> <span class="s2">&quot;Deny&quot;</span><span class="p">,</span>
    <span class="p">})</span>
</pre></div>
</div>
<ul class="simple">
<li><p><a class="reference external" href="https://docs.microsoft.com/en-us/rest/api/azure/devops/security/?view=azure-devops-rest-5.1">Azure DevOps Service REST API 5.1 - Security</a></p></li>
</ul>
<ul class="simple">
<li><p><strong>Project &amp; Team</strong>: vso.security_manage - Grants the ability to read, write, and manage security permissions.</p></li>
</ul>
<p>The resource does not support import.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>path</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Path to a query or folder beneath <code class="docutils literal notranslate"><span class="pre">Shared</span> <span class="pre">Queries</span></code></p></li>
<li><p><strong>pulumi.Input</strong><strong>[</strong><strong>str</strong><strong>]</strong><strong>]</strong><strong>] </strong><strong>permissions</strong> (<em>pulumi.Input</em><em>[</em><em>Mapping</em><em>[</em><em>str</em><em>,</em>) – the permissions to assign. The following permissions are available</p></li>
<li><p><strong>principal</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The <strong>group</strong> principal to assign the permissions.</p></li>
<li><p><strong>project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project to assign the permissions.</p></li>
<li><p><strong>replace</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Replace (<code class="docutils literal notranslate"><span class="pre">true</span></code>) or merge (<code class="docutils literal notranslate"><span class="pre">false</span></code>) the permissions. Default: <code class="docutils literal notranslate"><span class="pre">true</span></code></p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_azuredevops.WorkItemQueryPermissions.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">path</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">permissions</span><span class="p">:</span> <span class="n">Union[Mapping[str, Union[str, Awaitable[str], Output[T]]], Awaitable[Mapping[str, Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">principal</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">replace</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_azuredevops.work_item_query_permissions.WorkItemQueryPermissions<a class="headerlink" href="#pulumi_azuredevops.WorkItemQueryPermissions.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing WorkItemQueryPermissions resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>path</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Path to a query or folder beneath <code class="docutils literal notranslate"><span class="pre">Shared</span> <span class="pre">Queries</span></code></p></li>
<li><p><strong>pulumi.Input</strong><strong>[</strong><strong>str</strong><strong>]</strong><strong>]</strong><strong>] </strong><strong>permissions</strong> (<em>pulumi.Input</em><em>[</em><em>Mapping</em><em>[</em><em>str</em><em>,</em>) – the permissions to assign. The following permissions are available</p></li>
<li><p><strong>principal</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The <strong>group</strong> principal to assign the permissions.</p></li>
<li><p><strong>project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project to assign the permissions.</p></li>
<li><p><strong>replace</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Replace (<code class="docutils literal notranslate"><span class="pre">true</span></code>) or merge (<code class="docutils literal notranslate"><span class="pre">false</span></code>) the permissions. Default: <code class="docutils literal notranslate"><span class="pre">true</span></code></p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.WorkItemQueryPermissions.path">
<em class="property">property </em><code class="sig-name descname">path</code><a class="headerlink" href="#pulumi_azuredevops.WorkItemQueryPermissions.path" title="Permalink to this definition">¶</a></dt>
<dd><p>Path to a query or folder beneath <code class="docutils literal notranslate"><span class="pre">Shared</span> <span class="pre">Queries</span></code></p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.WorkItemQueryPermissions.permissions">
<em class="property">property </em><code class="sig-name descname">permissions</code><a class="headerlink" href="#pulumi_azuredevops.WorkItemQueryPermissions.permissions" title="Permalink to this definition">¶</a></dt>
<dd><p>the permissions to assign. The following permissions are available</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.WorkItemQueryPermissions.principal">
<em class="property">property </em><code class="sig-name descname">principal</code><a class="headerlink" href="#pulumi_azuredevops.WorkItemQueryPermissions.principal" title="Permalink to this definition">¶</a></dt>
<dd><p>The <strong>group</strong> principal to assign the permissions.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.WorkItemQueryPermissions.project_id">
<em class="property">property </em><code class="sig-name descname">project_id</code><a class="headerlink" href="#pulumi_azuredevops.WorkItemQueryPermissions.project_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project to assign the permissions.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.WorkItemQueryPermissions.replace">
<em class="property">property </em><code class="sig-name descname">replace</code><a class="headerlink" href="#pulumi_azuredevops.WorkItemQueryPermissions.replace" title="Permalink to this definition">¶</a></dt>
<dd><p>Replace (<code class="docutils literal notranslate"><span class="pre">true</span></code>) or merge (<code class="docutils literal notranslate"><span class="pre">false</span></code>) the permissions. Default: <code class="docutils literal notranslate"><span class="pre">true</span></code></p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.WorkItemQueryPermissions.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuredevops.WorkItemQueryPermissions.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azuredevops.WorkItemQueryPermissions.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuredevops.WorkItemQueryPermissions.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azuredevops.get_agent_queue">
<code class="sig-prename descclassname">pulumi_azuredevops.</code><code class="sig-name descname">get_agent_queue</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_azuredevops.get_agent_queue.AwaitableGetAgentQueueResult<a class="headerlink" href="#pulumi_azuredevops.get_agent_queue" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing Agent Queue within Azure DevOps.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_azuredevops</span> <span class="k">as</span> <span class="nn">azuredevops</span>

<span class="c1"># Azure DevOps project</span>
<span class="n">project</span> <span class="o">=</span> <span class="n">azuredevops</span><span class="o">.</span><span class="n">Project</span><span class="p">(</span><span class="s2">&quot;project&quot;</span><span class="p">,</span>
    <span class="n">work_item_template</span><span class="o">=</span><span class="s2">&quot;Agile&quot;</span><span class="p">,</span>
    <span class="n">version_control</span><span class="o">=</span><span class="s2">&quot;Git&quot;</span><span class="p">,</span>
    <span class="n">visibility</span><span class="o">=</span><span class="s2">&quot;private&quot;</span><span class="p">,</span>
    <span class="n">description</span><span class="o">=</span><span class="s2">&quot;Managed by Terraform&quot;</span><span class="p">)</span>
<span class="n">queue</span> <span class="o">=</span> <span class="n">project</span><span class="o">.</span><span class="n">id</span><span class="o">.</span><span class="n">apply</span><span class="p">(</span><span class="k">lambda</span> <span class="nb">id</span><span class="p">:</span> <span class="n">azuredevops</span><span class="o">.</span><span class="n">get_agent_queue</span><span class="p">(</span><span class="n">project_id</span><span class="o">=</span><span class="nb">id</span><span class="p">,</span>
    <span class="n">name</span><span class="o">=</span><span class="s2">&quot;Sample Agent Queue&quot;</span><span class="p">))</span>
<span class="n">pulumi</span><span class="o">.</span><span class="n">export</span><span class="p">(</span><span class="s2">&quot;name&quot;</span><span class="p">,</span> <span class="n">queue</span><span class="o">.</span><span class="n">name</span><span class="p">)</span>
<span class="n">pulumi</span><span class="o">.</span><span class="n">export</span><span class="p">(</span><span class="s2">&quot;poolId&quot;</span><span class="p">,</span> <span class="n">queue</span><span class="o">.</span><span class="n">agent_pool_id</span><span class="p">)</span>
</pre></div>
</div>
<ul class="simple">
<li><p><a class="reference external" href="https://docs.microsoft.com/en-us/rest/api/azure/devops/distributedtask/queues/get?view=azure-devops-rest-5.1">Azure DevOps Service REST API 5.1 - Agent Queues - Get</a></p></li>
</ul>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>name</strong> (<em>str</em>) – Name of the Agent Queue.</p></li>
<li><p><strong>project_id</strong> (<em>str</em>) – The Project Id.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_azuredevops.get_area">
<code class="sig-prename descclassname">pulumi_azuredevops.</code><code class="sig-name descname">get_area</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">fetch_children</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>bool<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">path</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_azuredevops.get_area.AwaitableGetAreaResult<a class="headerlink" href="#pulumi_azuredevops.get_area" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing Area (Component) within Azure DevOps.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_azuredevops</span> <span class="k">as</span> <span class="nn">azuredevops</span>

<span class="c1">#---------------------------------------------------------------------------</span>
<span class="c1"># Azure DevOps project</span>
<span class="n">project</span> <span class="o">=</span> <span class="n">azuredevops</span><span class="o">.</span><span class="n">Project</span><span class="p">(</span><span class="s2">&quot;project&quot;</span><span class="p">,</span>
    <span class="n">work_item_template</span><span class="o">=</span><span class="s2">&quot;Agile&quot;</span><span class="p">,</span>
    <span class="n">version_control</span><span class="o">=</span><span class="s2">&quot;Git&quot;</span><span class="p">,</span>
    <span class="n">visibility</span><span class="o">=</span><span class="s2">&quot;private&quot;</span><span class="p">,</span>
    <span class="n">description</span><span class="o">=</span><span class="s2">&quot;Managed by Terraform&quot;</span><span class="p">)</span>
<span class="n">area</span> <span class="o">=</span> <span class="n">project</span><span class="o">.</span><span class="n">id</span><span class="o">.</span><span class="n">apply</span><span class="p">(</span><span class="k">lambda</span> <span class="nb">id</span><span class="p">:</span> <span class="n">azuredevops</span><span class="o">.</span><span class="n">get_area</span><span class="p">(</span><span class="n">project_id</span><span class="o">=</span><span class="nb">id</span><span class="p">,</span>
    <span class="n">path</span><span class="o">=</span><span class="s2">&quot;/&quot;</span><span class="p">,</span>
    <span class="n">fetch_children</span><span class="o">=</span><span class="kc">False</span><span class="p">))</span>
</pre></div>
</div>
<ul class="simple">
<li><p><a class="reference external" href="https://docs.microsoft.com/en-us/rest/api/azure/devops/wit/classification%20nodes/get%20classification%20nodes?view=azure-devops-rest-5.1">Azure DevOps Service REST API 5.1 - Classification Nodes - Get Classification Nodes</a></p></li>
</ul>
<ul class="simple">
<li><p><strong>Project &amp; Team</strong>: vso.work - Grants the ability to read work items, queries, boards, area and iterations paths, and other work item tracking related metadata. Also grants the ability to execute queries, search work items and to receive notifications about work item events via service hooks.</p></li>
</ul>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>fetch_children</strong> (<em>bool</em>) – Read children nodes, <em>Depth</em>: 1, <em>Default</em>: <code class="docutils literal notranslate"><span class="pre">true</span></code></p></li>
<li><p><strong>path</strong> (<em>str</em>) – The path to the Area; <em>Format</em>: URL relative; if omitted, or value <code class="docutils literal notranslate"><span class="pre">&quot;/&quot;</span></code> is used, the root Area will be returned</p></li>
<li><p><strong>project_id</strong> (<em>str</em>) – The project ID.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_azuredevops.get_client_config">
<code class="sig-prename descclassname">pulumi_azuredevops.</code><code class="sig-name descname">get_client_config</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_azuredevops.get_client_config.AwaitableGetClientConfigResult<a class="headerlink" href="#pulumi_azuredevops.get_client_config" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about the Azure DevOps organization configured for the provider.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_azuredevops</span> <span class="k">as</span> <span class="nn">azuredevops</span>

<span class="n">client_config</span> <span class="o">=</span> <span class="n">azuredevops</span><span class="o">.</span><span class="n">get_client_config</span><span class="p">()</span>
<span class="n">pulumi</span><span class="o">.</span><span class="n">export</span><span class="p">(</span><span class="s2">&quot;orgUrl&quot;</span><span class="p">,</span> <span class="n">client_config</span><span class="o">.</span><span class="n">organization_url</span><span class="p">)</span>
</pre></div>
</div>
</dd></dl>

<dl class="py function">
<dt id="pulumi_azuredevops.get_git_repository">
<code class="sig-prename descclassname">pulumi_azuredevops.</code><code class="sig-name descname">get_git_repository</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_azuredevops.get_git_repository.AwaitableGetGitRepositoryResult<a class="headerlink" href="#pulumi_azuredevops.get_git_repository" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about a <strong>single</strong> (existing) Git Repository within Azure DevOps.
To read information about <strong>multiple</strong> Git Repositories use the data source <code class="docutils literal notranslate"><span class="pre">getRepositories</span></code></p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_azuredevops</span> <span class="k">as</span> <span class="nn">azuredevops</span>

<span class="n">project</span> <span class="o">=</span> <span class="n">azuredevops</span><span class="o">.</span><span class="n">get_project</span><span class="p">(</span><span class="n">name</span><span class="o">=</span><span class="s2">&quot;contoso-project&quot;</span><span class="p">)</span>
<span class="n">single_repo</span> <span class="o">=</span> <span class="n">azuredevops</span><span class="o">.</span><span class="n">get_git_repository</span><span class="p">(</span><span class="n">project_id</span><span class="o">=</span><span class="n">project</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">name</span><span class="o">=</span><span class="s2">&quot;contoso-repo&quot;</span><span class="p">)</span>
</pre></div>
</div>
<ul class="simple">
<li><p><a class="reference external" href="https://docs.microsoft.com/en-us/rest/api/azure/devops/git/?view=azure-devops-rest-5.1">Azure DevOps Service REST API 5.1 - Git API</a></p></li>
</ul>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>name</strong> (<em>str</em>) – Name of the Git repository to retrieve</p></li>
<li><p><strong>project_id</strong> (<em>str</em>) – ID of project to list Git repositories</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_azuredevops.get_group">
<code class="sig-prename descclassname">pulumi_azuredevops.</code><code class="sig-name descname">get_group</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_azuredevops.get_group.AwaitableGetGroupResult<a class="headerlink" href="#pulumi_azuredevops.get_group" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing Group within Azure DevOps</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_azuredevops</span> <span class="k">as</span> <span class="nn">azuredevops</span>

<span class="n">project</span> <span class="o">=</span> <span class="n">azuredevops</span><span class="o">.</span><span class="n">get_project</span><span class="p">(</span><span class="n">name</span><span class="o">=</span><span class="s2">&quot;contoso-project&quot;</span><span class="p">)</span>
<span class="n">test</span> <span class="o">=</span> <span class="n">azuredevops</span><span class="o">.</span><span class="n">get_group</span><span class="p">(</span><span class="n">project_id</span><span class="o">=</span><span class="n">project</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">name</span><span class="o">=</span><span class="s2">&quot;Test Group&quot;</span><span class="p">)</span>
<span class="n">pulumi</span><span class="o">.</span><span class="n">export</span><span class="p">(</span><span class="s2">&quot;groupId&quot;</span><span class="p">,</span> <span class="n">test</span><span class="o">.</span><span class="n">id</span><span class="p">)</span>
<span class="n">pulumi</span><span class="o">.</span><span class="n">export</span><span class="p">(</span><span class="s2">&quot;groupDescriptor&quot;</span><span class="p">,</span> <span class="n">test</span><span class="o">.</span><span class="n">descriptor</span><span class="p">)</span>
<span class="n">test_collection_group</span> <span class="o">=</span> <span class="n">azuredevops</span><span class="o">.</span><span class="n">get_group</span><span class="p">(</span><span class="n">name</span><span class="o">=</span><span class="s2">&quot;Project Collection Administrators&quot;</span><span class="p">)</span>
<span class="n">pulumi</span><span class="o">.</span><span class="n">export</span><span class="p">(</span><span class="s2">&quot;collectionGroupId&quot;</span><span class="p">,</span> <span class="n">test_collection_group</span><span class="o">.</span><span class="n">id</span><span class="p">)</span>
<span class="n">pulumi</span><span class="o">.</span><span class="n">export</span><span class="p">(</span><span class="s2">&quot;collectionGroupDescriptor&quot;</span><span class="p">,</span> <span class="n">test_collection_group</span><span class="o">.</span><span class="n">descriptor</span><span class="p">)</span>
</pre></div>
</div>
<ul class="simple">
<li><p><a class="reference external" href="https://docs.microsoft.com/en-us/rest/api/azure/devops/graph/groups/get?view=azure-devops-rest-5.1">Azure DevOps Service REST API 5.1 - Groups - Get</a></p></li>
</ul>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>name</strong> (<em>str</em>) – The Group Name.</p></li>
<li><p><strong>project_id</strong> (<em>str</em>) – The Project ID. If no project ID is specified the project collection groups will be searched.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_azuredevops.get_iteration">
<code class="sig-prename descclassname">pulumi_azuredevops.</code><code class="sig-name descname">get_iteration</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">fetch_children</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>bool<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">path</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_azuredevops.get_iteration.AwaitableGetIterationResult<a class="headerlink" href="#pulumi_azuredevops.get_iteration" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing Iteration (Sprint) within Azure DevOps.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_azuredevops</span> <span class="k">as</span> <span class="nn">azuredevops</span>

<span class="n">project</span> <span class="o">=</span> <span class="n">azuredevops</span><span class="o">.</span><span class="n">Project</span><span class="p">(</span><span class="s2">&quot;project&quot;</span><span class="p">,</span>
    <span class="n">work_item_template</span><span class="o">=</span><span class="s2">&quot;Agile&quot;</span><span class="p">,</span>
    <span class="n">version_control</span><span class="o">=</span><span class="s2">&quot;Git&quot;</span><span class="p">,</span>
    <span class="n">visibility</span><span class="o">=</span><span class="s2">&quot;private&quot;</span><span class="p">,</span>
    <span class="n">description</span><span class="o">=</span><span class="s2">&quot;Managed by Terraform&quot;</span><span class="p">)</span>
<span class="n">root_iteration</span> <span class="o">=</span> <span class="n">project</span><span class="o">.</span><span class="n">id</span><span class="o">.</span><span class="n">apply</span><span class="p">(</span><span class="k">lambda</span> <span class="nb">id</span><span class="p">:</span> <span class="n">azuredevops</span><span class="o">.</span><span class="n">get_iteration</span><span class="p">(</span><span class="n">project_id</span><span class="o">=</span><span class="nb">id</span><span class="p">,</span>
    <span class="n">path</span><span class="o">=</span><span class="s2">&quot;/&quot;</span><span class="p">,</span>
    <span class="n">fetch_children</span><span class="o">=</span><span class="kc">True</span><span class="p">))</span>
<span class="n">child_iteration</span> <span class="o">=</span> <span class="n">project</span><span class="o">.</span><span class="n">id</span><span class="o">.</span><span class="n">apply</span><span class="p">(</span><span class="k">lambda</span> <span class="nb">id</span><span class="p">:</span> <span class="n">azuredevops</span><span class="o">.</span><span class="n">get_iteration</span><span class="p">(</span><span class="n">project_id</span><span class="o">=</span><span class="nb">id</span><span class="p">,</span>
    <span class="n">path</span><span class="o">=</span><span class="s2">&quot;/Iteration 1&quot;</span><span class="p">,</span>
    <span class="n">fetch_children</span><span class="o">=</span><span class="kc">True</span><span class="p">))</span>
</pre></div>
</div>
<ul class="simple">
<li><p><a class="reference external" href="https://docs.microsoft.com/en-us/rest/api/azure/devops/wit/classification%20nodes/get%20classification%20nodes?view=azure-devops-rest-5.1">Azure DevOps Service REST API 5.1 - Classification Nodes - Get Classification Nodes</a></p></li>
</ul>
<ul class="simple">
<li><p><strong>Project &amp; Team</strong>: vso.work - Grants the ability to read work items, queries, boards, area and iterations paths, and other work item tracking related metadata. Also grants the ability to execute queries, search work items and to receive notifications about work item events via service hooks.</p></li>
</ul>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>fetch_children</strong> (<em>bool</em>) – Read children nodes, <em>Depth</em>: 1, <em>Default</em>: <code class="docutils literal notranslate"><span class="pre">true</span></code></p></li>
<li><p><strong>path</strong> (<em>str</em>) – The path to the Iteration, <em>Format</em>: URL relative; if omitted, or value <code class="docutils literal notranslate"><span class="pre">&quot;/&quot;</span></code> is used, the root Iteration will be returned</p></li>
<li><p><strong>project_id</strong> (<em>str</em>) – The project ID.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_azuredevops.get_pool">
<code class="sig-prename descclassname">pulumi_azuredevops.</code><code class="sig-name descname">get_pool</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_azuredevops.get_pool.AwaitableGetPoolResult<a class="headerlink" href="#pulumi_azuredevops.get_pool" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing Agent Pool within Azure DevOps.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_azuredevops</span> <span class="k">as</span> <span class="nn">azuredevops</span>

<span class="n">pool</span> <span class="o">=</span> <span class="n">azuredevops</span><span class="o">.</span><span class="n">get_pool</span><span class="p">(</span><span class="n">name</span><span class="o">=</span><span class="s2">&quot;Sample Agent Pool&quot;</span><span class="p">)</span>
<span class="n">pulumi</span><span class="o">.</span><span class="n">export</span><span class="p">(</span><span class="s2">&quot;name&quot;</span><span class="p">,</span> <span class="n">pool</span><span class="o">.</span><span class="n">name</span><span class="p">)</span>
<span class="n">pulumi</span><span class="o">.</span><span class="n">export</span><span class="p">(</span><span class="s2">&quot;poolType&quot;</span><span class="p">,</span> <span class="n">pool</span><span class="o">.</span><span class="n">pool_type</span><span class="p">)</span>
<span class="n">pulumi</span><span class="o">.</span><span class="n">export</span><span class="p">(</span><span class="s2">&quot;autoProvision&quot;</span><span class="p">,</span> <span class="n">pool</span><span class="o">.</span><span class="n">auto_provision</span><span class="p">)</span>
</pre></div>
</div>
<ul class="simple">
<li><p><a class="reference external" href="https://docs.microsoft.com/en-us/rest/api/azure/devops/distributedtask/pools/get?view=azure-devops-rest-5.1">Azure DevOps Service REST API 5.1 - Agent Pools - Get</a></p></li>
</ul>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>name</strong> (<em>str</em>) – Name of the Agent Pool.</p>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_azuredevops.get_pools">
<code class="sig-prename descclassname">pulumi_azuredevops.</code><code class="sig-name descname">get_pools</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_azuredevops.get_pools.AwaitableGetPoolsResult<a class="headerlink" href="#pulumi_azuredevops.get_pools" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about existing Agent Pools within Azure DevOps.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_azuredevops</span> <span class="k">as</span> <span class="nn">azuredevops</span>

<span class="n">pools</span> <span class="o">=</span> <span class="n">azuredevops</span><span class="o">.</span><span class="n">get_pools</span><span class="p">()</span>
<span class="n">pulumi</span><span class="o">.</span><span class="n">export</span><span class="p">(</span><span class="s2">&quot;agentPoolName&quot;</span><span class="p">,</span> <span class="p">[</span><span class="n">__item</span><span class="o">.</span><span class="n">name</span> <span class="k">for</span> <span class="n">__item</span> <span class="ow">in</span> <span class="n">pools</span><span class="o">.</span><span class="n">agent_pools</span><span class="p">])</span>
<span class="n">pulumi</span><span class="o">.</span><span class="n">export</span><span class="p">(</span><span class="s2">&quot;autoProvision&quot;</span><span class="p">,</span> <span class="p">[</span><span class="n">__item</span><span class="o">.</span><span class="n">auto_provision</span> <span class="k">for</span> <span class="n">__item</span> <span class="ow">in</span> <span class="n">pools</span><span class="o">.</span><span class="n">agent_pools</span><span class="p">])</span>
<span class="n">pulumi</span><span class="o">.</span><span class="n">export</span><span class="p">(</span><span class="s2">&quot;poolType&quot;</span><span class="p">,</span> <span class="p">[</span><span class="n">__item</span><span class="o">.</span><span class="n">pool_type</span> <span class="k">for</span> <span class="n">__item</span> <span class="ow">in</span> <span class="n">pools</span><span class="o">.</span><span class="n">agent_pools</span><span class="p">])</span>
</pre></div>
</div>
<ul class="simple">
<li><p><a class="reference external" href="https://docs.microsoft.com/en-us/rest/api/azure/devops/distributedtask/pools/get?view=azure-devops-rest-5.1">Azure DevOps Service REST API 5.1 - Agent Pools - Get</a></p></li>
</ul>
</dd></dl>

<dl class="py function">
<dt id="pulumi_azuredevops.get_project">
<code class="sig-prename descclassname">pulumi_azuredevops.</code><code class="sig-name descname">get_project</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_azuredevops.get_project.AwaitableGetProjectResult<a class="headerlink" href="#pulumi_azuredevops.get_project" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing Project within Azure DevOps.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_azuredevops</span> <span class="k">as</span> <span class="nn">azuredevops</span>

<span class="n">project</span> <span class="o">=</span> <span class="n">azuredevops</span><span class="o">.</span><span class="n">get_project</span><span class="p">(</span><span class="n">name</span><span class="o">=</span><span class="s2">&quot;Sample Project&quot;</span><span class="p">)</span>
<span class="n">pulumi</span><span class="o">.</span><span class="n">export</span><span class="p">(</span><span class="s2">&quot;id&quot;</span><span class="p">,</span> <span class="n">project</span><span class="o">.</span><span class="n">id</span><span class="p">)</span>
<span class="n">pulumi</span><span class="o">.</span><span class="n">export</span><span class="p">(</span><span class="s2">&quot;name&quot;</span><span class="p">,</span> <span class="n">project</span><span class="o">.</span><span class="n">name</span><span class="p">)</span>
<span class="n">pulumi</span><span class="o">.</span><span class="n">export</span><span class="p">(</span><span class="s2">&quot;visibility&quot;</span><span class="p">,</span> <span class="n">project</span><span class="o">.</span><span class="n">visibility</span><span class="p">)</span>
<span class="n">pulumi</span><span class="o">.</span><span class="n">export</span><span class="p">(</span><span class="s2">&quot;versionControl&quot;</span><span class="p">,</span> <span class="n">project</span><span class="o">.</span><span class="n">version_control</span><span class="p">)</span>
<span class="n">pulumi</span><span class="o">.</span><span class="n">export</span><span class="p">(</span><span class="s2">&quot;workItemTemplate&quot;</span><span class="p">,</span> <span class="n">project</span><span class="o">.</span><span class="n">work_item_template</span><span class="p">)</span>
<span class="n">pulumi</span><span class="o">.</span><span class="n">export</span><span class="p">(</span><span class="s2">&quot;processTemplateId&quot;</span><span class="p">,</span> <span class="n">project</span><span class="o">.</span><span class="n">process_template_id</span><span class="p">)</span>
</pre></div>
</div>
<ul class="simple">
<li><p><a class="reference external" href="https://docs.microsoft.com/en-us/rest/api/azure/devops/core/projects/get?view=azure-devops-rest-5.1">Azure DevOps Service REST API 5.1 - Projects - Get</a></p></li>
</ul>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>name</strong> (<em>str</em>) – Name of the Project.</p></li>
<li><p><strong>project_id</strong> (<em>str</em>) – ID of the Project.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_azuredevops.get_projects">
<code class="sig-prename descclassname">pulumi_azuredevops.</code><code class="sig-name descname">get_projects</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">state</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_azuredevops.get_projects.AwaitableGetProjectsResult<a class="headerlink" href="#pulumi_azuredevops.get_projects" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about existing Projects within Azure DevOps.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_azuredevops</span> <span class="k">as</span> <span class="nn">azuredevops</span>

<span class="n">test</span> <span class="o">=</span> <span class="n">azuredevops</span><span class="o">.</span><span class="n">get_projects</span><span class="p">(</span><span class="n">name</span><span class="o">=</span><span class="s2">&quot;contoso&quot;</span><span class="p">,</span>
    <span class="n">state</span><span class="o">=</span><span class="s2">&quot;wellFormed&quot;</span><span class="p">)</span>
<span class="n">pulumi</span><span class="o">.</span><span class="n">export</span><span class="p">(</span><span class="s2">&quot;projectId&quot;</span><span class="p">,</span> <span class="p">[</span><span class="n">__item</span><span class="o">.</span><span class="n">project_id</span> <span class="k">for</span> <span class="n">__item</span> <span class="ow">in</span> <span class="n">test</span><span class="o">.</span><span class="n">projects</span><span class="p">])</span>
<span class="n">pulumi</span><span class="o">.</span><span class="n">export</span><span class="p">(</span><span class="s2">&quot;name&quot;</span><span class="p">,</span> <span class="p">[</span><span class="n">__item</span><span class="o">.</span><span class="n">name</span> <span class="k">for</span> <span class="n">__item</span> <span class="ow">in</span> <span class="n">test</span><span class="o">.</span><span class="n">projects</span><span class="p">])</span>
<span class="n">pulumi</span><span class="o">.</span><span class="n">export</span><span class="p">(</span><span class="s2">&quot;projectUrl&quot;</span><span class="p">,</span> <span class="p">[</span><span class="n">__item</span><span class="o">.</span><span class="n">project_url</span> <span class="k">for</span> <span class="n">__item</span> <span class="ow">in</span> <span class="n">test</span><span class="o">.</span><span class="n">projects</span><span class="p">])</span>
<span class="n">pulumi</span><span class="o">.</span><span class="n">export</span><span class="p">(</span><span class="s2">&quot;state&quot;</span><span class="p">,</span> <span class="p">[</span><span class="n">__item</span><span class="o">.</span><span class="n">state</span> <span class="k">for</span> <span class="n">__item</span> <span class="ow">in</span> <span class="n">test</span><span class="o">.</span><span class="n">projects</span><span class="p">])</span>
</pre></div>
</div>
<ul class="simple">
<li><p><a class="reference external" href="https://docs.microsoft.com/en-us/rest/api/azure/devops/core/projects/get?view=azure-devops-rest-5.1">Azure DevOps Service REST API 5.1 - Projects - Get</a></p></li>
</ul>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>name</strong> (<em>str</em>) – Name of the Project, if not specified all projects will be returned.</p></li>
<li><p><strong>state</strong> (<em>str</em>) – State of the Project, if not specified all projects will be returned. Valid values are <code class="docutils literal notranslate"><span class="pre">all</span></code>, <code class="docutils literal notranslate"><span class="pre">deleting</span></code>, <code class="docutils literal notranslate"><span class="pre">new</span></code>, <code class="docutils literal notranslate"><span class="pre">wellFormed</span></code>, <code class="docutils literal notranslate"><span class="pre">createPending</span></code>, <code class="docutils literal notranslate"><span class="pre">unchanged</span></code>,<code class="docutils literal notranslate"><span class="pre">deleted</span></code>.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_azuredevops.get_repositories">
<code class="sig-prename descclassname">pulumi_azuredevops.</code><code class="sig-name descname">get_repositories</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">include_hidden</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>bool<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_azuredevops.get_repositories.AwaitableGetRepositoriesResult<a class="headerlink" href="#pulumi_azuredevops.get_repositories" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about <strong>multiple</strong> existing Git Repositories within Azure DevOps.
To read informations about a <strong>single</strong> Git Repository use the data source <code class="docutils literal notranslate"><span class="pre">Git</span></code></p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_azuredevops</span> <span class="k">as</span> <span class="nn">azuredevops</span>

<span class="n">project</span> <span class="o">=</span> <span class="n">azuredevops</span><span class="o">.</span><span class="n">get_project</span><span class="p">(</span><span class="n">name</span><span class="o">=</span><span class="s2">&quot;contoso-project&quot;</span><span class="p">)</span>
<span class="n">all_repos</span> <span class="o">=</span> <span class="n">azuredevops</span><span class="o">.</span><span class="n">get_repositories</span><span class="p">(</span><span class="n">project_id</span><span class="o">=</span><span class="n">project</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">include_hidden</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
<span class="n">single_repo</span> <span class="o">=</span> <span class="n">azuredevops</span><span class="o">.</span><span class="n">get_repositories</span><span class="p">(</span><span class="n">project_id</span><span class="o">=</span><span class="n">project</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">name</span><span class="o">=</span><span class="s2">&quot;contoso-repo&quot;</span><span class="p">)</span>
</pre></div>
</div>
<ul class="simple">
<li><p><a class="reference external" href="https://docs.microsoft.com/en-us/rest/api/azure/devops/git/?view=azure-devops-rest-5.1">Azure DevOps Service REST API 5.1 - Git API</a></p></li>
</ul>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>name</strong> (<em>str</em>) – Name of the Git repository to retrieve; requires <code class="docutils literal notranslate"><span class="pre">project_id</span></code> to be specified as well</p></li>
<li><p><strong>project_id</strong> (<em>str</em>) – ID of project to list Git repositories</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_azuredevops.get_users">
<code class="sig-prename descclassname">pulumi_azuredevops.</code><code class="sig-name descname">get_users</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">origin</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">origin_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">principal_name</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">subject_types</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>Sequence<span class="p">[</span>str<span class="p">]</span><span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_azuredevops.get_users.AwaitableGetUsersResult<a class="headerlink" href="#pulumi_azuredevops.get_users" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing users within Azure DevOps.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_azuredevops</span> <span class="k">as</span> <span class="nn">azuredevops</span>

<span class="n">user</span> <span class="o">=</span> <span class="n">azuredevops</span><span class="o">.</span><span class="n">get_users</span><span class="p">(</span><span class="n">principal_name</span><span class="o">=</span><span class="s2">&quot;contoso-user@contoso.onmicrosoft.com&quot;</span><span class="p">)</span>
<span class="n">all_users</span> <span class="o">=</span> <span class="n">azuredevops</span><span class="o">.</span><span class="n">get_users</span><span class="p">()</span>
<span class="n">all_from_origin</span> <span class="o">=</span> <span class="n">azuredevops</span><span class="o">.</span><span class="n">get_users</span><span class="p">(</span><span class="n">origin</span><span class="o">=</span><span class="s2">&quot;aad&quot;</span><span class="p">)</span>
<span class="n">all_from_subject_types</span> <span class="o">=</span> <span class="n">azuredevops</span><span class="o">.</span><span class="n">get_users</span><span class="p">(</span><span class="n">subject_types</span><span class="o">=</span><span class="p">[</span>
    <span class="s2">&quot;aad&quot;</span><span class="p">,</span>
    <span class="s2">&quot;msa&quot;</span><span class="p">,</span>
<span class="p">])</span>
<span class="n">all_from_origin_id</span> <span class="o">=</span> <span class="n">azuredevops</span><span class="o">.</span><span class="n">get_users</span><span class="p">(</span><span class="n">origin</span><span class="o">=</span><span class="s2">&quot;aad&quot;</span><span class="p">,</span>
    <span class="n">origin_id</span><span class="o">=</span><span class="s2">&quot;a7ead982-8438-4cd2-b9e3-c3aa51a7b675&quot;</span><span class="p">)</span>
</pre></div>
</div>
<ul class="simple">
<li><p><a class="reference external" href="https://docs.microsoft.com/en-us/rest/api/azure/devops/graph/users?view=azure-devops-rest-5.1">Azure DevOps Service REST API 5.1 - Graph Users API</a></p></li>
</ul>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>origin</strong> (<em>str</em>) – The type of source provider for the <code class="docutils literal notranslate"><span class="pre">origin_id</span></code> parameter (ex:AD, AAD, MSA) The supported origins are listed below.</p></li>
<li><p><strong>origin_id</strong> (<em>str</em>) – The unique identifier from the system of origin.</p></li>
<li><p><strong>principal_name</strong> (<em>str</em>) – The PrincipalName of this graph member from the source provider.</p></li>
<li><p><strong>subject_types</strong> (<em>Sequence</em><em>[</em><em>str</em><em>]</em>) – A list of user subject subtypes to reduce the retrieved results, e.g. <code class="docutils literal notranslate"><span class="pre">msa</span></code>, <code class="docutils literal notranslate"><span class="pre">aad</span></code>, <code class="docutils literal notranslate"><span class="pre">svc</span></code> (service identity), <code class="docutils literal notranslate"><span class="pre">imp</span></code> (imported identity), etc. The supported subject types are listed below.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

</div>
