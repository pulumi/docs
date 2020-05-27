---
title: Package pulumi_github
title_tag: Package pulumi_github | Python SDK
linktitle: pulumi_github
notitle: true
---

<div class="section" id="pulumi-github">
<h1>Pulumi GitHub<a class="headerlink" href="#pulumi-github" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-github">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-github/issues">pulumi/pulumi-github repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-github/issues">terraform-providers/terraform-provider-github repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_github"></span><dl class="py class">
<dt id="pulumi_github.ActionsSecret">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_github.</code><code class="sig-name descname">ActionsSecret</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">plaintext_value</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">repository</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">secret_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_github.ActionsSecret" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a ActionsSecret resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] plaintext_value: Plaintext value of the secret to be encrypted
:param pulumi.Input[str] repository: Name of the repository
:param pulumi.Input[str] secret_name: Name of the secret</p>
<dl class="py attribute">
<dt id="pulumi_github.ActionsSecret.created_at">
<code class="sig-name descname">created_at</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_github.ActionsSecret.created_at" title="Permalink to this definition">¶</a></dt>
<dd><p>Date of actions_secret creation.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_github.ActionsSecret.plaintext_value">
<code class="sig-name descname">plaintext_value</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_github.ActionsSecret.plaintext_value" title="Permalink to this definition">¶</a></dt>
<dd><p>Plaintext value of the secret to be encrypted</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_github.ActionsSecret.repository">
<code class="sig-name descname">repository</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_github.ActionsSecret.repository" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the repository</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_github.ActionsSecret.secret_name">
<code class="sig-name descname">secret_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_github.ActionsSecret.secret_name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the secret</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_github.ActionsSecret.updated_at">
<code class="sig-name descname">updated_at</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_github.ActionsSecret.updated_at" title="Permalink to this definition">¶</a></dt>
<dd><p>Date of actions_secret update.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_github.ActionsSecret.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">created_at</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">plaintext_value</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">repository</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">secret_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">updated_at</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_github.ActionsSecret.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ActionsSecret resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>created_at</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Date of actions_secret creation.</p></li>
<li><p><strong>plaintext_value</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Plaintext value of the secret to be encrypted</p></li>
<li><p><strong>repository</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the repository</p></li>
<li><p><strong>secret_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the secret</p></li>
<li><p><strong>updated_at</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Date of actions_secret update.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_github.ActionsSecret.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_github.ActionsSecret.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_github.ActionsSecret.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_github.ActionsSecret.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_github.AwaitableGetActionsPublicKeyResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_github.</code><code class="sig-name descname">AwaitableGetActionsPublicKeyResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">key</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">key_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">repository</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_github.AwaitableGetActionsPublicKeyResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_github.AwaitableGetBranchResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_github.</code><code class="sig-name descname">AwaitableGetBranchResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">branch</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">etag</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ref</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">repository</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sha</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_github.AwaitableGetBranchResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_github.AwaitableGetCollaboratorsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_github.</code><code class="sig-name descname">AwaitableGetCollaboratorsResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">affiliation</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">collaborators</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">owner</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">repository</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_github.AwaitableGetCollaboratorsResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_github.AwaitableGetIpRangesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_github.</code><code class="sig-name descname">AwaitableGetIpRangesResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">gits</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">hooks</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">importers</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">pages</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_github.AwaitableGetIpRangesResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_github.AwaitableGetMembershipResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_github.</code><code class="sig-name descname">AwaitableGetMembershipResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">etag</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">role</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">username</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_github.AwaitableGetMembershipResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_github.AwaitableGetOrganizationTeamSyncGroupsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_github.</code><code class="sig-name descname">AwaitableGetOrganizationTeamSyncGroupsResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">groups</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_github.AwaitableGetOrganizationTeamSyncGroupsResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_github.AwaitableGetReleaseResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_github.</code><code class="sig-name descname">AwaitableGetReleaseResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">asserts_url</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">body</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">created_at</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">draft</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">html_url</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">owner</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">prerelease</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">published_at</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">release_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">release_tag</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">repository</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">retrieve_by</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tarball_url</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">target_commitish</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">upload_url</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">url</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zipball_url</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_github.AwaitableGetReleaseResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_github.AwaitableGetRepositoriesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_github.</code><code class="sig-name descname">AwaitableGetRepositoriesResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">full_names</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">names</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">query</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sort</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_github.AwaitableGetRepositoriesResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_github.AwaitableGetRepositoryResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_github.</code><code class="sig-name descname">AwaitableGetRepositoryResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">allow_merge_commit</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">allow_rebase_merge</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">allow_squash_merge</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">archived</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">default_branch</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">full_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">git_clone_url</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">has_downloads</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">has_issues</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">has_projects</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">has_wiki</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">homepage_url</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">html_url</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">http_clone_url</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">node_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">private</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ssh_clone_url</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">svn_url</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">topics</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_github.AwaitableGetRepositoryResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_github.AwaitableGetTeamResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_github.</code><code class="sig-name descname">AwaitableGetTeamResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">members</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">node_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">permission</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">privacy</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">slug</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_github.AwaitableGetTeamResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_github.AwaitableGetUserResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_github.</code><code class="sig-name descname">AwaitableGetUserResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">avatar_url</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">bio</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">blog</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">company</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">created_at</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">email</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">followers</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">following</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">gpg_keys</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">gravatar_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">location</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">login</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">node_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">public_gists</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">public_repos</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">site_admin</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ssh_keys</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">updated_at</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">username</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_github.AwaitableGetUserResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_github.Branch">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_github.</code><code class="sig-name descname">Branch</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">branch</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">repository</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">source_branch</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">source_sha</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_github.Branch" title="Permalink to this definition">¶</a></dt>
<dd><p>This resource allows you to create and manage branches within your repository.</p>
<p>Additional constraints can be applied to ensure your branch is created from
another branch or commit.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_github</span> <span class="k">as</span> <span class="nn">github</span>

<span class="n">development</span> <span class="o">=</span> <span class="n">github</span><span class="o">.</span><span class="n">Branch</span><span class="p">(</span><span class="s2">&quot;development&quot;</span><span class="p">,</span>
    <span class="n">branch</span><span class="o">=</span><span class="s2">&quot;development&quot;</span><span class="p">,</span>
    <span class="n">repository</span><span class="o">=</span><span class="s2">&quot;example&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>branch</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The repository branch to create.</p></li>
<li><p><strong>repository</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The GitHub repository name.</p></li>
<li><p><strong>source_branch</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The branch name to start from. Defaults to <code class="docutils literal notranslate"><span class="pre">master</span></code>.</p></li>
<li><p><strong>source_sha</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The commit hash to start from. Defaults to the tip of <code class="docutils literal notranslate"><span class="pre">source_branch</span></code>. If provided, <code class="docutils literal notranslate"><span class="pre">source_branch</span></code> is ignored.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_github.Branch.branch">
<code class="sig-name descname">branch</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_github.Branch.branch" title="Permalink to this definition">¶</a></dt>
<dd><p>The repository branch to create.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_github.Branch.etag">
<code class="sig-name descname">etag</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_github.Branch.etag" title="Permalink to this definition">¶</a></dt>
<dd><p>An etag representing the Branch object.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_github.Branch.ref">
<code class="sig-name descname">ref</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_github.Branch.ref" title="Permalink to this definition">¶</a></dt>
<dd><p>A string representing a branch reference, in the form of <code class="docutils literal notranslate"><span class="pre">refs/heads/&lt;branch&gt;</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_github.Branch.repository">
<code class="sig-name descname">repository</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_github.Branch.repository" title="Permalink to this definition">¶</a></dt>
<dd><p>The GitHub repository name.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_github.Branch.sha">
<code class="sig-name descname">sha</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_github.Branch.sha" title="Permalink to this definition">¶</a></dt>
<dd><p>A string storing the reference’s <code class="docutils literal notranslate"><span class="pre">HEAD</span></code> commit’s SHA1.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_github.Branch.source_branch">
<code class="sig-name descname">source_branch</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_github.Branch.source_branch" title="Permalink to this definition">¶</a></dt>
<dd><p>The branch name to start from. Defaults to <code class="docutils literal notranslate"><span class="pre">master</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_github.Branch.source_sha">
<code class="sig-name descname">source_sha</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_github.Branch.source_sha" title="Permalink to this definition">¶</a></dt>
<dd><p>The commit hash to start from. Defaults to the tip of <code class="docutils literal notranslate"><span class="pre">source_branch</span></code>. If provided, <code class="docutils literal notranslate"><span class="pre">source_branch</span></code> is ignored.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_github.Branch.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">branch</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">etag</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ref</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">repository</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sha</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">source_branch</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">source_sha</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_github.Branch.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Branch resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>branch</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The repository branch to create.</p></li>
<li><p><strong>etag</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – An etag representing the Branch object.</p></li>
<li><p><strong>ref</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A string representing a branch reference, in the form of <code class="docutils literal notranslate"><span class="pre">refs/heads/&lt;branch&gt;</span></code>.</p></li>
<li><p><strong>repository</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The GitHub repository name.</p></li>
<li><p><strong>sha</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A string storing the reference’s <code class="docutils literal notranslate"><span class="pre">HEAD</span></code> commit’s SHA1.</p></li>
<li><p><strong>source_branch</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The branch name to start from. Defaults to <code class="docutils literal notranslate"><span class="pre">master</span></code>.</p></li>
<li><p><strong>source_sha</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The commit hash to start from. Defaults to the tip of <code class="docutils literal notranslate"><span class="pre">source_branch</span></code>. If provided, <code class="docutils literal notranslate"><span class="pre">source_branch</span></code> is ignored.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_github.Branch.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_github.Branch.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_github.Branch.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_github.Branch.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_github.BranchProtection">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_github.</code><code class="sig-name descname">BranchProtection</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">branch</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enforce_admins</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">repository</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">require_signed_commits</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">required_pull_request_reviews</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">required_status_checks</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">restrictions</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_github.BranchProtection" title="Permalink to this definition">¶</a></dt>
<dd><p>Protects a GitHub branch.</p>
<p>This resource allows you to configure branch protection for repositories in your organization. When applied, the branch will be protected from forced pushes and deletion. Additional constraints, such as required status checks or restrictions on users, teams, and apps, can also be configured.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_github</span> <span class="k">as</span> <span class="nn">github</span>

<span class="n">example_team</span> <span class="o">=</span> <span class="n">github</span><span class="o">.</span><span class="n">Team</span><span class="p">(</span><span class="s2">&quot;exampleTeam&quot;</span><span class="p">)</span>
<span class="c1"># Protect the master branch of the foo repository. Additionally, require that</span>
<span class="c1"># the &quot;ci/travis&quot; context to be passing and only allow the engineers team merge</span>
<span class="c1"># to the branch.</span>
<span class="n">example_branch_protection</span> <span class="o">=</span> <span class="n">github</span><span class="o">.</span><span class="n">BranchProtection</span><span class="p">(</span><span class="s2">&quot;exampleBranchProtection&quot;</span><span class="p">,</span>
    <span class="n">branch</span><span class="o">=</span><span class="s2">&quot;master&quot;</span><span class="p">,</span>
    <span class="n">enforce_admins</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span>
    <span class="n">repository</span><span class="o">=</span><span class="n">github_repository</span><span class="p">[</span><span class="s2">&quot;example&quot;</span><span class="p">][</span><span class="s2">&quot;name&quot;</span><span class="p">],</span>
    <span class="n">required_pull_request_reviews</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;dismissStaleReviews&quot;</span><span class="p">:</span> <span class="kc">True</span><span class="p">,</span>
        <span class="s2">&quot;dismissalTeams&quot;</span><span class="p">:</span> <span class="p">[</span>
            <span class="n">example_team</span><span class="o">.</span><span class="n">slug</span><span class="p">,</span>
            <span class="n">github_team</span><span class="p">[</span><span class="s2">&quot;second&quot;</span><span class="p">][</span><span class="s2">&quot;slug&quot;</span><span class="p">],</span>
        <span class="p">],</span>
        <span class="s2">&quot;dismissalUsers&quot;</span><span class="p">:</span> <span class="p">[</span><span class="s2">&quot;foo-user&quot;</span><span class="p">],</span>
    <span class="p">},</span>
    <span class="n">required_status_checks</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;contexts&quot;</span><span class="p">:</span> <span class="p">[</span><span class="s2">&quot;ci/travis&quot;</span><span class="p">],</span>
        <span class="s2">&quot;strict&quot;</span><span class="p">:</span> <span class="kc">False</span><span class="p">,</span>
    <span class="p">},</span>
    <span class="n">restrictions</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;apps&quot;</span><span class="p">:</span> <span class="p">[</span><span class="s2">&quot;foo-app&quot;</span><span class="p">],</span>
        <span class="s2">&quot;teams&quot;</span><span class="p">:</span> <span class="p">[</span><span class="n">example_team</span><span class="o">.</span><span class="n">slug</span><span class="p">],</span>
        <span class="s2">&quot;users&quot;</span><span class="p">:</span> <span class="p">[</span><span class="s2">&quot;foo-user&quot;</span><span class="p">],</span>
    <span class="p">})</span>
<span class="n">example_team_repository</span> <span class="o">=</span> <span class="n">github</span><span class="o">.</span><span class="n">TeamRepository</span><span class="p">(</span><span class="s2">&quot;exampleTeamRepository&quot;</span><span class="p">,</span>
    <span class="n">permission</span><span class="o">=</span><span class="s2">&quot;pull&quot;</span><span class="p">,</span>
    <span class="n">repository</span><span class="o">=</span><span class="n">github_repository</span><span class="p">[</span><span class="s2">&quot;example&quot;</span><span class="p">][</span><span class="s2">&quot;name&quot;</span><span class="p">],</span>
    <span class="n">team_id</span><span class="o">=</span><span class="n">example_team</span><span class="o">.</span><span class="n">id</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>branch</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Git branch to protect.</p></li>
<li><p><strong>enforce_admins</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean, setting this to <code class="docutils literal notranslate"><span class="pre">true</span></code> enforces status checks for repository administrators.</p></li>
<li><p><strong>repository</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The GitHub repository name.</p></li>
<li><p><strong>require_signed_commits</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean, setting this to <code class="docutils literal notranslate"><span class="pre">true</span></code> requires all commits to be signed with GPG.</p></li>
<li><p><strong>required_pull_request_reviews</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Enforce restrictions for pull request reviews. See Required Pull Request Reviews below for details.</p></li>
<li><p><strong>required_status_checks</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Enforce restrictions for required status checks. See Required Status Checks below for details.</p></li>
<li><p><strong>restrictions</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Enforce restrictions for the users and teams that may push to the branch. See Restrictions below for details.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>required_pull_request_reviews</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">dismissStaleReviews</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">dismissalTeams</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">dismissalUsers</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">includeAdmins</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">requireCodeOwnerReviews</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">requiredApprovingReviewCount</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
<p>The <strong>required_status_checks</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">contexts</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">includeAdmins</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">strict</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
</ul>
<p>The <strong>restrictions</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">apps</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">teams</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">users</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_github.BranchProtection.branch">
<code class="sig-name descname">branch</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_github.BranchProtection.branch" title="Permalink to this definition">¶</a></dt>
<dd><p>The Git branch to protect.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_github.BranchProtection.enforce_admins">
<code class="sig-name descname">enforce_admins</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_github.BranchProtection.enforce_admins" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean, setting this to <code class="docutils literal notranslate"><span class="pre">true</span></code> enforces status checks for repository administrators.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_github.BranchProtection.repository">
<code class="sig-name descname">repository</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_github.BranchProtection.repository" title="Permalink to this definition">¶</a></dt>
<dd><p>The GitHub repository name.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_github.BranchProtection.require_signed_commits">
<code class="sig-name descname">require_signed_commits</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_github.BranchProtection.require_signed_commits" title="Permalink to this definition">¶</a></dt>
<dd><p>Boolean, setting this to <code class="docutils literal notranslate"><span class="pre">true</span></code> requires all commits to be signed with GPG.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_github.BranchProtection.required_pull_request_reviews">
<code class="sig-name descname">required_pull_request_reviews</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_github.BranchProtection.required_pull_request_reviews" title="Permalink to this definition">¶</a></dt>
<dd><p>Enforce restrictions for pull request reviews. See Required Pull Request Reviews below for details.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">dismissStaleReviews</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">dismissalTeams</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">dismissalUsers</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">includeAdmins</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">requireCodeOwnerReviews</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">requiredApprovingReviewCount</span></code> (<code class="docutils literal notranslate"><span class="pre">float</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_github.BranchProtection.required_status_checks">
<code class="sig-name descname">required_status_checks</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_github.BranchProtection.required_status_checks" title="Permalink to this definition">¶</a></dt>
<dd><p>Enforce restrictions for required status checks. See Required Status Checks below for details.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">contexts</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">includeAdmins</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">strict</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_github.BranchProtection.restrictions">
<code class="sig-name descname">restrictions</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_github.BranchProtection.restrictions" title="Permalink to this definition">¶</a></dt>
<dd><p>Enforce restrictions for the users and teams that may push to the branch. See Restrictions below for details.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">apps</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">teams</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">users</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_github.BranchProtection.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">branch</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">enforce_admins</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">etag</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">repository</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">require_signed_commits</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">required_pull_request_reviews</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">required_status_checks</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">restrictions</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_github.BranchProtection.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing BranchProtection resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>branch</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Git branch to protect.</p></li>
<li><p><strong>enforce_admins</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean, setting this to <code class="docutils literal notranslate"><span class="pre">true</span></code> enforces status checks for repository administrators.</p></li>
<li><p><strong>repository</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The GitHub repository name.</p></li>
<li><p><strong>require_signed_commits</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Boolean, setting this to <code class="docutils literal notranslate"><span class="pre">true</span></code> requires all commits to be signed with GPG.</p></li>
<li><p><strong>required_pull_request_reviews</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Enforce restrictions for pull request reviews. See Required Pull Request Reviews below for details.</p></li>
<li><p><strong>required_status_checks</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Enforce restrictions for required status checks. See Required Status Checks below for details.</p></li>
<li><p><strong>restrictions</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Enforce restrictions for the users and teams that may push to the branch. See Restrictions below for details.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>required_pull_request_reviews</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">dismissStaleReviews</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">dismissalTeams</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">dismissalUsers</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">includeAdmins</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">requireCodeOwnerReviews</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">requiredApprovingReviewCount</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[float]</span></code>)</p></li>
</ul>
<p>The <strong>required_status_checks</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">contexts</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">includeAdmins</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">strict</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
</ul>
<p>The <strong>restrictions</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">apps</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">teams</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">users</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_github.BranchProtection.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_github.BranchProtection.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_github.BranchProtection.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_github.BranchProtection.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_github.GetActionsPublicKeyResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_github.</code><code class="sig-name descname">GetActionsPublicKeyResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">key</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">key_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">repository</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_github.GetActionsPublicKeyResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getActionsPublicKey.</p>
<dl class="py attribute">
<dt id="pulumi_github.GetActionsPublicKeyResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_github.GetActionsPublicKeyResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_github.GetActionsPublicKeyResult.key">
<code class="sig-name descname">key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_github.GetActionsPublicKeyResult.key" title="Permalink to this definition">¶</a></dt>
<dd><p>Actual key retrieved.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_github.GetActionsPublicKeyResult.key_id">
<code class="sig-name descname">key_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_github.GetActionsPublicKeyResult.key_id" title="Permalink to this definition">¶</a></dt>
<dd><p>ID of the key that has been retrieved.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_github.GetBranchResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_github.</code><code class="sig-name descname">GetBranchResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">branch</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">etag</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ref</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">repository</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sha</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_github.GetBranchResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getBranch.</p>
<dl class="py attribute">
<dt id="pulumi_github.GetBranchResult.etag">
<code class="sig-name descname">etag</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_github.GetBranchResult.etag" title="Permalink to this definition">¶</a></dt>
<dd><p>An etag representing the Branch object.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_github.GetBranchResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_github.GetBranchResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_github.GetBranchResult.ref">
<code class="sig-name descname">ref</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_github.GetBranchResult.ref" title="Permalink to this definition">¶</a></dt>
<dd><p>A string representing a branch reference, in the form of <code class="docutils literal notranslate"><span class="pre">refs/heads/&lt;branch&gt;</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_github.GetBranchResult.sha">
<code class="sig-name descname">sha</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_github.GetBranchResult.sha" title="Permalink to this definition">¶</a></dt>
<dd><p>A string storing the reference’s <code class="docutils literal notranslate"><span class="pre">HEAD</span></code> commit’s SHA1.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_github.GetCollaboratorsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_github.</code><code class="sig-name descname">GetCollaboratorsResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">affiliation</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">collaborators</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">owner</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">repository</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_github.GetCollaboratorsResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getCollaborators.</p>
<dl class="py attribute">
<dt id="pulumi_github.GetCollaboratorsResult.collaborators">
<code class="sig-name descname">collaborators</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_github.GetCollaboratorsResult.collaborators" title="Permalink to this definition">¶</a></dt>
<dd><p>An Array of GitHub collaborators.  Each <code class="docutils literal notranslate"><span class="pre">collaborator</span></code> block consists of the fields documented below.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_github.GetCollaboratorsResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_github.GetCollaboratorsResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_github.GetIpRangesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_github.</code><code class="sig-name descname">GetIpRangesResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">gits</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">hooks</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">importers</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">pages</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_github.GetIpRangesResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getIpRanges.</p>
<dl class="py attribute">
<dt id="pulumi_github.GetIpRangesResult.gits">
<code class="sig-name descname">gits</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_github.GetIpRangesResult.gits" title="Permalink to this definition">¶</a></dt>
<dd><p>An Array of IP addresses in CIDR format specifying the Git servers.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_github.GetIpRangesResult.hooks">
<code class="sig-name descname">hooks</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_github.GetIpRangesResult.hooks" title="Permalink to this definition">¶</a></dt>
<dd><p>An Array of IP addresses in CIDR format specifying the addresses that incoming service hooks will originate from.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_github.GetIpRangesResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_github.GetIpRangesResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_github.GetIpRangesResult.importers">
<code class="sig-name descname">importers</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_github.GetIpRangesResult.importers" title="Permalink to this definition">¶</a></dt>
<dd><p>An Array of IP addresses in CIDR format specifying the A records for GitHub Importer.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_github.GetIpRangesResult.pages">
<code class="sig-name descname">pages</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_github.GetIpRangesResult.pages" title="Permalink to this definition">¶</a></dt>
<dd><p>An Array of IP addresses in CIDR format specifying the A records for GitHub Pages.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_github.GetMembershipResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_github.</code><code class="sig-name descname">GetMembershipResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">etag</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">role</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">username</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_github.GetMembershipResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getMembership.</p>
<dl class="py attribute">
<dt id="pulumi_github.GetMembershipResult.etag">
<code class="sig-name descname">etag</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_github.GetMembershipResult.etag" title="Permalink to this definition">¶</a></dt>
<dd><p>An etag representing the membership object.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_github.GetMembershipResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_github.GetMembershipResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_github.GetMembershipResult.role">
<code class="sig-name descname">role</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_github.GetMembershipResult.role" title="Permalink to this definition">¶</a></dt>
<dd><p><code class="docutils literal notranslate"><span class="pre">admin</span></code> or <code class="docutils literal notranslate"><span class="pre">member</span></code> – the role the user has within the organization.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_github.GetMembershipResult.username">
<code class="sig-name descname">username</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_github.GetMembershipResult.username" title="Permalink to this definition">¶</a></dt>
<dd><p>The username.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_github.GetOrganizationTeamSyncGroupsResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_github.</code><code class="sig-name descname">GetOrganizationTeamSyncGroupsResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">groups</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_github.GetOrganizationTeamSyncGroupsResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getOrganizationTeamSyncGroups.</p>
<dl class="py attribute">
<dt id="pulumi_github.GetOrganizationTeamSyncGroupsResult.groups">
<code class="sig-name descname">groups</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_github.GetOrganizationTeamSyncGroupsResult.groups" title="Permalink to this definition">¶</a></dt>
<dd><p>An Array of GitHub Identity Provider Groups.  Each <code class="docutils literal notranslate"><span class="pre">group</span></code> block consists of the fields documented below.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_github.GetOrganizationTeamSyncGroupsResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_github.GetOrganizationTeamSyncGroupsResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_github.GetReleaseResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_github.</code><code class="sig-name descname">GetReleaseResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">asserts_url</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">body</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">created_at</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">draft</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">html_url</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">owner</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">prerelease</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">published_at</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">release_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">release_tag</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">repository</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">retrieve_by</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">tarball_url</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">target_commitish</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">upload_url</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">url</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">zipball_url</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_github.GetReleaseResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getRelease.</p>
<dl class="py attribute">
<dt id="pulumi_github.GetReleaseResult.asserts_url">
<code class="sig-name descname">asserts_url</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_github.GetReleaseResult.asserts_url" title="Permalink to this definition">¶</a></dt>
<dd><p>URL of any associated assets with the release</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_github.GetReleaseResult.body">
<code class="sig-name descname">body</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_github.GetReleaseResult.body" title="Permalink to this definition">¶</a></dt>
<dd><p>Contents of the description (body) of a release</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_github.GetReleaseResult.created_at">
<code class="sig-name descname">created_at</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_github.GetReleaseResult.created_at" title="Permalink to this definition">¶</a></dt>
<dd><p>Date of release creation</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_github.GetReleaseResult.draft">
<code class="sig-name descname">draft</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_github.GetReleaseResult.draft" title="Permalink to this definition">¶</a></dt>
<dd><p>(<code class="docutils literal notranslate"><span class="pre">Boolean</span></code>) indicates whether the release is a draft</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_github.GetReleaseResult.html_url">
<code class="sig-name descname">html_url</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_github.GetReleaseResult.html_url" title="Permalink to this definition">¶</a></dt>
<dd><p>URL directing to detailed information on the release</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_github.GetReleaseResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_github.GetReleaseResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_github.GetReleaseResult.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_github.GetReleaseResult.name" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of release</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_github.GetReleaseResult.prerelease">
<code class="sig-name descname">prerelease</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_github.GetReleaseResult.prerelease" title="Permalink to this definition">¶</a></dt>
<dd><p>(<code class="docutils literal notranslate"><span class="pre">Boolean</span></code>) indicates whether the release is a prerelease</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_github.GetReleaseResult.published_at">
<code class="sig-name descname">published_at</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_github.GetReleaseResult.published_at" title="Permalink to this definition">¶</a></dt>
<dd><p>Date of release publishing</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_github.GetReleaseResult.release_id">
<code class="sig-name descname">release_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_github.GetReleaseResult.release_id" title="Permalink to this definition">¶</a></dt>
<dd><p>ID of release</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_github.GetReleaseResult.release_tag">
<code class="sig-name descname">release_tag</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_github.GetReleaseResult.release_tag" title="Permalink to this definition">¶</a></dt>
<dd><p>Tag of release</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_github.GetReleaseResult.tarball_url">
<code class="sig-name descname">tarball_url</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_github.GetReleaseResult.tarball_url" title="Permalink to this definition">¶</a></dt>
<dd><p>Download URL of a specific release in <code class="docutils literal notranslate"><span class="pre">tar.gz</span></code> format</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_github.GetReleaseResult.target_commitish">
<code class="sig-name descname">target_commitish</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_github.GetReleaseResult.target_commitish" title="Permalink to this definition">¶</a></dt>
<dd><p>Commitish value that determines where the Git release is created from</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_github.GetReleaseResult.upload_url">
<code class="sig-name descname">upload_url</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_github.GetReleaseResult.upload_url" title="Permalink to this definition">¶</a></dt>
<dd><p>URL that can be used to upload Assets to the release</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_github.GetReleaseResult.url">
<code class="sig-name descname">url</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_github.GetReleaseResult.url" title="Permalink to this definition">¶</a></dt>
<dd><p>Base URL of the release</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_github.GetReleaseResult.zipball_url">
<code class="sig-name descname">zipball_url</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_github.GetReleaseResult.zipball_url" title="Permalink to this definition">¶</a></dt>
<dd><p>Download URL of a specific release in <code class="docutils literal notranslate"><span class="pre">zip</span></code> format</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_github.GetRepositoriesResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_github.</code><code class="sig-name descname">GetRepositoriesResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">full_names</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">names</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">query</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sort</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_github.GetRepositoriesResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getRepositories.</p>
<dl class="py attribute">
<dt id="pulumi_github.GetRepositoriesResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_github.GetRepositoriesResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_github.GetRepositoryResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_github.</code><code class="sig-name descname">GetRepositoryResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">allow_merge_commit</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">allow_rebase_merge</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">allow_squash_merge</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">archived</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">default_branch</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">full_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">git_clone_url</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">has_downloads</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">has_issues</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">has_projects</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">has_wiki</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">homepage_url</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">html_url</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">http_clone_url</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">node_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">private</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ssh_clone_url</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">svn_url</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">topics</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_github.GetRepositoryResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getRepository.</p>
<dl class="py attribute">
<dt id="pulumi_github.GetRepositoryResult.allow_merge_commit">
<code class="sig-name descname">allow_merge_commit</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_github.GetRepositoryResult.allow_merge_commit" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the repository allows merge commits.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_github.GetRepositoryResult.allow_rebase_merge">
<code class="sig-name descname">allow_rebase_merge</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_github.GetRepositoryResult.allow_rebase_merge" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the repository allows rebase merges.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_github.GetRepositoryResult.allow_squash_merge">
<code class="sig-name descname">allow_squash_merge</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_github.GetRepositoryResult.allow_squash_merge" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the repository allows squash merges.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_github.GetRepositoryResult.archived">
<code class="sig-name descname">archived</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_github.GetRepositoryResult.archived" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the repository is archived.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_github.GetRepositoryResult.default_branch">
<code class="sig-name descname">default_branch</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_github.GetRepositoryResult.default_branch" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the default branch of the repository.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_github.GetRepositoryResult.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_github.GetRepositoryResult.description" title="Permalink to this definition">¶</a></dt>
<dd><p>A description of the repository.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_github.GetRepositoryResult.git_clone_url">
<code class="sig-name descname">git_clone_url</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_github.GetRepositoryResult.git_clone_url" title="Permalink to this definition">¶</a></dt>
<dd><p>URL that can be provided to <code class="docutils literal notranslate"><span class="pre">git</span> <span class="pre">clone</span></code> to clone the repository anonymously via the git protocol.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_github.GetRepositoryResult.has_downloads">
<code class="sig-name descname">has_downloads</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_github.GetRepositoryResult.has_downloads" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the repository has Downloads feature enabled.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_github.GetRepositoryResult.has_issues">
<code class="sig-name descname">has_issues</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_github.GetRepositoryResult.has_issues" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the repository has GitHub Issues enabled.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_github.GetRepositoryResult.has_projects">
<code class="sig-name descname">has_projects</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_github.GetRepositoryResult.has_projects" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the repository has the GitHub Projects enabled.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_github.GetRepositoryResult.has_wiki">
<code class="sig-name descname">has_wiki</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_github.GetRepositoryResult.has_wiki" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the repository has the GitHub Wiki enabled.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_github.GetRepositoryResult.homepage_url">
<code class="sig-name descname">homepage_url</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_github.GetRepositoryResult.homepage_url" title="Permalink to this definition">¶</a></dt>
<dd><p>URL of a page describing the project.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_github.GetRepositoryResult.html_url">
<code class="sig-name descname">html_url</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_github.GetRepositoryResult.html_url" title="Permalink to this definition">¶</a></dt>
<dd><p>URL to the repository on the web.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_github.GetRepositoryResult.http_clone_url">
<code class="sig-name descname">http_clone_url</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_github.GetRepositoryResult.http_clone_url" title="Permalink to this definition">¶</a></dt>
<dd><p>URL that can be provided to <code class="docutils literal notranslate"><span class="pre">git</span> <span class="pre">clone</span></code> to clone the repository via HTTPS.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_github.GetRepositoryResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_github.GetRepositoryResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_github.GetRepositoryResult.private">
<code class="sig-name descname">private</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_github.GetRepositoryResult.private" title="Permalink to this definition">¶</a></dt>
<dd><p>Whether the repository is private.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_github.GetRepositoryResult.ssh_clone_url">
<code class="sig-name descname">ssh_clone_url</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_github.GetRepositoryResult.ssh_clone_url" title="Permalink to this definition">¶</a></dt>
<dd><p>URL that can be provided to <code class="docutils literal notranslate"><span class="pre">git</span> <span class="pre">clone</span></code> to clone the repository via SSH.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_github.GetRepositoryResult.svn_url">
<code class="sig-name descname">svn_url</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_github.GetRepositoryResult.svn_url" title="Permalink to this definition">¶</a></dt>
<dd><p>URL that can be provided to <code class="docutils literal notranslate"><span class="pre">svn</span> <span class="pre">checkout</span></code> to check out the repository via GitHub’s Subversion protocol emulation.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_github.GetRepositoryResult.topics">
<code class="sig-name descname">topics</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_github.GetRepositoryResult.topics" title="Permalink to this definition">¶</a></dt>
<dd><p>The list of topics of the repository.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_github.GetTeamResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_github.</code><code class="sig-name descname">GetTeamResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">members</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">node_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">permission</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">privacy</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">slug</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_github.GetTeamResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getTeam.</p>
<dl class="py attribute">
<dt id="pulumi_github.GetTeamResult.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_github.GetTeamResult.description" title="Permalink to this definition">¶</a></dt>
<dd><p>the team’s description.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_github.GetTeamResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_github.GetTeamResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_github.GetTeamResult.members">
<code class="sig-name descname">members</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_github.GetTeamResult.members" title="Permalink to this definition">¶</a></dt>
<dd><p>List of team members</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_github.GetTeamResult.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_github.GetTeamResult.name" title="Permalink to this definition">¶</a></dt>
<dd><p>the team’s full name.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_github.GetTeamResult.permission">
<code class="sig-name descname">permission</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_github.GetTeamResult.permission" title="Permalink to this definition">¶</a></dt>
<dd><p>the team’s permission level.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_github.GetTeamResult.privacy">
<code class="sig-name descname">privacy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_github.GetTeamResult.privacy" title="Permalink to this definition">¶</a></dt>
<dd><p>the team’s privacy type.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_github.GetUserResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_github.</code><code class="sig-name descname">GetUserResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">avatar_url</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">bio</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">blog</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">company</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">created_at</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">email</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">followers</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">following</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">gpg_keys</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">gravatar_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">location</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">login</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">node_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">public_gists</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">public_repos</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">site_admin</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ssh_keys</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">updated_at</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">username</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_github.GetUserResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getUser.</p>
<dl class="py attribute">
<dt id="pulumi_github.GetUserResult.avatar_url">
<code class="sig-name descname">avatar_url</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_github.GetUserResult.avatar_url" title="Permalink to this definition">¶</a></dt>
<dd><p>the user’s avatar URL.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_github.GetUserResult.bio">
<code class="sig-name descname">bio</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_github.GetUserResult.bio" title="Permalink to this definition">¶</a></dt>
<dd><p>the user’s bio.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_github.GetUserResult.blog">
<code class="sig-name descname">blog</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_github.GetUserResult.blog" title="Permalink to this definition">¶</a></dt>
<dd><p>the user’s blog location.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_github.GetUserResult.company">
<code class="sig-name descname">company</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_github.GetUserResult.company" title="Permalink to this definition">¶</a></dt>
<dd><p>the user’s company name.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_github.GetUserResult.created_at">
<code class="sig-name descname">created_at</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_github.GetUserResult.created_at" title="Permalink to this definition">¶</a></dt>
<dd><p>the creation date.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_github.GetUserResult.email">
<code class="sig-name descname">email</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_github.GetUserResult.email" title="Permalink to this definition">¶</a></dt>
<dd><p>the user’s email.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_github.GetUserResult.followers">
<code class="sig-name descname">followers</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_github.GetUserResult.followers" title="Permalink to this definition">¶</a></dt>
<dd><p>the number of followers.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_github.GetUserResult.following">
<code class="sig-name descname">following</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_github.GetUserResult.following" title="Permalink to this definition">¶</a></dt>
<dd><p>the number of following users.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_github.GetUserResult.gpg_keys">
<code class="sig-name descname">gpg_keys</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_github.GetUserResult.gpg_keys" title="Permalink to this definition">¶</a></dt>
<dd><p>list of user’s GPG keys.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_github.GetUserResult.gravatar_id">
<code class="sig-name descname">gravatar_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_github.GetUserResult.gravatar_id" title="Permalink to this definition">¶</a></dt>
<dd><p>the user’s gravatar ID.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_github.GetUserResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_github.GetUserResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_github.GetUserResult.location">
<code class="sig-name descname">location</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_github.GetUserResult.location" title="Permalink to this definition">¶</a></dt>
<dd><p>the user’s location.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_github.GetUserResult.login">
<code class="sig-name descname">login</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_github.GetUserResult.login" title="Permalink to this definition">¶</a></dt>
<dd><p>the user’s login.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_github.GetUserResult.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_github.GetUserResult.name" title="Permalink to this definition">¶</a></dt>
<dd><p>the user’s full name.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_github.GetUserResult.public_gists">
<code class="sig-name descname">public_gists</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_github.GetUserResult.public_gists" title="Permalink to this definition">¶</a></dt>
<dd><p>the number of public gists.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_github.GetUserResult.public_repos">
<code class="sig-name descname">public_repos</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_github.GetUserResult.public_repos" title="Permalink to this definition">¶</a></dt>
<dd><p>the number of public repositories.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_github.GetUserResult.site_admin">
<code class="sig-name descname">site_admin</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_github.GetUserResult.site_admin" title="Permalink to this definition">¶</a></dt>
<dd><p>whether the user is a GitHub admin.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_github.GetUserResult.ssh_keys">
<code class="sig-name descname">ssh_keys</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_github.GetUserResult.ssh_keys" title="Permalink to this definition">¶</a></dt>
<dd><p>list of user’s SSH keys.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_github.GetUserResult.updated_at">
<code class="sig-name descname">updated_at</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_github.GetUserResult.updated_at" title="Permalink to this definition">¶</a></dt>
<dd><p>the update date.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_github.IssueLabel">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_github.</code><code class="sig-name descname">IssueLabel</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">color</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">repository</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_github.IssueLabel" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a IssueLabel resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[str] color: A 6 character hex code, <strong>without the leading #</strong>, identifying the color of the label.
:param pulumi.Input[str] description: A short description of the label.
:param pulumi.Input[str] name: The name of the label.
:param pulumi.Input[str] repository: The GitHub repository</p>
<dl class="py attribute">
<dt id="pulumi_github.IssueLabel.color">
<code class="sig-name descname">color</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_github.IssueLabel.color" title="Permalink to this definition">¶</a></dt>
<dd><p>A 6 character hex code, <strong>without the leading #</strong>, identifying the color of the label.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_github.IssueLabel.description">
<code class="sig-name descname">description</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_github.IssueLabel.description" title="Permalink to this definition">¶</a></dt>
<dd><p>A short description of the label.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_github.IssueLabel.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_github.IssueLabel.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the label.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_github.IssueLabel.repository">
<code class="sig-name descname">repository</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_github.IssueLabel.repository" title="Permalink to this definition">¶</a></dt>
<dd><p>The GitHub repository</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_github.IssueLabel.url">
<code class="sig-name descname">url</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_github.IssueLabel.url" title="Permalink to this definition">¶</a></dt>
<dd><p>The URL to the issue label</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_github.IssueLabel.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">color</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">etag</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">repository</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">url</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_github.IssueLabel.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing IssueLabel resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>color</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A 6 character hex code, <strong>without the leading #</strong>, identifying the color of the label.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A short description of the label.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the label.</p></li>
<li><p><strong>repository</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The GitHub repository</p></li>
<li><p><strong>url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The URL to the issue label</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_github.IssueLabel.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_github.IssueLabel.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_github.IssueLabel.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_github.IssueLabel.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_github.Membership">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_github.</code><code class="sig-name descname">Membership</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">role</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">username</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_github.Membership" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a GitHub membership resource.</p>
<p>This resource allows you to add/remove users from your organization. When applied,
an invitation will be sent to the user to become part of the organization. When
destroyed, either the invitation will be cancelled or the user will be removed.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_github</span> <span class="k">as</span> <span class="nn">github</span>

<span class="c1"># Add a user to the organization</span>
<span class="n">membership_for_some_user</span> <span class="o">=</span> <span class="n">github</span><span class="o">.</span><span class="n">Membership</span><span class="p">(</span><span class="s2">&quot;membershipForSomeUser&quot;</span><span class="p">,</span>
    <span class="n">role</span><span class="o">=</span><span class="s2">&quot;member&quot;</span><span class="p">,</span>
    <span class="n">username</span><span class="o">=</span><span class="s2">&quot;SomeUser&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The role of the user within the organization.
Must be one of <code class="docutils literal notranslate"><span class="pre">member</span></code> or <code class="docutils literal notranslate"><span class="pre">admin</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">member</span></code>.</p></li>
<li><p><strong>username</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The user to add to the organization.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_github.Membership.role">
<code class="sig-name descname">role</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_github.Membership.role" title="Permalink to this definition">¶</a></dt>
<dd><p>The role of the user within the organization.
Must be one of <code class="docutils literal notranslate"><span class="pre">member</span></code> or <code class="docutils literal notranslate"><span class="pre">admin</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">member</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_github.Membership.username">
<code class="sig-name descname">username</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_github.Membership.username" title="Permalink to this definition">¶</a></dt>
<dd><p>The user to add to the organization.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_github.Membership.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">etag</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">role</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">username</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_github.Membership.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Membership resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The role of the user within the organization.
Must be one of <code class="docutils literal notranslate"><span class="pre">member</span></code> or <code class="docutils literal notranslate"><span class="pre">admin</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">member</span></code>.</p></li>
<li><p><strong>username</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The user to add to the organization.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_github.Membership.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_github.Membership.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_github.Membership.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_github.Membership.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_github.OrganizationBlock">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_github.</code><code class="sig-name descname">OrganizationBlock</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">username</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_github.OrganizationBlock" title="Permalink to this definition">¶</a></dt>
<dd><p>This resource allows you to create and manage blocks for GitHub organizations.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_github</span> <span class="k">as</span> <span class="nn">github</span>

<span class="n">example</span> <span class="o">=</span> <span class="n">github</span><span class="o">.</span><span class="n">OrganizationBlock</span><span class="p">(</span><span class="s2">&quot;example&quot;</span><span class="p">,</span> <span class="n">username</span><span class="o">=</span><span class="s2">&quot;paultyng&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>username</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the user to block.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_github.OrganizationBlock.username">
<code class="sig-name descname">username</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_github.OrganizationBlock.username" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the user to block.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_github.OrganizationBlock.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">etag</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">username</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_github.OrganizationBlock.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing OrganizationBlock resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>username</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the user to block.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_github.OrganizationBlock.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_github.OrganizationBlock.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_github.OrganizationBlock.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_github.OrganizationBlock.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_github.OrganizationProject">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_github.</code><code class="sig-name descname">OrganizationProject</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">body</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_github.OrganizationProject" title="Permalink to this definition">¶</a></dt>
<dd><p>This resource allows you to create and manage projects for GitHub organization.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_github</span> <span class="k">as</span> <span class="nn">github</span>

<span class="n">project</span> <span class="o">=</span> <span class="n">github</span><span class="o">.</span><span class="n">OrganizationProject</span><span class="p">(</span><span class="s2">&quot;project&quot;</span><span class="p">,</span> <span class="n">body</span><span class="o">=</span><span class="s2">&quot;This is a organization project.&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>body</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The body of the project.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the project.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_github.OrganizationProject.body">
<code class="sig-name descname">body</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_github.OrganizationProject.body" title="Permalink to this definition">¶</a></dt>
<dd><p>The body of the project.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_github.OrganizationProject.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_github.OrganizationProject.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the project.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_github.OrganizationProject.url">
<code class="sig-name descname">url</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_github.OrganizationProject.url" title="Permalink to this definition">¶</a></dt>
<dd><p>URL of the project</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_github.OrganizationProject.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">body</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">etag</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">url</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_github.OrganizationProject.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing OrganizationProject resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>body</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The body of the project.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the project.</p></li>
<li><p><strong>url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – URL of the project</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_github.OrganizationProject.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_github.OrganizationProject.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_github.OrganizationProject.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_github.OrganizationProject.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_github.OrganizationWebhook">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_github.</code><code class="sig-name descname">OrganizationWebhook</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">active</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">configuration</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">events</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_github.OrganizationWebhook" title="Permalink to this definition">¶</a></dt>
<dd><p>This resource allows you to create and manage webhooks for GitHub organization.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_github</span> <span class="k">as</span> <span class="nn">github</span>

<span class="n">foo</span> <span class="o">=</span> <span class="n">github</span><span class="o">.</span><span class="n">OrganizationWebhook</span><span class="p">(</span><span class="s2">&quot;foo&quot;</span><span class="p">,</span>
    <span class="n">active</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span>
    <span class="n">configuration</span><span class="o">=</span><span class="p">{</span>
        <span class="s2">&quot;contentType&quot;</span><span class="p">:</span> <span class="s2">&quot;form&quot;</span><span class="p">,</span>
        <span class="s2">&quot;insecureSsl&quot;</span><span class="p">:</span> <span class="kc">False</span><span class="p">,</span>
        <span class="s2">&quot;url&quot;</span><span class="p">:</span> <span class="s2">&quot;https://google.de/&quot;</span><span class="p">,</span>
    <span class="p">},</span>
    <span class="n">events</span><span class="o">=</span><span class="p">[</span><span class="s2">&quot;issues&quot;</span><span class="p">])</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>active</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Indicate of the webhook should receive events. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>configuration</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – key/value pair of configuration for this webhook. Available keys are <code class="docutils literal notranslate"><span class="pre">url</span></code>, <code class="docutils literal notranslate"><span class="pre">content_type</span></code>, <code class="docutils literal notranslate"><span class="pre">secret</span></code> and <code class="docutils literal notranslate"><span class="pre">insecure_ssl</span></code>.</p></li>
<li><p><strong>events</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of events which should trigger the webhook. See a list of <a class="reference external" href="https://developer.github.com/v3/activity/events/types/">available events</a></p></li>
</ul>
</dd>
</dl>
<p>The <strong>configuration</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">contentType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">insecureSsl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">secret</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">url</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - URL of the webhook</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_github.OrganizationWebhook.active">
<code class="sig-name descname">active</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_github.OrganizationWebhook.active" title="Permalink to this definition">¶</a></dt>
<dd><p>Indicate of the webhook should receive events. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_github.OrganizationWebhook.configuration">
<code class="sig-name descname">configuration</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_github.OrganizationWebhook.configuration" title="Permalink to this definition">¶</a></dt>
<dd><p>key/value pair of configuration for this webhook. Available keys are <code class="docutils literal notranslate"><span class="pre">url</span></code>, <code class="docutils literal notranslate"><span class="pre">content_type</span></code>, <code class="docutils literal notranslate"><span class="pre">secret</span></code> and <code class="docutils literal notranslate"><span class="pre">insecure_ssl</span></code>.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">contentType</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">insecureSsl</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">secret</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">url</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - URL of the webhook</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_github.OrganizationWebhook.events">
<code class="sig-name descname">events</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_github.OrganizationWebhook.events" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of events which should trigger the webhook. See a list of <a class="reference external" href="https://developer.github.com/v3/activity/events/types/">available events</a></p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_github.OrganizationWebhook.url">
<code class="sig-name descname">url</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_github.OrganizationWebhook.url" title="Permalink to this definition">¶</a></dt>
<dd><p>URL of the webhook</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_github.OrganizationWebhook.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">active</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">configuration</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">etag</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">events</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">url</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_github.OrganizationWebhook.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing OrganizationWebhook resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>active</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Indicate of the webhook should receive events. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>configuration</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – key/value pair of configuration for this webhook. Available keys are <code class="docutils literal notranslate"><span class="pre">url</span></code>, <code class="docutils literal notranslate"><span class="pre">content_type</span></code>, <code class="docutils literal notranslate"><span class="pre">secret</span></code> and <code class="docutils literal notranslate"><span class="pre">insecure_ssl</span></code>.</p></li>
<li><p><strong>events</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – <p>A list of events which should trigger the webhook. See a list of <a class="reference external" href="https://developer.github.com/v3/activity/events/types/">available events</a></p>
</p></li>
<li><p><strong>url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – URL of the webhook</p></li>
</ul>
</dd>
</dl>
<p>The <strong>configuration</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">contentType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">insecureSsl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">secret</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">url</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - URL of the webhook</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_github.OrganizationWebhook.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_github.OrganizationWebhook.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_github.OrganizationWebhook.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_github.OrganizationWebhook.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_github.ProjectColumn">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_github.</code><code class="sig-name descname">ProjectColumn</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_github.ProjectColumn" title="Permalink to this definition">¶</a></dt>
<dd><p>This resource allows you to create and manage columns for GitHub projects.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_github</span> <span class="k">as</span> <span class="nn">github</span>

<span class="n">project</span> <span class="o">=</span> <span class="n">github</span><span class="o">.</span><span class="n">OrganizationProject</span><span class="p">(</span><span class="s2">&quot;project&quot;</span><span class="p">,</span> <span class="n">body</span><span class="o">=</span><span class="s2">&quot;This is an organization project.&quot;</span><span class="p">)</span>
<span class="n">column</span> <span class="o">=</span> <span class="n">github</span><span class="o">.</span><span class="n">ProjectColumn</span><span class="p">(</span><span class="s2">&quot;column&quot;</span><span class="p">,</span> <span class="n">project_id</span><span class="o">=</span><span class="n">project</span><span class="o">.</span><span class="n">id</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the column.</p></li>
<li><p><strong>project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of an existing project that the column will be created in.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_github.ProjectColumn.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_github.ProjectColumn.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the column.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_github.ProjectColumn.project_id">
<code class="sig-name descname">project_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_github.ProjectColumn.project_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of an existing project that the column will be created in.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_github.ProjectColumn.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">etag</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_github.ProjectColumn.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing ProjectColumn resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the column.</p></li>
<li><p><strong>project_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of an existing project that the column will be created in.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_github.ProjectColumn.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_github.ProjectColumn.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_github.ProjectColumn.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_github.ProjectColumn.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_github.Provider">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_github.</code><code class="sig-name descname">Provider</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">anonymous</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">base_url</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">individual</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">insecure</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">organization</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">token</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_github.Provider" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider type for the github package. By default, resources use package-wide configuration
settings, however an explicit <code class="docutils literal notranslate"><span class="pre">Provider</span></code> instance may be created and passed during resource
construction to achieve fine-grained programmatic control over provider settings. See the
<a class="reference external" href="https://www.pulumi.com/docs/reference/programming-model/#providers">documentation</a> for more information.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>anonymous</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Authenticate without a token. When <code class="docutils literal notranslate"><span class="pre">anonymous</span></code>is true, the provider will not be able to access resourcesthat require
authentication.</p></li>
<li><p><strong>base_url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The GitHub Base API URL</p></li>
<li><p><strong>individual</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Run outside an organization. When <code class="docutils literal notranslate"><span class="pre">individual</span></code>is true, the provider will run outside the scope of anorganization.</p></li>
<li><p><strong>insecure</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Whether server should be accessed without verifying the TLS certificate.</p></li>
<li><p><strong>organization</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The GitHub organization name to manage. If <code class="docutils literal notranslate"><span class="pre">individual</span></code> is false, <code class="docutils literal notranslate"><span class="pre">organization</span></code> is required.</p></li>
<li><p><strong>token</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The OAuth token used to connect to GitHub. If <code class="docutils literal notranslate"><span class="pre">anonymous</span></code> is false, <code class="docutils literal notranslate"><span class="pre">token</span></code> is required.</p></li>
</ul>
</dd>
</dl>
<dl class="py method">
<dt id="pulumi_github.Provider.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_github.Provider.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_github.Provider.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_github.Provider.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_github.Repository">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_github.</code><code class="sig-name descname">Repository</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">allow_merge_commit</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">allow_rebase_merge</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">allow_squash_merge</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">archived</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auto_init</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">default_branch</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">delete_branch_on_merge</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">gitignore_template</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">has_downloads</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">has_issues</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">has_projects</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">has_wiki</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">homepage_url</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">is_template</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">license_template</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">private</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">template</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">topics</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_github.Repository" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a Repository resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[bool] allow_merge_commit: Set to <code class="docutils literal notranslate"><span class="pre">false</span></code> to disable merge commits on the repository.
:param pulumi.Input[bool] allow_rebase_merge: Set to <code class="docutils literal notranslate"><span class="pre">false</span></code> to disable rebase merges on the repository.
:param pulumi.Input[bool] allow_squash_merge: Set to <code class="docutils literal notranslate"><span class="pre">false</span></code> to disable squash merges on the repository.
:param pulumi.Input[bool] archived: Specifies if the repository should be archived. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>. <strong>NOTE</strong> Currently, the API does not support unarchiving.
:param pulumi.Input[bool] auto_init: Set to <code class="docutils literal notranslate"><span class="pre">true</span></code> to produce an initial commit in the repository.
:param pulumi.Input[str] default_branch: The name of the default branch of the repository. <strong>NOTE:</strong> This can only be set after a repository has already been created,</p>
<blockquote>
<div><p>and after a correct reference has been created for the target branch inside the repository. This means a user will have to omit this parameter from the
initial repository creation and create the target branch inside of the repository prior to setting this attribute.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>delete_branch_on_merge</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Automatically delete head branch after a pull request is merged. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A description of the repository.</p></li>
<li><p><strong>gitignore_template</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Use the <a class="reference external" href="https://github.com/github/gitignore">name of the template</a> without the extension. For example, “Haskell”.</p></li>
<li><p><strong>has_downloads</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Set to <code class="docutils literal notranslate"><span class="pre">true</span></code> to enable the (deprecated) downloads features on the repository.</p></li>
<li><p><strong>has_issues</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Set to <code class="docutils literal notranslate"><span class="pre">true</span></code> to enable the GitHub Issues features
on the repository.</p></li>
<li><p><strong>has_projects</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – <p>Set to <code class="docutils literal notranslate"><span class="pre">true</span></code> to enable the GitHub Projects features on the repository. Per the GitHub <a class="reference external" href="https://developer.github.com/v3/repos/#create">documentation</a> when in an organization that has disabled repository projects it will default to <code class="docutils literal notranslate"><span class="pre">false</span></code> and will otherwise default to <code class="docutils literal notranslate"><span class="pre">true</span></code>. If you specify <code class="docutils literal notranslate"><span class="pre">true</span></code> when it has been disabled it will return an error.</p>
</p></li>
<li><p><strong>has_wiki</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Set to <code class="docutils literal notranslate"><span class="pre">true</span></code> to enable the GitHub Wiki features on
the repository.</p></li>
<li><p><strong>homepage_url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – URL of a page describing the project.</p></li>
<li><p><strong>is_template</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Set to <code class="docutils literal notranslate"><span class="pre">true</span></code> to tell GitHub that this is a template repository.</p></li>
<li><p><strong>license_template</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>Use the <a class="reference external" href="https://github.com/github/choosealicense.com/tree/gh-pages/_licenses">name of the template</a> without the extension. For example, “mit” or “mpl-2.0”.</p>
</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the repository.</p></li>
<li><p><strong>private</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Set to <code class="docutils literal notranslate"><span class="pre">true</span></code> to create a private repository.
Repositories are created as public (e.g. open source) by default.</p></li>
<li><p><strong>template</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Use a template repository to create this resource. See Template Repositories below for details.</p></li>
<li><p><strong>topics</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The list of topics of the repository.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>template</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">owner</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">repository</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_github.Repository.allow_merge_commit">
<code class="sig-name descname">allow_merge_commit</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_github.Repository.allow_merge_commit" title="Permalink to this definition">¶</a></dt>
<dd><p>Set to <code class="docutils literal notranslate"><span class="pre">false</span></code> to disable merge commits on the repository.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_github.Repository.allow_rebase_merge">
<code class="sig-name descname">allow_rebase_merge</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_github.Repository.allow_rebase_merge" title="Permalink to this definition">¶</a></dt>
<dd><p>Set to <code class="docutils literal notranslate"><span class="pre">false</span></code> to disable rebase merges on the repository.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_github.Repository.allow_squash_merge">
<code class="sig-name descname">allow_squash_merge</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_github.Repository.allow_squash_merge" title="Permalink to this definition">¶</a></dt>
<dd><p>Set to <code class="docutils literal notranslate"><span class="pre">false</span></code> to disable squash merges on the repository.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_github.Repository.archived">
<code class="sig-name descname">archived</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_github.Repository.archived" title="Permalink to this definition">¶</a></dt>
<dd><p>Specifies if the repository should be archived. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>. <strong>NOTE</strong> Currently, the API does not support unarchiving.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_github.Repository.auto_init">
<code class="sig-name descname">auto_init</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_github.Repository.auto_init" title="Permalink to this definition">¶</a></dt>
<dd><p>Set to <code class="docutils literal notranslate"><span class="pre">true</span></code> to produce an initial commit in the repository.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_github.Repository.default_branch">
<code class="sig-name descname">default_branch</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_github.Repository.default_branch" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the default branch of the repository. <strong>NOTE:</strong> This can only be set after a repository has already been created,
and after a correct reference has been created for the target branch inside the repository. This means a user will have to omit this parameter from the
initial repository creation and create the target branch inside of the repository prior to setting this attribute.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_github.Repository.delete_branch_on_merge">
<code class="sig-name descname">delete_branch_on_merge</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_github.Repository.delete_branch_on_merge" title="Permalink to this definition">¶</a></dt>
<dd><p>Automatically delete head branch after a pull request is merged. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_github.Repository.description">
<code class="sig-name descname">description</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_github.Repository.description" title="Permalink to this definition">¶</a></dt>
<dd><p>A description of the repository.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_github.Repository.full_name">
<code class="sig-name descname">full_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_github.Repository.full_name" title="Permalink to this definition">¶</a></dt>
<dd><p>A string of the form “orgname/reponame”.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_github.Repository.git_clone_url">
<code class="sig-name descname">git_clone_url</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_github.Repository.git_clone_url" title="Permalink to this definition">¶</a></dt>
<dd><p>URL that can be provided to <code class="docutils literal notranslate"><span class="pre">git</span> <span class="pre">clone</span></code> to clone the repository anonymously via the git protocol.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_github.Repository.gitignore_template">
<code class="sig-name descname">gitignore_template</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_github.Repository.gitignore_template" title="Permalink to this definition">¶</a></dt>
<dd><p>Use the <a class="reference external" href="https://github.com/github/gitignore">name of the template</a> without the extension. For example, “Haskell”.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_github.Repository.has_downloads">
<code class="sig-name descname">has_downloads</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_github.Repository.has_downloads" title="Permalink to this definition">¶</a></dt>
<dd><p>Set to <code class="docutils literal notranslate"><span class="pre">true</span></code> to enable the (deprecated) downloads features on the repository.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_github.Repository.has_issues">
<code class="sig-name descname">has_issues</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_github.Repository.has_issues" title="Permalink to this definition">¶</a></dt>
<dd><p>Set to <code class="docutils literal notranslate"><span class="pre">true</span></code> to enable the GitHub Issues features
on the repository.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_github.Repository.has_projects">
<code class="sig-name descname">has_projects</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_github.Repository.has_projects" title="Permalink to this definition">¶</a></dt>
<dd><p>Set to <code class="docutils literal notranslate"><span class="pre">true</span></code> to enable the GitHub Projects features on the repository. Per the GitHub <a class="reference external" href="https://developer.github.com/v3/repos/#create">documentation</a> when in an organization that has disabled repository projects it will default to <code class="docutils literal notranslate"><span class="pre">false</span></code> and will otherwise default to <code class="docutils literal notranslate"><span class="pre">true</span></code>. If you specify <code class="docutils literal notranslate"><span class="pre">true</span></code> when it has been disabled it will return an error.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_github.Repository.has_wiki">
<code class="sig-name descname">has_wiki</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_github.Repository.has_wiki" title="Permalink to this definition">¶</a></dt>
<dd><p>Set to <code class="docutils literal notranslate"><span class="pre">true</span></code> to enable the GitHub Wiki features on
the repository.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_github.Repository.homepage_url">
<code class="sig-name descname">homepage_url</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_github.Repository.homepage_url" title="Permalink to this definition">¶</a></dt>
<dd><p>URL of a page describing the project.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_github.Repository.html_url">
<code class="sig-name descname">html_url</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_github.Repository.html_url" title="Permalink to this definition">¶</a></dt>
<dd><p>URL to the repository on the web.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_github.Repository.http_clone_url">
<code class="sig-name descname">http_clone_url</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_github.Repository.http_clone_url" title="Permalink to this definition">¶</a></dt>
<dd><p>URL that can be provided to <code class="docutils literal notranslate"><span class="pre">git</span> <span class="pre">clone</span></code> to clone the repository via HTTPS.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_github.Repository.is_template">
<code class="sig-name descname">is_template</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_github.Repository.is_template" title="Permalink to this definition">¶</a></dt>
<dd><p>Set to <code class="docutils literal notranslate"><span class="pre">true</span></code> to tell GitHub that this is a template repository.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_github.Repository.license_template">
<code class="sig-name descname">license_template</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_github.Repository.license_template" title="Permalink to this definition">¶</a></dt>
<dd><p>Use the <a class="reference external" href="https://github.com/github/choosealicense.com/tree/gh-pages/_licenses">name of the template</a> without the extension. For example, “mit” or “mpl-2.0”.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_github.Repository.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_github.Repository.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the repository.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_github.Repository.private">
<code class="sig-name descname">private</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_github.Repository.private" title="Permalink to this definition">¶</a></dt>
<dd><p>Set to <code class="docutils literal notranslate"><span class="pre">true</span></code> to create a private repository.
Repositories are created as public (e.g. open source) by default.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_github.Repository.ssh_clone_url">
<code class="sig-name descname">ssh_clone_url</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_github.Repository.ssh_clone_url" title="Permalink to this definition">¶</a></dt>
<dd><p>URL that can be provided to <code class="docutils literal notranslate"><span class="pre">git</span> <span class="pre">clone</span></code> to clone the repository via SSH.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_github.Repository.svn_url">
<code class="sig-name descname">svn_url</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_github.Repository.svn_url" title="Permalink to this definition">¶</a></dt>
<dd><p>URL that can be provided to <code class="docutils literal notranslate"><span class="pre">svn</span> <span class="pre">checkout</span></code> to check out the repository via GitHub’s Subversion protocol emulation.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_github.Repository.template">
<code class="sig-name descname">template</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_github.Repository.template" title="Permalink to this definition">¶</a></dt>
<dd><p>Use a template repository to create this resource. See Template Repositories below for details.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">owner</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">repository</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_github.Repository.topics">
<code class="sig-name descname">topics</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_github.Repository.topics" title="Permalink to this definition">¶</a></dt>
<dd><p>The list of topics of the repository.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_github.Repository.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">allow_merge_commit</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">allow_rebase_merge</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">allow_squash_merge</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">archived</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">auto_init</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">default_branch</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">delete_branch_on_merge</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">etag</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">full_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">git_clone_url</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">gitignore_template</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">has_downloads</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">has_issues</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">has_projects</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">has_wiki</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">homepage_url</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">html_url</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">http_clone_url</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">is_template</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">license_template</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">node_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">private</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ssh_clone_url</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">svn_url</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">template</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">topics</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_github.Repository.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Repository resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>allow_merge_commit</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Set to <code class="docutils literal notranslate"><span class="pre">false</span></code> to disable merge commits on the repository.</p></li>
<li><p><strong>allow_rebase_merge</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Set to <code class="docutils literal notranslate"><span class="pre">false</span></code> to disable rebase merges on the repository.</p></li>
<li><p><strong>allow_squash_merge</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Set to <code class="docutils literal notranslate"><span class="pre">false</span></code> to disable squash merges on the repository.</p></li>
<li><p><strong>archived</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Specifies if the repository should be archived. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>. <strong>NOTE</strong> Currently, the API does not support unarchiving.</p></li>
<li><p><strong>auto_init</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Set to <code class="docutils literal notranslate"><span class="pre">true</span></code> to produce an initial commit in the repository.</p></li>
<li><p><strong>default_branch</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the default branch of the repository. <strong>NOTE:</strong> This can only be set after a repository has already been created,
and after a correct reference has been created for the target branch inside the repository. This means a user will have to omit this parameter from the
initial repository creation and create the target branch inside of the repository prior to setting this attribute.</p></li>
<li><p><strong>delete_branch_on_merge</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Automatically delete head branch after a pull request is merged. Defaults to <code class="docutils literal notranslate"><span class="pre">false</span></code>.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A description of the repository.</p></li>
<li><p><strong>full_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A string of the form “orgname/reponame”.</p></li>
<li><p><strong>git_clone_url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – URL that can be provided to <code class="docutils literal notranslate"><span class="pre">git</span> <span class="pre">clone</span></code> to clone the repository anonymously via the git protocol.</p></li>
<li><p><strong>gitignore_template</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>Use the <a class="reference external" href="https://github.com/github/gitignore">name of the template</a> without the extension. For example, “Haskell”.</p>
</p></li>
<li><p><strong>has_downloads</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Set to <code class="docutils literal notranslate"><span class="pre">true</span></code> to enable the (deprecated) downloads features on the repository.</p></li>
<li><p><strong>has_issues</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Set to <code class="docutils literal notranslate"><span class="pre">true</span></code> to enable the GitHub Issues features
on the repository.</p></li>
<li><p><strong>has_projects</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – <p>Set to <code class="docutils literal notranslate"><span class="pre">true</span></code> to enable the GitHub Projects features on the repository. Per the GitHub <a class="reference external" href="https://developer.github.com/v3/repos/#create">documentation</a> when in an organization that has disabled repository projects it will default to <code class="docutils literal notranslate"><span class="pre">false</span></code> and will otherwise default to <code class="docutils literal notranslate"><span class="pre">true</span></code>. If you specify <code class="docutils literal notranslate"><span class="pre">true</span></code> when it has been disabled it will return an error.</p>
</p></li>
<li><p><strong>has_wiki</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Set to <code class="docutils literal notranslate"><span class="pre">true</span></code> to enable the GitHub Wiki features on
the repository.</p></li>
<li><p><strong>homepage_url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – URL of a page describing the project.</p></li>
<li><p><strong>html_url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – URL to the repository on the web.</p></li>
<li><p><strong>http_clone_url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – URL that can be provided to <code class="docutils literal notranslate"><span class="pre">git</span> <span class="pre">clone</span></code> to clone the repository via HTTPS.</p></li>
<li><p><strong>is_template</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Set to <code class="docutils literal notranslate"><span class="pre">true</span></code> to tell GitHub that this is a template repository.</p></li>
<li><p><strong>license_template</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>Use the <a class="reference external" href="https://github.com/github/choosealicense.com/tree/gh-pages/_licenses">name of the template</a> without the extension. For example, “mit” or “mpl-2.0”.</p>
</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the repository.</p></li>
<li><p><strong>private</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Set to <code class="docutils literal notranslate"><span class="pre">true</span></code> to create a private repository.
Repositories are created as public (e.g. open source) by default.</p></li>
<li><p><strong>ssh_clone_url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – URL that can be provided to <code class="docutils literal notranslate"><span class="pre">git</span> <span class="pre">clone</span></code> to clone the repository via SSH.</p></li>
<li><p><strong>svn_url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – URL that can be provided to <code class="docutils literal notranslate"><span class="pre">svn</span> <span class="pre">checkout</span></code> to check out the repository via GitHub’s Subversion protocol emulation.</p></li>
<li><p><strong>template</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – Use a template repository to create this resource. See Template Repositories below for details.</p></li>
<li><p><strong>topics</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The list of topics of the repository.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>template</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">owner</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">repository</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_github.Repository.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_github.Repository.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_github.Repository.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_github.Repository.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_github.RepositoryCollaborator">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_github.</code><code class="sig-name descname">RepositoryCollaborator</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">permission</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">repository</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">username</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_github.RepositoryCollaborator" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a GitHub repository collaborator resource.</p>
<p>This resource allows you to add/remove collaborators from repositories in your
organization. Collaborators can have explicit (and differing levels of) read,
write, or administrator access to specific repositories in your organization,
without giving the user full organization membership.</p>
<p>When applied, an invitation will be sent to the user to become a collaborator
on a repository. When destroyed, either the invitation will be cancelled or the
collaborator will be removed from the repository.</p>
<p>Further documentation on GitHub collaborators:</p>
<ul class="simple">
<li><p><a class="reference external" href="https://help.github.com/articles/adding-outside-collaborators-to-repositories-in-your-organization/">Adding outside collaborators to repositories in your organization</a></p></li>
<li><p><a class="reference external" href="https://help.github.com/articles/converting-an-organization-member-to-an-outside-collaborator/">Converting an organization member to an outside collaborator</a></p></li>
</ul>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_github</span> <span class="k">as</span> <span class="nn">github</span>

<span class="c1"># Add a collaborator to a repository</span>
<span class="n">a_repo_collaborator</span> <span class="o">=</span> <span class="n">github</span><span class="o">.</span><span class="n">RepositoryCollaborator</span><span class="p">(</span><span class="s2">&quot;aRepoCollaborator&quot;</span><span class="p">,</span>
    <span class="n">permission</span><span class="o">=</span><span class="s2">&quot;admin&quot;</span><span class="p">,</span>
    <span class="n">repository</span><span class="o">=</span><span class="s2">&quot;our-cool-repo&quot;</span><span class="p">,</span>
    <span class="n">username</span><span class="o">=</span><span class="s2">&quot;SomeUser&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>permission</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The permission of the outside collaborator for the repository.
Must be one of <code class="docutils literal notranslate"><span class="pre">pull</span></code>, <code class="docutils literal notranslate"><span class="pre">push</span></code>, <code class="docutils literal notranslate"><span class="pre">maintain</span></code>, <code class="docutils literal notranslate"><span class="pre">triage</span></code> or <code class="docutils literal notranslate"><span class="pre">admin</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">push</span></code>.</p></li>
<li><p><strong>repository</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The GitHub repository</p></li>
<li><p><strong>username</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The user to add to the repository as a collaborator.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_github.RepositoryCollaborator.invitation_id">
<code class="sig-name descname">invitation_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_github.RepositoryCollaborator.invitation_id" title="Permalink to this definition">¶</a></dt>
<dd><p>ID of the invitation to be used in <code class="docutils literal notranslate"><span class="pre">.UserInvitationAccepter</span></code></p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_github.RepositoryCollaborator.permission">
<code class="sig-name descname">permission</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_github.RepositoryCollaborator.permission" title="Permalink to this definition">¶</a></dt>
<dd><p>The permission of the outside collaborator for the repository.
Must be one of <code class="docutils literal notranslate"><span class="pre">pull</span></code>, <code class="docutils literal notranslate"><span class="pre">push</span></code>, <code class="docutils literal notranslate"><span class="pre">maintain</span></code>, <code class="docutils literal notranslate"><span class="pre">triage</span></code> or <code class="docutils literal notranslate"><span class="pre">admin</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">push</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_github.RepositoryCollaborator.repository">
<code class="sig-name descname">repository</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_github.RepositoryCollaborator.repository" title="Permalink to this definition">¶</a></dt>
<dd><p>The GitHub repository</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_github.RepositoryCollaborator.username">
<code class="sig-name descname">username</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_github.RepositoryCollaborator.username" title="Permalink to this definition">¶</a></dt>
<dd><p>The user to add to the repository as a collaborator.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_github.RepositoryCollaborator.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">invitation_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">permission</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">repository</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">username</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_github.RepositoryCollaborator.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing RepositoryCollaborator resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>invitation_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – ID of the invitation to be used in <code class="docutils literal notranslate"><span class="pre">.UserInvitationAccepter</span></code></p></li>
<li><p><strong>permission</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The permission of the outside collaborator for the repository.
Must be one of <code class="docutils literal notranslate"><span class="pre">pull</span></code>, <code class="docutils literal notranslate"><span class="pre">push</span></code>, <code class="docutils literal notranslate"><span class="pre">maintain</span></code>, <code class="docutils literal notranslate"><span class="pre">triage</span></code> or <code class="docutils literal notranslate"><span class="pre">admin</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">push</span></code>.</p></li>
<li><p><strong>repository</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The GitHub repository</p></li>
<li><p><strong>username</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The user to add to the repository as a collaborator.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_github.RepositoryCollaborator.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_github.RepositoryCollaborator.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_github.RepositoryCollaborator.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_github.RepositoryCollaborator.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_github.RepositoryDeployKey">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_github.</code><code class="sig-name descname">RepositoryDeployKey</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">key</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">read_only</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">repository</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">title</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_github.RepositoryDeployKey" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a GitHub repository deploy key resource.</p>
<p>A deploy key is an SSH key that is stored on your server and grants
access to a single GitHub repository. This key is attached directly to the repository instead of to a personal user
account.</p>
<p>This resource allows you to add/remove repository deploy keys.</p>
<p>Further documentation on GitHub repository deploy keys:</p>
<ul class="simple">
<li><p><a class="reference external" href="https://developer.github.com/guides/managing-deploy-keys/#deploy-keys">About deploy keys</a></p></li>
</ul>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_github</span> <span class="k">as</span> <span class="nn">github</span>

<span class="c1"># Add a deploy key</span>
<span class="n">example_repository_deploy_key</span> <span class="o">=</span> <span class="n">github</span><span class="o">.</span><span class="n">RepositoryDeployKey</span><span class="p">(</span><span class="s2">&quot;exampleRepositoryDeployKey&quot;</span><span class="p">,</span>
    <span class="n">key</span><span class="o">=</span><span class="s2">&quot;ssh-rsa AAA...&quot;</span><span class="p">,</span>
    <span class="n">read_only</span><span class="o">=</span><span class="s2">&quot;false&quot;</span><span class="p">,</span>
    <span class="n">repository</span><span class="o">=</span><span class="s2">&quot;test-repo&quot;</span><span class="p">,</span>
    <span class="n">title</span><span class="o">=</span><span class="s2">&quot;Repository test key&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A SSH key.</p></li>
<li><p><strong>read_only</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – A boolean qualifying the key to be either read only or read/write.</p></li>
<li><p><strong>repository</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the GitHub repository.</p></li>
<li><p><strong>title</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A title.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_github.RepositoryDeployKey.key">
<code class="sig-name descname">key</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_github.RepositoryDeployKey.key" title="Permalink to this definition">¶</a></dt>
<dd><p>A SSH key.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_github.RepositoryDeployKey.read_only">
<code class="sig-name descname">read_only</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_github.RepositoryDeployKey.read_only" title="Permalink to this definition">¶</a></dt>
<dd><p>A boolean qualifying the key to be either read only or read/write.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_github.RepositoryDeployKey.repository">
<code class="sig-name descname">repository</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_github.RepositoryDeployKey.repository" title="Permalink to this definition">¶</a></dt>
<dd><p>Name of the GitHub repository.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_github.RepositoryDeployKey.title">
<code class="sig-name descname">title</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_github.RepositoryDeployKey.title" title="Permalink to this definition">¶</a></dt>
<dd><p>A title.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_github.RepositoryDeployKey.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">etag</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">key</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">read_only</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">repository</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">title</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_github.RepositoryDeployKey.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing RepositoryDeployKey resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A SSH key.</p></li>
<li><p><strong>read_only</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – A boolean qualifying the key to be either read only or read/write.</p></li>
<li><p><strong>repository</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Name of the GitHub repository.</p></li>
<li><p><strong>title</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A title.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_github.RepositoryDeployKey.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_github.RepositoryDeployKey.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_github.RepositoryDeployKey.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_github.RepositoryDeployKey.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_github.RepositoryFile">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_github.</code><code class="sig-name descname">RepositoryFile</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">branch</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">commit_author</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">commit_email</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">commit_message</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">content</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">repository</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_github.RepositoryFile" title="Permalink to this definition">¶</a></dt>
<dd><p>This resource allows you to create and manage files within a
GitHub repository.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_github</span> <span class="k">as</span> <span class="nn">github</span>

<span class="n">gitignore</span> <span class="o">=</span> <span class="n">github</span><span class="o">.</span><span class="n">RepositoryFile</span><span class="p">(</span><span class="s2">&quot;gitignore&quot;</span><span class="p">,</span>
    <span class="n">content</span><span class="o">=</span><span class="s2">&quot;**/*.tfstate&quot;</span><span class="p">,</span>
    <span class="n">file</span><span class="o">=</span><span class="s2">&quot;.gitignore&quot;</span><span class="p">,</span>
    <span class="n">repository</span><span class="o">=</span><span class="s2">&quot;example&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>branch</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Git branch (defaults to <code class="docutils literal notranslate"><span class="pre">master</span></code>).
The branch must already exist, it will not be created if it does not already exist.</p></li>
<li><p><strong>commit_author</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Committer author name to use.</p></li>
<li><p><strong>commit_email</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Committer email address to use.</p></li>
<li><p><strong>commit_message</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Commit message when adding or updating the managed file.</p></li>
<li><p><strong>content</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The file content.</p></li>
<li><p><strong>file</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The path of the file to manage.</p></li>
<li><p><strong>repository</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The repository name</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_github.RepositoryFile.branch">
<code class="sig-name descname">branch</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_github.RepositoryFile.branch" title="Permalink to this definition">¶</a></dt>
<dd><p>Git branch (defaults to <code class="docutils literal notranslate"><span class="pre">master</span></code>).
The branch must already exist, it will not be created if it does not already exist.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_github.RepositoryFile.commit_author">
<code class="sig-name descname">commit_author</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_github.RepositoryFile.commit_author" title="Permalink to this definition">¶</a></dt>
<dd><p>Committer author name to use.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_github.RepositoryFile.commit_email">
<code class="sig-name descname">commit_email</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_github.RepositoryFile.commit_email" title="Permalink to this definition">¶</a></dt>
<dd><p>Committer email address to use.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_github.RepositoryFile.commit_message">
<code class="sig-name descname">commit_message</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_github.RepositoryFile.commit_message" title="Permalink to this definition">¶</a></dt>
<dd><p>Commit message when adding or updating the managed file.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_github.RepositoryFile.content">
<code class="sig-name descname">content</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_github.RepositoryFile.content" title="Permalink to this definition">¶</a></dt>
<dd><p>The file content.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_github.RepositoryFile.file">
<code class="sig-name descname">file</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_github.RepositoryFile.file" title="Permalink to this definition">¶</a></dt>
<dd><p>The path of the file to manage.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_github.RepositoryFile.repository">
<code class="sig-name descname">repository</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_github.RepositoryFile.repository" title="Permalink to this definition">¶</a></dt>
<dd><p>The repository name</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_github.RepositoryFile.sha">
<code class="sig-name descname">sha</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_github.RepositoryFile.sha" title="Permalink to this definition">¶</a></dt>
<dd><p>The SHA blob of the file.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_github.RepositoryFile.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">branch</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">commit_author</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">commit_email</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">commit_message</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">content</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">file</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">repository</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sha</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_github.RepositoryFile.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing RepositoryFile resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>branch</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Git branch (defaults to <code class="docutils literal notranslate"><span class="pre">master</span></code>).
The branch must already exist, it will not be created if it does not already exist.</p></li>
<li><p><strong>commit_author</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Committer author name to use.</p></li>
<li><p><strong>commit_email</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Committer email address to use.</p></li>
<li><p><strong>commit_message</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Commit message when adding or updating the managed file.</p></li>
<li><p><strong>content</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The file content.</p></li>
<li><p><strong>file</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The path of the file to manage.</p></li>
<li><p><strong>repository</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The repository name</p></li>
<li><p><strong>sha</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The SHA blob of the file.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_github.RepositoryFile.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_github.RepositoryFile.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_github.RepositoryFile.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_github.RepositoryFile.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_github.RepositoryProject">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_github.</code><code class="sig-name descname">RepositoryProject</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">body</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">repository</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_github.RepositoryProject" title="Permalink to this definition">¶</a></dt>
<dd><p>This resource allows you to create and manage projects for GitHub repository.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_github</span> <span class="k">as</span> <span class="nn">github</span>

<span class="n">example</span> <span class="o">=</span> <span class="n">github</span><span class="o">.</span><span class="n">Repository</span><span class="p">(</span><span class="s2">&quot;example&quot;</span><span class="p">,</span>
    <span class="n">description</span><span class="o">=</span><span class="s2">&quot;My awesome codebase&quot;</span><span class="p">,</span>
    <span class="n">has_projects</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
<span class="n">project</span> <span class="o">=</span> <span class="n">github</span><span class="o">.</span><span class="n">RepositoryProject</span><span class="p">(</span><span class="s2">&quot;project&quot;</span><span class="p">,</span>
    <span class="n">body</span><span class="o">=</span><span class="s2">&quot;This is a repository project.&quot;</span><span class="p">,</span>
    <span class="n">repository</span><span class="o">=</span><span class="n">example</span><span class="o">.</span><span class="n">name</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>body</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The body of the project.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the project.</p></li>
<li><p><strong>repository</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The repository of the project.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_github.RepositoryProject.body">
<code class="sig-name descname">body</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_github.RepositoryProject.body" title="Permalink to this definition">¶</a></dt>
<dd><p>The body of the project.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_github.RepositoryProject.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_github.RepositoryProject.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the project.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_github.RepositoryProject.repository">
<code class="sig-name descname">repository</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_github.RepositoryProject.repository" title="Permalink to this definition">¶</a></dt>
<dd><p>The repository of the project.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_github.RepositoryProject.url">
<code class="sig-name descname">url</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_github.RepositoryProject.url" title="Permalink to this definition">¶</a></dt>
<dd><p>URL of the project</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_github.RepositoryProject.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">body</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">etag</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">repository</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">url</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_github.RepositoryProject.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing RepositoryProject resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>body</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The body of the project.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the project.</p></li>
<li><p><strong>repository</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The repository of the project.</p></li>
<li><p><strong>url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – URL of the project</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_github.RepositoryProject.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_github.RepositoryProject.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_github.RepositoryProject.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_github.RepositoryProject.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_github.RepositoryWebhook">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_github.</code><code class="sig-name descname">RepositoryWebhook</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">active</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">configuration</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">events</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">repository</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_github.RepositoryWebhook" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a RepositoryWebhook resource with the given unique name, props, and options.
:param str resource_name: The name of the resource.
:param pulumi.ResourceOptions opts: Options for the resource.
:param pulumi.Input[bool] active: Indicate of the webhook should receive events. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.
:param pulumi.Input[dict] configuration: key/value pair of configuration for this webhook. Available keys are <code class="docutils literal notranslate"><span class="pre">url</span></code>, <code class="docutils literal notranslate"><span class="pre">content_type</span></code>, <code class="docutils literal notranslate"><span class="pre">secret</span></code> and <code class="docutils literal notranslate"><span class="pre">insecure_ssl</span></code>. <code class="docutils literal notranslate"><span class="pre">secret</span></code> is <a class="reference external" href="https://developer.github.com/v3/repos/hooks/#create-a-hook">the shared secret, see API documentation</a>.
:param pulumi.Input[list] events: A list of events which should trigger the webhook. See a list of <a class="reference external" href="https://developer.github.com/v3/activity/events/types/">available events</a>.
:param pulumi.Input[str] repository: The repository of the webhook.</p>
<p>The <strong>configuration</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">contentType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">insecureSsl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">secret</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">url</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - URL of the webhook</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_github.RepositoryWebhook.active">
<code class="sig-name descname">active</code><em class="property">: pulumi.Output[bool]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_github.RepositoryWebhook.active" title="Permalink to this definition">¶</a></dt>
<dd><p>Indicate of the webhook should receive events. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_github.RepositoryWebhook.configuration">
<code class="sig-name descname">configuration</code><em class="property">: pulumi.Output[dict]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_github.RepositoryWebhook.configuration" title="Permalink to this definition">¶</a></dt>
<dd><p>key/value pair of configuration for this webhook. Available keys are <code class="docutils literal notranslate"><span class="pre">url</span></code>, <code class="docutils literal notranslate"><span class="pre">content_type</span></code>, <code class="docutils literal notranslate"><span class="pre">secret</span></code> and <code class="docutils literal notranslate"><span class="pre">insecure_ssl</span></code>. <code class="docutils literal notranslate"><span class="pre">secret</span></code> is <a class="reference external" href="https://developer.github.com/v3/repos/hooks/#create-a-hook">the shared secret, see API documentation</a>.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">contentType</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">insecureSsl</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">secret</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">url</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - URL of the webhook</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_github.RepositoryWebhook.events">
<code class="sig-name descname">events</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_github.RepositoryWebhook.events" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of events which should trigger the webhook. See a list of <a class="reference external" href="https://developer.github.com/v3/activity/events/types/">available events</a>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_github.RepositoryWebhook.repository">
<code class="sig-name descname">repository</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_github.RepositoryWebhook.repository" title="Permalink to this definition">¶</a></dt>
<dd><p>The repository of the webhook.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_github.RepositoryWebhook.url">
<code class="sig-name descname">url</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_github.RepositoryWebhook.url" title="Permalink to this definition">¶</a></dt>
<dd><p>URL of the webhook</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_github.RepositoryWebhook.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">active</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">configuration</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">etag</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">events</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">repository</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">url</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_github.RepositoryWebhook.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing RepositoryWebhook resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>active</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – Indicate of the webhook should receive events. Defaults to <code class="docutils literal notranslate"><span class="pre">true</span></code>.</p></li>
<li><p><strong>configuration</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – <p>key/value pair of configuration for this webhook. Available keys are <code class="docutils literal notranslate"><span class="pre">url</span></code>, <code class="docutils literal notranslate"><span class="pre">content_type</span></code>, <code class="docutils literal notranslate"><span class="pre">secret</span></code> and <code class="docutils literal notranslate"><span class="pre">insecure_ssl</span></code>. <code class="docutils literal notranslate"><span class="pre">secret</span></code> is <a class="reference external" href="https://developer.github.com/v3/repos/hooks/#create-a-hook">the shared secret, see API documentation</a>.</p>
</p></li>
<li><p><strong>events</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – <p>A list of events which should trigger the webhook. See a list of <a class="reference external" href="https://developer.github.com/v3/activity/events/types/">available events</a>.</p>
</p></li>
<li><p><strong>repository</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The repository of the webhook.</p></li>
<li><p><strong>url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – URL of the webhook</p></li>
</ul>
</dd>
</dl>
<p>The <strong>configuration</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">contentType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">insecureSsl</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">secret</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">url</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - URL of the webhook</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_github.RepositoryWebhook.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_github.RepositoryWebhook.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_github.RepositoryWebhook.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_github.RepositoryWebhook.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_github.Team">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_github.</code><code class="sig-name descname">Team</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ldap_dn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">parent_team_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">privacy</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_github.Team" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a GitHub team resource.</p>
<p>This resource allows you to add/remove teams from your organization. When applied,
a new team will be created. When destroyed, that team will be removed.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_github</span> <span class="k">as</span> <span class="nn">github</span>

<span class="c1"># Add a team to the organization</span>
<span class="n">some_team</span> <span class="o">=</span> <span class="n">github</span><span class="o">.</span><span class="n">Team</span><span class="p">(</span><span class="s2">&quot;someTeam&quot;</span><span class="p">,</span>
    <span class="n">description</span><span class="o">=</span><span class="s2">&quot;Some cool team&quot;</span><span class="p">,</span>
    <span class="n">privacy</span><span class="o">=</span><span class="s2">&quot;closed&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A description of the team.</p></li>
<li><p><strong>ldap_dn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The LDAP Distinguished Name of the group where membership will be synchronized. Only available in GitHub Enterprise.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the team.</p></li>
<li><p><strong>parent_team_id</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The ID of the parent team, if this is a nested team.</p></li>
<li><p><strong>privacy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The level of privacy for the team. Must be one of <code class="docutils literal notranslate"><span class="pre">secret</span></code> or <code class="docutils literal notranslate"><span class="pre">closed</span></code>.
Defaults to <code class="docutils literal notranslate"><span class="pre">secret</span></code>.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_github.Team.description">
<code class="sig-name descname">description</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_github.Team.description" title="Permalink to this definition">¶</a></dt>
<dd><p>A description of the team.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_github.Team.ldap_dn">
<code class="sig-name descname">ldap_dn</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_github.Team.ldap_dn" title="Permalink to this definition">¶</a></dt>
<dd><p>The LDAP Distinguished Name of the group where membership will be synchronized. Only available in GitHub Enterprise.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_github.Team.name">
<code class="sig-name descname">name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_github.Team.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the team.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_github.Team.parent_team_id">
<code class="sig-name descname">parent_team_id</code><em class="property">: pulumi.Output[float]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_github.Team.parent_team_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the parent team, if this is a nested team.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_github.Team.privacy">
<code class="sig-name descname">privacy</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_github.Team.privacy" title="Permalink to this definition">¶</a></dt>
<dd><p>The level of privacy for the team. Must be one of <code class="docutils literal notranslate"><span class="pre">secret</span></code> or <code class="docutils literal notranslate"><span class="pre">closed</span></code>.
Defaults to <code class="docutils literal notranslate"><span class="pre">secret</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_github.Team.slug">
<code class="sig-name descname">slug</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_github.Team.slug" title="Permalink to this definition">¶</a></dt>
<dd><p>The slug of the created team, which may or may not differ from <code class="docutils literal notranslate"><span class="pre">name</span></code>,
depending on whether <code class="docutils literal notranslate"><span class="pre">name</span></code> contains “URL-unsafe” characters.
Useful when referencing the team in <cite>`</cite>.BranchProtection`` &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/github/r/branch_protection.html">https://www.terraform.io/docs/providers/github/r/branch_protection.html</a>&gt;`_.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_github.Team.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">etag</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">ldap_dn</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">node_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">parent_team_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">privacy</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">slug</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_github.Team.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Team resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A description of the team.</p></li>
<li><p><strong>ldap_dn</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The LDAP Distinguished Name of the group where membership will be synchronized. Only available in GitHub Enterprise.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the team.</p></li>
<li><p><strong>parent_team_id</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – The ID of the parent team, if this is a nested team.</p></li>
<li><p><strong>privacy</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The level of privacy for the team. Must be one of <code class="docutils literal notranslate"><span class="pre">secret</span></code> or <code class="docutils literal notranslate"><span class="pre">closed</span></code>.
Defaults to <code class="docutils literal notranslate"><span class="pre">secret</span></code>.</p></li>
<li><p><strong>slug</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The slug of the created team, which may or may not differ from <code class="docutils literal notranslate"><span class="pre">name</span></code>,
depending on whether <code class="docutils literal notranslate"><span class="pre">name</span></code> contains “URL-unsafe” characters.
Useful when referencing the team in <cite>`</cite>.BranchProtection`` &lt;<a class="reference external" href="https://www.terraform.io/docs/providers/github/r/branch_protection.html">https://www.terraform.io/docs/providers/github/r/branch_protection.html</a>&gt;`_.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_github.Team.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_github.Team.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_github.Team.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_github.Team.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_github.TeamMembership">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_github.</code><code class="sig-name descname">TeamMembership</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">role</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">team_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">username</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_github.TeamMembership" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a GitHub team membership resource.</p>
<p>This resource allows you to add/remove users from teams in your organization. When applied,
the user will be added to the team. If the user hasn’t accepted their invitation to the
organization, they won’t be part of the team until they do. When
destroyed, the user will be removed from the team.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_github</span> <span class="k">as</span> <span class="nn">github</span>

<span class="c1"># Add a user to the organization</span>
<span class="n">membership_for_some_user</span> <span class="o">=</span> <span class="n">github</span><span class="o">.</span><span class="n">Membership</span><span class="p">(</span><span class="s2">&quot;membershipForSomeUser&quot;</span><span class="p">,</span>
    <span class="n">role</span><span class="o">=</span><span class="s2">&quot;member&quot;</span><span class="p">,</span>
    <span class="n">username</span><span class="o">=</span><span class="s2">&quot;SomeUser&quot;</span><span class="p">)</span>
<span class="n">some_team</span> <span class="o">=</span> <span class="n">github</span><span class="o">.</span><span class="n">Team</span><span class="p">(</span><span class="s2">&quot;someTeam&quot;</span><span class="p">,</span> <span class="n">description</span><span class="o">=</span><span class="s2">&quot;Some cool team&quot;</span><span class="p">)</span>
<span class="n">some_team_membership</span> <span class="o">=</span> <span class="n">github</span><span class="o">.</span><span class="n">TeamMembership</span><span class="p">(</span><span class="s2">&quot;someTeamMembership&quot;</span><span class="p">,</span>
    <span class="n">role</span><span class="o">=</span><span class="s2">&quot;member&quot;</span><span class="p">,</span>
    <span class="n">team_id</span><span class="o">=</span><span class="n">some_team</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">username</span><span class="o">=</span><span class="s2">&quot;SomeUser&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The role of the user within the team.
Must be one of <code class="docutils literal notranslate"><span class="pre">member</span></code> or <code class="docutils literal notranslate"><span class="pre">maintainer</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">member</span></code>.</p></li>
<li><p><strong>team_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The GitHub team id</p></li>
<li><p><strong>username</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The user to add to the team.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_github.TeamMembership.role">
<code class="sig-name descname">role</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_github.TeamMembership.role" title="Permalink to this definition">¶</a></dt>
<dd><p>The role of the user within the team.
Must be one of <code class="docutils literal notranslate"><span class="pre">member</span></code> or <code class="docutils literal notranslate"><span class="pre">maintainer</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">member</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_github.TeamMembership.team_id">
<code class="sig-name descname">team_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_github.TeamMembership.team_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The GitHub team id</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_github.TeamMembership.username">
<code class="sig-name descname">username</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_github.TeamMembership.username" title="Permalink to this definition">¶</a></dt>
<dd><p>The user to add to the team.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_github.TeamMembership.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">etag</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">role</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">team_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">username</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_github.TeamMembership.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing TeamMembership resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The role of the user within the team.
Must be one of <code class="docutils literal notranslate"><span class="pre">member</span></code> or <code class="docutils literal notranslate"><span class="pre">maintainer</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">member</span></code>.</p></li>
<li><p><strong>team_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The GitHub team id</p></li>
<li><p><strong>username</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The user to add to the team.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_github.TeamMembership.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_github.TeamMembership.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_github.TeamMembership.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_github.TeamMembership.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_github.TeamRepository">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_github.</code><code class="sig-name descname">TeamRepository</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">permission</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">repository</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">team_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_github.TeamRepository" title="Permalink to this definition">¶</a></dt>
<dd><p>This resource manages relationships between teams and repositories
in your GitHub organization.</p>
<p>Creating this resource grants a particular team permissions on a
particular repository.</p>
<p>The repository and the team must both belong to the same organization
on GitHub. This resource does not actually <em>create</em> any repositories;
to do that, see <code class="docutils literal notranslate"><span class="pre">.Repository</span></code>.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_github</span> <span class="k">as</span> <span class="nn">github</span>

<span class="c1"># Add a repository to the team</span>
<span class="n">some_team</span> <span class="o">=</span> <span class="n">github</span><span class="o">.</span><span class="n">Team</span><span class="p">(</span><span class="s2">&quot;someTeam&quot;</span><span class="p">,</span> <span class="n">description</span><span class="o">=</span><span class="s2">&quot;Some cool team&quot;</span><span class="p">)</span>
<span class="n">some_repo</span> <span class="o">=</span> <span class="n">github</span><span class="o">.</span><span class="n">Repository</span><span class="p">(</span><span class="s2">&quot;someRepo&quot;</span><span class="p">)</span>
<span class="n">some_team_repo</span> <span class="o">=</span> <span class="n">github</span><span class="o">.</span><span class="n">TeamRepository</span><span class="p">(</span><span class="s2">&quot;someTeamRepo&quot;</span><span class="p">,</span>
    <span class="n">permission</span><span class="o">=</span><span class="s2">&quot;pull&quot;</span><span class="p">,</span>
    <span class="n">repository</span><span class="o">=</span><span class="n">some_repo</span><span class="o">.</span><span class="n">name</span><span class="p">,</span>
    <span class="n">team_id</span><span class="o">=</span><span class="n">some_team</span><span class="o">.</span><span class="n">id</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>permission</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The permissions of team members regarding the repository.
Must be one of <code class="docutils literal notranslate"><span class="pre">pull</span></code>, <code class="docutils literal notranslate"><span class="pre">triage</span></code>, <code class="docutils literal notranslate"><span class="pre">push</span></code>, <code class="docutils literal notranslate"><span class="pre">maintain</span></code>, or <code class="docutils literal notranslate"><span class="pre">admin</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">pull</span></code>.</p></li>
<li><p><strong>repository</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The repository to add to the team.</p></li>
<li><p><strong>team_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The GitHub team id</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_github.TeamRepository.permission">
<code class="sig-name descname">permission</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_github.TeamRepository.permission" title="Permalink to this definition">¶</a></dt>
<dd><p>The permissions of team members regarding the repository.
Must be one of <code class="docutils literal notranslate"><span class="pre">pull</span></code>, <code class="docutils literal notranslate"><span class="pre">triage</span></code>, <code class="docutils literal notranslate"><span class="pre">push</span></code>, <code class="docutils literal notranslate"><span class="pre">maintain</span></code>, or <code class="docutils literal notranslate"><span class="pre">admin</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">pull</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_github.TeamRepository.repository">
<code class="sig-name descname">repository</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_github.TeamRepository.repository" title="Permalink to this definition">¶</a></dt>
<dd><p>The repository to add to the team.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_github.TeamRepository.team_id">
<code class="sig-name descname">team_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_github.TeamRepository.team_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The GitHub team id</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_github.TeamRepository.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">etag</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">permission</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">repository</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">team_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_github.TeamRepository.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing TeamRepository resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>permission</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The permissions of team members regarding the repository.
Must be one of <code class="docutils literal notranslate"><span class="pre">pull</span></code>, <code class="docutils literal notranslate"><span class="pre">triage</span></code>, <code class="docutils literal notranslate"><span class="pre">push</span></code>, <code class="docutils literal notranslate"><span class="pre">maintain</span></code>, or <code class="docutils literal notranslate"><span class="pre">admin</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">pull</span></code>.</p></li>
<li><p><strong>repository</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The repository to add to the team.</p></li>
<li><p><strong>team_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The GitHub team id</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_github.TeamRepository.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_github.TeamRepository.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_github.TeamRepository.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_github.TeamRepository.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_github.TeamSyncGroupMapping">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_github.</code><code class="sig-name descname">TeamSyncGroupMapping</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">groups</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">team_slug</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_github.TeamSyncGroupMapping" title="Permalink to this definition">¶</a></dt>
<dd><p>This resource allows you to create and manage Identity Provider (IdP) group connections within your GitHub teams.
You must have team synchronization enabled for organizations owned by enterprise accounts.</p>
<p>To learn more about team synchronization between IdPs and Github, please refer to:
<a class="reference external" href="https://help.github.com/en/github/setting-up-and-managing-organizations-and-teams/synchronizing-teams-between-your-identity-provider-and-github">https://help.github.com/en/github/setting-up-and-managing-organizations-and-teams/synchronizing-teams-between-your-identity-provider-and-github</a></p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_github</span> <span class="k">as</span> <span class="nn">github</span>

<span class="n">example_groups</span> <span class="o">=</span> <span class="n">github</span><span class="o">.</span><span class="n">get_organization_team_sync_groups</span><span class="p">()</span>
<span class="n">example_group_mapping</span> <span class="o">=</span> <span class="n">github</span><span class="o">.</span><span class="n">TeamSyncGroupMapping</span><span class="p">(</span><span class="s2">&quot;exampleGroupMapping&quot;</span><span class="p">,</span>
    <span class="n">team_slug</span><span class="o">=</span><span class="s2">&quot;example&quot;</span><span class="p">,</span>
    <span class="n">dynamic</span><span class="o">=</span><span class="p">[{</span>
        <span class="s2">&quot;forEach&quot;</span><span class="p">:</span> <span class="p">[</span><span class="n">g</span> <span class="k">for</span> <span class="n">g</span> <span class="ow">in</span> <span class="n">example_groups</span><span class="o">.</span><span class="n">groups</span> <span class="k">if</span> <span class="n">g</span><span class="p">[</span><span class="s2">&quot;groupName&quot;</span><span class="p">]</span> <span class="o">==</span> <span class="s2">&quot;some_team_group&quot;</span><span class="p">],</span>
        <span class="s2">&quot;content&quot;</span><span class="p">:</span> <span class="p">[{</span>
            <span class="s2">&quot;groupId&quot;</span><span class="p">:</span> <span class="n">group</span><span class="p">[</span><span class="s2">&quot;value&quot;</span><span class="p">][</span><span class="s2">&quot;group_id&quot;</span><span class="p">],</span>
            <span class="s2">&quot;groupName&quot;</span><span class="p">:</span> <span class="n">group</span><span class="p">[</span><span class="s2">&quot;value&quot;</span><span class="p">][</span><span class="s2">&quot;group_name&quot;</span><span class="p">],</span>
            <span class="s2">&quot;groupDescription&quot;</span><span class="p">:</span> <span class="n">group</span><span class="p">[</span><span class="s2">&quot;value&quot;</span><span class="p">][</span><span class="s2">&quot;group_description&quot;</span><span class="p">],</span>
        <span class="p">}],</span>
    <span class="p">}])</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource*name</strong> (<em>str</em>) – <p>The name of the resource.</p>
</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>groups</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – An Array of GitHub Identity Provider Groups (or empty []).  Each <code class="docutils literal notranslate"><span class="pre">group</span></code> block consists of the fields documented below.
__*</p></li>
<li><p><strong>team_slug</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Slug of the team</p></li>
</ul>
</dd>
</dl>
<p>The <strong>groups</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">groupDescription</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The description of the IdP group.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">groupId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the IdP group.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">groupName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the IdP group.</p></li>
</ul>
<dl class="py attribute">
<dt id="pulumi_github.TeamSyncGroupMapping.groups">
<code class="sig-name descname">groups</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_github.TeamSyncGroupMapping.groups" title="Permalink to this definition">¶</a></dt>
<dd><p>An Array of GitHub Identity Provider Groups (or empty []).  Each <code class="docutils literal notranslate"><span class="pre">group</span></code> block consists of the fields documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">groupDescription</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The description of the IdP group.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">groupId</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The ID of the IdP group.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">groupName</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>) - The name of the IdP group.</p></li>
</ul>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_github.TeamSyncGroupMapping.team_slug">
<code class="sig-name descname">team_slug</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_github.TeamSyncGroupMapping.team_slug" title="Permalink to this definition">¶</a></dt>
<dd><p>Slug of the team</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_github.TeamSyncGroupMapping.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">etag</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">groups</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">team_slug</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_github.TeamSyncGroupMapping.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing TeamSyncGroupMapping resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource*name</strong> (<em>str</em>) – <p>The unique name of the resulting resource.</p>
</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>groups</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – An Array of GitHub Identity Provider Groups (or empty []).  Each <code class="docutils literal notranslate"><span class="pre">group</span></code> block consists of the fields documented below.
__*</p></li>
<li><p><strong>team_slug</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Slug of the team</p></li>
</ul>
</dd>
</dl>
<p>The <strong>groups</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">groupDescription</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The description of the IdP group.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">groupId</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The ID of the IdP group.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">groupName</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>) - The name of the IdP group.</p></li>
</ul>
</dd></dl>

<dl class="py method">
<dt id="pulumi_github.TeamSyncGroupMapping.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_github.TeamSyncGroupMapping.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_github.TeamSyncGroupMapping.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_github.TeamSyncGroupMapping.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_github.UserGpgKey">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_github.</code><code class="sig-name descname">UserGpgKey</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">armored_public_key</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_github.UserGpgKey" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a GitHub user’s GPG key resource.</p>
<p>This resource allows you to add/remove GPG keys from your user account.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_github</span> <span class="k">as</span> <span class="nn">github</span>

<span class="n">example</span> <span class="o">=</span> <span class="n">github</span><span class="o">.</span><span class="n">UserGpgKey</span><span class="p">(</span><span class="s2">&quot;example&quot;</span><span class="p">,</span> <span class="n">armored_public_key</span><span class="o">=</span><span class="s2">&quot;&quot;&quot;-----BEGIN PGP PUBLIC KEY BLOCK-----</span>
<span class="s2">...</span>
<span class="s2">-----END PGP PUBLIC KEY BLOCK-----</span>
<span class="s2">&quot;&quot;&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>armored_public_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Your public GPG key, generated in ASCII-armored format.
See <a class="reference external" href="https://help.github.com/articles/generating-a-new-gpg-key/">Generating a new GPG key</a> for help on creating a GPG key.</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_github.UserGpgKey.armored_public_key">
<code class="sig-name descname">armored_public_key</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_github.UserGpgKey.armored_public_key" title="Permalink to this definition">¶</a></dt>
<dd><p>Your public GPG key, generated in ASCII-armored format.
See <a class="reference external" href="https://help.github.com/articles/generating-a-new-gpg-key/">Generating a new GPG key</a> for help on creating a GPG key.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_github.UserGpgKey.key_id">
<code class="sig-name descname">key_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_github.UserGpgKey.key_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The key ID of the GPG key, e.g. <code class="docutils literal notranslate"><span class="pre">3262EFF25BA0D270</span></code></p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_github.UserGpgKey.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">armored_public_key</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">etag</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">key_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_github.UserGpgKey.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing UserGpgKey resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>armored_public_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>Your public GPG key, generated in ASCII-armored format.
See <a class="reference external" href="https://help.github.com/articles/generating-a-new-gpg-key/">Generating a new GPG key</a> for help on creating a GPG key.</p>
</p></li>
<li><p><strong>key_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The key ID of the GPG key, e.g. <code class="docutils literal notranslate"><span class="pre">3262EFF25BA0D270</span></code></p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_github.UserGpgKey.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_github.UserGpgKey.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_github.UserGpgKey.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_github.UserGpgKey.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_github.UserInvitationAccepter">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_github.</code><code class="sig-name descname">UserInvitationAccepter</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">invitation_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_github.UserInvitationAccepter" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a resource to manage GitHub repository collaborator invitations.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_github</span> <span class="k">as</span> <span class="nn">github</span>
<span class="kn">import</span> <span class="nn">pulumi_pulumi</span> <span class="k">as</span> <span class="nn">pulumi</span>

<span class="n">example_repository</span> <span class="o">=</span> <span class="n">github</span><span class="o">.</span><span class="n">Repository</span><span class="p">(</span><span class="s2">&quot;exampleRepository&quot;</span><span class="p">)</span>
<span class="n">example_repository_collaborator</span> <span class="o">=</span> <span class="n">github</span><span class="o">.</span><span class="n">RepositoryCollaborator</span><span class="p">(</span><span class="s2">&quot;exampleRepositoryCollaborator&quot;</span><span class="p">,</span>
    <span class="n">permission</span><span class="o">=</span><span class="s2">&quot;push&quot;</span><span class="p">,</span>
    <span class="n">repository</span><span class="o">=</span><span class="n">example_repository</span><span class="o">.</span><span class="n">name</span><span class="p">,</span>
    <span class="n">username</span><span class="o">=</span><span class="s2">&quot;example-username&quot;</span><span class="p">)</span>
<span class="n">invitee</span> <span class="o">=</span> <span class="n">pulumi</span><span class="o">.</span><span class="n">providers</span><span class="o">.</span><span class="n">Github</span><span class="p">(</span><span class="s2">&quot;invitee&quot;</span><span class="p">,</span> <span class="n">token</span><span class="o">=</span><span class="n">var</span><span class="p">[</span><span class="s2">&quot;invitee_token&quot;</span><span class="p">])</span>
<span class="n">example_user_invitation_accepter</span> <span class="o">=</span> <span class="n">github</span><span class="o">.</span><span class="n">UserInvitationAccepter</span><span class="p">(</span><span class="s2">&quot;exampleUserInvitationAccepter&quot;</span><span class="p">,</span> <span class="n">invitation_id</span><span class="o">=</span><span class="n">example_repository_collaborator</span><span class="o">.</span><span class="n">invitation_id</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>invitation_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – ID of the invitation to accept</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_github.UserInvitationAccepter.invitation_id">
<code class="sig-name descname">invitation_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_github.UserInvitationAccepter.invitation_id" title="Permalink to this definition">¶</a></dt>
<dd><p>ID of the invitation to accept</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_github.UserInvitationAccepter.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">invitation_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_github.UserInvitationAccepter.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing UserInvitationAccepter resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>invitation_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – ID of the invitation to accept</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_github.UserInvitationAccepter.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_github.UserInvitationAccepter.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_github.UserInvitationAccepter.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_github.UserInvitationAccepter.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_github.UserSshKey">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_github.</code><code class="sig-name descname">UserSshKey</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">key</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">title</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_github.UserSshKey" title="Permalink to this definition">¶</a></dt>
<dd><p>Provides a GitHub user’s SSH key resource.</p>
<p>This resource allows you to add/remove SSH keys from your user account.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_github</span> <span class="k">as</span> <span class="nn">github</span>

<span class="n">example</span> <span class="o">=</span> <span class="n">github</span><span class="o">.</span><span class="n">UserSshKey</span><span class="p">(</span><span class="s2">&quot;example&quot;</span><span class="p">,</span>
    <span class="n">key</span><span class="o">=</span><span class="p">(</span><span class="k">lambda</span> <span class="n">path</span><span class="p">:</span> <span class="nb">open</span><span class="p">(</span><span class="n">path</span><span class="p">)</span><span class="o">.</span><span class="n">read</span><span class="p">())(</span><span class="s2">&quot;~/.ssh/id_rsa.pub&quot;</span><span class="p">),</span>
    <span class="n">title</span><span class="o">=</span><span class="s2">&quot;example title&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The public SSH key to add to your GitHub account.</p></li>
<li><p><strong>title</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A descriptive name for the new key. e.g. <code class="docutils literal notranslate"><span class="pre">Personal</span> <span class="pre">MacBook</span> <span class="pre">Air</span></code></p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_github.UserSshKey.key">
<code class="sig-name descname">key</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_github.UserSshKey.key" title="Permalink to this definition">¶</a></dt>
<dd><p>The public SSH key to add to your GitHub account.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_github.UserSshKey.title">
<code class="sig-name descname">title</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_github.UserSshKey.title" title="Permalink to this definition">¶</a></dt>
<dd><p>A descriptive name for the new key. e.g. <code class="docutils literal notranslate"><span class="pre">Personal</span> <span class="pre">MacBook</span> <span class="pre">Air</span></code></p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_github.UserSshKey.url">
<code class="sig-name descname">url</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_github.UserSshKey.url" title="Permalink to this definition">¶</a></dt>
<dd><p>The URL of the SSH key</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_github.UserSshKey.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">etag</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">key</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">title</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">url</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_github.UserSshKey.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing UserSshKey resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The public SSH key to add to your GitHub account.</p></li>
<li><p><strong>title</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A descriptive name for the new key. e.g. <code class="docutils literal notranslate"><span class="pre">Personal</span> <span class="pre">MacBook</span> <span class="pre">Air</span></code></p></li>
<li><p><strong>url</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The URL of the SSH key</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py method">
<dt id="pulumi_github.UserSshKey.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_github.UserSshKey.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_github.UserSshKey.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_github.UserSshKey.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_github.get_actions_public_key">
<code class="sig-prename descclassname">pulumi_github.</code><code class="sig-name descname">get_actions_public_key</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">repository</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_github.get_actions_public_key" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to retrieve information about a GitHub Actions public key. This data source is required to be used with other GitHub secrets interactions.
Note that the provider <code class="docutils literal notranslate"><span class="pre">token</span></code> must have admin rights to a repository to retrieve it’s action public key.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_github</span> <span class="k">as</span> <span class="nn">github</span>

<span class="n">example</span> <span class="o">=</span> <span class="n">github</span><span class="o">.</span><span class="n">get_actions_public_key</span><span class="p">(</span><span class="n">repository</span><span class="o">=</span><span class="s2">&quot;example_repo&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>repository</strong> (<em>str</em>) – Name of the repository to get public key from.</p>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_github.get_branch">
<code class="sig-prename descclassname">pulumi_github.</code><code class="sig-name descname">get_branch</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">branch</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">repository</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_github.get_branch" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to retrieve information about a repository branch.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_github</span> <span class="k">as</span> <span class="nn">github</span>

<span class="n">development</span> <span class="o">=</span> <span class="n">github</span><span class="o">.</span><span class="n">get_branch</span><span class="p">(</span><span class="n">branch</span><span class="o">=</span><span class="s2">&quot;development&quot;</span><span class="p">,</span>
    <span class="n">repository</span><span class="o">=</span><span class="s2">&quot;example&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>branch</strong> (<em>str</em>) – The repository branch to create.</p></li>
<li><p><strong>repository</strong> (<em>str</em>) – The GitHub repository name.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_github.get_collaborators">
<code class="sig-prename descclassname">pulumi_github.</code><code class="sig-name descname">get_collaborators</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">affiliation</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">owner</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">repository</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_github.get_collaborators" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to retrieve the collaborators for a given repository.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_github</span> <span class="k">as</span> <span class="nn">github</span>

<span class="n">test</span> <span class="o">=</span> <span class="n">github</span><span class="o">.</span><span class="n">get_collaborators</span><span class="p">(</span><span class="n">owner</span><span class="o">=</span><span class="s2">&quot;example_owner&quot;</span><span class="p">,</span>
    <span class="n">repository</span><span class="o">=</span><span class="s2">&quot;example_repository&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>affiliation</strong> (<em>str</em>) – Filter collaborators returned by their affiliation. Can be one of: <code class="docutils literal notranslate"><span class="pre">outside</span></code>, <code class="docutils literal notranslate"><span class="pre">direct</span></code>, <code class="docutils literal notranslate"><span class="pre">all</span></code>.  Defaults to <code class="docutils literal notranslate"><span class="pre">all</span></code>.</p></li>
<li><p><strong>owner</strong> (<em>str</em>) – The organization that owns the repository.</p></li>
<li><p><strong>repository</strong> (<em>str</em>) – The name of the repository.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_github.get_ip_ranges">
<code class="sig-prename descclassname">pulumi_github.</code><code class="sig-name descname">get_ip_ranges</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_github.get_ip_ranges" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to retrieve information about GitHub’s IP addresses.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_github</span> <span class="k">as</span> <span class="nn">github</span>

<span class="n">test</span> <span class="o">=</span> <span class="n">github</span><span class="o">.</span><span class="n">get_ip_ranges</span><span class="p">()</span>
</pre></div>
</div>
</dd></dl>

<dl class="py function">
<dt id="pulumi_github.get_membership">
<code class="sig-prename descclassname">pulumi_github.</code><code class="sig-name descname">get_membership</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">username</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_github.get_membership" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to find out if a user is a member of your organization, as well
as what role they have within it.
If the user’s membership in the organization is pending their acceptance of an invite,
the role they would have once they accept will be returned.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_github</span> <span class="k">as</span> <span class="nn">github</span>

<span class="n">membership_for_some_user</span> <span class="o">=</span> <span class="n">github</span><span class="o">.</span><span class="n">get_membership</span><span class="p">(</span><span class="n">username</span><span class="o">=</span><span class="s2">&quot;SomeUser&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>username</strong> (<em>str</em>) – The username to lookup in the organization.</p>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_github.get_organization_team_sync_groups">
<code class="sig-prename descclassname">pulumi_github.</code><code class="sig-name descname">get_organization_team_sync_groups</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_github.get_organization_team_sync_groups" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to retrieve the identity provider (IdP) groups for an organization.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_github</span> <span class="k">as</span> <span class="nn">github</span>

<span class="n">test</span> <span class="o">=</span> <span class="n">github</span><span class="o">.</span><span class="n">get_organization_team_sync_groups</span><span class="p">()</span>
</pre></div>
</div>
</dd></dl>

<dl class="py function">
<dt id="pulumi_github.get_release">
<code class="sig-prename descclassname">pulumi_github.</code><code class="sig-name descname">get_release</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">owner</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">release_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">release_tag</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">repository</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">retrieve_by</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_github.get_release" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to retrieve information about a GitHub release in a specific repository.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_github</span> <span class="k">as</span> <span class="nn">github</span>

<span class="n">example</span> <span class="o">=</span> <span class="n">github</span><span class="o">.</span><span class="n">get_release</span><span class="p">(</span><span class="n">owner</span><span class="o">=</span><span class="s2">&quot;example-owner&quot;</span><span class="p">,</span>
    <span class="n">repository</span><span class="o">=</span><span class="s2">&quot;example-repository&quot;</span><span class="p">,</span>
    <span class="n">retrieve_by</span><span class="o">=</span><span class="s2">&quot;latest&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>owner</strong> (<em>str</em>) – Owner of the repository.</p></li>
<li><p><strong>release_id</strong> (<em>float</em>) – ID of the release to retrieve. Must be specified when <code class="docutils literal notranslate"><span class="pre">retrieve_by</span></code> = <code class="docutils literal notranslate"><span class="pre">id</span></code>.</p></li>
<li><p><strong>release_tag</strong> (<em>str</em>) – Tag of the release to retrieve. Must be specified when <code class="docutils literal notranslate"><span class="pre">retrieve_by</span></code> = <code class="docutils literal notranslate"><span class="pre">tag</span></code>.</p></li>
<li><p><strong>repository</strong> (<em>str</em>) – Name of the repository to retrieve the release from.</p></li>
<li><p><strong>retrieve_by</strong> (<em>str</em>) – Describes how to fetch the release. Valid values are <code class="docutils literal notranslate"><span class="pre">id</span></code>, <code class="docutils literal notranslate"><span class="pre">tag</span></code>, <code class="docutils literal notranslate"><span class="pre">latest</span></code>.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_github.get_repositories">
<code class="sig-prename descclassname">pulumi_github.</code><code class="sig-name descname">get_repositories</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">query</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">sort</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_github.get_repositories" title="Permalink to this definition">¶</a></dt>
<dd><blockquote>
<div><dl class="simple">
<dt><strong>Note:</strong> The data source will return a maximum of <code class="docutils literal notranslate"><span class="pre">1000</span></code> repositories</dt><dd><p><a class="reference external" href="https://developer.github.com/v3/search/#about-the-search-api">as documented in official API docs</a>.</p>
</dd>
</dl>
</div></blockquote>
<p>Use this data source to retrieve a list of GitHub repositories using a search query.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_github</span> <span class="k">as</span> <span class="nn">github</span>

<span class="n">example</span> <span class="o">=</span> <span class="n">github</span><span class="o">.</span><span class="n">get_repositories</span><span class="p">(</span><span class="n">query</span><span class="o">=</span><span class="s2">&quot;org:hashicorp language:Go&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>query</strong> (<em>str</em>) – Search query. See <a class="reference external" href="https://help.github.com/articles/understanding-the-search-syntax/">documentation for the search syntax</a>.</p></li>
<li><p><strong>sort</strong> (<em>str</em>) – Sorts the repositories returned by the specified attribute. Valid values include <code class="docutils literal notranslate"><span class="pre">stars</span></code>, <code class="docutils literal notranslate"><span class="pre">fork</span></code>, and <code class="docutils literal notranslate"><span class="pre">updated</span></code>. Defaults to <code class="docutils literal notranslate"><span class="pre">updated</span></code>.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_github.get_repository">
<code class="sig-prename descclassname">pulumi_github.</code><code class="sig-name descname">get_repository</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">full_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_github.get_repository" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing resource.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>full_name</strong> (<em>str</em>) – Full name of the repository (in <code class="docutils literal notranslate"><span class="pre">org/name</span></code> format).</p></li>
<li><p><strong>name</strong> (<em>str</em>) – The name of the repository.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_github.get_team">
<code class="sig-prename descclassname">pulumi_github.</code><code class="sig-name descname">get_team</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">slug</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_github.get_team" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to retrieve information about a GitHub team.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_github</span> <span class="k">as</span> <span class="nn">github</span>

<span class="n">example</span> <span class="o">=</span> <span class="n">github</span><span class="o">.</span><span class="n">get_team</span><span class="p">(</span><span class="n">slug</span><span class="o">=</span><span class="s2">&quot;example&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>slug</strong> (<em>str</em>) – The team slug.</p>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_github.get_user">
<code class="sig-prename descclassname">pulumi_github.</code><code class="sig-name descname">get_user</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">username</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_github.get_user" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to retrieve information about a GitHub user.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_github</span> <span class="k">as</span> <span class="nn">github</span>

<span class="n">example</span> <span class="o">=</span> <span class="n">github</span><span class="o">.</span><span class="n">get_user</span><span class="p">(</span><span class="n">username</span><span class="o">=</span><span class="s2">&quot;example&quot;</span><span class="p">)</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>username</strong> (<em>str</em>) – The username.</p>
</dd>
</dl>
</dd></dl>

</div>
