---
title: Module service_account
title_tag: Module service_account | Package pulumi_gcp | Python SDK
linktitle: service_account
notitle: true
---

<div class="section" id="service-account">
<h1>service_account<a class="headerlink" href="#service-account" title="Permalink to this headline">¶</a></h1>
<blockquote>
<div><p>This provider is a derived work of the <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google">Terraform Provider</a> distributed under
<a class="reference external" href="https://www.mozilla.org/en-US/MPL/2.0/">MPL 2.0</a>. If you encounter a bug or missing feature, first check the
<a class="reference external" href="https://github.com/pulumi/pulumi-gcp/issues">pulumi/pulumi-gcp repo</a>; however, if that doesn’t turn up
anything, please consult the source <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/issues">terraform-providers/terraform-provider-google repo</a>.</p>
</div></blockquote>
<span class="target" id="module-pulumi_gcp.service_account"></span><dl class="class">
<dt id="pulumi_gcp.service_account.Account">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.service_account.</code><code class="sig-name descname">Account</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">account_id=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">display_name=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.service_account.Account" title="Permalink to this definition">¶</a></dt>
<dd><p>Allows management of a <a class="reference external" href="https://cloud.google.com/compute/docs/access/service-accounts">Google Cloud Platform service account</a></p>
<blockquote>
<div><p>Creation of service accounts is eventually consistent, and that can lead to
errors when you try to apply ACLs to service accounts immediately after
creation.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>account_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The account id that is used to generate the service
account email address and a stable unique id. It is unique within a project,
must be 6-30 characters long, and match the regular expression <code class="docutils literal notranslate"><span class="pre">a-z</span></code>
to comply with RFC1035. Changing this forces a new service account to be created.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A text description of the service account.
Must be less than or equal to 256 UTF-8 bytes.</p></li>
<li><p><strong>display_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The display name for the service account.
Can be updated without creating a new resource.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project that the service account will be created in.
Defaults to the provider project configuration.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/service_account.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/service_account.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_gcp.service_account.Account.account_id">
<code class="sig-name descname">account_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.service_account.Account.account_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The account id that is used to generate the service
account email address and a stable unique id. It is unique within a project,
must be 6-30 characters long, and match the regular expression <code class="docutils literal notranslate"><span class="pre">a-z</span></code>
to comply with RFC1035. Changing this forces a new service account to be created.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.service_account.Account.description">
<code class="sig-name descname">description</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.service_account.Account.description" title="Permalink to this definition">¶</a></dt>
<dd><p>A text description of the service account.
Must be less than or equal to 256 UTF-8 bytes.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.service_account.Account.display_name">
<code class="sig-name descname">display_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.service_account.Account.display_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The display name for the service account.
Can be updated without creating a new resource.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.service_account.Account.email">
<code class="sig-name descname">email</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.service_account.Account.email" title="Permalink to this definition">¶</a></dt>
<dd><p>The e-mail address of the service account. This value
should be referenced from any <code class="docutils literal notranslate"><span class="pre">organizations.getIAMPolicy</span></code> data sources
that would grant the service account privileges.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.service_account.Account.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.service_account.Account.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The fully-qualified name of the service account.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.service_account.Account.project">
<code class="sig-name descname">project</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.service_account.Account.project" title="Permalink to this definition">¶</a></dt>
<dd><p>The ID of the project that the service account will be created in.
Defaults to the provider project configuration.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.service_account.Account.unique_id">
<code class="sig-name descname">unique_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.service_account.Account.unique_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The unique id of the service account.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.service_account.Account.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">account_id=None</em>, <em class="sig-param">description=None</em>, <em class="sig-param">display_name=None</em>, <em class="sig-param">email=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">unique_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.service_account.Account.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Account resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>account_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The account id that is used to generate the service
account email address and a stable unique id. It is unique within a project,
must be 6-30 characters long, and match the regular expression <code class="docutils literal notranslate"><span class="pre">a-z</span></code>
to comply with RFC1035. Changing this forces a new service account to be created.</p></li>
<li><p><strong>description</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – A text description of the service account.
Must be less than or equal to 256 UTF-8 bytes.</p></li>
<li><p><strong>display_name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The display name for the service account.
Can be updated without creating a new resource.</p></li>
<li><p><strong>email</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The e-mail address of the service account. This value
should be referenced from any <code class="docutils literal notranslate"><span class="pre">organizations.getIAMPolicy</span></code> data sources
that would grant the service account privileges.</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The fully-qualified name of the service account.</p></li>
<li><p><strong>project</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The ID of the project that the service account will be created in.
Defaults to the provider project configuration.</p></li>
<li><p><strong>unique_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The unique id of the service account.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/service_account.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/service_account.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.service_account.Account.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.service_account.Account.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.service_account.Account.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.service_account.Account.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.service_account.AwaitableGetAccountAccessTokenResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.service_account.</code><code class="sig-name descname">AwaitableGetAccountAccessTokenResult</code><span class="sig-paren">(</span><em class="sig-param">access_token=None</em>, <em class="sig-param">delegates=None</em>, <em class="sig-param">lifetime=None</em>, <em class="sig-param">scopes=None</em>, <em class="sig-param">target_service_account=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.service_account.AwaitableGetAccountAccessTokenResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_gcp.service_account.AwaitableGetAccountKeyResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.service_account.</code><code class="sig-name descname">AwaitableGetAccountKeyResult</code><span class="sig-paren">(</span><em class="sig-param">key_algorithm=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">public_key=None</em>, <em class="sig-param">public_key_type=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.service_account.AwaitableGetAccountKeyResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_gcp.service_account.AwaitableGetAccountResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.service_account.</code><code class="sig-name descname">AwaitableGetAccountResult</code><span class="sig-paren">(</span><em class="sig-param">account_id=None</em>, <em class="sig-param">display_name=None</em>, <em class="sig-param">email=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">unique_id=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.service_account.AwaitableGetAccountResult" title="Permalink to this definition">¶</a></dt>
<dd></dd></dl>

<dl class="class">
<dt id="pulumi_gcp.service_account.GetAccountAccessTokenResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.service_account.</code><code class="sig-name descname">GetAccountAccessTokenResult</code><span class="sig-paren">(</span><em class="sig-param">access_token=None</em>, <em class="sig-param">delegates=None</em>, <em class="sig-param">lifetime=None</em>, <em class="sig-param">scopes=None</em>, <em class="sig-param">target_service_account=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.service_account.GetAccountAccessTokenResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getAccountAccessToken.</p>
<dl class="attribute">
<dt id="pulumi_gcp.service_account.GetAccountAccessTokenResult.access_token">
<code class="sig-name descname">access_token</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.service_account.GetAccountAccessTokenResult.access_token" title="Permalink to this definition">¶</a></dt>
<dd><p>The <code class="docutils literal notranslate"><span class="pre">access_token</span></code> representing the new generated identity.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.service_account.GetAccountAccessTokenResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.service_account.GetAccountAccessTokenResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_gcp.service_account.GetAccountKeyResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.service_account.</code><code class="sig-name descname">GetAccountKeyResult</code><span class="sig-paren">(</span><em class="sig-param">key_algorithm=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">public_key=None</em>, <em class="sig-param">public_key_type=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.service_account.GetAccountKeyResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getAccountKey.</p>
<dl class="attribute">
<dt id="pulumi_gcp.service_account.GetAccountKeyResult.public_key">
<code class="sig-name descname">public_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.service_account.GetAccountKeyResult.public_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The public key, base64 encoded</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.service_account.GetAccountKeyResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.service_account.GetAccountKeyResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_gcp.service_account.GetAccountResult">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.service_account.</code><code class="sig-name descname">GetAccountResult</code><span class="sig-paren">(</span><em class="sig-param">account_id=None</em>, <em class="sig-param">display_name=None</em>, <em class="sig-param">email=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">unique_id=None</em>, <em class="sig-param">id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.service_account.GetAccountResult" title="Permalink to this definition">¶</a></dt>
<dd><p>A collection of values returned by getAccount.</p>
<dl class="attribute">
<dt id="pulumi_gcp.service_account.GetAccountResult.display_name">
<code class="sig-name descname">display_name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.service_account.GetAccountResult.display_name" title="Permalink to this definition">¶</a></dt>
<dd><p>The display name for the service account.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.service_account.GetAccountResult.email">
<code class="sig-name descname">email</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.service_account.GetAccountResult.email" title="Permalink to this definition">¶</a></dt>
<dd><p>The e-mail address of the service account. This value
should be referenced from any <code class="docutils literal notranslate"><span class="pre">organizations.getIAMPolicy</span></code> data sources
that would grant the service account privileges.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.service_account.GetAccountResult.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.service_account.GetAccountResult.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The fully-qualified name of the service account.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.service_account.GetAccountResult.unique_id">
<code class="sig-name descname">unique_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.service_account.GetAccountResult.unique_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The unique id of the service account.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.service_account.GetAccountResult.id">
<code class="sig-name descname">id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.service_account.GetAccountResult.id" title="Permalink to this definition">¶</a></dt>
<dd><p>id is the provider-assigned unique ID for this managed resource.</p>
</dd></dl>

</dd></dl>

<dl class="class">
<dt id="pulumi_gcp.service_account.IAMBinding">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.service_account.</code><code class="sig-name descname">IAMBinding</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">condition=None</em>, <em class="sig-param">members=None</em>, <em class="sig-param">role=None</em>, <em class="sig-param">service_account_id=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.service_account.IAMBinding" title="Permalink to this definition">¶</a></dt>
<dd><p>When managing IAM roles, you can treat a service account either as a resource or as an identity. This resource is to add iam policy bindings to a service account resource <strong>to configure permissions for who can edit the service account</strong>. To configure permissions for a service account to act as an identity that can manage other GCP resources, use the google_project_iam set of resources.</p>
<p>Three different resources help you manage your IAM policy for a service account. Each of these resources serves a different use case:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">serviceAccount.IAMPolicy</span></code>: Authoritative. Sets the IAM policy for the service account and replaces any existing policy already attached.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">serviceAccount.IAMBinding</span></code>: Authoritative for a given role. Updates the IAM policy to grant a role to a list of members. Other roles within the IAM policy for the service account are preserved.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">serviceAccount.IAMMember</span></code>: Non-authoritative. Updates the IAM policy to grant a role to a new member. Other members for the role for the service account are preserved.</p></li>
</ul>
<blockquote>
<div><p><strong>Note:</strong> <code class="docutils literal notranslate"><span class="pre">serviceAccount.IAMPolicy</span></code> <strong>cannot</strong> be used in conjunction with <code class="docutils literal notranslate"><span class="pre">serviceAccount.IAMBinding</span></code> and <code class="docutils literal notranslate"><span class="pre">serviceAccount.IAMMember</span></code> or they will fight over what your policy should be.</p>
<p><strong>Note:</strong> <code class="docutils literal notranslate"><span class="pre">serviceAccount.IAMBinding</span></code> resources <strong>can be</strong> used in conjunction with <code class="docutils literal notranslate"><span class="pre">serviceAccount.IAMMember</span></code> resources <strong>only if</strong> they do not grant privilege to the same role.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>condition</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – ) An <a class="reference external" href="https://cloud.google.com/iam/docs/conditions-overview">IAM Condition</a> for a given binding.
Structure is documented below.</p></li>
<li><p><strong>role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The role that should be applied. Only one
<code class="docutils literal notranslate"><span class="pre">serviceAccount.IAMBinding</span></code> can be used per role. Note that custom roles must be of the format
<code class="docutils literal notranslate"><span class="pre">[projects|organizations]/{parent-name}/roles/{role-name}</span></code>.</p></li>
<li><p><strong>service_account_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The fully-qualified name of the service account to apply policy to.</p></li>
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
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/service_account_iam_binding.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/service_account_iam_binding.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_gcp.service_account.IAMBinding.condition">
<code class="sig-name descname">condition</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.service_account.IAMBinding.condition" title="Permalink to this definition">¶</a></dt>
<dd><p>) An <a class="reference external" href="https://cloud.google.com/iam/docs/conditions-overview">IAM Condition</a> for a given binding.
Structure is documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">description</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">expression</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">title</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.service_account.IAMBinding.etag">
<code class="sig-name descname">etag</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.service_account.IAMBinding.etag" title="Permalink to this definition">¶</a></dt>
<dd><p>(Computed) The etag of the service account IAM policy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.service_account.IAMBinding.role">
<code class="sig-name descname">role</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.service_account.IAMBinding.role" title="Permalink to this definition">¶</a></dt>
<dd><p>The role that should be applied. Only one
<code class="docutils literal notranslate"><span class="pre">serviceAccount.IAMBinding</span></code> can be used per role. Note that custom roles must be of the format
<code class="docutils literal notranslate"><span class="pre">[projects|organizations]/{parent-name}/roles/{role-name}</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.service_account.IAMBinding.service_account_id">
<code class="sig-name descname">service_account_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.service_account.IAMBinding.service_account_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The fully-qualified name of the service account to apply policy to.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.service_account.IAMBinding.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">condition=None</em>, <em class="sig-param">etag=None</em>, <em class="sig-param">members=None</em>, <em class="sig-param">role=None</em>, <em class="sig-param">service_account_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.service_account.IAMBinding.get" title="Permalink to this definition">¶</a></dt>
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
<li><p><strong>etag</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – (Computed) The etag of the service account IAM policy.</p></li>
<li><p><strong>role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The role that should be applied. Only one
<code class="docutils literal notranslate"><span class="pre">serviceAccount.IAMBinding</span></code> can be used per role. Note that custom roles must be of the format
<code class="docutils literal notranslate"><span class="pre">[projects|organizations]/{parent-name}/roles/{role-name}</span></code>.</p></li>
<li><p><strong>service_account_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The fully-qualified name of the service account to apply policy to.</p></li>
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
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/service_account_iam_binding.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/service_account_iam_binding.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.service_account.IAMBinding.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.service_account.IAMBinding.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.service_account.IAMBinding.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.service_account.IAMBinding.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.service_account.IAMMember">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.service_account.</code><code class="sig-name descname">IAMMember</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">condition=None</em>, <em class="sig-param">member=None</em>, <em class="sig-param">role=None</em>, <em class="sig-param">service_account_id=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.service_account.IAMMember" title="Permalink to this definition">¶</a></dt>
<dd><p>When managing IAM roles, you can treat a service account either as a resource or as an identity. This resource is to add iam policy bindings to a service account resource <strong>to configure permissions for who can edit the service account</strong>. To configure permissions for a service account to act as an identity that can manage other GCP resources, use the google_project_iam set of resources.</p>
<p>Three different resources help you manage your IAM policy for a service account. Each of these resources serves a different use case:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">serviceAccount.IAMPolicy</span></code>: Authoritative. Sets the IAM policy for the service account and replaces any existing policy already attached.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">serviceAccount.IAMBinding</span></code>: Authoritative for a given role. Updates the IAM policy to grant a role to a list of members. Other roles within the IAM policy for the service account are preserved.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">serviceAccount.IAMMember</span></code>: Non-authoritative. Updates the IAM policy to grant a role to a new member. Other members for the role for the service account are preserved.</p></li>
</ul>
<blockquote>
<div><p><strong>Note:</strong> <code class="docutils literal notranslate"><span class="pre">serviceAccount.IAMPolicy</span></code> <strong>cannot</strong> be used in conjunction with <code class="docutils literal notranslate"><span class="pre">serviceAccount.IAMBinding</span></code> and <code class="docutils literal notranslate"><span class="pre">serviceAccount.IAMMember</span></code> or they will fight over what your policy should be.</p>
<p><strong>Note:</strong> <code class="docutils literal notranslate"><span class="pre">serviceAccount.IAMBinding</span></code> resources <strong>can be</strong> used in conjunction with <code class="docutils literal notranslate"><span class="pre">serviceAccount.IAMMember</span></code> resources <strong>only if</strong> they do not grant privilege to the same role.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>condition</strong> (<em>pulumi.Input</em><em>[</em><em>dict</em><em>]</em>) – <p>) An <a class="reference external" href="https://cloud.google.com/iam/docs/conditions-overview">IAM Condition</a> for a given binding.
Structure is documented below.</p>
</p></li>
<li><p><strong>role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The role that should be applied. Only one
<code class="docutils literal notranslate"><span class="pre">serviceAccount.IAMBinding</span></code> can be used per role. Note that custom roles must be of the format
<code class="docutils literal notranslate"><span class="pre">[projects|organizations]/{parent-name}/roles/{role-name}</span></code>.</p></li>
<li><p><strong>service_account_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The fully-qualified name of the service account to apply policy to.</p></li>
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
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/service_account_iam_member.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/service_account_iam_member.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_gcp.service_account.IAMMember.condition">
<code class="sig-name descname">condition</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.service_account.IAMMember.condition" title="Permalink to this definition">¶</a></dt>
<dd><p>) An <a class="reference external" href="https://cloud.google.com/iam/docs/conditions-overview">IAM Condition</a> for a given binding.
Structure is documented below.</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">description</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">expression</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">title</span></code> (<code class="docutils literal notranslate"><span class="pre">str</span></code>)</p></li>
</ul>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.service_account.IAMMember.etag">
<code class="sig-name descname">etag</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.service_account.IAMMember.etag" title="Permalink to this definition">¶</a></dt>
<dd><p>(Computed) The etag of the service account IAM policy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.service_account.IAMMember.role">
<code class="sig-name descname">role</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.service_account.IAMMember.role" title="Permalink to this definition">¶</a></dt>
<dd><p>The role that should be applied. Only one
<code class="docutils literal notranslate"><span class="pre">serviceAccount.IAMBinding</span></code> can be used per role. Note that custom roles must be of the format
<code class="docutils literal notranslate"><span class="pre">[projects|organizations]/{parent-name}/roles/{role-name}</span></code>.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.service_account.IAMMember.service_account_id">
<code class="sig-name descname">service_account_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.service_account.IAMMember.service_account_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The fully-qualified name of the service account to apply policy to.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.service_account.IAMMember.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">condition=None</em>, <em class="sig-param">etag=None</em>, <em class="sig-param">member=None</em>, <em class="sig-param">role=None</em>, <em class="sig-param">service_account_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.service_account.IAMMember.get" title="Permalink to this definition">¶</a></dt>
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
<li><p><strong>etag</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – (Computed) The etag of the service account IAM policy.</p></li>
<li><p><strong>role</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The role that should be applied. Only one
<code class="docutils literal notranslate"><span class="pre">serviceAccount.IAMBinding</span></code> can be used per role. Note that custom roles must be of the format
<code class="docutils literal notranslate"><span class="pre">[projects|organizations]/{parent-name}/roles/{role-name}</span></code>.</p></li>
<li><p><strong>service_account_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The fully-qualified name of the service account to apply policy to.</p></li>
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
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/service_account_iam_member.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/service_account_iam_member.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.service_account.IAMMember.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.service_account.IAMMember.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.service_account.IAMMember.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.service_account.IAMMember.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.service_account.IAMPolicy">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.service_account.</code><code class="sig-name descname">IAMPolicy</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">policy_data=None</em>, <em class="sig-param">service_account_id=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.service_account.IAMPolicy" title="Permalink to this definition">¶</a></dt>
<dd><p>When managing IAM roles, you can treat a service account either as a resource or as an identity. This resource is to add iam policy bindings to a service account resource <strong>to configure permissions for who can edit the service account</strong>. To configure permissions for a service account to act as an identity that can manage other GCP resources, use the google_project_iam set of resources.</p>
<p>Three different resources help you manage your IAM policy for a service account. Each of these resources serves a different use case:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">serviceAccount.IAMPolicy</span></code>: Authoritative. Sets the IAM policy for the service account and replaces any existing policy already attached.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">serviceAccount.IAMBinding</span></code>: Authoritative for a given role. Updates the IAM policy to grant a role to a list of members. Other roles within the IAM policy for the service account are preserved.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">serviceAccount.IAMMember</span></code>: Non-authoritative. Updates the IAM policy to grant a role to a new member. Other members for the role for the service account are preserved.</p></li>
</ul>
<blockquote>
<div><p><strong>Note:</strong> <code class="docutils literal notranslate"><span class="pre">serviceAccount.IAMPolicy</span></code> <strong>cannot</strong> be used in conjunction with <code class="docutils literal notranslate"><span class="pre">serviceAccount.IAMBinding</span></code> and <code class="docutils literal notranslate"><span class="pre">serviceAccount.IAMMember</span></code> or they will fight over what your policy should be.</p>
<p><strong>Note:</strong> <code class="docutils literal notranslate"><span class="pre">serviceAccount.IAMBinding</span></code> resources <strong>can be</strong> used in conjunction with <code class="docutils literal notranslate"><span class="pre">serviceAccount.IAMMember</span></code> resources <strong>only if</strong> they do not grant privilege to the same role.</p>
</div></blockquote>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>policy_data</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The policy data generated by
a <code class="docutils literal notranslate"><span class="pre">organizations.getIAMPolicy</span></code> data source.</p></li>
<li><p><strong>service_account_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The fully-qualified name of the service account to apply policy to.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/service_account_iam_policy.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/service_account_iam_policy.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_gcp.service_account.IAMPolicy.etag">
<code class="sig-name descname">etag</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.service_account.IAMPolicy.etag" title="Permalink to this definition">¶</a></dt>
<dd><p>(Computed) The etag of the service account IAM policy.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.service_account.IAMPolicy.policy_data">
<code class="sig-name descname">policy_data</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.service_account.IAMPolicy.policy_data" title="Permalink to this definition">¶</a></dt>
<dd><p>The policy data generated by
a <code class="docutils literal notranslate"><span class="pre">organizations.getIAMPolicy</span></code> data source.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.service_account.IAMPolicy.service_account_id">
<code class="sig-name descname">service_account_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.service_account.IAMPolicy.service_account_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The fully-qualified name of the service account to apply policy to.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.service_account.IAMPolicy.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">etag=None</em>, <em class="sig-param">policy_data=None</em>, <em class="sig-param">service_account_id=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.service_account.IAMPolicy.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing IAMPolicy resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>etag</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – (Computed) The etag of the service account IAM policy.</p></li>
<li><p><strong>policy_data</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The policy data generated by
a <code class="docutils literal notranslate"><span class="pre">organizations.getIAMPolicy</span></code> data source.</p></li>
<li><p><strong>service_account_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The fully-qualified name of the service account to apply policy to.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/service_account_iam_policy.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/service_account_iam_policy.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.service_account.IAMPolicy.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.service_account.IAMPolicy.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.service_account.IAMPolicy.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.service_account.IAMPolicy.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.service_account.Key">
<em class="property">class </em><code class="sig-prename descclassname">pulumi_gcp.service_account.</code><code class="sig-name descname">Key</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">key_algorithm=None</em>, <em class="sig-param">private_key_type=None</em>, <em class="sig-param">public_key_type=None</em>, <em class="sig-param">service_account_id=None</em>, <em class="sig-param">__props__=None</em>, <em class="sig-param">__name__=None</em>, <em class="sig-param">__opts__=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.service_account.Key" title="Permalink to this definition">¶</a></dt>
<dd><p>Creates and manages service account key-pairs, which allow the user to establish identity of a service account outside of GCP. For more information, see <a class="reference external" href="https://cloud.google.com/iam/docs/creating-managing-service-account-keys">the official documentation</a> and <a class="reference external" href="https://cloud.google.com/iam/reference/rest/v1/projects.serviceAccounts.keys">API</a>.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The name of the resource.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>key_algorithm</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The algorithm used to generate the key. KEY_ALG_RSA_2048 is the default algorithm.
Valid values are listed at
<a class="reference external" href="https://cloud.google.com/iam/reference/rest/v1/projects.serviceAccounts.keys#ServiceAccountKeyAlgorithm">ServiceAccountPrivateKeyType</a>
(only used on create)</p></li>
<li><p><strong>private_key_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The output format of the private key. TYPE_GOOGLE_CREDENTIALS_FILE is the default output format.</p></li>
<li><p><strong>public_key_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The output format of the public key requested. X509_PEM is the default output format.</p></li>
<li><p><strong>service_account_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Service account id of the Key Pair. This can be a string in the format
<code class="docutils literal notranslate"><span class="pre">{ACCOUNT}</span></code> or <code class="docutils literal notranslate"><span class="pre">projects/{PROJECT_ID}/serviceAccounts/{ACCOUNT}</span></code>, where <code class="docutils literal notranslate"><span class="pre">{ACCOUNT}</span></code> is the email address or
unique id of the service account. If the <code class="docutils literal notranslate"><span class="pre">{ACCOUNT}</span></code> syntax is used, the project will be inferred from the account.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/service_account_key.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/service_account_key.html.markdown</a>.</p>
</div></blockquote>
<dl class="attribute">
<dt id="pulumi_gcp.service_account.Key.key_algorithm">
<code class="sig-name descname">key_algorithm</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.service_account.Key.key_algorithm" title="Permalink to this definition">¶</a></dt>
<dd><p>The algorithm used to generate the key. KEY_ALG_RSA_2048 is the default algorithm.
Valid values are listed at
<a class="reference external" href="https://cloud.google.com/iam/reference/rest/v1/projects.serviceAccounts.keys#ServiceAccountKeyAlgorithm">ServiceAccountPrivateKeyType</a>
(only used on create)</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.service_account.Key.name">
<code class="sig-name descname">name</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.service_account.Key.name" title="Permalink to this definition">¶</a></dt>
<dd><p>The name used for this key pair</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.service_account.Key.private_key">
<code class="sig-name descname">private_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.service_account.Key.private_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The private key in JSON format, base64 encoded. This is what you normally get as a file when creating
service account keys through the CLI or web console. This is only populated when creating a new key.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.service_account.Key.private_key_type">
<code class="sig-name descname">private_key_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.service_account.Key.private_key_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The output format of the private key. TYPE_GOOGLE_CREDENTIALS_FILE is the default output format.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.service_account.Key.public_key">
<code class="sig-name descname">public_key</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.service_account.Key.public_key" title="Permalink to this definition">¶</a></dt>
<dd><p>The public key, base64 encoded</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.service_account.Key.public_key_type">
<code class="sig-name descname">public_key_type</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.service_account.Key.public_key_type" title="Permalink to this definition">¶</a></dt>
<dd><p>The output format of the public key requested. X509_PEM is the default output format.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.service_account.Key.service_account_id">
<code class="sig-name descname">service_account_id</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.service_account.Key.service_account_id" title="Permalink to this definition">¶</a></dt>
<dd><p>The Service account id of the Key Pair. This can be a string in the format
<code class="docutils literal notranslate"><span class="pre">{ACCOUNT}</span></code> or <code class="docutils literal notranslate"><span class="pre">projects/{PROJECT_ID}/serviceAccounts/{ACCOUNT}</span></code>, where <code class="docutils literal notranslate"><span class="pre">{ACCOUNT}</span></code> is the email address or
unique id of the service account. If the <code class="docutils literal notranslate"><span class="pre">{ACCOUNT}</span></code> syntax is used, the project will be inferred from the account.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.service_account.Key.valid_after">
<code class="sig-name descname">valid_after</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.service_account.Key.valid_after" title="Permalink to this definition">¶</a></dt>
<dd><p>The key can be used after this timestamp. A timestamp in RFC3339 UTC “Zulu” format, accurate to nanoseconds. Example: “2014-10-02T15:01:23.045123456Z”.</p>
</dd></dl>

<dl class="attribute">
<dt id="pulumi_gcp.service_account.Key.valid_before">
<code class="sig-name descname">valid_before</code><em class="property"> = None</em><a class="headerlink" href="#pulumi_gcp.service_account.Key.valid_before" title="Permalink to this definition">¶</a></dt>
<dd><p>The key can be used before this timestamp.
A timestamp in RFC3339 UTC “Zulu” format, accurate to nanoseconds. Example: “2014-10-02T15:01:23.045123456Z”.</p>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.service_account.Key.get">
<em class="property">static </em><code class="sig-name descname">get</code><span class="sig-paren">(</span><em class="sig-param">resource_name</em>, <em class="sig-param">id</em>, <em class="sig-param">opts=None</em>, <em class="sig-param">key_algorithm=None</em>, <em class="sig-param">name=None</em>, <em class="sig-param">private_key=None</em>, <em class="sig-param">private_key_type=None</em>, <em class="sig-param">public_key=None</em>, <em class="sig-param">public_key_type=None</em>, <em class="sig-param">service_account_id=None</em>, <em class="sig-param">valid_after=None</em>, <em class="sig-param">valid_before=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.service_account.Key.get" title="Permalink to this definition">¶</a></dt>
<dd><p>Get an existing Key resource’s state with the given name, id, and optional extra
properties used to qualify the lookup.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>resource_name</strong> (<em>str</em>) – The unique name of the resulting resource.</p></li>
<li><p><strong>id</strong> (<em>str</em>) – The unique provider ID of the resource to lookup.</p></li>
<li><p><strong>opts</strong> (<a class="reference internal" href="../../pulumi/#pulumi.ResourceOptions" title="pulumi.ResourceOptions"><em>pulumi.ResourceOptions</em></a>) – Options for the resource.</p></li>
<li><p><strong>key_algorithm</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – <p>The algorithm used to generate the key. KEY_ALG_RSA_2048 is the default algorithm.
Valid values are listed at
<a class="reference external" href="https://cloud.google.com/iam/reference/rest/v1/projects.serviceAccounts.keys#ServiceAccountKeyAlgorithm">ServiceAccountPrivateKeyType</a>
(only used on create)</p>
</p></li>
<li><p><strong>name</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The name used for this key pair</p></li>
<li><p><strong>private_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The private key in JSON format, base64 encoded. This is what you normally get as a file when creating
service account keys through the CLI or web console. This is only populated when creating a new key.</p></li>
<li><p><strong>private_key_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The output format of the private key. TYPE_GOOGLE_CREDENTIALS_FILE is the default output format.</p></li>
<li><p><strong>public_key</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The public key, base64 encoded</p></li>
<li><p><strong>public_key_type</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The output format of the public key requested. X509_PEM is the default output format.</p></li>
<li><p><strong>service_account_id</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The Service account id of the Key Pair. This can be a string in the format
<code class="docutils literal notranslate"><span class="pre">{ACCOUNT}</span></code> or <code class="docutils literal notranslate"><span class="pre">projects/{PROJECT_ID}/serviceAccounts/{ACCOUNT}</span></code>, where <code class="docutils literal notranslate"><span class="pre">{ACCOUNT}</span></code> is the email address or
unique id of the service account. If the <code class="docutils literal notranslate"><span class="pre">{ACCOUNT}</span></code> syntax is used, the project will be inferred from the account.</p></li>
<li><p><strong>valid_after</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The key can be used after this timestamp. A timestamp in RFC3339 UTC “Zulu” format, accurate to nanoseconds. Example: “2014-10-02T15:01:23.045123456Z”.</p></li>
<li><p><strong>valid_before</strong> (<em>pulumi.Input</em><em>[</em><em>str</em><em>]</em>) – The key can be used before this timestamp.
A timestamp in RFC3339 UTC “Zulu” format, accurate to nanoseconds. Example: “2014-10-02T15:01:23.045123456Z”.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/service_account_key.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/service_account_key.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="method">
<dt id="pulumi_gcp.service_account.Key.translate_output_property">
<code class="sig-name descname">translate_output_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.service_account.Key.translate_output_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.service_account.Key.translate_input_property">
<code class="sig-name descname">translate_input_property</code><span class="sig-paren">(</span><em class="sig-param">prop</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.service_account.Key.translate_input_property" title="Permalink to this definition">¶</a></dt>
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
<dt id="pulumi_gcp.service_account.get_account">
<code class="sig-prename descclassname">pulumi_gcp.service_account.</code><code class="sig-name descname">get_account</code><span class="sig-paren">(</span><em class="sig-param">account_id=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.service_account.get_account" title="Permalink to this definition">¶</a></dt>
<dd><p>Get the service account from a project. For more information see
the official <a class="reference external" href="https://cloud.google.com/compute/docs/access/service-accounts">API</a> documentation.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>account_id</strong> (<em>str</em>) – The Service account id.  (This is the part of the service account’s email field that comes before the &#64; symbol.)</p></li>
<li><p><strong>project</strong> (<em>str</em>) – The ID of the project that the service account is present in.
Defaults to the provider project configuration.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/d/service_account.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/d/service_account.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="function">
<dt id="pulumi_gcp.service_account.get_account_access_token">
<code class="sig-prename descclassname">pulumi_gcp.service_account.</code><code class="sig-name descname">get_account_access_token</code><span class="sig-paren">(</span><em class="sig-param">delegates=None</em>, <em class="sig-param">lifetime=None</em>, <em class="sig-param">scopes=None</em>, <em class="sig-param">target_service_account=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.service_account.get_account_access_token" title="Permalink to this definition">¶</a></dt>
<dd><p>This data source provides a google <code class="docutils literal notranslate"><span class="pre">oauth2</span></code> <code class="docutils literal notranslate"><span class="pre">access_token</span></code> for a different service account than the one initially running the script.</p>
<p>For more information see
<a class="reference external" href="https://cloud.google.com/iam/docs/creating-short-lived-service-account-credentials">the official documentation</a> as well as <a class="reference external" href="https://cloud.google.com/iam/credentials/reference/rest/v1/projects.serviceAccounts/generateAccessToken">iamcredentials.generateAccessToken()</a></p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>delegates</strong> (<em>list</em>) – Delegate chain of approvals needed to perform full impersonation. Specify the fully qualified service account name.  (e.g. <code class="docutils literal notranslate"><span class="pre">[&quot;projects/-/serviceAccounts/delegate-svc-account&#64;project-id.iam.gserviceaccount.com&quot;]</span></code>)</p></li>
<li><p><strong>lifetime</strong> (<em>str</em>) – Lifetime of the impersonated token (defaults to its max: <code class="docutils literal notranslate"><span class="pre">3600s</span></code>).</p></li>
<li><p><strong>scopes</strong> (<em>list</em>) – The scopes the new credential should have (e.g. <code class="docutils literal notranslate"><span class="pre">[&quot;storage-ro&quot;,</span> <span class="pre">&quot;cloud-platform&quot;]</span></code>)</p></li>
<li><p><strong>target_service_account</strong> (<em>str</em>) – The service account <em>to</em> impersonate (e.g. <code class="docutils literal notranslate"><span class="pre">service_B&#64;your-project-id.iam.gserviceaccount.com</span></code>)</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/d/service_account_access_token.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/d/service_account_access_token.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

<dl class="function">
<dt id="pulumi_gcp.service_account.get_account_key">
<code class="sig-prename descclassname">pulumi_gcp.service_account.</code><code class="sig-name descname">get_account_key</code><span class="sig-paren">(</span><em class="sig-param">name=None</em>, <em class="sig-param">project=None</em>, <em class="sig-param">public_key_type=None</em>, <em class="sig-param">opts=None</em><span class="sig-paren">)</span><a class="headerlink" href="#pulumi_gcp.service_account.get_account_key" title="Permalink to this definition">¶</a></dt>
<dd><p>Get service account public key. For more information, see <a class="reference external" href="https://cloud.google.com/iam/docs/creating-managing-service-account-keys">the official documentation</a> and <a class="reference external" href="https://cloud.google.com/iam/reference/rest/v1/projects.serviceAccounts.keys/get">API</a>.</p>
<dl class="field-list simple">
<dt class="field-odd">Parameters</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>name</strong> (<em>str</em>) – The name of the service account key. This must have format
<code class="docutils literal notranslate"><span class="pre">projects/{PROJECT_ID}/serviceAccounts/{ACCOUNT}/keys/{KEYID}</span></code>, where <code class="docutils literal notranslate"><span class="pre">{ACCOUNT}</span></code>
is the email address or unique id of the service account.</p></li>
<li><p><strong>project</strong> (<em>str</em>) – The ID of the project that the service account will be created in.
Defaults to the provider project configuration.</p></li>
<li><p><strong>public_key_type</strong> (<em>str</em>) – The output format of the public key requested. X509_PEM is the default output format.</p></li>
</ul>
</dd>
</dl>
<blockquote>
<div><p>This content is derived from <a class="reference external" href="https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/d/service_account_key.html.markdown">https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/d/service_account_key.html.markdown</a>.</p>
</div></blockquote>
</dd></dl>

</div>
