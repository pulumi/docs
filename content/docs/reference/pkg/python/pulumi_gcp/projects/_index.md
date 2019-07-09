---
---

<div class="section" id="projects">
<h1>projects<a class="headerlink" href="#projects" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-gcp">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-gcp/issues">pulumi/pulumi-gcp repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-gcp/issues">terraform-providers/terraform-provider-gcp repo</a>.</div></blockquote>
<span class="target" id="module-pulumi_gcp.projects"></span><dl class="class">
<dt id="pulumi_gcp.projects.GetOrganizationPolicyResult">
<em class="property">class </em><code class="descclassname">pulumi_gcp.projects.</code><code class="descname">GetOrganizationPolicyResult</code><span class="sig-paren">(</span><em>boolean_policies=None</em>, <em>constraint=None</em>, <em>etag=None</em>, <em>list_policies=None</em>, <em>project=None</em>, <em>restore_policies=None</em>, <em>update_time=None</em>, <em>version=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.projects.GetOrganizationPolicyResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getOrganizationPolicy.</p>
<dl class="attribute">
<dt id="pulumi_gcp.projects.GetOrganizationPolicyResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.projects.GetOrganizationPolicyResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_gcp.projects.GetProjectResult">
<em class="property">class </em><code class="descclassname">pulumi_gcp.projects.</code><code class="descname">GetProjectResult</code><span class="sig-paren">(</span><em>filter=None</em>, <em>projects=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.projects.GetProjectResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getProject.</p>
<dl class="attribute">
<dt id="pulumi_gcp.projects.GetProjectResult.projects">
<code class="descname">projects</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.projects.GetProjectResult.projects" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of projects matching the provided filter. Structure is defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.projects.GetProjectResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.projects.GetProjectResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_gcp.projects.IAMAuditConfig">
<em class="property">class </em><code class="descclassname">pulumi_gcp.projects.</code><code class="descname">IAMAuditConfig</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>audit_log_configs=None</em>, <em>project=None</em>, <em>service=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.projects.IAMAuditConfig" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a IAMAuditConfig resource with the given unique name, props, and options.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="method">
<dt id="pulumi_gcp.projects.IAMAuditConfig.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.projects.IAMAuditConfig.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.projects.IAMAuditConfig.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.projects.IAMAuditConfig.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.projects.IAMBinding">
<em class="property">class </em><code class="descclassname">pulumi_gcp.projects.</code><code class="descname">IAMBinding</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>members=None</em>, <em>project=None</em>, <em>role=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.projects.IAMBinding" title="Permalink to this definition">¶</a></dt>
<dd><p>Three different resources help you manage your IAM policy for a project. Each of these resources serves a different use case:</p>
<ul class="simple">
<li><code class="docutils literal notranslate"><span class="pre">google_project_iam_policy</span></code>: Authoritative. Sets the IAM policy for the project and replaces any existing policy already attached.</li>
<li><code class="docutils literal notranslate"><span class="pre">google_project_iam_binding</span></code>: Authoritative for a given role. Updates the IAM policy to grant a role to a list of members. Other roles within the IAM policy for the project are preserved.</li>
<li><code class="docutils literal notranslate"><span class="pre">google_project_iam_member</span></code>: Non-authoritative. Updates the IAM policy to grant a role to a new member. Other members for the role for the project are preserved.</li>
</ul>
<blockquote>
<div><p><strong>Note:</strong> <code class="docutils literal notranslate"><span class="pre">google_project_iam_policy</span></code> <strong>cannot</strong> be used in conjunction with <code class="docutils literal notranslate"><span class="pre">google_project_iam_binding</span></code> and <code class="docutils literal notranslate"><span class="pre">google_project_iam_member</span></code> or they will fight over what your policy should be.</p>
<p><strong>Note:</strong> <code class="docutils literal notranslate"><span class="pre">google_project_iam_binding</span></code> resources <strong>can be</strong> used in conjunction with <code class="docutils literal notranslate"><span class="pre">google_project_iam_member</span></code> resources <strong>only if</strong> they do not grant privilege to the same role.</p>
</div></blockquote>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The project ID. If not specified for <code class="docutils literal notranslate"><span class="pre">google_project_iam_binding</span></code>
or <code class="docutils literal notranslate"><span class="pre">google_project_iam_member</span></code>, uses the ID of the project configured with the provider.
Required for <code class="docutils literal notranslate"><span class="pre">google_project_iam_policy</span></code> - you must explicitly set the project, and it
will not be inferred from the provider.</li>
<li><strong>role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The role that should be applied. Only one
<code class="docutils literal notranslate"><span class="pre">google_project_iam_binding</span></code> can be used per role. Note that custom roles must be of the format
<code class="docutils literal notranslate"><span class="pre">[projects|organizations]/{parent-name}/roles/{role-name}</span></code>.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/project_iam_binding.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/project_iam_binding.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_gcp.projects.IAMBinding.etag">
<code class="descname">etag</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.projects.IAMBinding.etag" title="Permalink to this definition">¶</a></dt>
<dd><p>(Computed) The etag of the project’s IAM policy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.projects.IAMBinding.project">
<code class="descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.projects.IAMBinding.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The project ID. If not specified for <code class="docutils literal notranslate"><span class="pre">google_project_iam_binding</span></code>
or <code class="docutils literal notranslate"><span class="pre">google_project_iam_member</span></code>, uses the ID of the project configured with the provider.
Required for <code class="docutils literal notranslate"><span class="pre">google_project_iam_policy</span></code> - you must explicitly set the project, and it
will not be inferred from the provider.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.projects.IAMBinding.role">
<code class="descname">role</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.projects.IAMBinding.role" title="Permalink to this definition">¶</a></dt>
<dd><p>The role that should be applied. Only one
<code class="docutils literal notranslate"><span class="pre">google_project_iam_binding</span></code> can be used per role. Note that custom roles must be of the format
<code class="docutils literal notranslate"><span class="pre">[projects|organizations]/{parent-name}/roles/{role-name}</span></code>.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.projects.IAMBinding.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.projects.IAMBinding.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.projects.IAMBinding.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.projects.IAMBinding.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.projects.IAMCustomRole">
<em class="property">class </em><code class="descclassname">pulumi_gcp.projects.</code><code class="descname">IAMCustomRole</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>description=None</em>, <em>permissions=None</em>, <em>project=None</em>, <em>role_id=None</em>, <em>stage=None</em>, <em>title=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.projects.IAMCustomRole" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a IAMCustomRole resource with the given unique name, props, and options.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A human-readable description for the role.</li>
<li><strong>permissions</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The names of the permissions this role grants when bound in an IAM policy. At least one permission must be specified.</li>
<li><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The project that the service account will be created in.
Defaults to the provider project configuration.</li>
<li><strong>role_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The role id to use for this role.</li>
<li><strong>stage</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The current launch stage of the role.
Defaults to <code class="docutils literal notranslate"><span class="pre">GA</span></code>.
List of possible stages is <a class="reference external" href="https://cloud.google.com/iam/reference/rest/v1/organizations.roles#Role.RoleLaunchStage">here</a>.</li>
<li><strong>title</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A human-readable title for the role.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/project_iam_custom_role.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/project_iam_custom_role.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_gcp.projects.IAMCustomRole.deleted">
<code class="descname">deleted</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.projects.IAMCustomRole.deleted" title="Permalink to this definition">¶</a></dt>
<dd><p>(Optional) The current deleted state of the role.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.projects.IAMCustomRole.description">
<code class="descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.projects.IAMCustomRole.description" title="Permalink to this definition">¶</a></dt>
<dd><p>A human-readable description for the role.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.projects.IAMCustomRole.permissions">
<code class="descname">permissions</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.projects.IAMCustomRole.permissions" title="Permalink to this definition">¶</a></dt>
<dd><p>The names of the permissions this role grants when bound in an IAM policy. At least one permission must be specified.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.projects.IAMCustomRole.project">
<code class="descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.projects.IAMCustomRole.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The project that the service account will be created in.
Defaults to the provider project configuration.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.projects.IAMCustomRole.role_id">
<code class="descname">role_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.projects.IAMCustomRole.role_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The role id to use for this role.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.projects.IAMCustomRole.stage">
<code class="descname">stage</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.projects.IAMCustomRole.stage" title="Permalink to this definition">¶</a></dt>
<dd><p>The current launch stage of the role.
Defaults to <code class="docutils literal notranslate"><span class="pre">GA</span></code>.
List of possible stages is <a class="reference external" href="https://cloud.google.com/iam/reference/rest/v1/organizations.roles#Role.RoleLaunchStage">here</a>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.projects.IAMCustomRole.title">
<code class="descname">title</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.projects.IAMCustomRole.title" title="Permalink to this definition">¶</a></dt>
<dd><p>A human-readable title for the role.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.projects.IAMCustomRole.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.projects.IAMCustomRole.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.projects.IAMCustomRole.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.projects.IAMCustomRole.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.projects.IAMMember">
<em class="property">class </em><code class="descclassname">pulumi_gcp.projects.</code><code class="descname">IAMMember</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>member=None</em>, <em>project=None</em>, <em>role=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.projects.IAMMember" title="Permalink to this definition">¶</a></dt>
<dd><p>Three different resources help you manage your IAM policy for a project. Each of these resources serves a different use case:</p>
<ul class="simple">
<li><code class="docutils literal notranslate"><span class="pre">google_project_iam_policy</span></code>: Authoritative. Sets the IAM policy for the project and replaces any existing policy already attached.</li>
<li><code class="docutils literal notranslate"><span class="pre">google_project_iam_binding</span></code>: Authoritative for a given role. Updates the IAM policy to grant a role to a list of members. Other roles within the IAM policy for the project are preserved.</li>
<li><code class="docutils literal notranslate"><span class="pre">google_project_iam_member</span></code>: Non-authoritative. Updates the IAM policy to grant a role to a new member. Other members for the role for the project are preserved.</li>
</ul>
<blockquote>
<div><p><strong>Note:</strong> <code class="docutils literal notranslate"><span class="pre">google_project_iam_policy</span></code> <strong>cannot</strong> be used in conjunction with <code class="docutils literal notranslate"><span class="pre">google_project_iam_binding</span></code> and <code class="docutils literal notranslate"><span class="pre">google_project_iam_member</span></code> or they will fight over what your policy should be.</p>
<p><strong>Note:</strong> <code class="docutils literal notranslate"><span class="pre">google_project_iam_binding</span></code> resources <strong>can be</strong> used in conjunction with <code class="docutils literal notranslate"><span class="pre">google_project_iam_member</span></code> resources <strong>only if</strong> they do not grant privilege to the same role.</p>
</div></blockquote>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The project ID. If not specified for <code class="docutils literal notranslate"><span class="pre">google_project_iam_binding</span></code>
or <code class="docutils literal notranslate"><span class="pre">google_project_iam_member</span></code>, uses the ID of the project configured with the provider.
Required for <code class="docutils literal notranslate"><span class="pre">google_project_iam_policy</span></code> - you must explicitly set the project, and it
will not be inferred from the provider.</li>
<li><strong>role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The role that should be applied. Only one
<code class="docutils literal notranslate"><span class="pre">google_project_iam_binding</span></code> can be used per role. Note that custom roles must be of the format
<code class="docutils literal notranslate"><span class="pre">[projects|organizations]/{parent-name}/roles/{role-name}</span></code>.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/project_iam_member.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/project_iam_member.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_gcp.projects.IAMMember.etag">
<code class="descname">etag</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.projects.IAMMember.etag" title="Permalink to this definition">¶</a></dt>
<dd><p>(Computed) The etag of the project’s IAM policy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.projects.IAMMember.project">
<code class="descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.projects.IAMMember.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The project ID. If not specified for <code class="docutils literal notranslate"><span class="pre">google_project_iam_binding</span></code>
or <code class="docutils literal notranslate"><span class="pre">google_project_iam_member</span></code>, uses the ID of the project configured with the provider.
Required for <code class="docutils literal notranslate"><span class="pre">google_project_iam_policy</span></code> - you must explicitly set the project, and it
will not be inferred from the provider.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.projects.IAMMember.role">
<code class="descname">role</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.projects.IAMMember.role" title="Permalink to this definition">¶</a></dt>
<dd><p>The role that should be applied. Only one
<code class="docutils literal notranslate"><span class="pre">google_project_iam_binding</span></code> can be used per role. Note that custom roles must be of the format
<code class="docutils literal notranslate"><span class="pre">[projects|organizations]/{parent-name}/roles/{role-name}</span></code>.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.projects.IAMMember.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.projects.IAMMember.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.projects.IAMMember.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.projects.IAMMember.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.projects.IAMPolicy">
<em class="property">class </em><code class="descclassname">pulumi_gcp.projects.</code><code class="descname">IAMPolicy</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>policy_data=None</em>, <em>project=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.projects.IAMPolicy" title="Permalink to this definition">¶</a></dt>
<dd><p>Three different resources help you manage your IAM policy for a project. Each of these resources serves a different use case:</p>
<ul class="simple">
<li><code class="docutils literal notranslate"><span class="pre">google_project_iam_policy</span></code>: Authoritative. Sets the IAM policy for the project and replaces any existing policy already attached.</li>
<li><code class="docutils literal notranslate"><span class="pre">google_project_iam_binding</span></code>: Authoritative for a given role. Updates the IAM policy to grant a role to a list of members. Other roles within the IAM policy for the project are preserved.</li>
<li><code class="docutils literal notranslate"><span class="pre">google_project_iam_member</span></code>: Non-authoritative. Updates the IAM policy to grant a role to a new member. Other members for the role for the project are preserved.</li>
</ul>
<blockquote>
<div><p><strong>Note:</strong> <code class="docutils literal notranslate"><span class="pre">google_project_iam_policy</span></code> <strong>cannot</strong> be used in conjunction with <code class="docutils literal notranslate"><span class="pre">google_project_iam_binding</span></code> and <code class="docutils literal notranslate"><span class="pre">google_project_iam_member</span></code> or they will fight over what your policy should be.</p>
<p><strong>Note:</strong> <code class="docutils literal notranslate"><span class="pre">google_project_iam_binding</span></code> resources <strong>can be</strong> used in conjunction with <code class="docutils literal notranslate"><span class="pre">google_project_iam_member</span></code> resources <strong>only if</strong> they do not grant privilege to the same role.</p>
</div></blockquote>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>policy_data</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The <code class="docutils literal notranslate"><span class="pre">google_iam_policy</span></code> data source that represents
the IAM policy that will be applied to the project. The policy will be
merged with any existing policy applied to the project.</li>
<li><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The project ID. If not specified for <code class="docutils literal notranslate"><span class="pre">google_project_iam_binding</span></code>
or <code class="docutils literal notranslate"><span class="pre">google_project_iam_member</span></code>, uses the ID of the project configured with the provider.
Required for <code class="docutils literal notranslate"><span class="pre">google_project_iam_policy</span></code> - you must explicitly set the project, and it
will not be inferred from the provider.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/project_iam_policy.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/project_iam_policy.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_gcp.projects.IAMPolicy.etag">
<code class="descname">etag</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.projects.IAMPolicy.etag" title="Permalink to this definition">¶</a></dt>
<dd><p>(Computed) The etag of the project’s IAM policy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.projects.IAMPolicy.policy_data">
<code class="descname">policy_data</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.projects.IAMPolicy.policy_data" title="Permalink to this definition">¶</a></dt>
<dd><p>The <code class="docutils literal notranslate"><span class="pre">google_iam_policy</span></code> data source that represents
the IAM policy that will be applied to the project. The policy will be
merged with any existing policy applied to the project.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.projects.IAMPolicy.project">
<code class="descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.projects.IAMPolicy.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The project ID. If not specified for <code class="docutils literal notranslate"><span class="pre">google_project_iam_binding</span></code>
or <code class="docutils literal notranslate"><span class="pre">google_project_iam_member</span></code>, uses the ID of the project configured with the provider.
Required for <code class="docutils literal notranslate"><span class="pre">google_project_iam_policy</span></code> - you must explicitly set the project, and it
will not be inferred from the provider.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.projects.IAMPolicy.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.projects.IAMPolicy.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.projects.IAMPolicy.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.projects.IAMPolicy.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.projects.OrganizationPolicy">
<em class="property">class </em><code class="descclassname">pulumi_gcp.projects.</code><code class="descname">OrganizationPolicy</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>boolean_policy=None</em>, <em>constraint=None</em>, <em>list_policy=None</em>, <em>project=None</em>, <em>restore_policy=None</em>, <em>version=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.projects.OrganizationPolicy" title="Permalink to this definition">¶</a></dt>
<dd><p>Allows management of Organization policies for a Google Project. For more information see
<a class="reference external" href="https://cloud.google.com/resource-manager/docs/organization-policy/overview">the official
documentation</a> and
<a class="reference external" href="https://cloud.google.com/resource-manager/reference/rest/v1/projects/setOrgPolicy">API</a>.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>boolean_policy</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A boolean policy is a constraint that is either enforced or not. Structure is documented below.</li>
<li><strong>constraint</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Constraint the Policy is configuring, for example, <code class="docutils literal notranslate"><span class="pre">serviceuser.services</span></code>. Check out the <a class="reference external" href="https://cloud.google.com/resource-manager/docs/organization-policy/understanding-constraints#available_constraints">complete list of available constraints</a>.</li>
<li><strong>list_policy</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A policy that can define specific values that are allowed or denied for the given constraint. It can also be used to allow or deny all values. Structure is documented below.</li>
<li><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The project id of the project to set the policy for.</li>
<li><strong>restore_policy</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A restore policy is a constraint to restore the default policy. Structure is documented below.</li>
<li><strong>version</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Version of the Policy. Default version is 0.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/project_organization_policy.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/project_organization_policy.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_gcp.projects.OrganizationPolicy.boolean_policy">
<code class="descname">boolean_policy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.projects.OrganizationPolicy.boolean_policy" title="Permalink to this definition">¶</a></dt>
<dd><p>A boolean policy is a constraint that is either enforced or not. Structure is documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.projects.OrganizationPolicy.constraint">
<code class="descname">constraint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.projects.OrganizationPolicy.constraint" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Constraint the Policy is configuring, for example, <code class="docutils literal notranslate"><span class="pre">serviceuser.services</span></code>. Check out the <a class="reference external" href="https://cloud.google.com/resource-manager/docs/organization-policy/understanding-constraints#available_constraints">complete list of available constraints</a>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.projects.OrganizationPolicy.etag">
<code class="descname">etag</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.projects.OrganizationPolicy.etag" title="Permalink to this definition">¶</a></dt>
<dd><p>(Computed) The etag of the organization policy. <code class="docutils literal notranslate"><span class="pre">etag</span></code> is used for optimistic concurrency control as a way to help prevent simultaneous updates of a policy from overwriting each other.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.projects.OrganizationPolicy.list_policy">
<code class="descname">list_policy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.projects.OrganizationPolicy.list_policy" title="Permalink to this definition">¶</a></dt>
<dd><p>A policy that can define specific values that are allowed or denied for the given constraint. It can also be used to allow or deny all values. Structure is documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.projects.OrganizationPolicy.project">
<code class="descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.projects.OrganizationPolicy.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The project id of the project to set the policy for.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.projects.OrganizationPolicy.restore_policy">
<code class="descname">restore_policy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.projects.OrganizationPolicy.restore_policy" title="Permalink to this definition">¶</a></dt>
<dd><p>A restore policy is a constraint to restore the default policy. Structure is documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.projects.OrganizationPolicy.update_time">
<code class="descname">update_time</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.projects.OrganizationPolicy.update_time" title="Permalink to this definition">¶</a></dt>
<dd><p>(Computed) The timestamp in RFC3339 UTC “Zulu” format, accurate to nanoseconds, representing when the variable was last updated. Example: “2016-10-09T12:33:37.578138407Z”.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.projects.OrganizationPolicy.version">
<code class="descname">version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.projects.OrganizationPolicy.version" title="Permalink to this definition">¶</a></dt>
<dd><p>Version of the Policy. Default version is 0.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.projects.OrganizationPolicy.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.projects.OrganizationPolicy.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.projects.OrganizationPolicy.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.projects.OrganizationPolicy.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.projects.Service">
<em class="property">class </em><code class="descclassname">pulumi_gcp.projects.</code><code class="descname">Service</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>disable_dependent_services=None</em>, <em>disable_on_destroy=None</em>, <em>project=None</em>, <em>service=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.projects.Service" title="Permalink to this definition">¶</a></dt>
<dd><p>Allows management of a single API service for an existing Google Cloud Platform project.</p>
<p>For a list of services available, visit the
<a class="reference external" href="https://console.cloud.google.com/apis/library">API library page</a> or run <code class="docutils literal notranslate"><span class="pre">gcloud</span> <span class="pre">services</span> <span class="pre">list</span></code>.</p>
<blockquote>
<div><dl class="docutils">
<dt><strong>Note:</strong> This resource <em>must not</em> be used in conjunction with</dt>
<dd><code class="docutils literal notranslate"><span class="pre">google_project_services</span></code> or they will fight over which services should be enabled.</dd>
</dl>
</div></blockquote>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>disable_dependent_services</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If <code class="docutils literal notranslate"><span class="pre">true</span></code>, services that are enabled and which depend on this service should also be disabled when this service is destroyed.
If <code class="docutils literal notranslate"><span class="pre">false</span></code> or unset, an error will be generated if any enabled services depend on this service when destroying it.</li>
<li><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The project ID. If not provided, the provider project is used.</li>
<li><strong>service</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The service to enable.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/project_service.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/project_service.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_gcp.projects.Service.disable_dependent_services">
<code class="descname">disable_dependent_services</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.projects.Service.disable_dependent_services" title="Permalink to this definition">¶</a></dt>
<dd><p>If <code class="docutils literal notranslate"><span class="pre">true</span></code>, services that are enabled and which depend on this service should also be disabled when this service is destroyed.
If <code class="docutils literal notranslate"><span class="pre">false</span></code> or unset, an error will be generated if any enabled services depend on this service when destroying it.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.projects.Service.project">
<code class="descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.projects.Service.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The project ID. If not provided, the provider project is used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.projects.Service.service">
<code class="descname">service</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.projects.Service.service" title="Permalink to this definition">¶</a></dt>
<dd><p>The service to enable.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.projects.Service.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.projects.Service.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.projects.Service.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.projects.Service.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.projects.Services">
<em class="property">class </em><code class="descclassname">pulumi_gcp.projects.</code><code class="descname">Services</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>disable_on_destroy=None</em>, <em>project=None</em>, <em>services=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.projects.Services" title="Permalink to this definition">¶</a></dt>
<dd><p>Allows management of enabled API services for an existing Google Cloud
Platform project. Services in an existing project that are not defined
in the config will be removed.</p>
<p>For a list of services available, visit the
<a class="reference external" href="https://console.cloud.google.com/apis/library">API library page</a> or run <code class="docutils literal notranslate"><span class="pre">gcloud</span> <span class="pre">services</span> <span class="pre">list</span></code>.</p>
<blockquote>
<div><dl class="docutils">
<dt><strong>Note:</strong> This resource attempts to be the authoritative source on <em>all</em> enabled APIs, which often</dt>
<dd>leads to conflicts when certain actions enable other APIs. If you do not need to ensure that
<em>exclusively</em> a particular set of APIs are enabled, you should most likely use the
google_project_service resource, one resource per API.</dd>
</dl>
</div></blockquote>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>services</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The list of services that are enabled. Supports
update.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/project_services.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/project_services.html.markdown</a>.</div></blockquote>
<dl class="attribute">
<dt id="pulumi_gcp.projects.Services.services">
<code class="descname">services</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.projects.Services.services" title="Permalink to this definition">¶</a></dt>
<dd><p>The list of services that are enabled. Supports
update.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.projects.Services.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.projects.Services.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.projects.Services.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.projects.Services.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.projects.UsageExportBucket">
<em class="property">class </em><code class="descclassname">pulumi_gcp.projects.</code><code class="descname">UsageExportBucket</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>bucket_name=None</em>, <em>prefix=None</em>, <em>project=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.projects.UsageExportBucket" title="Permalink to this definition">¶</a></dt>
<dd><p>Create a UsageExportBucket resource with the given unique name, props, and options.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/project_usage_export_bucket.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/project_usage_export_bucket.html.markdown</a>.</div></blockquote>
<dl class="method">
<dt id="pulumi_gcp.projects.UsageExportBucket.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.projects.UsageExportBucket.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.projects.UsageExportBucket.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.projects.UsageExportBucket.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.projects.get_organization_policy">
<code class="descclassname">pulumi_gcp.projects.</code><code class="descname">get_organization_policy</code><span class="sig-paren">(</span><em>constraint=None</em>, <em>project=None</em>, <em>opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.projects.get_organization_policy" title="Permalink to this definition">¶</a></dt>
<dd><p>Allows management of Organization policies for a Google Project. For more information see
<a class="reference external" href="https://cloud.google.com/resource-manager/docs/organization-policy/overview">the official
documentation</a></p>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/d/project_organization_policy.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/d/project_organization_policy.html.markdown</a>.</div></blockquote>
</dd></dl>

<dl class="function">
<dt id="pulumi_gcp.projects.get_project">
<code class="descclassname">pulumi_gcp.projects.</code><code class="descname">get_project</code><span class="sig-paren">(</span><em>filter=None</em>, <em>opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.projects.get_project" title="Permalink to this definition">¶</a></dt>
<dd><p>Retrieve information about a set of projects based on a filter. See the
<a class="reference external" href="https://cloud.google.com/resource-manager/reference/rest/v1/projects/list">REST API</a>
for more details.</p>
<blockquote>
<div>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/d/projects.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/d/projects.html.markdown</a>.</div></blockquote>
</dd></dl>

</div>
