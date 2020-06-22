---
title: Module identities
title_tag: Module identities | Package pulumi_azuredevops | Python SDK
linktitle: identities
notitle: true
block_external_search_index: true
---

{{< resource-docs-alert "azuredevops" >}}

<div class="section" id="identities">
<h1>identities<a class="headerlink" href="#identities" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azuredevops">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-azuredevops/issues">pulumi/pulumi-azuredevops repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-azuredevops/issues">terraform-providers/terraform-provider-azuredevops repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_azuredevops.identities"></span><dl class="py class">
<dt id="pulumi_azuredevops.identities.AwaitableGetGroupResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azuredevops.identities.</code><code class="sig-name descname">AwaitableGetGroupResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">descriptor</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuredevops.identities.AwaitableGetGroupResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_azuredevops.identities.AwaitableGetUsersResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azuredevops.identities.</code><code class="sig-name descname">AwaitableGetUsersResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">origin</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">origin_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">principal_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">subject_types</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">users</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuredevops.identities.AwaitableGetUsersResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="py class">
<dt id="pulumi_azuredevops.identities.GetGroupResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azuredevops.identities.</code><code class="sig-name descname">GetGroupResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">descriptor</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuredevops.identities.GetGroupResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getGroup.</p>
<dl class="py attribute">
<dt id="pulumi_azuredevops.identities.GetGroupResult.descriptor">
<code class="sig-name descname">descriptor</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuredevops.identities.GetGroupResult.descriptor" title="Permalink to this definition">¶</a></dt>
<dd><p>The Descriptor is the primary way to reference the graph subject. This field will uniquely identify the same graph subject across both Accounts and Organizations.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azuredevops.identities.GetGroupResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuredevops.identities.GetGroupResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_azuredevops.identities.GetUsersResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azuredevops.identities.</code><code class="sig-name descname">GetUsersResult</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">origin</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">origin_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">principal_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">subject_types</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">users</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuredevops.identities.GetUsersResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getUsers.</p>
<dl class="py attribute">
<dt id="pulumi_azuredevops.identities.GetUsersResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuredevops.identities.GetUsersResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>The provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="py class">
<dt id="pulumi_azuredevops.identities.Group">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azuredevops.identities.</code><code class="sig-name descname">Group</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">display_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">mail</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">members</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">origin_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">scope</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuredevops.identities.Group" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages a group within Azure DevOps.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_azuredevops</span> <span class="k">as</span> <span class="nn">azuredevops</span>

<span class="n">project</span> <span class="o">=</span> <span class="n">azuredevops</span><span class="o">.</span><span class="n">core</span><span class="o">.</span><span class="n">Project</span><span class="p">(</span><span class="s2">&quot;project&quot;</span><span class="p">,</span> <span class="n">project_name</span><span class="o">=</span><span class="s2">&quot;Test Project&quot;</span><span class="p">)</span>
<span class="n">tf_project_readers</span> <span class="o">=</span> <span class="n">project</span><span class="o">.</span><span class="n">id</span><span class="o">.</span><span class="n">apply</span><span class="p">(</span><span class="k">lambda</span> <span class="nb">id</span><span class="p">:</span> <span class="n">azuredevops</span><span class="o">.</span><span class="n">Identities</span><span class="o">.</span><span class="n">get_group</span><span class="p">(</span><span class="n">project_id</span><span class="o">=</span><span class="nb">id</span><span class="p">,</span>
    <span class="n">name</span><span class="o">=</span><span class="s2">&quot;Readers&quot;</span><span class="p">))</span>
<span class="n">tf_project_contributors</span> <span class="o">=</span> <span class="n">project</span><span class="o">.</span><span class="n">id</span><span class="o">.</span><span class="n">apply</span><span class="p">(</span><span class="k">lambda</span> <span class="nb">id</span><span class="p">:</span> <span class="n">azuredevops</span><span class="o">.</span><span class="n">Identities</span><span class="o">.</span><span class="n">get_group</span><span class="p">(</span><span class="n">project_id</span><span class="o">=</span><span class="nb">id</span><span class="p">,</span>
    <span class="n">name</span><span class="o">=</span><span class="s2">&quot;Contributors&quot;</span><span class="p">))</span>
<span class="n">group</span> <span class="o">=</span> <span class="n">azuredevops</span><span class="o">.</span><span class="n">identities</span><span class="o">.</span><span class="n">Group</span><span class="p">(</span><span class="s2">&quot;group&quot;</span><span class="p">,</span>
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
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Description of the Project.</p></li>
<li><p><strong>display_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of a new Azure DevOps group that is not backed by an external provider. The <code class="docutils literal notranslate"><span class="pre">origin_id</span></code> and <code class="docutils literal notranslate"><span class="pre">mail</span></code> arguments cannot be used simultaneously with <code class="docutils literal notranslate"><span class="pre">display_name</span></code>.</p></li>
<li><p><strong>mail</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The mail address as a reference to an existing group from an external AD or AAD backed provider. The <code class="docutils literal notranslate"><span class="pre">scope</span></code>, <code class="docutils literal notranslate"><span class="pre">origin_id</span></code> and <code class="docutils literal notranslate"><span class="pre">display_name</span></code> arguments cannot be used simultaneously with <code class="docutils literal notranslate"><span class="pre">mail</span></code>.</p></li>
<li><p><strong>members</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – &gt; NOTE: It’s possible to define group members both within the <code class="docutils literal notranslate"><span class="pre">Identities.Group</span></code> resource via the members block and by using the   <code class="docutils literal notranslate"><span class="pre">Identities.GroupMembership</span></code> resource. However it’s not possible to use both methods to manage group members, since there’ll be conflicts.</p></li>
<li><p><strong>origin_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The OriginID as a reference to a group from an external AD or AAD backed provider. The <code class="docutils literal notranslate"><span class="pre">scope</span></code>, <code class="docutils literal notranslate"><span class="pre">mail</span></code> and <code class="docutils literal notranslate"><span class="pre">display_name</span></code> arguments cannot be used simultaneously with <code class="docutils literal notranslate"><span class="pre">origin_id</span></code>.</p></li>
<li><p><strong>scope</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The scope of the group. A descriptor referencing the scope (collection, project) in which the group should be created. If omitted, will be created in the scope of the enclosing account or organization.x</p></li>
</ul>
</dd>
</dl>
<dl class="py attribute">
<dt id="pulumi_azuredevops.identities.Group.description">
<code class="sig-name descname">description</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuredevops.identities.Group.description" title="Permalink to this definition">¶</a></dt>
<dd><p>The Description of the Project.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azuredevops.identities.Group.descriptor">
<code class="sig-name descname">descriptor</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuredevops.identities.Group.descriptor" title="Permalink to this definition">¶</a></dt>
<dd><p>The identity (subject) descriptor of the Group.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azuredevops.identities.Group.display_name">
<code class="sig-name descname">display_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuredevops.identities.Group.display_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of a new Azure DevOps group that is not backed by an external provider. The <code class="docutils literal notranslate"><span class="pre">origin_id</span></code> and <code class="docutils literal notranslate"><span class="pre">mail</span></code> arguments cannot be used simultaneously with <code class="docutils literal notranslate"><span class="pre">display_name</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azuredevops.identities.Group.domain">
<code class="sig-name descname">domain</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuredevops.identities.Group.domain" title="Permalink to this definition">¶</a></dt>
<dd><p>This represents the name of the container of origin for a graph member.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azuredevops.identities.Group.mail">
<code class="sig-name descname">mail</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuredevops.identities.Group.mail" title="Permalink to this definition">¶</a></dt>
<dd><p>The mail address as a reference to an existing group from an external AD or AAD backed provider. The <code class="docutils literal notranslate"><span class="pre">scope</span></code>, <code class="docutils literal notranslate"><span class="pre">origin_id</span></code> and <code class="docutils literal notranslate"><span class="pre">display_name</span></code> arguments cannot be used simultaneously with <code class="docutils literal notranslate"><span class="pre">mail</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azuredevops.identities.Group.members">
<code class="sig-name descname">members</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuredevops.identities.Group.members" title="Permalink to this definition">¶</a></dt>
<dd><blockquote>
<div><p>NOTE: It’s possible to define group members both within the <code class="docutils literal notranslate"><span class="pre">Identities.Group</span></code> resource via the members block and by using the   <code class="docutils literal notranslate"><span class="pre">Identities.GroupMembership</span></code> resource. However it’s not possible to use both methods to manage group members, since there’ll be conflicts.</p>
</div></blockquote>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azuredevops.identities.Group.origin">
<code class="sig-name descname">origin</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuredevops.identities.Group.origin" title="Permalink to this definition">¶</a></dt>
<dd><p>The type of source provider for the origin identifier (ex:AD, AAD, MSA)</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azuredevops.identities.Group.origin_id">
<code class="sig-name descname">origin_id</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuredevops.identities.Group.origin_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The OriginID as a reference to a group from an external AD or AAD backed provider. The <code class="docutils literal notranslate"><span class="pre">scope</span></code>, <code class="docutils literal notranslate"><span class="pre">mail</span></code> and <code class="docutils literal notranslate"><span class="pre">display_name</span></code> arguments cannot be used simultaneously with <code class="docutils literal notranslate"><span class="pre">origin_id</span></code>.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azuredevops.identities.Group.principal_name">
<code class="sig-name descname">principal_name</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuredevops.identities.Group.principal_name" title="Permalink to this definition">¶</a></dt>
<dd><p>This is the PrincipalName of this graph member from the source provider.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azuredevops.identities.Group.scope">
<code class="sig-name descname">scope</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuredevops.identities.Group.scope" title="Permalink to this definition">¶</a></dt>
<dd><p>The scope of the group. A descriptor referencing the scope (collection, project) in which the group should be created. If omitted, will be created in the scope of the enclosing account or organization.x</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azuredevops.identities.Group.subject_kind">
<code class="sig-name descname">subject_kind</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuredevops.identities.Group.subject_kind" title="Permalink to this definition">¶</a></dt>
<dd><p>This field identifies the type of the graph subject (ex: Group, Scope, User).</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azuredevops.identities.Group.url">
<code class="sig-name descname">url</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuredevops.identities.Group.url" title="Permalink to this definition">¶</a></dt>
<dd><p>This url is the full route to the source resource of this graph subject.</p>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.identities.Group.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">description</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">descriptor</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">display_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">domain</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">mail</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">members</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">origin</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">origin_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">principal_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">scope</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">subject_kind</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">url</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuredevops.identities.Group.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Group resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Description of the Project.</p></li>
<li><p><strong>descriptor</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The identity (subject) descriptor of the Group.</p></li>
<li><p><strong>display_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of a new Azure DevOps group that is not backed by an external provider. The <code class="docutils literal notranslate"><span class="pre">origin_id</span></code> and <code class="docutils literal notranslate"><span class="pre">mail</span></code> arguments cannot be used simultaneously with <code class="docutils literal notranslate"><span class="pre">display_name</span></code>.</p></li>
<li><p><strong>domain</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – This represents the name of the container of origin for a graph member.</p></li>
<li><p><strong>mail</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The mail address as a reference to an existing group from an external AD or AAD backed provider. The <code class="docutils literal notranslate"><span class="pre">scope</span></code>, <code class="docutils literal notranslate"><span class="pre">origin_id</span></code> and <code class="docutils literal notranslate"><span class="pre">display_name</span></code> arguments cannot be used simultaneously with <code class="docutils literal notranslate"><span class="pre">mail</span></code>.</p></li>
<li><p><strong>members</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – &gt; NOTE: It’s possible to define group members both within the <code class="docutils literal notranslate"><span class="pre">Identities.Group</span></code> resource via the members block and by using the   <code class="docutils literal notranslate"><span class="pre">Identities.GroupMembership</span></code> resource. However it’s not possible to use both methods to manage group members, since there’ll be conflicts.</p></li>
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
<dt id="pulumi_azuredevops.identities.Group.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuredevops.identities.Group.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azuredevops.identities.Group.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuredevops.identities.Group.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azuredevops.identities.GroupMembership">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_azuredevops.identities.</code><code class="sig-name descname">GroupMembership</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">group</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">members</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">mode</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__props__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__name__</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">__opts__</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuredevops.identities.GroupMembership" title="Permalink to this definition">¶</a></dt>
<dd><p>Manages group membership within Azure DevOps.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_azuredevops</span> <span class="k">as</span> <span class="nn">azuredevops</span>

<span class="n">project</span> <span class="o">=</span> <span class="n">azuredevops</span><span class="o">.</span><span class="n">core</span><span class="o">.</span><span class="n">Project</span><span class="p">(</span><span class="s2">&quot;project&quot;</span><span class="p">,</span> <span class="n">project_name</span><span class="o">=</span><span class="s2">&quot;Test Project&quot;</span><span class="p">)</span>
<span class="n">user</span> <span class="o">=</span> <span class="n">azuredevops</span><span class="o">.</span><span class="n">entitlement</span><span class="o">.</span><span class="n">User</span><span class="p">(</span><span class="s2">&quot;user&quot;</span><span class="p">,</span> <span class="n">principal_name</span><span class="o">=</span><span class="s2">&quot;foo@contoso.com&quot;</span><span class="p">)</span>
<span class="n">group</span> <span class="o">=</span> <span class="n">project</span><span class="o">.</span><span class="n">id</span><span class="o">.</span><span class="n">apply</span><span class="p">(</span><span class="k">lambda</span> <span class="nb">id</span><span class="p">:</span> <span class="n">azuredevops</span><span class="o">.</span><span class="n">Identities</span><span class="o">.</span><span class="n">get_group</span><span class="p">(</span><span class="n">project_id</span><span class="o">=</span><span class="nb">id</span><span class="p">,</span>
    <span class="n">name</span><span class="o">=</span><span class="s2">&quot;Build Administrators&quot;</span><span class="p">))</span>
<span class="n">membership</span> <span class="o">=</span> <span class="n">azuredevops</span><span class="o">.</span><span class="n">identities</span><span class="o">.</span><span class="n">GroupMembership</span><span class="p">(</span><span class="s2">&quot;membership&quot;</span><span class="p">,</span>
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
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>group</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The descriptor of the group being managed.</p></li>
<li><p><strong>members</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of user or group descriptors that will become members of the group.</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="o">&gt;</span> <span class="n">NOTE</span><span class="p">:</span> <span class="n">It</span><span class="s1">&#39;s possible to define group members both within the `Identities.GroupMembership resource` via the members block and by using the `Identities.Group` resource. However it&#39;</span><span class="n">s</span> <span class="ow">not</span> <span class="n">possible</span> <span class="n">to</span> <span class="n">use</span> <span class="n">both</span> <span class="n">methods</span> <span class="n">to</span> <span class="n">manage</span> <span class="n">group</span> <span class="n">members</span><span class="p">,</span> <span class="n">since</span> <span class="n">there</span><span class="s1">&#39;ll be conflicts.</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>mode</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The mode how the resource manages group members.</p>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>* `mode == add`: the resource will ensure that all specified members will be part of the referenced group
* `mode == overwrite`: the resource will replace all existing members with the members specified within the `members` block
&gt; NOTE: To clear all members from a group, specify an empty list of descriptors in the `members` attribute and set the `mode` member to `overwrite`.
</pre></div>
</div>
<dl class="py attribute">
<dt id="pulumi_azuredevops.identities.GroupMembership.group">
<code class="sig-name descname">group</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuredevops.identities.GroupMembership.group" title="Permalink to this definition">¶</a></dt>
<dd><p>The descriptor of the group being managed.</p>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azuredevops.identities.GroupMembership.members">
<code class="sig-name descname">members</code><em class="property">: pulumi.Output[list]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuredevops.identities.GroupMembership.members" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of user or group descriptors that will become members of the group.</p>
<blockquote>
<div><p>NOTE: It’s possible to define group members both within the <code class="docutils literal notranslate"><span class="pre">Identities.GroupMembership</span> <span class="pre">resource</span></code> via the members block and by using the <code class="docutils literal notranslate"><span class="pre">Identities.Group</span></code> resource. However it’s not possible to use both methods to manage group members, since there’ll be conflicts.</p>
</div></blockquote>
</dd></dl>

<dl class="py attribute">
<dt id="pulumi_azuredevops.identities.GroupMembership.mode">
<code class="sig-name descname">mode</code><em class="property">: pulumi.Output[str]</em><em class="property"> = None</em><a class="headerlink" href="#pulumi_azuredevops.identities.GroupMembership.mode" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azuredevops.identities.GroupMembership.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">resource_name</span></em>, <em class="sig-param"><span class="n">id</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">group</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">members</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">mode</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuredevops.identities.GroupMembership.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing GroupMembership resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>group</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The descriptor of the group being managed.</p></li>
<li><p><strong>members</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – A list of user or group descriptors that will become members of the group.</p></li>
</ul>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="o">&gt;</span> <span class="n">NOTE</span><span class="p">:</span> <span class="n">It</span><span class="s1">&#39;s possible to define group members both within the `Identities.GroupMembership resource` via the members block and by using the `Identities.Group` resource. However it&#39;</span><span class="n">s</span> <span class="ow">not</span> <span class="n">possible</span> <span class="n">to</span> <span class="n">use</span> <span class="n">both</span> <span class="n">methods</span> <span class="n">to</span> <span class="n">manage</span> <span class="n">group</span> <span class="n">members</span><span class="p">,</span> <span class="n">since</span> <span class="n">there</span><span class="s1">&#39;ll be conflicts.</span>
</pre></div>
</div>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>mode</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The mode how the resource manages group members.</p>
</dd>
</dl>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>* `mode == add`: the resource will ensure that all specified members will be part of the referenced group
* `mode == overwrite`: the resource will replace all existing members with the members specified within the `members` block
&gt; NOTE: To clear all members from a group, specify an empty list of descriptors in the `members` attribute and set the `mode` member to `overwrite`.
</pre></div>
</div>
</dd></dl>

<dl class="py method">
<dt id="pulumi_azuredevops.identities.GroupMembership.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuredevops.identities.GroupMembership.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azuredevops.identities.GroupMembership.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">prop</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuredevops.identities.GroupMembership.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_azuredevops.identities.get_group">
<code class="sig-prename descclassname">pulumi_azuredevops.identities.</code><code class="sig-name descname">get_group</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">project_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuredevops.identities.get_group" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing Group within Azure DevOps</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_azuredevops</span> <span class="k">as</span> <span class="nn">azuredevops</span>

<span class="n">project</span> <span class="o">=</span> <span class="n">azuredevops</span><span class="o">.</span><span class="n">Core</span><span class="o">.</span><span class="n">get_project</span><span class="p">(</span><span class="n">project_name</span><span class="o">=</span><span class="s2">&quot;contoso-project&quot;</span><span class="p">)</span>
<span class="n">test</span> <span class="o">=</span> <span class="n">azuredevops</span><span class="o">.</span><span class="n">Identities</span><span class="o">.</span><span class="n">get_group</span><span class="p">(</span><span class="n">project_id</span><span class="o">=</span><span class="n">project</span><span class="o">.</span><span class="n">id</span><span class="p">,</span>
    <span class="n">name</span><span class="o">=</span><span class="s2">&quot;Test Group&quot;</span><span class="p">)</span>
<span class="n">pulumi</span><span class="o">.</span><span class="n">export</span><span class="p">(</span><span class="s2">&quot;groupId&quot;</span><span class="p">,</span> <span class="n">test</span><span class="o">.</span><span class="n">id</span><span class="p">)</span>
<span class="n">pulumi</span><span class="o">.</span><span class="n">export</span><span class="p">(</span><span class="s2">&quot;groupDescriptor&quot;</span><span class="p">,</span> <span class="n">test</span><span class="o">.</span><span class="n">descriptor</span><span class="p">)</span>
</pre></div>
</div>
<ul class="simple">
<li><p><a class="reference external" href="https://docs.microsoft.com/en-us/rest/api/azure/devops/graph/groups/get?view=azure-devops-rest-5.1">Azure DevOps Service REST API 5.1 - Groups - Get</a></p></li>
</ul>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>name</strong> (<em>str</em>) – The Group Name.</p></li>
<li><p><strong>project_id</strong> (<em>str</em>) – The Project Id.</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<dl class="py function">
<dt id="pulumi_azuredevops.identities.get_users">
<code class="sig-prename descclassname">pulumi_azuredevops.identities.</code><code class="sig-name descname">get_users</code><span class="sig-paren">(</span><em class="sig-param"><span class="n">origin</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">origin_id</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">principal_name</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">subject_types</span><span class="o">=</span><span class="default_value">None</span></em>, <em class="sig-param"><span class="n">opts</span><span class="o">=</span><span class="default_value">None</span></em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_azuredevops.identities.get_users" title="Permalink to this definition">¶</a></dt>
<dd><p>Use this data source to access information about an existing users within Azure DevOps.</p>
<div class="highlight-python notranslate"><div class="highlight"><pre><span></span><span class="kn">import</span> <span class="nn">pulumi</span>
<span class="kn">import</span> <span class="nn">pulumi_azuredevops</span> <span class="k">as</span> <span class="nn">azuredevops</span>

<span class="n">user</span> <span class="o">=</span> <span class="n">azuredevops</span><span class="o">.</span><span class="n">Identities</span><span class="o">.</span><span class="n">get_users</span><span class="p">(</span><span class="n">principal_name</span><span class="o">=</span><span class="s2">&quot;contoso-user@contoso.onmicrosoft.com&quot;</span><span class="p">)</span>
<span class="n">all_users</span> <span class="o">=</span> <span class="n">azuredevops</span><span class="o">.</span><span class="n">Identities</span><span class="o">.</span><span class="n">get_users</span><span class="p">()</span>
<span class="n">all_from_origin</span> <span class="o">=</span> <span class="n">azuredevops</span><span class="o">.</span><span class="n">Identities</span><span class="o">.</span><span class="n">get_users</span><span class="p">(</span><span class="n">origin</span><span class="o">=</span><span class="s2">&quot;aad&quot;</span><span class="p">)</span>
<span class="n">all_from_subject_types</span> <span class="o">=</span> <span class="n">azuredevops</span><span class="o">.</span><span class="n">Identities</span><span class="o">.</span><span class="n">get_users</span><span class="p">(</span><span class="n">subject_types</span><span class="o">=</span><span class="p">[</span>
    <span class="s2">&quot;aad&quot;</span><span class="p">,</span>
    <span class="s2">&quot;msa&quot;</span><span class="p">,</span>
<span class="p">])</span>
<span class="n">all_from_origin_id</span> <span class="o">=</span> <span class="n">azuredevops</span><span class="o">.</span><span class="n">Identities</span><span class="o">.</span><span class="n">get_users</span><span class="p">(</span><span class="n">origin</span><span class="o">=</span><span class="s2">&quot;aad&quot;</span><span class="p">,</span>
    <span class="n">origin_id</span><span class="o">=</span><span class="s2">&quot;a7ead982-8438-4cd2-b9e3-c3aa51a7b675&quot;</span><span class="p">)</span>
</pre></div>
</div>
<ul class="simple">
<li><p><a class="reference external" href="https://docs.microsoft.com/en-us/rest/api/azure/devops/graph/users?view=azure-devops-rest-5.1">Azure DevOps Service REST API 5.1 - Graph Users API</a></p></li>
</ul>
</dd></dl>

</div>
