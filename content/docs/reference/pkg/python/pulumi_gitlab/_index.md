---
title: Package pulumi_gitlab
---

<div class="section" id="pulumi-gitlab">
<h1>Pulumi GitLab<a class="headerlink" href="#pulumi-gitlab" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-gitlab">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-gitlab/issues">pulumi/pulumi-gitlab repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-gitlab/issues">terraform-providers/terraform-provider-gitlab repo</a>.</div></blockquote>
<span class="target" id="module-pulumi_gitlab"></span><dl class="class">
<dt id="pulumi_gitlab.AwaitableGetGroupResult">
<em class="property">class </em><code class="descclassname">pulumi_gitlab.</code><code class="descname">AwaitableGetGroupResult</code><span class="sig-paren">(</span><em>description=None</em>, <em>full_name=None</em>, <em>full_path=None</em>, <em>group_id=None</em>, <em>lfs_enabled=None</em>, <em>name=None</em>, <em>parent_id=None</em>, <em>path=None</em>, <em>request_access_enabled=None</em>, <em>visibility_level=None</em>, <em>web_url=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gitlab.AwaitableGetGroupResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_gitlab.AwaitableGetProjectResult">
<em class="property">class </em><code class="descclassname">pulumi_gitlab.</code><code class="descname">AwaitableGetProjectResult</code><span class="sig-paren">(</span><em>archived=None</em>, <em>default_branch=None</em>, <em>description=None</em>, <em>http_url_to_repo=None</em>, <em>id=None</em>, <em>issues_enabled=None</em>, <em>merge_requests_enabled=None</em>, <em>name=None</em>, <em>namespace_id=None</em>, <em>path=None</em>, <em>runners_token=None</em>, <em>snippets_enabled=None</em>, <em>ssh_url_to_repo=None</em>, <em>visibility_level=None</em>, <em>web_url=None</em>, <em>wiki_enabled=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gitlab.AwaitableGetProjectResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_gitlab.AwaitableGetUserResult">
<em class="property">class </em><code class="descclassname">pulumi_gitlab.</code><code class="descname">AwaitableGetUserResult</code><span class="sig-paren">(</span><em>avatar_url=None</em>, <em>bio=None</em>, <em>can_create_group=None</em>, <em>can_create_project=None</em>, <em>color_scheme_id=None</em>, <em>created_at=None</em>, <em>current_sign_in_at=None</em>, <em>email=None</em>, <em>extern_uid=None</em>, <em>external=None</em>, <em>is_admin=None</em>, <em>last_sign_in_at=None</em>, <em>linkedin=None</em>, <em>location=None</em>, <em>name=None</em>, <em>organization=None</em>, <em>projects_limit=None</em>, <em>skype=None</em>, <em>state=None</em>, <em>theme_id=None</em>, <em>twitter=None</em>, <em>two_factor_enabled=None</em>, <em>user_id=None</em>, <em>user_provider=None</em>, <em>username=None</em>, <em>website_url=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gitlab.AwaitableGetUserResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_gitlab.AwaitableGetUsersResult">
<em class="property">class </em><code class="descclassname">pulumi_gitlab.</code><code class="descname">AwaitableGetUsersResult</code><span class="sig-paren">(</span><em>active=None</em>, <em>blocked=None</em>, <em>created_after=None</em>, <em>created_before=None</em>, <em>extern_provider=None</em>, <em>extern_uid=None</em>, <em>order_by=None</em>, <em>search=None</em>, <em>sort=None</em>, <em>users=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gitlab.AwaitableGetUsersResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_gitlab.BranchProtection">
<em class="property">class </em><code class="descclassname">pulumi_gitlab.</code><code class="descname">BranchProtection</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>branch=None</em>, <em>merge_access_level=None</em>, <em>project=None</em>, <em>push_access_level=None</em>, <em>__props__=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gitlab.BranchProtection" title="Permalink to this definition">¶</a></dt>
<dd><p>This resource allows you to protect a specific branch by an access level so that the user with less access level cannot Merge/Push to the branch. GitLab EE features to protect by group or user are not supported.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>branch</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the branch.</li>
<li><strong>merge_access_level</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – One of five levels of access to the project.</li>
<li><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The id of the project.</li>
<li><strong>push_access_level</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – One of five levels of access to the project.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-gitlab/blob/master/website/docs/r/branch_protection.html.markdown">https://github.com/terraform-providers/terraform-provider-gitlab/blob/master/website/docs/r/branch_protection.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_gitlab.BranchProtection.branch">
<code class="descname">branch</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gitlab.BranchProtection.branch" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the branch.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gitlab.BranchProtection.merge_access_level">
<code class="descname">merge_access_level</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gitlab.BranchProtection.merge_access_level" title="Permalink to this definition">¶</a></dt>
<dd><p>One of five levels of access to the project.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gitlab.BranchProtection.project">
<code class="descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gitlab.BranchProtection.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The id of the project.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gitlab.BranchProtection.push_access_level">
<code class="descname">push_access_level</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gitlab.BranchProtection.push_access_level" title="Permalink to this definition">¶</a></dt>
<dd><p>One of five levels of access to the project.</p>
</dd></dl>

<dl class="staticmethod">
<dt id="pulumi_gitlab.BranchProtection.get">
<em class="property">static </em><code class="descname">get</code><span class="sig-paren">(</span><em>resource_name</em>, <em>id</em>, <em>opts=None</em>, <em>branch=None</em>, <em>merge_access_level=None</em>, <em>project=None</em>, <em>push_access_level=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gitlab.BranchProtection.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing BranchProtection resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.
:param str resource_name: The unique name of the resulting resource.
:param str id: The unique provider ID of the resource to lookup.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] branch: Name of the branch.
:param pulumi.Input[str] merge_access_level: One of five levels of access to the project.
:param pulumi.Input[str] project: The id of the project.
:param pulumi.Input[str] push_access_level: One of five levels of access to the project.</p>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-gitlab/blob/master/website/docs/r/branch_protection.html.markdown">https://github.com/terraform-providers/terraform-provider-gitlab/blob/master/website/docs/r/branch_protection.html.markdown</a>.</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_gitlab.BranchProtection.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gitlab.BranchProtection.translate_output_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of output properties
into a format of their choosing before writing those properties to the resource object.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><strong>prop</strong> (<em>str</em>) – A property name.</td>
</tr>
<tr class="field-even field"><th class="field-name">Returns:</th><td class="field-body">A potentially transformed property name.</td>
</tr>
<tr class="field-odd field"><th class="field-name">Return type:</th><td class="field-body">str</td>
</tr>
</tbody>
</table>
</dd></dl>

<dl class="method">
<dt id="pulumi_gitlab.BranchProtection.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gitlab.BranchProtection.translate_input_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of input properties into
a format of their choosing before sending those properties to the Pulumi engine.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><strong>prop</strong> (<em>str</em>) – A property name.</td>
</tr>
<tr class="field-even field"><th class="field-name">Returns:</th><td class="field-body">A potentially transformed property name.</td>
</tr>
<tr class="field-odd field"><th class="field-name">Return type:</th><td class="field-body">str</td>
</tr>
</tbody>
</table>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_gitlab.DeployKey">
<em class="property">class </em><code class="descclassname">pulumi_gitlab.</code><code class="descname">DeployKey</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>can_push=None</em>, <em>key=None</em>, <em>project=None</em>, <em>title=None</em>, <em>__props__=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gitlab.DeployKey" title="Permalink to this definition">¶</a></dt>
<dd><p>This resource allows you to create and manage deploy keys for your GitLab projects.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>can_push</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Allow this deploy key to be used to push changes to the project.  Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>. <strong>NOTE:</strong> this cannot currently be managed.</li>
<li><strong>key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The public ssh key body.</li>
<li><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name or id of the project to add the deploy key to.</li>
<li><strong>title</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A title to describe the deploy key with.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-gitlab/blob/master/website/docs/r/deploy_key.html.markdown">https://github.com/terraform-providers/terraform-provider-gitlab/blob/master/website/docs/r/deploy_key.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_gitlab.DeployKey.can_push">
<code class="descname">can_push</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gitlab.DeployKey.can_push" title="Permalink to this definition">¶</a></dt>
<dd><p>Allow this deploy key to be used to push changes to the project.  Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>. <strong>NOTE:</strong> this cannot currently be managed.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gitlab.DeployKey.key">
<code class="descname">key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gitlab.DeployKey.key" title="Permalink to this definition">¶</a></dt>
<dd><p>The public ssh key body.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gitlab.DeployKey.project">
<code class="descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gitlab.DeployKey.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The name or id of the project to add the deploy key to.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gitlab.DeployKey.title">
<code class="descname">title</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gitlab.DeployKey.title" title="Permalink to this definition">¶</a></dt>
<dd><p>A title to describe the deploy key with.</p>
</dd></dl>

<dl class="staticmethod">
<dt id="pulumi_gitlab.DeployKey.get">
<em class="property">static </em><code class="descname">get</code><span class="sig-paren">(</span><em>resource_name</em>, <em>id</em>, <em>opts=None</em>, <em>can_push=None</em>, <em>key=None</em>, <em>project=None</em>, <em>title=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gitlab.DeployKey.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing DeployKey resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.
:param str resource_name: The unique name of the resulting resource.
:param str id: The unique provider ID of the resource to lookup.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[bool] can_push: Allow this deploy key to be used to push changes to the project.  Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>. <strong>NOTE:</strong> this cannot currently be managed.
:param pulumi.Input[str] key: The public ssh key body.
:param pulumi.Input[str] project: The name or id of the project to add the deploy key to.
:param pulumi.Input[str] title: A title to describe the deploy key with.</p>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-gitlab/blob/master/website/docs/r/deploy_key.html.markdown">https://github.com/terraform-providers/terraform-provider-gitlab/blob/master/website/docs/r/deploy_key.html.markdown</a>.</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_gitlab.DeployKey.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gitlab.DeployKey.translate_output_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of output properties
into a format of their choosing before writing those properties to the resource object.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><strong>prop</strong> (<em>str</em>) – A property name.</td>
</tr>
<tr class="field-even field"><th class="field-name">Returns:</th><td class="field-body">A potentially transformed property name.</td>
</tr>
<tr class="field-odd field"><th class="field-name">Return type:</th><td class="field-body">str</td>
</tr>
</tbody>
</table>
</dd></dl>

<dl class="method">
<dt id="pulumi_gitlab.DeployKey.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gitlab.DeployKey.translate_input_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of input properties into
a format of their choosing before sending those properties to the Pulumi engine.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><strong>prop</strong> (<em>str</em>) – A property name.</td>
</tr>
<tr class="field-even field"><th class="field-name">Returns:</th><td class="field-body">A potentially transformed property name.</td>
</tr>
<tr class="field-odd field"><th class="field-name">Return type:</th><td class="field-body">str</td>
</tr>
</tbody>
</table>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_gitlab.GetGroupResult">
<em class="property">class </em><code class="descclassname">pulumi_gitlab.</code><code class="descname">GetGroupResult</code><span class="sig-paren">(</span><em>description=None</em>, <em>full_name=None</em>, <em>full_path=None</em>, <em>group_id=None</em>, <em>lfs_enabled=None</em>, <em>name=None</em>, <em>parent_id=None</em>, <em>path=None</em>, <em>request_access_enabled=None</em>, <em>visibility_level=None</em>, <em>web_url=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gitlab.GetGroupResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getGroup.</p>
<dl class="attribute">
<dt id="pulumi_gitlab.GetGroupResult.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gitlab.GetGroupResult.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description of the group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gitlab.GetGroupResult.full_name">
<code class="descname">full_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gitlab.GetGroupResult.full_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The full name of the group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gitlab.GetGroupResult.full_path">
<code class="descname">full_path</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gitlab.GetGroupResult.full_path" title="Permalink to this definition">¶</a></dt>
<dd><p>The full path of the group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gitlab.GetGroupResult.lfs_enabled">
<code class="descname">lfs_enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gitlab.GetGroupResult.lfs_enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean, is LFS enabled for projects in this group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gitlab.GetGroupResult.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gitlab.GetGroupResult.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of this group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gitlab.GetGroupResult.parent_id">
<code class="descname">parent_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gitlab.GetGroupResult.parent_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Integer, ID of the parent group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gitlab.GetGroupResult.path">
<code class="descname">path</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gitlab.GetGroupResult.path" title="Permalink to this definition">¶</a></dt>
<dd><p>The path of the group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gitlab.GetGroupResult.request_access_enabled">
<code class="descname">request_access_enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gitlab.GetGroupResult.request_access_enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean, is request for access enabled to the group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gitlab.GetGroupResult.visibility_level">
<code class="descname">visibility_level</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gitlab.GetGroupResult.visibility_level" title="Permalink to this definition">¶</a></dt>
<dd><p>Visibility level of the group. Possible values are <code class="docutils literal notranslate"><span class="pre">private</span></code>, <code class="docutils literal notranslate"><span class="pre">internal</span></code>, <code class="docutils literal notranslate"><span class="pre">public</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gitlab.GetGroupResult.web_url">
<code class="descname">web_url</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gitlab.GetGroupResult.web_url" title="Permalink to this definition">¶</a></dt>
<dd><p>Web URL of the group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gitlab.GetGroupResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gitlab.GetGroupResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_gitlab.GetProjectResult">
<em class="property">class </em><code class="descclassname">pulumi_gitlab.</code><code class="descname">GetProjectResult</code><span class="sig-paren">(</span><em>archived=None</em>, <em>default_branch=None</em>, <em>description=None</em>, <em>http_url_to_repo=None</em>, <em>id=None</em>, <em>issues_enabled=None</em>, <em>merge_requests_enabled=None</em>, <em>name=None</em>, <em>namespace_id=None</em>, <em>path=None</em>, <em>runners_token=None</em>, <em>snippets_enabled=None</em>, <em>ssh_url_to_repo=None</em>, <em>visibility_level=None</em>, <em>web_url=None</em>, <em>wiki_enabled=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gitlab.GetProjectResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getProject.</p>
<dl class="attribute">
<dt id="pulumi_gitlab.GetProjectResult.archived">
<code class="descname">archived</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gitlab.GetProjectResult.archived" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the project is in read-only mode (archived).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gitlab.GetProjectResult.default_branch">
<code class="descname">default_branch</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gitlab.GetProjectResult.default_branch" title="Permalink to this definition">¶</a></dt>
<dd><p>The default branch for the project.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gitlab.GetProjectResult.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gitlab.GetProjectResult.description" title="Permalink to this definition">¶</a></dt>
<dd><p>A description of the project.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gitlab.GetProjectResult.http_url_to_repo">
<code class="descname">http_url_to_repo</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gitlab.GetProjectResult.http_url_to_repo" title="Permalink to this definition">¶</a></dt>
<dd><p>URL that can be provided to <code class="docutils literal notranslate"><span class="pre">git</span> <span class="pre">clone</span></code> to clone the
repository via HTTP.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gitlab.GetProjectResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gitlab.GetProjectResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>Integer that uniquely identifies the project within the gitlab install.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gitlab.GetProjectResult.issues_enabled">
<code class="descname">issues_enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gitlab.GetProjectResult.issues_enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Enable issue tracking for the project.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gitlab.GetProjectResult.merge_requests_enabled">
<code class="descname">merge_requests_enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gitlab.GetProjectResult.merge_requests_enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Enable merge requests for the project.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gitlab.GetProjectResult.namespace_id">
<code class="descname">namespace_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gitlab.GetProjectResult.namespace_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The namespace (group or user) of the project. Defaults to your user.
See <code class="docutils literal notranslate"><span class="pre">.Group</span></code> for an example.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gitlab.GetProjectResult.path">
<code class="descname">path</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gitlab.GetProjectResult.path" title="Permalink to this definition">¶</a></dt>
<dd><p>The path of the repository.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gitlab.GetProjectResult.runners_token">
<code class="descname">runners_token</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gitlab.GetProjectResult.runners_token" title="Permalink to this definition">¶</a></dt>
<dd><p>Registration token to use during runner setup.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gitlab.GetProjectResult.snippets_enabled">
<code class="descname">snippets_enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gitlab.GetProjectResult.snippets_enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Enable snippets for the project.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gitlab.GetProjectResult.ssh_url_to_repo">
<code class="descname">ssh_url_to_repo</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gitlab.GetProjectResult.ssh_url_to_repo" title="Permalink to this definition">¶</a></dt>
<dd><p>URL that can be provided to <code class="docutils literal notranslate"><span class="pre">git</span> <span class="pre">clone</span></code> to clone the
repository via SSH.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gitlab.GetProjectResult.visibility_level">
<code class="descname">visibility_level</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gitlab.GetProjectResult.visibility_level" title="Permalink to this definition">¶</a></dt>
<dd><p>Repositories are created as private by default.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gitlab.GetProjectResult.web_url">
<code class="descname">web_url</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gitlab.GetProjectResult.web_url" title="Permalink to this definition">¶</a></dt>
<dd><p>URL that can be used to find the project in a browser.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gitlab.GetProjectResult.wiki_enabled">
<code class="descname">wiki_enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gitlab.GetProjectResult.wiki_enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Enable wiki for the project.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_gitlab.GetUserResult">
<em class="property">class </em><code class="descclassname">pulumi_gitlab.</code><code class="descname">GetUserResult</code><span class="sig-paren">(</span><em>avatar_url=None</em>, <em>bio=None</em>, <em>can_create_group=None</em>, <em>can_create_project=None</em>, <em>color_scheme_id=None</em>, <em>created_at=None</em>, <em>current_sign_in_at=None</em>, <em>email=None</em>, <em>extern_uid=None</em>, <em>external=None</em>, <em>is_admin=None</em>, <em>last_sign_in_at=None</em>, <em>linkedin=None</em>, <em>location=None</em>, <em>name=None</em>, <em>organization=None</em>, <em>projects_limit=None</em>, <em>skype=None</em>, <em>state=None</em>, <em>theme_id=None</em>, <em>twitter=None</em>, <em>two_factor_enabled=None</em>, <em>user_id=None</em>, <em>user_provider=None</em>, <em>username=None</em>, <em>website_url=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gitlab.GetUserResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getUser.</p>
<dl class="attribute">
<dt id="pulumi_gitlab.GetUserResult.avatar_url">
<code class="descname">avatar_url</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gitlab.GetUserResult.avatar_url" title="Permalink to this definition">¶</a></dt>
<dd><p>The avatar URL of the user.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gitlab.GetUserResult.bio">
<code class="descname">bio</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gitlab.GetUserResult.bio" title="Permalink to this definition">¶</a></dt>
<dd><p>The bio of the user.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gitlab.GetUserResult.can_create_group">
<code class="descname">can_create_group</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gitlab.GetUserResult.can_create_group" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the user can create groups.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gitlab.GetUserResult.can_create_project">
<code class="descname">can_create_project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gitlab.GetUserResult.can_create_project" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the user can create projects.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gitlab.GetUserResult.color_scheme_id">
<code class="descname">color_scheme_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gitlab.GetUserResult.color_scheme_id" title="Permalink to this definition">¶</a></dt>
<dd><p>User’s color scheme ID.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gitlab.GetUserResult.created_at">
<code class="descname">created_at</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gitlab.GetUserResult.created_at" title="Permalink to this definition">¶</a></dt>
<dd><p>Date the user was created at.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gitlab.GetUserResult.current_sign_in_at">
<code class="descname">current_sign_in_at</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gitlab.GetUserResult.current_sign_in_at" title="Permalink to this definition">¶</a></dt>
<dd><p>Current user’s sign-in date.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gitlab.GetUserResult.email">
<code class="descname">email</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gitlab.GetUserResult.email" title="Permalink to this definition">¶</a></dt>
<dd><p>The e-mail address of the user.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gitlab.GetUserResult.extern_uid">
<code class="descname">extern_uid</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gitlab.GetUserResult.extern_uid" title="Permalink to this definition">¶</a></dt>
<dd><p>The external UID of the user.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gitlab.GetUserResult.external">
<code class="descname">external</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gitlab.GetUserResult.external" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the user is external.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gitlab.GetUserResult.is_admin">
<code class="descname">is_admin</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gitlab.GetUserResult.is_admin" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the user is an admin.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gitlab.GetUserResult.last_sign_in_at">
<code class="descname">last_sign_in_at</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gitlab.GetUserResult.last_sign_in_at" title="Permalink to this definition">¶</a></dt>
<dd><p>Last user’s sign-in date.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gitlab.GetUserResult.linkedin">
<code class="descname">linkedin</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gitlab.GetUserResult.linkedin" title="Permalink to this definition">¶</a></dt>
<dd><p>Linkedin profile of the user.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gitlab.GetUserResult.location">
<code class="descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gitlab.GetUserResult.location" title="Permalink to this definition">¶</a></dt>
<dd><p>The location of the user.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gitlab.GetUserResult.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gitlab.GetUserResult.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the user.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gitlab.GetUserResult.organization">
<code class="descname">organization</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gitlab.GetUserResult.organization" title="Permalink to this definition">¶</a></dt>
<dd><p>The organization of the user.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gitlab.GetUserResult.projects_limit">
<code class="descname">projects_limit</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gitlab.GetUserResult.projects_limit" title="Permalink to this definition">¶</a></dt>
<dd><p>Number of projects the user can create.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gitlab.GetUserResult.skype">
<code class="descname">skype</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gitlab.GetUserResult.skype" title="Permalink to this definition">¶</a></dt>
<dd><p>Skype username of the user.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gitlab.GetUserResult.state">
<code class="descname">state</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gitlab.GetUserResult.state" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the user is active or blocked.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gitlab.GetUserResult.theme_id">
<code class="descname">theme_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gitlab.GetUserResult.theme_id" title="Permalink to this definition">¶</a></dt>
<dd><p>User’s theme ID.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gitlab.GetUserResult.twitter">
<code class="descname">twitter</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gitlab.GetUserResult.twitter" title="Permalink to this definition">¶</a></dt>
<dd><p>Twitter username of the user.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gitlab.GetUserResult.two_factor_enabled">
<code class="descname">two_factor_enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gitlab.GetUserResult.two_factor_enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether user’s two factor auth is enabled.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gitlab.GetUserResult.user_provider">
<code class="descname">user_provider</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gitlab.GetUserResult.user_provider" title="Permalink to this definition">¶</a></dt>
<dd><p>The UID provider of the user.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gitlab.GetUserResult.username">
<code class="descname">username</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gitlab.GetUserResult.username" title="Permalink to this definition">¶</a></dt>
<dd><p>The username of the user.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gitlab.GetUserResult.website_url">
<code class="descname">website_url</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gitlab.GetUserResult.website_url" title="Permalink to this definition">¶</a></dt>
<dd><p>User’s website URL.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gitlab.GetUserResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gitlab.GetUserResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_gitlab.GetUsersResult">
<em class="property">class </em><code class="descclassname">pulumi_gitlab.</code><code class="descname">GetUsersResult</code><span class="sig-paren">(</span><em>active=None</em>, <em>blocked=None</em>, <em>created_after=None</em>, <em>created_before=None</em>, <em>extern_provider=None</em>, <em>extern_uid=None</em>, <em>order_by=None</em>, <em>search=None</em>, <em>sort=None</em>, <em>users=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gitlab.GetUsersResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getUsers.</p>
<dl class="attribute">
<dt id="pulumi_gitlab.GetUsersResult.extern_uid">
<code class="descname">extern_uid</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gitlab.GetUsersResult.extern_uid" title="Permalink to this definition">¶</a></dt>
<dd><p>The external UID of the user.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gitlab.GetUsersResult.users">
<code class="descname">users</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gitlab.GetUsersResult.users" title="Permalink to this definition">¶</a></dt>
<dd><p>The list of users.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gitlab.GetUsersResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gitlab.GetUsersResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_gitlab.Group">
<em class="property">class </em><code class="descclassname">pulumi_gitlab.</code><code class="descname">Group</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>description=None</em>, <em>lfs_enabled=None</em>, <em>name=None</em>, <em>parent_id=None</em>, <em>path=None</em>, <em>request_access_enabled=None</em>, <em>visibility_level=None</em>, <em>__props__=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gitlab.Group" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a Group resource with the given unique name, props, and options.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the group.</li>
<li><strong>lfs_enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean, defaults to true.  Whether to enable LFS
support for projects in this group.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of this group.</li>
<li><strong>parent_id</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Integer, id of the parent group (creates a nested group).</li>
<li><strong>path</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The path of the group.</li>
<li><strong>request_access_enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean, defaults to false.  Whether to
enable users to request access to the group.</li>
<li><strong>visibility_level</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Set to <code class="docutils literal notranslate"><span class="pre">public</span></code> to create a public group.
Valid values are <code class="docutils literal notranslate"><span class="pre">private</span></code>, <code class="docutils literal notranslate"><span class="pre">internal</span></code>, <code class="docutils literal notranslate"><span class="pre">public</span></code>.
Groups are created as private by default.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-gitlab/blob/master/website/docs/r/group.html.markdown">https://github.com/terraform-providers/terraform-provider-gitlab/blob/master/website/docs/r/group.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_gitlab.Group.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gitlab.Group.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description of the group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gitlab.Group.full_name">
<code class="descname">full_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gitlab.Group.full_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The full name of the group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gitlab.Group.full_path">
<code class="descname">full_path</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gitlab.Group.full_path" title="Permalink to this definition">¶</a></dt>
<dd><p>The full path of the group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gitlab.Group.lfs_enabled">
<code class="descname">lfs_enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gitlab.Group.lfs_enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean, defaults to true.  Whether to enable LFS
support for projects in this group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gitlab.Group.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gitlab.Group.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of this group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gitlab.Group.parent_id">
<code class="descname">parent_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gitlab.Group.parent_id" title="Permalink to this definition">¶</a></dt>
<dd><p>Integer, id of the parent group (creates a nested group).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gitlab.Group.path">
<code class="descname">path</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gitlab.Group.path" title="Permalink to this definition">¶</a></dt>
<dd><p>The path of the group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gitlab.Group.request_access_enabled">
<code class="descname">request_access_enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gitlab.Group.request_access_enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean, defaults to false.  Whether to
enable users to request access to the group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gitlab.Group.visibility_level">
<code class="descname">visibility_level</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gitlab.Group.visibility_level" title="Permalink to this definition">¶</a></dt>
<dd><p>Set to <code class="docutils literal notranslate"><span class="pre">public</span></code> to create a public group.
Valid values are <code class="docutils literal notranslate"><span class="pre">private</span></code>, <code class="docutils literal notranslate"><span class="pre">internal</span></code>, <code class="docutils literal notranslate"><span class="pre">public</span></code>.
Groups are created as private by default.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gitlab.Group.web_url">
<code class="descname">web_url</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gitlab.Group.web_url" title="Permalink to this definition">¶</a></dt>
<dd><p>Web URL of the group.</p>
</dd></dl>

<dl class="staticmethod">
<dt id="pulumi_gitlab.Group.get">
<em class="property">static </em><code class="descname">get</code><span class="sig-paren">(</span><em>resource_name</em>, <em>id</em>, <em>opts=None</em>, <em>description=None</em>, <em>full_name=None</em>, <em>full_path=None</em>, <em>lfs_enabled=None</em>, <em>name=None</em>, <em>parent_id=None</em>, <em>path=None</em>, <em>request_access_enabled=None</em>, <em>visibility_level=None</em>, <em>web_url=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gitlab.Group.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Group resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.
:param str resource_name: The unique name of the resulting resource.
:param str id: The unique provider ID of the resource to lookup.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] description: The description of the group.
:param pulumi.Input[str] full_name: The full name of the group.
:param pulumi.Input[str] full_path: The full path of the group.
:param pulumi.Input[bool] lfs_enabled: Boolean, defaults to true.  Whether to enable LFS</p>
<blockquote>
<div>support for projects in this group.</div></blockquote>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of this group.</li>
<li><strong>parent_id</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Integer, id of the parent group (creates a nested group).</li>
<li><strong>path</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The path of the group.</li>
<li><strong>request_access_enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean, defaults to false.  Whether to
enable users to request access to the group.</li>
<li><strong>visibility_level</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Set to <code class="docutils literal notranslate"><span class="pre">public</span></code> to create a public group.
Valid values are <code class="docutils literal notranslate"><span class="pre">private</span></code>, <code class="docutils literal notranslate"><span class="pre">internal</span></code>, <code class="docutils literal notranslate"><span class="pre">public</span></code>.
Groups are created as private by default.</li>
<li><strong>web_url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Web URL of the group.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-gitlab/blob/master/website/docs/r/group.html.markdown">https://github.com/terraform-providers/terraform-provider-gitlab/blob/master/website/docs/r/group.html.markdown</a>.</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_gitlab.Group.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gitlab.Group.translate_output_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of output properties
into a format of their choosing before writing those properties to the resource object.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><strong>prop</strong> (<em>str</em>) – A property name.</td>
</tr>
<tr class="field-even field"><th class="field-name">Returns:</th><td class="field-body">A potentially transformed property name.</td>
</tr>
<tr class="field-odd field"><th class="field-name">Return type:</th><td class="field-body">str</td>
</tr>
</tbody>
</table>
</dd></dl>

<dl class="method">
<dt id="pulumi_gitlab.Group.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gitlab.Group.translate_input_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of input properties into
a format of their choosing before sending those properties to the Pulumi engine.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><strong>prop</strong> (<em>str</em>) – A property name.</td>
</tr>
<tr class="field-even field"><th class="field-name">Returns:</th><td class="field-body">A potentially transformed property name.</td>
</tr>
<tr class="field-odd field"><th class="field-name">Return type:</th><td class="field-body">str</td>
</tr>
</tbody>
</table>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_gitlab.GroupMembership">
<em class="property">class </em><code class="descclassname">pulumi_gitlab.</code><code class="descname">GroupMembership</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>access_level=None</em>, <em>expires_at=None</em>, <em>group_id=None</em>, <em>user_id=None</em>, <em>__props__=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gitlab.GroupMembership" title="Permalink to this definition">¶</a></dt>
<dd><p>This resource allows you to add a user to an existing group.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>access_level</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Acceptable values are: guest, reporter, developer, master.</li>
<li><strong>expires_at</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Expiration date for the group membership. Format: <code class="docutils literal notranslate"><span class="pre">YYYY-MM-DD</span></code></li>
<li><strong>group_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The id of the group.</li>
<li><strong>user_id</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The id of the user.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-gitlab/blob/master/website/docs/r/group_membership.html.markdown">https://github.com/terraform-providers/terraform-provider-gitlab/blob/master/website/docs/r/group_membership.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_gitlab.GroupMembership.access_level">
<code class="descname">access_level</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gitlab.GroupMembership.access_level" title="Permalink to this definition">¶</a></dt>
<dd><p>Acceptable values are: guest, reporter, developer, master.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gitlab.GroupMembership.expires_at">
<code class="descname">expires_at</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gitlab.GroupMembership.expires_at" title="Permalink to this definition">¶</a></dt>
<dd><p>Expiration date for the group membership. Format: <code class="docutils literal notranslate"><span class="pre">YYYY-MM-DD</span></code></p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gitlab.GroupMembership.group_id">
<code class="descname">group_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gitlab.GroupMembership.group_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The id of the group.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gitlab.GroupMembership.user_id">
<code class="descname">user_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gitlab.GroupMembership.user_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The id of the user.</p>
</dd></dl>

<dl class="staticmethod">
<dt id="pulumi_gitlab.GroupMembership.get">
<em class="property">static </em><code class="descname">get</code><span class="sig-paren">(</span><em>resource_name</em>, <em>id</em>, <em>opts=None</em>, <em>access_level=None</em>, <em>expires_at=None</em>, <em>group_id=None</em>, <em>user_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gitlab.GroupMembership.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing GroupMembership resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.
:param str resource_name: The unique name of the resulting resource.
:param str id: The unique provider ID of the resource to lookup.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] access_level: Acceptable values are: guest, reporter, developer, master.
:param pulumi.Input[str] expires_at: Expiration date for the group membership. Format: <code class="docutils literal notranslate"><span class="pre">YYYY-MM-DD</span></code>
:param pulumi.Input[str] group_id: The id of the group.
:param pulumi.Input[float] user_id: The id of the user.</p>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-gitlab/blob/master/website/docs/r/group_membership.html.markdown">https://github.com/terraform-providers/terraform-provider-gitlab/blob/master/website/docs/r/group_membership.html.markdown</a>.</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_gitlab.GroupMembership.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gitlab.GroupMembership.translate_output_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of output properties
into a format of their choosing before writing those properties to the resource object.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><strong>prop</strong> (<em>str</em>) – A property name.</td>
</tr>
<tr class="field-even field"><th class="field-name">Returns:</th><td class="field-body">A potentially transformed property name.</td>
</tr>
<tr class="field-odd field"><th class="field-name">Return type:</th><td class="field-body">str</td>
</tr>
</tbody>
</table>
</dd></dl>

<dl class="method">
<dt id="pulumi_gitlab.GroupMembership.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gitlab.GroupMembership.translate_input_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of input properties into
a format of their choosing before sending those properties to the Pulumi engine.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><strong>prop</strong> (<em>str</em>) – A property name.</td>
</tr>
<tr class="field-even field"><th class="field-name">Returns:</th><td class="field-body">A potentially transformed property name.</td>
</tr>
<tr class="field-odd field"><th class="field-name">Return type:</th><td class="field-body">str</td>
</tr>
</tbody>
</table>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_gitlab.GroupVariable">
<em class="property">class </em><code class="descclassname">pulumi_gitlab.</code><code class="descname">GroupVariable</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>group=None</em>, <em>key=None</em>, <em>protected=None</em>, <em>value=None</em>, <em>__props__=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gitlab.GroupVariable" title="Permalink to this definition">¶</a></dt>
<dd><p>This resource allows you to create and manage CI/CD variables for your GitLab groups.
For further information on variables, consult the <a class="reference external" href="https://docs.gitlab.com/ce/ci/variables/README.html#variables">gitlab
documentation</a>.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>group</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name or id of the group to add the hook to.</li>
<li><strong>key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the variable.</li>
<li><strong>protected</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If set to <code class="docutils literal notranslate"><span class="pre">true</span></code>, the variable will be passed only to pipelines running on protected branches and tags. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</li>
<li><strong>value</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The value of the variable.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-gitlab/blob/master/website/docs/r/group_variable.html.markdown">https://github.com/terraform-providers/terraform-provider-gitlab/blob/master/website/docs/r/group_variable.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_gitlab.GroupVariable.group">
<code class="descname">group</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gitlab.GroupVariable.group" title="Permalink to this definition">¶</a></dt>
<dd><p>The name or id of the group to add the hook to.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gitlab.GroupVariable.key">
<code class="descname">key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gitlab.GroupVariable.key" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the variable.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gitlab.GroupVariable.protected">
<code class="descname">protected</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gitlab.GroupVariable.protected" title="Permalink to this definition">¶</a></dt>
<dd><p>If set to <code class="docutils literal notranslate"><span class="pre">true</span></code>, the variable will be passed only to pipelines running on protected branches and tags. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gitlab.GroupVariable.value">
<code class="descname">value</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gitlab.GroupVariable.value" title="Permalink to this definition">¶</a></dt>
<dd><p>The value of the variable.</p>
</dd></dl>

<dl class="staticmethod">
<dt id="pulumi_gitlab.GroupVariable.get">
<em class="property">static </em><code class="descname">get</code><span class="sig-paren">(</span><em>resource_name</em>, <em>id</em>, <em>opts=None</em>, <em>group=None</em>, <em>key=None</em>, <em>protected=None</em>, <em>value=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gitlab.GroupVariable.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing GroupVariable resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.
:param str resource_name: The unique name of the resulting resource.
:param str id: The unique provider ID of the resource to lookup.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] group: The name or id of the group to add the hook to.
:param pulumi.Input[str] key: The name of the variable.
:param pulumi.Input[bool] protected: If set to <code class="docutils literal notranslate"><span class="pre">true</span></code>, the variable will be passed only to pipelines running on protected branches and tags. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.
:param pulumi.Input[str] value: The value of the variable.</p>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-gitlab/blob/master/website/docs/r/group_variable.html.markdown">https://github.com/terraform-providers/terraform-provider-gitlab/blob/master/website/docs/r/group_variable.html.markdown</a>.</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_gitlab.GroupVariable.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gitlab.GroupVariable.translate_output_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of output properties
into a format of their choosing before writing those properties to the resource object.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><strong>prop</strong> (<em>str</em>) – A property name.</td>
</tr>
<tr class="field-even field"><th class="field-name">Returns:</th><td class="field-body">A potentially transformed property name.</td>
</tr>
<tr class="field-odd field"><th class="field-name">Return type:</th><td class="field-body">str</td>
</tr>
</tbody>
</table>
</dd></dl>

<dl class="method">
<dt id="pulumi_gitlab.GroupVariable.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gitlab.GroupVariable.translate_input_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of input properties into
a format of their choosing before sending those properties to the Pulumi engine.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><strong>prop</strong> (<em>str</em>) – A property name.</td>
</tr>
<tr class="field-even field"><th class="field-name">Returns:</th><td class="field-body">A potentially transformed property name.</td>
</tr>
<tr class="field-odd field"><th class="field-name">Return type:</th><td class="field-body">str</td>
</tr>
</tbody>
</table>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_gitlab.Label">
<em class="property">class </em><code class="descclassname">pulumi_gitlab.</code><code class="descname">Label</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>color=None</em>, <em>description=None</em>, <em>name=None</em>, <em>project=None</em>, <em>__props__=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gitlab.Label" title="Permalink to this definition">¶</a></dt>
<dd><p>This resource allows you to create and manage labels for your GitLab projects.
For further information on labels, consult the <a class="reference external" href="https://docs.gitlab.com/ee/user/project/labels.htm">gitlab
documentation</a>.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>color</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The color of the label given in 6-digit hex notation with leading ‘#’ sign (e.g. #FFAABB) or one of the <a class="reference external" href="https://developer.mozilla.org/en-US/docs/Web/CSS/color_value#Color_keywords">CSS color names</a>.</li>
<li><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the label.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the label.</li>
<li><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name or id of the project to add the label to.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-gitlab/blob/master/website/docs/r/label.html.markdown">https://github.com/terraform-providers/terraform-provider-gitlab/blob/master/website/docs/r/label.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_gitlab.Label.color">
<code class="descname">color</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gitlab.Label.color" title="Permalink to this definition">¶</a></dt>
<dd><p>The color of the label given in 6-digit hex notation with leading ‘#’ sign (e.g. #FFAABB) or one of the <a class="reference external" href="https://developer.mozilla.org/en-US/docs/Web/CSS/color_value#Color_keywords">CSS color names</a>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gitlab.Label.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gitlab.Label.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description of the label.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gitlab.Label.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gitlab.Label.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the label.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gitlab.Label.project">
<code class="descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gitlab.Label.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The name or id of the project to add the label to.</p>
</dd></dl>

<dl class="staticmethod">
<dt id="pulumi_gitlab.Label.get">
<em class="property">static </em><code class="descname">get</code><span class="sig-paren">(</span><em>resource_name</em>, <em>id</em>, <em>opts=None</em>, <em>color=None</em>, <em>description=None</em>, <em>name=None</em>, <em>project=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gitlab.Label.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Label resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.
:param str resource_name: The unique name of the resulting resource.
:param str id: The unique provider ID of the resource to lookup.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] color: The color of the label given in 6-digit hex notation with leading ‘#’ sign (e.g. #FFAABB) or one of the <a class="reference external" href="https://developer.mozilla.org/en-US/docs/Web/CSS/color_value#Color_keywords">CSS color names</a>.
:param pulumi.Input[str] description: The description of the label.
:param pulumi.Input[str] name: The name of the label.
:param pulumi.Input[str] project: The name or id of the project to add the label to.</p>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-gitlab/blob/master/website/docs/r/label.html.markdown">https://github.com/terraform-providers/terraform-provider-gitlab/blob/master/website/docs/r/label.html.markdown</a>.</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_gitlab.Label.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gitlab.Label.translate_output_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of output properties
into a format of their choosing before writing those properties to the resource object.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><strong>prop</strong> (<em>str</em>) – A property name.</td>
</tr>
<tr class="field-even field"><th class="field-name">Returns:</th><td class="field-body">A potentially transformed property name.</td>
</tr>
<tr class="field-odd field"><th class="field-name">Return type:</th><td class="field-body">str</td>
</tr>
</tbody>
</table>
</dd></dl>

<dl class="method">
<dt id="pulumi_gitlab.Label.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gitlab.Label.translate_input_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of input properties into
a format of their choosing before sending those properties to the Pulumi engine.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><strong>prop</strong> (<em>str</em>) – A property name.</td>
</tr>
<tr class="field-even field"><th class="field-name">Returns:</th><td class="field-body">A potentially transformed property name.</td>
</tr>
<tr class="field-odd field"><th class="field-name">Return type:</th><td class="field-body">str</td>
</tr>
</tbody>
</table>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_gitlab.PipelineSchedule">
<em class="property">class </em><code class="descclassname">pulumi_gitlab.</code><code class="descname">PipelineSchedule</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>active=None</em>, <em>cron=None</em>, <em>cron_timezone=None</em>, <em>description=None</em>, <em>project=None</em>, <em>ref=None</em>, <em>__props__=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gitlab.PipelineSchedule" title="Permalink to this definition">¶</a></dt>
<dd><p>This resource allows you to create and manage pipeline schedules.
For further information on clusters, consult the <a class="reference external" href="https://docs.gitlab.com/ce/user/project/pipelines/schedules.html">gitlab
documentation</a>.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>active</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – The activation of pipeline schedule. If false is set, the pipeline schedule will deactivated initially.</li>
<li><strong>cron</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The cron (e.g. <code class="docutils literal notranslate"><span class="pre">0</span> <span class="pre">1</span> <span class="pre">*</span> <span class="pre">*</span> <span class="pre">*</span></code>).</li>
<li><strong>cron_timezone</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The timezone.</li>
<li><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the pipeline schedule.</li>
<li><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name or id of the project to add the schedule to.</li>
<li><strong>ref</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The branch/tag name to be triggered.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-gitlab/blob/master/website/docs/r/pipeline_schedule.html.markdown">https://github.com/terraform-providers/terraform-provider-gitlab/blob/master/website/docs/r/pipeline_schedule.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_gitlab.PipelineSchedule.active">
<code class="descname">active</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gitlab.PipelineSchedule.active" title="Permalink to this definition">¶</a></dt>
<dd><p>The activation of pipeline schedule. If false is set, the pipeline schedule will deactivated initially.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gitlab.PipelineSchedule.cron">
<code class="descname">cron</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gitlab.PipelineSchedule.cron" title="Permalink to this definition">¶</a></dt>
<dd><p>The cron (e.g. <code class="docutils literal notranslate"><span class="pre">0</span> <span class="pre">1</span> <span class="pre">*</span> <span class="pre">*</span> <span class="pre">*</span></code>).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gitlab.PipelineSchedule.cron_timezone">
<code class="descname">cron_timezone</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gitlab.PipelineSchedule.cron_timezone" title="Permalink to this definition">¶</a></dt>
<dd><p>The timezone.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gitlab.PipelineSchedule.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gitlab.PipelineSchedule.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description of the pipeline schedule.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gitlab.PipelineSchedule.project">
<code class="descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gitlab.PipelineSchedule.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The name or id of the project to add the schedule to.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gitlab.PipelineSchedule.ref">
<code class="descname">ref</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gitlab.PipelineSchedule.ref" title="Permalink to this definition">¶</a></dt>
<dd><p>The branch/tag name to be triggered.</p>
</dd></dl>

<dl class="staticmethod">
<dt id="pulumi_gitlab.PipelineSchedule.get">
<em class="property">static </em><code class="descname">get</code><span class="sig-paren">(</span><em>resource_name</em>, <em>id</em>, <em>opts=None</em>, <em>active=None</em>, <em>cron=None</em>, <em>cron_timezone=None</em>, <em>description=None</em>, <em>project=None</em>, <em>ref=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gitlab.PipelineSchedule.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing PipelineSchedule resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.
:param str resource_name: The unique name of the resulting resource.
:param str id: The unique provider ID of the resource to lookup.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[bool] active: The activation of pipeline schedule. If false is set, the pipeline schedule will deactivated initially.
:param pulumi.Input[str] cron: The cron (e.g. <code class="docutils literal notranslate"><span class="pre">0</span> <span class="pre">1</span> <span class="pre">*</span> <span class="pre">*</span> <span class="pre">*</span></code>).
:param pulumi.Input[str] cron_timezone: The timezone.
:param pulumi.Input[str] description: The description of the pipeline schedule.
:param pulumi.Input[str] project: The name or id of the project to add the schedule to.
:param pulumi.Input[str] ref: The branch/tag name to be triggered.</p>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-gitlab/blob/master/website/docs/r/pipeline_schedule.html.markdown">https://github.com/terraform-providers/terraform-provider-gitlab/blob/master/website/docs/r/pipeline_schedule.html.markdown</a>.</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_gitlab.PipelineSchedule.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gitlab.PipelineSchedule.translate_output_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of output properties
into a format of their choosing before writing those properties to the resource object.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><strong>prop</strong> (<em>str</em>) – A property name.</td>
</tr>
<tr class="field-even field"><th class="field-name">Returns:</th><td class="field-body">A potentially transformed property name.</td>
</tr>
<tr class="field-odd field"><th class="field-name">Return type:</th><td class="field-body">str</td>
</tr>
</tbody>
</table>
</dd></dl>

<dl class="method">
<dt id="pulumi_gitlab.PipelineSchedule.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gitlab.PipelineSchedule.translate_input_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of input properties into
a format of their choosing before sending those properties to the Pulumi engine.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><strong>prop</strong> (<em>str</em>) – A property name.</td>
</tr>
<tr class="field-even field"><th class="field-name">Returns:</th><td class="field-body">A potentially transformed property name.</td>
</tr>
<tr class="field-odd field"><th class="field-name">Return type:</th><td class="field-body">str</td>
</tr>
</tbody>
</table>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_gitlab.PipelineTrigger">
<em class="property">class </em><code class="descclassname">pulumi_gitlab.</code><code class="descname">PipelineTrigger</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>description=None</em>, <em>project=None</em>, <em>__props__=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gitlab.PipelineTrigger" title="Permalink to this definition">¶</a></dt>
<dd><p>This resource allows you to create and manage pipeline triggers</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The description of the pipeline trigger.</li>
<li><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name or id of the project to add the trigger to.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-gitlab/blob/master/website/docs/r/pipeline_trigger.html.markdown">https://github.com/terraform-providers/terraform-provider-gitlab/blob/master/website/docs/r/pipeline_trigger.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_gitlab.PipelineTrigger.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gitlab.PipelineTrigger.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The description of the pipeline trigger.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gitlab.PipelineTrigger.project">
<code class="descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gitlab.PipelineTrigger.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The name or id of the project to add the trigger to.</p>
</dd></dl>

<dl class="staticmethod">
<dt id="pulumi_gitlab.PipelineTrigger.get">
<em class="property">static </em><code class="descname">get</code><span class="sig-paren">(</span><em>resource_name</em>, <em>id</em>, <em>opts=None</em>, <em>description=None</em>, <em>project=None</em>, <em>token=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gitlab.PipelineTrigger.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing PipelineTrigger resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.
:param str resource_name: The unique name of the resulting resource.
:param str id: The unique provider ID of the resource to lookup.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] description: The description of the pipeline trigger.
:param pulumi.Input[str] project: The name or id of the project to add the trigger to.</p>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-gitlab/blob/master/website/docs/r/pipeline_trigger.html.markdown">https://github.com/terraform-providers/terraform-provider-gitlab/blob/master/website/docs/r/pipeline_trigger.html.markdown</a>.</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_gitlab.PipelineTrigger.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gitlab.PipelineTrigger.translate_output_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of output properties
into a format of their choosing before writing those properties to the resource object.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><strong>prop</strong> (<em>str</em>) – A property name.</td>
</tr>
<tr class="field-even field"><th class="field-name">Returns:</th><td class="field-body">A potentially transformed property name.</td>
</tr>
<tr class="field-odd field"><th class="field-name">Return type:</th><td class="field-body">str</td>
</tr>
</tbody>
</table>
</dd></dl>

<dl class="method">
<dt id="pulumi_gitlab.PipelineTrigger.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gitlab.PipelineTrigger.translate_input_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of input properties into
a format of their choosing before sending those properties to the Pulumi engine.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><strong>prop</strong> (<em>str</em>) – A property name.</td>
</tr>
<tr class="field-even field"><th class="field-name">Returns:</th><td class="field-body">A potentially transformed property name.</td>
</tr>
<tr class="field-odd field"><th class="field-name">Return type:</th><td class="field-body">str</td>
</tr>
</tbody>
</table>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_gitlab.Project">
<em class="property">class </em><code class="descclassname">pulumi_gitlab.</code><code class="descname">Project</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>approvals_before_merge=None</em>, <em>archived=None</em>, <em>container_registry_enabled=None</em>, <em>default_branch=None</em>, <em>description=None</em>, <em>issues_enabled=None</em>, <em>merge_method=None</em>, <em>merge_requests_enabled=None</em>, <em>name=None</em>, <em>namespace_id=None</em>, <em>only_allow_merge_if_all_discussions_are_resolved=None</em>, <em>only_allow_merge_if_pipeline_succeeds=None</em>, <em>path=None</em>, <em>shared_runners_enabled=None</em>, <em>shared_with_groups=None</em>, <em>snippets_enabled=None</em>, <em>tags=None</em>, <em>visibility_level=None</em>, <em>wiki_enabled=None</em>, <em>__props__=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gitlab.Project" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a Project resource with the given unique name, props, and options.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>approvals_before_merge</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Number of merge request approvals required for merging. Default is 0.</li>
<li><strong>archived</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether the project is in read-only mode (archived). Repositories can be archived/unarchived by toggling this parameter.</li>
<li><strong>container_registry_enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enable container registry for the project.</li>
<li><strong>default_branch</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The default branch for the project.</li>
<li><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A description of the project.</li>
<li><strong>issues_enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enable issue tracking for the project.</li>
<li><strong>merge_method</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Set to <code class="docutils literal notranslate"><span class="pre">ff</span></code> to create fast-forward merges
Valid values are <code class="docutils literal notranslate"><span class="pre">merge</span></code>, <code class="docutils literal notranslate"><span class="pre">rebase_merge</span></code>, <code class="docutils literal notranslate"><span class="pre">ff</span></code>
Repositories are created with <code class="docutils literal notranslate"><span class="pre">merge</span></code> by default</li>
<li><strong>merge_requests_enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enable merge requests for the project.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the project.</li>
<li><strong>namespace_id</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The namespace (group or user) of the project. Defaults to your user.
See <code class="docutils literal notranslate"><span class="pre">.Group</span></code> for an example.</li>
<li><strong>only_allow_merge_if_all_discussions_are_resolved</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Set to true if you want allow merges only if all discussions are resolved.</li>
<li><strong>only_allow_merge_if_pipeline_succeeds</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Set to true if you want allow merges only if a pipeline succeeds.</li>
<li><strong>path</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The path of the repository.</li>
<li><strong>shared_runners_enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enable shared runners for this project.</li>
<li><strong>shared_with_groups</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Enable sharing the project with a list of groups (maps).</li>
<li><strong>snippets_enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enable snippets for the project.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Tags (topics) of the project.</li>
<li><strong>visibility_level</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Set to <code class="docutils literal notranslate"><span class="pre">public</span></code> to create a public project.
Valid values are <code class="docutils literal notranslate"><span class="pre">private</span></code>, <code class="docutils literal notranslate"><span class="pre">internal</span></code>, <code class="docutils literal notranslate"><span class="pre">public</span></code>.
Repositories are created as private by default.</li>
<li><strong>wiki_enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enable wiki for the project.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-gitlab/blob/master/website/docs/r/project.html.markdown">https://github.com/terraform-providers/terraform-provider-gitlab/blob/master/website/docs/r/project.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_gitlab.Project.approvals_before_merge">
<code class="descname">approvals_before_merge</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gitlab.Project.approvals_before_merge" title="Permalink to this definition">¶</a></dt>
<dd><p>Number of merge request approvals required for merging. Default is 0.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gitlab.Project.archived">
<code class="descname">archived</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gitlab.Project.archived" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the project is in read-only mode (archived). Repositories can be archived/unarchived by toggling this parameter.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gitlab.Project.container_registry_enabled">
<code class="descname">container_registry_enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gitlab.Project.container_registry_enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Enable container registry for the project.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gitlab.Project.default_branch">
<code class="descname">default_branch</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gitlab.Project.default_branch" title="Permalink to this definition">¶</a></dt>
<dd><p>The default branch for the project.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gitlab.Project.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gitlab.Project.description" title="Permalink to this definition">¶</a></dt>
<dd><p>A description of the project.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gitlab.Project.http_url_to_repo">
<code class="descname">http_url_to_repo</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gitlab.Project.http_url_to_repo" title="Permalink to this definition">¶</a></dt>
<dd><p>URL that can be provided to <code class="docutils literal notranslate"><span class="pre">git</span> <span class="pre">clone</span></code> to clone the
repository via HTTP.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gitlab.Project.issues_enabled">
<code class="descname">issues_enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gitlab.Project.issues_enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Enable issue tracking for the project.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gitlab.Project.merge_method">
<code class="descname">merge_method</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gitlab.Project.merge_method" title="Permalink to this definition">¶</a></dt>
<dd><p>Set to <code class="docutils literal notranslate"><span class="pre">ff</span></code> to create fast-forward merges
Valid values are <code class="docutils literal notranslate"><span class="pre">merge</span></code>, <code class="docutils literal notranslate"><span class="pre">rebase_merge</span></code>, <code class="docutils literal notranslate"><span class="pre">ff</span></code>
Repositories are created with <code class="docutils literal notranslate"><span class="pre">merge</span></code> by default</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gitlab.Project.merge_requests_enabled">
<code class="descname">merge_requests_enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gitlab.Project.merge_requests_enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Enable merge requests for the project.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gitlab.Project.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gitlab.Project.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the project.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gitlab.Project.namespace_id">
<code class="descname">namespace_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gitlab.Project.namespace_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The namespace (group or user) of the project. Defaults to your user.
See <code class="docutils literal notranslate"><span class="pre">.Group</span></code> for an example.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gitlab.Project.only_allow_merge_if_all_discussions_are_resolved">
<code class="descname">only_allow_merge_if_all_discussions_are_resolved</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gitlab.Project.only_allow_merge_if_all_discussions_are_resolved" title="Permalink to this definition">¶</a></dt>
<dd><p>Set to true if you want allow merges only if all discussions are resolved.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gitlab.Project.only_allow_merge_if_pipeline_succeeds">
<code class="descname">only_allow_merge_if_pipeline_succeeds</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gitlab.Project.only_allow_merge_if_pipeline_succeeds" title="Permalink to this definition">¶</a></dt>
<dd><p>Set to true if you want allow merges only if a pipeline succeeds.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gitlab.Project.path">
<code class="descname">path</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gitlab.Project.path" title="Permalink to this definition">¶</a></dt>
<dd><p>The path of the repository.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gitlab.Project.runners_token">
<code class="descname">runners_token</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gitlab.Project.runners_token" title="Permalink to this definition">¶</a></dt>
<dd><p>Registration token to use during runner setup.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gitlab.Project.shared_runners_enabled">
<code class="descname">shared_runners_enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gitlab.Project.shared_runners_enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Enable shared runners for this project.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gitlab.Project.shared_with_groups">
<code class="descname">shared_with_groups</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gitlab.Project.shared_with_groups" title="Permalink to this definition">¶</a></dt>
<dd><p>Enable sharing the project with a list of groups (maps).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gitlab.Project.snippets_enabled">
<code class="descname">snippets_enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gitlab.Project.snippets_enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Enable snippets for the project.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gitlab.Project.ssh_url_to_repo">
<code class="descname">ssh_url_to_repo</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gitlab.Project.ssh_url_to_repo" title="Permalink to this definition">¶</a></dt>
<dd><p>URL that can be provided to <code class="docutils literal notranslate"><span class="pre">git</span> <span class="pre">clone</span></code> to clone the
repository via SSH.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gitlab.Project.tags">
<code class="descname">tags</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gitlab.Project.tags" title="Permalink to this definition">¶</a></dt>
<dd><p>Tags (topics) of the project.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gitlab.Project.visibility_level">
<code class="descname">visibility_level</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gitlab.Project.visibility_level" title="Permalink to this definition">¶</a></dt>
<dd><p>Set to <code class="docutils literal notranslate"><span class="pre">public</span></code> to create a public project.
Valid values are <code class="docutils literal notranslate"><span class="pre">private</span></code>, <code class="docutils literal notranslate"><span class="pre">internal</span></code>, <code class="docutils literal notranslate"><span class="pre">public</span></code>.
Repositories are created as private by default.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gitlab.Project.web_url">
<code class="descname">web_url</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gitlab.Project.web_url" title="Permalink to this definition">¶</a></dt>
<dd><p>URL that can be used to find the project in a browser.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gitlab.Project.wiki_enabled">
<code class="descname">wiki_enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gitlab.Project.wiki_enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Enable wiki for the project.</p>
</dd></dl>

<dl class="staticmethod">
<dt id="pulumi_gitlab.Project.get">
<em class="property">static </em><code class="descname">get</code><span class="sig-paren">(</span><em>resource_name</em>, <em>id</em>, <em>opts=None</em>, <em>approvals_before_merge=None</em>, <em>archived=None</em>, <em>container_registry_enabled=None</em>, <em>default_branch=None</em>, <em>description=None</em>, <em>http_url_to_repo=None</em>, <em>issues_enabled=None</em>, <em>merge_method=None</em>, <em>merge_requests_enabled=None</em>, <em>name=None</em>, <em>namespace_id=None</em>, <em>only_allow_merge_if_all_discussions_are_resolved=None</em>, <em>only_allow_merge_if_pipeline_succeeds=None</em>, <em>path=None</em>, <em>runners_token=None</em>, <em>shared_runners_enabled=None</em>, <em>shared_with_groups=None</em>, <em>snippets_enabled=None</em>, <em>ssh_url_to_repo=None</em>, <em>tags=None</em>, <em>visibility_level=None</em>, <em>web_url=None</em>, <em>wiki_enabled=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gitlab.Project.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Project resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.
:param str resource_name: The unique name of the resulting resource.
:param str id: The unique provider ID of the resource to lookup.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[float] approvals_before_merge: Number of merge request approvals required for merging. Default is 0.
:param pulumi.Input[bool] archived: Whether the project is in read-only mode (archived). Repositories can be archived/unarchived by toggling this parameter.
:param pulumi.Input[bool] container_registry_enabled: Enable container registry for the project.
:param pulumi.Input[str] default_branch: The default branch for the project.
:param pulumi.Input[str] description: A description of the project.
:param pulumi.Input[str] http_url_to_repo: URL that can be provided to <code class="docutils literal notranslate"><span class="pre">git</span> <span class="pre">clone</span></code> to clone the</p>
<blockquote>
<div>repository via HTTP.</div></blockquote>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>issues_enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enable issue tracking for the project.</li>
<li><strong>merge_method</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Set to <code class="docutils literal notranslate"><span class="pre">ff</span></code> to create fast-forward merges
Valid values are <code class="docutils literal notranslate"><span class="pre">merge</span></code>, <code class="docutils literal notranslate"><span class="pre">rebase_merge</span></code>, <code class="docutils literal notranslate"><span class="pre">ff</span></code>
Repositories are created with <code class="docutils literal notranslate"><span class="pre">merge</span></code> by default</li>
<li><strong>merge_requests_enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enable merge requests for the project.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the project.</li>
<li><strong>namespace_id</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The namespace (group or user) of the project. Defaults to your user.
See <code class="docutils literal notranslate"><span class="pre">.Group</span></code> for an example.</li>
<li><strong>only_allow_merge_if_all_discussions_are_resolved</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Set to true if you want allow merges only if all discussions are resolved.</li>
<li><strong>only_allow_merge_if_pipeline_succeeds</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Set to true if you want allow merges only if a pipeline succeeds.</li>
<li><strong>path</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The path of the repository.</li>
<li><strong>runners_token</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Registration token to use during runner setup.</li>
<li><strong>shared_runners_enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enable shared runners for this project.</li>
<li><strong>shared_with_groups</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Enable sharing the project with a list of groups (maps).</li>
<li><strong>snippets_enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enable snippets for the project.</li>
<li><strong>ssh_url_to_repo</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – URL that can be provided to <code class="docutils literal notranslate"><span class="pre">git</span> <span class="pre">clone</span></code> to clone the
repository via SSH.</li>
<li><strong>tags</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – Tags (topics) of the project.</li>
<li><strong>visibility_level</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Set to <code class="docutils literal notranslate"><span class="pre">public</span></code> to create a public project.
Valid values are <code class="docutils literal notranslate"><span class="pre">private</span></code>, <code class="docutils literal notranslate"><span class="pre">internal</span></code>, <code class="docutils literal notranslate"><span class="pre">public</span></code>.
Repositories are created as private by default.</li>
<li><strong>web_url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – URL that can be used to find the project in a browser.</li>
<li><strong>wiki_enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enable wiki for the project.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-gitlab/blob/master/website/docs/r/project.html.markdown">https://github.com/terraform-providers/terraform-provider-gitlab/blob/master/website/docs/r/project.html.markdown</a>.</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_gitlab.Project.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gitlab.Project.translate_output_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of output properties
into a format of their choosing before writing those properties to the resource object.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><strong>prop</strong> (<em>str</em>) – A property name.</td>
</tr>
<tr class="field-even field"><th class="field-name">Returns:</th><td class="field-body">A potentially transformed property name.</td>
</tr>
<tr class="field-odd field"><th class="field-name">Return type:</th><td class="field-body">str</td>
</tr>
</tbody>
</table>
</dd></dl>

<dl class="method">
<dt id="pulumi_gitlab.Project.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gitlab.Project.translate_input_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of input properties into
a format of their choosing before sending those properties to the Pulumi engine.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><strong>prop</strong> (<em>str</em>) – A property name.</td>
</tr>
<tr class="field-even field"><th class="field-name">Returns:</th><td class="field-body">A potentially transformed property name.</td>
</tr>
<tr class="field-odd field"><th class="field-name">Return type:</th><td class="field-body">str</td>
</tr>
</tbody>
</table>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_gitlab.ProjectCluster">
<em class="property">class </em><code class="descclassname">pulumi_gitlab.</code><code class="descname">ProjectCluster</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>domain=None</em>, <em>enabled=None</em>, <em>environment_scope=None</em>, <em>kubernetes_api_url=None</em>, <em>kubernetes_authorization_type=None</em>, <em>kubernetes_ca_cert=None</em>, <em>kubernetes_namespace=None</em>, <em>kubernetes_token=None</em>, <em>managed=None</em>, <em>name=None</em>, <em>project=None</em>, <em>__props__=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gitlab.ProjectCluster" title="Permalink to this definition">¶</a></dt>
<dd><p>This resource allows you to create and manage project clusters for your GitLab projects.
For further information on clusters, consult the <a class="reference external" href="https://docs.gitlab.com/ce/user/project/clusters/index.html">gitlab
documentation</a>.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>domain</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The base domain of the cluster.</li>
<li><strong>enabled</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Determines if cluster is active or not. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>. This attribute cannot be read.</li>
<li><strong>environment_scope</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The associated environment to the cluster. Defaults to <code class="docutils literal notranslate"><span class="pre">*</span></code>.</li>
<li><strong>kubernetes_api_url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The URL to access the Kubernetes API.</li>
<li><strong>kubernetes_authorization_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The cluster authorization type. Valid values are <code class="docutils literal notranslate"><span class="pre">rbac</span></code>, <code class="docutils literal notranslate"><span class="pre">abac</span></code>, <code class="docutils literal notranslate"><span class="pre">unknown_authorization</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">rbac</span></code>.</li>
<li><strong>kubernetes_ca_cert</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – TLS certificate (needed if API is using a self-signed TLS certificate).</li>
<li><strong>kubernetes_namespace</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique namespace related to the project.</li>
<li><strong>kubernetes_token</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The token to authenticate against Kubernetes.</li>
<li><strong>managed</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Determines if cluster is managed by gitlab or not. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>. This attribute cannot be read.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of cluster.</li>
<li><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The id of the project to add the cluster to.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-gitlab/blob/master/website/docs/r/project_cluster.html.markdown">https://github.com/terraform-providers/terraform-provider-gitlab/blob/master/website/docs/r/project_cluster.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_gitlab.ProjectCluster.domain">
<code class="descname">domain</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gitlab.ProjectCluster.domain" title="Permalink to this definition">¶</a></dt>
<dd><p>The base domain of the cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gitlab.ProjectCluster.enabled">
<code class="descname">enabled</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gitlab.ProjectCluster.enabled" title="Permalink to this definition">¶</a></dt>
<dd><p>Determines if cluster is active or not. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>. This attribute cannot be read.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gitlab.ProjectCluster.environment_scope">
<code class="descname">environment_scope</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gitlab.ProjectCluster.environment_scope" title="Permalink to this definition">¶</a></dt>
<dd><p>The associated environment to the cluster. Defaults to <code class="docutils literal notranslate"><span class="pre">*</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gitlab.ProjectCluster.kubernetes_api_url">
<code class="descname">kubernetes_api_url</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gitlab.ProjectCluster.kubernetes_api_url" title="Permalink to this definition">¶</a></dt>
<dd><p>The URL to access the Kubernetes API.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gitlab.ProjectCluster.kubernetes_authorization_type">
<code class="descname">kubernetes_authorization_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gitlab.ProjectCluster.kubernetes_authorization_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The cluster authorization type. Valid values are <code class="docutils literal notranslate"><span class="pre">rbac</span></code>, <code class="docutils literal notranslate"><span class="pre">abac</span></code>, <code class="docutils literal notranslate"><span class="pre">unknown_authorization</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">rbac</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gitlab.ProjectCluster.kubernetes_ca_cert">
<code class="descname">kubernetes_ca_cert</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gitlab.ProjectCluster.kubernetes_ca_cert" title="Permalink to this definition">¶</a></dt>
<dd><p>TLS certificate (needed if API is using a self-signed TLS certificate).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gitlab.ProjectCluster.kubernetes_namespace">
<code class="descname">kubernetes_namespace</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gitlab.ProjectCluster.kubernetes_namespace" title="Permalink to this definition">¶</a></dt>
<dd><p>The unique namespace related to the project.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gitlab.ProjectCluster.kubernetes_token">
<code class="descname">kubernetes_token</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gitlab.ProjectCluster.kubernetes_token" title="Permalink to this definition">¶</a></dt>
<dd><p>The token to authenticate against Kubernetes.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gitlab.ProjectCluster.managed">
<code class="descname">managed</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gitlab.ProjectCluster.managed" title="Permalink to this definition">¶</a></dt>
<dd><p>Determines if cluster is managed by gitlab or not. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>. This attribute cannot be read.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gitlab.ProjectCluster.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gitlab.ProjectCluster.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of cluster.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gitlab.ProjectCluster.project">
<code class="descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gitlab.ProjectCluster.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The id of the project to add the cluster to.</p>
</dd></dl>

<dl class="staticmethod">
<dt id="pulumi_gitlab.ProjectCluster.get">
<em class="property">static </em><code class="descname">get</code><span class="sig-paren">(</span><em>resource_name</em>, <em>id</em>, <em>opts=None</em>, <em>cluster_type=None</em>, <em>created_at=None</em>, <em>domain=None</em>, <em>enabled=None</em>, <em>environment_scope=None</em>, <em>kubernetes_api_url=None</em>, <em>kubernetes_authorization_type=None</em>, <em>kubernetes_ca_cert=None</em>, <em>kubernetes_namespace=None</em>, <em>kubernetes_token=None</em>, <em>managed=None</em>, <em>name=None</em>, <em>platform_type=None</em>, <em>project=None</em>, <em>provider_type=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gitlab.ProjectCluster.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ProjectCluster resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.
:param str resource_name: The unique name of the resulting resource.
:param str id: The unique provider ID of the resource to lookup.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] domain: The base domain of the cluster.
:param pulumi.Input[bool] enabled: Determines if cluster is active or not. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>. This attribute cannot be read.
:param pulumi.Input[str] environment_scope: The associated environment to the cluster. Defaults to <code class="docutils literal notranslate"><span class="pre">*</span></code>.
:param pulumi.Input[str] kubernetes_api_url: The URL to access the Kubernetes API.
:param pulumi.Input[str] kubernetes_authorization_type: The cluster authorization type. Valid values are <code class="docutils literal notranslate"><span class="pre">rbac</span></code>, <code class="docutils literal notranslate"><span class="pre">abac</span></code>, <code class="docutils literal notranslate"><span class="pre">unknown_authorization</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">rbac</span></code>.
:param pulumi.Input[str] kubernetes_ca_cert: TLS certificate (needed if API is using a self-signed TLS certificate).
:param pulumi.Input[str] kubernetes_namespace: The unique namespace related to the project.
:param pulumi.Input[str] kubernetes_token: The token to authenticate against Kubernetes.
:param pulumi.Input[bool] managed: Determines if cluster is managed by gitlab or not. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>. This attribute cannot be read.
:param pulumi.Input[str] name: The name of cluster.
:param pulumi.Input[str] project: The id of the project to add the cluster to.</p>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-gitlab/blob/master/website/docs/r/project_cluster.html.markdown">https://github.com/terraform-providers/terraform-provider-gitlab/blob/master/website/docs/r/project_cluster.html.markdown</a>.</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_gitlab.ProjectCluster.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gitlab.ProjectCluster.translate_output_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of output properties
into a format of their choosing before writing those properties to the resource object.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><strong>prop</strong> (<em>str</em>) – A property name.</td>
</tr>
<tr class="field-even field"><th class="field-name">Returns:</th><td class="field-body">A potentially transformed property name.</td>
</tr>
<tr class="field-odd field"><th class="field-name">Return type:</th><td class="field-body">str</td>
</tr>
</tbody>
</table>
</dd></dl>

<dl class="method">
<dt id="pulumi_gitlab.ProjectCluster.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gitlab.ProjectCluster.translate_input_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of input properties into
a format of their choosing before sending those properties to the Pulumi engine.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><strong>prop</strong> (<em>str</em>) – A property name.</td>
</tr>
<tr class="field-even field"><th class="field-name">Returns:</th><td class="field-body">A potentially transformed property name.</td>
</tr>
<tr class="field-odd field"><th class="field-name">Return type:</th><td class="field-body">str</td>
</tr>
</tbody>
</table>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_gitlab.ProjectHook">
<em class="property">class </em><code class="descclassname">pulumi_gitlab.</code><code class="descname">ProjectHook</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>enable_ssl_verification=None</em>, <em>issues_events=None</em>, <em>job_events=None</em>, <em>merge_requests_events=None</em>, <em>note_events=None</em>, <em>pipeline_events=None</em>, <em>project=None</em>, <em>push_events=None</em>, <em>tag_push_events=None</em>, <em>token=None</em>, <em>url=None</em>, <em>wiki_page_events=None</em>, <em>__props__=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gitlab.ProjectHook" title="Permalink to this definition">¶</a></dt>
<dd><p>This resource allows you to create and manage hooks for your GitLab projects.
For further information on hooks, consult the <a class="reference external" href="https://docs.gitlab.com/ce/user/project/integrations/webhooks.html">gitlab
documentation</a>.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>enable_ssl_verification</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enable ssl verification when invoking
the hook.</li>
<li><strong>issues_events</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Invoke the hook for issues events.</li>
<li><strong>job_events</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Invoke the hook for job events.</li>
<li><strong>merge_requests_events</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Invoke the hook for merge requests.</li>
<li><strong>note_events</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Invoke the hook for notes events.</li>
<li><strong>pipeline_events</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Invoke the hook for pipeline events.</li>
<li><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name or id of the project to add the hook to.</li>
<li><strong>push_events</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Invoke the hook for push events.</li>
<li><strong>tag_push_events</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Invoke the hook for tag push events.</li>
<li><strong>token</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A token to present when invoking the hook.</li>
<li><strong>url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The url of the hook to invoke.</li>
<li><strong>wiki_page_events</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Invoke the hook for wiki page events.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-gitlab/blob/master/website/docs/r/project_hook.html.markdown">https://github.com/terraform-providers/terraform-provider-gitlab/blob/master/website/docs/r/project_hook.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_gitlab.ProjectHook.enable_ssl_verification">
<code class="descname">enable_ssl_verification</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gitlab.ProjectHook.enable_ssl_verification" title="Permalink to this definition">¶</a></dt>
<dd><p>Enable ssl verification when invoking
the hook.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gitlab.ProjectHook.issues_events">
<code class="descname">issues_events</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gitlab.ProjectHook.issues_events" title="Permalink to this definition">¶</a></dt>
<dd><p>Invoke the hook for issues events.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gitlab.ProjectHook.job_events">
<code class="descname">job_events</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gitlab.ProjectHook.job_events" title="Permalink to this definition">¶</a></dt>
<dd><p>Invoke the hook for job events.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gitlab.ProjectHook.merge_requests_events">
<code class="descname">merge_requests_events</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gitlab.ProjectHook.merge_requests_events" title="Permalink to this definition">¶</a></dt>
<dd><p>Invoke the hook for merge requests.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gitlab.ProjectHook.note_events">
<code class="descname">note_events</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gitlab.ProjectHook.note_events" title="Permalink to this definition">¶</a></dt>
<dd><p>Invoke the hook for notes events.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gitlab.ProjectHook.pipeline_events">
<code class="descname">pipeline_events</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gitlab.ProjectHook.pipeline_events" title="Permalink to this definition">¶</a></dt>
<dd><p>Invoke the hook for pipeline events.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gitlab.ProjectHook.project">
<code class="descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gitlab.ProjectHook.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The name or id of the project to add the hook to.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gitlab.ProjectHook.push_events">
<code class="descname">push_events</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gitlab.ProjectHook.push_events" title="Permalink to this definition">¶</a></dt>
<dd><p>Invoke the hook for push events.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gitlab.ProjectHook.tag_push_events">
<code class="descname">tag_push_events</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gitlab.ProjectHook.tag_push_events" title="Permalink to this definition">¶</a></dt>
<dd><p>Invoke the hook for tag push events.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gitlab.ProjectHook.token">
<code class="descname">token</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gitlab.ProjectHook.token" title="Permalink to this definition">¶</a></dt>
<dd><p>A token to present when invoking the hook.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gitlab.ProjectHook.url">
<code class="descname">url</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gitlab.ProjectHook.url" title="Permalink to this definition">¶</a></dt>
<dd><p>The url of the hook to invoke.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gitlab.ProjectHook.wiki_page_events">
<code class="descname">wiki_page_events</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gitlab.ProjectHook.wiki_page_events" title="Permalink to this definition">¶</a></dt>
<dd><p>Invoke the hook for wiki page events.</p>
</dd></dl>

<dl class="staticmethod">
<dt id="pulumi_gitlab.ProjectHook.get">
<em class="property">static </em><code class="descname">get</code><span class="sig-paren">(</span><em>resource_name</em>, <em>id</em>, <em>opts=None</em>, <em>enable_ssl_verification=None</em>, <em>issues_events=None</em>, <em>job_events=None</em>, <em>merge_requests_events=None</em>, <em>note_events=None</em>, <em>pipeline_events=None</em>, <em>project=None</em>, <em>push_events=None</em>, <em>tag_push_events=None</em>, <em>token=None</em>, <em>url=None</em>, <em>wiki_page_events=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gitlab.ProjectHook.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ProjectHook resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.
:param str resource_name: The unique name of the resulting resource.
:param str id: The unique provider ID of the resource to lookup.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[bool] enable_ssl_verification: Enable ssl verification when invoking</p>
<blockquote>
<div>the hook.</div></blockquote>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>issues_events</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Invoke the hook for issues events.</li>
<li><strong>job_events</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Invoke the hook for job events.</li>
<li><strong>merge_requests_events</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Invoke the hook for merge requests.</li>
<li><strong>note_events</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Invoke the hook for notes events.</li>
<li><strong>pipeline_events</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Invoke the hook for pipeline events.</li>
<li><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name or id of the project to add the hook to.</li>
<li><strong>push_events</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Invoke the hook for push events.</li>
<li><strong>tag_push_events</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Invoke the hook for tag push events.</li>
<li><strong>token</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A token to present when invoking the hook.</li>
<li><strong>url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The url of the hook to invoke.</li>
<li><strong>wiki_page_events</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Invoke the hook for wiki page events.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-gitlab/blob/master/website/docs/r/project_hook.html.markdown">https://github.com/terraform-providers/terraform-provider-gitlab/blob/master/website/docs/r/project_hook.html.markdown</a>.</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_gitlab.ProjectHook.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gitlab.ProjectHook.translate_output_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of output properties
into a format of their choosing before writing those properties to the resource object.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><strong>prop</strong> (<em>str</em>) – A property name.</td>
</tr>
<tr class="field-even field"><th class="field-name">Returns:</th><td class="field-body">A potentially transformed property name.</td>
</tr>
<tr class="field-odd field"><th class="field-name">Return type:</th><td class="field-body">str</td>
</tr>
</tbody>
</table>
</dd></dl>

<dl class="method">
<dt id="pulumi_gitlab.ProjectHook.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gitlab.ProjectHook.translate_input_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of input properties into
a format of their choosing before sending those properties to the Pulumi engine.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><strong>prop</strong> (<em>str</em>) – A property name.</td>
</tr>
<tr class="field-even field"><th class="field-name">Returns:</th><td class="field-body">A potentially transformed property name.</td>
</tr>
<tr class="field-odd field"><th class="field-name">Return type:</th><td class="field-body">str</td>
</tr>
</tbody>
</table>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_gitlab.ProjectMembership">
<em class="property">class </em><code class="descclassname">pulumi_gitlab.</code><code class="descname">ProjectMembership</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>access_level=None</em>, <em>project_id=None</em>, <em>user_id=None</em>, <em>__props__=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gitlab.ProjectMembership" title="Permalink to this definition">¶</a></dt>
<dd><p>This resource allows you to add a current user to an existing project with a set access level.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>access_level</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – One of five levels of access to the project.</li>
<li><strong>project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The id of the project.</li>
<li><strong>user_id</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The id of the user.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-gitlab/blob/master/website/docs/r/project_membership.html.markdown">https://github.com/terraform-providers/terraform-provider-gitlab/blob/master/website/docs/r/project_membership.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_gitlab.ProjectMembership.access_level">
<code class="descname">access_level</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gitlab.ProjectMembership.access_level" title="Permalink to this definition">¶</a></dt>
<dd><p>One of five levels of access to the project.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gitlab.ProjectMembership.project_id">
<code class="descname">project_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gitlab.ProjectMembership.project_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The id of the project.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gitlab.ProjectMembership.user_id">
<code class="descname">user_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gitlab.ProjectMembership.user_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The id of the user.</p>
</dd></dl>

<dl class="staticmethod">
<dt id="pulumi_gitlab.ProjectMembership.get">
<em class="property">static </em><code class="descname">get</code><span class="sig-paren">(</span><em>resource_name</em>, <em>id</em>, <em>opts=None</em>, <em>access_level=None</em>, <em>project_id=None</em>, <em>user_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gitlab.ProjectMembership.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ProjectMembership resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.
:param str resource_name: The unique name of the resulting resource.
:param str id: The unique provider ID of the resource to lookup.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] access_level: One of five levels of access to the project.
:param pulumi.Input[str] project_id: The id of the project.
:param pulumi.Input[float] user_id: The id of the user.</p>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-gitlab/blob/master/website/docs/r/project_membership.html.markdown">https://github.com/terraform-providers/terraform-provider-gitlab/blob/master/website/docs/r/project_membership.html.markdown</a>.</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_gitlab.ProjectMembership.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gitlab.ProjectMembership.translate_output_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of output properties
into a format of their choosing before writing those properties to the resource object.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><strong>prop</strong> (<em>str</em>) – A property name.</td>
</tr>
<tr class="field-even field"><th class="field-name">Returns:</th><td class="field-body">A potentially transformed property name.</td>
</tr>
<tr class="field-odd field"><th class="field-name">Return type:</th><td class="field-body">str</td>
</tr>
</tbody>
</table>
</dd></dl>

<dl class="method">
<dt id="pulumi_gitlab.ProjectMembership.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gitlab.ProjectMembership.translate_input_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of input properties into
a format of their choosing before sending those properties to the Pulumi engine.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><strong>prop</strong> (<em>str</em>) – A property name.</td>
</tr>
<tr class="field-even field"><th class="field-name">Returns:</th><td class="field-body">A potentially transformed property name.</td>
</tr>
<tr class="field-odd field"><th class="field-name">Return type:</th><td class="field-body">str</td>
</tr>
</tbody>
</table>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_gitlab.ProjectVariable">
<em class="property">class </em><code class="descclassname">pulumi_gitlab.</code><code class="descname">ProjectVariable</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>key=None</em>, <em>project=None</em>, <em>protected=None</em>, <em>value=None</em>, <em>__props__=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gitlab.ProjectVariable" title="Permalink to this definition">¶</a></dt>
<dd><p>This resource allows you to create and manage CI/CD variables for your GitLab projects.
For further information on variables, consult the <a class="reference external" href="https://docs.gitlab.com/ce/ci/variables/README.html#variables">gitlab
documentation</a>.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the variable.</li>
<li><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name or id of the project to add the hook to.</li>
<li><strong>protected</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If set to <code class="docutils literal notranslate"><span class="pre">true</span></code>, the variable will be passed only to pipelines running on protected branches and tags. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</li>
<li><strong>value</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The value of the variable.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-gitlab/blob/master/website/docs/r/project_variable.html.markdown">https://github.com/terraform-providers/terraform-provider-gitlab/blob/master/website/docs/r/project_variable.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_gitlab.ProjectVariable.key">
<code class="descname">key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gitlab.ProjectVariable.key" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the variable.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gitlab.ProjectVariable.project">
<code class="descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gitlab.ProjectVariable.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The name or id of the project to add the hook to.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gitlab.ProjectVariable.protected">
<code class="descname">protected</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gitlab.ProjectVariable.protected" title="Permalink to this definition">¶</a></dt>
<dd><p>If set to <code class="docutils literal notranslate"><span class="pre">true</span></code>, the variable will be passed only to pipelines running on protected branches and tags. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gitlab.ProjectVariable.value">
<code class="descname">value</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gitlab.ProjectVariable.value" title="Permalink to this definition">¶</a></dt>
<dd><p>The value of the variable.</p>
</dd></dl>

<dl class="staticmethod">
<dt id="pulumi_gitlab.ProjectVariable.get">
<em class="property">static </em><code class="descname">get</code><span class="sig-paren">(</span><em>resource_name</em>, <em>id</em>, <em>opts=None</em>, <em>key=None</em>, <em>project=None</em>, <em>protected=None</em>, <em>value=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gitlab.ProjectVariable.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ProjectVariable resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.
:param str resource_name: The unique name of the resulting resource.
:param str id: The unique provider ID of the resource to lookup.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] key: The name of the variable.
:param pulumi.Input[str] project: The name or id of the project to add the hook to.
:param pulumi.Input[bool] protected: If set to <code class="docutils literal notranslate"><span class="pre">true</span></code>, the variable will be passed only to pipelines running on protected branches and tags. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.
:param pulumi.Input[str] value: The value of the variable.</p>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-gitlab/blob/master/website/docs/r/project_variable.html.markdown">https://github.com/terraform-providers/terraform-provider-gitlab/blob/master/website/docs/r/project_variable.html.markdown</a>.</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_gitlab.ProjectVariable.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gitlab.ProjectVariable.translate_output_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of output properties
into a format of their choosing before writing those properties to the resource object.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><strong>prop</strong> (<em>str</em>) – A property name.</td>
</tr>
<tr class="field-even field"><th class="field-name">Returns:</th><td class="field-body">A potentially transformed property name.</td>
</tr>
<tr class="field-odd field"><th class="field-name">Return type:</th><td class="field-body">str</td>
</tr>
</tbody>
</table>
</dd></dl>

<dl class="method">
<dt id="pulumi_gitlab.ProjectVariable.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gitlab.ProjectVariable.translate_input_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of input properties into
a format of their choosing before sending those properties to the Pulumi engine.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><strong>prop</strong> (<em>str</em>) – A property name.</td>
</tr>
<tr class="field-even field"><th class="field-name">Returns:</th><td class="field-body">A potentially transformed property name.</td>
</tr>
<tr class="field-odd field"><th class="field-name">Return type:</th><td class="field-body">str</td>
</tr>
</tbody>
</table>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_gitlab.Provider">
<em class="property">class </em><code class="descclassname">pulumi_gitlab.</code><code class="descname">Provider</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>base_url=None</em>, <em>cacert_file=None</em>, <em>insecure=None</em>, <em>token=None</em>, <em>__props__=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gitlab.Provider" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider type for the gitlab package. By default, resources use package-wide configuration
settings, however an explicit <code class="docutils literal notranslate"><span class="pre">Provider</span></code> instance may be created and passed during resource
construction to achieve fine-grained programmatic control over provider settings. See the
<a class="reference external" href="https://www.pulumi.com/docs/intro/concepts/programming-model/#providers">documentation</a> for more information.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-gitlab/blob/master/website/docs/index.html.markdown">https://github.com/terraform-providers/terraform-provider-gitlab/blob/master/website/docs/index.html.markdown</a>.</div></blockquote>
<dl class="staticmethod">
<dt id="pulumi_gitlab.Provider.get">
<em class="property">static </em><code class="descname">get</code><span class="sig-paren">(</span><em>resource_name</em>, <em>id</em>, <em>opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gitlab.Provider.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Provider resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.
:param str resource_name: The unique name of the resulting resource.
:param str id: The unique provider ID of the resource to lookup.
:param pulumi.ResourceOptions opts: Options for the resource.</p>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-gitlab/blob/master/website/docs/index.html.markdown">https://github.com/terraform-providers/terraform-provider-gitlab/blob/master/website/docs/index.html.markdown</a>.</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_gitlab.Provider.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gitlab.Provider.translate_output_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of output properties
into a format of their choosing before writing those properties to the resource object.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><strong>prop</strong> (<em>str</em>) – A property name.</td>
</tr>
<tr class="field-even field"><th class="field-name">Returns:</th><td class="field-body">A potentially transformed property name.</td>
</tr>
<tr class="field-odd field"><th class="field-name">Return type:</th><td class="field-body">str</td>
</tr>
</tbody>
</table>
</dd></dl>

<dl class="method">
<dt id="pulumi_gitlab.Provider.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gitlab.Provider.translate_input_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of input properties into
a format of their choosing before sending those properties to the Pulumi engine.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><strong>prop</strong> (<em>str</em>) – A property name.</td>
</tr>
<tr class="field-even field"><th class="field-name">Returns:</th><td class="field-body">A potentially transformed property name.</td>
</tr>
<tr class="field-odd field"><th class="field-name">Return type:</th><td class="field-body">str</td>
</tr>
</tbody>
</table>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_gitlab.ServiceJira">
<em class="property">class </em><code class="descclassname">pulumi_gitlab.</code><code class="descname">ServiceJira</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>jira_issue_transition_id=None</em>, <em>password=None</em>, <em>project=None</em>, <em>project_key=None</em>, <em>url=None</em>, <em>username=None</em>, <em>__props__=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gitlab.ServiceJira" title="Permalink to this definition">¶</a></dt>
<dd><p>This resource allows you to manage Jira integration.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>jira_issue_transition_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of a transition that moves issues to a closed state. You can find this number under the JIRA workflow administration (Administration &gt; Issues &gt; Workflows) by selecting View under Operations of the desired workflow of your project. By default, this ID is set to 2.</li>
<li><strong>password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The password of the user created to be used with GitLab/JIRA.</li>
<li><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – ID of the project you want to activate integration on.</li>
<li><strong>project_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The short identifier for your JIRA project, all uppercase, e.g., PROJ.</li>
<li><strong>url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The URL to the JIRA project which is being linked to this GitLab project. For example, <a class="reference external" href="https://jira.example.com">https://jira.example.com</a>.</li>
<li><strong>username</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The username of the user created to be used with GitLab/JIRA.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-gitlab/blob/master/website/docs/r/service_jira.html.markdown">https://github.com/terraform-providers/terraform-provider-gitlab/blob/master/website/docs/r/service_jira.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_gitlab.ServiceJira.jira_issue_transition_id">
<code class="descname">jira_issue_transition_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gitlab.ServiceJira.jira_issue_transition_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of a transition that moves issues to a closed state. You can find this number under the JIRA workflow administration (Administration &gt; Issues &gt; Workflows) by selecting View under Operations of the desired workflow of your project. By default, this ID is set to 2.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gitlab.ServiceJira.password">
<code class="descname">password</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gitlab.ServiceJira.password" title="Permalink to this definition">¶</a></dt>
<dd><p>The password of the user created to be used with GitLab/JIRA.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gitlab.ServiceJira.project">
<code class="descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gitlab.ServiceJira.project" title="Permalink to this definition">¶</a></dt>
<dd><p>ID of the project you want to activate integration on.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gitlab.ServiceJira.project_key">
<code class="descname">project_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gitlab.ServiceJira.project_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The short identifier for your JIRA project, all uppercase, e.g., PROJ.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gitlab.ServiceJira.url">
<code class="descname">url</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gitlab.ServiceJira.url" title="Permalink to this definition">¶</a></dt>
<dd><p>The URL to the JIRA project which is being linked to this GitLab project. For example, <a class="reference external" href="https://jira.example.com">https://jira.example.com</a>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gitlab.ServiceJira.username">
<code class="descname">username</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gitlab.ServiceJira.username" title="Permalink to this definition">¶</a></dt>
<dd><p>The username of the user created to be used with GitLab/JIRA.</p>
</dd></dl>

<dl class="staticmethod">
<dt id="pulumi_gitlab.ServiceJira.get">
<em class="property">static </em><code class="descname">get</code><span class="sig-paren">(</span><em>resource_name</em>, <em>id</em>, <em>opts=None</em>, <em>active=None</em>, <em>created_at=None</em>, <em>jira_issue_transition_id=None</em>, <em>password=None</em>, <em>project=None</em>, <em>project_key=None</em>, <em>title=None</em>, <em>updated_at=None</em>, <em>url=None</em>, <em>username=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gitlab.ServiceJira.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ServiceJira resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.
:param str resource_name: The unique name of the resulting resource.
:param str id: The unique provider ID of the resource to lookup.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] jira_issue_transition_id: The ID of a transition that moves issues to a closed state. You can find this number under the JIRA workflow administration (Administration &gt; Issues &gt; Workflows) by selecting View under Operations of the desired workflow of your project. By default, this ID is set to 2.
:param pulumi.Input[str] password: The password of the user created to be used with GitLab/JIRA.
:param pulumi.Input[str] project: ID of the project you want to activate integration on.
:param pulumi.Input[str] project_key: The short identifier for your JIRA project, all uppercase, e.g., PROJ.
:param pulumi.Input[str] url: The URL to the JIRA project which is being linked to this GitLab project. For example, <a class="reference external" href="https://jira.example.com">https://jira.example.com</a>.
:param pulumi.Input[str] username: The username of the user created to be used with GitLab/JIRA.</p>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-gitlab/blob/master/website/docs/r/service_jira.html.markdown">https://github.com/terraform-providers/terraform-provider-gitlab/blob/master/website/docs/r/service_jira.html.markdown</a>.</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_gitlab.ServiceJira.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gitlab.ServiceJira.translate_output_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of output properties
into a format of their choosing before writing those properties to the resource object.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><strong>prop</strong> (<em>str</em>) – A property name.</td>
</tr>
<tr class="field-even field"><th class="field-name">Returns:</th><td class="field-body">A potentially transformed property name.</td>
</tr>
<tr class="field-odd field"><th class="field-name">Return type:</th><td class="field-body">str</td>
</tr>
</tbody>
</table>
</dd></dl>

<dl class="method">
<dt id="pulumi_gitlab.ServiceJira.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gitlab.ServiceJira.translate_input_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of input properties into
a format of their choosing before sending those properties to the Pulumi engine.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><strong>prop</strong> (<em>str</em>) – A property name.</td>
</tr>
<tr class="field-even field"><th class="field-name">Returns:</th><td class="field-body">A potentially transformed property name.</td>
</tr>
<tr class="field-odd field"><th class="field-name">Return type:</th><td class="field-body">str</td>
</tr>
</tbody>
</table>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_gitlab.ServiceSlack">
<em class="property">class </em><code class="descclassname">pulumi_gitlab.</code><code class="descname">ServiceSlack</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>confidential_issue_channel=None</em>, <em>confidential_issues_events=None</em>, <em>confidential_note_events=None</em>, <em>issue_channel=None</em>, <em>issues_events=None</em>, <em>merge_request_channel=None</em>, <em>merge_requests_events=None</em>, <em>note_channel=None</em>, <em>note_events=None</em>, <em>notify_only_broken_pipelines=None</em>, <em>notify_only_default_branch=None</em>, <em>pipeline_channel=None</em>, <em>pipeline_events=None</em>, <em>project=None</em>, <em>push_channel=None</em>, <em>push_events=None</em>, <em>tag_push_channel=None</em>, <em>tag_push_events=None</em>, <em>username=None</em>, <em>webhook=None</em>, <em>wiki_page_channel=None</em>, <em>wiki_page_events=None</em>, <em>__props__=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gitlab.ServiceSlack" title="Permalink to this definition">¶</a></dt>
<dd><p>This resource allows you to manage Slack notifications integration.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>confidential_issue_channel</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the channel to receive confidential issue events notifications.</li>
<li><strong>confidential_issues_events</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enable notifications for confidential issues events.</li>
<li><strong>confidential_note_events</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enable notifications for confidential note events.</li>
<li><strong>issue_channel</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the channel to receive issue events notifications.</li>
<li><strong>issues_events</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enable notifications for issues events.</li>
<li><strong>merge_request_channel</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the channel to receive merge request events notifications.</li>
<li><strong>merge_requests_events</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enable notifications for merge requests events.</li>
<li><strong>note_channel</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the channel to receive note events notifications.</li>
<li><strong>note_events</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enable notifications for note events.</li>
<li><strong>notify_only_broken_pipelines</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Send notifications for broken pipelines.</li>
<li><strong>notify_only_default_branch</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Send notifications only for the default branch.</li>
<li><strong>pipeline_channel</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the channel to receive pipeline events notifications.</li>
<li><strong>pipeline_events</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enable notifications for pipeline events.</li>
<li><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – ID of the project you want to activate integration on.</li>
<li><strong>push_channel</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the channel to receive push events notifications.</li>
<li><strong>push_events</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enable notifications for push events.</li>
<li><strong>tag_push_channel</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the channel to receive tag push events notifications.</li>
<li><strong>tag_push_events</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enable notifications for tag push events.</li>
<li><strong>username</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Username to use.</li>
<li><strong>webhook</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Webhook URL (ex.: <a class="reference external" href="https://hooks.slack.com/services/">https://hooks.slack.com/services/</a>…)</li>
<li><strong>wiki_page_channel</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the channel to receive wiki page events notifications.</li>
<li><strong>wiki_page_events</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Enable notifications for wiki page events.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-gitlab/blob/master/website/docs/r/service_slack.html.markdown">https://github.com/terraform-providers/terraform-provider-gitlab/blob/master/website/docs/r/service_slack.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_gitlab.ServiceSlack.confidential_issue_channel">
<code class="descname">confidential_issue_channel</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gitlab.ServiceSlack.confidential_issue_channel" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the channel to receive confidential issue events notifications.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gitlab.ServiceSlack.confidential_issues_events">
<code class="descname">confidential_issues_events</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gitlab.ServiceSlack.confidential_issues_events" title="Permalink to this definition">¶</a></dt>
<dd><p>Enable notifications for confidential issues events.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gitlab.ServiceSlack.confidential_note_events">
<code class="descname">confidential_note_events</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gitlab.ServiceSlack.confidential_note_events" title="Permalink to this definition">¶</a></dt>
<dd><p>Enable notifications for confidential note events.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gitlab.ServiceSlack.issue_channel">
<code class="descname">issue_channel</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gitlab.ServiceSlack.issue_channel" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the channel to receive issue events notifications.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gitlab.ServiceSlack.issues_events">
<code class="descname">issues_events</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gitlab.ServiceSlack.issues_events" title="Permalink to this definition">¶</a></dt>
<dd><p>Enable notifications for issues events.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gitlab.ServiceSlack.merge_request_channel">
<code class="descname">merge_request_channel</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gitlab.ServiceSlack.merge_request_channel" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the channel to receive merge request events notifications.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gitlab.ServiceSlack.merge_requests_events">
<code class="descname">merge_requests_events</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gitlab.ServiceSlack.merge_requests_events" title="Permalink to this definition">¶</a></dt>
<dd><p>Enable notifications for merge requests events.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gitlab.ServiceSlack.note_channel">
<code class="descname">note_channel</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gitlab.ServiceSlack.note_channel" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the channel to receive note events notifications.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gitlab.ServiceSlack.note_events">
<code class="descname">note_events</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gitlab.ServiceSlack.note_events" title="Permalink to this definition">¶</a></dt>
<dd><p>Enable notifications for note events.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gitlab.ServiceSlack.notify_only_broken_pipelines">
<code class="descname">notify_only_broken_pipelines</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gitlab.ServiceSlack.notify_only_broken_pipelines" title="Permalink to this definition">¶</a></dt>
<dd><p>Send notifications for broken pipelines.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gitlab.ServiceSlack.notify_only_default_branch">
<code class="descname">notify_only_default_branch</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gitlab.ServiceSlack.notify_only_default_branch" title="Permalink to this definition">¶</a></dt>
<dd><p>Send notifications only for the default branch.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gitlab.ServiceSlack.pipeline_channel">
<code class="descname">pipeline_channel</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gitlab.ServiceSlack.pipeline_channel" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the channel to receive pipeline events notifications.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gitlab.ServiceSlack.pipeline_events">
<code class="descname">pipeline_events</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gitlab.ServiceSlack.pipeline_events" title="Permalink to this definition">¶</a></dt>
<dd><p>Enable notifications for pipeline events.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gitlab.ServiceSlack.project">
<code class="descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gitlab.ServiceSlack.project" title="Permalink to this definition">¶</a></dt>
<dd><p>ID of the project you want to activate integration on.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gitlab.ServiceSlack.push_channel">
<code class="descname">push_channel</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gitlab.ServiceSlack.push_channel" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the channel to receive push events notifications.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gitlab.ServiceSlack.push_events">
<code class="descname">push_events</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gitlab.ServiceSlack.push_events" title="Permalink to this definition">¶</a></dt>
<dd><p>Enable notifications for push events.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gitlab.ServiceSlack.tag_push_channel">
<code class="descname">tag_push_channel</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gitlab.ServiceSlack.tag_push_channel" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the channel to receive tag push events notifications.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gitlab.ServiceSlack.tag_push_events">
<code class="descname">tag_push_events</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gitlab.ServiceSlack.tag_push_events" title="Permalink to this definition">¶</a></dt>
<dd><p>Enable notifications for tag push events.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gitlab.ServiceSlack.username">
<code class="descname">username</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gitlab.ServiceSlack.username" title="Permalink to this definition">¶</a></dt>
<dd><p>Username to use.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gitlab.ServiceSlack.webhook">
<code class="descname">webhook</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gitlab.ServiceSlack.webhook" title="Permalink to this definition">¶</a></dt>
<dd><p>Webhook URL (ex.: <a class="reference external" href="https://hooks.slack.com/services/">https://hooks.slack.com/services/</a>…)</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gitlab.ServiceSlack.wiki_page_channel">
<code class="descname">wiki_page_channel</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gitlab.ServiceSlack.wiki_page_channel" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the channel to receive wiki page events notifications.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gitlab.ServiceSlack.wiki_page_events">
<code class="descname">wiki_page_events</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gitlab.ServiceSlack.wiki_page_events" title="Permalink to this definition">¶</a></dt>
<dd><p>Enable notifications for wiki page events.</p>
</dd></dl>

<dl class="staticmethod">
<dt id="pulumi_gitlab.ServiceSlack.get">
<em class="property">static </em><code class="descname">get</code><span class="sig-paren">(</span><em>resource_name</em>, <em>id</em>, <em>opts=None</em>, <em>confidential_issue_channel=None</em>, <em>confidential_issues_events=None</em>, <em>confidential_note_events=None</em>, <em>issue_channel=None</em>, <em>issues_events=None</em>, <em>job_events=None</em>, <em>merge_request_channel=None</em>, <em>merge_requests_events=None</em>, <em>note_channel=None</em>, <em>note_events=None</em>, <em>notify_only_broken_pipelines=None</em>, <em>notify_only_default_branch=None</em>, <em>pipeline_channel=None</em>, <em>pipeline_events=None</em>, <em>project=None</em>, <em>push_channel=None</em>, <em>push_events=None</em>, <em>tag_push_channel=None</em>, <em>tag_push_events=None</em>, <em>username=None</em>, <em>webhook=None</em>, <em>wiki_page_channel=None</em>, <em>wiki_page_events=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gitlab.ServiceSlack.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ServiceSlack resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.
:param str resource_name: The unique name of the resulting resource.
:param str id: The unique provider ID of the resource to lookup.
:param pulumi.ResourceOptions opts: Options for the resource.
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
:param pulumi.Input[bool] notify_only_default_branch: Send notifications only for the default branch.
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
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-gitlab/blob/master/website/docs/r/service_slack.html.markdown">https://github.com/terraform-providers/terraform-provider-gitlab/blob/master/website/docs/r/service_slack.html.markdown</a>.</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_gitlab.ServiceSlack.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gitlab.ServiceSlack.translate_output_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of output properties
into a format of their choosing before writing those properties to the resource object.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><strong>prop</strong> (<em>str</em>) – A property name.</td>
</tr>
<tr class="field-even field"><th class="field-name">Returns:</th><td class="field-body">A potentially transformed property name.</td>
</tr>
<tr class="field-odd field"><th class="field-name">Return type:</th><td class="field-body">str</td>
</tr>
</tbody>
</table>
</dd></dl>

<dl class="method">
<dt id="pulumi_gitlab.ServiceSlack.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gitlab.ServiceSlack.translate_input_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of input properties into
a format of their choosing before sending those properties to the Pulumi engine.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><strong>prop</strong> (<em>str</em>) – A property name.</td>
</tr>
<tr class="field-even field"><th class="field-name">Returns:</th><td class="field-body">A potentially transformed property name.</td>
</tr>
<tr class="field-odd field"><th class="field-name">Return type:</th><td class="field-body">str</td>
</tr>
</tbody>
</table>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_gitlab.TagProtection">
<em class="property">class </em><code class="descclassname">pulumi_gitlab.</code><code class="descname">TagProtection</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>create_access_level=None</em>, <em>project=None</em>, <em>tag=None</em>, <em>__props__=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gitlab.TagProtection" title="Permalink to this definition">¶</a></dt>
<dd><p>This resource allows you to protect a specific tag or wildcard by an access level so that the user with less access level cannot Create the tags.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>create_access_level</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – One of five levels of access to the project.</li>
<li><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The id of the project.</li>
<li><strong>tag</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the tag or wildcard.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-gitlab/blob/master/website/docs/r/tag_protection.html.markdown">https://github.com/terraform-providers/terraform-provider-gitlab/blob/master/website/docs/r/tag_protection.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_gitlab.TagProtection.create_access_level">
<code class="descname">create_access_level</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gitlab.TagProtection.create_access_level" title="Permalink to this definition">¶</a></dt>
<dd><p>One of five levels of access to the project.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gitlab.TagProtection.project">
<code class="descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gitlab.TagProtection.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The id of the project.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gitlab.TagProtection.tag">
<code class="descname">tag</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gitlab.TagProtection.tag" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the tag or wildcard.</p>
</dd></dl>

<dl class="staticmethod">
<dt id="pulumi_gitlab.TagProtection.get">
<em class="property">static </em><code class="descname">get</code><span class="sig-paren">(</span><em>resource_name</em>, <em>id</em>, <em>opts=None</em>, <em>create_access_level=None</em>, <em>project=None</em>, <em>tag=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gitlab.TagProtection.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing TagProtection resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.
:param str resource_name: The unique name of the resulting resource.
:param str id: The unique provider ID of the resource to lookup.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] create_access_level: One of five levels of access to the project.
:param pulumi.Input[str] project: The id of the project.
:param pulumi.Input[str] tag: Name of the tag or wildcard.</p>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-gitlab/blob/master/website/docs/r/tag_protection.html.markdown">https://github.com/terraform-providers/terraform-provider-gitlab/blob/master/website/docs/r/tag_protection.html.markdown</a>.</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_gitlab.TagProtection.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gitlab.TagProtection.translate_output_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of output properties
into a format of their choosing before writing those properties to the resource object.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><strong>prop</strong> (<em>str</em>) – A property name.</td>
</tr>
<tr class="field-even field"><th class="field-name">Returns:</th><td class="field-body">A potentially transformed property name.</td>
</tr>
<tr class="field-odd field"><th class="field-name">Return type:</th><td class="field-body">str</td>
</tr>
</tbody>
</table>
</dd></dl>

<dl class="method">
<dt id="pulumi_gitlab.TagProtection.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gitlab.TagProtection.translate_input_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of input properties into
a format of their choosing before sending those properties to the Pulumi engine.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><strong>prop</strong> (<em>str</em>) – A property name.</td>
</tr>
<tr class="field-even field"><th class="field-name">Returns:</th><td class="field-body">A potentially transformed property name.</td>
</tr>
<tr class="field-odd field"><th class="field-name">Return type:</th><td class="field-body">str</td>
</tr>
</tbody>
</table>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_gitlab.User">
<em class="property">class </em><code class="descclassname">pulumi_gitlab.</code><code class="descname">User</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>can_create_group=None</em>, <em>email=None</em>, <em>is_admin=None</em>, <em>is_external=None</em>, <em>name=None</em>, <em>password=None</em>, <em>projects_limit=None</em>, <em>skip_confirmation=None</em>, <em>username=None</em>, <em>__props__=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gitlab.User" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a User resource with the given unique name, props, and options.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>can_create_group</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean, defaults to false. Whether to allow the user to create groups.</li>
<li><strong>email</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The e-mail address of the user.</li>
<li><strong>is_admin</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean, defaults to false.  Whether to enable administrative priviledges
for the user.</li>
<li><strong>is_external</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean, defaults to false. Whether a user has access only to some internal or private projects. External users can only access projects to which they are explicitly granted access.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the user.</li>
<li><strong>password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The password of the user.</li>
<li><strong>projects_limit</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Integer, defaults to 0.  Number of projects user can create.</li>
<li><strong>skip_confirmation</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean, defaults to true. Whether to skip confirmation.</li>
<li><strong>username</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The username of the user.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-gitlab/blob/master/website/docs/r/user.html.markdown">https://github.com/terraform-providers/terraform-provider-gitlab/blob/master/website/docs/r/user.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_gitlab.User.can_create_group">
<code class="descname">can_create_group</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gitlab.User.can_create_group" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean, defaults to false. Whether to allow the user to create groups.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gitlab.User.email">
<code class="descname">email</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gitlab.User.email" title="Permalink to this definition">¶</a></dt>
<dd><p>The e-mail address of the user.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gitlab.User.is_admin">
<code class="descname">is_admin</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gitlab.User.is_admin" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean, defaults to false.  Whether to enable administrative priviledges
for the user.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gitlab.User.is_external">
<code class="descname">is_external</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gitlab.User.is_external" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean, defaults to false. Whether a user has access only to some internal or private projects. External users can only access projects to which they are explicitly granted access.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gitlab.User.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gitlab.User.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the user.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gitlab.User.password">
<code class="descname">password</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gitlab.User.password" title="Permalink to this definition">¶</a></dt>
<dd><p>The password of the user.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gitlab.User.projects_limit">
<code class="descname">projects_limit</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gitlab.User.projects_limit" title="Permalink to this definition">¶</a></dt>
<dd><p>Integer, defaults to 0.  Number of projects user can create.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gitlab.User.skip_confirmation">
<code class="descname">skip_confirmation</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gitlab.User.skip_confirmation" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean, defaults to true. Whether to skip confirmation.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gitlab.User.username">
<code class="descname">username</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gitlab.User.username" title="Permalink to this definition">¶</a></dt>
<dd><p>The username of the user.</p>
</dd></dl>

<dl class="staticmethod">
<dt id="pulumi_gitlab.User.get">
<em class="property">static </em><code class="descname">get</code><span class="sig-paren">(</span><em>resource_name</em>, <em>id</em>, <em>opts=None</em>, <em>can_create_group=None</em>, <em>email=None</em>, <em>is_admin=None</em>, <em>is_external=None</em>, <em>name=None</em>, <em>password=None</em>, <em>projects_limit=None</em>, <em>skip_confirmation=None</em>, <em>username=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gitlab.User.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing User resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.
:param str resource_name: The unique name of the resulting resource.
:param str id: The unique provider ID of the resource to lookup.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[bool] can_create_group: Boolean, defaults to false. Whether to allow the user to create groups.
:param pulumi.Input[str] email: The e-mail address of the user.
:param pulumi.Input[bool] is_admin: Boolean, defaults to false.  Whether to enable administrative priviledges</p>
<blockquote>
<div>for the user.</div></blockquote>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>is_external</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean, defaults to false. Whether a user has access only to some internal or private projects. External users can only access projects to which they are explicitly granted access.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the user.</li>
<li><strong>password</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The password of the user.</li>
<li><strong>projects_limit</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Integer, defaults to 0.  Number of projects user can create.</li>
<li><strong>skip_confirmation</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean, defaults to true. Whether to skip confirmation.</li>
<li><strong>username</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The username of the user.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-gitlab/blob/master/website/docs/r/user.html.markdown">https://github.com/terraform-providers/terraform-provider-gitlab/blob/master/website/docs/r/user.html.markdown</a>.</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_gitlab.User.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gitlab.User.translate_output_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of output properties
into a format of their choosing before writing those properties to the resource object.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><strong>prop</strong> (<em>str</em>) – A property name.</td>
</tr>
<tr class="field-even field"><th class="field-name">Returns:</th><td class="field-body">A potentially transformed property name.</td>
</tr>
<tr class="field-odd field"><th class="field-name">Return type:</th><td class="field-body">str</td>
</tr>
</tbody>
</table>
</dd></dl>

<dl class="method">
<dt id="pulumi_gitlab.User.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gitlab.User.translate_input_property" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides subclasses of Resource an opportunity to translate names of input properties into
a format of their choosing before sending those properties to the Pulumi engine.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><strong>prop</strong> (<em>str</em>) – A property name.</td>
</tr>
<tr class="field-even field"><th class="field-name">Returns:</th><td class="field-body">A potentially transformed property name.</td>
</tr>
<tr class="field-odd field"><th class="field-name">Return type:</th><td class="field-body">str</td>
</tr>
</tbody>
</table>
</dd></dl>

</dd></dl>

<dl class="function">
<dt id="pulumi_gitlab.get_group">
<code class="descclassname">pulumi_gitlab.</code><code class="descname">get_group</code><span class="sig-paren">(</span><em>full_path=None</em>, <em>group_id=None</em>, <em>opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gitlab.get_group" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides details about a specific group in the gitlab provider.</p>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-gitlab/blob/master/website/docs/d/group.html.markdown">https://github.com/terraform-providers/terraform-provider-gitlab/blob/master/website/docs/d/group.html.markdown</a>.</div></blockquote>
</dd></dl>

<dl class="function">
<dt id="pulumi_gitlab.get_project">
<code class="descclassname">pulumi_gitlab.</code><code class="descname">get_project</code><span class="sig-paren">(</span><em>archived=None</em>, <em>default_branch=None</em>, <em>description=None</em>, <em>http_url_to_repo=None</em>, <em>id=None</em>, <em>issues_enabled=None</em>, <em>merge_requests_enabled=None</em>, <em>name=None</em>, <em>namespace_id=None</em>, <em>path=None</em>, <em>runners_token=None</em>, <em>snippets_enabled=None</em>, <em>ssh_url_to_repo=None</em>, <em>visibility_level=None</em>, <em>web_url=None</em>, <em>wiki_enabled=None</em>, <em>opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gitlab.get_project" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides details about a specific project in the gitlab provider. The results include the name of the project, path, description, default branch, etc.</p>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-gitlab/blob/master/website/docs/d/project.html.markdown">https://github.com/terraform-providers/terraform-provider-gitlab/blob/master/website/docs/d/project.html.markdown</a>.</div></blockquote>
</dd></dl>

<dl class="function">
<dt id="pulumi_gitlab.get_user">
<code class="descclassname">pulumi_gitlab.</code><code class="descname">get_user</code><span class="sig-paren">(</span><em>email=None</em>, <em>user_id=None</em>, <em>username=None</em>, <em>opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gitlab.get_user" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides details about a specific user in the gitlab provider. Especially the ability to lookup the id for linking to other resources.</p>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-gitlab/blob/master/website/docs/d/user.html.markdown">https://github.com/terraform-providers/terraform-provider-gitlab/blob/master/website/docs/d/user.html.markdown</a>.</div></blockquote>
</dd></dl>

<dl class="function">
<dt id="pulumi_gitlab.get_users">
<code class="descclassname">pulumi_gitlab.</code><code class="descname">get_users</code><span class="sig-paren">(</span><em>active=None</em>, <em>blocked=None</em>, <em>created_after=None</em>, <em>created_before=None</em>, <em>extern_provider=None</em>, <em>extern_uid=None</em>, <em>order_by=None</em>, <em>search=None</em>, <em>sort=None</em>, <em>opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gitlab.get_users" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides details about a list of users in the gitlab provider. The results include id, username, email, name and more about the requested users. Users can also be sorted and filtered using several options.</p>
<p><strong>NOTE</strong>: Some of the available options require administrator privileges. Please visit [Gitlab API documentation][users_for_admins] for more information.</p>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-gitlab/blob/master/website/docs/d/users.html.markdown">https://github.com/terraform-providers/terraform-provider-gitlab/blob/master/website/docs/d/users.html.markdown</a>.</div></blockquote>
</dd></dl>

</div>
