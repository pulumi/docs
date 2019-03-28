<div class="section" id="module-pulumi_gcp.service_account">
<span id="service-account"></span><h1>service_account<a class="headerlink" href="#module-pulumi_gcp.service_account" title="Permalink to this headline">¶</a></h1>
<dl class="class">
<dt id="pulumi_gcp.service_account.Account">
<em class="property">class </em><code class="descclassname">pulumi_gcp.service_account.</code><code class="descname">Account</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>account_id=None</em>, <em>display_name=None</em>, <em>project=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.service_account.Account" title="Permalink to this definition">¶</a></dt>
<dd><p>Allows management of a <a class="reference external" href="https://cloud.google.com/compute/docs/access/service-accounts">Google Cloud Platform service account</a></p>
<blockquote>
<div>Creation of service accounts is eventually consistent, and that can lead to
errors when you try to apply ACLs to service accounts immediately after
creation. If using these resources in the same config, you can add a
<cite>``sleep`</cite> using <code class="docutils literal notranslate"><span class="pre">local-exec</span></code> &lt;<a class="reference external" href="https://github.com/hashicorp/terraform/issues/17726#issuecomment-377357866">https://github.com/hashicorp/terraform/issues/17726#issuecomment-377357866</a>&gt;`_.</div></blockquote>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>account_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The account id that is used to generate the service
account email address and a stable unique id. It is unique within a project,
must be 6-30 characters long, and match the regular expression <code class="docutils literal notranslate"><span class="pre">a-z</span></code>
to comply with RFC1035. Changing this forces a new service account to be created.</li>
<li><strong>display_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The display name for the service account.
Can be updated without creating a new resource.</li>
<li><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project that the service account will be created in.
Defaults to the provider project configuration.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_gcp.service_account.Account.account_id">
<code class="descname">account_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.service_account.Account.account_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The account id that is used to generate the service
account email address and a stable unique id. It is unique within a project,
must be 6-30 characters long, and match the regular expression <code class="docutils literal notranslate"><span class="pre">a-z</span></code>
to comply with RFC1035. Changing this forces a new service account to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.service_account.Account.display_name">
<code class="descname">display_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.service_account.Account.display_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The display name for the service account.
Can be updated without creating a new resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.service_account.Account.email">
<code class="descname">email</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.service_account.Account.email" title="Permalink to this definition">¶</a></dt>
<dd><p>The e-mail address of the service account. This value
should be referenced from any <code class="docutils literal notranslate"><span class="pre">google_iam_policy</span></code> data sources
that would grant the service account privileges.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.service_account.Account.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.service_account.Account.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The fully-qualified name of the service account.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.service_account.Account.project">
<code class="descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.service_account.Account.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project that the service account will be created in.
Defaults to the provider project configuration.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.service_account.Account.unique_id">
<code class="descname">unique_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.service_account.Account.unique_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The unique id of the service account.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.service_account.Account.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.service_account.Account.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.service_account.Account.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.service_account.Account.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.service_account.GetAccountKeyResult">
<em class="property">class </em><code class="descclassname">pulumi_gcp.service_account.</code><code class="descname">GetAccountKeyResult</code><span class="sig-paren">(</span><em>key_algorithm=None</em>, <em>public_key=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.service_account.GetAccountKeyResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getAccountKey.</p>
<dl class="attribute">
<dt id="pulumi_gcp.service_account.GetAccountKeyResult.public_key">
<code class="descname">public_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.service_account.GetAccountKeyResult.public_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The public key, base64 encoded</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.service_account.GetAccountKeyResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.service_account.GetAccountKeyResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_gcp.service_account.GetAccountResult">
<em class="property">class </em><code class="descclassname">pulumi_gcp.service_account.</code><code class="descname">GetAccountResult</code><span class="sig-paren">(</span><em>display_name=None</em>, <em>email=None</em>, <em>name=None</em>, <em>unique_id=None</em>, <em>id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.service_account.GetAccountResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getAccount.</p>
<dl class="attribute">
<dt id="pulumi_gcp.service_account.GetAccountResult.display_name">
<code class="descname">display_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.service_account.GetAccountResult.display_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The display name for the service account.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.service_account.GetAccountResult.email">
<code class="descname">email</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.service_account.GetAccountResult.email" title="Permalink to this definition">¶</a></dt>
<dd><p>The e-mail address of the service account. This value
should be referenced from any <code class="docutils literal notranslate"><span class="pre">google_iam_policy</span></code> data sources
that would grant the service account privileges.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.service_account.GetAccountResult.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.service_account.GetAccountResult.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The fully-qualified name of the service account.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.service_account.GetAccountResult.unique_id">
<code class="descname">unique_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.service_account.GetAccountResult.unique_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The unique id of the service account.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.service_account.GetAccountResult.id">
<code class="descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.service_account.GetAccountResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_gcp.service_account.IAMBinding">
<em class="property">class </em><code class="descclassname">pulumi_gcp.service_account.</code><code class="descname">IAMBinding</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>members=None</em>, <em>role=None</em>, <em>service_account_id=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.service_account.IAMBinding" title="Permalink to this definition">¶</a></dt>
<dd><p>When managing IAM roles, you can treat a service account either as a resource or as an identity. This resource is to add iam policy bindings to a service account resource <strong>to configure permissions for who can edit the service account</strong>. To configure permissions for a service account to act as an identity that can manage other GCP resources, use the google_project_iam set of resources.</p>
<p>Three different resources help you manage your IAM policy for a service account. Each of these resources serves a different use case:</p>
<ul class="simple">
<li><code class="docutils literal notranslate"><span class="pre">google_service_account_iam_policy</span></code>: Authoritative. Sets the IAM policy for the service account and replaces any existing policy already attached.</li>
<li><code class="docutils literal notranslate"><span class="pre">google_service_account_iam_binding</span></code>: Authoritative for a given role. Updates the IAM policy to grant a role to a list of members. Other roles within the IAM policy for the service account are preserved.</li>
<li><code class="docutils literal notranslate"><span class="pre">google_service_account_iam_member</span></code>: Non-authoritative. Updates the IAM policy to grant a role to a new member. Other members for the role for the service account are preserved.</li>
</ul>
<blockquote>
<div><p><strong>Note:</strong> <code class="docutils literal notranslate"><span class="pre">google_service_account_iam_policy</span></code> <strong>cannot</strong> be used in conjunction with <code class="docutils literal notranslate"><span class="pre">google_service_account_iam_binding</span></code> and <code class="docutils literal notranslate"><span class="pre">google_service_account_iam_member</span></code> or they will fight over what your policy should be.</p>
<p><strong>Note:</strong> <code class="docutils literal notranslate"><span class="pre">google_service_account_iam_binding</span></code> resources <strong>can be</strong> used in conjunction with <code class="docutils literal notranslate"><span class="pre">google_service_account_iam_member</span></code> resources <strong>only if</strong> they do not grant privilege to the same role.</p>
</div></blockquote>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The role that should be applied. Only one
<code class="docutils literal notranslate"><span class="pre">google_service_account_iam_binding</span></code> can be used per role. Note that custom roles must be of the format
<code class="docutils literal notranslate"><span class="pre">[projects|organizations]/{parent-name}/roles/{role-name}</span></code>.</li>
<li><strong>service_account_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The fully-qualified name of the service account to apply policy to.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_gcp.service_account.IAMBinding.etag">
<code class="descname">etag</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.service_account.IAMBinding.etag" title="Permalink to this definition">¶</a></dt>
<dd><p>(Computed) The etag of the service account IAM policy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.service_account.IAMBinding.role">
<code class="descname">role</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.service_account.IAMBinding.role" title="Permalink to this definition">¶</a></dt>
<dd><p>The role that should be applied. Only one
<code class="docutils literal notranslate"><span class="pre">google_service_account_iam_binding</span></code> can be used per role. Note that custom roles must be of the format
<code class="docutils literal notranslate"><span class="pre">[projects|organizations]/{parent-name}/roles/{role-name}</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.service_account.IAMBinding.service_account_id">
<code class="descname">service_account_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.service_account.IAMBinding.service_account_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The fully-qualified name of the service account to apply policy to.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.service_account.IAMBinding.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.service_account.IAMBinding.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.service_account.IAMBinding.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.service_account.IAMBinding.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.service_account.IAMMember">
<em class="property">class </em><code class="descclassname">pulumi_gcp.service_account.</code><code class="descname">IAMMember</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>member=None</em>, <em>role=None</em>, <em>service_account_id=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.service_account.IAMMember" title="Permalink to this definition">¶</a></dt>
<dd><p>When managing IAM roles, you can treat a service account either as a resource or as an identity. This resource is to add iam policy bindings to a service account resource <strong>to configure permissions for who can edit the service account</strong>. To configure permissions for a service account to act as an identity that can manage other GCP resources, use the google_project_iam set of resources.</p>
<p>Three different resources help you manage your IAM policy for a service account. Each of these resources serves a different use case:</p>
<ul class="simple">
<li><code class="docutils literal notranslate"><span class="pre">google_service_account_iam_policy</span></code>: Authoritative. Sets the IAM policy for the service account and replaces any existing policy already attached.</li>
<li><code class="docutils literal notranslate"><span class="pre">google_service_account_iam_binding</span></code>: Authoritative for a given role. Updates the IAM policy to grant a role to a list of members. Other roles within the IAM policy for the service account are preserved.</li>
<li><code class="docutils literal notranslate"><span class="pre">google_service_account_iam_member</span></code>: Non-authoritative. Updates the IAM policy to grant a role to a new member. Other members for the role for the service account are preserved.</li>
</ul>
<blockquote>
<div><p><strong>Note:</strong> <code class="docutils literal notranslate"><span class="pre">google_service_account_iam_policy</span></code> <strong>cannot</strong> be used in conjunction with <code class="docutils literal notranslate"><span class="pre">google_service_account_iam_binding</span></code> and <code class="docutils literal notranslate"><span class="pre">google_service_account_iam_member</span></code> or they will fight over what your policy should be.</p>
<p><strong>Note:</strong> <code class="docutils literal notranslate"><span class="pre">google_service_account_iam_binding</span></code> resources <strong>can be</strong> used in conjunction with <code class="docutils literal notranslate"><span class="pre">google_service_account_iam_member</span></code> resources <strong>only if</strong> they do not grant privilege to the same role.</p>
</div></blockquote>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The role that should be applied. Only one
<code class="docutils literal notranslate"><span class="pre">google_service_account_iam_binding</span></code> can be used per role. Note that custom roles must be of the format
<code class="docutils literal notranslate"><span class="pre">[projects|organizations]/{parent-name}/roles/{role-name}</span></code>.</li>
<li><strong>service_account_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The fully-qualified name of the service account to apply policy to.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_gcp.service_account.IAMMember.etag">
<code class="descname">etag</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.service_account.IAMMember.etag" title="Permalink to this definition">¶</a></dt>
<dd><p>(Computed) The etag of the service account IAM policy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.service_account.IAMMember.role">
<code class="descname">role</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.service_account.IAMMember.role" title="Permalink to this definition">¶</a></dt>
<dd><p>The role that should be applied. Only one
<code class="docutils literal notranslate"><span class="pre">google_service_account_iam_binding</span></code> can be used per role. Note that custom roles must be of the format
<code class="docutils literal notranslate"><span class="pre">[projects|organizations]/{parent-name}/roles/{role-name}</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.service_account.IAMMember.service_account_id">
<code class="descname">service_account_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.service_account.IAMMember.service_account_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The fully-qualified name of the service account to apply policy to.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.service_account.IAMMember.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.service_account.IAMMember.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.service_account.IAMMember.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.service_account.IAMMember.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.service_account.IAMPolicy">
<em class="property">class </em><code class="descclassname">pulumi_gcp.service_account.</code><code class="descname">IAMPolicy</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>policy_data=None</em>, <em>service_account_id=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.service_account.IAMPolicy" title="Permalink to this definition">¶</a></dt>
<dd><p>When managing IAM roles, you can treat a service account either as a resource or as an identity. This resource is to add iam policy bindings to a service account resource <strong>to configure permissions for who can edit the service account</strong>. To configure permissions for a service account to act as an identity that can manage other GCP resources, use the google_project_iam set of resources.</p>
<p>Three different resources help you manage your IAM policy for a service account. Each of these resources serves a different use case:</p>
<ul class="simple">
<li><code class="docutils literal notranslate"><span class="pre">google_service_account_iam_policy</span></code>: Authoritative. Sets the IAM policy for the service account and replaces any existing policy already attached.</li>
<li><code class="docutils literal notranslate"><span class="pre">google_service_account_iam_binding</span></code>: Authoritative for a given role. Updates the IAM policy to grant a role to a list of members. Other roles within the IAM policy for the service account are preserved.</li>
<li><code class="docutils literal notranslate"><span class="pre">google_service_account_iam_member</span></code>: Non-authoritative. Updates the IAM policy to grant a role to a new member. Other members for the role for the service account are preserved.</li>
</ul>
<blockquote>
<div><p><strong>Note:</strong> <code class="docutils literal notranslate"><span class="pre">google_service_account_iam_policy</span></code> <strong>cannot</strong> be used in conjunction with <code class="docutils literal notranslate"><span class="pre">google_service_account_iam_binding</span></code> and <code class="docutils literal notranslate"><span class="pre">google_service_account_iam_member</span></code> or they will fight over what your policy should be.</p>
<p><strong>Note:</strong> <code class="docutils literal notranslate"><span class="pre">google_service_account_iam_binding</span></code> resources <strong>can be</strong> used in conjunction with <code class="docutils literal notranslate"><span class="pre">google_service_account_iam_member</span></code> resources <strong>only if</strong> they do not grant privilege to the same role.</p>
</div></blockquote>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>policy_data</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The policy data generated by
a <code class="docutils literal notranslate"><span class="pre">google_iam_policy</span></code> data source.</li>
<li><strong>service_account_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The fully-qualified name of the service account to apply policy to.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_gcp.service_account.IAMPolicy.etag">
<code class="descname">etag</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.service_account.IAMPolicy.etag" title="Permalink to this definition">¶</a></dt>
<dd><p>(Computed) The etag of the service account IAM policy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.service_account.IAMPolicy.policy_data">
<code class="descname">policy_data</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.service_account.IAMPolicy.policy_data" title="Permalink to this definition">¶</a></dt>
<dd><p>The policy data generated by
a <code class="docutils literal notranslate"><span class="pre">google_iam_policy</span></code> data source.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.service_account.IAMPolicy.service_account_id">
<code class="descname">service_account_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.service_account.IAMPolicy.service_account_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The fully-qualified name of the service account to apply policy to.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.service_account.IAMPolicy.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.service_account.IAMPolicy.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.service_account.IAMPolicy.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.service_account.IAMPolicy.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.service_account.Key">
<em class="property">class </em><code class="descclassname">pulumi_gcp.service_account.</code><code class="descname">Key</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>key_algorithm=None</em>, <em>pgp_key=None</em>, <em>private_key_type=None</em>, <em>public_key_type=None</em>, <em>service_account_id=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.service_account.Key" title="Permalink to this definition">¶</a></dt>
<dd><p>Creates and manages service account key-pairs, which allow the user to establish identity of a service account outside of GCP. For more information, see <a class="reference external" href="https://cloud.google.com/iam/docs/creating-managing-service-account-keys">the official documentation</a> and <a class="reference external" href="https://cloud.google.com/iam/reference/rest/v1/projects.serviceAccounts.keys">API</a>.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>key_algorithm</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The algorithm used to generate the key. KEY_ALG_RSA_2048 is the default algorithm.
Valid values are listed at
<a class="reference external" href="https://cloud.google.com/iam/reference/rest/v1/projects.serviceAccounts.keys#ServiceAccountKeyAlgorithm">ServiceAccountPrivateKeyType</a>
(only used on create)</li>
<li><strong>pgp_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – An optional PGP key to encrypt the resulting private
key material. Only used when creating or importing a new key pair. May either be
a base64-encoded public key or a <code class="docutils literal notranslate"><span class="pre">keybase:keybaseusername</span></code> string for looking up
in Vault.</li>
<li><strong>private_key_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The output format of the private key. TYPE_GOOGLE_CREDENTIALS_FILE is the default output format.</li>
<li><strong>public_key_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The output format of the public key requested. X509_PEM is the default output format.</li>
<li><strong>service_account_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Service account id of the Key Pair. This can be a string in the format
<code class="docutils literal notranslate"><span class="pre">{ACCOUNT}</span></code> or <code class="docutils literal notranslate"><span class="pre">projects/{PROJECT_ID}/serviceAccounts/{ACCOUNT}</span></code>, where <code class="docutils literal notranslate"><span class="pre">{ACCOUNT}</span></code> is the email address or
unique id of the service account. If the <code class="docutils literal notranslate"><span class="pre">{ACCOUNT}</span></code> syntax is used, the project will be inferred from the account.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_gcp.service_account.Key.key_algorithm">
<code class="descname">key_algorithm</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.service_account.Key.key_algorithm" title="Permalink to this definition">¶</a></dt>
<dd><p>The algorithm used to generate the key. KEY_ALG_RSA_2048 is the default algorithm.
Valid values are listed at
<a class="reference external" href="https://cloud.google.com/iam/reference/rest/v1/projects.serviceAccounts.keys#ServiceAccountKeyAlgorithm">ServiceAccountPrivateKeyType</a>
(only used on create)</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.service_account.Key.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.service_account.Key.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name used for this key pair</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.service_account.Key.pgp_key">
<code class="descname">pgp_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.service_account.Key.pgp_key" title="Permalink to this definition">¶</a></dt>
<dd><p>An optional PGP key to encrypt the resulting private
key material. Only used when creating or importing a new key pair. May either be
a base64-encoded public key or a <code class="docutils literal notranslate"><span class="pre">keybase:keybaseusername</span></code> string for looking up
in Vault.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.service_account.Key.private_key">
<code class="descname">private_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.service_account.Key.private_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The private key in JSON format, base64 encoded. This is what you normally get as a file when creating
service account keys through the CLI or web console. This is only populated when creating a new key, and when no
<code class="docutils literal notranslate"><span class="pre">pgp_key</span></code> is provided.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.service_account.Key.private_key_encrypted">
<code class="descname">private_key_encrypted</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.service_account.Key.private_key_encrypted" title="Permalink to this definition">¶</a></dt>
<dd><p>The private key material, base 64 encoded and
encrypted with the given <code class="docutils literal notranslate"><span class="pre">pgp_key</span></code>. This is only populated when creating a new
key and <code class="docutils literal notranslate"><span class="pre">pgp_key</span></code> is supplied</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.service_account.Key.private_key_fingerprint">
<code class="descname">private_key_fingerprint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.service_account.Key.private_key_fingerprint" title="Permalink to this definition">¶</a></dt>
<dd><p>The MD5 public key fingerprint for the encrypted
private key. This is only populated when creating a new key and <code class="docutils literal notranslate"><span class="pre">pgp_key</span></code> is supplied</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.service_account.Key.private_key_type">
<code class="descname">private_key_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.service_account.Key.private_key_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The output format of the private key. TYPE_GOOGLE_CREDENTIALS_FILE is the default output format.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.service_account.Key.public_key">
<code class="descname">public_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.service_account.Key.public_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The public key, base64 encoded</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.service_account.Key.public_key_type">
<code class="descname">public_key_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.service_account.Key.public_key_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The output format of the public key requested. X509_PEM is the default output format.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.service_account.Key.service_account_id">
<code class="descname">service_account_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.service_account.Key.service_account_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The Service account id of the Key Pair. This can be a string in the format
<code class="docutils literal notranslate"><span class="pre">{ACCOUNT}</span></code> or <code class="docutils literal notranslate"><span class="pre">projects/{PROJECT_ID}/serviceAccounts/{ACCOUNT}</span></code>, where <code class="docutils literal notranslate"><span class="pre">{ACCOUNT}</span></code> is the email address or
unique id of the service account. If the <code class="docutils literal notranslate"><span class="pre">{ACCOUNT}</span></code> syntax is used, the project will be inferred from the account.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.service_account.Key.valid_after">
<code class="descname">valid_after</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.service_account.Key.valid_after" title="Permalink to this definition">¶</a></dt>
<dd><p>The key can be used after this timestamp. A timestamp in RFC3339 UTC “Zulu” format, accurate to nanoseconds. Example: “2014-10-02T15:01:23.045123456Z”.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.service_account.Key.valid_before">
<code class="descname">valid_before</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.service_account.Key.valid_before" title="Permalink to this definition">¶</a></dt>
<dd><p>The key can be used before this timestamp.
A timestamp in RFC3339 UTC “Zulu” format, accurate to nanoseconds. Example: “2014-10-02T15:01:23.045123456Z”.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.service_account.Key.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.service_account.Key.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.service_account.Key.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.service_account.Key.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.service_account.get_account">
<code class="descclassname">pulumi_gcp.service_account.</code><code class="descname">get_account</code><span class="sig-paren">(</span><em>account_id=None</em>, <em>project=None</em>, <em>opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.service_account.get_account" title="Permalink to this definition">¶</a></dt>
<dd><p>Get the service account from a project. For more information see
the official <a class="reference external" href="https://cloud.google.com/compute/docs/access/service-accounts">API</a> documentation.</p>
</dd></dl>

<dl class="function">
<dt id="pulumi_gcp.service_account.get_account_key">
<code class="descclassname">pulumi_gcp.service_account.</code><code class="descname">get_account_key</code><span class="sig-paren">(</span><em>name=None</em>, <em>project=None</em>, <em>public_key_type=None</em>, <em>opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.service_account.get_account_key" title="Permalink to this definition">¶</a></dt>
<dd><p>Get service account public key. For more information, see <a class="reference external" href="https://cloud.google.com/iam/docs/creating-managing-service-account-keys">the official documentation</a> and <a class="reference external" href="https://cloud.google.com/iam/reference/rest/v1/projects.serviceAccounts.keys/get">API</a>.</p>
</dd></dl>

</div>
