<div class="section" id="module-pulumi_gcp.folder">
<span id="folder"></span><h1>folder<a class="headerlink" href="#module-pulumi_gcp.folder" title="Permalink to this headline">¶</a></h1>
<dl class="class">
<dt id="pulumi_gcp.folder.IAMBinding">
<em class="property">class </em><code class="descclassname">pulumi_gcp.folder.</code><code class="descname">IAMBinding</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>folder=None</em>, <em>members=None</em>, <em>role=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.folder.IAMBinding" title="Permalink to this definition">¶</a></dt>
<dd><p>Allows creation and management of a single binding within IAM policy for
an existing Google Cloud Platform folder.</p>
<blockquote>
<div><dl class="docutils">
<dt><strong>Note:</strong> This resource <em>must not</em> be used in conjunction with</dt>
<dd><code class="docutils literal notranslate"><span class="pre">google_folder_iam_policy</span></code> or they will fight over what your policy
should be.</dd>
</dl>
</div></blockquote>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>folder</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The resource name of the folder the policy is attached to. Its format is folders/{folder_id}.</li>
<li><strong>members</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – An array of identites that will be granted the privilege in the <code class="docutils literal notranslate"><span class="pre">role</span></code>.
Each entry can have one of the following values:</li>
</ul>
</td>
</tr>
</tbody>
</table>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><strong>role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The role that should be applied. Only one
<code class="docutils literal notranslate"><span class="pre">google_folder_iam_binding</span></code> can be used per role. Note that custom roles must be of the format
<code class="docutils literal notranslate"><span class="pre">[projects|organizations]/{parent-name}/roles/{role-name}</span></code>.</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_gcp.folder.IAMBinding.etag">
<code class="descname">etag</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.folder.IAMBinding.etag" title="Permalink to this definition">¶</a></dt>
<dd><p>(Computed) The etag of the folder’s IAM policy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.folder.IAMBinding.folder">
<code class="descname">folder</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.folder.IAMBinding.folder" title="Permalink to this definition">¶</a></dt>
<dd><p>The resource name of the folder the policy is attached to. Its format is folders/{folder_id}.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.folder.IAMBinding.members">
<code class="descname">members</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.folder.IAMBinding.members" title="Permalink to this definition">¶</a></dt>
<dd><p>An array of identites that will be granted the privilege in the <code class="docutils literal notranslate"><span class="pre">role</span></code>.
Each entry can have one of the following values:</p>
<ul class="simple">
<li><strong>user:{emailid}</strong>: An email address that represents a specific Google account. For example, <a class="reference external" href="mailto:alice&#37;&#52;&#48;gmail&#46;com">alice<span>&#64;</span>gmail<span>&#46;</span>com</a> or <a class="reference external" href="mailto:joe&#37;&#52;&#48;example&#46;com">joe<span>&#64;</span>example<span>&#46;</span>com</a>.</li>
<li><strong>serviceAccount:{emailid}</strong>: An email address that represents a service account. For example, <a class="reference external" href="mailto:my-other-app&#37;&#52;&#48;appspot&#46;gserviceaccount&#46;com">my-other-app<span>&#64;</span>appspot<span>&#46;</span>gserviceaccount<span>&#46;</span>com</a>.</li>
<li><strong>group:{emailid}</strong>: An email address that represents a Google group. For example, <a class="reference external" href="mailto:admins&#37;&#52;&#48;example&#46;com">admins<span>&#64;</span>example<span>&#46;</span>com</a>.</li>
<li><strong>domain:{domain}</strong>: A G Suite domain (primary, instead of alias) name that represents all the users of that domain. For example, google.com or example.com.</li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.folder.IAMBinding.role">
<code class="descname">role</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.folder.IAMBinding.role" title="Permalink to this definition">¶</a></dt>
<dd><p>The role that should be applied. Only one
<code class="docutils literal notranslate"><span class="pre">google_folder_iam_binding</span></code> can be used per role. Note that custom roles must be of the format
<code class="docutils literal notranslate"><span class="pre">[projects|organizations]/{parent-name}/roles/{role-name}</span></code>.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.folder.IAMBinding.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.folder.IAMBinding.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.folder.IAMBinding.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.folder.IAMBinding.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.folder.IAMMember">
<em class="property">class </em><code class="descclassname">pulumi_gcp.folder.</code><code class="descname">IAMMember</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>folder=None</em>, <em>member=None</em>, <em>role=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.folder.IAMMember" title="Permalink to this definition">¶</a></dt>
<dd><p>Allows creation and management of a single member for a single binding within
the IAM policy for an existing Google Cloud Platform folder.</p>
<blockquote>
<div><dl class="docutils">
<dt><strong>Note:</strong> This resource <em>must not</em> be used in conjunction with</dt>
<dd><code class="docutils literal notranslate"><span class="pre">google_folder_iam_policy</span></code> or they will fight over what your policy
should be. Similarly, roles controlled by <code class="docutils literal notranslate"><span class="pre">google_folder_iam_binding</span></code>
should not be assigned to using <code class="docutils literal notranslate"><span class="pre">google_folder_iam_member</span></code>.</dd>
</dl>
</div></blockquote>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>folder</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The resource name of the folder the policy is attached to. Its format is folders/{folder_id}.</li>
<li><strong>member</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The identity that will be granted the privilege in the <code class="docutils literal notranslate"><span class="pre">role</span></code>.
This field can have one of the following values:</li>
</ul>
</td>
</tr>
</tbody>
</table>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><strong>role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The role that should be applied. Note that custom roles must be of the format
<code class="docutils literal notranslate"><span class="pre">[projects|organizations]/{parent-name}/roles/{role-name}</span></code>.</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_gcp.folder.IAMMember.etag">
<code class="descname">etag</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.folder.IAMMember.etag" title="Permalink to this definition">¶</a></dt>
<dd><p>(Computed) The etag of the folder’s IAM policy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.folder.IAMMember.folder">
<code class="descname">folder</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.folder.IAMMember.folder" title="Permalink to this definition">¶</a></dt>
<dd><p>The resource name of the folder the policy is attached to. Its format is folders/{folder_id}.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.folder.IAMMember.member">
<code class="descname">member</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.folder.IAMMember.member" title="Permalink to this definition">¶</a></dt>
<dd><p>The identity that will be granted the privilege in the <code class="docutils literal notranslate"><span class="pre">role</span></code>.
This field can have one of the following values:</p>
<ul class="simple">
<li><strong>user:{emailid}</strong>: An email address that represents a specific Google account. For example, <a class="reference external" href="mailto:alice&#37;&#52;&#48;gmail&#46;com">alice<span>&#64;</span>gmail<span>&#46;</span>com</a> or <a class="reference external" href="mailto:joe&#37;&#52;&#48;example&#46;com">joe<span>&#64;</span>example<span>&#46;</span>com</a>.</li>
<li><strong>serviceAccount:{emailid}</strong>: An email address that represents a service account. For example, <a class="reference external" href="mailto:my-other-app&#37;&#52;&#48;appspot&#46;gserviceaccount&#46;com">my-other-app<span>&#64;</span>appspot<span>&#46;</span>gserviceaccount<span>&#46;</span>com</a>.</li>
<li><strong>group:{emailid}</strong>: An email address that represents a Google group. For example, <a class="reference external" href="mailto:admins&#37;&#52;&#48;example&#46;com">admins<span>&#64;</span>example<span>&#46;</span>com</a>.</li>
<li><strong>domain:{domain}</strong>: A G Suite domain (primary, instead of alias) name that represents all the users of that domain. For example, google.com or example.com.</li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.folder.IAMMember.role">
<code class="descname">role</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.folder.IAMMember.role" title="Permalink to this definition">¶</a></dt>
<dd><p>The role that should be applied. Note that custom roles must be of the format
<code class="docutils literal notranslate"><span class="pre">[projects|organizations]/{parent-name}/roles/{role-name}</span></code>.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.folder.IAMMember.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.folder.IAMMember.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.folder.IAMMember.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.folder.IAMMember.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.folder.IAMPolicy">
<em class="property">class </em><code class="descclassname">pulumi_gcp.folder.</code><code class="descname">IAMPolicy</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>folder=None</em>, <em>policy_data=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.folder.IAMPolicy" title="Permalink to this definition">¶</a></dt>
<dd><p>Allows creation and management of the IAM policy for an existing Google Cloud
Platform folder.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>folder</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The resource name of the folder the policy is attached to. Its format is folders/{folder_id}.</li>
<li><strong>policy_data</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The <code class="docutils literal notranslate"><span class="pre">google_iam_policy</span></code> data source that represents
the IAM policy that will be applied to the folder. This policy overrides any existing
policy applied to the folder.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_gcp.folder.IAMPolicy.etag">
<code class="descname">etag</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.folder.IAMPolicy.etag" title="Permalink to this definition">¶</a></dt>
<dd><p>(Computed) The etag of the folder’s IAM policy. <code class="docutils literal notranslate"><span class="pre">etag</span></code> is used for optimistic concurrency control as a way to help prevent simultaneous updates of a policy from overwriting each other.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.folder.IAMPolicy.folder">
<code class="descname">folder</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.folder.IAMPolicy.folder" title="Permalink to this definition">¶</a></dt>
<dd><p>The resource name of the folder the policy is attached to. Its format is folders/{folder_id}.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.folder.IAMPolicy.policy_data">
<code class="descname">policy_data</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.folder.IAMPolicy.policy_data" title="Permalink to this definition">¶</a></dt>
<dd><p>The <code class="docutils literal notranslate"><span class="pre">google_iam_policy</span></code> data source that represents
the IAM policy that will be applied to the folder. This policy overrides any existing
policy applied to the folder.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.folder.IAMPolicy.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.folder.IAMPolicy.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.folder.IAMPolicy.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.folder.IAMPolicy.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.folder.OrganizationPolicy">
<em class="property">class </em><code class="descclassname">pulumi_gcp.folder.</code><code class="descname">OrganizationPolicy</code><span class="sig-paren">(</span><em>resource_name</em>, <em>opts=None</em>, <em>boolean_policy=None</em>, <em>constraint=None</em>, <em>folder=None</em>, <em>list_policy=None</em>, <em>restore_policy=None</em>, <em>version=None</em>, <em>__name__=None</em>, <em>__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.folder.OrganizationPolicy" title="Permalink to this definition">¶</a></dt>
<dd><p>Allows management of Organization policies for a Google Folder. For more information see
<a class="reference external" href="https://cloud.google.com/resource-manager/docs/organization-policy/overview">the official
documentation</a> and
<a class="reference external" href="https://cloud.google.com/resource-manager/reference/rest/v1/folders/setOrgPolicy">API</a>.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>boolean_policy</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A boolean policy is a constraint that is either enforced or not. Structure is documented below.</li>
<li><strong>constraint</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Constraint the Policy is configuring, for example, <code class="docutils literal notranslate"><span class="pre">serviceuser.services</span></code>. Check out the <a class="reference external" href="https://cloud.google.com/resource-manager/docs/organization-policy/understanding-constraints#available_constraints">complete list of available constraints</a>.</li>
<li><strong>folder</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The resource name of the folder to set the policy for. Its format is folders/{folder_id}.</li>
<li><strong>list_policy</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A policy that can define specific values that are allowed or denied for the given constraint. It 
can also be used to allow or deny all values. Structure is documented below.</li>
<li><strong>restore_policy</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A restore policy is a constraint to restore the default policy. Structure is documented below.</li>
<li><strong>version</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – Version of the Policy. Default version is 0.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_gcp.folder.OrganizationPolicy.boolean_policy">
<code class="descname">boolean_policy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.folder.OrganizationPolicy.boolean_policy" title="Permalink to this definition">¶</a></dt>
<dd><p>A boolean policy is a constraint that is either enforced or not. Structure is documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.folder.OrganizationPolicy.constraint">
<code class="descname">constraint</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.folder.OrganizationPolicy.constraint" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Constraint the Policy is configuring, for example, <code class="docutils literal notranslate"><span class="pre">serviceuser.services</span></code>. Check out the <a class="reference external" href="https://cloud.google.com/resource-manager/docs/organization-policy/understanding-constraints#available_constraints">complete list of available constraints</a>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.folder.OrganizationPolicy.etag">
<code class="descname">etag</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.folder.OrganizationPolicy.etag" title="Permalink to this definition">¶</a></dt>
<dd><p>(Computed) The etag of the organization policy. <code class="docutils literal notranslate"><span class="pre">etag</span></code> is used for optimistic concurrency control as a way to help prevent simultaneous updates of a policy from overwriting each other.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.folder.OrganizationPolicy.folder">
<code class="descname">folder</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.folder.OrganizationPolicy.folder" title="Permalink to this definition">¶</a></dt>
<dd><p>The resource name of the folder to set the policy for. Its format is folders/{folder_id}.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.folder.OrganizationPolicy.list_policy">
<code class="descname">list_policy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.folder.OrganizationPolicy.list_policy" title="Permalink to this definition">¶</a></dt>
<dd><p>A policy that can define specific values that are allowed or denied for the given constraint. It 
can also be used to allow or deny all values. Structure is documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.folder.OrganizationPolicy.restore_policy">
<code class="descname">restore_policy</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.folder.OrganizationPolicy.restore_policy" title="Permalink to this definition">¶</a></dt>
<dd><p>A restore policy is a constraint to restore the default policy. Structure is documented below.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.folder.OrganizationPolicy.update_time">
<code class="descname">update_time</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.folder.OrganizationPolicy.update_time" title="Permalink to this definition">¶</a></dt>
<dd><p>(Computed) The timestamp in RFC3339 UTC “Zulu” format, accurate to nanoseconds, representing when the variable was last updated. Example: “2016-10-09T12:33:37.578138407Z”.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.folder.OrganizationPolicy.version">
<code class="descname">version</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.folder.OrganizationPolicy.version" title="Permalink to this definition">¶</a></dt>
<dd><p>Version of the Policy. Default version is 0.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.folder.OrganizationPolicy.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.folder.OrganizationPolicy.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.folder.OrganizationPolicy.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.folder.OrganizationPolicy.translate_input_property" title="Permalink to this definition">¶</a></dt>
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

</div>
