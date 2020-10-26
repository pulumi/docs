---
title: Package pulumi_gitlab
title_tag: Package pulumi_gitlab | Python SDK
linktitle: pulumi_gitlab
notitle: true
block_external_search_index: true
---

{{< resource-docs-alert "gitlab" >}}

<div class="section" id="pulumi-gitlab">
<h1>Pulumi GitLab<a class="headerlink" href="#pulumi-gitlab" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-gitlab">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-gitlab/issues">pulumi/pulumi-gitlab repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-gitlab/issues">terraform-providers/terraform-provider-gitlab repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_gitlab"></span><dl class="py class">
<dt id="pulumi_gitlab.AwaitableGetGroupMembershipResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gitlab.</code><code class="sig-name descname">AwaitableGetGroupMembershipResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">access_level</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">full_path</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">group_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">members</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gitlab.AwaitableGetGroupMembershipResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_gitlab.AwaitableGetGroupResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gitlab.</code><code class="sig-name descname">AwaitableGetGroupResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">full_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">full_path</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">group_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">lfs_enabled</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">parent_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">path</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">request_access_enabled</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">runners_token</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">visibility_level</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">web_url</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gitlab.AwaitableGetGroupResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_gitlab.AwaitableGetProjectResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gitlab.</code><code class="sig-name descname">AwaitableGetProjectResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">archived</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">default_branch</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">http_url_to_repo</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">issues_enabled</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">lfs_enabled</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">merge_requests_enabled</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">namespace_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">path</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">path_with_namespace</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">pipelines_enabled</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">push_rules</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">remove_source_branch_after_merge</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">request_access_enabled</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">runners_token</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">snippets_enabled</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ssh_url_to_repo</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">visibility_level</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">web_url</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">wiki_enabled</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gitlab.AwaitableGetProjectResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_gitlab.AwaitableGetProjectsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gitlab.</code><code class="sig-name descname">AwaitableGetProjectsResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">archived</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">group_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">include_subgroups</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">max_queryable_pages</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">membership</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">min_access_level</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">order_by</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">owned</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">page</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">per_page</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">projects</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">search</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">simple</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sort</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">starred</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">statistics</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">visibility</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">with_custom_attributes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">with_issues_enabled</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">with_merge_requests_enabled</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">with_programming_language</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">with_shared</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gitlab.AwaitableGetProjectsResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_gitlab.AwaitableGetUserResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gitlab.</code><code class="sig-name descname">AwaitableGetUserResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">avatar_url</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">bio</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">can_create_group</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">can_create_project</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">color_scheme_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">created_at</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">current_sign_in_at</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">email</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">extern_uid</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">external</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">is_admin</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">last_sign_in_at</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">linkedin</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">location</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">organization</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">projects_limit</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">skype</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">state</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">theme_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">twitter</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">two_factor_enabled</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_provider</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">username</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">website_url</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gitlab.AwaitableGetUserResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_gitlab.AwaitableGetUsersResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gitlab.</code><code class="sig-name descname">AwaitableGetUsersResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">active</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">blocked</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">created_after</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">created_before</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">extern_provider</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">extern_uid</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">order_by</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">search</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sort</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">users</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gitlab.AwaitableGetUsersResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_gitlab.BranchProtection">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gitlab.</code><code class="sig-name descname">BranchProtection</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">branch</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">code_owner_approval_required</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">merge_access_level</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">push_access_level</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gitlab.BranchProtection" title="Permalink to this definition">¶</a></dt>
<dd><p>This resource allows you to protect a specific branch by an access level so that the user with less access level cannot Merge/Push to the branch. GitLab EE features to protect by group or user are not supported.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_gitlab</span> <span class="k">as</span> <span class="nn">gitlab</span>

<span class="n">branch_protect</span> <span class="o">=</span> <span class="n">gitlab</span><span class="o">.</span><span class="n">BranchProtection</span><span class="p">(</span><span class="s2">&quot;branchProtect&quot;</span><span class="p">,</span>
    <span class="n">branch</span><span class="o">=</span><span class="s2">&quot;BranchProtected&quot;</span><span class="p">,</span>
    <span class="n">merge_access_level</span><span class="o">=</span><span class="s2">&quot;developer&quot;</span><span class="p">,</span>
    <span class="n">project</span><span class="o">=</span><span class="s2">&quot;12345&quot;</span><span class="p">,</span>
    <span class="n">push_access_level</span><span class="o">=</span><span class="s2">&quot;developer&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>branch</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the branch.</p></li>
<li><p><strong>code_owner_approval_required</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Bool, defaults to false. Can be set to true to require code owner approval before merging.</p></li>
<li><p><strong>merge_access_level</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – One of five levels of access to the project.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The id of the project.</p></li>
<li><p><strong>push_access_level</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – One of five levels of access to the project.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_gitlab.BranchProtection.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">branch</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">code_owner_approval_required</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">merge_access_level</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">push_access_level</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_gitlab.branch_protection.BranchProtection<a class="headerlink" href="#pulumi_gitlab.BranchProtection.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing BranchProtection resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>branch</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the branch.</p></li>
<li><p><strong>code_owner_approval_required</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Bool, defaults to false. Can be set to true to require code owner approval before merging.</p></li>
<li><p><strong>merge_access_level</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – One of five levels of access to the project.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The id of the project.</p></li>
<li><p><strong>push_access_level</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – One of five levels of access to the project.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.BranchProtection.branch">
<em class="property">property </em><code class="sig-name descname">branch</code><a class="headerlink" href="#pulumi_gitlab.BranchProtection.branch" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the branch.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.BranchProtection.code_owner_approval_required">
<em class="property">property </em><code class="sig-name descname">code_owner_approval_required</code><a class="headerlink" href="#pulumi_gitlab.BranchProtection.code_owner_approval_required" title="Permalink to this definition">¶</a></dt>
<dd><p>Bool, defaults to false. Can be set to true to require code owner approval before merging.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.BranchProtection.merge_access_level">
<em class="property">property </em><code class="sig-name descname">merge_access_level</code><a class="headerlink" href="#pulumi_gitlab.BranchProtection.merge_access_level" title="Permalink to this definition">¶</a></dt>
<dd><p>One of five levels of access to the project.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.BranchProtection.project">
<em class="property">property </em><code class="sig-name descname">project</code><a class="headerlink" href="#pulumi_gitlab.BranchProtection.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The id of the project.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.BranchProtection.push_access_level">
<em class="property">property </em><code class="sig-name descname">push_access_level</code><a class="headerlink" href="#pulumi_gitlab.BranchProtection.push_access_level" title="Permalink to this definition">¶</a></dt>
<dd><p>One of five levels of access to the project.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.BranchProtection.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gitlab.BranchProtection.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gitlab.BranchProtection.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gitlab.BranchProtection.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gitlab.DeployKey">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gitlab.</code><code class="sig-name descname">DeployKey</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">can_push</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">key</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">title</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gitlab.DeployKey" title="Permalink to this definition">¶</a></dt>
<dd><p>This resource allows you to create and manage deploy keys for your GitLab projects.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_gitlab</span> <span class="k">as</span> <span class="nn">gitlab</span>

<span class="n">example</span> <span class="o">=</span> <span class="n">gitlab</span><span class="o">.</span><span class="n">DeployKey</span><span class="p">(</span><span class="s2">&quot;example&quot;</span><span class="p">,</span>
    <span class="n">key</span><span class="o">=</span><span class="s2">&quot;ssh-rsa AAAA...&quot;</span><span class="p">,</span>
    <span class="n">project</span><span class="o">=</span><span class="s2">&quot;example/deploying&quot;</span><span class="p">,</span>
    <span class="n">title</span><span class="o">=</span><span class="s2">&quot;Example deploy key&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>can_push</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Allow this deploy key to be used to push changes to the project.  Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>. <strong>NOTE:</strong> this cannot currently be managed.</p></li>
<li><p><strong>key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The public ssh key body.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name or id of the project to add the deploy key to.</p></li>
<li><p><strong>title</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A title to describe the deploy key with.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_gitlab.DeployKey.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">can_push</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">key</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">title</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_gitlab.deploy_key.DeployKey<a class="headerlink" href="#pulumi_gitlab.DeployKey.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing DeployKey resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>can_push</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Allow this deploy key to be used to push changes to the project.  Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>. <strong>NOTE:</strong> this cannot currently be managed.</p></li>
<li><p><strong>key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The public ssh key body.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name or id of the project to add the deploy key to.</p></li>
<li><p><strong>title</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A title to describe the deploy key with.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.DeployKey.can_push">
<em class="property">property </em><code class="sig-name descname">can_push</code><a class="headerlink" href="#pulumi_gitlab.DeployKey.can_push" title="Permalink to this definition">¶</a></dt>
<dd><p>Allow this deploy key to be used to push changes to the project.  Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>. <strong>NOTE:</strong> this cannot currently be managed.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.DeployKey.key">
<em class="property">property </em><code class="sig-name descname">key</code><a class="headerlink" href="#pulumi_gitlab.DeployKey.key" title="Permalink to this definition">¶</a></dt>
<dd><p>The public ssh key body.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.DeployKey.project">
<em class="property">property </em><code class="sig-name descname">project</code><a class="headerlink" href="#pulumi_gitlab.DeployKey.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The name or id of the project to add the deploy key to.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.DeployKey.title">
<em class="property">property </em><code class="sig-name descname">title</code><a class="headerlink" href="#pulumi_gitlab.DeployKey.title" title="Permalink to this definition">¶</a></dt>
<dd><p>A title to describe the deploy key with.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.DeployKey.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gitlab.DeployKey.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gitlab.DeployKey.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gitlab.DeployKey.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gitlab.DeployKeyEnable">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gitlab.</code><code class="sig-name descname">DeployKeyEnable</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">can_push</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">key</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">key_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">title</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gitlab.DeployKeyEnable" title="Permalink to this definition">¶</a></dt>
<dd><p>This resource allows you to enable pre-existing deploy keys for your GitLab projects.</p>
<p><strong>the GITLAB KEY_ID for the deploy key must be known</strong></p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_gitlab</span> <span class="k">as</span> <span class="nn">gitlab</span>

<span class="c1"># A repo to host the deployment key</span>
<span class="n">parent_project</span> <span class="o">=</span> <span class="n">gitlab</span><span class="o">.</span><span class="n">Project</span><span class="p">(</span><span class="s2">&quot;parentProject&quot;</span><span class="p">)</span>
<span class="c1"># A second repo to use the deployment key from the parent project</span>
<span class="n">foo_project</span> <span class="o">=</span> <span class="n">gitlab</span><span class="o">.</span><span class="n">Project</span><span class="p">(</span><span class="s2">&quot;fooProject&quot;</span><span class="p">)</span>
<span class="c1"># Upload a deployment key for the parent repo</span>
<span class="n">parent_deploy_key</span> <span class="o">=</span> <span class="n">gitlab</span><span class="o">.</span><span class="n">DeployKey</span><span class="p">(</span><span class="s2">&quot;parentDeployKey&quot;</span><span class="p">,</span>
    <span class="n">key</span><span class="o">=</span><span class="s2">&quot;ssh-rsa AAAA...&quot;</span><span class="p">,</span>
    <span class="n">project</span><span class="o">=</span><span class="n">parent_project</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">title</span><span class="o">=</span><span class="s2">&quot;Example deploy key&quot;</span><span class="p">)</span>
<span class="c1"># Enable the deployment key on the second repo</span>
<span class="n">foo_deploy_key_enable</span> <span class="o">=</span> <span class="n">gitlab</span><span class="o">.</span><span class="n">DeployKeyEnable</span><span class="p">(</span><span class="s2">&quot;fooDeployKeyEnable&quot;</span><span class="p">,</span>
    <span class="n">key_id</span><span class="o">=</span><span class="n">parent_deploy_key</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">project</span><span class="o">=</span><span class="n">foo_project</span><span class="o">.</span><span class="n">id</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>key_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Gitlab key id for the pre-existing deploy key</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name or id of the project to add the deploy key to.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_gitlab.DeployKeyEnable.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">can_push</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">key</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">key_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">title</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_gitlab.deploy_key_enable.DeployKeyEnable<a class="headerlink" href="#pulumi_gitlab.DeployKeyEnable.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing DeployKeyEnable resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>key_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Gitlab key id for the pre-existing deploy key</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name or id of the project to add the deploy key to.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.DeployKeyEnable.key_id">
<em class="property">property </em><code class="sig-name descname">key_id</code><a class="headerlink" href="#pulumi_gitlab.DeployKeyEnable.key_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The Gitlab key id for the pre-existing deploy key</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.DeployKeyEnable.project">
<em class="property">property </em><code class="sig-name descname">project</code><a class="headerlink" href="#pulumi_gitlab.DeployKeyEnable.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The name or id of the project to add the deploy key to.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.DeployKeyEnable.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gitlab.DeployKeyEnable.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gitlab.DeployKeyEnable.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gitlab.DeployKeyEnable.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gitlab.DeployToken">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gitlab.</code><code class="sig-name descname">DeployToken</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">expires_at</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">group</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">scopes</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">username</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gitlab.DeployToken" title="Permalink to this definition">¶</a></dt>
<dd><p>This resource allows you to create and manage deploy token for your GitLab projects and groups.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_gitlab</span> <span class="k">as</span> <span class="nn">gitlab</span>

<span class="n">example</span> <span class="o">=</span> <span class="n">gitlab</span><span class="o">.</span><span class="n">DeployToken</span><span class="p">(</span><span class="s2">&quot;example&quot;</span><span class="p">,</span>
    <span class="n">expires_at</span><span class="o">=</span><span class="s2">&quot;2020-03-14T00:00:00.000Z&quot;</span><span class="p">,</span>
    <span class="n">project</span><span class="o">=</span><span class="s2">&quot;example/deploying&quot;</span><span class="p">,</span>
    <span class="n">scopes</span><span class="o">=</span><span class="p">[</span>
        <span class="s2">&quot;read_repository&quot;</span><span class="p">,</span>
        <span class="s2">&quot;read_registry&quot;</span><span class="p">,</span>
    <span class="p">],</span>
    <span class="n">username</span><span class="o">=</span><span class="s2">&quot;example-username&quot;</span><span class="p">)</span>
</pre></div>
</div>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_gitlab</span> <span class="k">as</span> <span class="nn">gitlab</span>

<span class="n">example</span> <span class="o">=</span> <span class="n">gitlab</span><span class="o">.</span><span class="n">DeployToken</span><span class="p">(</span><span class="s2">&quot;example&quot;</span><span class="p">,</span>
    <span class="n">group</span><span class="o">=</span><span class="s2">&quot;example/deploying&quot;</span><span class="p">,</span>
    <span class="n">scopes</span><span class="o">=</span><span class="p">[</span><span class="s2">&quot;read_repository&quot;</span><span class="p">])</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>group</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name or id of the group to add the deploy token to.
Either <code class="docutils literal notranslate"><span class="pre">project</span></code> or <code class="docutils literal notranslate"><span class="pre">group</span></code> must be set.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A name to describe the deploy token with.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name or id of the project to add the deploy token to.
Either <code class="docutils literal notranslate"><span class="pre">project</span></code> or <code class="docutils literal notranslate"><span class="pre">group</span></code> must be set.</p></li>
<li><p><strong>scopes</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – Valid values: <code class="docutils literal notranslate"><span class="pre">read_repository</span></code>, <code class="docutils literal notranslate"><span class="pre">read_registry</span></code>.</p></li>
<li><p><strong>username</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A username for the deploy token. Default is <code class="docutils literal notranslate"><span class="pre">gitlab+deploy-token-{n}</span></code>.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_gitlab.DeployToken.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">expires_at</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">group</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">scopes</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">token</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">username</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_gitlab.deploy_token.DeployToken<a class="headerlink" href="#pulumi_gitlab.DeployToken.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing DeployToken resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>group</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name or id of the group to add the deploy token to.
Either <code class="docutils literal notranslate"><span class="pre">project</span></code> or <code class="docutils literal notranslate"><span class="pre">group</span></code> must be set.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A name to describe the deploy token with.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name or id of the project to add the deploy token to.
Either <code class="docutils literal notranslate"><span class="pre">project</span></code> or <code class="docutils literal notranslate"><span class="pre">group</span></code> must be set.</p></li>
<li><p><strong>scopes</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – Valid values: <code class="docutils literal notranslate"><span class="pre">read_repository</span></code>, <code class="docutils literal notranslate"><span class="pre">read_registry</span></code>.</p></li>
<li><p><strong>token</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The secret token. This is only populated when creating a new deploy token.</p></li>
<li><p><strong>username</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A username for the deploy token. Default is <code class="docutils literal notranslate"><span class="pre">gitlab+deploy-token-{n}</span></code>.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.DeployToken.group">
<em class="property">property </em><code class="sig-name descname">group</code><a class="headerlink" href="#pulumi_gitlab.DeployToken.group" title="Permalink to this definition">¶</a></dt>
<dd><p>The name or id of the group to add the deploy token to.
Either <code class="docutils literal notranslate"><span class="pre">project</span></code> or <code class="docutils literal notranslate"><span class="pre">group</span></code> must be set.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.DeployToken.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_gitlab.DeployToken.name" title="Permalink to this definition">¶</a></dt>
<dd><p>A name to describe the deploy token with.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.DeployToken.project">
<em class="property">property </em><code class="sig-name descname">project</code><a class="headerlink" href="#pulumi_gitlab.DeployToken.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The name or id of the project to add the deploy token to.
Either <code class="docutils literal notranslate"><span class="pre">project</span></code> or <code class="docutils literal notranslate"><span class="pre">group</span></code> must be set.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.DeployToken.scopes">
<em class="property">property </em><code class="sig-name descname">scopes</code><a class="headerlink" href="#pulumi_gitlab.DeployToken.scopes" title="Permalink to this definition">¶</a></dt>
<dd><p>Valid values: <code class="docutils literal notranslate"><span class="pre">read_repository</span></code>, <code class="docutils literal notranslate"><span class="pre">read_registry</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.DeployToken.token">
<em class="property">property </em><code class="sig-name descname">token</code><a class="headerlink" href="#pulumi_gitlab.DeployToken.token" title="Permalink to this definition">¶</a></dt>
<dd><p>The secret token. This is only populated when creating a new deploy token.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.DeployToken.username">
<em class="property">property </em><code class="sig-name descname">username</code><a class="headerlink" href="#pulumi_gitlab.DeployToken.username" title="Permalink to this definition">¶</a></dt>
<dd><p>A username for the deploy token. Default is <code class="docutils literal notranslate"><span class="pre">gitlab+deploy-token-{n}</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.DeployToken.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gitlab.DeployToken.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gitlab.DeployToken.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gitlab.DeployToken.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gitlab.GetGroupMembershipResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gitlab.</code><code class="sig-name descname">GetGroupMembershipResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">access_level</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">full_path</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">group_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">members</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gitlab.GetGroupMembershipResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getGroupMembership.</p>
<dl class="py method">
<dt id="pulumi_gitlab.GetGroupMembershipResult.access_level">
<em class="property">property </em><code class="sig-name descname">access_level</code><a class="headerlink" href="#pulumi_gitlab.GetGroupMembershipResult.access_level" title="Permalink to this definition">¶</a></dt>
<dd><p>One of five levels of access to the group.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.GetGroupMembershipResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_gitlab.GetGroupMembershipResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.GetGroupMembershipResult.members">
<em class="property">property </em><code class="sig-name descname">members</code><a class="headerlink" href="#pulumi_gitlab.GetGroupMembershipResult.members" title="Permalink to this definition">¶</a></dt>
<dd><p>The list of group members.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_gitlab.GetGroupResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gitlab.</code><code class="sig-name descname">GetGroupResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">full_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">full_path</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">group_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">lfs_enabled</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">parent_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">path</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">request_access_enabled</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">runners_token</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">visibility_level</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">web_url</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gitlab.GetGroupResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getGroup.</p>
<dl class="py method">
<dt id="pulumi_gitlab.GetGroupResult.description">
<em class="property">property </em><code class="sig-name descname">description</code><a class="headerlink" href="#pulumi_gitlab.GetGroupResult.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description of the group.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.GetGroupResult.full_name">
<em class="property">property </em><code class="sig-name descname">full_name</code><a class="headerlink" href="#pulumi_gitlab.GetGroupResult.full_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The full name of the group.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.GetGroupResult.full_path">
<em class="property">property </em><code class="sig-name descname">full_path</code><a class="headerlink" href="#pulumi_gitlab.GetGroupResult.full_path" title="Permalink to this definition">¶</a></dt>
<dd><p>The full path of the group.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.GetGroupResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_gitlab.GetGroupResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.GetGroupResult.lfs_enabled">
<em class="property">property </em><code class="sig-name descname">lfs_enabled</code><a class="headerlink" href="#pulumi_gitlab.GetGroupResult.lfs_enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean, is LFS enabled for projects in this group.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.GetGroupResult.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_gitlab.GetGroupResult.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of this group.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.GetGroupResult.parent_id">
<em class="property">property </em><code class="sig-name descname">parent_id</code><a class="headerlink" href="#pulumi_gitlab.GetGroupResult.parent_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Integer, ID of the parent group.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.GetGroupResult.path">
<em class="property">property </em><code class="sig-name descname">path</code><a class="headerlink" href="#pulumi_gitlab.GetGroupResult.path" title="Permalink to this definition">¶</a></dt>
<dd><p>The path of the group.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.GetGroupResult.request_access_enabled">
<em class="property">property </em><code class="sig-name descname">request_access_enabled</code><a class="headerlink" href="#pulumi_gitlab.GetGroupResult.request_access_enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean, is request for access enabled to the group.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.GetGroupResult.runners_token">
<em class="property">property </em><code class="sig-name descname">runners_token</code><a class="headerlink" href="#pulumi_gitlab.GetGroupResult.runners_token" title="Permalink to this definition">¶</a></dt>
<dd><p>The group level registration token to use during runner setup.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.GetGroupResult.visibility_level">
<em class="property">property </em><code class="sig-name descname">visibility_level</code><a class="headerlink" href="#pulumi_gitlab.GetGroupResult.visibility_level" title="Permalink to this definition">¶</a></dt>
<dd><p>Visibility level of the group. Possible values are <code class="docutils literal notranslate"><span class="pre">private</span></code>, <code class="docutils literal notranslate"><span class="pre">internal</span></code>, <code class="docutils literal notranslate"><span class="pre">public</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.GetGroupResult.web_url">
<em class="property">property </em><code class="sig-name descname">web_url</code><a class="headerlink" href="#pulumi_gitlab.GetGroupResult.web_url" title="Permalink to this definition">¶</a></dt>
<dd><p>Web URL of the group.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_gitlab.GetProjectResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gitlab.</code><code class="sig-name descname">GetProjectResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">archived</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">default_branch</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">http_url_to_repo</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">issues_enabled</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">lfs_enabled</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">merge_requests_enabled</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">namespace_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">path</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">path_with_namespace</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">pipelines_enabled</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">push_rules</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">remove_source_branch_after_merge</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">request_access_enabled</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">runners_token</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">snippets_enabled</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ssh_url_to_repo</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">visibility_level</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">web_url</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">wiki_enabled</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gitlab.GetProjectResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getProject.</p>
<dl class="py method">
<dt id="pulumi_gitlab.GetProjectResult.archived">
<em class="property">property </em><code class="sig-name descname">archived</code><a class="headerlink" href="#pulumi_gitlab.GetProjectResult.archived" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the project is in read-only mode (archived).</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.GetProjectResult.default_branch">
<em class="property">property </em><code class="sig-name descname">default_branch</code><a class="headerlink" href="#pulumi_gitlab.GetProjectResult.default_branch" title="Permalink to this definition">¶</a></dt>
<dd><p>The default branch for the project.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.GetProjectResult.description">
<em class="property">property </em><code class="sig-name descname">description</code><a class="headerlink" href="#pulumi_gitlab.GetProjectResult.description" title="Permalink to this definition">¶</a></dt>
<dd><p>A description of the project.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.GetProjectResult.http_url_to_repo">
<em class="property">property </em><code class="sig-name descname">http_url_to_repo</code><a class="headerlink" href="#pulumi_gitlab.GetProjectResult.http_url_to_repo" title="Permalink to this definition">¶</a></dt>
<dd><p>URL that can be provided to <code class="docutils literal notranslate"><span class="pre">git</span> <span class="pre">clone</span></code> to clone the
repository via HTTP.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.GetProjectResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_gitlab.GetProjectResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>Integer that uniquely identifies the project within the gitlab install.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.GetProjectResult.issues_enabled">
<em class="property">property </em><code class="sig-name descname">issues_enabled</code><a class="headerlink" href="#pulumi_gitlab.GetProjectResult.issues_enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Enable issue tracking for the project.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.GetProjectResult.lfs_enabled">
<em class="property">property </em><code class="sig-name descname">lfs_enabled</code><a class="headerlink" href="#pulumi_gitlab.GetProjectResult.lfs_enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Enable LFS for the project.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.GetProjectResult.merge_requests_enabled">
<em class="property">property </em><code class="sig-name descname">merge_requests_enabled</code><a class="headerlink" href="#pulumi_gitlab.GetProjectResult.merge_requests_enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Enable merge requests for the project.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.GetProjectResult.namespace_id">
<em class="property">property </em><code class="sig-name descname">namespace_id</code><a class="headerlink" href="#pulumi_gitlab.GetProjectResult.namespace_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The namespace (group or user) of the project. Defaults to your user.
See <code class="docutils literal notranslate"><span class="pre">Group</span></code> for an example.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.GetProjectResult.path">
<em class="property">property </em><code class="sig-name descname">path</code><a class="headerlink" href="#pulumi_gitlab.GetProjectResult.path" title="Permalink to this definition">¶</a></dt>
<dd><p>The path of the repository.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.GetProjectResult.path_with_namespace">
<em class="property">property </em><code class="sig-name descname">path_with_namespace</code><a class="headerlink" href="#pulumi_gitlab.GetProjectResult.path_with_namespace" title="Permalink to this definition">¶</a></dt>
<dd><p>The path of the repository with namespace.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.GetProjectResult.pipelines_enabled">
<em class="property">property </em><code class="sig-name descname">pipelines_enabled</code><a class="headerlink" href="#pulumi_gitlab.GetProjectResult.pipelines_enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Enable pipelines for the project.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.GetProjectResult.remove_source_branch_after_merge">
<em class="property">property </em><code class="sig-name descname">remove_source_branch_after_merge</code><a class="headerlink" href="#pulumi_gitlab.GetProjectResult.remove_source_branch_after_merge" title="Permalink to this definition">¶</a></dt>
<dd><p>Enable <code class="docutils literal notranslate"><span class="pre">Delete</span> <span class="pre">source</span> <span class="pre">branch</span></code> option by default for all new merge requests</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.GetProjectResult.request_access_enabled">
<em class="property">property </em><code class="sig-name descname">request_access_enabled</code><a class="headerlink" href="#pulumi_gitlab.GetProjectResult.request_access_enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Allow users to request member access.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.GetProjectResult.runners_token">
<em class="property">property </em><code class="sig-name descname">runners_token</code><a class="headerlink" href="#pulumi_gitlab.GetProjectResult.runners_token" title="Permalink to this definition">¶</a></dt>
<dd><p>Registration token to use during runner setup.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.GetProjectResult.snippets_enabled">
<em class="property">property </em><code class="sig-name descname">snippets_enabled</code><a class="headerlink" href="#pulumi_gitlab.GetProjectResult.snippets_enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Enable snippets for the project.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.GetProjectResult.ssh_url_to_repo">
<em class="property">property </em><code class="sig-name descname">ssh_url_to_repo</code><a class="headerlink" href="#pulumi_gitlab.GetProjectResult.ssh_url_to_repo" title="Permalink to this definition">¶</a></dt>
<dd><p>URL that can be provided to <code class="docutils literal notranslate"><span class="pre">git</span> <span class="pre">clone</span></code> to clone the
repository via SSH.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.GetProjectResult.visibility_level">
<em class="property">property </em><code class="sig-name descname">visibility_level</code><a class="headerlink" href="#pulumi_gitlab.GetProjectResult.visibility_level" title="Permalink to this definition">¶</a></dt>
<dd><p>Repositories are created as private by default.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.GetProjectResult.web_url">
<em class="property">property </em><code class="sig-name descname">web_url</code><a class="headerlink" href="#pulumi_gitlab.GetProjectResult.web_url" title="Permalink to this definition">¶</a></dt>
<dd><p>URL that can be used to find the project in a browser.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.GetProjectResult.wiki_enabled">
<em class="property">property </em><code class="sig-name descname">wiki_enabled</code><a class="headerlink" href="#pulumi_gitlab.GetProjectResult.wiki_enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Enable wiki for the project.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_gitlab.GetProjectsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gitlab.</code><code class="sig-name descname">GetProjectsResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">archived</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">group_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">include_subgroups</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">max_queryable_pages</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">membership</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">min_access_level</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">order_by</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">owned</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">page</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">per_page</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">projects</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">search</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">simple</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sort</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">starred</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">statistics</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">visibility</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">with_custom_attributes</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">with_issues_enabled</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">with_merge_requests_enabled</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">with_programming_language</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">with_shared</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gitlab.GetProjectsResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getProjects.</p>
<dl class="py method">
<dt id="pulumi_gitlab.GetProjectsResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_gitlab.GetProjectsResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.GetProjectsResult.projects">
<em class="property">property </em><code class="sig-name descname">projects</code><a class="headerlink" href="#pulumi_gitlab.GetProjectsResult.projects" title="Permalink to this definition">¶</a></dt>
<dd><p>A list containing the projects matching the supplied arguments</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.GetProjectsResult.visibility">
<em class="property">property </em><code class="sig-name descname">visibility</code><a class="headerlink" href="#pulumi_gitlab.GetProjectsResult.visibility" title="Permalink to this definition">¶</a></dt>
<dd><p>The visibility of the project.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_gitlab.GetUserResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gitlab.</code><code class="sig-name descname">GetUserResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">avatar_url</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">bio</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">can_create_group</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">can_create_project</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">color_scheme_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">created_at</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">current_sign_in_at</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">email</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">extern_uid</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">external</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">is_admin</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">last_sign_in_at</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">linkedin</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">location</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">organization</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">projects_limit</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">skype</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">state</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">theme_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">twitter</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">two_factor_enabled</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_provider</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">username</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">website_url</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gitlab.GetUserResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getUser.</p>
<dl class="py method">
<dt id="pulumi_gitlab.GetUserResult.avatar_url">
<em class="property">property </em><code class="sig-name descname">avatar_url</code><a class="headerlink" href="#pulumi_gitlab.GetUserResult.avatar_url" title="Permalink to this definition">¶</a></dt>
<dd><p>The avatar URL of the user.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.GetUserResult.bio">
<em class="property">property </em><code class="sig-name descname">bio</code><a class="headerlink" href="#pulumi_gitlab.GetUserResult.bio" title="Permalink to this definition">¶</a></dt>
<dd><p>The bio of the user.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.GetUserResult.can_create_group">
<em class="property">property </em><code class="sig-name descname">can_create_group</code><a class="headerlink" href="#pulumi_gitlab.GetUserResult.can_create_group" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the user can create groups.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.GetUserResult.can_create_project">
<em class="property">property </em><code class="sig-name descname">can_create_project</code><a class="headerlink" href="#pulumi_gitlab.GetUserResult.can_create_project" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the user can create projects.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.GetUserResult.color_scheme_id">
<em class="property">property </em><code class="sig-name descname">color_scheme_id</code><a class="headerlink" href="#pulumi_gitlab.GetUserResult.color_scheme_id" title="Permalink to this definition">¶</a></dt>
<dd><p>User’s color scheme ID.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.GetUserResult.created_at">
<em class="property">property </em><code class="sig-name descname">created_at</code><a class="headerlink" href="#pulumi_gitlab.GetUserResult.created_at" title="Permalink to this definition">¶</a></dt>
<dd><p>Date the user was created at.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.GetUserResult.current_sign_in_at">
<em class="property">property </em><code class="sig-name descname">current_sign_in_at</code><a class="headerlink" href="#pulumi_gitlab.GetUserResult.current_sign_in_at" title="Permalink to this definition">¶</a></dt>
<dd><p>Current user’s sign-in date.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.GetUserResult.email">
<em class="property">property </em><code class="sig-name descname">email</code><a class="headerlink" href="#pulumi_gitlab.GetUserResult.email" title="Permalink to this definition">¶</a></dt>
<dd><p>The e-mail address of the user.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.GetUserResult.extern_uid">
<em class="property">property </em><code class="sig-name descname">extern_uid</code><a class="headerlink" href="#pulumi_gitlab.GetUserResult.extern_uid" title="Permalink to this definition">¶</a></dt>
<dd><p>The external UID of the user.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.GetUserResult.external">
<em class="property">property </em><code class="sig-name descname">external</code><a class="headerlink" href="#pulumi_gitlab.GetUserResult.external" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the user is external.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.GetUserResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_gitlab.GetUserResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.GetUserResult.is_admin">
<em class="property">property </em><code class="sig-name descname">is_admin</code><a class="headerlink" href="#pulumi_gitlab.GetUserResult.is_admin" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the user is an admin.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.GetUserResult.last_sign_in_at">
<em class="property">property </em><code class="sig-name descname">last_sign_in_at</code><a class="headerlink" href="#pulumi_gitlab.GetUserResult.last_sign_in_at" title="Permalink to this definition">¶</a></dt>
<dd><p>Last user’s sign-in date.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.GetUserResult.linkedin">
<em class="property">property </em><code class="sig-name descname">linkedin</code><a class="headerlink" href="#pulumi_gitlab.GetUserResult.linkedin" title="Permalink to this definition">¶</a></dt>
<dd><p>Linkedin profile of the user.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.GetUserResult.location">
<em class="property">property </em><code class="sig-name descname">location</code><a class="headerlink" href="#pulumi_gitlab.GetUserResult.location" title="Permalink to this definition">¶</a></dt>
<dd><p>The location of the user.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.GetUserResult.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_gitlab.GetUserResult.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the user.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.GetUserResult.organization">
<em class="property">property </em><code class="sig-name descname">organization</code><a class="headerlink" href="#pulumi_gitlab.GetUserResult.organization" title="Permalink to this definition">¶</a></dt>
<dd><p>The organization of the user.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.GetUserResult.projects_limit">
<em class="property">property </em><code class="sig-name descname">projects_limit</code><a class="headerlink" href="#pulumi_gitlab.GetUserResult.projects_limit" title="Permalink to this definition">¶</a></dt>
<dd><p>Number of projects the user can create.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.GetUserResult.skype">
<em class="property">property </em><code class="sig-name descname">skype</code><a class="headerlink" href="#pulumi_gitlab.GetUserResult.skype" title="Permalink to this definition">¶</a></dt>
<dd><p>Skype username of the user.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.GetUserResult.state">
<em class="property">property </em><code class="sig-name descname">state</code><a class="headerlink" href="#pulumi_gitlab.GetUserResult.state" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the user is active or blocked.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.GetUserResult.theme_id">
<em class="property">property </em><code class="sig-name descname">theme_id</code><a class="headerlink" href="#pulumi_gitlab.GetUserResult.theme_id" title="Permalink to this definition">¶</a></dt>
<dd><p>User’s theme ID.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.GetUserResult.twitter">
<em class="property">property </em><code class="sig-name descname">twitter</code><a class="headerlink" href="#pulumi_gitlab.GetUserResult.twitter" title="Permalink to this definition">¶</a></dt>
<dd><p>Twitter username of the user.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.GetUserResult.two_factor_enabled">
<em class="property">property </em><code class="sig-name descname">two_factor_enabled</code><a class="headerlink" href="#pulumi_gitlab.GetUserResult.two_factor_enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether user’s two factor auth is enabled.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.GetUserResult.user_provider">
<em class="property">property </em><code class="sig-name descname">user_provider</code><a class="headerlink" href="#pulumi_gitlab.GetUserResult.user_provider" title="Permalink to this definition">¶</a></dt>
<dd><p>The UID provider of the user.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.GetUserResult.username">
<em class="property">property </em><code class="sig-name descname">username</code><a class="headerlink" href="#pulumi_gitlab.GetUserResult.username" title="Permalink to this definition">¶</a></dt>
<dd><p>The username of the user.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.GetUserResult.website_url">
<em class="property">property </em><code class="sig-name descname">website_url</code><a class="headerlink" href="#pulumi_gitlab.GetUserResult.website_url" title="Permalink to this definition">¶</a></dt>
<dd><p>User’s website URL.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_gitlab.GetUsersResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gitlab.</code><code class="sig-name descname">GetUsersResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">active</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">blocked</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">created_after</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">created_before</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">extern_provider</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">extern_uid</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">order_by</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">search</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sort</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">users</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gitlab.GetUsersResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getUsers.</p>
<dl class="py method">
<dt id="pulumi_gitlab.GetUsersResult.extern_uid">
<em class="property">property </em><code class="sig-name descname">extern_uid</code><a class="headerlink" href="#pulumi_gitlab.GetUsersResult.extern_uid" title="Permalink to this definition">¶</a></dt>
<dd><p>The external UID of the user.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.GetUsersResult.id">
<em class="property">property </em><code class="sig-name descname">id</code><a class="headerlink" href="#pulumi_gitlab.GetUsersResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.GetUsersResult.users">
<em class="property">property </em><code class="sig-name descname">users</code><a class="headerlink" href="#pulumi_gitlab.GetUsersResult.users" title="Permalink to this definition">¶</a></dt>
<dd><p>The list of users.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_gitlab.Group">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gitlab.</code><code class="sig-name descname">Group</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auto_devops_enabled</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">emails_disabled</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">lfs_enabled</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">mentions_disabled</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">parent_id</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">path</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_creation_level</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">request_access_enabled</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">require_two_factor_authentication</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">share_with_group_lock</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">subgroup_creation_level</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">two_factor_grace_period</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">visibility_level</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gitlab.Group" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a Group resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[bool] auto_devops_enabled: Boolean, defaults to false.  Default to Auto</p>
<blockquote>
<div><p>DevOps pipeline for all projects within this group.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the group.</p></li>
<li><p><strong>emails_disabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean, defaults to false.  Disable email notifications</p></li>
<li><p><strong>lfs_enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean, defaults to true.  Whether to enable LFS
support for projects in this group.</p></li>
<li><p><strong>mentions_disabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean, defaults to false.  Disable the capability
of a group from getting mentioned</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of this group.</p></li>
<li><p><strong>parent_id</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Integer, id of the parent group (creates a nested group).</p></li>
<li><p><strong>path</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The path of the group.</p></li>
<li><p><strong>project_creation_level</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – , defaults to Maintainer.
Determine if developers can create projects
in the group. Can be noone (No one), maintainer (Maintainers),
or developer (Developers + Maintainers).</p></li>
<li><p><strong>request_access_enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean, defaults to false.  Whether to
enable users to request access to the group.</p></li>
<li><p><strong>require_two_factor_authentication</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean, defaults to false.
equire all users in this group to setup Two-factor authentication.</p></li>
<li><p><strong>share_with_group_lock</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean, defaults to false.  Prevent sharing
a project with another group within this group.</p></li>
<li><p><strong>subgroup_creation_level</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – , defaults to Owner.
Allowed to create subgroups.
Can be owner (Owners), or maintainer (Maintainers).</p></li>
<li><p><strong>two_factor_grace_period</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Int, defaults to 48.
Time before Two-factor authentication is enforced (in hours).</p></li>
<li><p><strong>visibility_level</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The group’s visibility. Can be <code class="docutils literal notranslate"><span class="pre">private</span></code>, <code class="docutils literal notranslate"><span class="pre">internal</span></code>, or <code class="docutils literal notranslate"><span class="pre">public</span></code>.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_gitlab.Group.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auto_devops_enabled</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">emails_disabled</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">full_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">full_path</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">lfs_enabled</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">mentions_disabled</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">parent_id</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">path</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_creation_level</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">request_access_enabled</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">require_two_factor_authentication</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">runners_token</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">share_with_group_lock</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">subgroup_creation_level</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">two_factor_grace_period</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">visibility_level</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">web_url</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_gitlab.group.Group<a class="headerlink" href="#pulumi_gitlab.Group.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Group resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>auto_devops_enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean, defaults to false.  Default to Auto
DevOps pipeline for all projects within this group.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the group.</p></li>
<li><p><strong>emails_disabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean, defaults to false.  Disable email notifications</p></li>
<li><p><strong>full_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The full name of the group.</p></li>
<li><p><strong>full_path</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The full path of the group.</p></li>
<li><p><strong>lfs_enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean, defaults to true.  Whether to enable LFS
support for projects in this group.</p></li>
<li><p><strong>mentions_disabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean, defaults to false.  Disable the capability
of a group from getting mentioned</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of this group.</p></li>
<li><p><strong>parent_id</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Integer, id of the parent group (creates a nested group).</p></li>
<li><p><strong>path</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The path of the group.</p></li>
<li><p><strong>project_creation_level</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – , defaults to Maintainer.
Determine if developers can create projects
in the group. Can be noone (No one), maintainer (Maintainers),
or developer (Developers + Maintainers).</p></li>
<li><p><strong>request_access_enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean, defaults to false.  Whether to
enable users to request access to the group.</p></li>
<li><p><strong>require_two_factor_authentication</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean, defaults to false.
equire all users in this group to setup Two-factor authentication.</p></li>
<li><p><strong>runners_token</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The group level registration token to use during runner setup.</p></li>
<li><p><strong>share_with_group_lock</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean, defaults to false.  Prevent sharing
a project with another group within this group.</p></li>
<li><p><strong>subgroup_creation_level</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – , defaults to Owner.
Allowed to create subgroups.
Can be owner (Owners), or maintainer (Maintainers).</p></li>
<li><p><strong>two_factor_grace_period</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Int, defaults to 48.
Time before Two-factor authentication is enforced (in hours).</p></li>
<li><p><strong>visibility_level</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The group’s visibility. Can be <code class="docutils literal notranslate"><span class="pre">private</span></code>, <code class="docutils literal notranslate"><span class="pre">internal</span></code>, or <code class="docutils literal notranslate"><span class="pre">public</span></code>.</p></li>
<li><p><strong>web_url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Web URL of the group.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.Group.auto_devops_enabled">
<em class="property">property </em><code class="sig-name descname">auto_devops_enabled</code><a class="headerlink" href="#pulumi_gitlab.Group.auto_devops_enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean, defaults to false.  Default to Auto
DevOps pipeline for all projects within this group.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.Group.description">
<em class="property">property </em><code class="sig-name descname">description</code><a class="headerlink" href="#pulumi_gitlab.Group.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description of the group.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.Group.emails_disabled">
<em class="property">property </em><code class="sig-name descname">emails_disabled</code><a class="headerlink" href="#pulumi_gitlab.Group.emails_disabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean, defaults to false.  Disable email notifications</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.Group.full_name">
<em class="property">property </em><code class="sig-name descname">full_name</code><a class="headerlink" href="#pulumi_gitlab.Group.full_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The full name of the group.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.Group.full_path">
<em class="property">property </em><code class="sig-name descname">full_path</code><a class="headerlink" href="#pulumi_gitlab.Group.full_path" title="Permalink to this definition">¶</a></dt>
<dd><p>The full path of the group.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.Group.lfs_enabled">
<em class="property">property </em><code class="sig-name descname">lfs_enabled</code><a class="headerlink" href="#pulumi_gitlab.Group.lfs_enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean, defaults to true.  Whether to enable LFS
support for projects in this group.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.Group.mentions_disabled">
<em class="property">property </em><code class="sig-name descname">mentions_disabled</code><a class="headerlink" href="#pulumi_gitlab.Group.mentions_disabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean, defaults to false.  Disable the capability
of a group from getting mentioned</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.Group.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_gitlab.Group.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of this group.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.Group.parent_id">
<em class="property">property </em><code class="sig-name descname">parent_id</code><a class="headerlink" href="#pulumi_gitlab.Group.parent_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Integer, id of the parent group (creates a nested group).</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.Group.path">
<em class="property">property </em><code class="sig-name descname">path</code><a class="headerlink" href="#pulumi_gitlab.Group.path" title="Permalink to this definition">¶</a></dt>
<dd><p>The path of the group.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.Group.project_creation_level">
<em class="property">property </em><code class="sig-name descname">project_creation_level</code><a class="headerlink" href="#pulumi_gitlab.Group.project_creation_level" title="Permalink to this definition">¶</a></dt>
<dd><p>, defaults to Maintainer.
Determine if developers can create projects
in the group. Can be noone (No one), maintainer (Maintainers),
or developer (Developers + Maintainers).</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.Group.request_access_enabled">
<em class="property">property </em><code class="sig-name descname">request_access_enabled</code><a class="headerlink" href="#pulumi_gitlab.Group.request_access_enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean, defaults to false.  Whether to
enable users to request access to the group.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.Group.require_two_factor_authentication">
<em class="property">property </em><code class="sig-name descname">require_two_factor_authentication</code><a class="headerlink" href="#pulumi_gitlab.Group.require_two_factor_authentication" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean, defaults to false.
equire all users in this group to setup Two-factor authentication.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.Group.runners_token">
<em class="property">property </em><code class="sig-name descname">runners_token</code><a class="headerlink" href="#pulumi_gitlab.Group.runners_token" title="Permalink to this definition">¶</a></dt>
<dd><p>The group level registration token to use during runner setup.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.Group.share_with_group_lock">
<em class="property">property </em><code class="sig-name descname">share_with_group_lock</code><a class="headerlink" href="#pulumi_gitlab.Group.share_with_group_lock" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean, defaults to false.  Prevent sharing
a project with another group within this group.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.Group.subgroup_creation_level">
<em class="property">property </em><code class="sig-name descname">subgroup_creation_level</code><a class="headerlink" href="#pulumi_gitlab.Group.subgroup_creation_level" title="Permalink to this definition">¶</a></dt>
<dd><p>, defaults to Owner.
Allowed to create subgroups.
Can be owner (Owners), or maintainer (Maintainers).</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.Group.two_factor_grace_period">
<em class="property">property </em><code class="sig-name descname">two_factor_grace_period</code><a class="headerlink" href="#pulumi_gitlab.Group.two_factor_grace_period" title="Permalink to this definition">¶</a></dt>
<dd><p>Int, defaults to 48.
Time before Two-factor authentication is enforced (in hours).</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.Group.visibility_level">
<em class="property">property </em><code class="sig-name descname">visibility_level</code><a class="headerlink" href="#pulumi_gitlab.Group.visibility_level" title="Permalink to this definition">¶</a></dt>
<dd><p>The group’s visibility. Can be <code class="docutils literal notranslate"><span class="pre">private</span></code>, <code class="docutils literal notranslate"><span class="pre">internal</span></code>, or <code class="docutils literal notranslate"><span class="pre">public</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.Group.web_url">
<em class="property">property </em><code class="sig-name descname">web_url</code><a class="headerlink" href="#pulumi_gitlab.Group.web_url" title="Permalink to this definition">¶</a></dt>
<dd><p>Web URL of the group.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.Group.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gitlab.Group.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gitlab.Group.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gitlab.Group.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gitlab.GroupCluster">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gitlab.</code><code class="sig-name descname">GroupCluster</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">domain</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">environment_scope</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">group</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kubernetes_api_url</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kubernetes_authorization_type</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kubernetes_ca_cert</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kubernetes_token</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">managed</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">management_project_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gitlab.GroupCluster" title="Permalink to this definition">¶</a></dt>
<dd><p>This resource allows you to create and manage group clusters for your GitLab groups.
For further information on clusters, consult the <a class="reference external" href="https://docs.gitlab.com/ce/user/group/clusters/index.html">gitlab
documentation</a>.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_gitlab</span> <span class="k">as</span> <span class="nn">gitlab</span>

<span class="n">foo</span> <span class="o">=</span> <span class="n">gitlab</span><span class="o">.</span><span class="n">Group</span><span class="p">(</span><span class="s2">&quot;foo&quot;</span><span class="p">,</span> <span class="n">path</span><span class="o">=</span><span class="s2">&quot;foo-path&quot;</span><span class="p">)</span>
<span class="n">bar</span> <span class="o">=</span> <span class="n">gitlab</span><span class="o">.</span><span class="n">GroupCluster</span><span class="p">(</span><span class="s2">&quot;bar&quot;</span><span class="p">,</span>
    <span class="n">domain</span><span class="o">=</span><span class="s2">&quot;example.com&quot;</span><span class="p">,</span>
    <span class="n">enabled</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="n">environment_scope</span><span class="o">=</span><span class="s2">&quot;*&quot;</span><span class="p">,</span>
    <span class="n">group</span><span class="o">=</span><span class="n">foo</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">kubernetes_api_url</span><span class="o">=</span><span class="s2">&quot;https://124.124.124&quot;</span><span class="p">,</span>
    <span class="n">kubernetes_authorization_type</span><span class="o">=</span><span class="s2">&quot;rbac&quot;</span><span class="p">,</span>
    <span class="n">kubernetes_ca_cert</span><span class="o">=</span><span class="s2">&quot;some-cert&quot;</span><span class="p">,</span>
    <span class="n">kubernetes_token</span><span class="o">=</span><span class="s2">&quot;some-token&quot;</span><span class="p">,</span>
    <span class="n">management_project_id</span><span class="o">=</span><span class="s2">&quot;123456&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>domain</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The base domain of the cluster.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Determines if cluster is active or not. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>. This attribute cannot be read.</p></li>
<li><p><strong>environment_scope</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The associated environment to the cluster. Defaults to <code class="docutils literal notranslate"><span class="pre">*</span></code>.</p></li>
<li><p><strong>group</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The id of the group to add the cluster to.</p></li>
<li><p><strong>kubernetes_api_url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The URL to access the Kubernetes API.</p></li>
<li><p><strong>kubernetes_authorization_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The cluster authorization type. Valid values are <code class="docutils literal notranslate"><span class="pre">rbac</span></code>, <code class="docutils literal notranslate"><span class="pre">abac</span></code>, <code class="docutils literal notranslate"><span class="pre">unknown_authorization</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">rbac</span></code>.</p></li>
<li><p><strong>kubernetes_ca_cert</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – TLS certificate (needed if API is using a self-signed TLS certificate).</p></li>
<li><p><strong>kubernetes_token</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The token to authenticate against Kubernetes.</p></li>
<li><p><strong>managed</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Determines if cluster is managed by gitlab or not. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>. This attribute cannot be read.</p></li>
<li><p><strong>management_project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the management project for the cluster.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of cluster.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_gitlab.GroupCluster.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cluster_type</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">created_at</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">domain</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">environment_scope</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">group</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kubernetes_api_url</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kubernetes_authorization_type</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kubernetes_ca_cert</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kubernetes_token</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">managed</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">management_project_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">platform_type</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">provider_type</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_gitlab.group_cluster.GroupCluster<a class="headerlink" href="#pulumi_gitlab.GroupCluster.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing GroupCluster resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>domain</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The base domain of the cluster.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Determines if cluster is active or not. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>. This attribute cannot be read.</p></li>
<li><p><strong>environment_scope</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The associated environment to the cluster. Defaults to <code class="docutils literal notranslate"><span class="pre">*</span></code>.</p></li>
<li><p><strong>group</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The id of the group to add the cluster to.</p></li>
<li><p><strong>kubernetes_api_url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The URL to access the Kubernetes API.</p></li>
<li><p><strong>kubernetes_authorization_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The cluster authorization type. Valid values are <code class="docutils literal notranslate"><span class="pre">rbac</span></code>, <code class="docutils literal notranslate"><span class="pre">abac</span></code>, <code class="docutils literal notranslate"><span class="pre">unknown_authorization</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">rbac</span></code>.</p></li>
<li><p><strong>kubernetes_ca_cert</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – TLS certificate (needed if API is using a self-signed TLS certificate).</p></li>
<li><p><strong>kubernetes_token</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The token to authenticate against Kubernetes.</p></li>
<li><p><strong>managed</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Determines if cluster is managed by gitlab or not. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>. This attribute cannot be read.</p></li>
<li><p><strong>management_project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the management project for the cluster.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of cluster.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.GroupCluster.domain">
<em class="property">property </em><code class="sig-name descname">domain</code><a class="headerlink" href="#pulumi_gitlab.GroupCluster.domain" title="Permalink to this definition">¶</a></dt>
<dd><p>The base domain of the cluster.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.GroupCluster.enabled">
<em class="property">property </em><code class="sig-name descname">enabled</code><a class="headerlink" href="#pulumi_gitlab.GroupCluster.enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Determines if cluster is active or not. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>. This attribute cannot be read.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.GroupCluster.environment_scope">
<em class="property">property </em><code class="sig-name descname">environment_scope</code><a class="headerlink" href="#pulumi_gitlab.GroupCluster.environment_scope" title="Permalink to this definition">¶</a></dt>
<dd><p>The associated environment to the cluster. Defaults to <code class="docutils literal notranslate"><span class="pre">*</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.GroupCluster.group">
<em class="property">property </em><code class="sig-name descname">group</code><a class="headerlink" href="#pulumi_gitlab.GroupCluster.group" title="Permalink to this definition">¶</a></dt>
<dd><p>The id of the group to add the cluster to.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.GroupCluster.kubernetes_api_url">
<em class="property">property </em><code class="sig-name descname">kubernetes_api_url</code><a class="headerlink" href="#pulumi_gitlab.GroupCluster.kubernetes_api_url" title="Permalink to this definition">¶</a></dt>
<dd><p>The URL to access the Kubernetes API.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.GroupCluster.kubernetes_authorization_type">
<em class="property">property </em><code class="sig-name descname">kubernetes_authorization_type</code><a class="headerlink" href="#pulumi_gitlab.GroupCluster.kubernetes_authorization_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The cluster authorization type. Valid values are <code class="docutils literal notranslate"><span class="pre">rbac</span></code>, <code class="docutils literal notranslate"><span class="pre">abac</span></code>, <code class="docutils literal notranslate"><span class="pre">unknown_authorization</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">rbac</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.GroupCluster.kubernetes_ca_cert">
<em class="property">property </em><code class="sig-name descname">kubernetes_ca_cert</code><a class="headerlink" href="#pulumi_gitlab.GroupCluster.kubernetes_ca_cert" title="Permalink to this definition">¶</a></dt>
<dd><p>TLS certificate (needed if API is using a self-signed TLS certificate).</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.GroupCluster.kubernetes_token">
<em class="property">property </em><code class="sig-name descname">kubernetes_token</code><a class="headerlink" href="#pulumi_gitlab.GroupCluster.kubernetes_token" title="Permalink to this definition">¶</a></dt>
<dd><p>The token to authenticate against Kubernetes.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.GroupCluster.managed">
<em class="property">property </em><code class="sig-name descname">managed</code><a class="headerlink" href="#pulumi_gitlab.GroupCluster.managed" title="Permalink to this definition">¶</a></dt>
<dd><p>Determines if cluster is managed by gitlab or not. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>. This attribute cannot be read.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.GroupCluster.management_project_id">
<em class="property">property </em><code class="sig-name descname">management_project_id</code><a class="headerlink" href="#pulumi_gitlab.GroupCluster.management_project_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the management project for the cluster.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.GroupCluster.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_gitlab.GroupCluster.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of cluster.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.GroupCluster.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gitlab.GroupCluster.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gitlab.GroupCluster.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gitlab.GroupCluster.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gitlab.GroupLabel">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gitlab.</code><code class="sig-name descname">GroupLabel</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">color</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">group</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gitlab.GroupLabel" title="Permalink to this definition">¶</a></dt>
<dd><p>This resource allows you to create and manage labels for your GitLab groups.
For further information on labels, consult the <a class="reference external" href="https://docs.gitlab.com/ee/user/project/labels.html#group-labels">gitlab
documentation</a>.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_gitlab</span> <span class="k">as</span> <span class="nn">gitlab</span>

<span class="n">fixme</span> <span class="o">=</span> <span class="n">gitlab</span><span class="o">.</span><span class="n">GroupLabel</span><span class="p">(</span><span class="s2">&quot;fixme&quot;</span><span class="p">,</span>
    <span class="n">color</span><span class="o">=</span><span class="s2">&quot;#ffcc00&quot;</span><span class="p">,</span>
    <span class="n">description</span><span class="o">=</span><span class="s2">&quot;issue with failing tests&quot;</span><span class="p">,</span>
    <span class="n">group</span><span class="o">=</span><span class="s2">&quot;example&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>color</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The color of the label given in 6-digit hex notation with leading ‘#’ sign (e.g. #FFAABB) or one of the <a class="reference external" href="https://developer.mozilla.org/en-US/docs/Web/CSS/color_value#Color_keywords">CSS color names</a>.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the label.</p></li>
<li><p><strong>group</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name or id of the group to add the label to.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the label.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_gitlab.GroupLabel.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">color</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">group</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_gitlab.group_label.GroupLabel<a class="headerlink" href="#pulumi_gitlab.GroupLabel.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing GroupLabel resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>color</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The color of the label given in 6-digit hex notation with leading ‘#’ sign (e.g. #FFAABB) or one of the <a class="reference external" href="https://developer.mozilla.org/en-US/docs/Web/CSS/color_value#Color_keywords">CSS color names</a>.</p>
</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the label.</p></li>
<li><p><strong>group</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name or id of the group to add the label to.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the label.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.GroupLabel.color">
<em class="property">property </em><code class="sig-name descname">color</code><a class="headerlink" href="#pulumi_gitlab.GroupLabel.color" title="Permalink to this definition">¶</a></dt>
<dd><p>The color of the label given in 6-digit hex notation with leading ‘#’ sign (e.g. #FFAABB) or one of the <a class="reference external" href="https://developer.mozilla.org/en-US/docs/Web/CSS/color_value#Color_keywords">CSS color names</a>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.GroupLabel.description">
<em class="property">property </em><code class="sig-name descname">description</code><a class="headerlink" href="#pulumi_gitlab.GroupLabel.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description of the label.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.GroupLabel.group">
<em class="property">property </em><code class="sig-name descname">group</code><a class="headerlink" href="#pulumi_gitlab.GroupLabel.group" title="Permalink to this definition">¶</a></dt>
<dd><p>The name or id of the group to add the label to.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.GroupLabel.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_gitlab.GroupLabel.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the label.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.GroupLabel.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gitlab.GroupLabel.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gitlab.GroupLabel.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gitlab.GroupLabel.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gitlab.GroupLdapLink">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gitlab.</code><code class="sig-name descname">GroupLdapLink</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">access_level</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cn</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">force</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">group_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ldap_provider</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gitlab.GroupLdapLink" title="Permalink to this definition">¶</a></dt>
<dd><p>This resource allows you to add an LDAP link to an existing GitLab group.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_gitlab</span> <span class="k">as</span> <span class="nn">gitlab</span>

<span class="n">test</span> <span class="o">=</span> <span class="n">gitlab</span><span class="o">.</span><span class="n">GroupLdapLink</span><span class="p">(</span><span class="s2">&quot;test&quot;</span><span class="p">,</span>
    <span class="n">access_level</span><span class="o">=</span><span class="s2">&quot;developer&quot;</span><span class="p">,</span>
    <span class="n">cn</span><span class="o">=</span><span class="s2">&quot;testuser&quot;</span><span class="p">,</span>
    <span class="n">group_id</span><span class="o">=</span><span class="s2">&quot;12345&quot;</span><span class="p">,</span>
    <span class="n">ldap_provider</span><span class="o">=</span><span class="s2">&quot;ldapmain&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>access_level</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Acceptable values are: guest, reporter, developer, maintainer, owner.</p></li>
<li><p><strong>cn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The CN of the LDAP group to link with.</p></li>
<li><p><strong>group_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The id of the GitLab group.</p></li>
<li><p><strong>ldap_provider</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the LDAP provider as stored in the GitLab database.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_gitlab.GroupLdapLink.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">access_level</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cn</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">force</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">group_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ldap_provider</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_gitlab.group_ldap_link.GroupLdapLink<a class="headerlink" href="#pulumi_gitlab.GroupLdapLink.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing GroupLdapLink resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>access_level</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Acceptable values are: guest, reporter, developer, maintainer, owner.</p></li>
<li><p><strong>cn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The CN of the LDAP group to link with.</p></li>
<li><p><strong>group_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The id of the GitLab group.</p></li>
<li><p><strong>ldap_provider</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the LDAP provider as stored in the GitLab database.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.GroupLdapLink.access_level">
<em class="property">property </em><code class="sig-name descname">access_level</code><a class="headerlink" href="#pulumi_gitlab.GroupLdapLink.access_level" title="Permalink to this definition">¶</a></dt>
<dd><p>Acceptable values are: guest, reporter, developer, maintainer, owner.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.GroupLdapLink.cn">
<em class="property">property </em><code class="sig-name descname">cn</code><a class="headerlink" href="#pulumi_gitlab.GroupLdapLink.cn" title="Permalink to this definition">¶</a></dt>
<dd><p>The CN of the LDAP group to link with.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.GroupLdapLink.group_id">
<em class="property">property </em><code class="sig-name descname">group_id</code><a class="headerlink" href="#pulumi_gitlab.GroupLdapLink.group_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The id of the GitLab group.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.GroupLdapLink.ldap_provider">
<em class="property">property </em><code class="sig-name descname">ldap_provider</code><a class="headerlink" href="#pulumi_gitlab.GroupLdapLink.ldap_provider" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the LDAP provider as stored in the GitLab database.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.GroupLdapLink.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gitlab.GroupLdapLink.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gitlab.GroupLdapLink.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gitlab.GroupLdapLink.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gitlab.GroupMembership">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gitlab.</code><code class="sig-name descname">GroupMembership</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">access_level</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">expires_at</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">group_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_id</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gitlab.GroupMembership" title="Permalink to this definition">¶</a></dt>
<dd><p>This resource allows you to add a user to an existing group.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_gitlab</span> <span class="k">as</span> <span class="nn">gitlab</span>

<span class="n">test</span> <span class="o">=</span> <span class="n">gitlab</span><span class="o">.</span><span class="n">GroupMembership</span><span class="p">(</span><span class="s2">&quot;test&quot;</span><span class="p">,</span>
    <span class="n">access_level</span><span class="o">=</span><span class="s2">&quot;guest&quot;</span><span class="p">,</span>
    <span class="n">expires_at</span><span class="o">=</span><span class="s2">&quot;2020-12-31&quot;</span><span class="p">,</span>
    <span class="n">group_id</span><span class="o">=</span><span class="s2">&quot;12345&quot;</span><span class="p">,</span>
    <span class="n">user_id</span><span class="o">=</span><span class="mi">1337</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>access_level</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Acceptable values are: guest, reporter, developer, maintainer, owner.</p></li>
<li><p><strong>expires_at</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Expiration date for the group membership. Format: <code class="docutils literal notranslate"><span class="pre">YYYY-MM-DD</span></code></p></li>
<li><p><strong>group_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The id of the group.</p></li>
<li><p><strong>user_id</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The id of the user.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_gitlab.GroupMembership.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">access_level</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">expires_at</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">group_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_id</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_gitlab.group_membership.GroupMembership<a class="headerlink" href="#pulumi_gitlab.GroupMembership.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing GroupMembership resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>access_level</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Acceptable values are: guest, reporter, developer, maintainer, owner.</p></li>
<li><p><strong>expires_at</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Expiration date for the group membership. Format: <code class="docutils literal notranslate"><span class="pre">YYYY-MM-DD</span></code></p></li>
<li><p><strong>group_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The id of the group.</p></li>
<li><p><strong>user_id</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The id of the user.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.GroupMembership.access_level">
<em class="property">property </em><code class="sig-name descname">access_level</code><a class="headerlink" href="#pulumi_gitlab.GroupMembership.access_level" title="Permalink to this definition">¶</a></dt>
<dd><p>Acceptable values are: guest, reporter, developer, maintainer, owner.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.GroupMembership.expires_at">
<em class="property">property </em><code class="sig-name descname">expires_at</code><a class="headerlink" href="#pulumi_gitlab.GroupMembership.expires_at" title="Permalink to this definition">¶</a></dt>
<dd><p>Expiration date for the group membership. Format: <code class="docutils literal notranslate"><span class="pre">YYYY-MM-DD</span></code></p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.GroupMembership.group_id">
<em class="property">property </em><code class="sig-name descname">group_id</code><a class="headerlink" href="#pulumi_gitlab.GroupMembership.group_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The id of the group.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.GroupMembership.user_id">
<em class="property">property </em><code class="sig-name descname">user_id</code><a class="headerlink" href="#pulumi_gitlab.GroupMembership.user_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The id of the user.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.GroupMembership.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gitlab.GroupMembership.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gitlab.GroupMembership.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gitlab.GroupMembership.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gitlab.GroupVariable">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gitlab.</code><code class="sig-name descname">GroupVariable</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">group</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">key</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">masked</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">protected</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">value</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">variable_type</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gitlab.GroupVariable" title="Permalink to this definition">¶</a></dt>
<dd><p>This resource allows you to create and manage CI/CD variables for your GitLab groups.
For further information on variables, consult the <a class="reference external" href="https://docs.gitlab.com/ce/ci/variables/README.html#variables">gitlab
documentation</a>.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_gitlab</span> <span class="k">as</span> <span class="nn">gitlab</span>

<span class="n">example</span> <span class="o">=</span> <span class="n">gitlab</span><span class="o">.</span><span class="n">GroupVariable</span><span class="p">(</span><span class="s2">&quot;example&quot;</span><span class="p">,</span>
    <span class="n">group</span><span class="o">=</span><span class="s2">&quot;12345&quot;</span><span class="p">,</span>
    <span class="n">key</span><span class="o">=</span><span class="s2">&quot;group_variable_key&quot;</span><span class="p">,</span>
    <span class="n">masked</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span>
    <span class="n">protected</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span>
    <span class="n">value</span><span class="o">=</span><span class="s2">&quot;group_variable_value&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>group</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name or id of the group to add the hook to.</p></li>
<li><p><strong>key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the variable.</p></li>
<li><p><strong>protected</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If set to <code class="docutils literal notranslate"><span class="pre">true</span></code>, the variable will be passed only to pipelines running on protected branches and tags. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>value</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The value of the variable.</p></li>
<li><p><strong>variable_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of a variable. Available types are: env_var (default) and file.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_gitlab.GroupVariable.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">group</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">key</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">masked</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">protected</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">value</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">variable_type</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_gitlab.group_variable.GroupVariable<a class="headerlink" href="#pulumi_gitlab.GroupVariable.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing GroupVariable resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>group</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name or id of the group to add the hook to.</p></li>
<li><p><strong>key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the variable.</p></li>
<li><p><strong>protected</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If set to <code class="docutils literal notranslate"><span class="pre">true</span></code>, the variable will be passed only to pipelines running on protected branches and tags. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>value</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The value of the variable.</p></li>
<li><p><strong>variable_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of a variable. Available types are: env_var (default) and file.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.GroupVariable.group">
<em class="property">property </em><code class="sig-name descname">group</code><a class="headerlink" href="#pulumi_gitlab.GroupVariable.group" title="Permalink to this definition">¶</a></dt>
<dd><p>The name or id of the group to add the hook to.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.GroupVariable.key">
<em class="property">property </em><code class="sig-name descname">key</code><a class="headerlink" href="#pulumi_gitlab.GroupVariable.key" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the variable.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.GroupVariable.protected">
<em class="property">property </em><code class="sig-name descname">protected</code><a class="headerlink" href="#pulumi_gitlab.GroupVariable.protected" title="Permalink to this definition">¶</a></dt>
<dd><p>If set to <code class="docutils literal notranslate"><span class="pre">true</span></code>, the variable will be passed only to pipelines running on protected branches and tags. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.GroupVariable.value">
<em class="property">property </em><code class="sig-name descname">value</code><a class="headerlink" href="#pulumi_gitlab.GroupVariable.value" title="Permalink to this definition">¶</a></dt>
<dd><p>The value of the variable.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.GroupVariable.variable_type">
<em class="property">property </em><code class="sig-name descname">variable_type</code><a class="headerlink" href="#pulumi_gitlab.GroupVariable.variable_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of a variable. Available types are: env_var (default) and file.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.GroupVariable.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gitlab.GroupVariable.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gitlab.GroupVariable.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gitlab.GroupVariable.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gitlab.InstanceCluster">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gitlab.</code><code class="sig-name descname">InstanceCluster</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">domain</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">environment_scope</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kubernetes_api_url</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kubernetes_authorization_type</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kubernetes_ca_cert</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kubernetes_namespace</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kubernetes_token</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">managed</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">management_project_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gitlab.InstanceCluster" title="Permalink to this definition">¶</a></dt>
<dd><p>This resource allows you to create and manage instance clusters for your GitLab instances.
For further information on clusters, consult the <a class="reference external" href="https://docs.gitlab.com/ee/user/instance/clusters/">gitlab
documentation</a>.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_gitlab</span> <span class="k">as</span> <span class="nn">gitlab</span>

<span class="n">bar</span> <span class="o">=</span> <span class="n">gitlab</span><span class="o">.</span><span class="n">InstanceCluster</span><span class="p">(</span><span class="s2">&quot;bar&quot;</span><span class="p">,</span>
    <span class="n">domain</span><span class="o">=</span><span class="s2">&quot;example.com&quot;</span><span class="p">,</span>
    <span class="n">enabled</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="n">environment_scope</span><span class="o">=</span><span class="s2">&quot;*&quot;</span><span class="p">,</span>
    <span class="n">kubernetes_api_url</span><span class="o">=</span><span class="s2">&quot;https://124.124.124&quot;</span><span class="p">,</span>
    <span class="n">kubernetes_authorization_type</span><span class="o">=</span><span class="s2">&quot;rbac&quot;</span><span class="p">,</span>
    <span class="n">kubernetes_ca_cert</span><span class="o">=</span><span class="s2">&quot;some-cert&quot;</span><span class="p">,</span>
    <span class="n">kubernetes_namespace</span><span class="o">=</span><span class="s2">&quot;namespace&quot;</span><span class="p">,</span>
    <span class="n">kubernetes_token</span><span class="o">=</span><span class="s2">&quot;some-token&quot;</span><span class="p">,</span>
    <span class="n">management_project_id</span><span class="o">=</span><span class="s2">&quot;123456&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>domain</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The base domain of the cluster.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Determines if cluster is active or not. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>. This attribute cannot be read.</p></li>
<li><p><strong>environment_scope</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The associated environment to the cluster. Defaults to <code class="docutils literal notranslate"><span class="pre">*</span></code>.</p></li>
<li><p><strong>kubernetes_api_url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The URL to access the Kubernetes API.</p></li>
<li><p><strong>kubernetes_authorization_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The cluster authorization type. Valid values are <code class="docutils literal notranslate"><span class="pre">rbac</span></code>, <code class="docutils literal notranslate"><span class="pre">abac</span></code>, <code class="docutils literal notranslate"><span class="pre">unknown_authorization</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">rbac</span></code>.</p></li>
<li><p><strong>kubernetes_ca_cert</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – TLS certificate (needed if API is using a self-signed TLS certificate).</p></li>
<li><p><strong>kubernetes_namespace</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique namespace related to the instance.</p></li>
<li><p><strong>kubernetes_token</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The token to authenticate against Kubernetes. This attribute cannot be read.</p></li>
<li><p><strong>managed</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Determines if cluster is managed by gitlab or not. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>. This attribute cannot be read.</p></li>
<li><p><strong>management_project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the management project for the cluster.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of cluster.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_gitlab.InstanceCluster.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cluster_type</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">created_at</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">domain</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">environment_scope</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kubernetes_api_url</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kubernetes_authorization_type</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kubernetes_ca_cert</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kubernetes_namespace</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kubernetes_token</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">managed</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">management_project_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">platform_type</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">provider_type</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_gitlab.instance_cluster.InstanceCluster<a class="headerlink" href="#pulumi_gitlab.InstanceCluster.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing InstanceCluster resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>domain</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The base domain of the cluster.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Determines if cluster is active or not. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>. This attribute cannot be read.</p></li>
<li><p><strong>environment_scope</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The associated environment to the cluster. Defaults to <code class="docutils literal notranslate"><span class="pre">*</span></code>.</p></li>
<li><p><strong>kubernetes_api_url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The URL to access the Kubernetes API.</p></li>
<li><p><strong>kubernetes_authorization_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The cluster authorization type. Valid values are <code class="docutils literal notranslate"><span class="pre">rbac</span></code>, <code class="docutils literal notranslate"><span class="pre">abac</span></code>, <code class="docutils literal notranslate"><span class="pre">unknown_authorization</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">rbac</span></code>.</p></li>
<li><p><strong>kubernetes_ca_cert</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – TLS certificate (needed if API is using a self-signed TLS certificate).</p></li>
<li><p><strong>kubernetes_namespace</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique namespace related to the instance.</p></li>
<li><p><strong>kubernetes_token</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The token to authenticate against Kubernetes. This attribute cannot be read.</p></li>
<li><p><strong>managed</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Determines if cluster is managed by gitlab or not. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>. This attribute cannot be read.</p></li>
<li><p><strong>management_project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the management project for the cluster.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of cluster.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.InstanceCluster.domain">
<em class="property">property </em><code class="sig-name descname">domain</code><a class="headerlink" href="#pulumi_gitlab.InstanceCluster.domain" title="Permalink to this definition">¶</a></dt>
<dd><p>The base domain of the cluster.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.InstanceCluster.enabled">
<em class="property">property </em><code class="sig-name descname">enabled</code><a class="headerlink" href="#pulumi_gitlab.InstanceCluster.enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Determines if cluster is active or not. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>. This attribute cannot be read.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.InstanceCluster.environment_scope">
<em class="property">property </em><code class="sig-name descname">environment_scope</code><a class="headerlink" href="#pulumi_gitlab.InstanceCluster.environment_scope" title="Permalink to this definition">¶</a></dt>
<dd><p>The associated environment to the cluster. Defaults to <code class="docutils literal notranslate"><span class="pre">*</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.InstanceCluster.kubernetes_api_url">
<em class="property">property </em><code class="sig-name descname">kubernetes_api_url</code><a class="headerlink" href="#pulumi_gitlab.InstanceCluster.kubernetes_api_url" title="Permalink to this definition">¶</a></dt>
<dd><p>The URL to access the Kubernetes API.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.InstanceCluster.kubernetes_authorization_type">
<em class="property">property </em><code class="sig-name descname">kubernetes_authorization_type</code><a class="headerlink" href="#pulumi_gitlab.InstanceCluster.kubernetes_authorization_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The cluster authorization type. Valid values are <code class="docutils literal notranslate"><span class="pre">rbac</span></code>, <code class="docutils literal notranslate"><span class="pre">abac</span></code>, <code class="docutils literal notranslate"><span class="pre">unknown_authorization</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">rbac</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.InstanceCluster.kubernetes_ca_cert">
<em class="property">property </em><code class="sig-name descname">kubernetes_ca_cert</code><a class="headerlink" href="#pulumi_gitlab.InstanceCluster.kubernetes_ca_cert" title="Permalink to this definition">¶</a></dt>
<dd><p>TLS certificate (needed if API is using a self-signed TLS certificate).</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.InstanceCluster.kubernetes_namespace">
<em class="property">property </em><code class="sig-name descname">kubernetes_namespace</code><a class="headerlink" href="#pulumi_gitlab.InstanceCluster.kubernetes_namespace" title="Permalink to this definition">¶</a></dt>
<dd><p>The unique namespace related to the instance.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.InstanceCluster.kubernetes_token">
<em class="property">property </em><code class="sig-name descname">kubernetes_token</code><a class="headerlink" href="#pulumi_gitlab.InstanceCluster.kubernetes_token" title="Permalink to this definition">¶</a></dt>
<dd><p>The token to authenticate against Kubernetes. This attribute cannot be read.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.InstanceCluster.managed">
<em class="property">property </em><code class="sig-name descname">managed</code><a class="headerlink" href="#pulumi_gitlab.InstanceCluster.managed" title="Permalink to this definition">¶</a></dt>
<dd><p>Determines if cluster is managed by gitlab or not. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>. This attribute cannot be read.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.InstanceCluster.management_project_id">
<em class="property">property </em><code class="sig-name descname">management_project_id</code><a class="headerlink" href="#pulumi_gitlab.InstanceCluster.management_project_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the management project for the cluster.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.InstanceCluster.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_gitlab.InstanceCluster.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of cluster.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.InstanceCluster.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gitlab.InstanceCluster.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gitlab.InstanceCluster.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gitlab.InstanceCluster.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gitlab.Label">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gitlab.</code><code class="sig-name descname">Label</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">color</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gitlab.Label" title="Permalink to this definition">¶</a></dt>
<dd><p>This resource allows you to create and manage labels for your GitLab projects.
For further information on labels, consult the <a class="reference external" href="https://docs.gitlab.com/ee/user/project/labels.html#project-labels">gitlab
documentation</a>.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_gitlab</span> <span class="k">as</span> <span class="nn">gitlab</span>

<span class="n">fixme</span> <span class="o">=</span> <span class="n">gitlab</span><span class="o">.</span><span class="n">Label</span><span class="p">(</span><span class="s2">&quot;fixme&quot;</span><span class="p">,</span>
    <span class="n">color</span><span class="o">=</span><span class="s2">&quot;#ffcc00&quot;</span><span class="p">,</span>
    <span class="n">description</span><span class="o">=</span><span class="s2">&quot;issue with failing tests&quot;</span><span class="p">,</span>
    <span class="n">project</span><span class="o">=</span><span class="s2">&quot;example&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>color</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The color of the label given in 6-digit hex notation with leading ‘#’ sign (e.g. #FFAABB) or one of the <a class="reference external" href="https://developer.mozilla.org/en-US/docs/Web/CSS/color_value#Color_keywords">CSS color names</a>.</p>
</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the label.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the label.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name or id of the project to add the label to.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_gitlab.Label.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">color</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_gitlab.label.Label<a class="headerlink" href="#pulumi_gitlab.Label.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Label resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>color</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The color of the label given in 6-digit hex notation with leading ‘#’ sign (e.g. #FFAABB) or one of the <a class="reference external" href="https://developer.mozilla.org/en-US/docs/Web/CSS/color_value#Color_keywords">CSS color names</a>.</p>
</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the label.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the label.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name or id of the project to add the label to.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.Label.color">
<em class="property">property </em><code class="sig-name descname">color</code><a class="headerlink" href="#pulumi_gitlab.Label.color" title="Permalink to this definition">¶</a></dt>
<dd><p>The color of the label given in 6-digit hex notation with leading ‘#’ sign (e.g. #FFAABB) or one of the <a class="reference external" href="https://developer.mozilla.org/en-US/docs/Web/CSS/color_value#Color_keywords">CSS color names</a>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.Label.description">
<em class="property">property </em><code class="sig-name descname">description</code><a class="headerlink" href="#pulumi_gitlab.Label.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description of the label.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.Label.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_gitlab.Label.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the label.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.Label.project">
<em class="property">property </em><code class="sig-name descname">project</code><a class="headerlink" href="#pulumi_gitlab.Label.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The name or id of the project to add the label to.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.Label.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gitlab.Label.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gitlab.Label.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gitlab.Label.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gitlab.PipelineSchedule">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gitlab.</code><code class="sig-name descname">PipelineSchedule</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">active</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cron</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cron_timezone</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ref</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gitlab.PipelineSchedule" title="Permalink to this definition">¶</a></dt>
<dd><p>This resource allows you to create and manage pipeline schedules.
For further information on clusters, consult the <a class="reference external" href="https://docs.gitlab.com/ce/user/project/pipelines/schedules.html">gitlab
documentation</a>.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_gitlab</span> <span class="k">as</span> <span class="nn">gitlab</span>

<span class="n">example</span> <span class="o">=</span> <span class="n">gitlab</span><span class="o">.</span><span class="n">PipelineSchedule</span><span class="p">(</span><span class="s2">&quot;example&quot;</span><span class="p">,</span>
    <span class="n">cron</span><span class="o">=</span><span class="s2">&quot;0 1 * * *&quot;</span><span class="p">,</span>
    <span class="n">description</span><span class="o">=</span><span class="s2">&quot;Used to schedule builds&quot;</span><span class="p">,</span>
    <span class="n">project</span><span class="o">=</span><span class="s2">&quot;12345&quot;</span><span class="p">,</span>
    <span class="n">ref</span><span class="o">=</span><span class="s2">&quot;master&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>active</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – The activation of pipeline schedule. If false is set, the pipeline schedule will deactivated initially.</p></li>
<li><p><strong>cron</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The cron (e.g. <code class="docutils literal notranslate"><span class="pre">0</span> <span class="pre">1</span> <span class="pre">*</span> <span class="pre">*</span> <span class="pre">*</span></code>).</p></li>
<li><p><strong>cron_timezone</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The timezone.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the pipeline schedule.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name or id of the project to add the schedule to.</p></li>
<li><p><strong>ref</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The branch/tag name to be triggered.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_gitlab.PipelineSchedule.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">active</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cron</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cron_timezone</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ref</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_gitlab.pipeline_schedule.PipelineSchedule<a class="headerlink" href="#pulumi_gitlab.PipelineSchedule.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing PipelineSchedule resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>active</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – The activation of pipeline schedule. If false is set, the pipeline schedule will deactivated initially.</p></li>
<li><p><strong>cron</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The cron (e.g. <code class="docutils literal notranslate"><span class="pre">0</span> <span class="pre">1</span> <span class="pre">*</span> <span class="pre">*</span> <span class="pre">*</span></code>).</p></li>
<li><p><strong>cron_timezone</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The timezone.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the pipeline schedule.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name or id of the project to add the schedule to.</p></li>
<li><p><strong>ref</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The branch/tag name to be triggered.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.PipelineSchedule.active">
<em class="property">property </em><code class="sig-name descname">active</code><a class="headerlink" href="#pulumi_gitlab.PipelineSchedule.active" title="Permalink to this definition">¶</a></dt>
<dd><p>The activation of pipeline schedule. If false is set, the pipeline schedule will deactivated initially.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.PipelineSchedule.cron">
<em class="property">property </em><code class="sig-name descname">cron</code><a class="headerlink" href="#pulumi_gitlab.PipelineSchedule.cron" title="Permalink to this definition">¶</a></dt>
<dd><p>The cron (e.g. <code class="docutils literal notranslate"><span class="pre">0</span> <span class="pre">1</span> <span class="pre">*</span> <span class="pre">*</span> <span class="pre">*</span></code>).</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.PipelineSchedule.cron_timezone">
<em class="property">property </em><code class="sig-name descname">cron_timezone</code><a class="headerlink" href="#pulumi_gitlab.PipelineSchedule.cron_timezone" title="Permalink to this definition">¶</a></dt>
<dd><p>The timezone.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.PipelineSchedule.description">
<em class="property">property </em><code class="sig-name descname">description</code><a class="headerlink" href="#pulumi_gitlab.PipelineSchedule.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description of the pipeline schedule.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.PipelineSchedule.project">
<em class="property">property </em><code class="sig-name descname">project</code><a class="headerlink" href="#pulumi_gitlab.PipelineSchedule.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The name or id of the project to add the schedule to.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.PipelineSchedule.ref">
<em class="property">property </em><code class="sig-name descname">ref</code><a class="headerlink" href="#pulumi_gitlab.PipelineSchedule.ref" title="Permalink to this definition">¶</a></dt>
<dd><p>The branch/tag name to be triggered.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.PipelineSchedule.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gitlab.PipelineSchedule.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gitlab.PipelineSchedule.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gitlab.PipelineSchedule.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gitlab.PipelineScheduleVariable">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gitlab.</code><code class="sig-name descname">PipelineScheduleVariable</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">key</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">pipeline_schedule_id</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">value</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gitlab.PipelineScheduleVariable" title="Permalink to this definition">¶</a></dt>
<dd><p>This resource allows you to create and manage variables for pipeline schedules.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_gitlab</span> <span class="k">as</span> <span class="nn">gitlab</span>

<span class="n">example_pipeline_schedule</span> <span class="o">=</span> <span class="n">gitlab</span><span class="o">.</span><span class="n">PipelineSchedule</span><span class="p">(</span><span class="s2">&quot;examplePipelineSchedule&quot;</span><span class="p">,</span>
    <span class="n">project</span><span class="o">=</span><span class="s2">&quot;12345&quot;</span><span class="p">,</span>
    <span class="n">description</span><span class="o">=</span><span class="s2">&quot;Used to schedule builds&quot;</span><span class="p">,</span>
    <span class="n">ref</span><span class="o">=</span><span class="s2">&quot;master&quot;</span><span class="p">,</span>
    <span class="n">cron</span><span class="o">=</span><span class="s2">&quot;0 1 * * *&quot;</span><span class="p">)</span>
<span class="n">example_pipeline_schedule_variable</span> <span class="o">=</span> <span class="n">gitlab</span><span class="o">.</span><span class="n">PipelineScheduleVariable</span><span class="p">(</span><span class="s2">&quot;examplePipelineScheduleVariable&quot;</span><span class="p">,</span>
    <span class="n">project</span><span class="o">=</span><span class="n">gitlab_pipeline_schedule</span><span class="p">[</span><span class="s2">&quot;project&quot;</span><span class="p">],</span>
    <span class="n">pipeline_schedule_id</span><span class="o">=</span><span class="n">gitlab_pipeline_schedule</span><span class="p">[</span><span class="s2">&quot;id&quot;</span><span class="p">],</span>
    <span class="n">key</span><span class="o">=</span><span class="s2">&quot;EXAMPLE_KEY&quot;</span><span class="p">,</span>
    <span class="n">value</span><span class="o">=</span><span class="s2">&quot;example&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the variable.</p></li>
<li><p><strong>pipeline_schedule_id</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The id of the pipeline schedule.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The id of the project to add the schedule to.</p></li>
<li><p><strong>value</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Value of the variable.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_gitlab.PipelineScheduleVariable.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">key</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">pipeline_schedule_id</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">value</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_gitlab.pipeline_schedule_variable.PipelineScheduleVariable<a class="headerlink" href="#pulumi_gitlab.PipelineScheduleVariable.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing PipelineScheduleVariable resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the variable.</p></li>
<li><p><strong>pipeline_schedule_id</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The id of the pipeline schedule.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The id of the project to add the schedule to.</p></li>
<li><p><strong>value</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Value of the variable.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.PipelineScheduleVariable.key">
<em class="property">property </em><code class="sig-name descname">key</code><a class="headerlink" href="#pulumi_gitlab.PipelineScheduleVariable.key" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the variable.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.PipelineScheduleVariable.pipeline_schedule_id">
<em class="property">property </em><code class="sig-name descname">pipeline_schedule_id</code><a class="headerlink" href="#pulumi_gitlab.PipelineScheduleVariable.pipeline_schedule_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The id of the pipeline schedule.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.PipelineScheduleVariable.project">
<em class="property">property </em><code class="sig-name descname">project</code><a class="headerlink" href="#pulumi_gitlab.PipelineScheduleVariable.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The id of the project to add the schedule to.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.PipelineScheduleVariable.value">
<em class="property">property </em><code class="sig-name descname">value</code><a class="headerlink" href="#pulumi_gitlab.PipelineScheduleVariable.value" title="Permalink to this definition">¶</a></dt>
<dd><p>Value of the variable.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.PipelineScheduleVariable.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gitlab.PipelineScheduleVariable.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gitlab.PipelineScheduleVariable.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gitlab.PipelineScheduleVariable.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gitlab.PipelineTrigger">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gitlab.</code><code class="sig-name descname">PipelineTrigger</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gitlab.PipelineTrigger" title="Permalink to this definition">¶</a></dt>
<dd><p>This resource allows you to create and manage pipeline triggers</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_gitlab</span> <span class="k">as</span> <span class="nn">gitlab</span>

<span class="n">example</span> <span class="o">=</span> <span class="n">gitlab</span><span class="o">.</span><span class="n">PipelineTrigger</span><span class="p">(</span><span class="s2">&quot;example&quot;</span><span class="p">,</span>
    <span class="n">description</span><span class="o">=</span><span class="s2">&quot;Used to trigger builds&quot;</span><span class="p">,</span>
    <span class="n">project</span><span class="o">=</span><span class="s2">&quot;12345&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the pipeline trigger.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name or id of the project to add the trigger to.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_gitlab.PipelineTrigger.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">token</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_gitlab.pipeline_trigger.PipelineTrigger<a class="headerlink" href="#pulumi_gitlab.PipelineTrigger.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing PipelineTrigger resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the pipeline trigger.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name or id of the project to add the trigger to.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.PipelineTrigger.description">
<em class="property">property </em><code class="sig-name descname">description</code><a class="headerlink" href="#pulumi_gitlab.PipelineTrigger.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description of the pipeline trigger.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.PipelineTrigger.project">
<em class="property">property </em><code class="sig-name descname">project</code><a class="headerlink" href="#pulumi_gitlab.PipelineTrigger.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The name or id of the project to add the trigger to.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.PipelineTrigger.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gitlab.PipelineTrigger.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gitlab.PipelineTrigger.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gitlab.PipelineTrigger.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gitlab.Project">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gitlab.</code><code class="sig-name descname">Project</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">approvals_before_merge</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">archived</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">container_registry_enabled</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">default_branch</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">group_with_project_templates_id</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">import_url</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">initialize_with_readme</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">issues_enabled</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">lfs_enabled</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">merge_method</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">merge_requests_enabled</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">namespace_id</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">only_allow_merge_if_all_discussions_are_resolved</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">only_allow_merge_if_pipeline_succeeds</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">packages_enabled</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">path</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">pipelines_enabled</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">push_rules</span><span class="p">:</span> <span class="n">Union[ProjectPushRulesArgs, Mapping[str, Any], Awaitable[Union[ProjectPushRulesArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">remove_source_branch_after_merge</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">request_access_enabled</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">shared_runners_enabled</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">snippets_enabled</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">template_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">template_project_id</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">use_custom_template</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">visibility_level</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">wiki_enabled</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gitlab.Project" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a Project resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[int] approvals_before_merge: Number of merge request approvals required for merging. Default is 0.
:param pulumi.Input[bool] archived: Whether the project is in read-only mode (archived). Repositories can be archived/unarchived by toggling this parameter.
:param pulumi.Input[bool] container_registry_enabled: Enable container registry for the project.
:param pulumi.Input[str] default_branch: The default branch for the project.
:param pulumi.Input[str] description: A description of the project.
:param pulumi.Input[int] group_with_project_templates_id: For group-level custom templates, specifies ID of group from which all the custom project templates are sourced. Leave empty for instance-level templates. Requires use_custom_template to be true (enterprise edition).
:param pulumi.Input[str] import_url: Git URL to a repository to be imported.
:param pulumi.Input[bool] initialize_with_readme: Create master branch with first commit containing a README.md file.
:param pulumi.Input[bool] issues_enabled: Enable issue tracking for the project.
:param pulumi.Input[bool] lfs_enabled: Enable LFS for the project.
:param pulumi.Input[str] merge_method: Set to <code class="docutils literal notranslate"><span class="pre">ff</span></code> to create fast-forward merges</p>
<blockquote>
<div><p>Valid values are <code class="docutils literal notranslate"><span class="pre">merge</span></code>, <code class="docutils literal notranslate"><span class="pre">rebase_merge</span></code>, <code class="docutils literal notranslate"><span class="pre">ff</span></code>
Repositories are created with <code class="docutils literal notranslate"><span class="pre">merge</span></code> by default</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>merge_requests_enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enable merge requests for the project.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the project.</p></li>
<li><p><strong>namespace_id</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The namespace (group or user) of the project. Defaults to your user.
See <code class="docutils literal notranslate"><span class="pre">Group</span></code> for an example.</p></li>
<li><p><strong>only_allow_merge_if_all_discussions_are_resolved</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Set to true if you want allow merges only if all discussions are resolved.</p></li>
<li><p><strong>only_allow_merge_if_pipeline_succeeds</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Set to true if you want allow merges only if a pipeline succeeds.</p></li>
<li><p><strong>packages_enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enable packages repository for the project.</p></li>
<li><p><strong>path</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The path of the repository.</p></li>
<li><p><strong>pipelines_enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enable pipelines for the project.</p></li>
<li><p><strong>push_rules</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'ProjectPushRulesArgs'</em><em>]</em><em>]</em>) – Push rules for the project (documented below).</p></li>
<li><p><strong>remove_source_branch_after_merge</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enable <code class="docutils literal notranslate"><span class="pre">Delete</span> <span class="pre">source</span> <span class="pre">branch</span></code> option by default for all new merge requests.</p></li>
<li><p><strong>request_access_enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Allow users to request member access.</p></li>
<li><p><strong>shared_runners_enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enable shared runners for this project.</p></li>
<li><p><strong>snippets_enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enable snippets for the project.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – Tags (topics) of the project.</p></li>
<li><p><strong>template_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – When used without use_custom_template, name of a built-in project template. When used with use_custom_template, name of a custom project template. This option is mutually exclusive with <code class="docutils literal notranslate"><span class="pre">template_project_id</span></code>.</p></li>
<li><p><strong>template_project_id</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – When used with use_custom_template, project ID of a custom project template. This is preferable to using template_name since template_name may be ambiguous (enterprise edition). This option is mutually exclusive with <code class="docutils literal notranslate"><span class="pre">template_name</span></code>.</p></li>
<li><p><strong>use_custom_template</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Use either custom instance or group (with group_with_project_templates_id) project template (enterprise edition).</p></li>
<li><p><strong>visibility_level</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Set to <code class="docutils literal notranslate"><span class="pre">public</span></code> to create a public project.
Valid values are <code class="docutils literal notranslate"><span class="pre">private</span></code>, <code class="docutils literal notranslate"><span class="pre">internal</span></code>, <code class="docutils literal notranslate"><span class="pre">public</span></code>.
Repositories are created as private by default.</p></li>
<li><p><strong>wiki_enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enable wiki for the project.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_gitlab.Project.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">approvals_before_merge</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">archived</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">container_registry_enabled</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">default_branch</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">group_with_project_templates_id</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">http_url_to_repo</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">import_url</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">initialize_with_readme</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">issues_enabled</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">lfs_enabled</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">merge_method</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">merge_requests_enabled</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">namespace_id</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">only_allow_merge_if_all_discussions_are_resolved</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">only_allow_merge_if_pipeline_succeeds</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">packages_enabled</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">path</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">path_with_namespace</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">pipelines_enabled</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">push_rules</span><span class="p">:</span> <span class="n">Union[ProjectPushRulesArgs, Mapping[str, Any], Awaitable[Union[ProjectPushRulesArgs, Mapping[str, Any]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">remove_source_branch_after_merge</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">request_access_enabled</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">runners_token</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">shared_runners_enabled</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">snippets_enabled</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ssh_url_to_repo</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tags</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">template_name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">template_project_id</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">use_custom_template</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">visibility_level</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">web_url</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">wiki_enabled</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_gitlab.project.Project<a class="headerlink" href="#pulumi_gitlab.Project.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Project resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>approvals_before_merge</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Number of merge request approvals required for merging. Default is 0.</p></li>
<li><p><strong>archived</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the project is in read-only mode (archived). Repositories can be archived/unarchived by toggling this parameter.</p></li>
<li><p><strong>container_registry_enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enable container registry for the project.</p></li>
<li><p><strong>default_branch</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The default branch for the project.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A description of the project.</p></li>
<li><p><strong>group_with_project_templates_id</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – For group-level custom templates, specifies ID of group from which all the custom project templates are sourced. Leave empty for instance-level templates. Requires use_custom_template to be true (enterprise edition).</p></li>
<li><p><strong>http_url_to_repo</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – URL that can be provided to <code class="docutils literal notranslate"><span class="pre">git</span> <span class="pre">clone</span></code> to clone the
repository via HTTP.</p></li>
<li><p><strong>import_url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Git URL to a repository to be imported.</p></li>
<li><p><strong>initialize_with_readme</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Create master branch with first commit containing a README.md file.</p></li>
<li><p><strong>issues_enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enable issue tracking for the project.</p></li>
<li><p><strong>lfs_enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enable LFS for the project.</p></li>
<li><p><strong>merge_method</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Set to <code class="docutils literal notranslate"><span class="pre">ff</span></code> to create fast-forward merges
Valid values are <code class="docutils literal notranslate"><span class="pre">merge</span></code>, <code class="docutils literal notranslate"><span class="pre">rebase_merge</span></code>, <code class="docutils literal notranslate"><span class="pre">ff</span></code>
Repositories are created with <code class="docutils literal notranslate"><span class="pre">merge</span></code> by default</p></li>
<li><p><strong>merge_requests_enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enable merge requests for the project.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the project.</p></li>
<li><p><strong>namespace_id</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The namespace (group or user) of the project. Defaults to your user.
See <code class="docutils literal notranslate"><span class="pre">Group</span></code> for an example.</p></li>
<li><p><strong>only_allow_merge_if_all_discussions_are_resolved</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Set to true if you want allow merges only if all discussions are resolved.</p></li>
<li><p><strong>only_allow_merge_if_pipeline_succeeds</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Set to true if you want allow merges only if a pipeline succeeds.</p></li>
<li><p><strong>packages_enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enable packages repository for the project.</p></li>
<li><p><strong>path</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The path of the repository.</p></li>
<li><p><strong>path_with_namespace</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The path of the repository with namespace.</p></li>
<li><p><strong>pipelines_enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enable pipelines for the project.</p></li>
<li><p><strong>push_rules</strong> (<em>pulumi.Input</em><em>[</em><em>pulumi.InputType</em><em>[</em><em>'ProjectPushRulesArgs'</em><em>]</em><em>]</em>) – Push rules for the project (documented below).</p></li>
<li><p><strong>remove_source_branch_after_merge</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enable <code class="docutils literal notranslate"><span class="pre">Delete</span> <span class="pre">source</span> <span class="pre">branch</span></code> option by default for all new merge requests.</p></li>
<li><p><strong>request_access_enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Allow users to request member access.</p></li>
<li><p><strong>runners_token</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Registration token to use during runner setup.</p></li>
<li><p><strong>shared_runners_enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enable shared runners for this project.</p></li>
<li><p><strong>snippets_enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enable snippets for the project.</p></li>
<li><p><strong>ssh_url_to_repo</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – URL that can be provided to <code class="docutils literal notranslate"><span class="pre">git</span> <span class="pre">clone</span></code> to clone the
repository via SSH.</p></li>
<li><p><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – Tags (topics) of the project.</p></li>
<li><p><strong>template_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – When used without use_custom_template, name of a built-in project template. When used with use_custom_template, name of a custom project template. This option is mutually exclusive with <code class="docutils literal notranslate"><span class="pre">template_project_id</span></code>.</p></li>
<li><p><strong>template_project_id</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – When used with use_custom_template, project ID of a custom project template. This is preferable to using template_name since template_name may be ambiguous (enterprise edition). This option is mutually exclusive with <code class="docutils literal notranslate"><span class="pre">template_name</span></code>.</p></li>
<li><p><strong>use_custom_template</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Use either custom instance or group (with group_with_project_templates_id) project template (enterprise edition).</p></li>
<li><p><strong>visibility_level</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Set to <code class="docutils literal notranslate"><span class="pre">public</span></code> to create a public project.
Valid values are <code class="docutils literal notranslate"><span class="pre">private</span></code>, <code class="docutils literal notranslate"><span class="pre">internal</span></code>, <code class="docutils literal notranslate"><span class="pre">public</span></code>.
Repositories are created as private by default.</p></li>
<li><p><strong>web_url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – URL that can be used to find the project in a browser.</p></li>
<li><p><strong>wiki_enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enable wiki for the project.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.Project.approvals_before_merge">
<em class="property">property </em><code class="sig-name descname">approvals_before_merge</code><a class="headerlink" href="#pulumi_gitlab.Project.approvals_before_merge" title="Permalink to this definition">¶</a></dt>
<dd><p>Number of merge request approvals required for merging. Default is 0.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.Project.archived">
<em class="property">property </em><code class="sig-name descname">archived</code><a class="headerlink" href="#pulumi_gitlab.Project.archived" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the project is in read-only mode (archived). Repositories can be archived/unarchived by toggling this parameter.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.Project.container_registry_enabled">
<em class="property">property </em><code class="sig-name descname">container_registry_enabled</code><a class="headerlink" href="#pulumi_gitlab.Project.container_registry_enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Enable container registry for the project.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.Project.default_branch">
<em class="property">property </em><code class="sig-name descname">default_branch</code><a class="headerlink" href="#pulumi_gitlab.Project.default_branch" title="Permalink to this definition">¶</a></dt>
<dd><p>The default branch for the project.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.Project.description">
<em class="property">property </em><code class="sig-name descname">description</code><a class="headerlink" href="#pulumi_gitlab.Project.description" title="Permalink to this definition">¶</a></dt>
<dd><p>A description of the project.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.Project.group_with_project_templates_id">
<em class="property">property </em><code class="sig-name descname">group_with_project_templates_id</code><a class="headerlink" href="#pulumi_gitlab.Project.group_with_project_templates_id" title="Permalink to this definition">¶</a></dt>
<dd><p>For group-level custom templates, specifies ID of group from which all the custom project templates are sourced. Leave empty for instance-level templates. Requires use_custom_template to be true (enterprise edition).</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.Project.http_url_to_repo">
<em class="property">property </em><code class="sig-name descname">http_url_to_repo</code><a class="headerlink" href="#pulumi_gitlab.Project.http_url_to_repo" title="Permalink to this definition">¶</a></dt>
<dd><p>URL that can be provided to <code class="docutils literal notranslate"><span class="pre">git</span> <span class="pre">clone</span></code> to clone the
repository via HTTP.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.Project.import_url">
<em class="property">property </em><code class="sig-name descname">import_url</code><a class="headerlink" href="#pulumi_gitlab.Project.import_url" title="Permalink to this definition">¶</a></dt>
<dd><p>Git URL to a repository to be imported.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.Project.initialize_with_readme">
<em class="property">property </em><code class="sig-name descname">initialize_with_readme</code><a class="headerlink" href="#pulumi_gitlab.Project.initialize_with_readme" title="Permalink to this definition">¶</a></dt>
<dd><p>Create master branch with first commit containing a README.md file.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.Project.issues_enabled">
<em class="property">property </em><code class="sig-name descname">issues_enabled</code><a class="headerlink" href="#pulumi_gitlab.Project.issues_enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Enable issue tracking for the project.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.Project.lfs_enabled">
<em class="property">property </em><code class="sig-name descname">lfs_enabled</code><a class="headerlink" href="#pulumi_gitlab.Project.lfs_enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Enable LFS for the project.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.Project.merge_method">
<em class="property">property </em><code class="sig-name descname">merge_method</code><a class="headerlink" href="#pulumi_gitlab.Project.merge_method" title="Permalink to this definition">¶</a></dt>
<dd><p>Set to <code class="docutils literal notranslate"><span class="pre">ff</span></code> to create fast-forward merges
Valid values are <code class="docutils literal notranslate"><span class="pre">merge</span></code>, <code class="docutils literal notranslate"><span class="pre">rebase_merge</span></code>, <code class="docutils literal notranslate"><span class="pre">ff</span></code>
Repositories are created with <code class="docutils literal notranslate"><span class="pre">merge</span></code> by default</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.Project.merge_requests_enabled">
<em class="property">property </em><code class="sig-name descname">merge_requests_enabled</code><a class="headerlink" href="#pulumi_gitlab.Project.merge_requests_enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Enable merge requests for the project.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.Project.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_gitlab.Project.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the project.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.Project.namespace_id">
<em class="property">property </em><code class="sig-name descname">namespace_id</code><a class="headerlink" href="#pulumi_gitlab.Project.namespace_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The namespace (group or user) of the project. Defaults to your user.
See <code class="docutils literal notranslate"><span class="pre">Group</span></code> for an example.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.Project.only_allow_merge_if_all_discussions_are_resolved">
<em class="property">property </em><code class="sig-name descname">only_allow_merge_if_all_discussions_are_resolved</code><a class="headerlink" href="#pulumi_gitlab.Project.only_allow_merge_if_all_discussions_are_resolved" title="Permalink to this definition">¶</a></dt>
<dd><p>Set to true if you want allow merges only if all discussions are resolved.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.Project.only_allow_merge_if_pipeline_succeeds">
<em class="property">property </em><code class="sig-name descname">only_allow_merge_if_pipeline_succeeds</code><a class="headerlink" href="#pulumi_gitlab.Project.only_allow_merge_if_pipeline_succeeds" title="Permalink to this definition">¶</a></dt>
<dd><p>Set to true if you want allow merges only if a pipeline succeeds.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.Project.packages_enabled">
<em class="property">property </em><code class="sig-name descname">packages_enabled</code><a class="headerlink" href="#pulumi_gitlab.Project.packages_enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Enable packages repository for the project.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.Project.path">
<em class="property">property </em><code class="sig-name descname">path</code><a class="headerlink" href="#pulumi_gitlab.Project.path" title="Permalink to this definition">¶</a></dt>
<dd><p>The path of the repository.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.Project.path_with_namespace">
<em class="property">property </em><code class="sig-name descname">path_with_namespace</code><a class="headerlink" href="#pulumi_gitlab.Project.path_with_namespace" title="Permalink to this definition">¶</a></dt>
<dd><p>The path of the repository with namespace.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.Project.pipelines_enabled">
<em class="property">property </em><code class="sig-name descname">pipelines_enabled</code><a class="headerlink" href="#pulumi_gitlab.Project.pipelines_enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Enable pipelines for the project.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.Project.push_rules">
<em class="property">property </em><code class="sig-name descname">push_rules</code><a class="headerlink" href="#pulumi_gitlab.Project.push_rules" title="Permalink to this definition">¶</a></dt>
<dd><p>Push rules for the project (documented below).</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.Project.remove_source_branch_after_merge">
<em class="property">property </em><code class="sig-name descname">remove_source_branch_after_merge</code><a class="headerlink" href="#pulumi_gitlab.Project.remove_source_branch_after_merge" title="Permalink to this definition">¶</a></dt>
<dd><p>Enable <code class="docutils literal notranslate"><span class="pre">Delete</span> <span class="pre">source</span> <span class="pre">branch</span></code> option by default for all new merge requests.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.Project.request_access_enabled">
<em class="property">property </em><code class="sig-name descname">request_access_enabled</code><a class="headerlink" href="#pulumi_gitlab.Project.request_access_enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Allow users to request member access.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.Project.runners_token">
<em class="property">property </em><code class="sig-name descname">runners_token</code><a class="headerlink" href="#pulumi_gitlab.Project.runners_token" title="Permalink to this definition">¶</a></dt>
<dd><p>Registration token to use during runner setup.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.Project.shared_runners_enabled">
<em class="property">property </em><code class="sig-name descname">shared_runners_enabled</code><a class="headerlink" href="#pulumi_gitlab.Project.shared_runners_enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Enable shared runners for this project.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.Project.snippets_enabled">
<em class="property">property </em><code class="sig-name descname">snippets_enabled</code><a class="headerlink" href="#pulumi_gitlab.Project.snippets_enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Enable snippets for the project.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.Project.ssh_url_to_repo">
<em class="property">property </em><code class="sig-name descname">ssh_url_to_repo</code><a class="headerlink" href="#pulumi_gitlab.Project.ssh_url_to_repo" title="Permalink to this definition">¶</a></dt>
<dd><p>URL that can be provided to <code class="docutils literal notranslate"><span class="pre">git</span> <span class="pre">clone</span></code> to clone the
repository via SSH.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.Project.tags">
<em class="property">property </em><code class="sig-name descname">tags</code><a class="headerlink" href="#pulumi_gitlab.Project.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>Tags (topics) of the project.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.Project.template_name">
<em class="property">property </em><code class="sig-name descname">template_name</code><a class="headerlink" href="#pulumi_gitlab.Project.template_name" title="Permalink to this definition">¶</a></dt>
<dd><p>When used without use_custom_template, name of a built-in project template. When used with use_custom_template, name of a custom project template. This option is mutually exclusive with <code class="docutils literal notranslate"><span class="pre">template_project_id</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.Project.template_project_id">
<em class="property">property </em><code class="sig-name descname">template_project_id</code><a class="headerlink" href="#pulumi_gitlab.Project.template_project_id" title="Permalink to this definition">¶</a></dt>
<dd><p>When used with use_custom_template, project ID of a custom project template. This is preferable to using template_name since template_name may be ambiguous (enterprise edition). This option is mutually exclusive with <code class="docutils literal notranslate"><span class="pre">template_name</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.Project.use_custom_template">
<em class="property">property </em><code class="sig-name descname">use_custom_template</code><a class="headerlink" href="#pulumi_gitlab.Project.use_custom_template" title="Permalink to this definition">¶</a></dt>
<dd><p>Use either custom instance or group (with group_with_project_templates_id) project template (enterprise edition).</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.Project.visibility_level">
<em class="property">property </em><code class="sig-name descname">visibility_level</code><a class="headerlink" href="#pulumi_gitlab.Project.visibility_level" title="Permalink to this definition">¶</a></dt>
<dd><p>Set to <code class="docutils literal notranslate"><span class="pre">public</span></code> to create a public project.
Valid values are <code class="docutils literal notranslate"><span class="pre">private</span></code>, <code class="docutils literal notranslate"><span class="pre">internal</span></code>, <code class="docutils literal notranslate"><span class="pre">public</span></code>.
Repositories are created as private by default.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.Project.web_url">
<em class="property">property </em><code class="sig-name descname">web_url</code><a class="headerlink" href="#pulumi_gitlab.Project.web_url" title="Permalink to this definition">¶</a></dt>
<dd><p>URL that can be used to find the project in a browser.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.Project.wiki_enabled">
<em class="property">property </em><code class="sig-name descname">wiki_enabled</code><a class="headerlink" href="#pulumi_gitlab.Project.wiki_enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Enable wiki for the project.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.Project.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gitlab.Project.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gitlab.Project.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gitlab.Project.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gitlab.ProjectCluster">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gitlab.</code><code class="sig-name descname">ProjectCluster</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">domain</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">environment_scope</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kubernetes_api_url</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kubernetes_authorization_type</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kubernetes_ca_cert</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kubernetes_namespace</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kubernetes_token</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">managed</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">management_project_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gitlab.ProjectCluster" title="Permalink to this definition">¶</a></dt>
<dd><p>This resource allows you to create and manage project clusters for your GitLab projects.
For further information on clusters, consult the <a class="reference external" href="https://docs.gitlab.com/ce/user/project/clusters/index.html">gitlab
documentation</a>.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_gitlab</span> <span class="k">as</span> <span class="nn">gitlab</span>

<span class="n">foo</span> <span class="o">=</span> <span class="n">gitlab</span><span class="o">.</span><span class="n">Project</span><span class="p">(</span><span class="s2">&quot;foo&quot;</span><span class="p">)</span>
<span class="n">bar</span> <span class="o">=</span> <span class="n">gitlab</span><span class="o">.</span><span class="n">ProjectCluster</span><span class="p">(</span><span class="s2">&quot;bar&quot;</span><span class="p">,</span>
    <span class="n">domain</span><span class="o">=</span><span class="s2">&quot;example.com&quot;</span><span class="p">,</span>
    <span class="n">enabled</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="n">environment_scope</span><span class="o">=</span><span class="s2">&quot;*&quot;</span><span class="p">,</span>
    <span class="n">kubernetes_api_url</span><span class="o">=</span><span class="s2">&quot;https://124.124.124&quot;</span><span class="p">,</span>
    <span class="n">kubernetes_authorization_type</span><span class="o">=</span><span class="s2">&quot;rbac&quot;</span><span class="p">,</span>
    <span class="n">kubernetes_ca_cert</span><span class="o">=</span><span class="s2">&quot;some-cert&quot;</span><span class="p">,</span>
    <span class="n">kubernetes_namespace</span><span class="o">=</span><span class="s2">&quot;namespace&quot;</span><span class="p">,</span>
    <span class="n">kubernetes_token</span><span class="o">=</span><span class="s2">&quot;some-token&quot;</span><span class="p">,</span>
    <span class="n">management_project_id</span><span class="o">=</span><span class="s2">&quot;123456&quot;</span><span class="p">,</span>
    <span class="n">project</span><span class="o">=</span><span class="n">foo</span><span class="o">.</span><span class="n">id</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>domain</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The base domain of the cluster.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Determines if cluster is active or not. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>. This attribute cannot be read.</p></li>
<li><p><strong>environment_scope</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The associated environment to the cluster. Defaults to <code class="docutils literal notranslate"><span class="pre">*</span></code>.</p></li>
<li><p><strong>kubernetes_api_url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The URL to access the Kubernetes API.</p></li>
<li><p><strong>kubernetes_authorization_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The cluster authorization type. Valid values are <code class="docutils literal notranslate"><span class="pre">rbac</span></code>, <code class="docutils literal notranslate"><span class="pre">abac</span></code>, <code class="docutils literal notranslate"><span class="pre">unknown_authorization</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">rbac</span></code>.</p></li>
<li><p><strong>kubernetes_ca_cert</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – TLS certificate (needed if API is using a self-signed TLS certificate).</p></li>
<li><p><strong>kubernetes_namespace</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique namespace related to the project.</p></li>
<li><p><strong>kubernetes_token</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The token to authenticate against Kubernetes.</p></li>
<li><p><strong>managed</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Determines if cluster is managed by gitlab or not. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>. This attribute cannot be read.</p></li>
<li><p><strong>management_project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the management project for the cluster.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of cluster.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The id of the project to add the cluster to.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_gitlab.ProjectCluster.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cluster_type</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">created_at</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">domain</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">environment_scope</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kubernetes_api_url</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kubernetes_authorization_type</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kubernetes_ca_cert</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kubernetes_namespace</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">kubernetes_token</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">managed</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">management_project_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">platform_type</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">provider_type</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_gitlab.project_cluster.ProjectCluster<a class="headerlink" href="#pulumi_gitlab.ProjectCluster.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ProjectCluster resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>domain</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The base domain of the cluster.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Determines if cluster is active or not. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>. This attribute cannot be read.</p></li>
<li><p><strong>environment_scope</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The associated environment to the cluster. Defaults to <code class="docutils literal notranslate"><span class="pre">*</span></code>.</p></li>
<li><p><strong>kubernetes_api_url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The URL to access the Kubernetes API.</p></li>
<li><p><strong>kubernetes_authorization_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The cluster authorization type. Valid values are <code class="docutils literal notranslate"><span class="pre">rbac</span></code>, <code class="docutils literal notranslate"><span class="pre">abac</span></code>, <code class="docutils literal notranslate"><span class="pre">unknown_authorization</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">rbac</span></code>.</p></li>
<li><p><strong>kubernetes_ca_cert</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – TLS certificate (needed if API is using a self-signed TLS certificate).</p></li>
<li><p><strong>kubernetes_namespace</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique namespace related to the project.</p></li>
<li><p><strong>kubernetes_token</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The token to authenticate against Kubernetes.</p></li>
<li><p><strong>managed</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Determines if cluster is managed by gitlab or not. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>. This attribute cannot be read.</p></li>
<li><p><strong>management_project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the management project for the cluster.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of cluster.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The id of the project to add the cluster to.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.ProjectCluster.domain">
<em class="property">property </em><code class="sig-name descname">domain</code><a class="headerlink" href="#pulumi_gitlab.ProjectCluster.domain" title="Permalink to this definition">¶</a></dt>
<dd><p>The base domain of the cluster.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.ProjectCluster.enabled">
<em class="property">property </em><code class="sig-name descname">enabled</code><a class="headerlink" href="#pulumi_gitlab.ProjectCluster.enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Determines if cluster is active or not. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>. This attribute cannot be read.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.ProjectCluster.environment_scope">
<em class="property">property </em><code class="sig-name descname">environment_scope</code><a class="headerlink" href="#pulumi_gitlab.ProjectCluster.environment_scope" title="Permalink to this definition">¶</a></dt>
<dd><p>The associated environment to the cluster. Defaults to <code class="docutils literal notranslate"><span class="pre">*</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.ProjectCluster.kubernetes_api_url">
<em class="property">property </em><code class="sig-name descname">kubernetes_api_url</code><a class="headerlink" href="#pulumi_gitlab.ProjectCluster.kubernetes_api_url" title="Permalink to this definition">¶</a></dt>
<dd><p>The URL to access the Kubernetes API.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.ProjectCluster.kubernetes_authorization_type">
<em class="property">property </em><code class="sig-name descname">kubernetes_authorization_type</code><a class="headerlink" href="#pulumi_gitlab.ProjectCluster.kubernetes_authorization_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The cluster authorization type. Valid values are <code class="docutils literal notranslate"><span class="pre">rbac</span></code>, <code class="docutils literal notranslate"><span class="pre">abac</span></code>, <code class="docutils literal notranslate"><span class="pre">unknown_authorization</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">rbac</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.ProjectCluster.kubernetes_ca_cert">
<em class="property">property </em><code class="sig-name descname">kubernetes_ca_cert</code><a class="headerlink" href="#pulumi_gitlab.ProjectCluster.kubernetes_ca_cert" title="Permalink to this definition">¶</a></dt>
<dd><p>TLS certificate (needed if API is using a self-signed TLS certificate).</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.ProjectCluster.kubernetes_namespace">
<em class="property">property </em><code class="sig-name descname">kubernetes_namespace</code><a class="headerlink" href="#pulumi_gitlab.ProjectCluster.kubernetes_namespace" title="Permalink to this definition">¶</a></dt>
<dd><p>The unique namespace related to the project.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.ProjectCluster.kubernetes_token">
<em class="property">property </em><code class="sig-name descname">kubernetes_token</code><a class="headerlink" href="#pulumi_gitlab.ProjectCluster.kubernetes_token" title="Permalink to this definition">¶</a></dt>
<dd><p>The token to authenticate against Kubernetes.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.ProjectCluster.managed">
<em class="property">property </em><code class="sig-name descname">managed</code><a class="headerlink" href="#pulumi_gitlab.ProjectCluster.managed" title="Permalink to this definition">¶</a></dt>
<dd><p>Determines if cluster is managed by gitlab or not. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>. This attribute cannot be read.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.ProjectCluster.management_project_id">
<em class="property">property </em><code class="sig-name descname">management_project_id</code><a class="headerlink" href="#pulumi_gitlab.ProjectCluster.management_project_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the management project for the cluster.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.ProjectCluster.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_gitlab.ProjectCluster.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of cluster.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.ProjectCluster.project">
<em class="property">property </em><code class="sig-name descname">project</code><a class="headerlink" href="#pulumi_gitlab.ProjectCluster.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The id of the project to add the cluster to.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.ProjectCluster.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gitlab.ProjectCluster.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gitlab.ProjectCluster.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gitlab.ProjectCluster.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gitlab.ProjectHook">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gitlab.</code><code class="sig-name descname">ProjectHook</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enable_ssl_verification</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">issues_events</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">job_events</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">merge_requests_events</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">note_events</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">pipeline_events</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">push_events</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tag_push_events</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">token</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">url</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">wiki_page_events</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gitlab.ProjectHook" title="Permalink to this definition">¶</a></dt>
<dd><p>This resource allows you to create and manage hooks for your GitLab projects.
For further information on hooks, consult the <a class="reference external" href="https://docs.gitlab.com/ce/user/project/integrations/webhooks.html">gitlab
documentation</a>.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_gitlab</span> <span class="k">as</span> <span class="nn">gitlab</span>

<span class="n">example</span> <span class="o">=</span> <span class="n">gitlab</span><span class="o">.</span><span class="n">ProjectHook</span><span class="p">(</span><span class="s2">&quot;example&quot;</span><span class="p">,</span>
    <span class="n">merge_requests_events</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="n">project</span><span class="o">=</span><span class="s2">&quot;example/hooked&quot;</span><span class="p">,</span>
    <span class="n">url</span><span class="o">=</span><span class="s2">&quot;https://example.com/hook/example&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>enable_ssl_verification</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enable ssl verification when invoking
the hook.</p></li>
<li><p><strong>issues_events</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Invoke the hook for issues events.</p></li>
<li><p><strong>job_events</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Invoke the hook for job events.</p></li>
<li><p><strong>merge_requests_events</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Invoke the hook for merge requests.</p></li>
<li><p><strong>note_events</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Invoke the hook for notes events.</p></li>
<li><p><strong>pipeline_events</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Invoke the hook for pipeline events.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name or id of the project to add the hook to.</p></li>
<li><p><strong>push_events</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Invoke the hook for push events.</p></li>
<li><p><strong>tag_push_events</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Invoke the hook for tag push events.</p></li>
<li><p><strong>token</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A token to present when invoking the hook.</p></li>
<li><p><strong>url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The url of the hook to invoke.</p></li>
<li><p><strong>wiki_page_events</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Invoke the hook for wiki page events.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_gitlab.ProjectHook.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enable_ssl_verification</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">issues_events</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">job_events</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">merge_requests_events</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">note_events</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">pipeline_events</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">push_events</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tag_push_events</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">token</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">url</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">wiki_page_events</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_gitlab.project_hook.ProjectHook<a class="headerlink" href="#pulumi_gitlab.ProjectHook.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ProjectHook resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>enable_ssl_verification</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enable ssl verification when invoking
the hook.</p></li>
<li><p><strong>issues_events</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Invoke the hook for issues events.</p></li>
<li><p><strong>job_events</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Invoke the hook for job events.</p></li>
<li><p><strong>merge_requests_events</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Invoke the hook for merge requests.</p></li>
<li><p><strong>note_events</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Invoke the hook for notes events.</p></li>
<li><p><strong>pipeline_events</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Invoke the hook for pipeline events.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name or id of the project to add the hook to.</p></li>
<li><p><strong>push_events</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Invoke the hook for push events.</p></li>
<li><p><strong>tag_push_events</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Invoke the hook for tag push events.</p></li>
<li><p><strong>token</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A token to present when invoking the hook.</p></li>
<li><p><strong>url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The url of the hook to invoke.</p></li>
<li><p><strong>wiki_page_events</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Invoke the hook for wiki page events.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.ProjectHook.enable_ssl_verification">
<em class="property">property </em><code class="sig-name descname">enable_ssl_verification</code><a class="headerlink" href="#pulumi_gitlab.ProjectHook.enable_ssl_verification" title="Permalink to this definition">¶</a></dt>
<dd><p>Enable ssl verification when invoking
the hook.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.ProjectHook.issues_events">
<em class="property">property </em><code class="sig-name descname">issues_events</code><a class="headerlink" href="#pulumi_gitlab.ProjectHook.issues_events" title="Permalink to this definition">¶</a></dt>
<dd><p>Invoke the hook for issues events.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.ProjectHook.job_events">
<em class="property">property </em><code class="sig-name descname">job_events</code><a class="headerlink" href="#pulumi_gitlab.ProjectHook.job_events" title="Permalink to this definition">¶</a></dt>
<dd><p>Invoke the hook for job events.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.ProjectHook.merge_requests_events">
<em class="property">property </em><code class="sig-name descname">merge_requests_events</code><a class="headerlink" href="#pulumi_gitlab.ProjectHook.merge_requests_events" title="Permalink to this definition">¶</a></dt>
<dd><p>Invoke the hook for merge requests.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.ProjectHook.note_events">
<em class="property">property </em><code class="sig-name descname">note_events</code><a class="headerlink" href="#pulumi_gitlab.ProjectHook.note_events" title="Permalink to this definition">¶</a></dt>
<dd><p>Invoke the hook for notes events.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.ProjectHook.pipeline_events">
<em class="property">property </em><code class="sig-name descname">pipeline_events</code><a class="headerlink" href="#pulumi_gitlab.ProjectHook.pipeline_events" title="Permalink to this definition">¶</a></dt>
<dd><p>Invoke the hook for pipeline events.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.ProjectHook.project">
<em class="property">property </em><code class="sig-name descname">project</code><a class="headerlink" href="#pulumi_gitlab.ProjectHook.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The name or id of the project to add the hook to.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.ProjectHook.push_events">
<em class="property">property </em><code class="sig-name descname">push_events</code><a class="headerlink" href="#pulumi_gitlab.ProjectHook.push_events" title="Permalink to this definition">¶</a></dt>
<dd><p>Invoke the hook for push events.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.ProjectHook.tag_push_events">
<em class="property">property </em><code class="sig-name descname">tag_push_events</code><a class="headerlink" href="#pulumi_gitlab.ProjectHook.tag_push_events" title="Permalink to this definition">¶</a></dt>
<dd><p>Invoke the hook for tag push events.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.ProjectHook.token">
<em class="property">property </em><code class="sig-name descname">token</code><a class="headerlink" href="#pulumi_gitlab.ProjectHook.token" title="Permalink to this definition">¶</a></dt>
<dd><p>A token to present when invoking the hook.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.ProjectHook.url">
<em class="property">property </em><code class="sig-name descname">url</code><a class="headerlink" href="#pulumi_gitlab.ProjectHook.url" title="Permalink to this definition">¶</a></dt>
<dd><p>The url of the hook to invoke.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.ProjectHook.wiki_page_events">
<em class="property">property </em><code class="sig-name descname">wiki_page_events</code><a class="headerlink" href="#pulumi_gitlab.ProjectHook.wiki_page_events" title="Permalink to this definition">¶</a></dt>
<dd><p>Invoke the hook for wiki page events.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.ProjectHook.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gitlab.ProjectHook.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gitlab.ProjectHook.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gitlab.ProjectHook.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gitlab.ProjectLevelMrApprovals">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gitlab.</code><code class="sig-name descname">ProjectLevelMrApprovals</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">disable_overriding_approvers_per_merge_request</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">merge_requests_author_approval</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">merge_requests_disable_committers_approval</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">reset_approvals_on_push</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gitlab.ProjectLevelMrApprovals" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a ProjectLevelMrApprovals resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[bool] disable_overriding_approvers_per_merge_request: By default, users are able to edit the approval rules in merge requests. If set to true,</p>
<blockquote>
<div><p>the approval rules for all new merge requests will be determined by the default approval rules. Default is <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>merge_requests_author_approval</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Set to <code class="docutils literal notranslate"><span class="pre">true</span></code> if you want to allow merge request authors to self-approve merge requests. Authors
also need to be included in the approvers list in order to be able to approve their merge request. Default is <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>merge_requests_disable_committers_approval</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Set to <code class="docutils literal notranslate"><span class="pre">true</span></code> if you want to prevent approval of merge requests by merge request committers. Default is <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>project_id</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The ID of the project to change MR approval configuration.</p></li>
<li><p><strong>reset_approvals_on_push</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Set to <code class="docutils literal notranslate"><span class="pre">true</span></code> if you want to remove all approvals in a merge request when new commits are pushed to its source branch. Default is <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_gitlab.ProjectLevelMrApprovals.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">disable_overriding_approvers_per_merge_request</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">merge_requests_author_approval</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">merge_requests_disable_committers_approval</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">reset_approvals_on_push</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_gitlab.project_level_mr_approvals.ProjectLevelMrApprovals<a class="headerlink" href="#pulumi_gitlab.ProjectLevelMrApprovals.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ProjectLevelMrApprovals resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>disable_overriding_approvers_per_merge_request</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – By default, users are able to edit the approval rules in merge requests. If set to true,
the approval rules for all new merge requests will be determined by the default approval rules. Default is <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>merge_requests_author_approval</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Set to <code class="docutils literal notranslate"><span class="pre">true</span></code> if you want to allow merge request authors to self-approve merge requests. Authors
also need to be included in the approvers list in order to be able to approve their merge request. Default is <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>merge_requests_disable_committers_approval</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Set to <code class="docutils literal notranslate"><span class="pre">true</span></code> if you want to prevent approval of merge requests by merge request committers. Default is <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>project_id</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The ID of the project to change MR approval configuration.</p></li>
<li><p><strong>reset_approvals_on_push</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Set to <code class="docutils literal notranslate"><span class="pre">true</span></code> if you want to remove all approvals in a merge request when new commits are pushed to its source branch. Default is <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.ProjectLevelMrApprovals.disable_overriding_approvers_per_merge_request">
<em class="property">property </em><code class="sig-name descname">disable_overriding_approvers_per_merge_request</code><a class="headerlink" href="#pulumi_gitlab.ProjectLevelMrApprovals.disable_overriding_approvers_per_merge_request" title="Permalink to this definition">¶</a></dt>
<dd><p>By default, users are able to edit the approval rules in merge requests. If set to true,
the approval rules for all new merge requests will be determined by the default approval rules. Default is <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.ProjectLevelMrApprovals.merge_requests_author_approval">
<em class="property">property </em><code class="sig-name descname">merge_requests_author_approval</code><a class="headerlink" href="#pulumi_gitlab.ProjectLevelMrApprovals.merge_requests_author_approval" title="Permalink to this definition">¶</a></dt>
<dd><p>Set to <code class="docutils literal notranslate"><span class="pre">true</span></code> if you want to allow merge request authors to self-approve merge requests. Authors
also need to be included in the approvers list in order to be able to approve their merge request. Default is <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.ProjectLevelMrApprovals.merge_requests_disable_committers_approval">
<em class="property">property </em><code class="sig-name descname">merge_requests_disable_committers_approval</code><a class="headerlink" href="#pulumi_gitlab.ProjectLevelMrApprovals.merge_requests_disable_committers_approval" title="Permalink to this definition">¶</a></dt>
<dd><p>Set to <code class="docutils literal notranslate"><span class="pre">true</span></code> if you want to prevent approval of merge requests by merge request committers. Default is <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.ProjectLevelMrApprovals.project_id">
<em class="property">property </em><code class="sig-name descname">project_id</code><a class="headerlink" href="#pulumi_gitlab.ProjectLevelMrApprovals.project_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project to change MR approval configuration.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.ProjectLevelMrApprovals.reset_approvals_on_push">
<em class="property">property </em><code class="sig-name descname">reset_approvals_on_push</code><a class="headerlink" href="#pulumi_gitlab.ProjectLevelMrApprovals.reset_approvals_on_push" title="Permalink to this definition">¶</a></dt>
<dd><p>Set to <code class="docutils literal notranslate"><span class="pre">true</span></code> if you want to remove all approvals in a merge request when new commits are pushed to its source branch. Default is <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.ProjectLevelMrApprovals.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gitlab.ProjectLevelMrApprovals.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gitlab.ProjectLevelMrApprovals.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gitlab.ProjectLevelMrApprovals.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gitlab.ProjectMembership">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gitlab.</code><code class="sig-name descname">ProjectMembership</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">access_level</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_id</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gitlab.ProjectMembership" title="Permalink to this definition">¶</a></dt>
<dd><p>This resource allows you to add a current user to an existing project with a set access level.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_gitlab</span> <span class="k">as</span> <span class="nn">gitlab</span>

<span class="n">test</span> <span class="o">=</span> <span class="n">gitlab</span><span class="o">.</span><span class="n">ProjectMembership</span><span class="p">(</span><span class="s2">&quot;test&quot;</span><span class="p">,</span>
    <span class="n">access_level</span><span class="o">=</span><span class="s2">&quot;guest&quot;</span><span class="p">,</span>
    <span class="n">project_id</span><span class="o">=</span><span class="s2">&quot;12345&quot;</span><span class="p">,</span>
    <span class="n">user_id</span><span class="o">=</span><span class="mi">1337</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>access_level</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – One of five levels of access to the project.</p></li>
<li><p><strong>project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The id of the project.</p></li>
<li><p><strong>user_id</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The id of the user.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_gitlab.ProjectMembership.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">access_level</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_id</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_gitlab.project_membership.ProjectMembership<a class="headerlink" href="#pulumi_gitlab.ProjectMembership.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ProjectMembership resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>access_level</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – One of five levels of access to the project.</p></li>
<li><p><strong>project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The id of the project.</p></li>
<li><p><strong>user_id</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The id of the user.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.ProjectMembership.access_level">
<em class="property">property </em><code class="sig-name descname">access_level</code><a class="headerlink" href="#pulumi_gitlab.ProjectMembership.access_level" title="Permalink to this definition">¶</a></dt>
<dd><p>One of five levels of access to the project.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.ProjectMembership.project_id">
<em class="property">property </em><code class="sig-name descname">project_id</code><a class="headerlink" href="#pulumi_gitlab.ProjectMembership.project_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The id of the project.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.ProjectMembership.user_id">
<em class="property">property </em><code class="sig-name descname">user_id</code><a class="headerlink" href="#pulumi_gitlab.ProjectMembership.user_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The id of the user.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.ProjectMembership.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gitlab.ProjectMembership.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gitlab.ProjectMembership.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gitlab.ProjectMembership.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gitlab.ProjectMirror">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gitlab.</code><code class="sig-name descname">ProjectMirror</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">keep_divergent_refs</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">only_protected_branches</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">url</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gitlab.ProjectMirror" title="Permalink to this definition">¶</a></dt>
<dd><p>This resource allows you to add a mirror target for the repository, all changes will be synced to the remote target.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_gitlab</span> <span class="k">as</span> <span class="nn">gitlab</span>

<span class="n">foo</span> <span class="o">=</span> <span class="n">gitlab</span><span class="o">.</span><span class="n">ProjectMirror</span><span class="p">(</span><span class="s2">&quot;foo&quot;</span><span class="p">,</span>
    <span class="n">project</span><span class="o">=</span><span class="s2">&quot;1&quot;</span><span class="p">,</span>
    <span class="n">url</span><span class="o">=</span><span class="s2">&quot;https://username:password@github.com/org/repository.git&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Determines if the mirror is enabled.</p></li>
<li><p><strong>keep_divergent_refs</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Determines if divergent refs are skipped.</p></li>
<li><p><strong>only_protected_branches</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Determines if only protected branches are mirrored.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The id of the project.</p></li>
<li><p><strong>url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The URL of the remote repository to be mirrored.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_gitlab.ProjectMirror.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enabled</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">keep_divergent_refs</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">mirror_id</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">only_protected_branches</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">url</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_gitlab.project_mirror.ProjectMirror<a class="headerlink" href="#pulumi_gitlab.ProjectMirror.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ProjectMirror resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Determines if the mirror is enabled.</p></li>
<li><p><strong>keep_divergent_refs</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Determines if divergent refs are skipped.</p></li>
<li><p><strong>only_protected_branches</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Determines if only protected branches are mirrored.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The id of the project.</p></li>
<li><p><strong>url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The URL of the remote repository to be mirrored.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.ProjectMirror.enabled">
<em class="property">property </em><code class="sig-name descname">enabled</code><a class="headerlink" href="#pulumi_gitlab.ProjectMirror.enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Determines if the mirror is enabled.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.ProjectMirror.keep_divergent_refs">
<em class="property">property </em><code class="sig-name descname">keep_divergent_refs</code><a class="headerlink" href="#pulumi_gitlab.ProjectMirror.keep_divergent_refs" title="Permalink to this definition">¶</a></dt>
<dd><p>Determines if divergent refs are skipped.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.ProjectMirror.only_protected_branches">
<em class="property">property </em><code class="sig-name descname">only_protected_branches</code><a class="headerlink" href="#pulumi_gitlab.ProjectMirror.only_protected_branches" title="Permalink to this definition">¶</a></dt>
<dd><p>Determines if only protected branches are mirrored.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.ProjectMirror.project">
<em class="property">property </em><code class="sig-name descname">project</code><a class="headerlink" href="#pulumi_gitlab.ProjectMirror.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The id of the project.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.ProjectMirror.url">
<em class="property">property </em><code class="sig-name descname">url</code><a class="headerlink" href="#pulumi_gitlab.ProjectMirror.url" title="Permalink to this definition">¶</a></dt>
<dd><p>The URL of the remote repository to be mirrored.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.ProjectMirror.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gitlab.ProjectMirror.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gitlab.ProjectMirror.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gitlab.ProjectMirror.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gitlab.ProjectShareGroup">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gitlab.</code><code class="sig-name descname">ProjectShareGroup</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">access_level</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">group_id</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gitlab.ProjectShareGroup" title="Permalink to this definition">¶</a></dt>
<dd><p>This resource allows you to share a project with a group</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_gitlab</span> <span class="k">as</span> <span class="nn">gitlab</span>

<span class="n">test</span> <span class="o">=</span> <span class="n">gitlab</span><span class="o">.</span><span class="n">ProjectShareGroup</span><span class="p">(</span><span class="s2">&quot;test&quot;</span><span class="p">,</span>
    <span class="n">access_level</span><span class="o">=</span><span class="s2">&quot;guest&quot;</span><span class="p">,</span>
    <span class="n">group_id</span><span class="o">=</span><span class="mi">1337</span><span class="p">,</span>
    <span class="n">project_id</span><span class="o">=</span><span class="s2">&quot;12345&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>access_level</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – One of five levels of access to the project.</p></li>
<li><p><strong>group_id</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The id of the group.</p></li>
<li><p><strong>project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The id of the project.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_gitlab.ProjectShareGroup.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">access_level</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">group_id</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_gitlab.project_share_group.ProjectShareGroup<a class="headerlink" href="#pulumi_gitlab.ProjectShareGroup.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ProjectShareGroup resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>access_level</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – One of five levels of access to the project.</p></li>
<li><p><strong>group_id</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The id of the group.</p></li>
<li><p><strong>project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The id of the project.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.ProjectShareGroup.access_level">
<em class="property">property </em><code class="sig-name descname">access_level</code><a class="headerlink" href="#pulumi_gitlab.ProjectShareGroup.access_level" title="Permalink to this definition">¶</a></dt>
<dd><p>One of five levels of access to the project.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.ProjectShareGroup.group_id">
<em class="property">property </em><code class="sig-name descname">group_id</code><a class="headerlink" href="#pulumi_gitlab.ProjectShareGroup.group_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The id of the group.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.ProjectShareGroup.project_id">
<em class="property">property </em><code class="sig-name descname">project_id</code><a class="headerlink" href="#pulumi_gitlab.ProjectShareGroup.project_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The id of the project.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.ProjectShareGroup.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gitlab.ProjectShareGroup.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gitlab.ProjectShareGroup.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gitlab.ProjectShareGroup.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gitlab.ProjectVariable">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gitlab.</code><code class="sig-name descname">ProjectVariable</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">environment_scope</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">key</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">masked</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">protected</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">value</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">variable_type</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gitlab.ProjectVariable" title="Permalink to this definition">¶</a></dt>
<dd><p>This resource allows you to create and manage CI/CD variables for your GitLab projects.
For further information on variables, consult the <a class="reference external" href="https://docs.gitlab.com/ce/ci/variables/README.html#variables">gitlab
documentation</a>.</p>
<blockquote>
<div><p><strong>Important:</strong> If your GitLab version is older than 13.4, you may see nondeterministic behavior
when updating or deleting <code class="docutils literal notranslate"><span class="pre">ProjectVariable</span></code> resources with non-unique keys, for example if
there is another variable with the same key and different environment scope. See
<a class="reference external" href="https://gitlab.com/gitlab-org/gitlab/-/issues/9912">this GitLab issue</a>.</p>
</div></blockquote>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_gitlab</span> <span class="k">as</span> <span class="nn">gitlab</span>

<span class="n">example</span> <span class="o">=</span> <span class="n">gitlab</span><span class="o">.</span><span class="n">ProjectVariable</span><span class="p">(</span><span class="s2">&quot;example&quot;</span><span class="p">,</span>
    <span class="n">key</span><span class="o">=</span><span class="s2">&quot;project_variable_key&quot;</span><span class="p">,</span>
    <span class="n">project</span><span class="o">=</span><span class="s2">&quot;12345&quot;</span><span class="p">,</span>
    <span class="n">protected</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span>
    <span class="n">value</span><span class="o">=</span><span class="s2">&quot;project_variable_value&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>environment_scope</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The environment_scope of the variable. Defaults to <code class="docutils literal notranslate"><span class="pre">*</span></code>.</p></li>
<li><p><strong>key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the variable.</p></li>
<li><p><strong>masked</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If set to <code class="docutils literal notranslate"><span class="pre">true</span></code>, the variable will be masked if it would have been written to the logs. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name or id of the project to add the hook to.</p></li>
<li><p><strong>protected</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If set to <code class="docutils literal notranslate"><span class="pre">true</span></code>, the variable will be passed only to pipelines running on protected branches and tags. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>value</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The value of the variable.</p></li>
<li><p><strong>variable_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of a variable. Available types are: env_var (default) and file.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_gitlab.ProjectVariable.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">environment_scope</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">key</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">masked</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">protected</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">value</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">variable_type</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_gitlab.project_variable.ProjectVariable<a class="headerlink" href="#pulumi_gitlab.ProjectVariable.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ProjectVariable resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>environment_scope</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The environment_scope of the variable. Defaults to <code class="docutils literal notranslate"><span class="pre">*</span></code>.</p></li>
<li><p><strong>key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the variable.</p></li>
<li><p><strong>masked</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If set to <code class="docutils literal notranslate"><span class="pre">true</span></code>, the variable will be masked if it would have been written to the logs. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name or id of the project to add the hook to.</p></li>
<li><p><strong>protected</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If set to <code class="docutils literal notranslate"><span class="pre">true</span></code>, the variable will be passed only to pipelines running on protected branches and tags. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>value</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The value of the variable.</p></li>
<li><p><strong>variable_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The type of a variable. Available types are: env_var (default) and file.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.ProjectVariable.environment_scope">
<em class="property">property </em><code class="sig-name descname">environment_scope</code><a class="headerlink" href="#pulumi_gitlab.ProjectVariable.environment_scope" title="Permalink to this definition">¶</a></dt>
<dd><p>The environment_scope of the variable. Defaults to <code class="docutils literal notranslate"><span class="pre">*</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.ProjectVariable.key">
<em class="property">property </em><code class="sig-name descname">key</code><a class="headerlink" href="#pulumi_gitlab.ProjectVariable.key" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the variable.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.ProjectVariable.masked">
<em class="property">property </em><code class="sig-name descname">masked</code><a class="headerlink" href="#pulumi_gitlab.ProjectVariable.masked" title="Permalink to this definition">¶</a></dt>
<dd><p>If set to <code class="docutils literal notranslate"><span class="pre">true</span></code>, the variable will be masked if it would have been written to the logs. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.ProjectVariable.project">
<em class="property">property </em><code class="sig-name descname">project</code><a class="headerlink" href="#pulumi_gitlab.ProjectVariable.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The name or id of the project to add the hook to.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.ProjectVariable.protected">
<em class="property">property </em><code class="sig-name descname">protected</code><a class="headerlink" href="#pulumi_gitlab.ProjectVariable.protected" title="Permalink to this definition">¶</a></dt>
<dd><p>If set to <code class="docutils literal notranslate"><span class="pre">true</span></code>, the variable will be passed only to pipelines running on protected branches and tags. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.ProjectVariable.value">
<em class="property">property </em><code class="sig-name descname">value</code><a class="headerlink" href="#pulumi_gitlab.ProjectVariable.value" title="Permalink to this definition">¶</a></dt>
<dd><p>The value of the variable.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.ProjectVariable.variable_type">
<em class="property">property </em><code class="sig-name descname">variable_type</code><a class="headerlink" href="#pulumi_gitlab.ProjectVariable.variable_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of a variable. Available types are: env_var (default) and file.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.ProjectVariable.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gitlab.ProjectVariable.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gitlab.ProjectVariable.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gitlab.ProjectVariable.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gitlab.Provider">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gitlab.</code><code class="sig-name descname">Provider</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">base_url</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">cacert_file</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">client_cert</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">client_key</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">insecure</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">token</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gitlab.Provider" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider type for the gitlab package. By default, resources use package-wide configuration
settings, however an explicit <code class="docutils literal notranslate"><span class="pre">Provider</span></code> instance may be created and passed during resource
construction to achieve fine-grained programmatic control over provider settings. See the
<a class="reference external" href="https://www.pulumi.com/docs/reference/programming-model/#providers">documentation</a> for more information.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>base_url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The GitLab Base API URL</p></li>
<li><p><strong>cacert_file</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A file containing the ca certificate to use in case ssl certificate is not from a standard chain</p></li>
<li><p><strong>client_cert</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – File path to client certificate when GitLab instance is behind company proxy. File must contain PEM encoded data.</p></li>
<li><p><strong>client_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – File path to client key when GitLab instance is behind company proxy. File must contain PEM encoded data.</p></li>
<li><p><strong>insecure</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Disable SSL verification of API calls</p></li>
<li><p><strong>token</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The OAuth token used to connect to GitLab.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_gitlab.Provider.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gitlab.Provider.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gitlab.Provider.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gitlab.Provider.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gitlab.ServiceGithub">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gitlab.</code><code class="sig-name descname">ServiceGithub</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">repository_url</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">static_context</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">token</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gitlab.ServiceGithub" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a ServiceGithub resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] project: ID of the project you want to activate integration on.
:param pulumi.Input[bool] static_context: Append instance name instead of branch to the status. Must enable to set a GitLab status check as <em>required</em> in GitHub. See [Static / dynamic status check names] to learn more.
:param pulumi.Input[str] token: A GitHub personal access token with at least <code class="docutils literal notranslate"><span class="pre">repo:status</span></code> scope.</p>
<dl class="py method">
<dt id="pulumi_gitlab.ServiceGithub.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">active</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">created_at</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">repository_url</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">static_context</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">title</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">token</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">updated_at</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_gitlab.service_github.ServiceGithub<a class="headerlink" href="#pulumi_gitlab.ServiceGithub.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ServiceGithub resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – ID of the project you want to activate integration on.</p></li>
<li><p><strong>static_context</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Append instance name instead of branch to the status. Must enable to set a GitLab status check as <em>required</em> in GitHub. See [Static / dynamic status check names] to learn more.</p></li>
<li><p><strong>token</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A GitHub personal access token with at least <code class="docutils literal notranslate"><span class="pre">repo:status</span></code> scope.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.ServiceGithub.project">
<em class="property">property </em><code class="sig-name descname">project</code><a class="headerlink" href="#pulumi_gitlab.ServiceGithub.project" title="Permalink to this definition">¶</a></dt>
<dd><p>ID of the project you want to activate integration on.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.ServiceGithub.static_context">
<em class="property">property </em><code class="sig-name descname">static_context</code><a class="headerlink" href="#pulumi_gitlab.ServiceGithub.static_context" title="Permalink to this definition">¶</a></dt>
<dd><p>Append instance name instead of branch to the status. Must enable to set a GitLab status check as <em>required</em> in GitHub. See [Static / dynamic status check names] to learn more.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.ServiceGithub.token">
<em class="property">property </em><code class="sig-name descname">token</code><a class="headerlink" href="#pulumi_gitlab.ServiceGithub.token" title="Permalink to this definition">¶</a></dt>
<dd><p>A GitHub personal access token with at least <code class="docutils literal notranslate"><span class="pre">repo:status</span></code> scope.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.ServiceGithub.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gitlab.ServiceGithub.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gitlab.ServiceGithub.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gitlab.ServiceGithub.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gitlab.ServiceJira">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gitlab.</code><code class="sig-name descname">ServiceJira</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">comment_on_event_enabled</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">commit_events</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">jira_issue_transition_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">merge_requests_events</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">password</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_key</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">url</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">username</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gitlab.ServiceJira" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a ServiceJira resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[bool] comment_on_event_enabled: Enable comments inside Jira issues on each GitLab event (commit / merge request)
:param pulumi.Input[bool] commit_events: Enable notifications for commit events
:param pulumi.Input[str] jira_issue_transition_id: The ID of a transition that moves issues to a closed state. You can find this number under the JIRA workflow administration (Administration &gt; Issues &gt; Workflows) by selecting View under Operations of the desired workflow of your project. By default, this ID is set to 2.
:param pulumi.Input[bool] merge_requests_events: Enable notifications for merge request events
:param pulumi.Input[str] password: The password of the user created to be used with GitLab/JIRA.
:param pulumi.Input[str] project: ID of the project you want to activate integration on.
:param pulumi.Input[str] project_key: The short identifier for your JIRA project, all uppercase, e.g., PROJ.
:param pulumi.Input[str] url: The URL to the JIRA project which is being linked to this GitLab project. For example, <a class="reference external" href="https://jira.example.com">https://jira.example.com</a>.
:param pulumi.Input[str] username: The username of the user created to be used with GitLab/JIRA.</p>
<dl class="py method">
<dt id="pulumi_gitlab.ServiceJira.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">active</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">comment_on_event_enabled</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">commit_events</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">created_at</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">jira_issue_transition_id</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">merge_requests_events</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">password</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_key</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">title</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">updated_at</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">url</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">username</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_gitlab.service_jira.ServiceJira<a class="headerlink" href="#pulumi_gitlab.ServiceJira.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ServiceJira resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>comment_on_event_enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enable comments inside Jira issues on each GitLab event (commit / merge request)</p></li>
<li><p><strong>commit_events</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enable notifications for commit events</p></li>
<li><p><strong>jira_issue_transition_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of a transition that moves issues to a closed state. You can find this number under the JIRA workflow administration (Administration &gt; Issues &gt; Workflows) by selecting View under Operations of the desired workflow of your project. By default, this ID is set to 2.</p></li>
<li><p><strong>merge_requests_events</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enable notifications for merge request events</p></li>
<li><p><strong>password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The password of the user created to be used with GitLab/JIRA.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – ID of the project you want to activate integration on.</p></li>
<li><p><strong>project_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The short identifier for your JIRA project, all uppercase, e.g., PROJ.</p></li>
<li><p><strong>url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The URL to the JIRA project which is being linked to this GitLab project. For example, <a class="reference external" href="https://jira.example.com">https://jira.example.com</a>.</p></li>
<li><p><strong>username</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The username of the user created to be used with GitLab/JIRA.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.ServiceJira.comment_on_event_enabled">
<em class="property">property </em><code class="sig-name descname">comment_on_event_enabled</code><a class="headerlink" href="#pulumi_gitlab.ServiceJira.comment_on_event_enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Enable comments inside Jira issues on each GitLab event (commit / merge request)</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.ServiceJira.commit_events">
<em class="property">property </em><code class="sig-name descname">commit_events</code><a class="headerlink" href="#pulumi_gitlab.ServiceJira.commit_events" title="Permalink to this definition">¶</a></dt>
<dd><p>Enable notifications for commit events</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.ServiceJira.jira_issue_transition_id">
<em class="property">property </em><code class="sig-name descname">jira_issue_transition_id</code><a class="headerlink" href="#pulumi_gitlab.ServiceJira.jira_issue_transition_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of a transition that moves issues to a closed state. You can find this number under the JIRA workflow administration (Administration &gt; Issues &gt; Workflows) by selecting View under Operations of the desired workflow of your project. By default, this ID is set to 2.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.ServiceJira.merge_requests_events">
<em class="property">property </em><code class="sig-name descname">merge_requests_events</code><a class="headerlink" href="#pulumi_gitlab.ServiceJira.merge_requests_events" title="Permalink to this definition">¶</a></dt>
<dd><p>Enable notifications for merge request events</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.ServiceJira.password">
<em class="property">property </em><code class="sig-name descname">password</code><a class="headerlink" href="#pulumi_gitlab.ServiceJira.password" title="Permalink to this definition">¶</a></dt>
<dd><p>The password of the user created to be used with GitLab/JIRA.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.ServiceJira.project">
<em class="property">property </em><code class="sig-name descname">project</code><a class="headerlink" href="#pulumi_gitlab.ServiceJira.project" title="Permalink to this definition">¶</a></dt>
<dd><p>ID of the project you want to activate integration on.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.ServiceJira.project_key">
<em class="property">property </em><code class="sig-name descname">project_key</code><a class="headerlink" href="#pulumi_gitlab.ServiceJira.project_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The short identifier for your JIRA project, all uppercase, e.g., PROJ.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.ServiceJira.url">
<em class="property">property </em><code class="sig-name descname">url</code><a class="headerlink" href="#pulumi_gitlab.ServiceJira.url" title="Permalink to this definition">¶</a></dt>
<dd><p>The URL to the JIRA project which is being linked to this GitLab project. For example, <a class="reference external" href="https://jira.example.com">https://jira.example.com</a>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.ServiceJira.username">
<em class="property">property </em><code class="sig-name descname">username</code><a class="headerlink" href="#pulumi_gitlab.ServiceJira.username" title="Permalink to this definition">¶</a></dt>
<dd><p>The username of the user created to be used with GitLab/JIRA.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.ServiceJira.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gitlab.ServiceJira.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gitlab.ServiceJira.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gitlab.ServiceJira.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gitlab.ServicePipelinesEmail">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gitlab.</code><code class="sig-name descname">ServicePipelinesEmail</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">branches_to_be_notified</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">notify_only_broken_pipelines</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">recipients</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gitlab.ServicePipelinesEmail" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a ServicePipelinesEmail resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] branches_to_be_notified: Branches to send notifications for. Valid options are <code class="docutils literal notranslate"><span class="pre">all</span></code>, <code class="docutils literal notranslate"><span class="pre">default</span></code>, <code class="docutils literal notranslate"><span class="pre">protected</span></code>, and <code class="docutils literal notranslate"><span class="pre">default_and_protected</span></code>. Default is <code class="docutils literal notranslate"><span class="pre">default</span></code>
:param pulumi.Input[bool] notify_only_broken_pipelines: Notify only broken pipelines. Default is true.
:param pulumi.Input[str] project: ID of the project you want to activate integration on.
:param pulumi.Input[Sequence[pulumi.Input[str]]] recipients: ) email addresses where notifications are sent.</p>
<dl class="py method">
<dt id="pulumi_gitlab.ServicePipelinesEmail.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">branches_to_be_notified</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">notify_only_broken_pipelines</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">recipients</span><span class="p">:</span> <span class="n">Union[Sequence[Union[str, Awaitable[str], Output[T]]], Awaitable[Sequence[Union[str, Awaitable[str], Output[T]]]], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_gitlab.service_pipelines_email.ServicePipelinesEmail<a class="headerlink" href="#pulumi_gitlab.ServicePipelinesEmail.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ServicePipelinesEmail resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>branches_to_be_notified</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Branches to send notifications for. Valid options are <code class="docutils literal notranslate"><span class="pre">all</span></code>, <code class="docutils literal notranslate"><span class="pre">default</span></code>, <code class="docutils literal notranslate"><span class="pre">protected</span></code>, and <code class="docutils literal notranslate"><span class="pre">default_and_protected</span></code>. Default is <code class="docutils literal notranslate"><span class="pre">default</span></code></p></li>
<li><p><strong>notify_only_broken_pipelines</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Notify only broken pipelines. Default is true.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – ID of the project you want to activate integration on.</p></li>
<li><p><strong>recipients</strong> (<em>pulumi.Input</em><em>[</em><em>Sequence</em><em>[</em><em>pulumi.Input</em><em>[</em><em>str</em><em>]</em><em>]</em><em>]</em>) – ) email addresses where notifications are sent.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.ServicePipelinesEmail.branches_to_be_notified">
<em class="property">property </em><code class="sig-name descname">branches_to_be_notified</code><a class="headerlink" href="#pulumi_gitlab.ServicePipelinesEmail.branches_to_be_notified" title="Permalink to this definition">¶</a></dt>
<dd><p>Branches to send notifications for. Valid options are <code class="docutils literal notranslate"><span class="pre">all</span></code>, <code class="docutils literal notranslate"><span class="pre">default</span></code>, <code class="docutils literal notranslate"><span class="pre">protected</span></code>, and <code class="docutils literal notranslate"><span class="pre">default_and_protected</span></code>. Default is <code class="docutils literal notranslate"><span class="pre">default</span></code></p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.ServicePipelinesEmail.notify_only_broken_pipelines">
<em class="property">property </em><code class="sig-name descname">notify_only_broken_pipelines</code><a class="headerlink" href="#pulumi_gitlab.ServicePipelinesEmail.notify_only_broken_pipelines" title="Permalink to this definition">¶</a></dt>
<dd><p>Notify only broken pipelines. Default is true.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.ServicePipelinesEmail.project">
<em class="property">property </em><code class="sig-name descname">project</code><a class="headerlink" href="#pulumi_gitlab.ServicePipelinesEmail.project" title="Permalink to this definition">¶</a></dt>
<dd><p>ID of the project you want to activate integration on.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.ServicePipelinesEmail.recipients">
<em class="property">property </em><code class="sig-name descname">recipients</code><a class="headerlink" href="#pulumi_gitlab.ServicePipelinesEmail.recipients" title="Permalink to this definition">¶</a></dt>
<dd><p>) email addresses where notifications are sent.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.ServicePipelinesEmail.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gitlab.ServicePipelinesEmail.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gitlab.ServicePipelinesEmail.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gitlab.ServicePipelinesEmail.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gitlab.ServiceSlack">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gitlab.</code><code class="sig-name descname">ServiceSlack</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">branches_to_be_notified</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">confidential_issue_channel</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">confidential_issues_events</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">confidential_note_events</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">issue_channel</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">issues_events</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">merge_request_channel</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">merge_requests_events</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">note_channel</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">note_events</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">notify_only_broken_pipelines</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">notify_only_default_branch</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">pipeline_channel</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">pipeline_events</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">push_channel</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">push_events</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tag_push_channel</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tag_push_events</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">username</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">webhook</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">wiki_page_channel</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">wiki_page_events</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gitlab.ServiceSlack" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a ServiceSlack resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] branches_to_be_notified: Branches to send notifications for. Valid options are “all”, “default”, “protected”, and “default_and_protected”.
:param pulumi.Input[str] confidential_issue_channel: The name of the channel to receive confidential issue events notifications.
:param pulumi.Input[bool] confidential_issues_events: Enable notifications for confidential issues events.
:param pulumi.Input[bool] confidential_note_events: Enable notifications for confidential note events.
:param pulumi.Input[str] issue_channel: The name of the channel to receive issue events notifications.
:param pulumi.Input[bool] issues_events: Enable notifications for issues events.
:param pulumi.Input[str] merge_request_channel: The name of the channel to receive merge request events notifications.
:param pulumi.Input[bool] merge_requests_events: Enable notifications for merge requests events.
:param pulumi.Input[str] note_channel: The name of the channel to receive note events notifications.
:param pulumi.Input[bool] note_events: Enable notifications for note events.
:param pulumi.Input[bool] notify_only_broken_pipelines: Send notifications for broken pipelines.
:param pulumi.Input[bool] notify_only_default_branch: DEPRECATED: This parameter has been replaced with <code class="docutils literal notranslate"><span class="pre">branches_to_be_notified</span></code>.
:param pulumi.Input[str] pipeline_channel: The name of the channel to receive pipeline events notifications.
:param pulumi.Input[bool] pipeline_events: Enable notifications for pipeline events.
:param pulumi.Input[str] project: ID of the project you want to activate integration on.
:param pulumi.Input[str] push_channel: The name of the channel to receive push events notifications.
:param pulumi.Input[bool] push_events: Enable notifications for push events.
:param pulumi.Input[str] tag_push_channel: The name of the channel to receive tag push events notifications.
:param pulumi.Input[bool] tag_push_events: Enable notifications for tag push events.
:param pulumi.Input[str] username: Username to use.
:param pulumi.Input[str] webhook: Webhook URL (ex.: <a class="reference external" href="https://hooks.slack.com/services/">https://hooks.slack.com/services/</a>…)
:param pulumi.Input[str] wiki_page_channel: The name of the channel to receive wiki page events notifications.
:param pulumi.Input[bool] wiki_page_events: Enable notifications for wiki page events.</p>
<dl class="py method">
<dt id="pulumi_gitlab.ServiceSlack.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">branches_to_be_notified</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">confidential_issue_channel</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">confidential_issues_events</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">confidential_note_events</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">issue_channel</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">issues_events</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">job_events</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">merge_request_channel</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">merge_requests_events</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">note_channel</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">note_events</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">notify_only_broken_pipelines</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">notify_only_default_branch</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">pipeline_channel</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">pipeline_events</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">push_channel</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">push_events</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tag_push_channel</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tag_push_events</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">username</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">webhook</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">wiki_page_channel</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">wiki_page_events</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_gitlab.service_slack.ServiceSlack<a class="headerlink" href="#pulumi_gitlab.ServiceSlack.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ServiceSlack resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>branches_to_be_notified</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Branches to send notifications for. Valid options are “all”, “default”, “protected”, and “default_and_protected”.</p></li>
<li><p><strong>confidential_issue_channel</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the channel to receive confidential issue events notifications.</p></li>
<li><p><strong>confidential_issues_events</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enable notifications for confidential issues events.</p></li>
<li><p><strong>confidential_note_events</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enable notifications for confidential note events.</p></li>
<li><p><strong>issue_channel</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the channel to receive issue events notifications.</p></li>
<li><p><strong>issues_events</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enable notifications for issues events.</p></li>
<li><p><strong>merge_request_channel</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the channel to receive merge request events notifications.</p></li>
<li><p><strong>merge_requests_events</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enable notifications for merge requests events.</p></li>
<li><p><strong>note_channel</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the channel to receive note events notifications.</p></li>
<li><p><strong>note_events</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enable notifications for note events.</p></li>
<li><p><strong>notify_only_broken_pipelines</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Send notifications for broken pipelines.</p></li>
<li><p><strong>notify_only_default_branch</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – DEPRECATED: This parameter has been replaced with <code class="docutils literal notranslate"><span class="pre">branches_to_be_notified</span></code>.</p></li>
<li><p><strong>pipeline_channel</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the channel to receive pipeline events notifications.</p></li>
<li><p><strong>pipeline_events</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enable notifications for pipeline events.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – ID of the project you want to activate integration on.</p></li>
<li><p><strong>push_channel</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the channel to receive push events notifications.</p></li>
<li><p><strong>push_events</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enable notifications for push events.</p></li>
<li><p><strong>tag_push_channel</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the channel to receive tag push events notifications.</p></li>
<li><p><strong>tag_push_events</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enable notifications for tag push events.</p></li>
<li><p><strong>username</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Username to use.</p></li>
<li><p><strong>webhook</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Webhook URL (ex.: <a class="reference external" href="https://hooks.slack.com/services/">https://hooks.slack.com/services/</a>…)</p></li>
<li><p><strong>wiki_page_channel</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the channel to receive wiki page events notifications.</p></li>
<li><p><strong>wiki_page_events</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enable notifications for wiki page events.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.ServiceSlack.branches_to_be_notified">
<em class="property">property </em><code class="sig-name descname">branches_to_be_notified</code><a class="headerlink" href="#pulumi_gitlab.ServiceSlack.branches_to_be_notified" title="Permalink to this definition">¶</a></dt>
<dd><p>Branches to send notifications for. Valid options are “all”, “default”, “protected”, and “default_and_protected”.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.ServiceSlack.confidential_issue_channel">
<em class="property">property </em><code class="sig-name descname">confidential_issue_channel</code><a class="headerlink" href="#pulumi_gitlab.ServiceSlack.confidential_issue_channel" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the channel to receive confidential issue events notifications.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.ServiceSlack.confidential_issues_events">
<em class="property">property </em><code class="sig-name descname">confidential_issues_events</code><a class="headerlink" href="#pulumi_gitlab.ServiceSlack.confidential_issues_events" title="Permalink to this definition">¶</a></dt>
<dd><p>Enable notifications for confidential issues events.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.ServiceSlack.confidential_note_events">
<em class="property">property </em><code class="sig-name descname">confidential_note_events</code><a class="headerlink" href="#pulumi_gitlab.ServiceSlack.confidential_note_events" title="Permalink to this definition">¶</a></dt>
<dd><p>Enable notifications for confidential note events.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.ServiceSlack.issue_channel">
<em class="property">property </em><code class="sig-name descname">issue_channel</code><a class="headerlink" href="#pulumi_gitlab.ServiceSlack.issue_channel" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the channel to receive issue events notifications.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.ServiceSlack.issues_events">
<em class="property">property </em><code class="sig-name descname">issues_events</code><a class="headerlink" href="#pulumi_gitlab.ServiceSlack.issues_events" title="Permalink to this definition">¶</a></dt>
<dd><p>Enable notifications for issues events.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.ServiceSlack.merge_request_channel">
<em class="property">property </em><code class="sig-name descname">merge_request_channel</code><a class="headerlink" href="#pulumi_gitlab.ServiceSlack.merge_request_channel" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the channel to receive merge request events notifications.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.ServiceSlack.merge_requests_events">
<em class="property">property </em><code class="sig-name descname">merge_requests_events</code><a class="headerlink" href="#pulumi_gitlab.ServiceSlack.merge_requests_events" title="Permalink to this definition">¶</a></dt>
<dd><p>Enable notifications for merge requests events.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.ServiceSlack.note_channel">
<em class="property">property </em><code class="sig-name descname">note_channel</code><a class="headerlink" href="#pulumi_gitlab.ServiceSlack.note_channel" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the channel to receive note events notifications.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.ServiceSlack.note_events">
<em class="property">property </em><code class="sig-name descname">note_events</code><a class="headerlink" href="#pulumi_gitlab.ServiceSlack.note_events" title="Permalink to this definition">¶</a></dt>
<dd><p>Enable notifications for note events.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.ServiceSlack.notify_only_broken_pipelines">
<em class="property">property </em><code class="sig-name descname">notify_only_broken_pipelines</code><a class="headerlink" href="#pulumi_gitlab.ServiceSlack.notify_only_broken_pipelines" title="Permalink to this definition">¶</a></dt>
<dd><p>Send notifications for broken pipelines.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.ServiceSlack.notify_only_default_branch">
<em class="property">property </em><code class="sig-name descname">notify_only_default_branch</code><a class="headerlink" href="#pulumi_gitlab.ServiceSlack.notify_only_default_branch" title="Permalink to this definition">¶</a></dt>
<dd><p>DEPRECATED: This parameter has been replaced with <code class="docutils literal notranslate"><span class="pre">branches_to_be_notified</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.ServiceSlack.pipeline_channel">
<em class="property">property </em><code class="sig-name descname">pipeline_channel</code><a class="headerlink" href="#pulumi_gitlab.ServiceSlack.pipeline_channel" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the channel to receive pipeline events notifications.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.ServiceSlack.pipeline_events">
<em class="property">property </em><code class="sig-name descname">pipeline_events</code><a class="headerlink" href="#pulumi_gitlab.ServiceSlack.pipeline_events" title="Permalink to this definition">¶</a></dt>
<dd><p>Enable notifications for pipeline events.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.ServiceSlack.project">
<em class="property">property </em><code class="sig-name descname">project</code><a class="headerlink" href="#pulumi_gitlab.ServiceSlack.project" title="Permalink to this definition">¶</a></dt>
<dd><p>ID of the project you want to activate integration on.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.ServiceSlack.push_channel">
<em class="property">property </em><code class="sig-name descname">push_channel</code><a class="headerlink" href="#pulumi_gitlab.ServiceSlack.push_channel" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the channel to receive push events notifications.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.ServiceSlack.push_events">
<em class="property">property </em><code class="sig-name descname">push_events</code><a class="headerlink" href="#pulumi_gitlab.ServiceSlack.push_events" title="Permalink to this definition">¶</a></dt>
<dd><p>Enable notifications for push events.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.ServiceSlack.tag_push_channel">
<em class="property">property </em><code class="sig-name descname">tag_push_channel</code><a class="headerlink" href="#pulumi_gitlab.ServiceSlack.tag_push_channel" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the channel to receive tag push events notifications.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.ServiceSlack.tag_push_events">
<em class="property">property </em><code class="sig-name descname">tag_push_events</code><a class="headerlink" href="#pulumi_gitlab.ServiceSlack.tag_push_events" title="Permalink to this definition">¶</a></dt>
<dd><p>Enable notifications for tag push events.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.ServiceSlack.username">
<em class="property">property </em><code class="sig-name descname">username</code><a class="headerlink" href="#pulumi_gitlab.ServiceSlack.username" title="Permalink to this definition">¶</a></dt>
<dd><p>Username to use.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.ServiceSlack.webhook">
<em class="property">property </em><code class="sig-name descname">webhook</code><a class="headerlink" href="#pulumi_gitlab.ServiceSlack.webhook" title="Permalink to this definition">¶</a></dt>
<dd><p>Webhook URL (ex.: <a class="reference external" href="https://hooks.slack.com/services/">https://hooks.slack.com/services/</a>…)</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.ServiceSlack.wiki_page_channel">
<em class="property">property </em><code class="sig-name descname">wiki_page_channel</code><a class="headerlink" href="#pulumi_gitlab.ServiceSlack.wiki_page_channel" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the channel to receive wiki page events notifications.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.ServiceSlack.wiki_page_events">
<em class="property">property </em><code class="sig-name descname">wiki_page_events</code><a class="headerlink" href="#pulumi_gitlab.ServiceSlack.wiki_page_events" title="Permalink to this definition">¶</a></dt>
<dd><p>Enable notifications for wiki page events.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.ServiceSlack.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gitlab.ServiceSlack.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gitlab.ServiceSlack.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gitlab.ServiceSlack.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gitlab.TagProtection">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gitlab.</code><code class="sig-name descname">TagProtection</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">create_access_level</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tag</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gitlab.TagProtection" title="Permalink to this definition">¶</a></dt>
<dd><p>This resource allows you to protect a specific tag or wildcard by an access level so that the user with less access level cannot Create the tags.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_gitlab</span> <span class="k">as</span> <span class="nn">gitlab</span>

<span class="n">tag_protect</span> <span class="o">=</span> <span class="n">gitlab</span><span class="o">.</span><span class="n">TagProtection</span><span class="p">(</span><span class="s2">&quot;tagProtect&quot;</span><span class="p">,</span>
    <span class="n">create_access_level</span><span class="o">=</span><span class="s2">&quot;developer&quot;</span><span class="p">,</span>
    <span class="n">project</span><span class="o">=</span><span class="s2">&quot;12345&quot;</span><span class="p">,</span>
    <span class="n">tag</span><span class="o">=</span><span class="s2">&quot;TagProtected&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>create_access_level</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – One of five levels of access to the project.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The id of the project.</p></li>
<li><p><strong>tag</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the tag or wildcard.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_gitlab.TagProtection.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">create_access_level</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tag</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_gitlab.tag_protection.TagProtection<a class="headerlink" href="#pulumi_gitlab.TagProtection.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing TagProtection resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>create_access_level</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – One of five levels of access to the project.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The id of the project.</p></li>
<li><p><strong>tag</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the tag or wildcard.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.TagProtection.create_access_level">
<em class="property">property </em><code class="sig-name descname">create_access_level</code><a class="headerlink" href="#pulumi_gitlab.TagProtection.create_access_level" title="Permalink to this definition">¶</a></dt>
<dd><p>One of five levels of access to the project.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.TagProtection.project">
<em class="property">property </em><code class="sig-name descname">project</code><a class="headerlink" href="#pulumi_gitlab.TagProtection.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The id of the project.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.TagProtection.tag">
<em class="property">property </em><code class="sig-name descname">tag</code><a class="headerlink" href="#pulumi_gitlab.TagProtection.tag" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the tag or wildcard.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.TagProtection.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gitlab.TagProtection.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gitlab.TagProtection.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gitlab.TagProtection.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gitlab.User">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gitlab.</code><code class="sig-name descname">User</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">can_create_group</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">email</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">is_admin</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">is_external</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">password</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">projects_limit</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">reset_password</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">skip_confirmation</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">username</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gitlab.User" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a User resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[bool] can_create_group: Boolean, defaults to false. Whether to allow the user to create groups.
:param pulumi.Input[str] email: The e-mail address of the user.
:param pulumi.Input[bool] is_admin: Boolean, defaults to false.  Whether to enable administrative priviledges</p>
<blockquote>
<div><p>for the user.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>is_external</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean, defaults to false. Whether a user has access only to some internal or private projects. External users can only access projects to which they are explicitly granted access.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the user.</p></li>
<li><p><strong>password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The password of the user.</p></li>
<li><p><strong>projects_limit</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Integer, defaults to 0.  Number of projects user can create.</p></li>
<li><p><strong>reset_password</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean, defaults to false. Send user password reset link.</p></li>
<li><p><strong>skip_confirmation</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean, defaults to true. Whether to skip confirmation.</p></li>
<li><p><strong>username</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The username of the user.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_gitlab.User.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span><span class="p">:</span> <span class="n">str</span></em>, <em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Union<span class="p">[</span>str<span class="p">, </span>Awaitable<span class="p">[</span>str<span class="p">]</span><span class="p">, </span>Output<span class="p">[</span>T<span class="p">]</span><span class="p">]</span></span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.resource.ResourceOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">can_create_group</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">email</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">is_admin</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">is_external</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">password</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">projects_limit</span><span class="p">:</span> <span class="n">Union[int, Awaitable[int], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">reset_password</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">skip_confirmation</span><span class="p">:</span> <span class="n">Union[bool, Awaitable[bool], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">username</span><span class="p">:</span> <span class="n">Union[str, Awaitable[str], Output[T], None]</span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_gitlab.user.User<a class="headerlink" href="#pulumi_gitlab.User.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing User resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>can_create_group</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean, defaults to false. Whether to allow the user to create groups.</p></li>
<li><p><strong>email</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The e-mail address of the user.</p></li>
<li><p><strong>is_admin</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean, defaults to false.  Whether to enable administrative priviledges
for the user.</p></li>
<li><p><strong>is_external</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean, defaults to false. Whether a user has access only to some internal or private projects. External users can only access projects to which they are explicitly granted access.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the user.</p></li>
<li><p><strong>password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The password of the user.</p></li>
<li><p><strong>projects_limit</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Integer, defaults to 0.  Number of projects user can create.</p></li>
<li><p><strong>reset_password</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean, defaults to false. Send user password reset link.</p></li>
<li><p><strong>skip_confirmation</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean, defaults to true. Whether to skip confirmation.</p></li>
<li><p><strong>username</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The username of the user.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.User.can_create_group">
<em class="property">property </em><code class="sig-name descname">can_create_group</code><a class="headerlink" href="#pulumi_gitlab.User.can_create_group" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean, defaults to false. Whether to allow the user to create groups.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.User.email">
<em class="property">property </em><code class="sig-name descname">email</code><a class="headerlink" href="#pulumi_gitlab.User.email" title="Permalink to this definition">¶</a></dt>
<dd><p>The e-mail address of the user.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.User.is_admin">
<em class="property">property </em><code class="sig-name descname">is_admin</code><a class="headerlink" href="#pulumi_gitlab.User.is_admin" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean, defaults to false.  Whether to enable administrative priviledges
for the user.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.User.is_external">
<em class="property">property </em><code class="sig-name descname">is_external</code><a class="headerlink" href="#pulumi_gitlab.User.is_external" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean, defaults to false. Whether a user has access only to some internal or private projects. External users can only access projects to which they are explicitly granted access.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.User.name">
<em class="property">property </em><code class="sig-name descname">name</code><a class="headerlink" href="#pulumi_gitlab.User.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the user.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.User.password">
<em class="property">property </em><code class="sig-name descname">password</code><a class="headerlink" href="#pulumi_gitlab.User.password" title="Permalink to this definition">¶</a></dt>
<dd><p>The password of the user.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.User.projects_limit">
<em class="property">property </em><code class="sig-name descname">projects_limit</code><a class="headerlink" href="#pulumi_gitlab.User.projects_limit" title="Permalink to this definition">¶</a></dt>
<dd><p>Integer, defaults to 0.  Number of projects user can create.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.User.reset_password">
<em class="property">property </em><code class="sig-name descname">reset_password</code><a class="headerlink" href="#pulumi_gitlab.User.reset_password" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean, defaults to false. Send user password reset link.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.User.skip_confirmation">
<em class="property">property </em><code class="sig-name descname">skip_confirmation</code><a class="headerlink" href="#pulumi_gitlab.User.skip_confirmation" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean, defaults to true. Whether to skip confirmation.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.User.username">
<em class="property">property </em><code class="sig-name descname">username</code><a class="headerlink" href="#pulumi_gitlab.User.username" title="Permalink to this definition">¶</a></dt>
<dd><p>The username of the user.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_gitlab.User.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gitlab.User.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gitlab.User.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gitlab.User.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gitlab.get_group">
<code class="sig-prename descclassname">pulumi_gitlab.</code><code class="sig-name descname">get_group</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">full_path</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">group_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>int<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_gitlab.get_group.AwaitableGetGroupResult<a class="headerlink" href="#pulumi_gitlab.get_group" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides details about a specific group in the gitlab provider.</p>
<p><strong>By group’s ID</strong></p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_gitlab</span> <span class="k">as</span> <span class="nn">gitlab</span>

<span class="n">foo</span> <span class="o">=</span> <span class="n">gitlab</span><span class="o">.</span><span class="n">get_group</span><span class="p">(</span><span class="n">group_id</span><span class="o">=</span><span class="mi">123</span><span class="p">)</span>
</pre></div>
</div>
<p><strong>By group’s full path</strong></p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_gitlab</span> <span class="k">as</span> <span class="nn">gitlab</span>

<span class="n">foo</span> <span class="o">=</span> <span class="n">gitlab</span><span class="o">.</span><span class="n">get_group</span><span class="p">(</span><span class="n">full_path</span><span class="o">=</span><span class="s2">&quot;foo/bar&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>full_path</strong> (<em>str</em>) – The full path of the group.</p></li>
<li><p><strong>group_id</strong> (<em>int</em>) – The ID of the group.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_gitlab.get_group_membership">
<code class="sig-prename descclassname">pulumi_gitlab.</code><code class="sig-name descname">get_group_membership</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">access_level</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">full_path</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">group_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>int<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_gitlab.get_group_membership.AwaitableGetGroupMembershipResult<a class="headerlink" href="#pulumi_gitlab.get_group_membership" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides details about a list of group members in the gitlab provider. The results include id, username, name and more about the requested members.</p>
<p><strong>By group’s ID</strong></p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_gitlab</span> <span class="k">as</span> <span class="nn">gitlab</span>

<span class="n">example</span> <span class="o">=</span> <span class="n">gitlab</span><span class="o">.</span><span class="n">get_group_membership</span><span class="p">(</span><span class="n">group_id</span><span class="o">=</span><span class="mi">123</span><span class="p">)</span>
</pre></div>
</div>
<p><strong>By group’s full path</strong></p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_gitlab</span> <span class="k">as</span> <span class="nn">gitlab</span>

<span class="n">example</span> <span class="o">=</span> <span class="n">gitlab</span><span class="o">.</span><span class="n">get_group_membership</span><span class="p">(</span><span class="n">full_path</span><span class="o">=</span><span class="s2">&quot;foo/bar&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>access_level</strong> (<em>str</em>) – Only return members with the desidered access level. Acceptable values are: <code class="docutils literal notranslate"><span class="pre">guest</span></code>, <code class="docutils literal notranslate"><span class="pre">reporter</span></code>, <code class="docutils literal notranslate"><span class="pre">developer</span></code>, <code class="docutils literal notranslate"><span class="pre">maintainer</span></code>, <code class="docutils literal notranslate"><span class="pre">owner</span></code>.</p></li>
<li><p><strong>full_path</strong> (<em>str</em>) – The full path of the group.</p></li>
<li><p><strong>group_id</strong> (<em>int</em>) – The ID of the group.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_gitlab.get_project">
<code class="sig-prename descclassname">pulumi_gitlab.</code><code class="sig-name descname">get_project</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>int<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_gitlab.get_project.AwaitableGetProjectResult<a class="headerlink" href="#pulumi_gitlab.get_project" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides details about a specific project in the gitlab provider. The results include the name of the project, path, description, default branch, etc.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_gitlab</span> <span class="k">as</span> <span class="nn">gitlab</span>

<span class="n">example</span> <span class="o">=</span> <span class="n">gitlab</span><span class="o">.</span><span class="n">get_project</span><span class="p">(</span><span class="nb">id</span><span class="o">=</span><span class="mi">30</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>id</strong> (<em>int</em>) – The integer that uniquely identifies the project within the gitlab install.</p>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_gitlab.get_projects">
<code class="sig-prename descclassname">pulumi_gitlab.</code><code class="sig-name descname">get_projects</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">archived</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>bool<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">group_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>int<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">include_subgroups</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>bool<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">max_queryable_pages</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>int<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">membership</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>bool<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">min_access_level</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>int<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">order_by</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">owned</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>bool<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">page</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>int<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">per_page</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>int<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">search</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">simple</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>bool<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sort</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">starred</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>bool<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">statistics</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>bool<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">visibility</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">with_custom_attributes</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>bool<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">with_issues_enabled</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>bool<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">with_merge_requests_enabled</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>bool<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">with_programming_language</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">with_shared</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>bool<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_gitlab.get_projects.AwaitableGetProjectsResult<a class="headerlink" href="#pulumi_gitlab.get_projects" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides details about a list of projects in the Gitlab provider. Listing all projects and group projects with <a class="reference external" href="https://docs.gitlab.com/ee/api/projects.html#list-user-projects">project filtering</a> or <a class="reference external" href="https://docs.gitlab.com/ee/api/groups.html#list-a-groups-projects">group project filtering</a> is supported.</p>
<blockquote>
<div><p>NOTE: This data source supports all available filters exposed by the <code class="docutils literal notranslate"><span class="pre">xanzy/go-gitlab</span></code> package, which might not expose all available filters exposed by the Gitlab APIs.</p>
</div></blockquote>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_gitlab</span> <span class="k">as</span> <span class="nn">gitlab</span>

<span class="n">mygroup</span> <span class="o">=</span> <span class="n">gitlab</span><span class="o">.</span><span class="n">get_group</span><span class="p">(</span><span class="n">full_path</span><span class="o">=</span><span class="s2">&quot;mygroup&quot;</span><span class="p">)</span>
<span class="n">group_projects</span> <span class="o">=</span> <span class="n">gitlab</span><span class="o">.</span><span class="n">get_projects</span><span class="p">(</span><span class="n">group_id</span><span class="o">=</span><span class="n">mygroup</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">order_by</span><span class="o">=</span><span class="s2">&quot;name&quot;</span><span class="p">,</span>
    <span class="n">include_subgroups</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="n">with_shared</span><span class="o">=</span><span class="kc">False</span><span class="p">)</span>
</pre></div>
</div>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_gitlab</span> <span class="k">as</span> <span class="nn">gitlab</span>

<span class="n">projects</span> <span class="o">=</span> <span class="n">gitlab</span><span class="o">.</span><span class="n">get_projects</span><span class="p">(</span><span class="n">search</span><span class="o">=</span><span class="s2">&quot;postgresql&quot;</span><span class="p">,</span>
    <span class="n">visibility</span><span class="o">=</span><span class="s2">&quot;private&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>archived</strong> (<em>bool</em>) – Limit by archived status.</p></li>
<li><p><strong>group_id</strong> (<em>int</em>) – The ID of the group owned by the authenticated user to look projects for within. Cannot be used with <code class="docutils literal notranslate"><span class="pre">min_access_level</span></code>, <code class="docutils literal notranslate"><span class="pre">with_programming_language</span></code> or <code class="docutils literal notranslate"><span class="pre">statistics</span></code>.</p></li>
<li><p><strong>include_subgroups</strong> (<em>bool</em>) – Include projects in subgroups of this group. Default is <code class="docutils literal notranslate"><span class="pre">false</span></code>. Needs <code class="docutils literal notranslate"><span class="pre">group_id</span></code>.</p></li>
<li><p><strong>max_queryable_pages</strong> (<em>int</em>) – Prevents overloading your Gitlab instance in case of a misconfiguration. Default is <code class="docutils literal notranslate"><span class="pre">10</span></code>.</p></li>
<li><p><strong>membership</strong> (<em>bool</em>) – Limit by projects that the current user is a member of.</p></li>
<li><p><strong>min_access_level</strong> (<em>int</em>) – Limit to projects where current user has at least this access level, refer to the <a class="reference external" href="https://docs.gitlab.com/ee/api/members.html">official documentation</a> for values. Cannot be used with <code class="docutils literal notranslate"><span class="pre">group_id</span></code>.</p></li>
<li><p><strong>order_by</strong> (<em>str</em>) – Return projects ordered by <code class="docutils literal notranslate"><span class="pre">id</span></code>, <code class="docutils literal notranslate"><span class="pre">name</span></code>, <code class="docutils literal notranslate"><span class="pre">path</span></code>, <code class="docutils literal notranslate"><span class="pre">created_at</span></code>, <code class="docutils literal notranslate"><span class="pre">updated_at</span></code>, or <code class="docutils literal notranslate"><span class="pre">last_activity_at</span></code> fields. Default is <code class="docutils literal notranslate"><span class="pre">created_at</span></code>.</p></li>
<li><p><strong>owned</strong> (<em>bool</em>) – Limit by projects owned by the current user.</p></li>
<li><p><strong>search</strong> (<em>str</em>) – Return list of authorized projects matching the search criteria.</p></li>
<li><p><strong>simple</strong> (<em>bool</em>) – Return only the ID, URL, name, and path of each project.</p></li>
<li><p><strong>sort</strong> (<em>str</em>) – Return projects sorted in <code class="docutils literal notranslate"><span class="pre">asc</span></code> or <code class="docutils literal notranslate"><span class="pre">desc</span></code> order. Default is <code class="docutils literal notranslate"><span class="pre">desc</span></code>.</p></li>
<li><p><strong>starred</strong> (<em>bool</em>) – Limit by projects starred by the current user.</p></li>
<li><p><strong>statistics</strong> (<em>bool</em>) – Include project statistics. Cannot be used with <code class="docutils literal notranslate"><span class="pre">group_id</span></code>.</p></li>
<li><p><strong>visibility</strong> (<em>str</em>) – Limit by visibility <code class="docutils literal notranslate"><span class="pre">public</span></code>, <code class="docutils literal notranslate"><span class="pre">internal</span></code>, or <code class="docutils literal notranslate"><span class="pre">private</span></code>.</p></li>
<li><p><strong>with_custom*attributes</strong> (<em>bool</em>) – <p>Include custom attributes in response <a href="#id16"><span class="problematic" id="id17">*</span></a>(admins only)_.</p>
</p></li>
<li><p><strong>with_issues_enabled</strong> (<em>bool</em>) – Limit by projects with issues feature enabled. Default is <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>with_merge_requests_enabled</strong> (<em>bool</em>) – Limit by projects with merge requests feature enabled. Default is <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>with_programming_language</strong> (<em>str</em>) – Limit by projects which use the given programming language. Cannot be used with <code class="docutils literal notranslate"><span class="pre">group_id</span></code>.</p></li>
<li><p><strong>with_shared</strong> (<em>bool</em>) – Include projects shared to this group. Default is <code class="docutils literal notranslate"><span class="pre">true</span></code>. Needs <code class="docutils literal notranslate"><span class="pre">group_id</span></code>.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_gitlab.get_user">
<code class="sig-prename descclassname">pulumi_gitlab.</code><code class="sig-name descname">get_user</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">email</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">user_id</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>int<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">username</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_gitlab.get_user.AwaitableGetUserResult<a class="headerlink" href="#pulumi_gitlab.get_user" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides details about a specific user in the gitlab provider. Especially the ability to lookup the id for linking to other resources.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_gitlab</span> <span class="k">as</span> <span class="nn">gitlab</span>

<span class="n">example</span> <span class="o">=</span> <span class="n">gitlab</span><span class="o">.</span><span class="n">get_user</span><span class="p">(</span><span class="n">username</span><span class="o">=</span><span class="s2">&quot;myuser&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>email</strong> (<em>str</em>) – The e-mail address of the user. (Requires administrator privileges)</p></li>
<li><p><strong>user_id</strong> (<em>int</em>) – The ID of the user.</p></li>
<li><p><strong>username</strong> (<em>str</em>) – The username of the user.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_gitlab.get_users">
<code class="sig-prename descclassname">pulumi_gitlab.</code><code class="sig-name descname">get_users</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">active</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>bool<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">blocked</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>bool<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">created_after</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">created_before</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">extern_provider</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">extern_uid</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">order_by</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">search</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sort</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>str<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="p">:</span> <span class="n">Optional<span class="p">[</span>pulumi.invoke.InvokeOptions<span class="p">]</span></span> <span class="o">=</span> <span class="default_value">None</span></em><span class="sig-paren">)</span> &#x2192; pulumi_gitlab.get_users.AwaitableGetUsersResult<a class="headerlink" href="#pulumi_gitlab.get_users" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides details about a list of users in the gitlab provider. The results include id, username, email, name and more about the requested users. Users can also be sorted and filtered using several options.</p>
<p><strong>NOTE</strong>: Some of the available options require administrator privileges. Please visit [Gitlab API documentation][users_for_admins] for more information.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_gitlab</span> <span class="k">as</span> <span class="nn">gitlab</span>

<span class="n">example</span> <span class="o">=</span> <span class="n">gitlab</span><span class="o">.</span><span class="n">get_users</span><span class="p">(</span><span class="n">created_before</span><span class="o">=</span><span class="s2">&quot;2019-01-01&quot;</span><span class="p">,</span>
    <span class="n">order_by</span><span class="o">=</span><span class="s2">&quot;name&quot;</span><span class="p">,</span>
    <span class="n">sort</span><span class="o">=</span><span class="s2">&quot;desc&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>active</strong> (<em>bool</em>) – Filter users that are active.</p></li>
<li><p><strong>blocked</strong> (<em>bool</em>) – Filter users that are blocked.</p></li>
<li><p><strong>created_after</strong> (<em>str</em>) – Search for users created after a specific date. (Requires administrator privileges)</p></li>
<li><p><strong>created_before</strong> (<em>str</em>) – Search for users created before a specific date. (Requires administrator privileges)</p></li>
<li><p><strong>extern_provider</strong> (<em>str</em>) – Lookup users by external provider. (Requires administrator privileges)</p></li>
<li><p><strong>extern_uid</strong> (<em>str</em>) – Lookup users by external UID. (Requires administrator privileges)</p></li>
<li><p><strong>order_by</strong> (<em>str</em>) – Order the users’ list by <code class="docutils literal notranslate"><span class="pre">id</span></code>, <code class="docutils literal notranslate"><span class="pre">name</span></code>, <code class="docutils literal notranslate"><span class="pre">username</span></code>, <code class="docutils literal notranslate"><span class="pre">created_at</span></code> or <code class="docutils literal notranslate"><span class="pre">updated_at</span></code>. (Requires administrator privileges)</p></li>
<li><p><strong>search</strong> (<em>str</em>) – Search users by username, name or email.</p></li>
<li><p><strong>sort</strong> (<em>str</em>) – Sort users’ list in asc or desc order. (Requires administrator privileges)</p></li>
</ul>
</dd>
</dl>
</dd></dl>

</div>
