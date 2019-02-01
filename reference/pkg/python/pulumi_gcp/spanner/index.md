<div class="section" id="module-pulumi_gcp.spanner">
<span id="spanner"></span><h1>spanner<a class="headerlink" href="#module-pulumi_gcp.spanner" title="Permalink to this headline">¶</a></h1>
<dl class="class">
<dt id="pulumi_gcp.spanner.Database">
<em class="property">class </em><code class="descclassname">pulumi_gcp.spanner.</code><code class="descname">Database</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>ddls=None</em>, <em>instance=None</em>, <em>name=None</em>, <em>project=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.spanner.Database" title="Permalink to this definition">¶</a></dt>
<dd><p>Creates a Google Spanner Database within a Spanner Instance. For more information, see the [official documentation](<a class="reference external" href="https://cloud.google.com/spanner/">https://cloud.google.com/spanner/</a>), or the [JSON API](<a class="reference external" href="https://cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases">https://cloud.google.com/spanner/docs/reference/rest/v1/projects.instances.databases</a>).</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>ddls</strong> (<em>pulumi.Input</em><em>[</em><em>list</em><em>]</em>) – An optional list of DDL statements to run inside the newly created
database. Statements can create tables, indexes, etc. These statements execute atomically
with the creation of the database: if there is an error in any statement, the database
is not created.</li>
<li><strong>instance</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the instance that will serve the new database.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the database.</li>
<li><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which to look for the <cite>instance</cite> specified. If it
is not provided, the provider project is used.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_gcp.spanner.Database.ddls">
<code class="descname">ddls</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.spanner.Database.ddls" title="Permalink to this definition">¶</a></dt>
<dd><p>An optional list of DDL statements to run inside the newly created
database. Statements can create tables, indexes, etc. These statements execute atomically
with the creation of the database: if there is an error in any statement, the database
is not created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.spanner.Database.instance">
<code class="descname">instance</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.spanner.Database.instance" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the instance that will serve the new database.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.spanner.Database.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.spanner.Database.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the database.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.spanner.Database.project">
<code class="descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.spanner.Database.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which to look for the <cite>instance</cite> specified. If it
is not provided, the provider project is used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.spanner.Database.state">
<code class="descname">state</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.spanner.Database.state" title="Permalink to this definition">¶</a></dt>
<dd><p>The current state of the database.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.spanner.Database.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.spanner.Database.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.spanner.Database.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.spanner.Database.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.spanner.DatabaseIAMBinding">
<em class="property">class </em><code class="descclassname">pulumi_gcp.spanner.</code><code class="descname">DatabaseIAMBinding</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>database=None</em>, <em>instance=None</em>, <em>members=None</em>, <em>project=None</em>, <em>role=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.spanner.DatabaseIAMBinding" title="Permalink to this definition">¶</a></dt>
<dd><p>Three different resources help you manage your IAM policy for a Spanner database. Each of these resources serves a different use case:</p>
<ul class="simple">
<li><cite>google_spanner_database_iam_policy</cite>: Authoritative. Sets the IAM policy for the database and replaces any existing policy already attached.</li>
</ul>
<p>&gt; <strong>Warning:</strong> It’s entirely possibly to lock yourself out of your database using <cite>google_spanner_database_iam_policy</cite>. Any permissions granted by default will be removed unless you include them in your config.</p>
<ul class="simple">
<li><cite>google_spanner_database_iam_binding</cite>: Authoritative for a given role. Updates the IAM policy to grant a role to a list of members. Other roles within the IAM policy for the database are preserved.</li>
<li><cite>google_spanner_database_iam_member</cite>: Non-authoritative. Updates the IAM policy to grant a role to a new member. Other members for the role for the database are preserved.</li>
</ul>
<p>&gt; <strong>Note:</strong> <cite>google_spanner_database_iam_policy</cite> <strong>cannot</strong> be used in conjunction with <cite>google_spanner_database_iam_binding</cite> and <cite>google_spanner_database_iam_member</cite> or they will fight over what your policy should be.</p>
<p>&gt; <strong>Note:</strong> <cite>google_spanner_database_iam_binding</cite> resources <strong>can be</strong> used in conjunction with <cite>google_spanner_database_iam_member</cite> resources <strong>only if</strong> they do not grant privilege to the same role.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>database</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Spanner database.</li>
<li><strong>instance</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Spanner instance the database belongs to.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<p>:param pulumi.Input[list] members
:param pulumi.Input[str] project: The ID of the project in which the resource belongs. If it</p>
<blockquote>
<div>is not provided, the provider project is used.</div></blockquote>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><strong>role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The role that should be applied. Only one
<cite>google_spanner_database_iam_binding</cite> can be used per role. Note that custom roles must be of the format
<cite>[projects|organizations]/{parent-name}/roles/{role-name}</cite>.</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_gcp.spanner.DatabaseIAMBinding.database">
<code class="descname">database</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.spanner.DatabaseIAMBinding.database" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Spanner database.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.spanner.DatabaseIAMBinding.etag">
<code class="descname">etag</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.spanner.DatabaseIAMBinding.etag" title="Permalink to this definition">¶</a></dt>
<dd><p>(Computed) The etag of the database’s IAM policy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.spanner.DatabaseIAMBinding.instance">
<code class="descname">instance</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.spanner.DatabaseIAMBinding.instance" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Spanner instance the database belongs to.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.spanner.DatabaseIAMBinding.project">
<code class="descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.spanner.DatabaseIAMBinding.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.spanner.DatabaseIAMBinding.role">
<code class="descname">role</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.spanner.DatabaseIAMBinding.role" title="Permalink to this definition">¶</a></dt>
<dd><p>The role that should be applied. Only one
<cite>google_spanner_database_iam_binding</cite> can be used per role. Note that custom roles must be of the format
<cite>[projects|organizations]/{parent-name}/roles/{role-name}</cite>.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.spanner.DatabaseIAMBinding.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.spanner.DatabaseIAMBinding.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.spanner.DatabaseIAMBinding.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.spanner.DatabaseIAMBinding.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.spanner.DatabaseIAMMember">
<em class="property">class </em><code class="descclassname">pulumi_gcp.spanner.</code><code class="descname">DatabaseIAMMember</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>database=None</em>, <em>instance=None</em>, <em>member=None</em>, <em>project=None</em>, <em>role=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.spanner.DatabaseIAMMember" title="Permalink to this definition">¶</a></dt>
<dd><p>Three different resources help you manage your IAM policy for a Spanner database. Each of these resources serves a different use case:</p>
<ul class="simple">
<li><cite>google_spanner_database_iam_policy</cite>: Authoritative. Sets the IAM policy for the database and replaces any existing policy already attached.</li>
</ul>
<p>&gt; <strong>Warning:</strong> It’s entirely possibly to lock yourself out of your database using <cite>google_spanner_database_iam_policy</cite>. Any permissions granted by default will be removed unless you include them in your config.</p>
<ul class="simple">
<li><cite>google_spanner_database_iam_binding</cite>: Authoritative for a given role. Updates the IAM policy to grant a role to a list of members. Other roles within the IAM policy for the database are preserved.</li>
<li><cite>google_spanner_database_iam_member</cite>: Non-authoritative. Updates the IAM policy to grant a role to a new member. Other members for the role for the database are preserved.</li>
</ul>
<p>&gt; <strong>Note:</strong> <cite>google_spanner_database_iam_policy</cite> <strong>cannot</strong> be used in conjunction with <cite>google_spanner_database_iam_binding</cite> and <cite>google_spanner_database_iam_member</cite> or they will fight over what your policy should be.</p>
<p>&gt; <strong>Note:</strong> <cite>google_spanner_database_iam_binding</cite> resources <strong>can be</strong> used in conjunction with <cite>google_spanner_database_iam_member</cite> resources <strong>only if</strong> they do not grant privilege to the same role.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>database</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Spanner database.</li>
<li><strong>instance</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Spanner instance the database belongs to.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<p>:param pulumi.Input[str] member
:param pulumi.Input[str] project: The ID of the project in which the resource belongs. If it</p>
<blockquote>
<div>is not provided, the provider project is used.</div></blockquote>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><strong>role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The role that should be applied. Only one
<cite>google_spanner_database_iam_binding</cite> can be used per role. Note that custom roles must be of the format
<cite>[projects|organizations]/{parent-name}/roles/{role-name}</cite>.</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_gcp.spanner.DatabaseIAMMember.database">
<code class="descname">database</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.spanner.DatabaseIAMMember.database" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Spanner database.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.spanner.DatabaseIAMMember.etag">
<code class="descname">etag</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.spanner.DatabaseIAMMember.etag" title="Permalink to this definition">¶</a></dt>
<dd><p>(Computed) The etag of the database’s IAM policy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.spanner.DatabaseIAMMember.instance">
<code class="descname">instance</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.spanner.DatabaseIAMMember.instance" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Spanner instance the database belongs to.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.spanner.DatabaseIAMMember.project">
<code class="descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.spanner.DatabaseIAMMember.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.spanner.DatabaseIAMMember.role">
<code class="descname">role</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.spanner.DatabaseIAMMember.role" title="Permalink to this definition">¶</a></dt>
<dd><p>The role that should be applied. Only one
<cite>google_spanner_database_iam_binding</cite> can be used per role. Note that custom roles must be of the format
<cite>[projects|organizations]/{parent-name}/roles/{role-name}</cite>.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.spanner.DatabaseIAMMember.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.spanner.DatabaseIAMMember.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.spanner.DatabaseIAMMember.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.spanner.DatabaseIAMMember.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.spanner.DatabaseIAMPolicy">
<em class="property">class </em><code class="descclassname">pulumi_gcp.spanner.</code><code class="descname">DatabaseIAMPolicy</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>database=None</em>, <em>instance=None</em>, <em>policy_data=None</em>, <em>project=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.spanner.DatabaseIAMPolicy" title="Permalink to this definition">¶</a></dt>
<dd><p>Three different resources help you manage your IAM policy for a Spanner database. Each of these resources serves a different use case:</p>
<ul class="simple">
<li><cite>google_spanner_database_iam_policy</cite>: Authoritative. Sets the IAM policy for the database and replaces any existing policy already attached.</li>
</ul>
<p>&gt; <strong>Warning:</strong> It’s entirely possibly to lock yourself out of your database using <cite>google_spanner_database_iam_policy</cite>. Any permissions granted by default will be removed unless you include them in your config.</p>
<ul class="simple">
<li><cite>google_spanner_database_iam_binding</cite>: Authoritative for a given role. Updates the IAM policy to grant a role to a list of members. Other roles within the IAM policy for the database are preserved.</li>
<li><cite>google_spanner_database_iam_member</cite>: Non-authoritative. Updates the IAM policy to grant a role to a new member. Other members for the role for the database are preserved.</li>
</ul>
<p>&gt; <strong>Note:</strong> <cite>google_spanner_database_iam_policy</cite> <strong>cannot</strong> be used in conjunction with <cite>google_spanner_database_iam_binding</cite> and <cite>google_spanner_database_iam_member</cite> or they will fight over what your policy should be.</p>
<p>&gt; <strong>Note:</strong> <cite>google_spanner_database_iam_binding</cite> resources <strong>can be</strong> used in conjunction with <cite>google_spanner_database_iam_member</cite> resources <strong>only if</strong> they do not grant privilege to the same role.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>database</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Spanner database.</li>
<li><strong>instance</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the Spanner instance the database belongs to.</li>
<li><strong>policy_data</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The policy data generated by
a <cite>google_iam_policy</cite> data source.</li>
<li><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_gcp.spanner.DatabaseIAMPolicy.database">
<code class="descname">database</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.spanner.DatabaseIAMPolicy.database" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Spanner database.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.spanner.DatabaseIAMPolicy.etag">
<code class="descname">etag</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.spanner.DatabaseIAMPolicy.etag" title="Permalink to this definition">¶</a></dt>
<dd><p>(Computed) The etag of the database’s IAM policy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.spanner.DatabaseIAMPolicy.instance">
<code class="descname">instance</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.spanner.DatabaseIAMPolicy.instance" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the Spanner instance the database belongs to.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.spanner.DatabaseIAMPolicy.policy_data">
<code class="descname">policy_data</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.spanner.DatabaseIAMPolicy.policy_data" title="Permalink to this definition">¶</a></dt>
<dd><p>The policy data generated by
a <cite>google_iam_policy</cite> data source.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.spanner.DatabaseIAMPolicy.project">
<code class="descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.spanner.DatabaseIAMPolicy.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.spanner.DatabaseIAMPolicy.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.spanner.DatabaseIAMPolicy.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.spanner.DatabaseIAMPolicy.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.spanner.DatabaseIAMPolicy.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.spanner.Instance">
<em class="property">class </em><code class="descclassname">pulumi_gcp.spanner.</code><code class="descname">Instance</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>config=None</em>, <em>display_name=None</em>, <em>labels=None</em>, <em>name=None</em>, <em>num_nodes=None</em>, <em>project=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.spanner.Instance" title="Permalink to this definition">¶</a></dt>
<dd><p>Creates and manages a Google Spanner Instance. For more information, see the [official documentation](<a class="reference external" href="https://cloud.google.com/spanner/">https://cloud.google.com/spanner/</a>), or the [JSON API](<a class="reference external" href="https://cloud.google.com/spanner/docs/reference/rest/v1/projects.instances">https://cloud.google.com/spanner/docs/reference/rest/v1/projects.instances</a>).</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>config</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the instance’s configuration (similar but not
quite the same as a region) which defines defines the geographic placement and
replication of your databases in this instance. It determines where your data
is stored. Values are typically of the form <cite>regional-europe-west1</cite> , <cite>us-central</cite> etc.
In order to obtain a valid list please consult the
[Configuration section of the docs](<a class="reference external" href="https://cloud.google.com/spanner/docs/instances">https://cloud.google.com/spanner/docs/instances</a>).</li>
<li><strong>display_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The descriptive name for this instance as it appears
in UIs. Can be updated, however should be kept globally unique to avoid confusion.</li>
<li><strong>labels</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – A mapping (key/value pairs) of labels to assign to the instance.</li>
<li><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique name (ID) of the instance. If the name is left
blank, Terraform will randomly generate one when the instance is first
created.</li>
<li><strong>num_nodes</strong> (<em>pulumi.Input</em><em>[</em><em>int</em><em>]</em>) – The number of nodes allocated to this instance.
Defaults to <cite>1</cite>. This can be updated after creation.</li>
<li><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_gcp.spanner.Instance.config">
<code class="descname">config</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.spanner.Instance.config" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the instance’s configuration (similar but not
quite the same as a region) which defines defines the geographic placement and
replication of your databases in this instance. It determines where your data
is stored. Values are typically of the form <cite>regional-europe-west1</cite> , <cite>us-central</cite> etc.
In order to obtain a valid list please consult the
[Configuration section of the docs](<a class="reference external" href="https://cloud.google.com/spanner/docs/instances">https://cloud.google.com/spanner/docs/instances</a>).</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.spanner.Instance.display_name">
<code class="descname">display_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.spanner.Instance.display_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The descriptive name for this instance as it appears
in UIs. Can be updated, however should be kept globally unique to avoid confusion.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.spanner.Instance.labels">
<code class="descname">labels</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.spanner.Instance.labels" title="Permalink to this definition">¶</a></dt>
<dd><p>A mapping (key/value pairs) of labels to assign to the instance.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.spanner.Instance.name">
<code class="descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.spanner.Instance.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The unique name (ID) of the instance. If the name is left
blank, Terraform will randomly generate one when the instance is first
created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.spanner.Instance.num_nodes">
<code class="descname">num_nodes</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.spanner.Instance.num_nodes" title="Permalink to this definition">¶</a></dt>
<dd><p>The number of nodes allocated to this instance.
Defaults to <cite>1</cite>. This can be updated after creation.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.spanner.Instance.project">
<code class="descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.spanner.Instance.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.spanner.Instance.state">
<code class="descname">state</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.spanner.Instance.state" title="Permalink to this definition">¶</a></dt>
<dd><p>The current state of the instance.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.spanner.Instance.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.spanner.Instance.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.spanner.Instance.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.spanner.Instance.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.spanner.InstanceIAMBinding">
<em class="property">class </em><code class="descclassname">pulumi_gcp.spanner.</code><code class="descname">InstanceIAMBinding</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>instance=None</em>, <em>members=None</em>, <em>project=None</em>, <em>role=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.spanner.InstanceIAMBinding" title="Permalink to this definition">¶</a></dt>
<dd><p>Three different resources help you manage your IAM policy for a Spanner instance. Each of these resources serves a different use case:</p>
<ul class="simple">
<li><cite>google_spanner_instance_iam_policy</cite>: Authoritative. Sets the IAM policy for the instance and replaces any existing policy already attached.</li>
</ul>
<p>&gt; <strong>Warning:</strong> It’s entirely possibly to lock yourself out of your instance using <cite>google_spanner_instance_iam_policy</cite>. Any permissions granted by default will be removed unless you include them in your config.</p>
<ul class="simple">
<li><cite>google_spanner_instance_iam_binding</cite>: Authoritative for a given role. Updates the IAM policy to grant a role to a list of members. Other roles within the IAM policy for the instance are preserved.</li>
<li><cite>google_spanner_instance_iam_member</cite>: Non-authoritative. Updates the IAM policy to grant a role to a new member. Other members for the role for the instance are preserved.</li>
</ul>
<p>&gt; <strong>Note:</strong> <cite>google_spanner_instance_iam_policy</cite> <strong>cannot</strong> be used in conjunction with <cite>google_spanner_instance_iam_binding</cite> and <cite>google_spanner_instance_iam_member</cite> or they will fight over what your policy should be.</p>
<p>&gt; <strong>Note:</strong> <cite>google_spanner_instance_iam_binding</cite> resources <strong>can be</strong> used in conjunction with <cite>google_spanner_instance_iam_member</cite> resources <strong>only if</strong> they do not grant privilege to the same role.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>instance</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the instance.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<p>:param pulumi.Input[list] members
:param pulumi.Input[str] project: The ID of the project in which the resource belongs. If it</p>
<blockquote>
<div>is not provided, the provider project is used.</div></blockquote>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><strong>role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The role that should be applied. Only one
<cite>google_spanner_instance_iam_binding</cite> can be used per role. Note that custom roles must be of the format
<cite>[projects|organizations]/{parent-name}/roles/{role-name}</cite>.</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_gcp.spanner.InstanceIAMBinding.etag">
<code class="descname">etag</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.spanner.InstanceIAMBinding.etag" title="Permalink to this definition">¶</a></dt>
<dd><p>(Computed) The etag of the instance’s IAM policy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.spanner.InstanceIAMBinding.instance">
<code class="descname">instance</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.spanner.InstanceIAMBinding.instance" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the instance.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.spanner.InstanceIAMBinding.project">
<code class="descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.spanner.InstanceIAMBinding.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.spanner.InstanceIAMBinding.role">
<code class="descname">role</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.spanner.InstanceIAMBinding.role" title="Permalink to this definition">¶</a></dt>
<dd><p>The role that should be applied. Only one
<cite>google_spanner_instance_iam_binding</cite> can be used per role. Note that custom roles must be of the format
<cite>[projects|organizations]/{parent-name}/roles/{role-name}</cite>.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.spanner.InstanceIAMBinding.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.spanner.InstanceIAMBinding.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.spanner.InstanceIAMBinding.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.spanner.InstanceIAMBinding.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.spanner.InstanceIAMMember">
<em class="property">class </em><code class="descclassname">pulumi_gcp.spanner.</code><code class="descname">InstanceIAMMember</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>instance=None</em>, <em>member=None</em>, <em>project=None</em>, <em>role=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.spanner.InstanceIAMMember" title="Permalink to this definition">¶</a></dt>
<dd><p>Three different resources help you manage your IAM policy for a Spanner instance. Each of these resources serves a different use case:</p>
<ul class="simple">
<li><cite>google_spanner_instance_iam_policy</cite>: Authoritative. Sets the IAM policy for the instance and replaces any existing policy already attached.</li>
</ul>
<p>&gt; <strong>Warning:</strong> It’s entirely possibly to lock yourself out of your instance using <cite>google_spanner_instance_iam_policy</cite>. Any permissions granted by default will be removed unless you include them in your config.</p>
<ul class="simple">
<li><cite>google_spanner_instance_iam_binding</cite>: Authoritative for a given role. Updates the IAM policy to grant a role to a list of members. Other roles within the IAM policy for the instance are preserved.</li>
<li><cite>google_spanner_instance_iam_member</cite>: Non-authoritative. Updates the IAM policy to grant a role to a new member. Other members for the role for the instance are preserved.</li>
</ul>
<p>&gt; <strong>Note:</strong> <cite>google_spanner_instance_iam_policy</cite> <strong>cannot</strong> be used in conjunction with <cite>google_spanner_instance_iam_binding</cite> and <cite>google_spanner_instance_iam_member</cite> or they will fight over what your policy should be.</p>
<p>&gt; <strong>Note:</strong> <cite>google_spanner_instance_iam_binding</cite> resources <strong>can be</strong> used in conjunction with <cite>google_spanner_instance_iam_member</cite> resources <strong>only if</strong> they do not grant privilege to the same role.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>instance</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the instance.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<p>:param pulumi.Input[str] member
:param pulumi.Input[str] project: The ID of the project in which the resource belongs. If it</p>
<blockquote>
<div>is not provided, the provider project is used.</div></blockquote>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><strong>role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The role that should be applied. Only one
<cite>google_spanner_instance_iam_binding</cite> can be used per role. Note that custom roles must be of the format
<cite>[projects|organizations]/{parent-name}/roles/{role-name}</cite>.</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_gcp.spanner.InstanceIAMMember.etag">
<code class="descname">etag</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.spanner.InstanceIAMMember.etag" title="Permalink to this definition">¶</a></dt>
<dd><p>(Computed) The etag of the instance’s IAM policy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.spanner.InstanceIAMMember.instance">
<code class="descname">instance</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.spanner.InstanceIAMMember.instance" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the instance.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.spanner.InstanceIAMMember.project">
<code class="descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.spanner.InstanceIAMMember.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.spanner.InstanceIAMMember.role">
<code class="descname">role</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.spanner.InstanceIAMMember.role" title="Permalink to this definition">¶</a></dt>
<dd><p>The role that should be applied. Only one
<cite>google_spanner_instance_iam_binding</cite> can be used per role. Note that custom roles must be of the format
<cite>[projects|organizations]/{parent-name}/roles/{role-name}</cite>.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.spanner.InstanceIAMMember.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.spanner.InstanceIAMMember.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.spanner.InstanceIAMMember.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.spanner.InstanceIAMMember.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.spanner.InstanceIAMPolicy">
<em class="property">class </em><code class="descclassname">pulumi_gcp.spanner.</code><code class="descname">InstanceIAMPolicy</code><span class="sig-paren">(</span><em>__name__</em>, <em>__opts__=None</em>, <em>instance=None</em>, <em>policy_data=None</em>, <em>project=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.spanner.InstanceIAMPolicy" title="Permalink to this definition">¶</a></dt>
<dd><p>Three different resources help you manage your IAM policy for a Spanner instance. Each of these resources serves a different use case:</p>
<ul class="simple">
<li><cite>google_spanner_instance_iam_policy</cite>: Authoritative. Sets the IAM policy for the instance and replaces any existing policy already attached.</li>
</ul>
<p>&gt; <strong>Warning:</strong> It’s entirely possibly to lock yourself out of your instance using <cite>google_spanner_instance_iam_policy</cite>. Any permissions granted by default will be removed unless you include them in your config.</p>
<ul class="simple">
<li><cite>google_spanner_instance_iam_binding</cite>: Authoritative for a given role. Updates the IAM policy to grant a role to a list of members. Other roles within the IAM policy for the instance are preserved.</li>
<li><cite>google_spanner_instance_iam_member</cite>: Non-authoritative. Updates the IAM policy to grant a role to a new member. Other members for the role for the instance are preserved.</li>
</ul>
<p>&gt; <strong>Note:</strong> <cite>google_spanner_instance_iam_policy</cite> <strong>cannot</strong> be used in conjunction with <cite>google_spanner_instance_iam_binding</cite> and <cite>google_spanner_instance_iam_member</cite> or they will fight over what your policy should be.</p>
<p>&gt; <strong>Note:</strong> <cite>google_spanner_instance_iam_binding</cite> resources <strong>can be</strong> used in conjunction with <cite>google_spanner_instance_iam_member</cite> resources <strong>only if</strong> they do not grant privilege to the same role.</p>
<table class="docutils field-list" frame="void" rules="none">
<col class="field-name" />
<col class="field-body" />
<tbody valign="top">
<tr class="field-odd field"><th class="field-name">Parameters:</th><td class="field-body"><ul class="first last simple">
<li><strong>__name__</strong> (<em>str</em>) – The name of the resource.</li>
<li><strong>__opts__</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</li>
<li><strong>instance</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name of the instance.</li>
<li><strong>policy_data</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The policy data generated by
a <cite>google_iam_policy</cite> data source.</li>
<li><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.</li>
</ul>
</td>
</tr>
</tbody>
</table>
<dl class="attribute">
<dt id="pulumi_gcp.spanner.InstanceIAMPolicy.etag">
<code class="descname">etag</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.spanner.InstanceIAMPolicy.etag" title="Permalink to this definition">¶</a></dt>
<dd><p>(Computed) The etag of the instance’s IAM policy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.spanner.InstanceIAMPolicy.instance">
<code class="descname">instance</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.spanner.InstanceIAMPolicy.instance" title="Permalink to this definition">¶</a></dt>
<dd><p>The name of the instance.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.spanner.InstanceIAMPolicy.policy_data">
<code class="descname">policy_data</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.spanner.InstanceIAMPolicy.policy_data" title="Permalink to this definition">¶</a></dt>
<dd><p>The policy data generated by
a <cite>google_iam_policy</cite> data source.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.spanner.InstanceIAMPolicy.project">
<code class="descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.spanner.InstanceIAMPolicy.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project in which the resource belongs. If it
is not provided, the provider project is used.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.spanner.InstanceIAMPolicy.translate_output_property">
<code class="descname">translate_output_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.spanner.InstanceIAMPolicy.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.spanner.InstanceIAMPolicy.translate_input_property">
<code class="descname">translate_input_property</code><span class="sig-paren">(</span><em>prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.spanner.InstanceIAMPolicy.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
