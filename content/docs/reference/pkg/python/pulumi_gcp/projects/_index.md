---
title: Module projects
title_tag: Module projects | Package pulumi_gcp | Python SDK
linktitle: projects
notitle: true
---

<div class="section" id="projects">
<h1>projects<a class="headerlink" href="#projects" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-gcp/issues">pulumi/pulumi-gcp repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/issues">terraform-providers/terraform-provider-google repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_gcp.projects"></span><dl class="class">
<dt id="pulumi_gcp.projects.AwaitableGetOrganizationPolicyResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.projects.</code><code class="sig-name descname">AwaitableGetOrganizationPolicyResult</code><span class="sig-paren">(</span><em class="sig-param">boolean_policies=None</em>, <em class="sig-param">constraint=None</em>, <em class="sig-param">etag=None</em>, <em class="sig-param">list_policies=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">restore_policies=None</em>, <em class="sig-param">update_time=None</em>, <em class="sig-param">version=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.projects.AwaitableGetOrganizationPolicyResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_gcp.projects.AwaitableGetProjectResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.projects.</code><code class="sig-name descname">AwaitableGetProjectResult</code><span class="sig-paren">(</span><em class="sig-param">filter=None</em>, <em class="sig-param">projects=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.projects.AwaitableGetProjectResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_gcp.projects.GetOrganizationPolicyResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.projects.</code><code class="sig-name descname">GetOrganizationPolicyResult</code><span class="sig-paren">(</span><em class="sig-param">boolean_policies=None</em>, <em class="sig-param">constraint=None</em>, <em class="sig-param">etag=None</em>, <em class="sig-param">list_policies=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">restore_policies=None</em>, <em class="sig-param">update_time=None</em>, <em class="sig-param">version=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.projects.GetOrganizationPolicyResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getOrganizationPolicy.</p>
<dl class="attribute">
<dt id="pulumi_gcp.projects.GetOrganizationPolicyResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.projects.GetOrganizationPolicyResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_gcp.projects.GetProjectResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.projects.</code><code class="sig-name descname">GetProjectResult</code><span class="sig-paren">(</span><em class="sig-param">filter=None</em>, <em class="sig-param">projects=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.projects.GetProjectResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getProject.</p>
<dl class="attribute">
<dt id="pulumi_gcp.projects.GetProjectResult.projects">
<code class="sig-name descname">projects</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.projects.GetProjectResult.projects" title="Permalink to this definition">¶</a></dt>
<dd><p>A list of projects matching the provided filter. Structure is defined below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.projects.GetProjectResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.projects.GetProjectResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_gcp.projects.IAMAuditConfig">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.projects.</code><code class="sig-name descname">IAMAuditConfig</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">audit_log_configs=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">service=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.projects.IAMAuditConfig" title="Permalink to this definition">¶</a></dt>
<dd><p>Four different resources help you manage your IAM policy for a project. Each of these resources serves a different use case:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">projects.IAMPolicy</span></code>: Authoritative. Sets the IAM policy for the project and replaces any existing policy already attached.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">projects.IAMBinding</span></code>: Authoritative for a given role. Updates the IAM policy to grant a role to a list of members. Other roles within the IAM policy for the project are preserved.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">projects.IAMMember</span></code>: Non-authoritative. Updates the IAM policy to grant a role to a new member. Other members for the role for the project are preserved.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">projects.IAMAuditConfig</span></code>: Authoritative for a given service. Updates the IAM policy to enable audit logging for the given service.</p></li>
</ul>
<blockquote>
<div><p><strong>Note:</strong> <code class="docutils literal notranslate"><span class="pre">projects.IAMPolicy</span></code> <strong>cannot</strong> be used in conjunction with <code class="docutils literal notranslate"><span class="pre">projects.IAMBinding</span></code>, <code class="docutils literal notranslate"><span class="pre">projects.IAMMember</span></code>, or <code class="docutils literal notranslate"><span class="pre">projects.IAMAuditConfig</span></code> or they will fight over what your policy should be.</p>
<p><strong>Note:</strong> <code class="docutils literal notranslate"><span class="pre">projects.IAMBinding</span></code> resources <strong>can be</strong> used in conjunction with <code class="docutils literal notranslate"><span class="pre">projects.IAMMember</span></code> resources <strong>only if</strong> they do not grant privilege to the same role.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>audit_log_configs</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The configuration for logging of each type of permission.  This can be specified multiple times.  Structure is documented below.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The project ID. If not specified for <code class="docutils literal notranslate"><span class="pre">projects.IAMBinding</span></code>, <code class="docutils literal notranslate"><span class="pre">projects.IAMMember</span></code>, or <code class="docutils literal notranslate"><span class="pre">projects.IAMAuditConfig</span></code>, uses the ID of the project configured with the provider.
Required for <code class="docutils literal notranslate"><span class="pre">projects.IAMPolicy</span></code> - you must explicitly set the project, and it
will not be inferred from the provider.</p></li>
<li><p><strong>service</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Service which will be enabled for audit logging.  The special value <code class="docutils literal notranslate"><span class="pre">allServices</span></code> covers all services.  Note that if there are google_project_iam_audit_config resources covering both <code class="docutils literal notranslate"><span class="pre">allServices</span></code> and a specific service then the union of the two AuditConfigs is used for that service: the <code class="docutils literal notranslate"><span class="pre">log_types</span></code> specified in each <code class="docutils literal notranslate"><span class="pre">audit_log_config</span></code> are enabled, and the <code class="docutils literal notranslate"><span class="pre">exempted_members</span></code> in each <code class="docutils literal notranslate"><span class="pre">audit_log_config</span></code> are exempted.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>audit_log_configs</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">exemptedMembers</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">logType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/project_iam_audit_config.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/project_iam_audit_config.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_gcp.projects.IAMAuditConfig.audit_log_configs">
<code class="sig-name descname">audit_log_configs</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.projects.IAMAuditConfig.audit_log_configs" title="Permalink to this definition">¶</a></dt>
<dd><p>The configuration for logging of each type of permission.  This can be specified multiple times.  Structure is documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">exemptedMembers</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">logType</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.projects.IAMAuditConfig.etag">
<code class="sig-name descname">etag</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.projects.IAMAuditConfig.etag" title="Permalink to this definition">¶</a></dt>
<dd><p>(Computed) The etag of the project’s IAM policy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.projects.IAMAuditConfig.project">
<code class="sig-name descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.projects.IAMAuditConfig.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The project ID. If not specified for <code class="docutils literal notranslate"><span class="pre">projects.IAMBinding</span></code>, <code class="docutils literal notranslate"><span class="pre">projects.IAMMember</span></code>, or <code class="docutils literal notranslate"><span class="pre">projects.IAMAuditConfig</span></code>, uses the ID of the project configured with the provider.
Required for <code class="docutils literal notranslate"><span class="pre">projects.IAMPolicy</span></code> - you must explicitly set the project, and it
will not be inferred from the provider.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.projects.IAMAuditConfig.service">
<code class="sig-name descname">service</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.projects.IAMAuditConfig.service" title="Permalink to this definition">¶</a></dt>
<dd><p>Service which will be enabled for audit logging.  The special value <code class="docutils literal notranslate"><span class="pre">allServices</span></code> covers all services.  Note that if there are google_project_iam_audit_config resources covering both <code class="docutils literal notranslate"><span class="pre">allServices</span></code> and a specific service then the union of the two AuditConfigs is used for that service: the <code class="docutils literal notranslate"><span class="pre">log_types</span></code> specified in each <code class="docutils literal notranslate"><span class="pre">audit_log_config</span></code> are enabled, and the <code class="docutils literal notranslate"><span class="pre">exempted_members</span></code> in each <code class="docutils literal notranslate"><span class="pre">audit_log_config</span></code> are exempted.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.projects.IAMAuditConfig.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">audit_log_configs=None</em>, <em class="sig-param">etag=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">service=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.projects.IAMAuditConfig.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing IAMAuditConfig resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>audit_log_configs</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The configuration for logging of each type of permission.  This can be specified multiple times.  Structure is documented below.</p></li>
<li><p><strong>etag</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – (Computed) The etag of the project’s IAM policy.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The project ID. If not specified for <code class="docutils literal notranslate"><span class="pre">projects.IAMBinding</span></code>, <code class="docutils literal notranslate"><span class="pre">projects.IAMMember</span></code>, or <code class="docutils literal notranslate"><span class="pre">projects.IAMAuditConfig</span></code>, uses the ID of the project configured with the provider.
Required for <code class="docutils literal notranslate"><span class="pre">projects.IAMPolicy</span></code> - you must explicitly set the project, and it
will not be inferred from the provider.</p></li>
<li><p><strong>service</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – Service which will be enabled for audit logging.  The special value <code class="docutils literal notranslate"><span class="pre">allServices</span></code> covers all services.  Note that if there are google_project_iam_audit_config resources covering both <code class="docutils literal notranslate"><span class="pre">allServices</span></code> and a specific service then the union of the two AuditConfigs is used for that service: the <code class="docutils literal notranslate"><span class="pre">log_types</span></code> specified in each <code class="docutils literal notranslate"><span class="pre">audit_log_config</span></code> are enabled, and the <code class="docutils literal notranslate"><span class="pre">exempted_members</span></code> in each <code class="docutils literal notranslate"><span class="pre">audit_log_config</span></code> are exempted.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>audit_log_configs</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">exemptedMembers</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">logType</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/project_iam_audit_config.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/project_iam_audit_config.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.projects.IAMAuditConfig.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.projects.IAMAuditConfig.translate_output_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="method">
<dt id="pulumi_gcp.projects.IAMAuditConfig.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.projects.IAMAuditConfig.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="class">
<dt id="pulumi_gcp.projects.IAMBinding">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.projects.</code><code class="sig-name descname">IAMBinding</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">condition=None</em>, <em class="sig-param">members=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">role=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.projects.IAMBinding" title="Permalink to this definition">¶</a></dt>
<dd><p>Four different resources help you manage your IAM policy for a project. Each of these resources serves a different use case:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">projects.IAMPolicy</span></code>: Authoritative. Sets the IAM policy for the project and replaces any existing policy already attached.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">projects.IAMBinding</span></code>: Authoritative for a given role. Updates the IAM policy to grant a role to a list of members. Other roles within the IAM policy for the project are preserved.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">projects.IAMMember</span></code>: Non-authoritative. Updates the IAM policy to grant a role to a new member. Other members for the role for the project are preserved.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">projects.IAMAuditConfig</span></code>: Authoritative for a given service. Updates the IAM policy to enable audit logging for the given service.</p></li>
</ul>
<blockquote>
<div><p><strong>Note:</strong> <code class="docutils literal notranslate"><span class="pre">projects.IAMPolicy</span></code> <strong>cannot</strong> be used in conjunction with <code class="docutils literal notranslate"><span class="pre">projects.IAMBinding</span></code>, <code class="docutils literal notranslate"><span class="pre">projects.IAMMember</span></code>, or <code class="docutils literal notranslate"><span class="pre">projects.IAMAuditConfig</span></code> or they will fight over what your policy should be.</p>
<p><strong>Note:</strong> <code class="docutils literal notranslate"><span class="pre">projects.IAMBinding</span></code> resources <strong>can be</strong> used in conjunction with <code class="docutils literal notranslate"><span class="pre">projects.IAMMember</span></code> resources <strong>only if</strong> they do not grant privilege to the same role.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>condition</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – ) An <a class="reference external" href="https://cloud.google.com/iam/docs/conditions-overview">IAM Condition</a> for a given binding.
Structure is documented below.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The project ID. If not specified for <code class="docutils literal notranslate"><span class="pre">projects.IAMBinding</span></code>, <code class="docutils literal notranslate"><span class="pre">projects.IAMMember</span></code>, or <code class="docutils literal notranslate"><span class="pre">projects.IAMAuditConfig</span></code>, uses the ID of the project configured with the provider.
Required for <code class="docutils literal notranslate"><span class="pre">projects.IAMPolicy</span></code> - you must explicitly set the project, and it
will not be inferred from the provider.</p></li>
<li><p><strong>role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The role that should be applied. Only one
<code class="docutils literal notranslate"><span class="pre">projects.IAMBinding</span></code> can be used per role. Note that custom roles must be of the format
<code class="docutils literal notranslate"><span class="pre">[projects|organizations]/{parent-name}/roles/{role-name}</span></code>.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>condition</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">description</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">expression</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">title</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/project_iam_binding.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/project_iam_binding.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_gcp.projects.IAMBinding.condition">
<code class="sig-name descname">condition</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.projects.IAMBinding.condition" title="Permalink to this definition">¶</a></dt>
<dd><p>) An <a class="reference external" href="https://cloud.google.com/iam/docs/conditions-overview">IAM Condition</a> for a given binding.
Structure is documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">description</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">expression</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">title</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.projects.IAMBinding.etag">
<code class="sig-name descname">etag</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.projects.IAMBinding.etag" title="Permalink to this definition">¶</a></dt>
<dd><p>(Computed) The etag of the project’s IAM policy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.projects.IAMBinding.project">
<code class="sig-name descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.projects.IAMBinding.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The project ID. If not specified for <code class="docutils literal notranslate"><span class="pre">projects.IAMBinding</span></code>, <code class="docutils literal notranslate"><span class="pre">projects.IAMMember</span></code>, or <code class="docutils literal notranslate"><span class="pre">projects.IAMAuditConfig</span></code>, uses the ID of the project configured with the provider.
Required for <code class="docutils literal notranslate"><span class="pre">projects.IAMPolicy</span></code> - you must explicitly set the project, and it
will not be inferred from the provider.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.projects.IAMBinding.role">
<code class="sig-name descname">role</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.projects.IAMBinding.role" title="Permalink to this definition">¶</a></dt>
<dd><p>The role that should be applied. Only one
<code class="docutils literal notranslate"><span class="pre">projects.IAMBinding</span></code> can be used per role. Note that custom roles must be of the format
<code class="docutils literal notranslate"><span class="pre">[projects|organizations]/{parent-name}/roles/{role-name}</span></code>.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.projects.IAMBinding.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">condition=None</em>, <em class="sig-param">etag=None</em>, <em class="sig-param">members=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">role=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.projects.IAMBinding.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing IAMBinding resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>condition</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – <p>) An <a class="reference external" href="https://cloud.google.com/iam/docs/conditions-overview">IAM Condition</a> for a given binding.
Structure is documented below.</p>
</p></li>
<li><p><strong>etag</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – (Computed) The etag of the project’s IAM policy.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The project ID. If not specified for <code class="docutils literal notranslate"><span class="pre">projects.IAMBinding</span></code>, <code class="docutils literal notranslate"><span class="pre">projects.IAMMember</span></code>, or <code class="docutils literal notranslate"><span class="pre">projects.IAMAuditConfig</span></code>, uses the ID of the project configured with the provider.
Required for <code class="docutils literal notranslate"><span class="pre">projects.IAMPolicy</span></code> - you must explicitly set the project, and it
will not be inferred from the provider.</p></li>
<li><p><strong>role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The role that should be applied. Only one
<code class="docutils literal notranslate"><span class="pre">projects.IAMBinding</span></code> can be used per role. Note that custom roles must be of the format
<code class="docutils literal notranslate"><span class="pre">[projects|organizations]/{parent-name}/roles/{role-name}</span></code>.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>condition</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">description</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">expression</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">title</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/project_iam_binding.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/project_iam_binding.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.projects.IAMBinding.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.projects.IAMBinding.translate_output_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="method">
<dt id="pulumi_gcp.projects.IAMBinding.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.projects.IAMBinding.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="class">
<dt id="pulumi_gcp.projects.IAMCustomRole">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.projects.</code><code class="sig-name descname">IAMCustomRole</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">permissions=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">role_id=None</em>, <em class="sig-param">stage=None</em>, <em class="sig-param">title=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.projects.IAMCustomRole" title="Permalink to this definition">¶</a></dt>
<dd><p>Allows management of a customized Cloud IAM project role. For more information see
<a class="reference external" href="https://cloud.google.com/iam/docs/understanding-custom-roles">the official documentation</a>
and
<a class="reference external" href="https://cloud.google.com/iam/reference/rest/v1/projects.roles">API</a>.</p>
<blockquote>
<div><dl class="simple">
<dt><strong>Warning:</strong> Note that custom roles in GCP have the concept of a soft-delete. There are two issues that may arise</dt><dd><p>from this and how roles are propagated. 1) creating a role may involve undeleting and then updating a role with the
same name, possibly causing confusing behavior between undelete and update. 2) A deleted role is permanently deleted
after 7 days, but it can take up to 30 more days (i.e. between 7 and 37 days after deletion) before the role name is
made available again. This means a deleted role that has been deleted for more than 7 days cannot be changed at all
by this provider, and new roles cannot share that name.</p>
</dd>
</dl>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A human-readable description for the role.</p></li>
<li><p><strong>permissions</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The names of the permissions this role grants when bound in an IAM policy. At least one permission must be specified.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The project that the service account will be created in.
Defaults to the provider project configuration.</p></li>
<li><p><strong>role_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The role id to use for this role.</p></li>
<li><p><strong>stage</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The current launch stage of the role.
Defaults to <code class="docutils literal notranslate"><span class="pre">GA</span></code>.
List of possible stages is <a class="reference external" href="https://cloud.google.com/iam/reference/rest/v1/organizations.roles#Role.RoleLaunchStage">here</a>.</p></li>
<li><p><strong>title</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A human-readable title for the role.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/project_iam_custom_role.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/project_iam_custom_role.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_gcp.projects.IAMCustomRole.deleted">
<code class="sig-name descname">deleted</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.projects.IAMCustomRole.deleted" title="Permalink to this definition">¶</a></dt>
<dd><p>(Optional) The current deleted state of the role.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.projects.IAMCustomRole.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.projects.IAMCustomRole.description" title="Permalink to this definition">¶</a></dt>
<dd><p>A human-readable description for the role.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.projects.IAMCustomRole.permissions">
<code class="sig-name descname">permissions</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.projects.IAMCustomRole.permissions" title="Permalink to this definition">¶</a></dt>
<dd><p>The names of the permissions this role grants when bound in an IAM policy. At least one permission must be specified.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.projects.IAMCustomRole.project">
<code class="sig-name descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.projects.IAMCustomRole.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The project that the service account will be created in.
Defaults to the provider project configuration.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.projects.IAMCustomRole.role_id">
<code class="sig-name descname">role_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.projects.IAMCustomRole.role_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The role id to use for this role.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.projects.IAMCustomRole.stage">
<code class="sig-name descname">stage</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.projects.IAMCustomRole.stage" title="Permalink to this definition">¶</a></dt>
<dd><p>The current launch stage of the role.
Defaults to <code class="docutils literal notranslate"><span class="pre">GA</span></code>.
List of possible stages is <a class="reference external" href="https://cloud.google.com/iam/reference/rest/v1/organizations.roles#Role.RoleLaunchStage">here</a>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.projects.IAMCustomRole.title">
<code class="sig-name descname">title</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.projects.IAMCustomRole.title" title="Permalink to this definition">¶</a></dt>
<dd><p>A human-readable title for the role.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.projects.IAMCustomRole.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">deleted=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">permissions=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">role_id=None</em>, <em class="sig-param">stage=None</em>, <em class="sig-param">title=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.projects.IAMCustomRole.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing IAMCustomRole resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>deleted</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – (Optional) The current deleted state of the role.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A human-readable description for the role.</p></li>
<li><p><strong>permissions</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – The names of the permissions this role grants when bound in an IAM policy. At least one permission must be specified.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The project that the service account will be created in.
Defaults to the provider project configuration.</p></li>
<li><p><strong>role_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The role id to use for this role.</p></li>
<li><p><strong>stage</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The current launch stage of the role.
Defaults to <code class="docutils literal notranslate"><span class="pre">GA</span></code>.
List of possible stages is <a class="reference external" href="https://cloud.google.com/iam/reference/rest/v1/organizations.roles#Role.RoleLaunchStage">here</a>.</p>
</p></li>
<li><p><strong>title</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A human-readable title for the role.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/project_iam_custom_role.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/project_iam_custom_role.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.projects.IAMCustomRole.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.projects.IAMCustomRole.translate_output_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="method">
<dt id="pulumi_gcp.projects.IAMCustomRole.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.projects.IAMCustomRole.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="class">
<dt id="pulumi_gcp.projects.IAMMember">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.projects.</code><code class="sig-name descname">IAMMember</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">condition=None</em>, <em class="sig-param">member=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">role=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.projects.IAMMember" title="Permalink to this definition">¶</a></dt>
<dd><p>Four different resources help you manage your IAM policy for a project. Each of these resources serves a different use case:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">projects.IAMPolicy</span></code>: Authoritative. Sets the IAM policy for the project and replaces any existing policy already attached.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">projects.IAMBinding</span></code>: Authoritative for a given role. Updates the IAM policy to grant a role to a list of members. Other roles within the IAM policy for the project are preserved.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">projects.IAMMember</span></code>: Non-authoritative. Updates the IAM policy to grant a role to a new member. Other members for the role for the project are preserved.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">projects.IAMAuditConfig</span></code>: Authoritative for a given service. Updates the IAM policy to enable audit logging for the given service.</p></li>
</ul>
<blockquote>
<div><p><strong>Note:</strong> <code class="docutils literal notranslate"><span class="pre">projects.IAMPolicy</span></code> <strong>cannot</strong> be used in conjunction with <code class="docutils literal notranslate"><span class="pre">projects.IAMBinding</span></code>, <code class="docutils literal notranslate"><span class="pre">projects.IAMMember</span></code>, or <code class="docutils literal notranslate"><span class="pre">projects.IAMAuditConfig</span></code> or they will fight over what your policy should be.</p>
<p><strong>Note:</strong> <code class="docutils literal notranslate"><span class="pre">projects.IAMBinding</span></code> resources <strong>can be</strong> used in conjunction with <code class="docutils literal notranslate"><span class="pre">projects.IAMMember</span></code> resources <strong>only if</strong> they do not grant privilege to the same role.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>condition</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – <p>) An <a class="reference external" href="https://cloud.google.com/iam/docs/conditions-overview">IAM Condition</a> for a given binding.
Structure is documented below.</p>
</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The project ID. If not specified for <code class="docutils literal notranslate"><span class="pre">projects.IAMBinding</span></code>, <code class="docutils literal notranslate"><span class="pre">projects.IAMMember</span></code>, or <code class="docutils literal notranslate"><span class="pre">projects.IAMAuditConfig</span></code>, uses the ID of the project configured with the provider.
Required for <code class="docutils literal notranslate"><span class="pre">projects.IAMPolicy</span></code> - you must explicitly set the project, and it
will not be inferred from the provider.</p></li>
<li><p><strong>role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The role that should be applied. Only one
<code class="docutils literal notranslate"><span class="pre">projects.IAMBinding</span></code> can be used per role. Note that custom roles must be of the format
<code class="docutils literal notranslate"><span class="pre">[projects|organizations]/{parent-name}/roles/{role-name}</span></code>.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>condition</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">description</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">expression</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">title</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/project_iam_member.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/project_iam_member.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_gcp.projects.IAMMember.condition">
<code class="sig-name descname">condition</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.projects.IAMMember.condition" title="Permalink to this definition">¶</a></dt>
<dd><p>) An <a class="reference external" href="https://cloud.google.com/iam/docs/conditions-overview">IAM Condition</a> for a given binding.
Structure is documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">description</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">expression</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">title</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.projects.IAMMember.etag">
<code class="sig-name descname">etag</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.projects.IAMMember.etag" title="Permalink to this definition">¶</a></dt>
<dd><p>(Computed) The etag of the project’s IAM policy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.projects.IAMMember.project">
<code class="sig-name descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.projects.IAMMember.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The project ID. If not specified for <code class="docutils literal notranslate"><span class="pre">projects.IAMBinding</span></code>, <code class="docutils literal notranslate"><span class="pre">projects.IAMMember</span></code>, or <code class="docutils literal notranslate"><span class="pre">projects.IAMAuditConfig</span></code>, uses the ID of the project configured with the provider.
Required for <code class="docutils literal notranslate"><span class="pre">projects.IAMPolicy</span></code> - you must explicitly set the project, and it
will not be inferred from the provider.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.projects.IAMMember.role">
<code class="sig-name descname">role</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.projects.IAMMember.role" title="Permalink to this definition">¶</a></dt>
<dd><p>The role that should be applied. Only one
<code class="docutils literal notranslate"><span class="pre">projects.IAMBinding</span></code> can be used per role. Note that custom roles must be of the format
<code class="docutils literal notranslate"><span class="pre">[projects|organizations]/{parent-name}/roles/{role-name}</span></code>.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.projects.IAMMember.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">condition=None</em>, <em class="sig-param">etag=None</em>, <em class="sig-param">member=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">role=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.projects.IAMMember.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing IAMMember resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>condition</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – <p>) An <a class="reference external" href="https://cloud.google.com/iam/docs/conditions-overview">IAM Condition</a> for a given binding.
Structure is documented below.</p>
</p></li>
<li><p><strong>etag</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – (Computed) The etag of the project’s IAM policy.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The project ID. If not specified for <code class="docutils literal notranslate"><span class="pre">projects.IAMBinding</span></code>, <code class="docutils literal notranslate"><span class="pre">projects.IAMMember</span></code>, or <code class="docutils literal notranslate"><span class="pre">projects.IAMAuditConfig</span></code>, uses the ID of the project configured with the provider.
Required for <code class="docutils literal notranslate"><span class="pre">projects.IAMPolicy</span></code> - you must explicitly set the project, and it
will not be inferred from the provider.</p></li>
<li><p><strong>role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The role that should be applied. Only one
<code class="docutils literal notranslate"><span class="pre">projects.IAMBinding</span></code> can be used per role. Note that custom roles must be of the format
<code class="docutils literal notranslate"><span class="pre">[projects|organizations]/{parent-name}/roles/{role-name}</span></code>.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>condition</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">description</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">expression</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">title</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/project_iam_member.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/project_iam_member.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.projects.IAMMember.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.projects.IAMMember.translate_output_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="method">
<dt id="pulumi_gcp.projects.IAMMember.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.projects.IAMMember.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="class">
<dt id="pulumi_gcp.projects.IAMPolicy">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.projects.</code><code class="sig-name descname">IAMPolicy</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">policy_data=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.projects.IAMPolicy" title="Permalink to this definition">¶</a></dt>
<dd><p>Four different resources help you manage your IAM policy for a project. Each of these resources serves a different use case:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">projects.IAMPolicy</span></code>: Authoritative. Sets the IAM policy for the project and replaces any existing policy already attached.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">projects.IAMBinding</span></code>: Authoritative for a given role. Updates the IAM policy to grant a role to a list of members. Other roles within the IAM policy for the project are preserved.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">projects.IAMMember</span></code>: Non-authoritative. Updates the IAM policy to grant a role to a new member. Other members for the role for the project are preserved.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">projects.IAMAuditConfig</span></code>: Authoritative for a given service. Updates the IAM policy to enable audit logging for the given service.</p></li>
</ul>
<blockquote>
<div><p><strong>Note:</strong> <code class="docutils literal notranslate"><span class="pre">projects.IAMPolicy</span></code> <strong>cannot</strong> be used in conjunction with <code class="docutils literal notranslate"><span class="pre">projects.IAMBinding</span></code>, <code class="docutils literal notranslate"><span class="pre">projects.IAMMember</span></code>, or <code class="docutils literal notranslate"><span class="pre">projects.IAMAuditConfig</span></code> or they will fight over what your policy should be.</p>
<p><strong>Note:</strong> <code class="docutils literal notranslate"><span class="pre">projects.IAMBinding</span></code> resources <strong>can be</strong> used in conjunction with <code class="docutils literal notranslate"><span class="pre">projects.IAMMember</span></code> resources <strong>only if</strong> they do not grant privilege to the same role.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>policy_data</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The <code class="docutils literal notranslate"><span class="pre">organizations.getIAMPolicy</span></code> data source that represents
the IAM policy that will be applied to the project. The policy will be
merged with any existing policy applied to the project.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The project ID. If not specified for <code class="docutils literal notranslate"><span class="pre">projects.IAMBinding</span></code>, <code class="docutils literal notranslate"><span class="pre">projects.IAMMember</span></code>, or <code class="docutils literal notranslate"><span class="pre">projects.IAMAuditConfig</span></code>, uses the ID of the project configured with the provider.
Required for <code class="docutils literal notranslate"><span class="pre">projects.IAMPolicy</span></code> - you must explicitly set the project, and it
will not be inferred from the provider.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/project_iam_policy.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/project_iam_policy.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_gcp.projects.IAMPolicy.etag">
<code class="sig-name descname">etag</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.projects.IAMPolicy.etag" title="Permalink to this definition">¶</a></dt>
<dd><p>(Computed) The etag of the project’s IAM policy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.projects.IAMPolicy.policy_data">
<code class="sig-name descname">policy_data</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.projects.IAMPolicy.policy_data" title="Permalink to this definition">¶</a></dt>
<dd><p>The <code class="docutils literal notranslate"><span class="pre">organizations.getIAMPolicy</span></code> data source that represents
the IAM policy that will be applied to the project. The policy will be
merged with any existing policy applied to the project.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.projects.IAMPolicy.project">
<code class="sig-name descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.projects.IAMPolicy.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The project ID. If not specified for <code class="docutils literal notranslate"><span class="pre">projects.IAMBinding</span></code>, <code class="docutils literal notranslate"><span class="pre">projects.IAMMember</span></code>, or <code class="docutils literal notranslate"><span class="pre">projects.IAMAuditConfig</span></code>, uses the ID of the project configured with the provider.
Required for <code class="docutils literal notranslate"><span class="pre">projects.IAMPolicy</span></code> - you must explicitly set the project, and it
will not be inferred from the provider.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.projects.IAMPolicy.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">etag=None</em>, <em class="sig-param">policy_data=None</em>, <em class="sig-param">project=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.projects.IAMPolicy.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing IAMPolicy resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>etag</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – (Computed) The etag of the project’s IAM policy.</p></li>
<li><p><strong>policy_data</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The <code class="docutils literal notranslate"><span class="pre">organizations.getIAMPolicy</span></code> data source that represents
the IAM policy that will be applied to the project. The policy will be
merged with any existing policy applied to the project.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The project ID. If not specified for <code class="docutils literal notranslate"><span class="pre">projects.IAMBinding</span></code>, <code class="docutils literal notranslate"><span class="pre">projects.IAMMember</span></code>, or <code class="docutils literal notranslate"><span class="pre">projects.IAMAuditConfig</span></code>, uses the ID of the project configured with the provider.
Required for <code class="docutils literal notranslate"><span class="pre">projects.IAMPolicy</span></code> - you must explicitly set the project, and it
will not be inferred from the provider.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/project_iam_policy.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/project_iam_policy.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.projects.IAMPolicy.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.projects.IAMPolicy.translate_output_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="method">
<dt id="pulumi_gcp.projects.IAMPolicy.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.projects.IAMPolicy.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="class">
<dt id="pulumi_gcp.projects.OrganizationPolicy">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.projects.</code><code class="sig-name descname">OrganizationPolicy</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">boolean_policy=None</em>, <em class="sig-param">constraint=None</em>, <em class="sig-param">list_policy=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">restore_policy=None</em>, <em class="sig-param">version=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.projects.OrganizationPolicy" title="Permalink to this definition">¶</a></dt>
<dd><p>Allows management of Organization policies for a Google Project. For more information see
<a class="reference external" href="https://cloud.google.com/resource-manager/docs/organization-policy/overview">the official
documentation</a> and
<a class="reference external" href="https://cloud.google.com/resource-manager/reference/rest/v1/projects/setOrgPolicy">API</a>.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>boolean_policy</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A boolean policy is a constraint that is either enforced or not. Structure is documented below.</p></li>
<li><p><strong>constraint</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Constraint the Policy is configuring, for example, <code class="docutils literal notranslate"><span class="pre">serviceuser.services</span></code>. Check out the <a class="reference external" href="https://cloud.google.com/resource-manager/docs/organization-policy/understanding-constraints#available_constraints">complete list of available constraints</a>.</p></li>
<li><p><strong>list_policy</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A policy that can define specific values that are allowed or denied for the given constraint. It can also be used to allow or deny all values. Structure is documented below.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The project id of the project to set the policy for.</p></li>
<li><p><strong>restore_policy</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A restore policy is a constraint to restore the default policy. Structure is documented below.</p></li>
<li><p><strong>version</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Version of the Policy. Default version is 0.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>boolean_policy</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">enforced</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
</ul>
<p>The <strong>list_policy</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">allow</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">all</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">values</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">deny</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">all</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">values</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">inheritFromParent</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">suggestedValue</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>restore_policy</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">default</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/project_organization_policy.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/project_organization_policy.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_gcp.projects.OrganizationPolicy.boolean_policy">
<code class="sig-name descname">boolean_policy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.projects.OrganizationPolicy.boolean_policy" title="Permalink to this definition">¶</a></dt>
<dd><p>A boolean policy is a constraint that is either enforced or not. Structure is documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">enforced</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.projects.OrganizationPolicy.constraint">
<code class="sig-name descname">constraint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.projects.OrganizationPolicy.constraint" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Constraint the Policy is configuring, for example, <code class="docutils literal notranslate"><span class="pre">serviceuser.services</span></code>. Check out the <a class="reference external" href="https://cloud.google.com/resource-manager/docs/organization-policy/understanding-constraints#available_constraints">complete list of available constraints</a>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.projects.OrganizationPolicy.etag">
<code class="sig-name descname">etag</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.projects.OrganizationPolicy.etag" title="Permalink to this definition">¶</a></dt>
<dd><p>(Computed) The etag of the organization policy. <code class="docutils literal notranslate"><span class="pre">etag</span></code> is used for optimistic concurrency control as a way to help prevent simultaneous updates of a policy from overwriting each other.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.projects.OrganizationPolicy.list_policy">
<code class="sig-name descname">list_policy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.projects.OrganizationPolicy.list_policy" title="Permalink to this definition">¶</a></dt>
<dd><p>A policy that can define specific values that are allowed or denied for the given constraint. It can also be used to allow or deny all values. Structure is documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">allow</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">all</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">values</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">deny</span></code> (<code class="docutils literal notranslate"><span class="pre">dict</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">all</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">values</span></code> (<code class="docutils literal notranslate"><span class="pre">list</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">inheritFromParent</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">suggestedValue</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.projects.OrganizationPolicy.project">
<code class="sig-name descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.projects.OrganizationPolicy.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The project id of the project to set the policy for.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.projects.OrganizationPolicy.restore_policy">
<code class="sig-name descname">restore_policy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.projects.OrganizationPolicy.restore_policy" title="Permalink to this definition">¶</a></dt>
<dd><p>A restore policy is a constraint to restore the default policy. Structure is documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">default</span></code> (<code class="docutils literal notranslate"><span class="pre">bool</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.projects.OrganizationPolicy.update_time">
<code class="sig-name descname">update_time</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.projects.OrganizationPolicy.update_time" title="Permalink to this definition">¶</a></dt>
<dd><p>(Computed) The timestamp in RFC3339 UTC “Zulu” format, accurate to nanoseconds, representing when the variable was last updated. Example: “2016-10-09T12:33:37.578138407Z”.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.projects.OrganizationPolicy.version">
<code class="sig-name descname">version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.projects.OrganizationPolicy.version" title="Permalink to this definition">¶</a></dt>
<dd><p>Version of the Policy. Default version is 0.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.projects.OrganizationPolicy.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">boolean_policy=None</em>, <em class="sig-param">constraint=None</em>, <em class="sig-param">etag=None</em>, <em class="sig-param">list_policy=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">restore_policy=None</em>, <em class="sig-param">update_time=None</em>, <em class="sig-param">version=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.projects.OrganizationPolicy.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing OrganizationPolicy resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>boolean_policy</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A boolean policy is a constraint that is either enforced or not. Structure is documented below.</p></li>
<li><p><strong>constraint</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The name of the Constraint the Policy is configuring, for example, <code class="docutils literal notranslate"><span class="pre">serviceuser.services</span></code>. Check out the <a class="reference external" href="https://cloud.google.com/resource-manager/docs/organization-policy/understanding-constraints#available_constraints">complete list of available constraints</a>.</p>
</p></li>
<li><p><strong>etag</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – (Computed) The etag of the organization policy. <code class="docutils literal notranslate"><span class="pre">etag</span></code> is used for optimistic concurrency control as a way to help prevent simultaneous updates of a policy from overwriting each other.</p></li>
<li><p><strong>list_policy</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A policy that can define specific values that are allowed or denied for the given constraint. It can also be used to allow or deny all values. Structure is documented below.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The project id of the project to set the policy for.</p></li>
<li><p><strong>restore_policy</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A restore policy is a constraint to restore the default policy. Structure is documented below.</p></li>
<li><p><strong>update_time</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – (Computed) The timestamp in RFC3339 UTC “Zulu” format, accurate to nanoseconds, representing when the variable was last updated. Example: “2016-10-09T12:33:37.578138407Z”.</p></li>
<li><p><strong>version</strong> (<em>pulumi.Input</em><em>[</em><em>float</em><em>]</em>) – Version of the Policy. Default version is 0.</p></li>
</ul>
</dd>
</dl>
<p>The <strong>boolean_policy</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">enforced</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
</ul>
<p>The <strong>list_policy</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">allow</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">all</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">values</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">deny</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[dict]</span></code>)</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">all</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">values</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[list]</span></code>)</p></li>
</ul>
</li>
<li><p><code class="docutils literal notranslate"><span class="pre">inheritFromParent</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">suggestedValue</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[str]</span></code>)</p></li>
</ul>
<p>The <strong>restore_policy</strong> object supports the following:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">default</span></code> (<code class="docutils literal notranslate"><span class="pre">pulumi.Input[bool]</span></code>)</p></li>
</ul>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/project_organization_policy.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/project_organization_policy.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.projects.OrganizationPolicy.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.projects.OrganizationPolicy.translate_output_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="method">
<dt id="pulumi_gcp.projects.OrganizationPolicy.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.projects.OrganizationPolicy.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="class">
<dt id="pulumi_gcp.projects.Service">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.projects.</code><code class="sig-name descname">Service</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">disable_dependent_services=None</em>, <em class="sig-param">disable_on_destroy=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">service=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.projects.Service" title="Permalink to this definition">¶</a></dt>
<dd><p>Allows management of a single API service for an existing Google Cloud Platform project.</p>
<p>For a list of services available, visit the
<a class="reference external" href="https://console.cloud.google.com/apis/library">API library page</a> or run <code class="docutils literal notranslate"><span class="pre">gcloud</span> <span class="pre">services</span> <span class="pre">list</span></code>.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>disable_dependent_services</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If <code class="docutils literal notranslate"><span class="pre">true</span></code>, services that are enabled and which depend on this service should also be disabled when this service is destroyed.
If <code class="docutils literal notranslate"><span class="pre">false</span></code> or unset, an error will be generated if any enabled services depend on this service when destroying it.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The project ID. If not provided, the provider project is used.</p></li>
<li><p><strong>service</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The service to enable.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/project_service.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/project_service.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_gcp.projects.Service.disable_dependent_services">
<code class="sig-name descname">disable_dependent_services</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.projects.Service.disable_dependent_services" title="Permalink to this definition">¶</a></dt>
<dd><p>If <code class="docutils literal notranslate"><span class="pre">true</span></code>, services that are enabled and which depend on this service should also be disabled when this service is destroyed.
If <code class="docutils literal notranslate"><span class="pre">false</span></code> or unset, an error will be generated if any enabled services depend on this service when destroying it.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.projects.Service.project">
<code class="sig-name descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.projects.Service.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The project ID. If not provided, the provider project is used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.projects.Service.service">
<code class="sig-name descname">service</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.projects.Service.service" title="Permalink to this definition">¶</a></dt>
<dd><p>The service to enable.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.projects.Service.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">disable_dependent_services=None</em>, <em class="sig-param">disable_on_destroy=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">service=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.projects.Service.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Service resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>disable_dependent_services</strong> (<em>pulumi.Input</em><em>[</em><em>bool</em><em>]</em>) – If <code class="docutils literal notranslate"><span class="pre">true</span></code>, services that are enabled and which depend on this service should also be disabled when this service is destroyed.
If <code class="docutils literal notranslate"><span class="pre">false</span></code> or unset, an error will be generated if any enabled services depend on this service when destroying it.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The project ID. If not provided, the provider project is used.</p></li>
<li><p><strong>service</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The service to enable.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/project_service.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/project_service.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.projects.Service.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.projects.Service.translate_output_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="method">
<dt id="pulumi_gcp.projects.Service.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.projects.Service.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="class">
<dt id="pulumi_gcp.projects.UsageExportBucket">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.projects.</code><code class="sig-name descname">UsageExportBucket</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">bucket_name=None</em>, <em class="sig-param">prefix=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.projects.UsageExportBucket" title="Permalink to this definition">¶</a></dt>
<dd><p>Allows creation and management of a Google Cloud Platform project.</p>
<p>Projects created with this resource must be associated with an Organization.
See the <a class="reference external" href="https://cloud.google.com/resource-manager/docs/quickstarts">Organization documentation</a> for more details.</p>
<p>The service account used to run this provider when creating a <code class="docutils literal notranslate"><span class="pre">organizations.Project</span></code>
resource must have <code class="docutils literal notranslate"><span class="pre">roles/resourcemanager.projectCreator</span></code>. See the
<a class="reference external" href="https://cloud.google.com/resource-manager/docs/access-control-org">Access Control for Organizations Using IAM</a>
doc for more information.</p>
<p>Note that prior to 0.8.5, <code class="docutils literal notranslate"><span class="pre">organizations.Project</span></code> functioned like a data source,
meaning any project referenced by it had to be created and managed outside
this provider. As of 0.8.5, <code class="docutils literal notranslate"><span class="pre">organizations.Project</span></code> functions like any other
resource, with this provider creating and managing the project. To replicate the old
behavior, either:</p>
<ul class="simple">
<li><p>Use the project ID directly in whatever is referencing the project, using the
<a class="reference external" href="https://www.terraform.io/docs/providers/google/r/google_project_iam.html">projects.IAMPolicy</a>
to replace the old <code class="docutils literal notranslate"><span class="pre">policy_data</span></code> property.</p></li>
<li><p>Use the <a class="reference external" href="https://www.terraform.io/docs/import/usage.html">import</a> functionality
to import your pre-existing project into this provider, where it can be referenced and
used just like always, keeping in mind that this provider will attempt to undo any changes
made outside this provider.</p></li>
</ul>
<blockquote>
<div><p>It’s important to note that any project resources that were added to your config
prior to 0.8.5 will continue to function as they always have, and will not be managed by
this provider. Only newly added projects are affected.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/project_usage_export_bucket.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/project_usage_export_bucket.html.markdown</a>.</p>
</div></blockquote>
<dl class="method">
<dt id="pulumi_gcp.projects.UsageExportBucket.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">bucket_name=None</em>, <em class="sig-param">prefix=None</em>, <em class="sig-param">project=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.projects.UsageExportBucket.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing UsageExportBucket resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/project_usage_export_bucket.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/project_usage_export_bucket.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.projects.UsageExportBucket.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.projects.UsageExportBucket.translate_output_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="method">
<dt id="pulumi_gcp.projects.UsageExportBucket.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.projects.UsageExportBucket.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

<dl class="function">
<dt id="pulumi_gcp.projects.get_organization_policy">
<code class="sig-prename descclassname">pulumi_gcp.projects.</code><code class="sig-name descname">get_organization_policy</code><span class="sig-paren">(</span><em class="sig-param">constraint=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.projects.get_organization_policy" title="Permalink to this definition">¶</a></dt>
<dd><p>Allows management of Organization policies for a Google Project. For more information see
<a class="reference external" href="https://cloud.google.com/resource-manager/docs/organization-policy/overview">the official
documentation</a></p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>constraint</strong> (<em>str</em>) – <p>(Required) The name of the Constraint the Policy is configuring, for example, <code class="docutils literal notranslate"><span class="pre">serviceuser.services</span></code>. Check out the <a class="reference external" href="https://cloud.google.com/resource-manager/docs/organization-policy/understanding-constraints#available_constraints">complete list of available constraints</a>.</p>
</p></li>
<li><p><strong>project</strong> (<em>str</em>) – The project ID.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/d/project_organization_policy.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/d/project_organization_policy.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="function">
<dt id="pulumi_gcp.projects.get_project">
<code class="sig-prename descclassname">pulumi_gcp.projects.</code><code class="sig-name descname">get_project</code><span class="sig-paren">(</span><em class="sig-param">filter=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.projects.get_project" title="Permalink to this definition">¶</a></dt>
<dd><p>Retrieve information about a set of projects based on a filter. See the
<a class="reference external" href="https://cloud.google.com/resource-manager/reference/rest/v1/projects/list">REST API</a>
for more details.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><p><strong>filter</strong> (<em>str</em>) – <p>A string filter as defined in the <a class="reference external" href="https://cloud.google.com/resource-manager/reference/rest/v1/projects/list#query-parameters">REST API</a>.</p>
</p>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/d/projects.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/d/projects.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

</div>
